"""Tests for the coverage guard and the checks that rely on it.

Three checks in this wiki have failed the same way: absent data read as PASS.
The numeric provenance check classified unreadable sources as "unverifiable"
and still reported all-clear while 153 pages dropped out. The revision-hash
check skipped every page lacking a `revision_hash` field -- all 1,595 of them --
and reported "All revision hashes match content".

The guard here is the shared answer: a check must say how much it actually
covered, and a fall in that number with nothing in the ledger to explain it is
a failure rather than a quieter success.
"""

import pytest

from llm_wiki import Wiki, wiki_init
from llm_wiki.coverage import check_regression, read_baseline, record_baseline
from llm_wiki.frontmatter import compute_content_hash, parse_page, write_page
from llm_wiki.manifest import (
    ManifestEntry,
    OperationInputs,
    OperationStatus,
    OperationType,
)
from llm_wiki.verify import verify_revision_hashes


@pytest.fixture
def wiki(tmp_path):
    root = tmp_path / "vault"
    wiki_init(root, name="Coverage Wiki")
    return Wiki(root)


def append_op(wiki, op_type: OperationType) -> None:
    entry = ManifestEntry.create(op_type, inputs=OperationInputs())
    entry.status = OperationStatus.COMPLETED
    wiki.manifest.append(entry)


def write_source(wiki, slug: str, body: str, hashed: bool = True) -> None:
    """Write a source page, with or without a revision_hash field.

    The hash has to be taken from the body as it reads back off disk, which is
    what a backfill would do: serialising the frontmatter can renormalise the
    content, so hashing the string passed in here would mismatch every time.
    """
    path = wiki.wiki_dir / "sources" / f"{slug}.md"
    metadata = {
        "title": slug,
        "page_id": f"sources/{slug}",
        "page_type": "source",
        "revision_id": 1,
    }
    write_page(path, metadata, body)
    if hashed:
        stored, content = parse_page(path)
        stored["revision_hash"] = compute_content_hash(content)
        write_page(path, stored, content)


class TestBaselineRecording:
    def test_first_check_arms_the_baseline(self, wiki):
        assert check_regression(wiki, "demo", covered=4) is None
        assert read_baseline(wiki, "demo").covered == 4

    def test_read_only_mode_records_nothing(self, wiki):
        assert check_regression(wiki, "demo", covered=4, record=False) is None
        assert read_baseline(wiki, "demo") is None

    def test_baseline_ratchets_up_without_ceremony(self, wiki):
        """Growth is the normal case and must never need a manual reset."""
        check_regression(wiki, "demo", covered=1)
        assert check_regression(wiki, "demo", covered=2) is None
        assert read_baseline(wiki, "demo").covered == 2

    def test_steady_state_appends_nothing(self, wiki):
        """Verifying repeatedly must not pad the ledger."""
        check_regression(wiki, "demo", covered=3)
        before = len(wiki.manifest.read_all())
        check_regression(wiki, "demo", covered=3)
        check_regression(wiki, "demo", covered=3)
        assert len(wiki.manifest.read_all()) == before

    def test_checks_keep_separate_baselines(self, wiki):
        """One check's coverage must not stand in for another's."""
        record_baseline(wiki, "alpha", covered=10)
        record_baseline(wiki, "beta", covered=2)
        assert read_baseline(wiki, "alpha").covered == 10
        assert read_baseline(wiki, "beta").covered == 2
        assert check_regression(wiki, "beta", covered=2) is None

    def test_detail_survives_the_round_trip(self, wiki):
        record_baseline(wiki, "demo", covered=3, detail={"figures": 12})
        assert read_baseline(wiki, "demo").detail == {"figures": 12}


