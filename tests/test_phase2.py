"""Tests for Phase 2: Derived Artifacts.

Tests the derived artifact generation:
- compile_index: Generate index.md
- compile_mind_map: Generate MIND_MAP.md
- rebuild: Regenerate all derived artifacts
- freshness: Detect stale artifacts
"""

import tempfile
from pathlib import Path
import pytest

from llm_wiki import (
    Wiki,
    wiki_init,
    wiki_ingest,
    wiki_rebuild,
    wiki_freshness,
    compile_index,
    compile_mind_map,
    check_freshness,
    rebuild_derived,
)


class TestCompileIndex:
    """Test index.md compilation."""

    def test_compile_index_empty_wiki(self, tmp_path):
        """Index for empty wiki has section headers."""
        wiki_init(tmp_path, name="Test Wiki", topic="testing")
        wiki = Wiki(tmp_path)

        index_content = compile_index(wiki)

        assert "# Test Wiki" in index_content
        assert "## Sources" in index_content
        assert "## Entities" in index_content
        assert "## Concepts" in index_content
        assert "(No sources ingested yet)" in index_content

    def test_compile_index_with_pages(self, tmp_path):
        """Index includes ingested pages."""
        wiki_init(tmp_path, name="Test Wiki")

        # Create source
        source_path = tmp_path / "raw" / "test.md"
        source_path.write_text("# Test Article\n\nThis is a test.")

        wiki = Wiki(tmp_path)
        wiki_ingest(
            wiki,
            Path("raw/test.md"),
            title="Test Article",
            summary="A test article",
            extracted_concepts=["Testing"],
        )

        index_content = compile_index(wiki)

        assert "[[Test Article]]" in index_content
        assert "[[Testing]]" in index_content
        assert "Total sources: 1" in index_content
        assert "Total concepts: 1" in index_content

    def test_compile_index_deterministic(self, tmp_path):
        """Same input produces same output."""
        wiki_init(tmp_path, name="Test Wiki")

        source_path = tmp_path / "raw" / "test.md"
        source_path.write_text("# Test")

        wiki = Wiki(tmp_path)
        wiki_ingest(wiki, Path("raw/test.md"), title="Test")

        index1 = compile_index(wiki)
        index2 = compile_index(wiki)

        # Content should be identical (except timestamps which are inside)
        # Split and compare non-timestamp lines
        lines1 = [l for l in index1.split('\n') if 'Generated:' not in l and 'Last updated:' not in l]
        lines2 = [l for l in index2.split('\n') if 'Generated:' not in l and 'Last updated:' not in l]
        assert lines1 == lines2

    def test_compile_index_has_generation_header(self, tmp_path):
        """Index has auto-generated header."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        index_content = compile_index(wiki)

        assert "AUTO-GENERATED FILE" in index_content
        assert "Source hash:" in index_content
        assert "wiki:rebuild" in index_content


class TestCompileMindMap:
    """Test MIND_MAP.md compilation."""

    def test_compile_mind_map_empty_wiki(self, tmp_path):
        """Mind map for empty wiki has routing nodes."""
        wiki_init(tmp_path, name="Test Wiki", topic="testing")
        wiki = Wiki(tmp_path)

        mind_map = compile_mind_map(wiki)

        assert "[1] **Overview**" in mind_map
        assert "[2] **Sources**" in mind_map
        assert "[3] **Entities**" in mind_map
        assert "[4] **Concepts**" in mind_map
        assert "[5] **Analyses**" in mind_map

    def test_compile_mind_map_with_content(self, tmp_path):
        """Mind map includes page nodes."""
        wiki_init(tmp_path, name="Test Wiki", topic="ML")

        source_path = tmp_path / "raw" / "paper.md"
        source_path.write_text("# Important Paper\n\nKey findings about ML.")

        wiki = Wiki(tmp_path)
        wiki_ingest(
            wiki,
            Path("raw/paper.md"),
            title="Important Paper",
            summary="Key findings about machine learning",
            extracted_concepts=["Machine Learning"],
        )

        mind_map = compile_mind_map(wiki)

        # Should have routing nodes
        assert "[1] **Overview**" in mind_map
        # Should reference the topic
        assert "ML" in mind_map or "testing" in mind_map
        # Should have source count
        assert "1 source" in mind_map or "sources" in mind_map

    def test_compile_mind_map_single_line_nodes(self, tmp_path):
        """Each node is on a single line (grep-friendly)."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        mind_map = compile_mind_map(wiki)

        # Find all node lines
        node_lines = [l for l in mind_map.split('\n') if l.startswith('[')]

        for line in node_lines:
            # Each node should be a single line (no embedded newlines)
            assert '\n' not in line
            # Should start with [N]
            assert line[0] == '['
            assert ']' in line[:5]


