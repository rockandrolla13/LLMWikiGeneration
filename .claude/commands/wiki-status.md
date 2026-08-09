Show wiki health: size, integrity checks, broken links, and what needs writing. $ARGUMENTS

Run this from the repository root. The wiki lives in `wiki/`, not `.`.

```python
import sys, collections
from pathlib import Path

sys.path.insert(0, "src")

from llm_wiki import Wiki, wiki_stats, wiki_freshness
from llm_wiki.io import parse_page, extract_wikilinks, normalize_link_target
from llm_wiki.verify import verify_wiki

WIKI = Path("wiki")          # the vault: contains schema.yml, manifest.jsonl, wiki/
wiki = Wiki(WIKI)

# ---------------------------------------------------------------- size
stats = wiki_stats(wiki)
print("=== Wiki ===")
print(f"Name    : {stats['wiki_name']}")
print(f"Topic   : {stats['wiki_topic']}")
print(f"Pages   : {stats['total_pages']}")
print(f"  sources        {stats['total_sources']}")
print(f"  concepts       {stats['total_concepts']}")
print(f"  entities       {stats['total_entities']}")
print(f"  analyses       {stats['total_analyses']}")
print(f"  contradictions {stats['total_contradictions']}")
print(f"Ledger  : {stats['total_operations']} operations, {stats['total_ingests']} ingests")

# ---------------------------------------------------------------- schema
v2 = sum(1 for p in wiki.list_pages()
         if (parse_page(p)[0].get("schema_version") == 2))
total = stats["total_pages"]
print(f"Schema  : {v2}/{total} pages on v2" + ("" if v2 == total else "  <- migrate the rest"))

# ---------------------------------------------------------------- integrity
print()
print("=== Integrity ===")
report = verify_wiki(wiki)
print(f"{report.passed}/{report.total_checks} checks pass")
for r in report.results:
    if not r.passed:
        print(f"  FAIL  {r.name}: {r.message}")

# ---------------------------------------------------------------- gaps
print()
print("=== Missing pages ===")
targets = set()
for p in wiki.list_pages():
    targets.add(p.stem)
    targets.add(str(p.relative_to(wiki.wiki_dir).with_suffix("")))
    try:
        meta, _ = parse_page(p)
    except Exception:
        continue
    if meta.get("title"):
        targets.add(meta["title"])
    if meta.get("page_id"):
        targets.add(meta["page_id"])

missing = collections.Counter()
for p in wiki.list_pages():
    try:
        _, body = parse_page(p)
    except Exception:
        continue
    for link in extract_wikilinks(body):
        t = normalize_link_target(link)
        if t and t not in targets:
            missing[t] += 1

print(f"{sum(missing.values())} links point at {len(missing)} pages that do not exist")
for name, n in missing.most_common(10):
    print(f"  {n:3d}x  {name}")

# ---------------------------------------------------------------- derived
print()
print("=== Derived files ===")
fresh = wiki_freshness(wiki)
for name, s in fresh["artifacts"].items():
    state = "fresh" if s["is_fresh"] else "stale"
    print(f"  {name:16s} {state}")

# ---------------------------------------------------------------- last rebuilt
# The ledger already records this -- do not invent a separate flag file, it would
# become a second source of truth that drifts. Note the key is `op_type`, not
# `operation_type`; querying the wrong name silently returns zero rebuilds.
import json

print()
print("=== Last rebuilt ===")
rebuilds = []
for line in (WIKI / "manifest.jsonl").read_text().splitlines():
    line = line.strip()
    if not line:
        continue
    try:
        op = json.loads(line)
    except json.JSONDecodeError:
        continue
    if op.get("op_type") == "rebuild":
        rebuilds.append(op)

if not rebuilds:
    print("  index.md / index.full.md : never rebuilt through wiki_rebuild()")
else:
    latest = {}
    for op in rebuilds:                       # ledger is append-ordered
        for art in op.get("outputs", {}).get("rebuilt", []):
            latest[art] = op["timestamp"]
    for art in ("index.md", "index.full.md"):
        print(f"  {art:16s} {latest.get(art, 'never')}")
    print(f"  ({len(rebuilds)} rebuild operations in the ledger)")

# MIND_MAP.md is never machine-rebuilt, so it needs a different clock: its last
# git commit, and its own self-reported coverage versus today's counts.
import re
import subprocess

mm = WIKI / "MIND_MAP.md"
try:
    edited = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", str(mm)],
        capture_output=True, text=True, check=True,
    ).stdout.strip() or "uncommitted"
except Exception:
    edited = "unknown (git unavailable)"
print(f"  {'MIND_MAP.md':16s} {edited}  (hand-curated -- rebuild refuses to overwrite it)")

m = re.search(
    r"Coverage as of (\d{4}-\d{2}-\d{2}):\s*\*\*(\d+) sources, (\d+) entities, (\d+) concepts\*\*",
    mm.read_text(),
)
if m:
    as_of, src, ent, con = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))
    drift = (stats["total_sources"] - src, stats["total_entities"] - ent,
             stats["total_concepts"] - con)
    print(f"    self-reported coverage as of {as_of}: "
          f"{src} sources, {ent} entities, {con} concepts")
    if any(d > 0 for d in drift):
        print(f"    NOT ON THE MAP since then: +{drift[0]} sources, "
              f"+{drift[1]} entities, +{drift[2]} concepts")
else:
    print("    no 'Coverage as of' line found -- cannot judge how stale it is")
```

## What the numbers mean

- **Numeric Provenance** compares every decimal figure on a source page against
  the document that page cites. It exists because two invented statistics were
  found in drafted pages. Pages counted `unverifiable` have no text source
  recorded -- add `source_path: markdown_output/<file>.md` to bring them in.
- **Integrity failures** are usually real. `Page Frontmatter` means pages are missing a
  required field. `Wikilinks` means pages link to something that was never written.
- **Missing pages** is the useful worklist. A page linked five times is worth writing
  before one linked once.
- **Stale derived files** just means `index.md` has not been regenerated since the last
  ingest. Fix with `wiki_rebuild(wiki, force=True)` — it will not touch `MIND_MAP.md`.

## Next actions

- `/wiki-ingest` — add sources
- `/wiki-query` — search and synthesise
- `wiki_rebuild(wiki, force=True)` — regenerate `index.md` and `index.full.md`