class TestRegressionDetection:
    def test_silent_drop_fails(self, wiki):
        check_regression(wiki, "demo", covered=5)
        message = check_regression(wiki, "demo", covered=2)
        assert message is not None
        assert "5" in message and "2" in message and "3" in message

    def test_drop_after_an_ingest_is_legitimate(self, wiki):
        """A guard that cries wolf on every ingest is worse than no guard."""
        check_regression(wiki, "demo", covered=5)
        append_op(wiki, OperationType.INGEST)
        assert check_regression(wiki, "demo", covered=2) is None
        assert read_baseline(wiki, "demo").covered == 2

    def test_drop_after_a_delete_is_legitimate(self, wiki):
        check_regression(wiki, "demo", covered=5)
        append_op(wiki, OperationType.DELETE)
        assert check_regression(wiki, "demo", covered=1) is None

    def test_a_rebuild_does_not_excuse_a_drop(self, wiki):
        """Rebuild writes derived artifacts; it cannot remove a source page."""
        check_regression(wiki, "demo", covered=5)
        append_op(wiki, OperationType.REBUILD)
        assert check_regression(wiki, "demo", covered=1) is not None

    def test_failure_is_sticky(self, wiki):
        """A guard you can silence by running it twice is not a guard."""
        check_regression(wiki, "demo", covered=5)
        assert check_regression(wiki, "demo", covered=1) is not None
        assert check_regression(wiki, "demo", covered=1) is not None
        assert read_baseline(wiki, "demo").covered == 5

    def test_recovery_clears_the_failure(self, wiki):
        check_regression(wiki, "demo", covered=5)
        check_regression(wiki, "demo", covered=1)
        assert check_regression(wiki, "demo", covered=5) is None

    def test_message_names_a_second_unit_when_asked(self, wiki):
        check_regression(
            wiki, "demo", covered=5, detail={"figures": 20},
            detail_unit=("figures", "figures"),
        )
        message = check_regression(
            wiki, "demo", covered=2, detail={"figures": 6},
            detail_unit=("figures", "figures"),
        )
        assert "14 figures" in message

    def test_singular_reads_correctly(self, wiki):
        check_regression(wiki, "demo", covered=2, unit="pages")
        message = check_regression(wiki, "demo", covered=1, unit="pages")
        assert "1 page dropped out" in message


class TestVerifyRevisionHashes:
    """The check reported all-clear while verifying nothing at all."""

    def test_zero_coverage_does_not_claim_success(self, wiki):
        write_source(wiki, "a", "Body one.\n", hashed=False)
        write_source(wiki, "b", "Body two.\n", hashed=False)

        result = verify_revision_hashes(wiki, record_baseline=False)

        assert "all revision hashes match" not in result.message.lower()
        assert "0 of" in result.message
        assert "verifies nothing" in result.message

    def test_zero_coverage_still_passes(self, wiki):
        """No stored hash is a gap to backfill, not a mismatch to fail on."""
        write_source(wiki, "a", "Body one.\n", hashed=False)
        assert verify_revision_hashes(wiki, record_baseline=False).passed

    def test_coverage_is_reported_when_partial(self, wiki):
        write_source(wiki, "a", "Body one.\n")
        write_source(wiki, "b", "Body two.\n", hashed=False)

        message = verify_revision_hashes(wiki, record_baseline=False).message

        assert "1 of" in message

    def test_a_tampered_body_fails(self, wiki):
        """The check's actual job, which zero coverage had made untestable."""
        write_source(wiki, "a", "Body one.\n")
        path = wiki.wiki_dir / "sources" / "a.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("Body one.", "Body edited."),
            encoding="utf-8",
        )

        result = verify_revision_hashes(wiki, record_baseline=False)

        assert not result.passed
        assert "mismatch" in result.message

    def test_losing_hashes_fails_as_a_regression(self, wiki):
        write_source(wiki, "a", "Body one.\n")
        write_source(wiki, "b", "Body two.\n")
        assert verify_revision_hashes(wiki).passed

        write_source(wiki, "b", "Body two.\n", hashed=False)
        result = verify_revision_hashes(wiki)

        assert not result.passed
        assert "1 page" in result.message

    def test_gaining_hashes_ratchets_the_baseline(self, wiki):
        """A backfill must not need the guard reset by hand."""
        write_source(wiki, "a", "Body one.\n", hashed=False)
        verify_revision_hashes(wiki)

        write_source(wiki, "a", "Body one.\n")
        assert verify_revision_hashes(wiki).passed
        assert read_baseline(wiki, "revision_hashes").covered == 1
