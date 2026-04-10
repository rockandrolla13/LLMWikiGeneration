"""SHA-256 hashing utilities for LLM Wiki.

Provides content and file hashing for revision tracking.
All hashes are returned in the format "sha256:<hexdigest>".
"""

import hashlib
from pathlib import Path


def compute_content_hash(content: str) -> str:
    """Compute SHA-256 hash of content.

    Args:
        content: String content to hash

    Returns:
        Hash string in format "sha256:hexdigest"
    """
    digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def compute_file_hash(file_path: Path) -> str:
    """Compute SHA-256 hash of a file.

    Reads the file in chunks to handle large files efficiently.

    Args:
        file_path: Path to the file

    Returns:
        Hash string in format "sha256:hexdigest"
    """
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return f"sha256:{h.hexdigest()}"
