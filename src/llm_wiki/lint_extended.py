"""Extended lint checks for LLM Wiki (P7).

Provides four lint categories:
- STRUCTURAL: unclosed code fences, skipped heading levels
- REFERENTIAL: broken wikilinks, out-of-vocab relation types, unresolved relation targets
- GRAPH: orphan pages (zero inbound edges)
- STALE: pages flagged by staleness detection

Usage:
    from pathlib import Path
    from llm_wiki.lint_extended import run_lint, write_lint_report

    issues = run_lint(Path("wiki"))
    report_path = write_lint_report(issues, Path("wiki"))
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml

# Allow running directly or as module
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))

from llm_wiki.graph import KnowledgeGraph, build_graph
from llm_wiki.io.page_io import parse_page
from llm_wiki.staleness import detect_stale_pages

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

SEVERITY_ORDER = {"ERROR": 0, "WARNING": 1, "INFO": 2}


@dataclass
class LintIssue:
    """A single lint finding."""

    category: str
    """One of: STRUCTURAL, REFERENTIAL, GRAPH, STALE."""

    severity: str
    """One of: ERROR, WARNING, INFO."""

    page_id: str
    """Identifier of the affected page (or empty string for wiki-level issues)."""

    message: str
    """Human-readable description of the issue."""


# ---------------------------------------------------------------------------
# Structural checks
# ---------------------------------------------------------------------------

_WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
_HEADING_RE = re.compile(r"^(#{1,6})\s", re.MULTILINE)


def _count_backtick_fences(body: str) -> int:
    """Count occurrences of triple-backtick fence markers."""
    return body.count("```")


def check_structural(path: Path, body: str, page_id: str) -> list[LintIssue]:
    """Run structural checks on a page body.

    Checks:
    1. Unclosed code fences — an odd count of ``` markers means one is unclosed.
    2. Skipped heading levels — e.g. jumping from H1 to H3 without H2.

    Args:
        path: Filesystem path (used only for context in messages).
        body: Markdown body text (no frontmatter).
        page_id: Page identifier string.

    Returns:
        List of LintIssue objects (may be empty).
    """
    issues: list[LintIssue] = []

    # Check 1: unclosed fences
    fence_count = _count_backtick_fences(body)
    if fence_count % 2 != 0:
        issues.append(
            LintIssue(
                category="STRUCTURAL",
                severity="ERROR",
                page_id=page_id,
                message=(
                    f"Unclosed code fence: found {fence_count} triple-backtick "
                    "markers (odd count implies one is not closed)"
                ),
            )
        )

    # Check 2: skipped heading levels
    headings = _HEADING_RE.findall(body)
    prev_level = 0
    for hashes in headings:
        level = len(hashes)
        if prev_level > 0 and level > prev_level + 1:
            issues.append(
                LintIssue(
                    category="STRUCTURAL",
                    severity="WARNING",
                    page_id=page_id,
                    message=(
                        f"Skipped heading level: jumped from H{prev_level} to "
                        f"H{level}"
                    ),
                )
            )
        prev_level = level

    return issues


# ---------------------------------------------------------------------------
# Referential checks
# ---------------------------------------------------------------------------


def check_referential(
    fm: dict,
    body: str,
    page_id: str,
    known_ids: set[str],
    valid_rels: set[str],
) -> list[LintIssue]:
    """Run referential checks on a page.

    Checks:
    1. Broken wikilinks — [[Target]] that does not match any known page_id.
    2. Out-of-vocab relation types — relation 'rel' not in schema vocabulary.
    3. Unresolved relation targets — relation 'target' not in known page_ids.

    Args:
        fm: Parsed frontmatter dictionary.
        body: Markdown body text.
        page_id: Page identifier string.
        known_ids: Set of all page_id values in the wiki.
        valid_rels: Set of allowed relation type strings from schema.yml.

    Returns:
        List of LintIssue objects (may be empty).
    """
    issues: list[LintIssue] = []

    # Check 1: broken wikilinks in body
    wikilinks = _WIKILINK_RE.findall(body)
    for link in wikilinks:
        # Strip optional display text: [[target|display]] -> target
        target = link.split("|")[0].strip()
        if target not in known_ids:
            issues.append(
                LintIssue(
                    category="REFERENTIAL",
                    severity="WARNING",
                    page_id=page_id,
                    message=f"Broken wikilink: [[{target}]] does not match any known page_id",
                )
            )

    # Check 2 & 3: relations block
    relations = fm.get("relations", [])
    if isinstance(relations, list):
        for entry in relations:
            if not isinstance(entry, dict):
                continue
            rel = entry.get("rel")
            target = entry.get("target")

            if rel and rel not in valid_rels:
                issues.append(
                    LintIssue(
                        category="REFERENTIAL",
                        severity="ERROR",
                        page_id=page_id,
                        message=(
                            f"Out-of-vocab relation type: '{rel}' not in "
                            f"schema vocabulary {sorted(valid_rels)}"
                        ),
                    )
                )

            if target and target not in known_ids:
                issues.append(
                    LintIssue(
                        category="REFERENTIAL",
                        severity="WARNING",
                        page_id=page_id,
                        message=(
                            f"Unresolved relation target: '{target}' not in known page_ids"
                        ),
                    )
                )

    return issues


# ---------------------------------------------------------------------------
# Schema loading
# ---------------------------------------------------------------------------


def _load_valid_rels(wiki_dir: Path) -> set[str]:
    """Load the allowed relation vocabulary from schema.yml.

    Falls back to an empty set if schema.yml is missing or malformed.

    Args:
        wiki_dir: Root wiki directory (contains schema.yml at top level).

    Returns:
        Set of valid relation type strings.
    """
    schema_path = wiki_dir / "schema.yml"
    if not schema_path.exists():
        return set()
    try:
        data = yaml.safe_load(schema_path.read_text(encoding="utf-8"))
        vocab = data.get("relations", {}).get("vocabulary", [])
        # Also include computed inverses from inverse_map values
        inverse_map = data.get("relations", {}).get("inverse_map", {})
        all_rels = set(vocab) | set(inverse_map.values())
        return all_rels
    except Exception:
        return set()


# ---------------------------------------------------------------------------
# Page discovery helpers
# ---------------------------------------------------------------------------

# Directories that contain actual wiki pages (not meta-files)
_PAGE_DIRS = {"sources", "entities", "concepts", "analyses", "contradictions"}

# Filenames at the wiki root to skip (meta-files, not content pages)
_SKIP_NAMES = {"index.md", "index.full.md", "log.md", "lint_report.md"}


def _iter_page_paths(wiki_dir: Path):
    """Yield (path, page_id) for all content pages in wiki_dir/wiki/.

    Skips meta-files (index.md, log.md, etc.) and only processes .md files
    under recognised subdirectories.

    Args:
        wiki_dir: Root wiki directory (contains wiki/ sub-dir).
    """
    content_root = wiki_dir / "wiki"
    if not content_root.exists():
        # Fallback: treat wiki_dir itself as content root
        content_root = wiki_dir

    for md_path in sorted(content_root.rglob("*.md")):
        if md_path.name in _SKIP_NAMES:
            continue
        # Compute page_id relative to content_root
        rel = md_path.relative_to(content_root)
        page_id = str(rel.with_suffix(""))
        yield md_path, page_id


def _collect_known_ids(wiki_dir: Path) -> dict[str, Path]:
    """Return a mapping of page_id -> path for all content pages.

    Args:
        wiki_dir: Root wiki directory.

    Returns:
        dict mapping page_id strings to their filesystem paths.
    """
    mapping: dict[str, Path] = {}
    for path, page_id in _iter_page_paths(wiki_dir):
        # Prefer page_id from frontmatter if available
        try:
            fm, _ = parse_page(path)
            fm_id = fm.get("page_id")
            if fm_id:
                mapping[fm_id] = path
            else:
                mapping[page_id] = path
        except Exception:
            mapping[page_id] = path
    return mapping


# ---------------------------------------------------------------------------
# Main lint runner
# ---------------------------------------------------------------------------


def run_lint(wiki_dir: Path) -> list[LintIssue]:
    """Run all lint checks against the wiki.

    Steps:
    1. Collect all known page_ids.
    2. Load relation vocabulary from schema.yml.
    3. For each page: run structural and referential checks.
    4. Build knowledge graph; find orphan pages (0 inbound edges).
    5. Run staleness detection; emit STALE issues.

    Args:
        wiki_dir: Root wiki directory (contains schema.yml and wiki/ sub-dir).

    Returns:
        Sorted list of LintIssue objects (by severity then category then page_id).
    """
    issues: list[LintIssue] = []

    # Step 1: collect known page_ids
    id_to_path = _collect_known_ids(wiki_dir)
    known_ids = set(id_to_path.keys())

    # Step 2: load relation vocabulary
    valid_rels = _load_valid_rels(wiki_dir)

    # Step 3: per-page structural and referential checks
    for path, _ in _iter_page_paths(wiki_dir):
        try:
            fm, body = parse_page(path)
        except Exception as exc:
            issues.append(
                LintIssue(
                    category="STRUCTURAL",
                    severity="ERROR",
                    page_id=str(path),
                    message=f"Failed to parse page: {exc}",
                )
            )
            continue

        page_id = fm.get("page_id") or str(path.relative_to(wiki_dir).with_suffix(""))

        issues.extend(check_structural(path, body, page_id))
        issues.extend(check_referential(fm, body, page_id, known_ids, valid_rels))

    # Step 4: graph-level checks (orphans)
    try:
        graph = build_graph(wiki_dir / "wiki" if (wiki_dir / "wiki").exists() else wiki_dir)

        for pid in known_ids:
            inbound = graph.incoming(pid)
            if not inbound:
                issues.append(
                    LintIssue(
                        category="GRAPH",
                        severity="INFO",
                        page_id=pid,
                        message="Orphan page: no inbound edges (not linked from any other page)",
                    )
                )

        # Step 5: staleness detection
        stale_reports = detect_stale_pages(graph, list(known_ids))
        for report in stale_reports:
            issues.append(
                LintIssue(
                    category="STALE",
                    severity="WARNING",
                    page_id=report.page_id,
                    message=report.reason,
                )
            )

    except Exception as exc:
        issues.append(
            LintIssue(
                category="GRAPH",
                severity="ERROR",
                page_id="",
                message=f"Failed to build knowledge graph: {exc}",
            )
        )

    # Sort: severity first (ERROR < WARNING < INFO), then category, then page_id
    issues.sort(
        key=lambda i: (SEVERITY_ORDER.get(i.severity, 99), i.category, i.page_id)
    )
    return issues


# ---------------------------------------------------------------------------
# Report writer
# ---------------------------------------------------------------------------


def write_lint_report(issues: list[LintIssue], wiki_dir: Path) -> Path:
    """Write lint results as a markdown table to wiki/wiki/lint_report.md.

    Args:
        issues: List of LintIssue objects (as returned by run_lint).
        wiki_dir: Root wiki directory.

    Returns:
        Path to the written report file.
    """
    report_path = wiki_dir / "wiki" / "lint_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    from collections import Counter

    counts = Counter(i.category for i in issues)
    sev_counts = Counter(i.severity for i in issues)

    lines = [
        "# Lint Report",
        "",
        f"Generated: {now}",
        "",
        f"**Total issues:** {len(issues)}  ",
        f"**By severity:** "
        + ", ".join(
            f"{k}: {v}" for k, v in sorted(sev_counts.items(), key=lambda x: SEVERITY_ORDER.get(x[0], 99))
        ),
        "",
        f"**By category:** "
        + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())),
        "",
        "## Issues",
        "",
        "| Severity | Category | Page ID | Message |",
        "| --- | --- | --- | --- |",
    ]

    for issue in issues:
        # Escape pipe characters in message
        msg = issue.message.replace("|", "\\|")
        page_id = issue.page_id.replace("|", "\\|")
        lines.append(f"| {issue.severity} | {issue.category} | {page_id} | {msg} |")

    if not issues:
        lines.append("| — | — | — | No issues found |")

    lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path
