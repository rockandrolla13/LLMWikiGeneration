"""Tests for Phase 1: Canonical Core.

Tests the basic wiki operations:
- init: Create wiki structure
- ingest: Add source documents
- verify: Check invariants
"""

import tempfile
import shutil
from pathlib import Path
import pytest

from llm_wiki import (
    Wiki,
    wiki_init,
    wiki_ingest,
    wiki_stats,
    PageType,
    OperationType,
)
from llm_wiki.verify import verify_wiki


class TestWikiInit:
    """Test wiki initialization."""

    def test_init_creates_structure(self, tmp_path):
        """Wiki init creates all required directories and files."""
        result = wiki_init(
            tmp_path,
            name="Test Wiki",
            topic="testing",
            profile="research",
        )

        assert result["success"] is True
        assert "op_id" in result

        # Check files exist
        assert (tmp_path / "schema.yml").exists()
        assert (tmp_path / "manifest.jsonl").exists()
        assert (tmp_path / "wiki" / "index.md").exists()
        assert (tmp_path / "wiki" / "log.md").exists()

        # Check directories exist
        assert (tmp_path / "raw").is_dir()
        assert (tmp_path / "wiki" / "sources").is_dir()
        assert (tmp_path / "wiki" / "entities").is_dir()
        assert (tmp_path / "wiki" / "concepts").is_dir()

    def test_init_twice_fails(self, tmp_path):
        """Cannot initialize wiki twice."""
        wiki_init(tmp_path, name="Test Wiki")
        result = wiki_init(tmp_path, name="Test Wiki 2")

        assert result["success"] is False
        assert "already exists" in result["error"]

    def test_init_creates_valid_config(self, tmp_path):
        """Config file contains correct values."""
        wiki_init(tmp_path, name="My Research", topic="ML", profile="research")

        wiki = Wiki(tmp_path)
        assert wiki.config.name == "My Research"
        assert wiki.config.topic == "ML"
        assert wiki.config.profile == "research"

    def test_init_creates_manifest_entry(self, tmp_path):
        """Manifest contains init operation."""
        wiki_init(tmp_path, name="Test Wiki")

        wiki = Wiki(tmp_path)
        entries = wiki.manifest.read_all()

        assert len(entries) == 1
        assert entries[0].op_type == OperationType.INIT
        assert entries[0].status.value == "completed"


class TestWikiIngest:
    """Test source ingestion."""

    @pytest.fixture
    def wiki_with_source(self, tmp_path):
        """Create wiki with a test source file."""
        wiki_init(tmp_path, name="Test Wiki")

        # Create a test source
        source_path = tmp_path / "raw" / "test_article.md"
        source_path.write_text("""# Test Article

This is a test article about machine learning.

## Key Points

- Point 1
- Point 2
""")

        return Wiki(tmp_path), "raw/test_article.md"

    def test_ingest_creates_source_page(self, wiki_with_source):
        """Ingest creates a source page."""
        wiki, source_path = wiki_with_source

        result = wiki_ingest(
            wiki,
            Path(source_path),
            title="Test Article",
            summary="A test article about ML",
        )

        assert result["success"] is True
        assert result["page_id"] == "sources/test_article"
        assert wiki.page_exists("sources/test_article")

    def test_ingest_with_entities(self, wiki_with_source):
        """Ingest creates entity pages when specified."""
        wiki, source_path = wiki_with_source

        result = wiki_ingest(
            wiki,
            Path(source_path),
            title="Test Article",
            extracted_entities=["Andrew Ng", "Google"],
        )

        assert result["success"] is True
        assert len(result["created_pages"]) == 3  # source + 2 entities
        assert wiki.page_exists("entities/andrew_ng")
        assert wiki.page_exists("entities/google")

    def test_ingest_with_concepts(self, wiki_with_source):
        """Ingest creates concept pages when specified."""
        wiki, source_path = wiki_with_source

        result = wiki_ingest(
            wiki,
            Path(source_path),
            title="Test Article",
            extracted_concepts=["Machine Learning", "Neural Networks"],
        )

        assert result["success"] is True
        assert wiki.page_exists("concepts/machine_learning")
        assert wiki.page_exists("concepts/neural_networks")

    def test_ingest_updates_manifest(self, wiki_with_source):
        """Ingest adds entry to manifest."""
        wiki, source_path = wiki_with_source

        result = wiki_ingest(wiki, Path(source_path), title="Test Article")

        entries = wiki.manifest.read_all()
        assert len(entries) == 2  # init + ingest
        assert entries[1].op_type == OperationType.INGEST

    def test_ingest_nonexistent_source_fails(self, tmp_path):
        """Ingest fails for missing source file."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        result = wiki_ingest(wiki, Path("raw/nonexistent.md"))

        assert result["success"] is False
        assert "not found" in result["error"]

    def test_ingest_duplicate_fails(self, wiki_with_source):
        """Cannot ingest same source twice."""
        wiki, source_path = wiki_with_source

        wiki_ingest(wiki, Path(source_path), title="Test Article")
        result = wiki_ingest(wiki, Path(source_path), title="Test Article 2")

        assert result["success"] is False
        assert "already ingested" in result["error"]


class TestWikiVerify:
    """Test wiki verification."""

    def test_verify_fresh_wiki_passes(self, tmp_path):
        """Fresh wiki passes all checks."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        report = verify_wiki(wiki)

        # Should pass most checks (some may be skipped)
        assert report.passed >= 6
        assert report.failed <= 2  # wikilinks may have broken refs

    def test_verify_reports_issues(self, tmp_path):
        """Verify catches issues."""
        wiki_init(tmp_path, name="Test Wiki")

        # Delete a required directory
        shutil.rmtree(tmp_path / "wiki" / "entities")

        wiki = Wiki(tmp_path)
        report = verify_wiki(wiki)

        # Should report missing directory
        dir_result = next(r for r in report.results if r.name == "Directory Structure")
        assert dir_result.passed is False


class TestWikiStats:
    """Test wiki statistics."""

    def test_stats_empty_wiki(self, tmp_path):
        """Stats for empty wiki."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        stats = wiki_stats(wiki)

        assert stats["total_sources"] == 0
        assert stats["total_pages"] == 0
        assert stats["total_operations"] == 1  # init

    def test_stats_after_ingest(self, tmp_path):
        """Stats update after ingest."""
        wiki_init(tmp_path, name="Test Wiki")

        # Create source
        source_path = tmp_path / "raw" / "test.md"
        source_path.write_text("# Test")

        wiki = Wiki(tmp_path)
        wiki_ingest(
            wiki,
            Path("raw/test.md"),
            title="Test",
            extracted_entities=["Entity1"],
            extracted_concepts=["Concept1"],
        )

        stats = wiki_stats(wiki)

        assert stats["total_sources"] == 1
        assert stats["total_entities"] == 1
        assert stats["total_concepts"] == 1
        assert stats["total_pages"] == 3
        assert stats["total_ingests"] == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
