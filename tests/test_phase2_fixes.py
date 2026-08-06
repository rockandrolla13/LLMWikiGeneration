"""Tests for the Phase 2 correctness fixes.

Each test pins a bug that shipped silently: a hash that was computed but never
written, a hash convention that could never verify, path properties that
changed answer with call order, and a script that emitted invalid YAML.
"""

from datetime import datetime
from pathlib import Path

import frontmatter
import pytest
import yaml

from llm_wiki import Wiki, wiki_init, wiki_ingest
from llm_wiki.clock import utc_now
from llm_wiki.io import (
    compute_content_hash,
    compute_page_content_hash,
    parse_page,
    write_page,
)


class TestPageHashRoundTrip:
    """A stored revision_hash must be verifiable after a write/read cycle."""

    @pytest.mark.parametrize("content", [
        "# Title\n\nBody.\n\n",          # trailing blank lines
        "\n\n# Title\n\nBody.",          # leading blank lines
        "# Title\n\nBody.",              # already tight
        "# Title\n\nBody with trailing spaces.   \n",
    ])
    def test_hash_survives_round_trip(self, tmp_path, content):
        path = tmp_path / "page.md"
        written_hash = write_page(path, {"title": "T"}, content)

        _, read_back = parse_page(path)

        assert compute_page_content_hash(read_back) == written_hash

    def test_raw_hash_does_not_survive_round_trip(self, tmp_path):
        """Documents WHY the normalised variant exists.

        The frontmatter library strips surrounding whitespace, so the raw hash
        of the pre-write body differs from the raw hash of the post-read body.
        """
        content = "# Title\n\nBody.\n\n"
        path = tmp_path / "page.md"
        write_page(path, {"title": "T"}, content)

        _, read_back = parse_page(path)

        assert compute_content_hash(content) != compute_content_hash(read_back)
        # ...but the normalised form agrees
        assert compute_page_content_hash(content) == compute_page_content_hash(read_back)


class TestIngestPersistsRevisionHash:
    """wiki_ingest computed a hash into a local dict and dropped it."""

    def test_source_page_has_matching_hash(self, tmp_path):
        wiki_init(tmp_path, name="T")
        wiki = Wiki(tmp_path)
        (tmp_path / "raw" / "doc.md").write_text("# Doc\n\nBody.")

        wiki_ingest(wiki, Path("raw/doc.md"), title="Doc")

        metadata, content = parse_page(tmp_path / "wiki" / "sources" / "doc.md")
        assert metadata["revision_hash"]
        assert metadata["revision_hash"] == compute_page_content_hash(content)

    def test_derived_entity_and_concept_pages_have_matching_hashes(self, tmp_path):
        wiki_init(tmp_path, name="T")
        wiki = Wiki(tmp_path)
        (tmp_path / "raw" / "doc.md").write_text("# Doc\n\nBody.")

        wiki_ingest(
            wiki,
            Path("raw/doc.md"),
            title="Doc",
            extracted_entities=["Ada Lovelace"],
            extracted_concepts=["Analytical Engine"],
        )

        for rel in ["entities/ada_lovelace.md", "concepts/analytical_engine.md"]:
            metadata, content = parse_page(tmp_path / "wiki" / rel)
            assert metadata["revision_hash"] == compute_page_content_hash(content), rel

    def test_verify_revision_hashes_passes_after_ingest(self, tmp_path):
        from llm_wiki.verify import verify_revision_hashes

        wiki_init(tmp_path, name="T")
        wiki = Wiki(tmp_path)
        (tmp_path / "raw" / "doc.md").write_text("# Doc\n\nBody.")
        wiki_ingest(wiki, Path("raw/doc.md"), title="Doc",
                    extracted_concepts=["Some Concept"])

        result = verify_revision_hashes(wiki)

        assert result.passed, result.details


class TestPathPropertiesAreOrderIndependent:
    """raw_dir/wiki_dir/assets_dir returned different values before and after
    config was lazily loaded."""

    @pytest.fixture
    def custom_wiki(self, tmp_path):
        wiki_init(tmp_path, name="T")
        # Point the config at non-default directory names
        cfg = yaml.safe_load((tmp_path / "schema.yml").read_text())
        cfg["paths"] = {"raw": "inputs", "wiki": "pages", "assets": "inputs/media"}
        (tmp_path / "schema.yml").write_text(yaml.safe_dump(cfg))
        return tmp_path

    @pytest.mark.parametrize("attr,expected", [
        ("raw_dir", "inputs"),
        ("wiki_dir", "pages"),
        ("assets_dir", "inputs/media"),
    ])
    def test_value_is_same_before_and_after_config_load(self, custom_wiki, attr, expected):
        cold = Wiki(custom_wiki)
        before = getattr(cold, attr)

        warm = Wiki(custom_wiki)
        _ = warm.config          # force the lazy load first
        after = getattr(warm, attr)

        assert before == after
        assert before == custom_wiki / expected

    def test_falls_back_to_defaults_when_no_config_exists(self, tmp_path):
        """An uninitialised wiki must not raise -- it uses the defaults."""
        w = Wiki(tmp_path / "nothing-here")

        assert w.raw_dir.name == "raw"
        assert w.wiki_dir.name == "wiki"


class TestWikiBuilderYamlSafety:
    """The builder interpolated titles into a YAML template by hand."""

    @pytest.fixture
    def builder(self, tmp_path, monkeypatch):
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "wiki_builder",
            Path(__file__).parent.parent / "scripts" / "wiki_builder.py",
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        monkeypatch.setattr(module, "WIKI_ROOT", tmp_path)
        return module

    @pytest.mark.parametrize("title", [
        'A Title With "Quotes"',
        "Title: With A Colon",
        "Title with 'single quotes'",
        "Title with \\ backslash",
        "Ünïcödé Títlé",
    ])
    def test_hostile_titles_produce_parseable_frontmatter(self, builder, title):
        path = builder.create_source_page(
            {"title": title, "slug": "test-doc", "authors": ["A. Author"]},
            "Preview text.",
        )

        post = frontmatter.load(str(path))

        assert post["title"] == title
        assert post["page_id"] == "sources/test-doc"

    def test_update_index_does_not_claim_success(self, builder, capsys):
        """It never edited the index; it must not print that it did."""
        (builder.WIKI_ROOT / "index.md").write_text("# Index\n")

        builder.update_index([builder.WIKI_ROOT / "sources" / "a.md"])

        out = capsys.readouterr().out
        assert "✓ Updated index.md" not in out
        assert "NOT updated" in out


class TestClock:
    """utc_now must stay naive so isoformat() + 'Z' remains correct."""

    def test_returns_naive_datetime(self):
        assert utc_now().tzinfo is None

    def test_serialises_without_double_offset(self):
        stamp = utc_now().isoformat() + "Z"

        assert "+00:00" not in stamp
        assert stamp.endswith("Z")
        # And it round-trips the way the manifest reader expects
        assert isinstance(datetime.fromisoformat(stamp.rstrip("Z")), datetime)
