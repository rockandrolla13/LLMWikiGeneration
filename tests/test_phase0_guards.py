"""Tests for the Phase 0 safety fixes.

Three behaviours that had no coverage and cost real data or real trust:

1. rebuild must not overwrite hand-curated derived artifacts
2. the manifest reader must tolerate legacy hand-written entries
3. the wikilink check must resolve page_id links, not only titles
"""

import pytest

from llm_wiki import Wiki, wiki_init, wiki_rebuild
from llm_wiki.derived import rebuild_derived
from llm_wiki.io.page_io import GENERATED_MARKER, is_generated
from llm_wiki.manifest import Manifest, OperationType, OperationStatus, Actor
from llm_wiki.verify import (
    verify_wikilinks,
    resolve_link_targets,
    normalize_link_target,
)


CURATED_MIND_MAP = """# My Wiki - Knowledge Map

[1] **Overview** - Hand-written synthesis that the generator cannot reproduce.
"""


@pytest.fixture
def wiki(tmp_path):
    wiki_init(tmp_path, name="Test Wiki")
    return Wiki(tmp_path)


def write_page_file(wiki, page_type, slug, body, title=None, page_id=None):
    """Write a minimal valid wiki page and return its path."""
    path = wiki.wiki_dir / page_type / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        f"title: {title or slug}\n"
        f"page_id: {page_id or f'{page_type}/{slug}'}\n"
        f"page_type: {page_type.rstrip('s')}\n"
        "revision_id: 1\n"
        "---\n\n"
        f"{body}\n",
        encoding="utf-8",
    )
    return path


class TestRebuildGuard:
    """rebuild_derived must refuse to destroy hand-curated artifacts."""

    def test_curated_mind_map_is_not_overwritten(self, wiki, tmp_path):
        mind_map = tmp_path / "MIND_MAP.md"
        mind_map.write_text(CURATED_MIND_MAP, encoding="utf-8")

        result = rebuild_derived(wiki)

        assert mind_map.read_text() == CURATED_MIND_MAP
        assert "MIND_MAP.md" not in result["rebuilt"]
        assert any("MIND_MAP.md" in s for s in result["skipped"])

    def test_curated_index_is_not_overwritten(self, wiki):
        index = wiki.wiki_dir / "index.md"
        index.write_text("# Curated index\n\n- [[a-page]]\n", encoding="utf-8")

        result = rebuild_derived(wiki)

        assert "Curated index" in index.read_text()
        assert "index.md" not in result["rebuilt"]

    def test_generated_artifacts_are_still_rebuilt(self, wiki, tmp_path):
        """The guard must not block the normal regeneration path."""
        rebuild_derived(wiki)  # first pass stamps both with the marker

        result = rebuild_derived(wiki)

        assert set(result["rebuilt"]) == {"index.md", "MIND_MAP.md"}
        assert result["skipped"] == []
        assert GENERATED_MARKER in (tmp_path / "MIND_MAP.md").read_text()

    def test_overwrite_curated_overwrites_curated(self, wiki, tmp_path):
        mind_map = tmp_path / "MIND_MAP.md"
        mind_map.write_text(CURATED_MIND_MAP, encoding="utf-8")

        result = rebuild_derived(wiki, overwrite_curated=True)

        assert "MIND_MAP.md" in result["rebuilt"]
        assert GENERATED_MARKER in mind_map.read_text()

    def test_rebuild_derived_has_no_force_parameter(self, wiki):
        """`force` means "ignore freshness" in wiki_rebuild. Reusing the word
        here for "destroy curated work" is how accidents happen."""
        import inspect

        params = inspect.signature(rebuild_derived).parameters
        assert "force" not in params
        assert "overwrite_curated" in params

    def test_wiki_rebuild_force_does_not_overwrite_curated(self, wiki, tmp_path):
        """`force` bypasses the freshness check only -- never the guard.

        `wiki_rebuild(wiki, force=True)` is the documented command. It must
        stay safe; discarding curated work requires overwrite_curated=True.
        """
        mind_map = tmp_path / "MIND_MAP.md"
        mind_map.write_text(CURATED_MIND_MAP, encoding="utf-8")

        result = wiki_rebuild(wiki, force=True)

        assert mind_map.read_text() == CURATED_MIND_MAP
        assert result["skipped"]

    def test_wiki_rebuild_overwrite_curated_is_explicit(self, wiki, tmp_path):
        mind_map = tmp_path / "MIND_MAP.md"
        mind_map.write_text(CURATED_MIND_MAP, encoding="utf-8")

        wiki_rebuild(wiki, force=True, overwrite_curated=True)

        assert GENERATED_MARKER in mind_map.read_text()

    def test_is_generated_on_absent_file(self, tmp_path):
        assert is_generated(tmp_path / "nope.md") is True

    def test_init_placeholder_index_is_generator_owned(self, wiki):
        """Regression: the tool's own placeholder must not look curated."""
        assert is_generated(wiki.wiki_dir / "index.md") is True


