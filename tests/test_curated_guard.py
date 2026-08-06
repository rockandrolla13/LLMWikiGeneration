"""Tests for the curated-artifact guard and the v1 correctness fixes.

The guard exists because it already failed once: an unguarded rebuild replaced
wiki/MIND_MAP.md's 211 hand-curated nodes with 28 generated ones, and the
warning comment added afterwards could not stop a program.
"""

import pytest

from llm_wiki import Wiki, wiki_init, wiki_rebuild
from llm_wiki.clock import utc_now
from llm_wiki.derived import rebuild_derived
from llm_wiki.io.page_io import GENERATED_MARKER, is_generated
from llm_wiki.io.wikilinks import normalize_link_target
from llm_wiki.manifest import Manifest, Actor, OperationStatus, OperationType


CURATED = """<!--
TIER 1 - HANDCRAFTED - DO NOT OVERWRITE WITH wiki_rebuild()
-->

[1] **Overview** - Hand-written synthesis the generator cannot reproduce.
"""


@pytest.fixture
def wiki(tmp_path):
    wiki_init(tmp_path, name="Test Wiki")
    return Wiki(tmp_path)


class TestCuratedGuard:
    def test_curated_mind_map_survives_rebuild(self, wiki, tmp_path):
        mind_map = tmp_path / "MIND_MAP.md"
        mind_map.write_text(CURATED, encoding="utf-8")

        result = rebuild_derived(wiki)

        assert mind_map.read_text() == CURATED
        assert "MIND_MAP.md" not in result["rebuilt"]
        assert any("MIND_MAP.md" in s for s in result["skipped"])

    def test_wiki_rebuild_force_does_not_overwrite_curated(self, wiki, tmp_path):
        """`force` bypasses the freshness check only, never the guard.

        wiki_rebuild(wiki, force=True) is the documented command and must stay
        safe; discarding curated work has to be asked for separately.
        """
        mind_map = tmp_path / "MIND_MAP.md"
        mind_map.write_text(CURATED, encoding="utf-8")

        wiki_rebuild(wiki, force=True)

        assert mind_map.read_text() == CURATED

    def test_overwrite_curated_is_explicit(self, wiki, tmp_path):
        mind_map = tmp_path / "MIND_MAP.md"
        mind_map.write_text(CURATED, encoding="utf-8")

        result = rebuild_derived(wiki, overwrite_curated=True)

        assert "MIND_MAP.md" in result["rebuilt"]
        assert GENERATED_MARKER in mind_map.read_text()

    def test_generated_artifacts_still_rebuild(self, wiki):
        """The guard must not block the normal regeneration path."""
        rebuild_derived(wiki)
        result = rebuild_derived(wiki)

        assert "index.md" in result["rebuilt"]
        assert "MIND_MAP.md" in result["rebuilt"]
        assert result["skipped"] == []

    def test_init_placeholder_is_generator_owned(self, wiki):
        """Regression: the tool's own placeholder must not look curated."""
        assert is_generated(wiki.wiki_dir / "index.md") is True

    def test_absent_file_is_writable(self, tmp_path):
        assert is_generated(tmp_path / "nothing.md") is True


class TestLegacyManifest:
    LEGACY = (
        '{"op_id":"op_legacy_1","timestamp":"2026-05-15T22:00:00Z",'
        '"operation":"create","page_id":"sources/a-paper","revision_id":1,'
        '"comment":"hand-written note"}'
    )

    def test_legacy_entry_parses(self, tmp_path):
        path = tmp_path / "manifest.jsonl"
        path.write_text(self.LEGACY + "\n", encoding="utf-8")

        entry = Manifest(path).read_all()[0]

        assert entry.op_id == "op_legacy_1"
        assert entry.op_type is OperationType.INGEST
        assert entry.actor is Actor.LLM
        assert entry.status is OperationStatus.COMPLETED
        assert entry.outputs.created_pages == ["sources/a-paper"]

    def test_comment_preserved_not_treated_as_error(self, tmp_path):
        path = tmp_path / "manifest.jsonl"
        path.write_text(self.LEGACY + "\n", encoding="utf-8")

        entry = Manifest(path).read_all()[0]

        assert entry.error_message is None
        assert entry.outputs.extra["comment"] == "hand-written note"

    def test_mixed_shapes_read_together(self, tmp_path):
        current = (
            '{"op_id":"op_new","op_type":"ingest",'
            '"timestamp":"2026-06-01T10:00:00Z","actor":"llm",'
            '"inputs":{},"outputs":{},"status":"completed"}'
        )
        path = tmp_path / "manifest.jsonl"
        path.write_text(self.LEGACY + "\n" + current + "\n", encoding="utf-8")

        assert [e.op_id for e in Manifest(path).read_all()] == ["op_legacy_1", "op_new"]

    def test_missing_op_id_still_raises(self, tmp_path):
        """op_id has no sensible fallback, so that IS an error."""
        path = tmp_path / "manifest.jsonl"
        path.write_text('{"timestamp":"2024-01-01T00:00:00Z","operation":"create"}\n')

        with pytest.raises(KeyError):
            Manifest(path).read_all()


class TestLinkNormalisation:
    @pytest.mark.parametrize("raw,expected", [
        ("concepts/carry-trade", "concepts/carry-trade"),
        ("concepts/carry-trade|the carry trade", "concepts/carry-trade"),
        ("concepts/carry-trade#Definition", "concepts/carry-trade"),
        ("concepts/enbpi\\", "concepts/enbpi"),          # table-escaped pipe
        ("concepts/enbpi\\|EnbPI", "concepts/enbpi"),
        ("#Section", ""),                                 # same-page anchor
    ])
    def test_targets_normalise(self, raw, expected):
        assert normalize_link_target(raw) == expected


class TestPathPropertiesOrderIndependent:
    def test_same_answer_before_and_after_config_load(self, tmp_path):
        import yaml

        wiki_init(tmp_path, name="T")
        cfg = yaml.safe_load((tmp_path / "schema.yml").read_text())
        cfg["paths"] = {"raw": "inputs", "wiki": "pages", "assets": "inputs/media"}
        (tmp_path / "schema.yml").write_text(yaml.safe_dump(cfg))

        cold = Wiki(tmp_path).wiki_dir
        warm = Wiki(tmp_path)
        _ = warm.config
        assert cold == warm.wiki_dir == tmp_path / "pages"

    def test_defaults_when_no_config(self, tmp_path):
        w = Wiki(tmp_path / "absent")
        assert w.wiki_dir.name == "wiki"


class TestClock:
    def test_naive_so_z_suffix_stays_correct(self):
        stamp = utc_now().isoformat() + "Z"
        assert utc_now().tzinfo is None
        assert "+00:00" not in stamp and stamp.endswith("Z")
