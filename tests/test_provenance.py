"""Tests for the numeric provenance check.

The regression cases are the two fabrications this check was built after: an
invented beta of "-1.51" attributed to Daniel & Moskowitz (2016), and invented
factor counts of "8.9" and "7.7" attributed to Li, Chen & Linton (2023). The
second is the important shape -- invented figures sitting in a sentence whose
other numbers are real.
"""

import pytest

from llm_wiki.provenance import (
    ProvenanceResult,
    check_page_provenance,
    extract_numeric_claims,
    normalize_document,
    resolve_source_path,
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