class TestLegacyManifestEntries:
    """The reader must handle hand-written entries without crashing."""

    LEGACY = (
        '{"op_id":"op_legacy_1","timestamp":"2026-05-15T22:00:00Z",'
        '"operation":"create","page_id":"sources/a-paper","revision_id":1,'
        '"comment":"hand-written note"}'
    )

    def test_legacy_entry_parses(self, tmp_path):
        path = tmp_path / "manifest.jsonl"
        path.write_text(self.LEGACY + "\n", encoding="utf-8")

        entries = Manifest(path).read_all()

        assert len(entries) == 1
        entry = entries[0]
        assert entry.op_id == "op_legacy_1"
        assert entry.op_type is OperationType.INGEST
        assert entry.actor is Actor.LLM
        assert entry.status is OperationStatus.COMPLETED
        assert entry.outputs.created_pages == ["sources/a-paper"]
        assert entry.outputs.page_revisions == {"sources/a-paper": 1}

    def test_legacy_comment_is_preserved_not_treated_as_error(self, tmp_path):
        path = tmp_path / "manifest.jsonl"
        path.write_text(self.LEGACY + "\n", encoding="utf-8")

        entry = Manifest(path).read_all()[0]

        assert entry.error_message is None
        assert entry.outputs.extra["comment"] == "hand-written note"

    def test_legacy_delete_maps_to_deleted_pages(self, tmp_path):
        path = tmp_path / "manifest.jsonl"
        path.write_text(
            '{"op_id":"op_d","timestamp":"2026-05-15T22:00:00Z",'
            '"operation":"delete","page_id":"concepts/gone"}\n',
            encoding="utf-8",
        )

        entry = Manifest(path).read_all()[0]

        assert entry.op_type is OperationType.DELETE
        assert entry.outputs.deleted_pages == ["concepts/gone"]

    def test_mixed_legacy_and_current_entries(self, tmp_path):
        current = (
            '{"op_id":"op_new","op_type":"ingest",'
            '"timestamp":"2026-06-01T10:00:00Z","actor":"llm",'
            '"inputs":{},"outputs":{},"status":"completed"}'
        )
        path = tmp_path / "manifest.jsonl"
        path.write_text(self.LEGACY + "\n" + current + "\n", encoding="utf-8")

        entries = Manifest(path).read_all()

        assert [e.op_id for e in entries] == ["op_legacy_1", "op_new"]
        assert all(e.op_type is OperationType.INGEST for e in entries)

    def test_count_operations_spans_both_shapes(self, tmp_path):
        current = (
            '{"op_id":"op_new","op_type":"ingest",'
            '"timestamp":"2026-06-01T10:00:00Z","actor":"llm",'
            '"inputs":{},"outputs":{},"status":"completed"}'
        )
        path = tmp_path / "manifest.jsonl"
        path.write_text(self.LEGACY + "\n" + current + "\n", encoding="utf-8")

        assert Manifest(path).count_operations(OperationType.INGEST) == 2


