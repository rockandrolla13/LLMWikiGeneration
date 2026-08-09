#!/usr/bin/env python3
"""Report which sources wiki/MIND_MAP.md does not reach.

MIND_MAP.md is Tier 1 -- 211 nodes of hand-written synthesis. The MindMapCompiler
emits a ~28-node routing stub, so there is no such thing as "rebuilding" it:
running the generator is what destroyed the file in June 2026. This script
therefore WRITES NOTHING. It produces the worklist a curation session needs.

WHAT COUNTS AS COVERED
----------------------
The map is a graph of numbered nodes. Nodes [1]-[11] are routing hubs named after
topics; every other node is a detail node whose **bold title** names one source.
So the real question is not "does this text appear somewhere" but "is there a
node ABOUT this source". Each signal below answers that, and the reason is
recorded per source so any verdict can be audited:

  wikilink           the page_id appears as a [[wikilink]]
  exact title        the full title appears verbatim in the prose
  near-exact title   >=95% token containment against a detail node's bold title
  title+author       >=60% containment AND that node names one of its authors
  author+year        a detail node names one of its authors and its year

WHY THE AUTHOR IS REQUIRED BELOW 95%
------------------------------------
Title similarity alone is actively dangerous. At 75% containment it matched
"Build a DeepSeek Model From Scratch" to node [87] (Raschka's LLM book), and
"Hands-on Small Language Models" to node [14] ("Hands-On Large Language
Models"). Those are different books, and accepting them would have hidden two
real gaps. Requiring the node to also name an author of the source rejects all
three look-alikes while keeping true shortenings such as node [106], "The
Developer's Playbook for LLM Security".

Hubs are excluded from title matching for the same reason: "Optimal execution
with limit and market orders" matches hub [7] "Market Microstructure & Optimal
Execution" on topic words alone, which says nothing about whether that paper has
a node.

HISTORY, SO THIS IS NOT RE-LITIGATED
------------------------------------
An earlier version matched surnames against the whole file rather than per node.
It reported 96 uncovered sources; hand-checking found Statistical Rethinking,
Data Analysis and Data Mining, Understanding Changes in Corporate Credit Spreads
and others counted as covered while appearing zero times in MIND_MAP. A shared
surname elsewhere in the file was enough to mark a paper covered. Per-node
matching raised the count to its current level, which is the honest direction:
under-reporting hides work, over-reporting only wastes a check.

Exit status:
    0  drift is at or below --threshold
    1  drift exceeds --threshold  (a scheduled run reports only in this case)
    2  MIND_MAP.md or the wiki could not be read

Usage:
    python scripts/mind_map_drift.py
    python scripts/mind_map_drift.py --json
    python scripts/mind_map_drift.py --show-covered      # audit the verdicts
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from llm_wiki import Wiki  # noqa: E402
from llm_wiki.io import extract_wikilinks, normalize_link_target, parse_page  # noqa: E402

# Nodes [1]-[11] are the routing hubs, named after topics rather than sources.
HUB_NODES = {str(i) for i in range(1, 12)}

# Titles shorter than this are matched only as wikilinks. "main", "AG" and "out"
# are real page titles here and would match inside ordinary words.
MIN_TITLE_LEN_FOR_PROSE = 8

NEAR_EXACT = 0.95      # accept on title alone at or above this containment

# Below NEAR_EXACT, a bag-of-words threshold cannot separate the cases. Tuning it
# failed in both directions:
#   0.60 accepted "Evidence of Intraday Multifractality in European Stock
#        Markets" as node [17], "COVID-19 Impact on European Stock Market
#        Multifractality" -- same authors, same topic words, different paper.
#   0.75 rejected node [59], "DR-ACI: Doubly Robust Adaptive Conformal Inference
#        (2026)", which really is the DR-ACI paper. It scored 0.71.
#
# The distinction is not how MANY words overlap but WHICH. A true shortening
# keeps the distinctive opening phrase of the title ("Doubly Robust Adaptive
# Conformal Inference", "Learn Then Test"); a look-alike shares only trailing
# topic words ("European Stock Market"). So match the source's LEADING tokens as
# a contiguous run, and require an author match on top.
LEAD_TOKENS = 4        # how many leading significant tokens to consider
LEAD_MIN_RUN = 3       # how many of them must appear contiguously in the node

# Curator's own ranking, from `mind_map_priority` frontmatter.
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}

STOPWORDS = {
    "a", "an", "the", "of", "for", "and", "in", "on", "to", "with", "under",
    "via", "from", "using", "by", "its", "at", "is", "are", "toward", "towards",
}

COVERAGE_RE = re.compile(
    r"Coverage as of (\d{4}-\d{2}-\d{2}):\s*\*\*(\d+) sources, "
    r"(\d+) entities, (\d+) concepts\*\*"
)
NODE_RE = re.compile(r"^\[(\d+)\]\s*(.*)$", re.M)
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
SLUG_YEAR_RE = re.compile(r"-(\d{4})(?:-|$)")


def tokens(text: str) -> set[str]:
    text = re.sub(r"[^\w\s]", " ", text.lower())
    return {t for t in text.split() if t and t not in STOPWORDS and len(t) > 2}


def surnames(authors) -> list[str]:
    """Last name of each author.

    `authors:` appears in two shapes and both must be handled:
        ['Anastasios N. Angelopoulos', 'Emmanuel J. Candes']
        ['entities/chen-xu', 'entities/yao-xie']
    Treating the second as a name matches nothing, which once reported
    xu-2022-spci as missing although it is node [108], "Xu SPCI".
    """
    if not authors:
        return []
    if isinstance(authors, str):
        authors = [authors]
    out = []
    for name in authors:
        if not isinstance(name, str) or not name.strip():
            continue
        if "/" in name:                                   # entity page_id form
            parts = [p for p in name.rsplit("/", 1)[-1].split("-") if len(p) > 1]
            if parts:
                out.append(parts[-1].capitalize())
            continue
        parts = [p.strip(" .,;()") for p in name.split()]
        parts = [p for p in parts if len(p) > 1]          # drop initials
        if parts:
            out.append(parts[-1])
    return out


def parse_nodes(map_text: str) -> list[dict]:
    nodes = []
    for num, body in NODE_RE.findall(map_text):
        bold = BOLD_RE.search(body)
        title = bold.group(1) if bold else ""
        nodes.append({
            "num": num,
            "title": title,
            "text": body,
            "tokens": tokens(title),
            "is_hub": num in HUB_NODES,
        })
    return nodes


def names_author(node: dict, people: list[str]) -> bool:
    return any(re.search(rf"\b{re.escape(p)}\b", node["text"]) for p in people)


def significant_sequence(text: str) -> list[str]:
    """Ordered significant tokens -- order matters here, unlike tokens()."""
    words = re.sub(r"[^\w\s]", " ", text.lower()).split()
    return [w for w in words if w not in STOPWORDS and len(w) > 2]


def leading_phrase_matches(source_title: str, node_title: str) -> bool:
    """Does the node title carry the source title's distinctive opening phrase?

    Titles put the distinctive part first ("Doubly Robust Adaptive Conformal
    Inference ..."), and a shortened node title keeps it. A look-alike shares
    only trailing topic words, which this ignores by construction.
    """
    lead = significant_sequence(source_title)[:LEAD_TOKENS]
    if len(lead) < LEAD_MIN_RUN:
        return False
    node_seq = significant_sequence(node_title)
    if not node_seq:
        return False
    joined = " ".join(node_seq)
    # Try the longest run first: 4 tokens beats 3.
    for size in range(len(lead), LEAD_MIN_RUN - 1, -1):
        if f" {' '.join(lead[:size])} " in f" {joined} ":
            return True
    return False


def classify(page, meta, map_text, nodes, links) -> str | None:
    """Return the reason this source is covered, or None."""
    page_id = meta.get("page_id") or ""
    title = (meta.get("title") or "").strip()
    people = surnames(meta.get("authors"))

    if page_id in links or page.stem in links or (title and title in links):
        return "wikilink"

    if title and len(title) >= MIN_TITLE_LEN_FOR_PROSE and re.search(
        rf"\b{re.escape(title)}\b", map_text, re.IGNORECASE
    ):
        return "exact title"

    detail = [n for n in nodes if not n["is_hub"]]
    title_tokens = tokens(title)
    if title_tokens:
        for node in detail:
            if not node["tokens"]:
                continue
            overlap = len(title_tokens & node["tokens"]) / min(
                len(title_tokens), len(node["tokens"])
            )
            if overlap >= NEAR_EXACT:
                return f"near-exact title [{node['num']}]"
            if leading_phrase_matches(title, node["title"]) and names_author(
                node, people
            ):
                return f"lead-phrase+author [{node['num']}]"

    # An "author + year appear in the same node" signal was tried and REMOVED.
    # It reads as reasonable and is not: a node needs only to mention one of the
    # authors and any matching four-digit number. It accepted "Claude Code: The
    # Definitive Guide to Agentic Development" and "How We Built Our Multi-Agent
    # Research System" as covered by node [56], which is Huyen's AI Engineering,
    # and "Learn Then Test" as covered by a node about Vovk's 2012
    # cross-conformal predictors. Every one of those is a real gap it would have
    # hidden. Prolific authors make this failure systematic, not incidental.
    #
    # Over-reporting costs a check. Under-reporting loses the work entirely.

    return None


def self_reported(map_text: str) -> dict | None:
    m = COVERAGE_RE.search(map_text)
    if not m:
        return None
    return {"as_of": m.group(1), "sources": int(m.group(2)),
            "entities": int(m.group(3)), "concepts": int(m.group(4))}


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--wiki", default="wiki")
    ap.add_argument("--threshold", type=int, default=20,
                    help="exit 1 above this many uncovered sources (default: 20)")
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--show-covered", action="store_true",
                    help="list each covered source and why it was accepted")
    args = ap.parse_args()

    wiki_root = Path(args.wiki)
    try:
        wiki = Wiki(wiki_root)
    except Exception as exc:
        print(f"could not open wiki at {wiki_root}: {exc}", file=sys.stderr)
        return 2

    mind_map = wiki_root / "MIND_MAP.md"
    if not mind_map.exists():
        print(f"MIND_MAP.md not found at {mind_map}", file=sys.stderr)
        return 2
    map_text = mind_map.read_text(encoding="utf-8")

    nodes = parse_nodes(map_text)
    links = {t for t in (normalize_link_target(x)
                         for x in extract_wikilinks(map_text)) if t}

    # Inbound link counts across the whole wiki, for ranking the worklist.
    inbound: dict[str, int] = collections.Counter()
    titles_to_id: dict[str, str] = {}
    sources = []
    for path in wiki.list_pages():
        try:
            meta, body = parse_page(path)
        except Exception:
            continue
        pid = meta.get("page_id")
        if pid and meta.get("title"):
            titles_to_id.setdefault(meta["title"], pid)
        if meta.get("page_type") == "source" and pid:
            sources.append((path, meta))
        for raw in extract_wikilinks(body):
            target = normalize_link_target(raw)
            if target:
                inbound[target] += 1

    covered, missing = {}, {}
    for path, meta in sources:
        pid = meta["page_id"]
        reason = classify(path, meta, map_text, nodes, links)
        n_in = inbound.get(pid, 0) + inbound.get(meta.get("title", ""), 0)
        entry = {"page_id": pid, "title": meta.get("title", ""),
                 "priority": meta.get("mind_map_priority"), "inbound": n_in,
                 "reason": reason}
        (covered if reason else missing)[pid] = entry

    ranked = sorted(
        missing.values(),
        key=lambda e: (PRIORITY_ORDER.get(e["priority"], 3), -e["inbound"]),
    )

    if args.json:
        print(json.dumps({
            "totals": {"sources": len(sources), "covered": len(covered),
                       "missing": len(missing)},
            "by_signal": dict(collections.Counter(
                e["reason"].split(" [")[0] for e in covered.values())),
            "self_reported": self_reported(map_text),
            "uncovered_sources": ranked,
            "covered_sources": sorted(covered.values(), key=lambda e: e["page_id"]),
        }, indent=2, ensure_ascii=False))
        return 1 if len(missing) > args.threshold else 0

    print("=== MIND_MAP source coverage ===")
    print(f"  source pages : {len(sources)}")
    print(f"  has a node   : {len(covered)}")
    print(f"  NO node      : {len(missing)}")
    print("\n  accepted by signal:")
    for sig, n in collections.Counter(
        e["reason"].split(" [")[0] for e in covered.values()
    ).most_common():
        print(f"    {n:4d}  {sig}")

    claim = self_reported(map_text)
    if claim:
        print(f"\n  MIND_MAP self-reports, as of {claim['as_of']}: "
              f"{claim['sources']} sources, {claim['entities']} entities, "
              f"{claim['concepts']} concepts")

    if args.show_covered:
        print("\n=== Covered, with the reason (audit these) ===")
        for e in sorted(covered.values(), key=lambda e: e["reason"]):
            print(f"  {e['reason']:<26} {e['title'][:60]}")

    print("\n=== Worklist: sources with no node ===")
    print("(ranked by mind_map_priority -- the curator's own call -- then inbound links)")
    if not ranked:
        print("  none")
    for e in ranked[:args.limit]:
        print(f"  {e['priority'] or '-':<6} {e['inbound']:3d} inbound  {e['title'][:62]}")
    if len(ranked) > args.limit:
        print(f"  ... and {len(ranked) - args.limit} more (raise --limit)")

    over = len(missing) > args.threshold
    print(f"\ndrift threshold {args.threshold}: "
          f"{'EXCEEDED' if over else 'within limit'}")
    print("This script writes nothing. MIND_MAP.md is curated by hand.")
    return 1 if over else 0


if __name__ == "__main__":
    raise SystemExit(main())
