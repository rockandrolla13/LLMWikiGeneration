# LLM Wiki

An LLM-maintained personal knowledge base. You add sources; Claude (or another LLM) maintains the wiki.

## What It Does

You drop documents into `raw/`. The LLM reads them, creates summaries, extracts entities and concepts, maintains cross-references, and keeps everything consistent. The wiki compounds over time.

```
raw/                    ← You add sources here (PDFs, markdown, notes)
    attention-paper.pdf
    my-notes.md

wiki/                   ← LLM maintains this
    sources/            ← Summary of each source
    entities/           ← People, orgs, places
    concepts/           ← Ideas, themes, topics
    analyses/           ← Syntheses, comparisons
    index.md            ← Auto-generated catalog

MIND_MAP.md             ← Grep-friendly knowledge graph
```

## Installation

```bash
# Clone and install
git clone <this-repo>
cd LLMWikiGeneration
pip install -e .

# Optional: Install OMEGA for cross-session memory
pip install omega-memory[server]
omega setup --hooks-only

# Verify
python -c "from llm_wiki import wiki_help, is_omega_available; print(f'OMEGA: {is_omega_available()}')"
```

## Quick Start with Slash Commands

Open this repo in Claude Code and use these commands:

| Command | What it does |
|---------|--------------|
| `/wiki-init` | Initialize a new wiki (interactive) |
| `/wiki-ingest` | Add a source document |
| `/wiki-query` | Search and answer questions |
| `/wiki-status` | Show wiki stats and OMEGA memory |
| `/wiki-guide` | Step-by-step tutorial |
| `/wiki-remember` | Store a decision/lesson in OMEGA |
| `/wiki-resume` | Resume work with session briefing |

Example session:
```
/wiki-init
> What topic? transformers and attention mechanisms
> Name? ML Research

/wiki-ingest raw/attention-paper.pdf

/wiki-query What is self-attention?

/wiki-remember lesson: Always link concepts back to source pages
```

## OMEGA Integration

OMEGA provides persistent memory across sessions. Your decisions, lessons, and work context are remembered.

```python
from llm_wiki import (
    is_omega_available,
    store_wiki_event,
    store_lesson,
    query_wiki_history,
    get_wiki_briefing,
)

# Check if OMEGA is available
if is_omega_available():
    # Store a decision
    store_wiki_event("decision", "Created entity page for Vaswani", "ml-wiki")

    # Store a lesson learned
    store_lesson("Entity pages need publication dates", "ml-wiki")

    # Query past work
    results = query_wiki_history("attention", "ml-wiki")

    # Get session briefing
    briefing = get_wiki_briefing("ml-wiki")
```

### What OMEGA Remembers

| Type | Purpose | Example |
|------|---------|---------|
| `decision` | Choices made | "Using JWT for auth" |
| `lesson` | Things learned | "Check for duplicates first" |
| `error` | Mistakes to avoid | "Don't create trivial concept pages" |
| `summary` | Work summaries | "Ingested 5 papers on transformers" |

### Cross-Session Continuity

Start each session with `/wiki-resume` to see:
- Recent decisions made
- Lessons learned
- Incomplete tasks (checkpointed)
- Activity summary

## Python API

```python
from pathlib import Path
from llm_wiki import Wiki, wiki_init, wiki_ingest, wiki_query

# 1. Initialize
wiki_init(Path("./my-wiki"), name="ML Research", topic="transformers")

# 2. Load wiki
wiki = Wiki(Path("./my-wiki"))

# 3. Add a source
wiki_ingest(wiki, Path("raw/paper.pdf"), title="Attention Is All You Need")

# 4. Query
result = wiki_query(wiki, "What is self-attention?")
```

## Commands Reference

### Core Operations

| Command | Purpose |
|---------|---------|
| `wiki_init(path, name, topic)` | Create new wiki |
| `wiki_ingest(wiki, source)` | Add source document |
| `wiki_query(wiki, question)` | Search and answer |
| `wiki_stats(wiki)` | Statistics |
| `wiki_rebuild(wiki)` | Regenerate index, mind map |
| `wiki_freshness(wiki)` | Check what needs updating |
| `wiki_find_links(wiki, page_id)` | Find page connections |