class TestWikilinkResolution:
    """Links are page_id-shaped in real vaults; the check must accept that."""

    def test_page_id_link_resolves(self, wiki):
        write_page_file(wiki, "concepts", "carry-trade", "A concept.",
                        title="Carry Trade")
        write_page_file(wiki, "sources", "a-paper",
                        "Cites [[concepts/carry-trade]].", title="A Paper")

        result = verify_wikilinks(wiki)

        assert result.passed, result.details

    def test_title_link_still_resolves(self, wiki):
        write_page_file(wiki, "concepts", "carry-trade", "A concept.",
                        title="Carry Trade")
        write_page_file(wiki, "sources", "a-paper", "Cites [[Carry Trade]].",
                        title="A Paper")

        assert verify_wikilinks(wiki).passed

    def test_bare_stem_link_resolves(self, wiki):
        """Obsidian resolves [[carry-trade]] by filename."""
        write_page_file(wiki, "concepts", "carry-trade", "A concept.",
                        title="Carry Trade")
        write_page_file(wiki, "sources", "a-paper", "Cites [[carry-trade]].",
                        title="A Paper")

        assert verify_wikilinks(wiki).passed

    def test_link_with_display_text_resolves(self, wiki):
        write_page_file(wiki, "concepts", "carry-trade", "A concept.",
                        title="Carry Trade")
        write_page_file(wiki, "sources", "a-paper",
                        "Cites [[concepts/carry-trade|the carry trade]].",
                        title="A Paper")

        assert verify_wikilinks(wiki).passed

    def test_link_with_section_anchor_resolves(self, wiki):
        write_page_file(wiki, "concepts", "carry-trade", "A concept.",
                        title="Carry Trade")
        write_page_file(wiki, "sources", "a-paper",
                        "Cites [[concepts/carry-trade#Definition]].",
                        title="A Paper")

        assert verify_wikilinks(wiki).passed

    def test_genuinely_broken_link_is_still_reported(self, wiki):
        write_page_file(wiki, "sources", "a-paper",
                        "Cites [[concepts/does-not-exist]].", title="A Paper")

        result = verify_wikilinks(wiki)

        assert not result.passed
        assert any("does-not-exist" in d for d in result.details)

    def test_normalize_link_target_strips_anchor(self):
        assert normalize_link_target("concepts/x#Section") == "concepts/x"
        assert normalize_link_target("concepts/x") == "concepts/x"
        assert normalize_link_target("#Section") == ""

    def test_resolve_link_targets_includes_all_three_names(self, wiki):
        write_page_file(wiki, "concepts", "carry-trade", "A concept.",
                        title="Carry Trade")

        targets = resolve_link_targets(wiki)

        assert "concepts/carry-trade" in targets
        assert "Carry Trade" in targets
        assert "carry-trade" in targets


class TestEscapedPipeLinks:
    """Inside a markdown table the pipe must be escaped as \\|, which leaves a
    trailing backslash on the captured target. 32 links in the real wiki use
    this form and were all reported broken."""

    def test_table_escaped_pipe_resolves(self, wiki):
        write_page_file(wiki, "concepts", "enbpi", "A concept.", title="EnbPI")
        write_page_file(
            wiki, "sources", "a-paper",
            "| Method | Note |\n|---|---|\n| [[concepts/enbpi\\|EnbPI]] | x |",
            title="A Paper",
        )

        result = verify_wikilinks(wiki)

        assert result.passed, result.details

    def test_normalize_strips_trailing_backslash(self):
        assert normalize_link_target("concepts/enbpi\\") == "concepts/enbpi"
        assert normalize_link_target("concepts/x\\#Sec") == "concepts/x"

    def test_backslash_inside_name_is_not_stripped(self):
        """Only a TRAILING backslash is an escape artefact."""
        assert normalize_link_target("concepts/a\\b") == "concepts/a\\b"


class TestMarkerSearchWindow:
    """The marker sits after the frontmatter; real pages have ~6 KB of it."""

    def test_marker_found_beyond_a_small_window(self, wiki, tmp_path):
        from llm_wiki.io.page_io import GENERATED_MARKER, is_generated

        big_frontmatter = "---\n" + "".join(
            f"related_{i}: some-fairly-long-page-identifier-value-{i}\n"
            for i in range(400)
        ) + "---\n\n"
        path = tmp_path / "big.md"
        path.write_text(big_frontmatter + f"<!--\n{GENERATED_MARKER}\n-->\n", encoding="utf-8")

        assert len(big_frontmatter) > 4096, "fixture must exceed the old window"
        assert is_generated(path) is True
