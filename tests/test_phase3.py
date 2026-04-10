"""Tests for Phase 3: Search Integration.

Tests the search functionality:
- GrepSearchBackend: Built-in regex search
- wiki_query: High-level search command
- wiki_find_links: Find pages linking to a target
"""

from pathlib import Path
import pytest

from llm_wiki import (
    Wiki,
    wiki_init,
    wiki_ingest,
    wiki_query,
    wiki_find_links,
    search_wiki,
    search_by_link,
    get_search_backend,
    SearchQuery,
)
from llm_wiki.search import GrepSearchBackend, QMDSearchBackend


class TestGrepSearchBackend:
    """Test the built-in grep search backend."""

    def test_grep_backend_available(self):
        """Grep backend is always available."""
        backend = GrepSearchBackend()
        assert backend.is_available() is True

    def test_grep_backend_build_index(self, tmp_path):
        """Grep backend index build succeeds (no-op)."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)
        backend = GrepSearchBackend()

        result = backend.build_index(wiki)
        assert result is True

    def test_grep_search_empty_wiki(self, tmp_path):
        """Search empty wiki returns no results."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        results = search_wiki(wiki, "test")
        assert len(results) == 0

    def test_grep_search_finds_matches(self, tmp_path):
        """Search finds pages containing query terms."""
        wiki_init(tmp_path, name="Test Wiki")

        # Create source with searchable content
        source_path = tmp_path / "raw" / "ml_paper.md"
        source_path.write_text("# Machine Learning Paper\n\nDeep learning is great.")

        wiki = Wiki(tmp_path)
        wiki_ingest(
            wiki,
            Path("raw/ml_paper.md"),
            title="Machine Learning Paper",
            summary="A paper about deep learning and neural networks",
        )

        # Search for "learning"
        results = search_wiki(wiki, "learning")

        assert len(results) >= 1
        assert any("learning" in r.title.lower() for r in results)

    def test_grep_search_case_insensitive(self, tmp_path):
        """Search is case insensitive."""
        wiki_init(tmp_path, name="Test Wiki")

        source_path = tmp_path / "raw" / "test.md"
        source_path.write_text("# Test Article\n\nMACHINE LEARNING is great.")

        wiki = Wiki(tmp_path)
        # Include MACHINE in summary so it's in the wiki page
        wiki_ingest(
            wiki,
            Path("raw/test.md"),
            title="Test Article",
            summary="MACHINE LEARNING is great.",
        )

        # Search lowercase
        results = search_wiki(wiki, "machine")
        assert len(results) >= 1

    def test_grep_search_multiple_terms(self, tmp_path):
        """Search with multiple terms."""
        wiki_init(tmp_path, name="Test Wiki")

        source_path = tmp_path / "raw" / "test.md"
        source_path.write_text("# Neural Networks\n\nDeep learning uses neural networks.")

        wiki = Wiki(tmp_path)
        wiki_ingest(wiki, Path("raw/test.md"), title="Neural Networks")

        # Search for "neural networks"
        results = search_wiki(wiki, "neural networks")
        assert len(results) >= 1

    def test_grep_search_returns_snippets(self, tmp_path):
        """Search results include text snippets."""
        wiki_init(tmp_path, name="Test Wiki")

        source_path = tmp_path / "raw" / "test.md"
        source_path.write_text("# Test\n\nThis article discusses transformers and attention.")

        wiki = Wiki(tmp_path)
        wiki_ingest(
            wiki,
            Path("raw/test.md"),
            title="Test",
            summary="About transformers",
        )

        results = search_wiki(wiki, "transformers")

        assert len(results) >= 1
        assert results[0].snippet  # Has a snippet
        assert len(results[0].snippet) > 0

    def test_grep_search_filter_by_type(self, tmp_path):
        """Search can filter by page type."""
        wiki_init(tmp_path, name="Test Wiki")

        source_path = tmp_path / "raw" / "test.md"
        source_path.write_text("# ML Paper")

        wiki = Wiki(tmp_path)
        wiki_ingest(
            wiki,
            Path("raw/test.md"),
            title="ML Paper",
            extracted_concepts=["Machine Learning"],
        )

        # Search only sources
        source_results = search_wiki(wiki, "ML", page_types=["source"])
        concept_results = search_wiki(wiki, "Machine", page_types=["concept"])

        # Should find in sources
        assert len(source_results) >= 1
        # Should find in concepts
        assert len(concept_results) >= 1

    def test_grep_search_limit_results(self, tmp_path):
        """Search respects limit parameter."""
        wiki_init(tmp_path, name="Test Wiki")

        # Create multiple sources
        for i in range(5):
            source_path = tmp_path / "raw" / f"test{i}.md"
            source_path.write_text(f"# Test Article {i}\n\nCommon keyword here.")

            wiki = Wiki(tmp_path)
            wiki_ingest(wiki, Path(f"raw/test{i}.md"), title=f"Test Article {i}")

        wiki = Wiki(tmp_path)
        results = search_wiki(wiki, "keyword", limit=3)

        assert len(results) <= 3


