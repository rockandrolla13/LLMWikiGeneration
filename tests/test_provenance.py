"""Tests for the numeric provenance check.

The regression cases are the two fabrications this check was built after: an
invented beta of "-1.51" attributed to Daniel & Moskowitz (2016), and invented
factor counts of "8.9" and "7.7" attributed to Li, Chen & Linton (2023). The
second is the important shape -- invented figures sitting in a sentence whose
other numbers are real.
"""

import pytest

from llm_wiki import Wiki, wiki_init
from llm_wiki.frontmatter import write_page
from llm_wiki.manifest import (
    ManifestEntry,
    OperationInputs,
    OperationStatus,
    OperationType,
)
from llm_wiki.provenance import (
    ProvenanceResult,
    Unverifiable,
    check_page_provenance,
    extract_body_source_path,
    extract_numeric_claims,
    normalize_document,
    resolve_source_path,
    summarize_coverage,
)


@pytest.fixture
def paper(tmp_path):
    """A source document with a handful of real figures."""
    doc = tmp_path / "paper.md"
    doc.write_text(
        "# A Paper\n\n"
        "The strategy returns 0.62% per month with a t-statistic of 3.14.\n"
        "At the 1-minute frequency the mean total is 13.0, of which 4.2 are noise.\n"
        "Sample: 1,234.5 million observations.\n",
        encoding="utf-8",
    )
    return doc


class TestExtractNumericClaims:
    def test_finds_decimals(self):
        assert extract_numeric_claims("returns 0.62% with t = 3.14") == {"0.62", "3.14"}

    def test_ignores_whole_numbers(self):
        """Years and counts collide with everything; only decimals are evidence."""
        assert extract_numeric_claims("in 2019 across 500 stocks, Section 4") == set()

    def test_ignores_wikilinks(self):
        """Slugs and years inside links are navigation, not claims."""
        assert extract_numeric_claims("see [[sources/foo-2023-bar|Foo (2023)]]") == set()

    def test_ignores_code(self):
        assert extract_numeric_claims("`alpha=0.05`") == set()
        assert extract_numeric_claims("```\nx = 1.96\n```") == set()

    def test_ignores_arxiv_identifiers(self):
        """arXiv IDs and DOIs look like decimals but name a thing."""
        assert extract_numeric_claims("arXiv:1910.07325v1") == set()
        assert extract_numeric_claims("(arXiv preprint 2601.02998)") == set()

    def test_keeps_a_real_figure_beside_an_identifier(self):
        claims = extract_numeric_claims("arXiv:1910.07325 reports a Sharpe of 1.42")
        assert claims == {"1.42"}


class TestNormalizeDocument:
    def test_strips_pdf_extraction_artifacts(self):
        """PDF conversion breaks numbers across whitespace and commas."""
        assert "1234.5" in normalize_document("1, 234. 5")
        assert "0.62" in normalize_document("0.\n62")


class TestCheckPageProvenance:
    def test_supported_figures_pass(self, tmp_path, paper):
        r = check_page_provenance(
            tmp_path, "sources/x", {"source_path": str(paper)},
            "The strategy returns 0.62% per month, t = 3.14.",
        )
        assert r.passed
        assert r.checked == 2

    def test_invented_figure_is_caught(self, tmp_path, paper):
        r = check_page_provenance(
            tmp_path, "sources/x", {"source_path": str(paper)},
            "The strategy returns 0.99% per month.",
        )
        assert not r.passed
        assert r.unsupported == ["0.99"]

    def test_invented_figure_beside_real_ones_is_caught(self, tmp_path, paper):
        """The dangerous shape: real numbers lending credibility to a fake one."""
        r = check_page_provenance(
            tmp_path, "sources/x", {"source_path": str(paper)},
            "Mean total is 13.0, of which 8.9 are efficient-price and 4.2 are noise.",
        )
        assert not r.passed
        assert r.unsupported == ["8.9"]

    def test_missing_source_path_is_unverifiable_not_passing(self, tmp_path):
        """An unchecked page must not look like a checked one."""
        r = check_page_provenance(tmp_path, "sources/x", {}, "A claim of 9.99.")
        assert not r.verifiable
        assert not r.passed
        assert "no source_path" in r.note

    def test_pdf_source_is_unverifiable(self, tmp_path):
        """Comparing prose against PDF bytes flags every real figure as invented."""
        pdf = tmp_path / "paper.pdf"
        pdf.write_bytes(b"%PDF-1.4 binary junk")
        r = check_page_provenance(
            tmp_path, "sources/x", {"source_path": str(pdf)}, "A figure of 0.62."
        )
        assert not r.verifiable
        assert "not text" in r.note

    def test_absent_source_is_unverifiable(self, tmp_path):
        r = check_page_provenance(
            tmp_path, "sources/x", {"source_path": "nowhere/absent.md"}, "0.62"
        )
        assert not r.verifiable
        assert "not found" in r.note


