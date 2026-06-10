"""Frontmatter parsing and writing utilities for LLM Wiki.

This module re-exports from llm_wiki.io for backward compatibility.
New code should import directly from llm_wiki.io submodules.

Handles reading and writing YAML frontmatter in markdown files.
Uses python-frontmatter library for parsing.
"""

# Re-export from io package for backward compatibility
from .io.hashing import compute_content_hash, compute_file_hash
from .io.wikilinks import (
    extract_wikilinks,
    normalize_page_id,
    page_id_to_path,
    path_to_page_id,
)
from .io.page_io import (
    parse_page,
    write_page,
    update_frontmatter,
    get_frontmatter,
    get_content,
    validate_frontmatter,
)
from .io.dedup import (
    DuplicateCheckResult,
    compute_source_content_hash,
    get_existing_sources_hashes,
    get_source_by_slug,
    check_duplicate,
    format_duplicate_result,
)

__all__ = [
    # Hashing (from io.hashing)
    "compute_content_hash",
    "compute_file_hash",
    # Wikilinks (from io.wikilinks)
    "extract_wikilinks",
    "normalize_page_id",
    "page_id_to_path",
    "path_to_page_id",
    # Page I/O (from io.page_io)
    "parse_page",
    "write_page",
    "update_frontmatter",
    "get_frontmatter",
    "get_content",
    "validate_frontmatter",
    # Duplicate Detection (from io.dedup)
    "DuplicateCheckResult",
    "compute_source_content_hash",
    "get_existing_sources_hashes",
    "get_source_by_slug",
    "check_duplicate",
    "format_duplicate_result",
]