class TestFreshness:
    """Test freshness tracking."""

    def test_freshness_missing_artifacts(self, tmp_path):
        """Detect missing derived artifacts."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        # MIND_MAP.md doesn't exist yet
        freshness = check_freshness(wiki)

        assert "MIND_MAP.md" in freshness
        assert freshness["MIND_MAP.md"].exists is False
        assert freshness["MIND_MAP.md"].needs_rebuild is True

    def test_freshness_after_rebuild(self, tmp_path):
        """Fresh after rebuild."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        # Rebuild
        rebuild_derived(wiki)

        freshness = check_freshness(wiki)

        assert freshness["index.md"].exists is True
        assert freshness["MIND_MAP.md"].exists is True
        # Both should be fresh (source hash matches)
        assert freshness["index.md"].is_fresh is True
        assert freshness["MIND_MAP.md"].is_fresh is True

    def test_freshness_stale_after_ingest(self, tmp_path):
        """Stale after new content added."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        # Build initial
        rebuild_derived(wiki)

        # Add new content
        source_path = tmp_path / "raw" / "new.md"
        source_path.write_text("# New Content")
        wiki_ingest(wiki, Path("raw/new.md"), title="New Content")

        # Should now be stale
        freshness = check_freshness(wiki)

        assert freshness["index.md"].is_fresh is False
        assert freshness["MIND_MAP.md"].is_fresh is False


class TestRebuild:
    """Test rebuild command."""

    def test_rebuild_creates_artifacts(self, tmp_path):
        """Rebuild creates missing artifacts."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        result = wiki_rebuild(wiki, force=True)

        assert result["success"] is True
        assert "index.md" in result["rebuilt"]
        assert "MIND_MAP.md" in result["rebuilt"]
        assert (tmp_path / "MIND_MAP.md").exists()

    def test_rebuild_skips_fresh(self, tmp_path):
        """Rebuild skips fresh artifacts unless forced."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        # First rebuild
        wiki_rebuild(wiki, force=True)

        # Second rebuild without force should skip
        result = wiki_rebuild(wiki, force=False)

        assert result["success"] is True
        assert "fresh" in result["message"].lower()
        assert result["rebuilt"] == []

    def test_rebuild_force_always_rebuilds(self, tmp_path):
        """Force rebuild even if fresh."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        # First rebuild
        wiki_rebuild(wiki, force=True)

        # Force rebuild should rebuild anyway
        result = wiki_rebuild(wiki, force=True)

        assert result["success"] is True
        assert len(result["rebuilt"]) == 2

    def test_rebuild_updates_manifest(self, tmp_path):
        """Rebuild adds entry to manifest."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        wiki_rebuild(wiki, force=True)

        entries = wiki.manifest.read_all()
        rebuild_entries = [e for e in entries if e.op_type.value == "rebuild"]
        assert len(rebuild_entries) == 1


class TestWikiFreshness:
    """Test wiki_freshness command."""

    def test_wiki_freshness_reports_status(self, tmp_path):
        """Reports freshness status for all artifacts."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        result = wiki_freshness(wiki)

        assert "all_fresh" in result
        assert "artifacts" in result
        assert "index.md" in result["artifacts"]
        assert "MIND_MAP.md" in result["artifacts"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
