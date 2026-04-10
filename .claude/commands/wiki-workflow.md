# LLM Wiki Workflow

Interactive workflow for managing your wiki with Obsidian as the visual frontend.

## Environment Check

```python
import subprocess
import sys

# Check conda environment
result = subprocess.run(["conda", "info", "--envs"], capture_output=True, text=True)
if "llm-wiki" not in result.stdout:
    print("ERROR: conda env 'llm-wiki' not found")
    print("Run: conda create -n llm-wiki python=3.11 && conda activate llm-wiki && pip install -e .")
    sys.exit(1)

# Check imports
from llm_wiki import Wiki, wiki_stats, wiki_help
from llm_wiki.integrations.omega import is_omega_available
print("✓ llm-wiki loaded")
print(f"✓ OMEGA: {'available' if is_omega_available() else 'not installed'}")
```

## Workflow Steps

### Step 1: Check Wiki Status

Show current wiki state:
```python
from pathlib import Path
from llm_wiki import Wiki, wiki_stats

wiki = Wiki(Path("."))
if wiki.exists():
    stats = wiki_stats(wiki)
    print(f"Wiki: {stats['wiki_name']}")
    print(f"Topic: {stats['wiki_topic']}")
    print(f"Pages: {stats['total_pages']}")
    print(f"Sources: {stats.get('source_count', 0)}")
    print(f"Entities: {stats.get('entity_count', 0)}")
    print(f"Concepts: {stats.get('concept_count', 0)}")
else:
    print("No wiki found. Run /wiki-init first.")
```

### Step 2: Ingest a Source

If user provides a file path in $ARGUMENTS, ingest it:
```python
# Parse $ARGUMENTS for file path
# Read the source file
# Discuss key takeaways with user
# Create source page with summary, key claims, entities, concepts
# Update related pages
# Log the operation
```

Use /wiki-ingest for the full ingest workflow.

### Step 3: Query the Wiki

If user provides a question in $ARGUMENTS:
```python
# Search wiki pages for relevant content
# Synthesize answer with citations
# Offer to save as analysis page
```

Use /wiki-query for the full query workflow.

### Step 4: View in Obsidian

Remind user:
- Graph View shows connections (colored by type)
- dashboard.md has Dataview tables
- All changes appear in real-time

## Quick Actions

Based on $ARGUMENTS, route to the appropriate action:

| Input | Action |
|-------|--------|
| (empty) | Show status and menu |
| `ingest <path>` | Ingest a source |
| `query <question>` | Search and answer |
| `status` | Show wiki stats |
| `graph` | Remind to check Obsidian graph |
| `help` | Show available commands |

## Menu

If no arguments provided, show this menu:

```
=== LLM Wiki Workflow ===

What would you like to do?

1. /wiki-ingest <file>  - Add a source document
2. /wiki-query <question> - Search and answer
3. /wiki-status - Show wiki statistics  
4. /wiki-guide - Step-by-step tutorial

Obsidian Views:
- Open Graph View to see connections
- Open dashboard.md for Dataview tables
- All changes sync automatically

Current Status:
[Show wiki_stats output]
```
