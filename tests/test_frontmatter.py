"""Unit tests for frontmatter module.

Tests all functions in llm_wiki.frontmatter:
- parse_page, write_page
- compute_content_hash, compute_file_hash
- update_frontmatter, get_frontmatter, get_content
- validate_frontmatter, extract_wikilinks
- normalize_page_id, page_id_to_path, path_to_page_id
"""

import tempfile
from pathlib import Path
import pytest

from llm_wiki.frontmatter import (
    parse_page,
    write_page,
    compute_content_hash,
    compute_file_hash,
    update_frontmatter,
    get_frontmatter,
    get_content,
    validate_frontmatter,
    extract_wikilinks,
    normalize_page_id,
    page_id_to_path,
    path_to_page_id,
)


class TestParsePage:
    """Test parse_page function."""

    def test_parse_simple_page(self, tmp_path):
        """Parse page with simple frontmatter."""
        page_path = tmp_path / "test.md"
        page_path.write_text("""---
title: Test Page
page_type: concept
---

# Test Page

This is the content.
""")

        metadata, content = parse_page(page_path)

        assert metadata["title"] == "Test Page"
        assert metadata["page_type"] == "concept"
        assert "# Test Page" in content
        assert "This is the content." in content

    def test_parse_page_with_lists(self, tmp_path):
        """Parse page with list values in frontmatter."""
        page_path = tmp_path / "test.md"
        page_path.write_text("""---
title: Test
tags:
  - tag1
  - tag2
  - tag3
sources:
  - source1
  - source2
---

Content here.
""")

        metadata, content = parse_page(page_path)

        assert metadata["tags"] == ["tag1", "tag2", "tag3"]
        assert metadata["sources"] == ["source1", "source2"]

    def test_parse_page_with_nested_dict(self, tmp_path):
        """Parse page with nested dict in frontmatter."""
        page_path = tmp_path / "test.md"
        page_path.write_text("""---
title: Test
metadata:
  created_by: user
  version: 1.0
---

Content.
""")

        metadata, content = parse_page(page_path)

        assert metadata["metadata"]["created_by"] == "user"
        assert metadata["metadata"]["version"] == 1.0

    def test_parse_page_empty_frontmatter(self, tmp_path):
        """Parse page with empty frontmatter."""
        page_path = tmp_path / "test.md"
        page_path.write_text("""---
---

Just content.
""")

        metadata, content = parse_page(page_path)

        assert metadata == {}
        assert "Just content." in content

    def test_parse_page_no_frontmatter(self, tmp_path):
        """Parse page without frontmatter."""
        page_path = tmp_path / "test.md"
        page_path.write_text("# Just Content\n\nNo frontmatter here.")

        metadata, content = parse_page(page_path)

        assert metadata == {}
        assert "# Just Content" in content

    def test_parse_page_nonexistent(self, tmp_path):
        """Parse nonexistent page raises error."""
        with pytest.raises(FileNotFoundError):
            parse_page(tmp_path / "nonexistent.md")

    def test_parse_page_unicode(self, tmp_path):
        """Parse page with unicode characters."""
        page_path = tmp_path / "test.md"
        page_path.write_text("""---
title: ""
author: Caf
---

Content with unicode:
""", encoding="utf-8")

        metadata, content = parse_page(page_path)

        assert "" in metadata["title"]
        assert "Caf" in metadata["author"]
        assert "" in content