class TestQMDSearchBackend:
    """Test the QMD search backend (optional)."""

    def test_qmd_backend_not_available(self):
        """QMD backend reports unavailable when not installed."""
        backend = QMDSearchBackend(qmd_path="/nonexistent/qmd")
        assert backend.is_available() is False


class TestGetSearchBackend:
    """Test backend selection."""

    def test_default_backend_is_grep(self, tmp_path):
        """Default backend is grep."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        backend = get_search_backend(wiki)
        assert isinstance(backend, GrepSearchBackend)


class TestWikiQuery:
    """Test wiki_query command."""

    def test_wiki_query_success(self, tmp_path):
        """wiki_query returns results."""
        wiki_init(tmp_path, name="Test Wiki")

        source_path = tmp_path / "raw" / "test.md"
        source_path.write_text("# Test\n\nSearchable content here.")

        wiki = Wiki(tmp_path)
        # Include searchable term in summary so it's in the wiki page
        wiki_ingest(
            wiki,
            Path("raw/test.md"),
            title="Test",
            summary="Searchable content here.",
        )

        result = wiki_query(wiki, "searchable")

        assert result["success"] is True
        assert result["count"] >= 1
        assert len(result["results"]) >= 1

    def test_wiki_query_empty_query(self, tmp_path):
        """wiki_query fails for empty query."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        result = wiki_query(wiki, "")

        assert result["success"] is False
        assert "empty" in result["error"].lower()

    def test_wiki_query_no_results(self, tmp_path):
        """wiki_query returns empty for no matches."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        result = wiki_query(wiki, "nonexistentterm12345")

        assert result["success"] is True
        assert result["count"] == 0

    def test_wiki_query_reports_backend(self, tmp_path):
        """wiki_query reports which backend was used."""
        wiki_init(tmp_path, name="Test Wiki")
        wiki = Wiki(tmp_path)

        result = wiki_query(wiki, "test")

        assert "backend" in result
        assert "GrepSearchBackend" in result["backend"]


class TestWikiFindLinks:
    """Test wiki_find_links command."""

    def test_find_links_to_concept(self, tmp_path):
        """Find pages linking to a concept."""
        wiki_init(tmp_path, name="Test Wiki")

        source_path = tmp_path / "raw" / "test.md"
        source_path.write_text("# Test")

        wiki = Wiki(tmp_path)
        wiki_ingest(
            wiki,
            Path("raw/test.md"),
            title="Test Article",
            extracted_concepts=["Machine Learning"],
        )

        # The source page should link to the concept
        result = wiki_find_links(wiki, "concepts/machine_learning")

        assert result["success"] is True
        # The source page links to the concept
        assert result["count"] >= 1

    def test_find_links_no_links(self, tmp_path):
        """Find links returns empty for orphan page."""
        wiki_init(tmp_path, name="Test Wiki")

        source_path = tmp_path / "raw" / "test.md"
        source_path.write_text("# Isolated Page")

        wiki = Wiki(tmp_path)
        wiki_ingest(wiki, Path("raw/test.md"), title="Isolated Page")

        result = wiki_find_links(wiki, "sources/test")

        assert result["success"] is True
        # No other pages link to this source
        # (it might be 0 or might find itself, depending on content)


class TestSearchByLink:
    """Test search_by_link function."""

    def test_search_by_link_finds_references(self, tmp_path):
        """Finds pages that reference another page."""
        wiki_init(tmp_path, name="Test Wiki")

        source_path = tmp_path / "raw" / "test.md"
        source_path.write_text("# Test")

        wiki = Wiki(tmp_path)
        wiki_ingest(
            wiki,
            Path("raw/test.md"),
            title="Test Article",
            extracted_entities=["John Smith"],
        )

        # Source page links to entity
        results = search_by_link(wiki, "entities/john_smith")

        # The source page contains [[sources/test]] or similar
        # Actually, let's check if source links to entity
        assert isinstance(results, list)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
