"""Wikilink extraction and page ID utilities for LLM Wiki.

Provides functions for:
- Extracting [[wikilinks]] from markdown content
- Normalizing page titles to page IDs
- Converting between page IDs and file paths
"""

import re
from pathlib import Path


# Regex pattern for wikilinks: [[link]] or [[link|display text]]
_WIKILINK_PATTERN = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def extract_wikilinks(content: str) -> list[str]:
    """Extract all wikilinks from markdown content.

    Wikilinks are in the format [[Page Name]] or [[Page Name|display text]].

    Args:
        content: Markdown content

    Returns:
        List of linked page names (without display text)
    """
    return _WIKILINK_PATTERN.findall(content)


def normalize_page_id(title: str) -> str:
    """Convert a page title to a normalized page_id.

    Transformation:
    - Convert to lowercase
    - Replace spaces and hyphens with underscores
    - Remove non-alphanumeric characters (except underscores)
    - Collapse multiple underscores
    - Strip leading/trailing underscores

    Args:
        title: Page title (e.g., "Machine Learning")

    Returns:
        Normalized page_id (e.g., "machine_learning")
    """
    # Convert to lowercase
    page_id = title.lower()
    # Replace spaces and hyphens with underscores
    page_id = re.sub(r"[\s-]+", "_", page_id)
    # Remove any non-alphanumeric characters except underscores
    page_id = re.sub(r"[^\w]", "", page_id)
    # Collapse multiple underscores
    page_id = re.sub(r"_+", "_", page_id)
    # Strip leading/trailing underscores
    page_id = page_id.strip("_")
    return page_id


def page_id_to_path(page_id: str, wiki_dir: Path) -> Path:
    """Convert a page_id to its file path.

    Args:
        page_id: Page ID (e.g., "concepts/machine_learning")
        wiki_dir: Path to wiki directory

    Returns:
        Full path to the page file
    """
    return wiki_dir / f"{page_id}.md"


def path_to_page_id(file_path: Path, wiki_dir: Path) -> str:
    """Convert a file path to its page_id.

    Args:
        file_path: Full path to page file
        wiki_dir: Path to wiki directory

    Returns:
        Page ID (e.g., "concepts/machine_learning")
    """
    rel_path = file_path.relative_to(wiki_dir)
    # Remove .md extension
    page_id = str(rel_path.with_suffix(""))
    return page_id