class TestWritePage:
    """Test write_page function."""

    def test_write_simple_page(self, tmp_path):
        """Write page with simple metadata."""
        page_path = tmp_path / "test.md"

        metadata = {"title": "Test", "page_type": "concept"}
        content = "# Test\n\nThis is content."

        content_hash = write_page(page_path, metadata, content)

        assert page_path.exists()
        assert content_hash.startswith("sha256:")

        # Read back
        text = page_path.read_text()
        assert "title: Test" in text
        assert "# Test" in text

    def test_write_creates_parent_dirs(self, tmp_path):
        """write_page creates parent directories."""
        page_path = tmp_path / "a" / "b" / "c" / "test.md"

        write_page(page_path, {"title": "Test"}, "Content")

        assert page_path.exists()
        assert page_path.parent.exists()

    def test_write_page_atomic(self, tmp_path):
        """Write uses atomic operation by default."""
        page_path = tmp_path / "test.md"

        write_page(page_path, {"title": "Test"}, "Content", atomic=True)

        # Should not have .tmp file remaining
        assert not (tmp_path / "test.md.tmp").exists()
        assert page_path.exists()

    def test_write_page_non_atomic(self, tmp_path):
        """Write can skip atomic operation."""
        page_path = tmp_path / "test.md"

        write_page(page_path, {"title": "Test"}, "Content", atomic=False)

        assert page_path.exists()

    def test_write_page_returns_content_hash(self, tmp_path):
        """write_page returns hash of content only."""
        page_path = tmp_path / "test.md"
        content = "Test content"

        hash_val = write_page(page_path, {"title": "Test"}, content)
        expected_hash = compute_content_hash(content)

        assert hash_val == expected_hash

    def test_write_overwrites_existing(self, tmp_path):
        """write_page overwrites existing file."""
        page_path = tmp_path / "test.md"
        page_path.write_text("old content")

        write_page(page_path, {"title": "New"}, "New content")

        text = page_path.read_text()
        assert "New content" in text
        assert "old content" not in text


class TestComputeContentHash:
    """Test compute_content_hash function."""

    def test_hash_format(self):
        """Hash has correct format."""
        hash_val = compute_content_hash("test")
        assert hash_val.startswith("sha256:")
        assert len(hash_val) == 7 + 64

    def test_hash_deterministic(self):
        """Same content gives same hash."""
        content = "Test content here"
        h1 = compute_content_hash(content)
        h2 = compute_content_hash(content)
        assert h1 == h2

    def test_hash_different_content(self):
        """Different content gives different hash."""
        h1 = compute_content_hash("content a")
        h2 = compute_content_hash("content b")
        assert h1 != h2

    def test_hash_empty(self):
        """Empty string has known hash."""
        h = compute_content_hash("")
        assert h == "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"


class TestComputeFileHash:
    """Test compute_file_hash function."""

    def test_file_hash_format(self, tmp_path):
        """File hash has correct format."""
        file_path = tmp_path / "test.txt"
        file_path.write_text("content")

        hash_val = compute_file_hash(file_path)
        assert hash_val.startswith("sha256:")
        assert len(hash_val) == 7 + 64

    def test_file_hash_matches_content_hash(self, tmp_path):
        """File hash matches content hash for text files."""
        file_path = tmp_path / "test.txt"
        content = "test content"
        file_path.write_text(content)

        file_hash = compute_file_hash(file_path)
        content_hash = compute_content_hash(content)

        assert file_hash == content_hash

    def test_file_hash_binary(self, tmp_path):
        """File hash works for binary files."""
        file_path = tmp_path / "test.bin"
        file_path.write_bytes(b"\x00\x01\x02\x03")

        hash_val = compute_file_hash(file_path)
        assert hash_val.startswith("sha256:")

    def test_file_hash_large_file(self, tmp_path):
        """File hash works for large files."""
        file_path = tmp_path / "large.txt"
        # Write ~1MB of data
        file_path.write_text("x" * 1000000)

        hash_val = compute_file_hash(file_path)
        assert hash_val.startswith("sha256:")


class TestUpdateFrontmatter:
    """Test update_frontmatter function."""

    def test_update_existing_field(self, tmp_path):
        """Update existing frontmatter field."""
        page_path = tmp_path / "test.md"
        page_path.write_text("""---
title: Original
version: 1
---

Content.
""")

        update_frontmatter(page_path, {"title": "Updated"})

        metadata, _ = parse_page(page_path)
        assert metadata["title"] == "Updated"
        assert metadata["version"] == 1

    def test_update_add_new_field(self, tmp_path):
        """Add new frontmatter field."""
        page_path = tmp_path / "test.md"
        page_path.write_text("""---
title: Test
---

Content.
""")

        update_frontmatter(page_path, {"new_field": "new_value"})

        metadata, _ = parse_page(page_path)
        assert metadata["title"] == "Test"
        assert metadata["new_field"] == "new_value"

    def test_update_preserves_content(self, tmp_path):
        """Update preserves content unchanged."""
        page_path = tmp_path / "test.md"
        original_content = "# Test\n\nImportant content."
        page_path.write_text(f"""---
title: Test
---

{original_content}
""")

        update_frontmatter(page_path, {"title": "Updated"})

        _, content = parse_page(page_path)
        assert "Important content." in content