class TestResolveSourcePath:
    def test_finds_relative_to_wiki_root(self, tmp_path):
        (tmp_path / "raw").mkdir()
        doc = tmp_path / "raw" / "d.md"
        doc.write_text("x", encoding="utf-8")
        assert resolve_source_path(tmp_path, "raw/d.md") == doc

    def test_finds_relative_to_repo_root(self, tmp_path):
        repo = tmp_path
        wiki = repo / "wiki"
        (repo / "markdown_output").mkdir()
        wiki.mkdir()
        doc = repo / "markdown_output" / "d.md"
        doc.write_text("x", encoding="utf-8")
        assert resolve_source_path(wiki, "markdown_output/d.md") == doc

    def test_returns_none_when_absent(self, tmp_path):
        assert resolve_source_path(tmp_path, "no/such.md") is None


class TestResultSemantics:
    def test_unverifiable_is_not_passed(self):
        """Guards the distinction the whole check rests on."""
        r = ProvenanceResult("p", None, note="no source_path recorded")
        assert not r.verifiable and not r.passed

    def test_clean_is_passed(self):
        assert ProvenanceResult("p", "d.md", checked=3).passed


class TestBodySourcePath:
    """Most pages in this corpus state their origin in prose, not frontmatter."""

    def test_reads_the_bold_backticked_form(self):
        body = "## Provenance\n\n**Markdown source:** `markdown_output/a-2025-b.md`\n"
        assert extract_body_source_path(body) == "markdown_output/a-2025-b.md"

    def test_tolerates_formatting_variation(self):
        for line in [
            "Markdown source: markdown_output/d.md",
            "**Markdown source**: `markdown_output/d.md`",
            "   **Markdown source:**   `markdown_output/d.md`   ",
            "**markdown SOURCE:** markdown_output/d.md",
        ]:
            assert extract_body_source_path(line) == "markdown_output/d.md", line

    def test_keeps_spaces_inside_a_backticked_path(self):
        body = "**Markdown source:** `markdown_output/A pairs trade.md`"
        assert extract_body_source_path(body) == "markdown_output/A pairs trade.md"

    def test_ignores_prose_that_merely_mentions_a_source(self):
        assert extract_body_source_path("The markdown source was lost.") is None
        assert extract_body_source_path("Converted from a PDF.") is None

    def test_returns_none_when_absent(self):
        assert extract_body_source_path("# A page\n\nNo provenance here.\n") is None


class TestBodySourceFallback:
    """The fallback must find pages the frontmatter-only check could not see."""

    def test_body_line_makes_a_page_verifiable(self, tmp_path, paper):
        r = check_page_provenance(
            tmp_path,
            "sources/x",
            {},
            f"Returns of 0.62%.\n\n**Markdown source:** `{paper}`\n",
        )
        assert r.passed
        assert r.checked == 1

    def test_body_line_catches_an_invented_figure(self, tmp_path, paper):
        r = check_page_provenance(
            tmp_path,
            "sources/x",
            {},
            f"Returns of 0.99%.\n\n**Markdown source:** `{paper}`\n",
        )
        assert not r.passed
        assert r.unsupported == ["0.99"]

    def test_frontmatter_wins_over_the_body_line(self, tmp_path, paper):
        """Frontmatter is the declared field; prose is only the fallback."""
        r = check_page_provenance(
            tmp_path,
            "sources/x",
            {"source_path": str(paper)},
            "Returns of 0.62%.\n\n**Markdown source:** `nowhere/absent.md`\n",
        )
        assert r.passed
        assert r.source_path == str(paper)

    def test_body_path_resolves_relative_to_the_wiki_root(self, tmp_path):
        (tmp_path / "markdown_output").mkdir()
        (tmp_path / "markdown_output" / "d.md").write_text(
            "A Sharpe of 1.42.", encoding="utf-8"
        )
        r = check_page_provenance(
            tmp_path,
            "sources/x",
            {},
            "Sharpe 1.42.\n\n**Markdown source:** `markdown_output/d.md`\n",
        )
        assert r.passed


class TestUnverifiableReasons:
    """Three states, not one bucket. Only one of them is actionable."""

    def test_no_source_anywhere(self, tmp_path):
        r = check_page_provenance(tmp_path, "sources/x", {}, "A claim of 9.99.")
        assert r.reason is Unverifiable.NO_SOURCE
        assert not r.verifiable

    def test_source_recorded_but_file_missing(self, tmp_path):
        """The actionable state: the page names a document, disk does not have it."""
        r = check_page_provenance(
            tmp_path,
            "sources/x",
            {},
            "A claim of 9.99.\n\n**Markdown source:** `markdown_output/gone.md`\n",
        )
        assert r.reason is Unverifiable.SOURCE_MISSING
        assert r.source_path == "markdown_output/gone.md"
        assert not r.verifiable

    def test_frontmatter_source_missing_uses_the_same_reason(self, tmp_path):
        r = check_page_provenance(
            tmp_path, "sources/x", {"source_path": "nowhere/absent.md"}, "0.62"
        )
        assert r.reason is Unverifiable.SOURCE_MISSING

    def test_pdf_source_is_its_own_reason(self, tmp_path):
        pdf = tmp_path / "paper.pdf"
        pdf.write_bytes(b"%PDF-1.4 binary junk")
        r = check_page_provenance(
            tmp_path, "sources/x", {"source_path": str(pdf)}, "A figure of 0.62."
        )
        assert r.reason is Unverifiable.NOT_TEXT

    def test_verified_page_has_no_reason(self, tmp_path, paper):
        r = check_page_provenance(
            tmp_path, "sources/x", {"source_path": str(paper)}, "Returns 0.62%."
        )
        assert r.reason is None


