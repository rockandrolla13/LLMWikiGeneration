"""
Wiki page chunker: splits markdown pages into per-heading Chunk objects.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

import yaml

# Ensure src is importable when run directly
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

_HEADING_RE = re.compile(r"^(#{1,3})\s+(.*)", re.MULTILINE)

_SKIP_NAMES = {"index.md", "index.full.md", "log.md", "lint_report.md"}


@dataclass
class Chunk:
    page_id: str
    page_title: str
    heading_path: str
    text: str
    source_citations: List[str] = field(default_factory=list)


def chunk_page(path: Path) -> List[Chunk]:
    """Read a single wiki markdown file and return one Chunk per heading section."""
    raw = path.read_text(encoding="utf-8")

    # --- Extract YAML frontmatter ---
    frontmatter: dict = {}
    body = raw
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            fm_text = raw[3:end].strip()
            try:
                frontmatter = yaml.safe_load(fm_text) or {}
            except yaml.YAMLError:
                frontmatter = {}
            body = raw[end + 4:]

    page_id: str = frontmatter.get("page_id", path.stem)
    page_title: str = frontmatter.get("title", path.stem)
    sources: List[str] = frontmatter.get("sources", []) or []
    # Normalise sources to strings
    source_citations: List[str] = [str(s) for s in sources]

    # --- Split body on heading lines ---
    chunks: List[Chunk] = []
    matches = list(_HEADING_RE.finditer(body))

    if not matches:
        # No headings — entire body is one chunk
        text = body.strip()
        if text:
            chunks.append(
                Chunk(
                    page_id=page_id,
                    page_title=page_title,
                    heading_path="",
                    text=text,
                    source_citations=source_citations,
                )
            )
        return chunks

    # Text before the first heading (preamble)
    preamble = body[: matches[0].start()].strip()
    if preamble:
        chunks.append(
            Chunk(
                page_id=page_id,
                page_title=page_title,
                heading_path="",
                text=preamble,
                source_citations=source_citations,
            )
        )

    for i, m in enumerate(matches):
        heading_text = m.group(2).strip()
        section_start = m.end()
        section_end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        section_body = body[section_start:section_end].strip()

        chunks.append(
            Chunk(
                page_id=page_id,
                page_title=page_title,
                heading_path=heading_text,
                text=section_body,
                source_citations=source_citations,
            )
        )

    return chunks


def chunk_wiki(wiki_dir: Path) -> List[Chunk]:
    """Recursively chunk all non-index markdown files under wiki_dir/wiki/."""
    wiki_subdir = wiki_dir / "wiki"
    all_chunks: List[Chunk] = []

    for md_path in sorted(wiki_subdir.rglob("*.md")):
        if md_path.name in _SKIP_NAMES:
            continue
        try:
            all_chunks.extend(chunk_page(md_path))
        except Exception as exc:  # noqa: BLE001
            # Skip files that cannot be parsed; surface as a warning
            import warnings
            warnings.warn(f"chunker: skipping {md_path}: {exc}", stacklevel=1)

    return all_chunks
