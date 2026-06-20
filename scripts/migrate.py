#!/usr/bin/env python3
"""Idempotent schema v2 migration script for LLM Wiki (P9).

Walks all wiki pages under wiki_dir/wiki/, upgrades each to schema_version 2:
  - Assigns a stable UUID via identity.source_uuid()
  - Wraps body prose in authored-region markers (if absent)
  - Computes content_hash over the authored region
  - Resolves relations[].target slugs -> UUIDs where possible
  - Stamps schema_version: 2 and updated: <now>

Idempotent: pages that already satisfy all v2 conditions are skipped.

Usage:
    python3 scripts/migrate.py [--dry-run] [--wiki-dir wiki/] [--index-dir .index/]
"""

from __future__ import annotations

import argparse
import json
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Path bootstrap
# ---------------------------------------------------------------------------

_REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO_ROOT / "src"))

from llm_wiki.identity import SlugRegistry, source_uuid  # noqa: E402
from llm_wiki.io.authored_hash import (  # noqa: E402
    compute_authored_hash,
    wrap_authored_region,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_SKIP_NAMES = frozenset(
    ["index.md", "index.full.md", "log.md", "lint_report.md", "README.md"]
)
_AUTHORED_START = "<!-- AUTHORED REGION START -->"
_AUTHORED_END = "<!-- AUTHORED REGION END -->"

# ---------------------------------------------------------------------------
# Frontmatter helpers
# ---------------------------------------------------------------------------


def split_frontmatter(text: str) -> tuple[dict, str]:
    """Split a page into (frontmatter_dict, body_str).

    Expects the file to start with '---\\n' ... '---\\n'.
    Returns empty dict and full text if no frontmatter found.
    """
    if not text.startswith("---"):
        return {}, text

    end = text.find("\n---", 3)
    if end == -1:
        return {}, text

    fm_text = text[3 : end + 1].strip()
    body = text[end + 4 :].lstrip("\n")
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, body


def dump_frontmatter(fm: dict, body: str) -> str:
    """Serialise frontmatter dict + body back to a full page string."""
    # Use default_flow_style=False for readable multi-line YAML.
    # sort_keys=False preserves field order (Python 3.7+ dict ordering).
    fm_text = yaml.dump(
        fm,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    ).rstrip("\n")
    return f"---\n{fm_text}\n---\n\n{body}\n"


# ---------------------------------------------------------------------------
# Migration logic for a single page
# ---------------------------------------------------------------------------

_Status = str  # "already_v2" | "migrated" | "no_change" | "error" | "skipped"


def _is_already_v2(fm: dict, body: str) -> bool:
    """Return True if the page already satisfies all v2 conditions."""
    return (
        fm.get("schema_version") == 2
        and bool(fm.get("uuid"))
        and bool(fm.get("content_hash"))
        and _AUTHORED_START in body
    )


def migrate_page(
    path: Path,
    registry: SlugRegistry,
    *,
    dry_run: bool,
    now_iso: str,
) -> tuple[_Status, str]:
    """Migrate a single page file to schema v2.

    Returns (status, detail_message).
    """
    raw = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(raw)

    if not fm:
        return "error", "no frontmatter found"

    if _is_already_v2(fm, body):
        return "already_v2", ""

    try:
        # --- 1. Derive UUID from raw body (pre-wrap, stable) ---------------
        page_uuid = source_uuid(body)
        uuid_str = str(page_uuid)

        # Register slug -> UUID in registry (in-memory; saved in batch after)
        slug = fm.get("page_id", "")
        if slug:
            registry.register(slug, page_uuid)

        # --- 2. Wrap authored region if absent ------------------------------
        if _AUTHORED_START not in body:
            body = wrap_authored_region(body)

        # --- 3. Compute content_hash over (potentially wrapped) body --------
        content_hash = compute_authored_hash(body)

        # --- 4. Resolve relations[].target slugs -> UUIDs -------------------
        relations = fm.get("relations", []) or []
        updated_relations = []
        for rel in relations:
            if isinstance(rel, dict):
                target = rel.get("target", "")
                resolved = registry.uuid_for_slug(target) if target else None
                if resolved and resolved != target:
                    rel = dict(rel)
                    rel["target"] = resolved
            updated_relations.append(rel)
        if updated_relations:
            fm["relations"] = updated_relations

        # --- 5. Stamp v2 fields ---------------------------------------------
        fm["schema_version"] = 2
        fm["uuid"] = uuid_str
        fm["content_hash"] = content_hash
        fm["updated"] = now_iso

        # --- 6. Write back (unless dry-run) ---------------------------------
        if not dry_run:
            new_content = dump_frontmatter(fm, body)
            path.write_text(new_content, encoding="utf-8")

        return "migrated", f"uuid={uuid_str} hash={content_hash}"

    except Exception as exc:  # noqa: BLE001
        return "error", f"{type(exc).__name__}: {exc}\n{traceback.format_exc()}"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Idempotent schema v2 migration for LLM Wiki (P9)."
    )
    parser.add_argument(
        "--wiki-dir",
        default="wiki/",
        help="Root wiki directory (default: wiki/). Pages are under <wiki-dir>/wiki/.",
    )
    parser.add_argument(
        "--index-dir",
        default=".index/",
        help="Index directory containing slug_registry.json (default: .index/).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would change without writing any files.",
    )
    args = parser.parse_args()

    repo_root = Path.cwd()
    wiki_dir = (repo_root / args.wiki_dir).resolve()
    pages_dir = wiki_dir / "wiki"
    index_dir = (repo_root / args.index_dir).resolve()
    registry_path = index_dir / "slug_registry.json"
    log_path = wiki_dir / "migration_v2_log.jsonl"

    if not pages_dir.exists():
        print(f"ERROR: pages directory not found: {pages_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Scanning {pages_dir}")

    registry = SlugRegistry(registry_path)
    now_iso = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Collect all eligible .md files (recursive, skip reserved names)
    md_files = sorted(
        p
        for p in pages_dir.rglob("*.md")
        if p.name not in _SKIP_NAMES
    )

    total = len(md_files)
    counts: dict[str, int] = {
        "migrated": 0,
        "already_v2": 0,
        "no_change": 0,
        "error": 0,
        "skipped": 0,
    }
    log_entries: list[dict] = []

    for path in md_files:
        rel = path.relative_to(pages_dir)
        status, detail = migrate_page(
            path,
            registry,
            dry_run=args.dry_run,
            now_iso=now_iso,
        )
        counts[status] = counts.get(status, 0) + 1

        # Print per-page status
        marker = {
            "migrated": "[MIGRATE]",
            "already_v2": "[SKIP-V2]",
            "no_change": "[NO-CHG ]",
            "error": "[ERROR  ]",
            "skipped": "[SKIP   ]",
        }.get(status, f"[{status.upper()}]")
        detail_str = f"  {detail}" if detail else ""
        print(f"  {marker} {rel}{detail_str}")

        log_entries.append(
            {
                "file": str(rel),
                "status": status,
                "detail": detail,
                "timestamp": now_iso,
            }
        )

    # Save registry if not dry-run (already saved incrementally via register(),
    # but an explicit final save ensures consistency)
    if not args.dry_run:
        registry.save()

    # Write migration log
    if not args.dry_run:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open("a", encoding="utf-8") as fh:
            for entry in log_entries:
                fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
        print(f"\nMigration log appended to {log_path}")
    else:
        print("\n[DRY RUN] No files written; log not updated.")

    # Final summary
    print(
        f"\n{'[DRY RUN] ' if args.dry_run else ''}Summary:"
        f" total={total}"
        f" migrated={counts.get('migrated', 0)}"
        f" already_v2={counts.get('already_v2', 0)}"
        f" no_change={counts.get('no_change', 0)}"
        f" errors={counts.get('error', 0)}"
    )
    if counts.get("error", 0):
        sys.exit(1)


if __name__ == "__main__":
    main()
