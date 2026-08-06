"""Page I/O utilities for LLM Wiki.

Handles reading and writing YAML frontmatter in markdown files.
Uses python-frontmatter library for parsing.
"""

from pathlib import Path
import frontmatter

from .hashing import compute_content_hash


# Marker stamped into every artifact this tool generates. Its presence is what
# distinguishes a regenerable file from hand-curated work that must not be
# overwritten, so the literal is defined once and imported everywhere.
GENERATED_MARKER = "AUTO-GENERATED FILE - DO NOT EDIT MANUALLY"

# How far into a file to look for the marker. It sits after the YAML frontmatter,
# and real pages carry ~6 KB of frontmatter, so a small window would scan past it
# and misreport a generated file as hand-curated.
_MARKER_SEARCH_BYTES = 65536


def is_generated(file_path: Path) -> bool:
    """Check whether an artifact is safe for the generator to overwrite.

    Safe means one of:
    - the file does not exist yet (nothing to lose), or
    - the file carries GENERATED_MARKER, so this tool wrote it.

    Hand-curated artifacts carry no marker. Overwriting one destroys work the
    generator cannot reproduce, so callers must treat False as "skip".

    Args:
        file_path: Path to the artifact

    Returns:
        True if absent or generator-owned, False if hand-curated
    """
    if not file_path.exists():
        return True

    with open(file_path, "r", encoding="utf-8") as f:
        head = f.read(_MARKER_SEARCH_BYTES)

    return GENERATED_MARKER in head


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
