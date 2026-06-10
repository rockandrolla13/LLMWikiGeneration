"""Unit tests for duplicate detection module.

Tests all functions in llm_wiki.io.dedup:
- compute_source_content_hash
- get_existing_sources_hashes
- get_source_by_slug
- check_duplicate
- format_duplicate_result
"""

import pytest
from pathlib import Path

from llm_wiki.io.dedup import (
    DuplicateCheckResult,
    compute_source_content_hash,
    get_existing_sources_hashes,
    get_source_by_slug,
    check_duplicate,
    format_duplicate_result,
)
from llm_wiki.io.page_io import write_page


class TestComputeSourceContentHash:
    """Test compute_source_content_hash function."""

    def test_hash_format(self):
        """Hash has correct format."""
        hash_val = compute_source_content_hash("test content")
        assert hash_val.startswith("sha256:")
        assert len(hash_val) == 7 + 64  # "sha256:" + 64 hex chars

    def test_hash_deterministic(self):
        """Same content gives same hash."""
        content = "This is a test document about machine learning."
        h1 = compute_source_content_hash(content)
        h2 = compute_source_content_hash(content)
        assert h1 == h2

    def test_hash_different_content(self):
        """Different content gives different hash."""
        h1 = compute_source_content_hash("Document A")
        h2 = compute_source_content_hash("Document B")
        assert h1 != h2

    def test_hash_whitespace_sensitive(self):
        """Hash is sensitive to whitespace."""
        h1 = compute_source_content_hash("Hello World")
        h2 = compute_source_content_hash("Hello  World")
        assert h1 != h2


class TestGetExistingSourcesHashes:
    """Test get_existing_sources_hashes function."""

    def test_empty_directory(self, tmp_path):
        """Returns empty dict for empty directory."""
        sources_dir = tmp_path / "sources"
        sources_dir.mkdir()

        result = get_existing_sources_hashes(sources_dir)
        assert result == {}

    def test_nonexistent_directory(self, tmp_path):
        """Returns empty dict for nonexistent directory."""
        result = get_existing_sources_hashes(tmp_path / "nonexistent")
        assert result == {}

    def test_source_with_hash(self, tmp_path):
        """Extracts hash from source with content_hash field."""
        sources_dir = tmp_path / "sources"
        sources_dir.mkdir()

        test_hash = "sha256:abc123def456"
        metadata = {
            "title": "Test Source",
            "page_type": "source",
            "content_hash": test_hash,
        }
        write_page(sources_dir / "test-source.md", metadata, "Content here")

        result = get_existing_sources_hashes(sources_dir)

        assert test_hash in result
        assert result[test_hash][0] == sources_dir / "test-source.md"
        assert result[test_hash][1] == "test-source"

    def test_source_without_hash(self, tmp_path):
        """Skips sources without content_hash field."""
        sources_dir = tmp_path / "sources"
        sources_dir.mkdir()

        metadata = {
            "title": "Test Source",
            "page_type": "source",
            # No content_hash field
        }
        write_page(sources_dir / "test-source.md", metadata, "Content here")

        result = get_existing_sources_hashes(sources_dir)
        assert result == {}

    def test_multiple_sources(self, tmp_path):
        """Extracts hashes from multiple sources."""
        sources_dir = tmp_path / "sources"
        sources_dir.mkdir()

        for i in range(3):
            hash_val = f"sha256:hash{i}"
            metadata = {
                "title": f"Source {i}",
                "content_hash": hash_val,
            }
            write_page(sources_dir / f"source-{i}.md", metadata, f"Content {i}")

        result = get_existing_sources_hashes(sources_dir)

        assert len(result) == 3
        assert "sha256:hash0" in result
        assert "sha256:hash1" in result
        assert "sha256:hash2" in result


class TestGetSourceBySlug:
    """Test get_source_by_slug function."""

    def test_existing_source(self, tmp_path):
        """Returns path for existing source."""
        sources_dir = tmp_path / "sources"
        sources_dir.mkdir()
        source_path = sources_dir / "my-source.md"
        source_path.write_text("# Test")

        result = get_source_by_slug(sources_dir, "my-source")
        assert result == source_path

    def test_nonexistent_source(self, tmp_path):
        """Returns None for nonexistent source."""
        sources_dir = tmp_path / "sources"
        sources_dir.mkdir()

        result = get_source_by_slug(sources_dir, "nonexistent")
        assert result is None


