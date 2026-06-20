"""
merge.py - Structural heading-tree merge for wiki markdown files.

Implements a monotonic merge: the heading-path set of the output is always
a superset of the heading-path set of the old document.  No section is ever
deleted.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Section:
    heading: str          # Raw heading line, e.g. "## Summary"
    heading_level: int    # Number of '#' chars
    heading_text: str     # Text after the hashes, stripped
    path: Tuple[str, ...] # Hierarchical path tuple, e.g. ("Test", "Summary")
    body_lines: List[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

_HEADING_RE = re.compile(r'^(#{1,6})\s+(.+)$')


def _parse_sections(md: str) -> Tuple[List[str], List[Section]]:
    """Parse *md* into a preamble (lines before the first heading) and an
    ordered list of Section objects.

    Each Section carries a hierarchical *path* tuple derived from a stack of
    ancestor headings at higher levels.
    """
    lines = md.splitlines(keepends=True)

    preamble: List[str] = []
    sections: List[Section] = []
    current: Optional[Section] = None

    # Stack entries: (level: int, text: str)
    path_stack: List[Tuple[int, str]] = []

    for line in lines:
        m = _HEADING_RE.match(line.rstrip('\n').rstrip('\r'))
        if m:
            # Save previous section
            if current is not None:
                sections.append(current)
            elif preamble is not None and current is None and not sections:
                pass  # preamble already accumulated

            level = len(m.group(1))
            text = m.group(2).strip()

            # Trim stack to ancestors only (levels strictly less than current)
            path_stack = [(l, t) for l, t in path_stack if l < level]
            path_stack.append((level, text))

            path = tuple(t for _, t in path_stack)
            heading_raw = line.rstrip('\n').rstrip('\r')

            current = Section(
                heading=heading_raw,
                heading_level=level,
                heading_text=text,
                path=path,
                body_lines=[],
            )
        else:
            if current is None:
                preamble.append(line)
            else:
                current.body_lines.append(line)

    # Flush the last open section
    if current is not None:
        sections.append(current)

    return preamble, sections


# ---------------------------------------------------------------------------
# Dict representation
# ---------------------------------------------------------------------------

def _sections_to_dict(sections: List[Section]) -> Dict[Tuple[str, ...], Section]:
    """Map each section's path tuple to the Section.

    If duplicate paths exist (edge case), last-one-wins so callers get a
    deterministic result.
    """
    return {s.path: s for s in sections}


# ---------------------------------------------------------------------------
# Body deduplication helpers
# ---------------------------------------------------------------------------

def _dedupe_lines(lines: List[str]) -> List[str]:
    """Return *lines* with duplicate non-blank lines removed (order preserved,
    first occurrence kept)."""
    seen: set = set()
    out: List[str] = []
    for ln in lines:
        stripped = ln.rstrip('\n').rstrip('\r').strip()
        if stripped == '':
            out.append(ln)
        elif stripped not in seen:
            seen.add(stripped)
            out.append(ln)
    return out


def _merge_bodies(old_lines: List[str], new_lines: List[str]) -> List[str]:
    """Append new body lines that are not already present in old body."""
    old_stripped = {ln.rstrip('\n').rstrip('\r').strip() for ln in old_lines
                    if ln.rstrip('\n').rstrip('\r').strip()}
    appended: List[str] = []
    for ln in new_lines:
        s = ln.rstrip('\n').rstrip('\r').strip()
        if s and s not in old_stripped:
            appended.append(ln)
            old_stripped.add(s)
    return old_lines + appended


# ---------------------------------------------------------------------------
# Heading reconstruction
# ---------------------------------------------------------------------------

def _reconstruct_heading(path: Tuple[str, ...], original_section: Section) -> str:
    """Return the heading line for *path*.

    We prefer the original heading string if available, otherwise synthesise
    one from the path depth and the last element.
    """
    return original_section.heading


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def markdown_merge(
    old_md: str,
    new_md: str,
    dedupe_headings: bool = True,
) -> str:
    """Merge *new_md* into *old_md* using structural heading-tree merge.

    Rules
    -----
    * Old sections are always retained (monotonic invariant).
    * New-only sections are appended after all old sections that share the
      same parent path, preserving approximate structural locality.
    * When both documents contain the same section path, their body content
      is unioned (new non-duplicate lines appended to old body).
    * If *dedupe_headings* is True, duplicate non-blank body lines within a
      merged section are removed.

    Returns the merged markdown string.
    """
    old_preamble, old_sections = _parse_sections(old_md)
    new_preamble, new_sections = _parse_sections(new_md)

    old_dict = _sections_to_dict(old_sections)
    new_dict = _sections_to_dict(new_sections)

    # Build merged ordered path list:
    #   1. All old paths in original order.
    #   2. New-only paths inserted after the last old sibling (or appended).
    merged_paths: List[Tuple[str, ...]] = list(path for path in
                                               (s.path for s in old_sections))

    # Track insertion positions for new-only sections grouped by parent
    new_only_paths = [s.path for s in new_sections if s.path not in old_dict]

    for np in new_only_paths:
        parent = np[:-1]
        # Find last index in merged_paths whose path starts with parent
        insert_after = -1
        for i, mp in enumerate(merged_paths):
            if mp[:len(parent)] == parent:
                insert_after = i
        merged_paths.insert(insert_after + 1, np)

    # Build merged section objects
    merged_sections: List[Section] = []
    for path in merged_paths:
        if path in old_dict and path in new_dict:
            old_sec = old_dict[path]
            new_sec = new_dict[path]
            merged_body = _merge_bodies(old_sec.body_lines, new_sec.body_lines)
            if dedupe_headings:
                merged_body = _dedupe_lines(merged_body)
            merged_sec = Section(
                heading=old_sec.heading,
                heading_level=old_sec.heading_level,
                heading_text=old_sec.heading_text,
                path=path,
                body_lines=merged_body,
            )
        elif path in old_dict:
            merged_sec = old_dict[path]
        else:
            # new-only
            src = new_dict[path]
            # Adjust heading level to match depth implied by path
            level = len(path)
            heading_text = src.heading_text
            heading = '#' * level + ' ' + heading_text
            merged_sec = Section(
                heading=heading,
                heading_level=level,
                heading_text=heading_text,
                path=path,
                body_lines=src.body_lines,
            )
        merged_sections.append(merged_sec)

    # Reconstruct markdown
    out_parts: List[str] = []

    # Preamble: prefer old, fall back to new
    preamble = old_preamble if old_preamble else new_preamble
    for ln in preamble:
        out_parts.append(ln if ln.endswith('\n') else ln + '\n')

    for sec in merged_sections:
        out_parts.append(sec.heading + '\n')
        for ln in sec.body_lines:
            out_parts.append(ln if ln.endswith('\n') else ln + '\n')

    return ''.join(out_parts)
