Show wiki status, statistics, and OMEGA memory summary. $ARGUMENTS

```python
from pathlib import Path
from llm_wiki import (
    Wiki, wiki_stats, wiki_freshness,
    is_omega_available, get_wiki_briefing, query_wiki_history,
)

wiki = Wiki(Path("."))

# Get wiki stats
print("=== Wiki Status ===")
stats = wiki_stats(wiki)
print(f"Name: {wiki.config.name}")
print(f"Topic: {wiki.config.topic}")
print(f"Pages: {stats['total_pages']}")
print(f"Links: {stats['total_links']}")
print(f"Sources: {stats['source_count']}")
print(f"Entities: {stats['entity_count']}")
print(f"Concepts: {stats['concept_count']}")

# Check freshness
print()
print("=== Freshness ===")
fresh = wiki_freshness(wiki)
if fresh['stale_pages']:
    print(f"Stale pages: {len(fresh['stale_pages'])}")
else:
    print("All pages up to date")

# OMEGA memory summary
if is_omega_available():
    print()
    print("=== OMEGA Memory ===")
    briefing = get_wiki_briefing(wiki.config.name, limit=5)
    if briefing:
        print(f"Recent memories: {len(briefing)}")
        for b in briefing[:3]:
            content = b.get('content', '')[:80]
            print(f"  - {content}...")

    # Show recent decisions
    decisions = query_wiki_history("decision", wiki.config.name, limit=3)
    lessons = query_wiki_history("lesson", wiki.config.name, limit=3)
    print(f"  Decisions stored: found results")
    print(f"  Lessons stored: found results")
else:
    print()
    print("=== OMEGA ===")
    print("Not installed. Install with: pip install omega-memory[server]")
```

Index files:
- wiki/wiki/index.md — lightweight summary (one line per page), used by /wiki-query
- wiki/wiki/index.full.md — full catalog with summaries and stats, use this for detailed
  maintenance inspection (page counts, summaries, broken links, etc.)

Offer next actions:
- /wiki-ingest to add more sources
- /wiki-query to search
- wiki_rebuild() if derived files are stale