class TestCheckDuplicate:
    """Test check_duplicate function."""

    def test_new_source(self, tmp_path):
        """Detects new source (no match)."""
        sources_dir = tmp_path / "sources"
        sources_dir.mkdir()

        result = check_duplicate(
            sources_dir,
            content="Brand new content",
            slug="new-source",
        )

        assert not result.is_duplicate
        assert not result.is_update
        assert result.existing_path is None
        assert result.new_hash.startswith("sha256:")

    def test_duplicate_by_hash(self, tmp_path):
        """Detects duplicate by content hash."""
        sources_dir = tmp_path / "sources"
        sources_dir.mkdir()

        content = "This is the original content."
        content_hash = compute_source_content_hash(content)

        metadata = {
            "title": "Original Source",
            "content_hash": content_hash,
        }
        write_page(sources_dir / "original.md", metadata, "Wiki page content")

        result = check_duplicate(
            sources_dir,
            content=content,  # Same content
            slug="different-slug",  # Different slug
        )

        assert result.is_duplicate
        assert not result.is_update
        assert result.existing_path == sources_dir / "original.md"
        assert result.existing_hash == content_hash
        assert result.new_hash == content_hash

    def test_update_same_slug_different_content(self, tmp_path):
        """Detects update (same slug, different content)."""
        sources_dir = tmp_path / "sources"
        sources_dir.mkdir()

        old_content = "Original content"
        old_hash = compute_source_content_hash(old_content)

        metadata = {
            "title": "My Source",
            "content_hash": old_hash,
        }
        write_page(sources_dir / "my-source.md", metadata, "Wiki content")

        new_content = "Updated content with changes"
        result = check_duplicate(
            sources_dir,
            content=new_content,
            slug="my-source",  # Same slug
        )

        assert not result.is_duplicate
        assert result.is_update
        assert result.existing_path == sources_dir / "my-source.md"
        assert result.existing_hash == old_hash
        assert result.new_hash != old_hash

    def test_same_slug_same_content(self, tmp_path):
        """Same slug and content is a duplicate."""
        sources_dir = tmp_path / "sources"
        sources_dir.mkdir()

        content = "Same content"
        content_hash = compute_source_content_hash(content)

        metadata = {
            "title": "My Source",
            "content_hash": content_hash,
        }
        write_page(sources_dir / "my-source.md", metadata, "Wiki content")

        result = check_duplicate(
            sources_dir,
            content=content,
            slug="my-source",
        )

        # Should be detected as duplicate (by hash), not update
        assert result.is_duplicate
        assert not result.is_update


class TestFormatDuplicateResult:
    """Test format_duplicate_result function."""

    def test_format_new(self):
        """Format new source result."""
        result = DuplicateCheckResult(
            is_duplicate=False,
            is_update=False,
            existing_path=None,
            existing_hash=None,
            new_hash="sha256:abc123",
        )

        formatted = format_duplicate_result(result)

        assert formatted["status"] == "new"
        assert formatted["content_hash"] == "sha256:abc123"

    def test_format_duplicate(self, tmp_path):
        """Format duplicate result."""
        existing = tmp_path / "existing.md"
        result = DuplicateCheckResult(
            is_duplicate=True,
            is_update=False,
            existing_path=existing,
            existing_hash="sha256:abc123",
            new_hash="sha256:abc123",
        )

        formatted = format_duplicate_result(result)

        assert formatted["status"] == "skipped"
        assert formatted["reason"] == "duplicate"
        assert formatted["existing"] == str(existing)
        assert formatted["content_hash"] == "sha256:abc123"

    def test_format_update(self, tmp_path):
        """Format update result."""
        existing = tmp_path / "existing.md"
        result = DuplicateCheckResult(
            is_duplicate=False,
            is_update=True,
            existing_path=existing,
            existing_hash="sha256:old123",
            new_hash="sha256:new456",
        )

        formatted = format_duplicate_result(result)

        assert formatted["status"] == "update"
        assert formatted["reason"] == "content_changed"
        assert formatted["existing"] == str(existing)
        assert formatted["old_hash"] == "sha256:old123"
        assert formatted["new_hash"] == "sha256:new456"


class TestDuplicateCheckResult:
    """Test DuplicateCheckResult dataclass."""

    def test_create_result(self):
        """Create result with all fields."""
        result = DuplicateCheckResult(
            is_duplicate=True,
            is_update=False,
            existing_path=Path("/test/path.md"),
            existing_hash="sha256:abc",
            new_hash="sha256:xyz",
        )

        assert result.is_duplicate is True
        assert result.is_update is False
        assert result.existing_path == Path("/test/path.md")
        assert result.existing_hash == "sha256:abc"
        assert result.new_hash == "sha256:xyz"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
