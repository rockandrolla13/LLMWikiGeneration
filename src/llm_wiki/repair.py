"""Auto-repair utilities for LLM Wiki (P7).

Handles mechanical fixes for STRUCTURAL lint errors (currently: unclosed code
fences) and escalates STALE pages to in_review verification status.

Usage:
    from pathlib import Path
    from llm_wiki.repair import run_repair

    result = run_repair(Path("wiki"))
    print(result)
    # {'repaired': 3, 'escalated_to_review': 5, 'remaining_issues': 42}
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))

from llm_wiki.io.page_io import parse_page, write_page
from llm_wiki.lint_extended import LintIssue, run_lint, write_lint_report


# ---------------------------------------------------------------------------
# Fence repair
# ---------------------------------------------------------------------------


def fix_unclosed_fences(body: str) -> str:
    """Append a closing ``` if the body has an odd number of fence markers.

    Only triple-backtick (```) fences are considered. If the count is already
    even (fences are balanced), the body is returned unchanged.

    Args:
        body: Markdown body text.

    Returns:
        Possibly-modified body with balanced fences.
    """
    count = body.count("```")
    if count % 2 == 0:
        return body
    # Append closing fence on its own line
    if body.endswith("\n"):
        return body + "```\n"
    return body + "\n```\n"


# ---------------------------------------------------------------------------
# Per-page repair
# ---------------------------------------------------------------------------


def repair_page(path: Path) -> bool:
    """Read a page, apply mechanical repairs, and write it back if changed.

    Currently applies:
    - fix_unclosed_fences: adds a closing ``` if the body has an odd count.

    Args:
        path: Filesystem path to a markdown wiki page.

    Returns:
        True if the page was modified and written; False if no changes were needed.
    """
    try:
        fm, body = parse_page(path)
    except Exception:
        return False

    original_body = body
    body = fix_unclosed_fences(body)

    if body == original_body:
        return False

    try:
        write_page(path, fm, body, atomic=True)
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Main repair runner
# ---------------------------------------------------------------------------


def run_repair(wiki_dir: Path) -> dict:
    """Lint the wiki, repair STRUCTURAL ERRORs, escalate STALE pages.

    Steps:
    1. Run lint to collect all issues.
    2. For each STRUCTURAL ERROR issue: attempt to repair the page file.
    3. For each STALE WARNING issue: update frontmatter verification.status
       to 'in_review' (if not already verified/in_review).
    4. Re-run lint after repairs and write updated lint_report.md.
    5. Return summary dict.

    Args:
        wiki_dir: Root wiki directory.

    Returns:
        dict with keys:
            repaired (int): number of pages successfully repaired.
            escalated_to_review (int): number of STALE pages escalated.
            remaining_issues (int): total issues after repair.
    """
    # Step 1: initial lint
    initial_issues = run_lint(wiki_dir)

    repaired = 0
    escalated = 0

    # Build a mapping from page_id -> filesystem path
    # We need this to resolve page_id -> file for both repair and escalation.
    id_to_path: dict[str, Path] = {}
    content_root = wiki_dir / "wiki" if (wiki_dir / "wiki").exists() else wiki_dir
    for md_path in sorted(content_root.rglob("*.md")):
        try:
            fm, _ = parse_page(md_path)
            pid = fm.get("page_id")
            if pid:
                id_to_path[pid] = md_path
        except Exception:
            pass

    # Step 2: repair STRUCTURAL ERRORs
    structural_errors = [
        i for i in initial_issues
        if i.category == "STRUCTURAL" and i.severity == "ERROR"
        and "Unclosed code fence" in i.message
    ]

    repaired_ids: set[str] = set()
    for issue in structural_errors:
        path = id_to_path.get(issue.page_id)
        if path is None:
            # Try treating page_id as a direct path segment
            candidate = wiki_dir / (issue.page_id + ".md")
            if candidate.exists():
                path = candidate

        if path and path.exists():
            if repair_page(path):
                repaired += 1
                repaired_ids.add(issue.page_id)

    # Step 3: escalate STALE pages to in_review
    stale_issues = [
        i for i in initial_issues
        if i.category == "STALE"
    ]

    escalated_ids: set[str] = set()
    _skip_statuses = {"verified", "in_review"}

    for issue in stale_issues:
        path = id_to_path.get(issue.page_id)
        if path is None or not path.exists():
            continue

        try:
            fm, body = parse_page(path)
        except Exception:
            continue

        verification = fm.get("verification")
        # verification may be a dict or a string
        if isinstance(verification, dict):
            current_status = verification.get("status", "unverified")
            if current_status in _skip_statuses:
                continue
            fm["verification"] = dict(verification)
            fm["verification"]["status"] = "in_review"
        elif isinstance(verification, str):
            if verification in _skip_statuses:
                continue
            fm["verification"] = "in_review"
        else:
            # No verification field: add one
            fm["verification"] = {"status": "in_review", "unverified_claims": 0}

        try:
            write_page(path, fm, body, atomic=True)
            escalated += 1
            escalated_ids.add(issue.page_id)
        except Exception:
            pass

    # Step 4: re-run lint and write updated report
    final_issues = run_lint(wiki_dir)
    write_lint_report(final_issues, wiki_dir)

    return {
        "repaired": repaired,
        "escalated_to_review": escalated,
        "remaining_issues": len(final_issues),
    }
