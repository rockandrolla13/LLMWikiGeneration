"""I/O utilities for LLM Wiki.

This package provides file operations:
- hashing: SHA-256 content and file hashing
- wikilinks: Wikilink extraction and page ID normalization
- page_io: Markdown page parsing and writing with YAML frontmatter
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
]