class TestSummarizeCoverage:
    def test_counts_each_state_separately(self):
        coverage = summarize_coverage([
            ProvenanceResult("a", "d.md", checked=3),
            ProvenanceResult("b", "e.md", checked=1),
            ProvenanceResult("c", "gone.md", note="x", reason=Unverifiable.SOURCE_MISSING),
            ProvenanceResult("d", None, note="x", reason=Unverifiable.NO_SOURCE),
            ProvenanceResult("e", "p.pdf", note="x", reason=Unverifiable.NOT_TEXT),
        ])
        assert coverage.verified_pages == 2
        assert coverage.verified_figures == 4
        assert coverage.source_missing == 1
        assert coverage.no_source == 1
        assert coverage.not_text == 1

    def test_a_page_with_unsupported_figures_still_counts_as_covered(self):
        """Coverage measures what was read, not what passed."""
        coverage = summarize_coverage(
            [ProvenanceResult("a", "d.md", checked=3, unsupported=["9.99"])]
        )
        assert coverage.verified_pages == 1


# --- End-to-end through the verification report ---------------------------


def make_wiki(tmp_path):
    root = tmp_path / "vault"
    wiki_init(root, name="Coverage Wiki")
    return Wiki(root)


def add_source_page(wiki, slug: str, figure: str, doc_name: str) -> None:
    """Write a source page whose figure lives in `markdown_output/<doc_name>`."""
    docs = wiki.root / "markdown_output"
    docs.mkdir(exist_ok=True)
    (docs / doc_name).write_text(f"The value is {figure}.\n", encoding="utf-8")
    write_page(
        wiki.wiki_dir / "sources" / f"{slug}.md",
        {
            "title": slug,
            "page_id": f"sources/{slug}",
            "page_type": "source",
            "revision_id": 1,
        },
        f"A figure of {figure}.\n\n**Markdown source:** `markdown_output/{doc_name}`\n",
    )


def append_op(wiki, op_type: OperationType) -> None:
    entry = ManifestEntry.create(op_type, inputs=OperationInputs())
    entry.status = OperationStatus.COMPLETED
    wiki.manifest.append(entry)


class TestVerifyNumericProvenanceCheck:
    """End-to-end through the VerificationResult the report shows."""

    def test_message_separates_the_three_states(self, tmp_path):
        from llm_wiki.verify import verify_numeric_provenance

        wiki = make_wiki(tmp_path)
        add_source_page(wiki, "good", "0.62", "good.md")
        write_page(
            wiki.wiki_dir / "sources" / "orphan.md",
            {
                "title": "orphan",
                "page_id": "sources/orphan",
                "page_type": "source",
                "revision_id": 1,
            },
            "A figure of 1.23.\n\n**Markdown source:** `markdown_output/gone.md`\n",
        )
        write_page(
            wiki.wiki_dir / "sources" / "silent.md",
            {
                "title": "silent",
                "page_id": "sources/silent",
                "page_type": "source",
                "revision_id": 1,
            },
            "A figure of 4.56 with no provenance line at all.\n",
        )

        result = verify_numeric_provenance(wiki, record_baseline=False)

        assert result.passed
        assert "1 record a source not found on disk" in result.message
        assert "1 record no source at all" in result.message

    def test_a_silent_coverage_drop_fails_the_check(self, tmp_path):
        from llm_wiki.verify import verify_numeric_provenance

        wiki = make_wiki(tmp_path)
        add_source_page(wiki, "a", "0.62", "a.md")
        add_source_page(wiki, "b", "3.14", "b.md")

        assert verify_numeric_provenance(wiki).passed

        (wiki.root / "markdown_output" / "b.md").unlink()
        result = verify_numeric_provenance(wiki)

        assert not result.passed
        assert "1 page" in result.message

    def test_an_ingest_lets_coverage_fall_without_failing(self, tmp_path):
        from llm_wiki.verify import verify_numeric_provenance

        wiki = make_wiki(tmp_path)
        add_source_page(wiki, "a", "0.62", "a.md")
        add_source_page(wiki, "b", "3.14", "b.md")
        assert verify_numeric_provenance(wiki).passed

        (wiki.wiki_dir / "sources" / "b.md").unlink()
        append_op(wiki, OperationType.DELETE)

        assert verify_numeric_provenance(wiki).passed