class TestGetFrontmatter:
    """Test get_frontmatter function."""

    def test_get_frontmatter_only(self, tmp_path):
        """Get only frontmatter dict."""
        page_path = tmp_path / "test.md"
        page_path.write_text("""---
title: Test
tags: [a, b]
---

Content.
""")

        metadata = get_frontmatter(page_path)

        assert metadata["title"] == "Test"
        assert metadata["tags"] == ["a", "b"]


class TestGetContent:
    """Test get_content function."""

    def test_get_content_only(self, tmp_path):
        """Get only content string."""
        page_path = tmp_path / "test.md"
        page_path.write_text("""---
title: Test
---

# Heading

Body text.
""")

        content = get_content(page_path)

        assert "# Heading" in content
        assert "Body text." in content
        assert "title: Test" not in content


class TestValidateFrontmatter:
    """Test validate_frontmatter function."""

    def test_validate_all_present(self):
        """Validate returns empty list when all fields present."""
        metadata = {"title": "Test", "page_id": "test", "page_type": "concept"}
        missing = validate_frontmatter(metadata, ["title", "page_id", "page_type"])
        assert missing == []

    def test_validate_some_missing(self):
        """Validate returns missing field names."""
        metadata = {"title": "Test"}
        missing = validate_frontmatter(metadata, ["title", "page_id", "page_type"])
        assert "page_id" in missing
        assert "page_type" in missing
        assert "title" not in missing

    def test_validate_none_value_is_missing(self):
        """Validate treats None values as missing."""
        metadata = {"title": "Test", "page_id": None}
        missing = validate_frontmatter(metadata, ["title", "page_id"])
        assert "page_id" in missing

    def test_validate_empty_required(self):
        """Validate with empty required list."""
        metadata = {"title": "Test"}
        missing = validate_frontmatter(metadata, [])
        assert missing == []


class TestExtractWikilinks:
    """Test extract_wikilinks function."""

    def test_extract_simple_links(self):
        """Extract simple wikilinks."""
        content = "See [[Page A]] and [[Page B]] for details."
        links = extract_wikilinks(content)
        assert links == ["Page A", "Page B"]

    def test_extract_links_with_display_text(self):
        """Extract links with display text (pipetrick)."""
        content = "See [[Page A|Display Text]] for details."
        links = extract_wikilinks(content)
        assert links == ["Page A"]
        assert "Display Text" not in links

    def test_extract_mixed_links(self):
        """Extract mix of simple and piped links."""
        content = "[[Simple Link]] and [[Complex|Display]] and [[Another]]."
        links = extract_wikilinks(content)
        assert "Simple Link" in links
        assert "Complex" in links
        assert "Another" in links

    def test_extract_no_links(self):
        """Extract from content with no links."""
        content = "No wikilinks here, just [regular](markdown) links."
        links = extract_wikilinks(content)
        assert links == []

    def test_extract_multiline(self):
        """Extract links across multiple lines."""
        content = """First [[Link A]].
Second [[Link B]].
Third [[Link C]]."""
        links = extract_wikilinks(content)
        assert len(links) == 3

    def test_extract_duplicate_links(self):
        """Extract handles duplicate links."""
        content = "[[Same Page]] and [[Same Page]] again."
        links = extract_wikilinks(content)
        # Returns all occurrences
        assert links == ["Same Page", "Same Page"]

    def test_extract_nested_brackets(self):
        """Extract handles edge case with extra brackets."""
        content = "[[Valid Link]]"
        links = extract_wikilinks(content)
        assert links == ["Valid Link"]


