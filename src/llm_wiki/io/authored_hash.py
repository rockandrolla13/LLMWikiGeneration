"""Authored-region hashing utilities for LLM Wiki.

Provides functions to extract, hash, and wrap the authored region of wiki pages.
The authored region is the human/LLM-written prose section delimited by HTML
comment markers. Only this region is hashed for content_hash tracking (P4).

Inverse edges and computed fields are excluded from the hash so that graph
operations do not thrash the authored-region hash.
"""

import hashlib
import re
from typing import Optional

_START_MARKER = "<!-- AUTHORED REGION START -->"
_END_MARKER = "<!-- AUTHORED REGION END -->"

_REGION_RE = re.compile(
    r"<!-- AUTHORED REGION START -->(.*?)<!-- AUTHORED REGION END -->",
    re.DOTALL,
)


def extract_authored_region(content: str) -> Optional[str]:
    """Extract the text between authored region markers.

    Args:
        content: Full page content (frontmatter already stripped, or full file).

    Returns:
        The text between the markers (including any leading/trailing whitespace
        inside the markers), or None if no markers are found.
    """
    match = _REGION_RE.search(content)
    if match is None:
        return None
    return match.group(1)


def compute_authored_hash(content: str) -> str:
    """Compute a stable SHA-256 hash for the authored region of a page.

    If authored-region markers are present, hashes only the text between them.
    Falls back to hashing the full content when markers are absent (pre-P9 pages).

    Args:
        content: Full page content string.

    Returns:
        String of the form "sha256:<hex_digest>".
    """
    region = extract_authored_region(content)
    text = region if region is not None else content
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def wrap_authored_region(prose: str) -> str:
    """Wrap prose in authored-region markers.

    Args:
        prose: The human/LLM-written body text to protect from hash thrash.

    Returns:
        The prose wrapped in START/END comment markers, with a surrounding
        newline on each side for clean markdown rendering.
    """
    return f"{_START_MARKER}\n{prose}\n{_END_MARKER}"
