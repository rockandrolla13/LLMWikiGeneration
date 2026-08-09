#!/usr/bin/env python3
"""Report what wiki/MIND_MAP.md no longer reaches.

MIND_MAP.md is Tier 1 -- 211 nodes of hand-written synthesis. The MindMapCompiler
produces a ~28-node routing stub, so there is no such thing as "rebuilding" it:
running the generator over it destroys the curation, which is what happened in
June 2026. This script therefore WRITES NOTHING. It produces the worklist a human
curation session needs, and nothing else.

Coverage is counted three ways, kept separate so any number can be audited back
to the signal that produced it:

  linked    -- the page appears as a [[wikilink]] in MIND_MAP.md
  titled    -- the page's title appears verbatim in the MIND_MAP prose
  by-author -- a surname from the page's `authors:` frontmatter appears in it

All three are needed. Counting links alone overstates the gap roughly fourfold,
because most nodes cite sources in prose rather than as links. Titles alone still
miss shortened citations: page "Build a Large Language Model (From Scratch)" is
node [87], written "Raschka's Build LLM from Scratch".

The by-author signal reads `authors:` from frontmatter (present on 362 of 364
sources). An earlier version parsed surnames out of the page slug instead and was
wrong twice: a length floor silently dropped Xu, Bao, Sun, Lee and Zhi, and a
regex requiring a year missed slugs like `koukorinis-stylized-facts`. Both
reported curated sources as missing. The frontmatter states the authors outright,
so nothing needs inferring.

By-author is still the weakest of the three -- a common surname can match a node
about a different paper -- so it is reported on its own line.

Exit status:
    0  drift is at or below --threshold
    1  drift exceeds --threshold  (a scheduled run reports only in this case)
    2  MIND_MAP.md or the wiki could not be read

Usage:
    python scripts/mind_map_drift.py                  # human-readable worklist
    python scripts/mind_map_drift.py --json           # machine-readable
    python scripts/mind_map_drift.py --threshold 25   # quiet under 25 sources
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from llm_wiki import Wiki  # noqa: E402
from llm_wiki.io import extract_wikilinks, normalize_link_target, parse_page  # noqa: E402

# Titles shorter than this are matched only as wikilinks, never as prose. "main",
# "AG" and "out" are real page titles here and would match inside ordinary words.
MIN_TITLE_LEN_FOR_PROSE = 8

# Curator's own ranking, from `mind_map_priority` frontmatter. Sources marked
# high earn a node before ones marked medium, whatever their link count.
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}

COVERAGE_RE = re.compile(
    r"Coverage as of (\d{4}-\d{2}-\d{2}):\s*\*\*(\d+) sources, "
    r"(\d+) entities, (\d+) concepts\*\*"
)


def surnames(authors) -> list[str]:
    """Last name of each author.

    `authors:` appears in TWO shapes in this vault and both must be handled:

        authors: ['Anastasios N. Angelopoulos', 'Emmanuel J. Candes']
        authors: ['entities/chen-xu', 'entities/yao-xie']

    The second form is an entity page_id, not a name. Splitting it on whitespace
    yields the whole string, which matches nothing -- that bug reported
    xu-2022-spci as missing even though it is node [108], "Xu SPCI".

    Returns names capitalised, so callers can match case-sensitively against
    MIND_MAP prose without any length heuristic.
    """
    if not authors:
        return []
    if isinstance(authors, str):
        authors = [authors]
    out = []
    for name in authors:
        if not isinstance(name, str) or not name.strip():
            continue
        if "/" in name:                                # entity page_id form
            slug = name.rsplit("/", 1)[-1]
            parts = [p for p in slug.split("-") if len(p) > 1]
            if parts:
                out.append(parts[-1].capitalize())
            continue
        parts = [p.strip(" .,;()") for p in name.split()]
        parts = [p for p in parts if len(p) > 1]      # drop initials like "J."
        if parts:
            out.append(parts[-1])
    return out


def load_map_text(wiki_root: Path) -> str:
    mind_map = wiki_root / "MIND_MAP.md"
    if not mind_map.exists():
        print(f"MIND_MAP.md not found at {mind_map}", file=sys.stderr)
        raise SystemExit(2)
    return mind_map.read_text(encoding="utf-8")


def build_coverage(wiki: Wiki, map_text: str) -> tuple[dict, dict]:
    """Return (pages, coverage), both keyed by page_id."""
    linked_targets = {
        t for t in (normalize_link_target(x) for x in extract_wikilinks(map_text)) if t
    }

    pages: dict[str, dict] = {}
    title_to_id: dict[str, str] = {}
    for path in wiki.list_pages():
        try:
            meta, _ = parse_page(path)
        except Exception:
            continue
        page_id = meta.get("page_id")
        if not page_id:
            continue
        title = (meta.get("title") or "").strip()
        pages[page_id] = {
            "title": title,
            "kind": page_id.split("/", 1)[0] if "/" in page_id else "other",
            "stem": path.stem,
            "inbound": 0,
            "surnames": surnames(meta.get("authors")),
            "priority": meta.get("mind_map_priority"),
        }
        if title:
            title_to_id.setdefault(title, page_id)

    # Inbound link count across the whole wiki -- a source cited often by other
    # pages earns a node before one cited never.
    for path in wiki.list_pages():
        try:
            _, body = parse_page(path)
        except Exception:
            continue
        for raw in extract_wikilinks(body):
            target = normalize_link_target(raw)
            if not target:
                continue
            if target in pages:
                pages[target]["inbound"] += 1
            elif target in title_to_id:
                pages[title_to_id[target]]["inbound"] += 1

    coverage = {}
    for page_id, info in pages.items():
        linked = page_id in linked_targets or info["stem"] in linked_targets
        if info["title"]:
            linked = linked or info["title"] in linked_targets

        # Case-insensitive: nodes write concept-style titles in lower case
        # ("residual momentum"), so a case-sensitive match reported those as
        # missing. The MIN_TITLE_LEN floor is what keeps this from over-matching.
        titled = bool(
            info["title"]
            and len(info["title"]) >= MIN_TITLE_LEN_FOR_PROSE
            and re.search(rf"\b{re.escape(info['title'])}\b", map_text, re.IGNORECASE)
        )

        by_author = any(
            re.search(rf"\b{re.escape(s)}\b", map_text) for s in info["surnames"]
        )

        coverage[page_id] = {
            "linked": linked,
            "titled": titled,
            "by_author": by_author,
        }

    return pages, coverage


def self_reported(map_text: str) -> dict | None:
    m = COVERAGE_RE.search(map_text)
    if not m:
        return None
    return {
        "as_of": m.group(1),
        "sources": int(m.group(2)),
        "entities": int(m.group(3)),
        "concepts": int(m.group(4)),
    }


def rank_key(item):
    _, info = item
    return (PRIORITY_ORDER.get(info["priority"], 3), -info["inbound"])


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--wiki", default="wiki", help="vault root (default: wiki)")
    ap.add_argument("--threshold", type=int, default=20,
                    help="exit 1 when this many sources are uncovered (default: 20)")
    ap.add_argument("--limit", type=int, default=25,
                    help="worklist entries to print (default: 25)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    wiki_root = Path(args.wiki)
    try:
        wiki = Wiki(wiki_root)
    except Exception as exc:
        print(f"could not open wiki at {wiki_root}: {exc}", file=sys.stderr)
        return 2

    map_text = load_map_text(wiki_root)
    pages, coverage = build_coverage(wiki, map_text)

    def reached(page_id: str) -> bool:
        c = coverage[page_id]
        return c["linked"] or c["titled"] or c["by_author"]

    uncovered = {pid: info for pid, info in pages.items() if not reached(pid)}
    sources_uncovered = {k: v for k, v in uncovered.items() if v["kind"] == "sources"}

    totals = {
        "pages": len(pages),
        "linked": sum(1 for c in coverage.values() if c["linked"]),
        "titled_only": sum(
            1 for c in coverage.values() if c["titled"] and not c["linked"]
        ),
        "by_author_only": sum(
            1 for c in coverage.values()
            if c["by_author"] and not (c["linked"] or c["titled"])
        ),
        "covered": sum(1 for pid in pages if reached(pid)),
        "uncovered": len(uncovered),
        "uncovered_sources": len(sources_uncovered),
    }

    ranked = sorted(sources_uncovered.items(), key=rank_key)

    if args.json:
        print(json.dumps({
            "totals": totals,
            "self_reported": self_reported(map_text),
            "uncovered_sources": [
                {"page_id": k, "title": v["title"], "priority": v["priority"],
                 "inbound": v["inbound"]}
                for k, v in ranked
            ],
        }, indent=2, ensure_ascii=False))
        return 1 if totals["uncovered_sources"] > args.threshold else 0

    print("=== MIND_MAP coverage ===")
    print(f"  pages in wiki           : {totals['pages']}")
    print(f"  reached as wikilink     : {totals['linked']}")
    print(f"  reached by title only   : {totals['titled_only']}")
    print(f"  reached by author only  : {totals['by_author_only']}   (weakest signal)")
    print(f"  reached at all          : {totals['covered']}")
    print(f"  NOT reached             : {totals['uncovered']}"
          f"   (of which sources: {totals['uncovered_sources']})")

    claim = self_reported(map_text)
    if claim:
        print(f"\n  MIND_MAP self-reports, as of {claim['as_of']}: "
              f"{claim['sources']} sources, {claim['entities']} entities, "
              f"{claim['concepts']} concepts")

    # A source with no authors recorded cannot use the by-author signal, so it can
    # appear here even when MIND_MAP does cite it. Say so rather than let the
    # number look cleaner than it is.
    authorless = [
        pid for pid, info in sources_uncovered.items() if not info["surnames"]
    ]
    if authorless:
        print(f"\n  note: {len(authorless)} of the uncovered sources record no "
              f"authors, so the by-author check cannot see them.")
        print("        They may already be on the map under a short citation:")
        for pid in authorless[:5]:
            print(f"          {pid}")

    print("\n=== Worklist: uncovered sources ===")
    print("(ranked by the curator's own mind_map_priority, then by inbound links)")
    if not ranked:
        print("  none -- every source is reachable from the map")
    for page_id, info in ranked[:args.limit]:
        prio = info["priority"] or "-"
        print(f"  {prio:<6} {info['inbound']:3d} inbound  {info['title'] or page_id}")
    if len(ranked) > args.limit:
        print(f"  ... and {len(ranked) - args.limit} more (raise --limit)")

    over = totals["uncovered_sources"] > args.threshold
    print(f"\ndrift threshold {args.threshold} sources: "
          f"{'EXCEEDED' if over else 'within limit'}")
    print("This script writes nothing. MIND_MAP.md is curated by hand.")
    return 1 if over else 0


if __name__ == "__main__":
    raise SystemExit(main())