class TestNormalizePageId:
    """Test normalize_page_id function."""

    def test_normalize_simple(self):
        """Normalize simple title."""
        assert normalize_page_id("Machine Learning") == "machine_learning"

    def test_normalize_hyphens(self):
        """Normalize title with hyphens."""
        assert normalize_page_id("Deep-Learning") == "deep_learning"

    def test_normalize_special_chars(self):
        """Normalize title with special characters."""
        assert normalize_page_id("What's 'this'?") == "whats_this"

    def test_normalize_multiple_spaces(self):
        """Normalize title with multiple spaces."""
        assert normalize_page_id("Multiple   Spaces") == "multiple_spaces"

    def test_normalize_leading_trailing(self):
        """Normalize title with leading/trailing spaces."""
        assert normalize_page_id("  Trimmed  ") == "trimmed"

    def test_normalize_numbers(self):
        """Normalize title with numbers."""
        assert normalize_page_id("Model 123") == "model_123"

    def test_normalize_unicode(self):
        """Normalize title with unicode."""
        # Non-ASCII characters are removed
        result = normalize_page_id("Caf")
        assert "caf" in result.lower()

    def test_normalize_empty_after_strip(self):
        """Normalize title that becomes empty."""
        result = normalize_page_id("   ")
        assert result == ""


class TestPageIdToPath:
    """Test page_id_to_path function."""

    def test_simple_page_id(self, tmp_path):
        """Convert simple page_id to path."""
        wiki_dir = tmp_path / "wiki"
        path = page_id_to_path("concepts/machine_learning", wiki_dir)
        assert path == wiki_dir / "concepts" / "machine_learning.md"

    def test_nested_page_id(self, tmp_path):
        """Convert nested page_id to path."""
        wiki_dir = tmp_path / "wiki"
        path = page_id_to_path("sources/papers/paper1", wiki_dir)
        assert path == wiki_dir / "sources" / "papers" / "paper1.md"


class TestPathToPageId:
    """Test path_to_page_id function."""

    def test_simple_path(self, tmp_path):
        """Convert simple path to page_id."""
        wiki_dir = tmp_path / "wiki"
        file_path = wiki_dir / "concepts" / "machine_learning.md"
        page_id = path_to_page_id(file_path, wiki_dir)
        assert page_id == "concepts/machine_learning"

    def test_nested_path(self, tmp_path):
        """Convert nested path to page_id."""
        wiki_dir = tmp_path / "wiki"
        file_path = wiki_dir / "sources" / "papers" / "paper1.md"
        page_id = path_to_page_id(file_path, wiki_dir)
        assert page_id == "sources/papers/paper1"


class TestRoundtrip:
    """Test roundtrip conversions."""

    def test_write_parse_roundtrip(self, tmp_path):
        """Write and parse produces same metadata and content."""
        page_path = tmp_path / "test.md"

        original_metadata = {
            "title": "Test Page",
            "page_type": "concept",
            "tags": ["a", "b"],
            "number": 42,
        }
        original_content = "# Test\n\nContent here."

        write_page(page_path, original_metadata, original_content)
        metadata, content = parse_page(page_path)

        assert metadata["title"] == original_metadata["title"]
        assert metadata["page_type"] == original_metadata["page_type"]
        assert metadata["tags"] == original_metadata["tags"]
        assert metadata["number"] == original_metadata["number"]
        assert original_content.strip() == content.strip()

    def test_page_id_path_roundtrip(self, tmp_path):
        """page_id -> path -> page_id preserves value."""
        wiki_dir = tmp_path / "wiki"
        original_id = "concepts/machine_learning"

        path = page_id_to_path(original_id, wiki_dir)
        restored_id = path_to_page_id(path, wiki_dir)

        assert restored_id == original_id


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_parse_file_with_only_dashes(self, tmp_path):
        """Parse file that looks like it might have frontmatter."""
        page_path = tmp_path / "test.md"
        page_path.write_text("---\nThis is just a horizontal rule, not frontmatter.")

        # This should handle gracefully
        metadata, content = parse_page(page_path)
        # Behavior depends on frontmatter library

    def test_write_page_empty_content(self, tmp_path):
        """Write page with empty content."""
        page_path = tmp_path / "test.md"
        write_page(page_path, {"title": "Empty"}, "")

        _, content = parse_page(page_path)
        assert content.strip() == ""

    def test_write_page_empty_metadata(self, tmp_path):
        """Write page with empty metadata."""
        page_path = tmp_path / "test.md"
        write_page(page_path, {}, "Content only")

        metadata, content = parse_page(page_path)
        assert metadata == {}
        assert "Content only" in content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
