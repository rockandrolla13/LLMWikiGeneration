"""Page I/O utilities for LLM Wiki.

Handles reading and writing YAML frontmatter in markdown files.
Uses python-frontmatter library for parsing.
"""

from pathlib import Path
import frontmatter

from .hashing import compute_content_hash


def parse_page(file_path: Path) -> tuple[dict, str]:
    """Parse a markdown file with YAML frontmatter.

    Args:
        file_path: Path to the markdown file

    Returns:
        Tuple of (frontmatter_dict, body_content)

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If frontmatter is invalid
    """
    with open(file_path, "r", encoding="utf-8") as f:
        post = frontmatter.load(f)
    return dict(post.metadata), post.content


def write_page(
    file_path: Path,
    metadata: dict,
    content: str,
    atomic: bool = True,
) -> str:
    """Write a markdown file with YAML frontmatter.

    Args:
        file_path: Path to write the file
        metadata: Dictionary to serialize as YAML frontmatter
        content: Markdown body content
        atomic: If True, write to temp file then rename (default True)

    Returns:
        SHA-256 hash of the content (for revision tracking)
    """
    # Create parent directories if needed
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Create the frontmatter post
    post = frontmatter.Post(content, **metadata)

    # Serialize to string
    output = frontmatter.dumps(post)

    # Compute hash of content (body only, not frontmatter)
    content_hash = compute_content_hash(content)

    if atomic:
        # Write to temp file then rename (atomic on POSIX)
        temp_path = file_path.with_suffix(file_path.suffix + ".tmp")
        with open(temp_path, "w", encoding="utf-8") as f:
            f.write(output)
        temp_path.rename(file_path)
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(output)

    return content_hash


def update_frontmatter(
    file_path: Path,
    updates: dict,
    atomic: bool = True,
) -> str:
    """Update specific frontmatter fields without changing content.

    Args:
        file_path: Path to the markdown file
        updates: Dictionary of fields to update
        atomic: If True, write to temp file then rename

    Returns:
        SHA-256 hash of the content
    """
    metadata, content = parse_page(file_path)
    metadata.update(updates)
    return write_page(file_path, metadata, content, atomic=atomic)


def get_frontmatter(file_path: Path) -> dict:
    """Get only the frontmatter from a markdown file.

    Args:
        file_path: Path to the markdown file

    Returns:
        Dictionary of frontmatter fields
    """
    metadata, _ = parse_page(file_path)
    return metadata


def get_content(file_path: Path) -> str:
    """Get only the content (body) from a markdown file.

    Args:
        file_path: Path to the markdown file

    Returns:
        Markdown body content without frontmatter
    """
    _, content = parse_page(file_path)
    return content


def validate_frontmatter(metadata: dict, required_fields: list[str]) -> list[str]:
    """Validate that required frontmatter fields are present.

    Args:
        metadata: Frontmatter dictionary
        required_fields: List of required field names

    Returns:
        List of missing field names (empty if all present)
    """
    missing = []
    for field in required_fields:
        if field not in metadata or metadata[field] is None:
            missing.append(field)
    return missing
