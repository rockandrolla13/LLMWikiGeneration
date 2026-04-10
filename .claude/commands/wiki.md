# Wiki Command Hub

Main entry point for LLM Wiki. Routes to specific commands based on action.

## Usage

```
/wiki                     → Show status + menu
/wiki status              → Wiki statistics
/wiki ingest <file>       → Add source document
/wiki query <question>    → Search and answer
/wiki graph               → Graph view reminder
/wiki help                → List all commands
```

## Implementation

```python
from pathlib import Path
from llm_wiki import Wiki, wiki_stats, wiki_help
from llm_wiki.integrations.omega import is_omega_available

wiki_path = Path(".")
wiki = Wiki(wiki_path)

# Parse $ARGUMENTS
args = "$ARGUMENTS".strip().lower()

if not args or args == "status":
    # Show status
    if wiki.exists():
        stats = wiki_stats(wiki)
        print(f"""
=== {stats['wiki_name']} ===
Topic: {stats['wiki_topic']}

Pages: {stats['total_pages']}
├── Sources:  {stats.get('source_count', 0)}
├── Entities: {stats.get('entity_count', 0)}
├── Concepts: {stats.get('concept_count', 0)}
└── Analyses: {stats.get('analysis_count', 0)}

OMEGA: {'✓ connected' if is_omega_available() else '✗ not installed'}

Quick Actions:
  /wiki ingest <file>   Add a source
  /wiki query <text>    Search wiki
  /wiki graph           Check Obsidian

Obsidian: Open Graph View or dashboard.md
""")
    else:
        print("No wiki found. Run /wiki-init to create one.")

elif args == "help":
    result = wiki_help()
    for category, commands in result['commands'].items():
        print(f"\n{category}:")
        for cmd, desc in commands.items():
            print(f"  {cmd}: {desc}")

elif args == "graph":
    print("""
=== Obsidian Graph View ===

Your wiki pages are color-coded:
  🔵 Blue   = sources/
  🟢 Green  = entities/
  🟣 Purple = concepts/
  🟠 Orange = analyses/

Actions:
1. Click Graph View icon in Obsidian sidebar
2. Hover nodes to see connections
3. Click a node to open the page
4. Use filters to show/hide types

The graph updates automatically as you add pages.
""")

elif args.startswith("ingest"):
    print("Use: /wiki-ingest <filepath>")
    print("Example: /wiki-ingest raw/paper.pdf")

elif args.startswith("query"):
    print("Use: /wiki-query <your question>")
    print("Example: /wiki-query What is self-attention?")

else:
    print(f"Unknown command: {args}")
    print("Try: /wiki help")
```
