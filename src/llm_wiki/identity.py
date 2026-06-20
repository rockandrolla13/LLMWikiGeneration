"""Content-addressable identity for wiki pages.

Provides stable UUIDs derived from normalized page content and slug registries
for mapping human-readable slugs to UUIDs.
"""

from __future__ import annotations

import json
import re
import unicodedata
import uuid
from pathlib import Path
from typing import Optional

# DNS namespace UUID (RFC 4122 section 4.3 example) used as our wiki namespace
NAMESPACE_WIKI = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")

# ---------------------------------------------------------------------------
# Text normalisation
# ---------------------------------------------------------------------------

_YAML_FRONTMATTER = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
_MARKDOWN_IMAGE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
_MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_WIKILINK = re.compile(r"\[\[(?:[^\]|]+\|)?([^\]]+)\]\]")
_HEADING = re.compile(r"^#{1,6}\s+", re.MULTILINE)
_CODE_FENCE = re.compile(r"```[\s\S]*?```", re.DOTALL)
_INLINE_CODE = re.compile(r"`[^`]+`")
_HTML_TAG = re.compile(r"<[^>]+>")
_WHITESPACE = re.compile(r"\s+")


def normalize_text(raw: str) -> str:
    """Return a canonical, whitespace-collapsed string for *raw*.

    Steps (in order):
    1. NFKC Unicode normalisation.
    2. Strip YAML frontmatter (``---`` ... ``---`` block at the very start).
    3. Remove markdown images (drop alt text too — purely decorative).
    4. Resolve wikilinks to their display text ``[[target|display]]`` → ``display``.
    5. Resolve markdown links to their link text ``[text](url)`` → ``text``.
    6. Strip heading markers (``# ``, ``## `` …).
    7. Remove code fences and inline code.
    8. Remove HTML tags.
    9. Collapse all whitespace (newlines, tabs, multiple spaces) to a single space
       and strip leading/trailing whitespace.
    """
    text = unicodedata.normalize("NFKC", raw)

    # Strip YAML frontmatter
    text = _YAML_FRONTMATTER.sub("", text)

    # Remove markdown images entirely (alt text is decorative)
    text = _MARKDOWN_IMAGE.sub("", text)

    # Wikilinks: keep display text
    text = _WIKILINK.sub(r"\1", text)

    # Markdown links: keep link text
    text = _MARKDOWN_LINK.sub(r"\1", text)

    # Remove heading markers
    text = _HEADING.sub("", text)

    # Remove code fences
    text = _CODE_FENCE.sub("", text)

    # Remove inline code
    text = _INLINE_CODE.sub("", text)

    # Remove HTML tags
    text = _HTML_TAG.sub("", text)

    # Collapse whitespace
    text = _WHITESPACE.sub(" ", text).strip()

    return text


# ---------------------------------------------------------------------------
# UUID derivation
# ---------------------------------------------------------------------------


def content_uuid(normalized: str) -> uuid.UUID:
    """Return a UUID5 derived from *normalized* text (already normalised)."""
    return uuid.uuid5(NAMESPACE_WIKI, normalized)


def source_uuid(raw: str) -> uuid.UUID:
    """Normalise *raw* then return its UUID5.

    Two raw strings that normalise to the same text will produce the same UUID.
    """
    return content_uuid(normalize_text(raw))


# ---------------------------------------------------------------------------
# Slug registry
# ---------------------------------------------------------------------------


class SlugRegistry:
    """Persistent bidirectional mapping between page slugs and UUIDs.

    The registry is stored as a JSON file at *path* with the shape::

        {
            "slug_to_uuid": {"concepts/attention": "<uuid>", ...},
            "uuid_to_slug": {"<uuid>": "concepts/attention", ...}
        }

    The parent directory is created automatically if it does not exist.
    """

    def __init__(self, path: Path) -> None:
        self._path = Path(path)
        self._data: dict[str, dict[str, str]] = {"slug_to_uuid": {}, "uuid_to_slug": {}}
        if self._path.exists():
            with self._path.open("r", encoding="utf-8") as fh:
                loaded = json.load(fh)
            self._data["slug_to_uuid"] = loaded.get("slug_to_uuid", {})
            self._data["uuid_to_slug"] = loaded.get("uuid_to_slug", {})

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self) -> None:
        """Write the current registry to disk."""
        self._path.parent.mkdir(parents=True, exist_ok=True)
        with self._path.open("w", encoding="utf-8") as fh:
            json.dump(self._data, fh, indent=2, sort_keys=True)

    # ------------------------------------------------------------------
    # Mutation
    # ------------------------------------------------------------------

    def register(self, slug: str, page_uuid: uuid.UUID) -> None:
        """Associate *slug* with *page_uuid* and persist immediately."""
        uid_str = str(page_uuid)
        self._data["slug_to_uuid"][slug] = uid_str
        self._data["uuid_to_slug"][uid_str] = slug
        self.save()

    # ------------------------------------------------------------------
    # Lookup
    # ------------------------------------------------------------------

    def uuid_for_slug(self, slug: str) -> Optional[str]:
        """Return the UUID string registered for *slug*, or ``None``."""
        return self._data["slug_to_uuid"].get(slug)

    def slug_for_uuid(self, uid: str) -> Optional[str]:
        """Return the slug registered for *uid* (string form), or ``None``."""
        return self._data["uuid_to_slug"].get(uid)

    def all_slugs(self) -> list[str]:
        """Return a sorted list of all registered slugs."""
        return sorted(self._data["slug_to_uuid"].keys())
