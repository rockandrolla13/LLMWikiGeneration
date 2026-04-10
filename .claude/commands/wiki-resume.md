Resume work on this wiki with OMEGA session briefing. $ARGUMENTS

Call this at the start of a new session to get context from previous work.

```python
from pathlib import Path
from llm_wiki import (
    Wiki, wiki_stats,
    is_omega_available, get_wiki_briefing, query_wiki_history,
)

wiki = Wiki(Path("."))

print(f"=== Resuming: {wiki.config.name} ===")
print(f"Topic: {wiki.config.topic}")
print()

# Get wiki stats
stats = wiki_stats(wiki)
print(f"Current state: {stats['total_pages']} pages, {stats['source_count']} sources")
print()

# Get OMEGA briefing
if is_omega_available():
    print("=== From Previous Sessions (OMEGA) ===")

    # Recent decisions
    decisions = query_wiki_history("decision", wiki.config.name, limit=5)
    if decisions:
        print("\nRecent decisions:")
        # Parse and display

    # Lessons learned
    lessons = query_wiki_history("lesson", wiki.config.name, limit=5)
    if lessons:
        print("\nLessons learned:")
        # Parse and display

    # Check for incomplete tasks
    print("\nChecking for incomplete tasks...")
    # Look for checkpointed tasks

    # Session briefing
    briefing = get_wiki_briefing(wiki.config.name, limit=5)
    if briefing:
        print("\nSession briefing:")
        for item in briefing:
            print(f"  - {item.get('content', '')[:100]}...")
else:
    print("OMEGA not available - no cross-session memory")
    print("Install with: pip install omega-memory[server]")

print()
print("Ready to continue. Use /wiki-query, /wiki-ingest, or /wiki-status")
```

This command helps you pick up where you left off by surfacing:
1. Recent decisions made
2. Lessons learned
3. Incomplete tasks (checkpointed)
4. Recent activity summary
