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
print("MIND_MAP.md is hand-curated; rebuild refuses to overwrite it.")
```

## What the numbers mean

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
