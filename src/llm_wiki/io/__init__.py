"""I/O utilities for LLM Wiki.

This package provides file operations:
- hashing: SHA-256 content and file hashing
- wikilinks: Wikilink extraction and page ID normalization
- page_io: Markdown page parsing and writing with YAML frontmatter
- dedup: Duplicate detection for source ingestion
"""

from .hashing import compute_content_hash, compute_file_hash
from .wikilinks import (
    extract_wikilinks,
    normalize_page_id,
    page_id_to_path,
    path_to_page_id,
)
from .page_io import (
    parse_page,
    write_page,
    update_frontmatter,
    get_frontmatter,
    get_content,
    validate_frontmatter,
)
from .dedup import (
    DuplicateCheckResult,
    compute_source_content_hash,
    get_existing_sources_hashes,
    get_source_by_slug,
    check_duplicate,
    format_duplicate_result,
)

__all__ = [
    # Hashing
    "compute_content_hash",
    "compute_file_hash",
    # Wikilinks
    "extract_wikilinks",
    "normalize_page_id",
    "page_id_to_path",
    "path_to_page_id",
    # Page I/O
    "parse_page",
    "write_page",
    "update_frontmatter",
    "get_frontmatter",
    "get_content",
    "validate_frontmatter",
    # Duplicate Detection
    "DuplicateCheckResult",
    "compute_source_content_hash",
    "get_existing_sources_hashes",
    "get_source_by_slug",
    "check_duplicate",
    "format_duplicate_result",
]
