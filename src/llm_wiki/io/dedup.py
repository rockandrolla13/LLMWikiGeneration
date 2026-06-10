"""Duplicate detection utilities for LLM Wiki.

Provides SHA-256 based idempotency for source ingestion.
Detects duplicate sources by content hash to enable safe re-runs.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .hashing import compute_content_hash
from .page_io import get_frontmatter


@dataclass
class DuplicateCheckResult:
    """Result of a duplicate check.

    Attributes:
        is_duplicate: True if content hash matches an existing source
        is_update: True if slug matches but content differs (content changed)
        existing_path: Path to the existing source file if found
        existing_hash: Content hash of the existing source
        new_hash: Content hash of the new content
    """

    is_duplicate: bool
    is_update: bool
    existing_path: Optional[Path]
    existing_hash: Optional[str]
    new_hash: str


def compute_source_content_hash(content: str) -> str:
    """Compute content hash for a source document.

    This is the hash stored in the frontmatter `content_hash` field.
    It hashes the raw source content (the markdown being ingested),
    not the wiki page content.

    Args:
        content: Source document content (markdown text)

    Returns:
        Hash string in format "sha256:hexdigest"
    """
    return compute_content_hash(content)


def get_existing_sources_hashes(wiki_sources_dir: Path) -> dict[str, tuple[Path, str]]:
    """Scan existing source pages and extract content hashes.

    Args:
        wiki_sources_dir: Path to wiki/sources/ directory

    Returns:
        Dictionary mapping content_hash -> (file_path, page_slug)
        Only includes sources that have content_hash in frontmatter.
    """
    hashes: dict[str, tuple[Path, str]] = {}

    if not wiki_sources_dir.exists():
        return hashes

    for source_file in wiki_sources_dir.glob("*.md"):
        try:
            metadata = get_frontmatter(source_file)
            content_hash = metadata.get("content_hash")
            if content_hash:
                slug = source_file.stem
                hashes[content_hash] = (source_file, slug)
        except Exception:
            # Skip files that can't be parsed
            continue

    return hashes


def get_source_by_slug(wiki_sources_dir: Path, slug: str) -> Optional[Path]:
    """Find a source page by its slug.

    Args:
        wiki_sources_dir: Path to wiki/sources/ directory
        slug: Source page slug (filename without .md)

    Returns:
        Path to the source file if found, None otherwise
    """
    source_path = wiki_sources_dir / f"{slug}.md"
    return source_path if source_path.exists() else None


def check_duplicate(
    wiki_sources_dir: Path,
    content: str,
    slug: str,
) -> DuplicateCheckResult:
    """Check if a source document is a duplicate.

    Compares the content hash against existing sources to detect:
    1. Exact duplicates (same content hash)
    2. Updates (same slug, different content)
    3. New sources (no match)

    Args:
        wiki_sources_dir: Path to wiki/sources/ directory
        content: Source document content to check
        slug: Proposed slug for the new source

    Returns:
        DuplicateCheckResult with detection status and details
    """
    new_hash = compute_source_content_hash(content)

    # Check for exact content match (duplicate)
    existing_hashes = get_existing_sources_hashes(wiki_sources_dir)
    if new_hash in existing_hashes:
        existing_path, existing_slug = existing_hashes[new_hash]
        return DuplicateCheckResult(
            is_duplicate=True,
            is_update=False,
            existing_path=existing_path,
            existing_hash=new_hash,
            new_hash=new_hash,
        )

    # Check for slug match with different content (update)
    existing_by_slug = get_source_by_slug(wiki_sources_dir, slug)
    if existing_by_slug:
        try:
            existing_metadata = get_frontmatter(existing_by_slug)
            existing_hash = existing_metadata.get("content_hash")
            if existing_hash and existing_hash != new_hash:
                return DuplicateCheckResult(
                    is_duplicate=False,
                    is_update=True,
                    existing_path=existing_by_slug,
                    existing_hash=existing_hash,
                    new_hash=new_hash,
                )
        except Exception:
            pass

    # New source (no match)
    return DuplicateCheckResult(
        is_duplicate=False,
        is_update=False,
        existing_path=None,
        existing_hash=None,
        new_hash=new_hash,
    )


def format_duplicate_result(result: DuplicateCheckResult) -> dict:
    """Format a duplicate check result as a dictionary for API responses.

    Args:
        result: DuplicateCheckResult to format

    Returns:
        Dictionary with status and details
    """
    if result.is_duplicate:
        return {
            "status": "skipped",
            "reason": "duplicate",
            "existing": str(result.existing_path) if result.existing_path else None,
            "content_hash": result.new_hash,
        }
    elif result.is_update:
        return {
            "status": "update",
            "reason": "content_changed",
            "existing": str(result.existing_path) if result.existing_path else None,
            "old_hash": result.existing_hash,
            "new_hash": result.new_hash,
        }
    else:
        return {
            "status": "new",
            "content_hash": result.new_hash,
        }