### OMEGA Functions

| Function | Purpose |
|----------|---------|
| `is_omega_available()` | Check if OMEGA installed |
| `store_wiki_event(type, content, wiki)` | Store decision/lesson/error |
| `store_lesson(lesson, wiki)` | Store a lesson learned |
| `query_wiki_history(query, wiki)` | Search past work |
| `get_wiki_briefing(wiki)` | Get session briefing |
| `checkpoint_task(id, state, wiki)` | Save task for later |
| `resume_task(id)` | Resume checkpointed task |

### Help Commands

```python
from llm_wiki import wiki_help, wiki_guide, wiki_structure

wiki_help()              # List all commands
wiki_help("ingest")      # Details on specific command
wiki_guide()             # Step-by-step walkthrough
wiki_guide(step=1)       # Specific step
wiki_structure()         # Directory layout explained
```

## Directory Structure (3 Tiers)

### Tier 1: Source of Truth
Committed to git. Never auto-deleted.

```
schema.yml          # Wiki configuration
manifest.jsonl      # Append-only operation log
raw/                # Your source documents (immutable)
wiki/sources/       # Source summaries
wiki/entities/      # Entity pages
wiki/concepts/      # Concept pages
wiki/analyses/      # Analysis pages
```

### Tier 2: Derived
Regenerated from Tier 1. Safe to delete.

```
wiki/index.md       # Master catalog
wiki/log.md         # Operation history
MIND_MAP.md         # Knowledge graph
```

Regenerate with: `wiki_rebuild(wiki, force=True)`

### Tier 3: Ephemeral (OMEGA)
Session context. Persisted in OMEGA, not in wiki.

```
~/.omega/omega.db   # OMEGA memory database
```

Functions:
- `wiki_session_start()` - Start tracking
- `wiki_session_status()` - Check status
- `wiki_session_end()` - End session
- `store_wiki_event()` - Store in OMEGA
- `get_wiki_briefing()` - Retrieve from OMEGA

## Multiple Topics

Create separate wikis for different interests:

```python
wiki_init(Path("./wikis/ml-research"), name="ML Research", topic="...")
wiki_init(Path("./wikis/philosophy"), name="Philosophy", topic="...")
wiki_init(Path("./wikis/work"), name="Work Projects", topic="...")
```

Each wiki is independent with its own sources, pages, and configuration.
OMEGA memory is shared across all wikis (filtered by wiki name).

## How It Works

1. **You** add source documents to `raw/`
2. **LLM** reads sources, creates wiki pages, maintains links
3. **OMEGA** remembers decisions and lessons across sessions
4. **You** ask questions, LLM searches and synthesizes
5. **Wiki** compounds - cross-references grow, contradictions get flagged
6. **You** browse in Obsidian, VS Code, or any markdown viewer

The key insight: the wiki is the artifact, not the chat. Knowledge is compiled once and maintained, not re-derived per query.

## Configuration

`schema.yml` controls wiki behavior:

```yaml
name: "My Wiki"
topic: "machine learning"
profile: "research"  # research | reading | personal | business

taxonomy:
  sources_dir: "sources"
  entities_dir: "entities"
  concepts_dir: "concepts"

mind_map:
  target_nodes: 30
  max_nodes: 50
```

## Development

```bash
# Run tests
pytest tests/ -v

# Test count: 325
# - Core wiki: 292 tests
# - OMEGA integration: 33 tests
```

## Architecture

```
src/llm_wiki/
├── core/           # Protocols and types
├── io/             # File I/O (hashing, wikilinks, page parsing)
├── registry/       # Pluggable checks (8) and compilers (2)
├── factories/      # Page creation (5 factories)
├── integrations/   # OMEGA integration
├── commands.py     # High-level operations
├── wiki.py         # Wiki class
├── manifest.py     # Operation logging
└── session.py      # Session context

.claude/commands/   # Slash commands for Claude Code
├── wiki-init.md
├── wiki-ingest.md
├── wiki-query.md
├── wiki-guide.md
├── wiki-status.md
├── wiki-remember.md
└── wiki-resume.md
```

## License

MIT
