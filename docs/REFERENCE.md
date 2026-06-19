# LLM Wiki Reference

> This file is the detailed operational reference. Load it when you need command syntax,
> workflow checklists, or integration details. It is NOT auto-loaded every session.
> See CLAUDE.md for the session startup protocol.

---

## Command Reference

**All operations in one view.** Use slash commands in Claude Code or Python API for scripting.

| Operation | Slash Command | Python Function | Tier Effect | Common Use |
|-----------|---------------|-----------------|-------------|------------|
| **Core Operations** |||||
| Initialize wiki | `/wiki-init` | `wiki_init(root, name, topic, profile="default")` | Creates T1 | First-time setup |
| Add source | `/wiki-ingest <file>` | `wiki_ingest(wiki, path, title=None, tags=[])` | Writes T1+T2 | Process new document |
| Search wiki | `/wiki-query <q>` | `wiki_query(wiki, query, page_types=None, tags=None)` | Reads T1+T2, writes T3 | Ask questions |
| Rebuild artifacts | — | `wiki_rebuild(wiki, force=False)` | Regenerates T2 from T1 | Fix corruption |
| **Inspection** |||||
| Show statistics | `/wiki-status` | `wiki_stats(wiki)` | Reads T1+T2 | Health check |
| Check freshness | — | `wiki_freshness(wiki)` | Reads T1+T2 | Detect stale artifacts |
| Find links | — | `wiki_find_links(wiki, page_id)` | Reads T2 | Debug connections |
| **Session** |||||
| Start tracking | — | `wiki_session_start(wiki)` | Initializes T3 | Begin work session |
| End tracking | — | `wiki_session_end(save_to_temp=False)` | Clears T3 | Finish work session |
| Session info | — | `wiki_session_status()` | Reads T3 | Debug session state |
| **Navigation** |||||
| Main hub | `/wiki` | — | — | Status + menu |
| Tutorial | `/wiki-guide` | `wiki_guide(step=None)` | — | Learn workflows |
| Help | — | `wiki_help(command=None)` | — | Command reference |
| Structure guide | — | `wiki_structure(wiki=None)` | — | Understand layout |
| Full workflow | `/wiki-workflow` | — | — | Guided process |
| **OMEGA Integration** (if installed) |||||
| Store memory | `/wiki-remember <text>` | `store_wiki_event(type, content, wiki)` | Writes OMEGA DB | Save decision/lesson |
| Session briefing | `/wiki-resume` | `get_wiki_briefing(wiki, limit=20)` | Reads OMEGA DB | Resume from last session |

**Tier Legend:**
- **T1** = Source of Truth (schema.yml, manifest.jsonl, raw/, wiki/) — must be backed up
- **T2** = Derived Artifacts (index.md, log.md) — regenerate with `wiki_rebuild()`
- **T1\*** = `wiki/MIND_MAP.md` is handcrafted Tier 1, NOT regenerable (see CLAUDE.md)
- **T3** = Ephemeral (session context, navigation history) — lost on session end

**Python Quick Start:**
```python
from pathlib import Path
from llm_wiki import Wiki, wiki_init, wiki_ingest, wiki_query

# Initialize
wiki_init(Path("."), name="Research", topic="transformers")

# Use
wiki = Wiki(Path("."))
wiki_ingest(wiki, Path("raw/paper.pdf"))
wiki_query(wiki, "What is self-attention?")
```

---

## Document Processing Tools

**MANDATORY: Use these tools before ingesting documents.**

| Tool | Purpose | Command | Status |
|------|---------|---------|--------|
| **pymupdf4llm** | PDF → Markdown + images | `/wiki-convert <pdf>` | ✓ Installed |
| **grobid-client** | Citation/reference extraction | Python API | ✓ Installed (needs server) |
| **pix2text** | Math equation OCR (LaTeX) | Python API | Not installed |

### PDF Conversion (Required)

**PDFs cannot be ingested directly.** Always convert first:

```bash
# Using skill (recommended)
/wiki-convert raw/paper.pdf

# Manual command
conda run -n llm-wiki python test_marker.py "path/to/paper.pdf"
```

**Output location:** `markdown_output/<filename>.md` + `markdown_output/<filename>_images/`

### Tool Chain for Academic Papers

For complex academic papers with equations, citations, and figures:

1. **Text + Images:** `/wiki-convert` (pymupdf4llm) - fast, CPU-only
2. **Citations:** `grobid-client` - when GROBID server available
3. **Equations:** `pix2text` - if installed, converts math to LaTeX

### Installing Additional Tools

```bash
# Math OCR (Mathpix alternative)
pip install pix2text

# Start local GROBID (requires Docker)
docker run -d --name grobid -p 8070:8070 grobid/grobid:0.8.0
```

---

## Core Concepts

### The 3-Tier Data Model

LLM Wiki separates data by **durability** and **ownership**:

```
TIER 1 - Source of Truth (committed, version-controlled)
├── schema.yml           Wiki config (name, topic, taxonomy)
├── manifest.jsonl       Append-only operation log (audit trail)
├── raw/                 Source documents (user writes, LLM reads)
│   └── *.pdf, *.md      Immutable once added
└── wiki/                LLM-generated pages (LLM writes, user reads)
    ├── sources/         Summary of each raw source
    ├── entities/        People, organizations, places
    ├── concepts/        Ideas, themes, topics
    ├── analyses/        Comparisons, syntheses, saved answers
    ├── contradictions/  Conflicting claims flagged for resolution
    └── MIND_MAP.md      Handcrafted knowledge graph — T1, NOT regenerable

TIER 2 - Derived Artifacts (regenerated from Tier 1)
├── wiki/index.md        Master catalog (auto-generated)
└── wiki/log.md          Operation history (auto-generated)

TIER 3 - Ephemeral (session-only, not persisted)
├── ~/.omega/omega.db    OMEGA persistent memory (optional)
└── Session context      Navigation history, working pages, focus
```

**Recovery:** If T2 is lost → run `wiki_rebuild()`. If T3 is lost → wiki still fully functional. Only T1 requires backup. MIND_MAP.md is T1 — do not delete it.

### Page Types

| Type | Directory | Purpose | Link Target |
|------|-----------|---------|-------------|
| `source` | `wiki/sources/` | Summary of ingested document | 3-7 links |
| `entity` | `wiki/entities/` | Person, organization, place | 5-10 links |
| `concept` | `wiki/concepts/` | Idea, theme, methodology | 5-15 links |
| `analysis` | `wiki/analyses/` | Comparison, synthesis, saved answer | 10+ links |
| `contradiction` | `wiki/contradictions/` | Conflicting claims to resolve | 3-5 links |

**Frontmatter (all pages):**
```yaml
---
title: Page Title
page_id: concepts/attention              # Must match file path
page_type: concept
revision_id: 1
revision_hash: sha256:abc123...          # Content hash for verification
created: 2024-01-15T10:00:00Z
updated: 2024-01-15T10:00:00Z
updated_by: op_xyz123                    # Operation ID from manifest
tags: [nlp, transformers]
sources: [sources/vaswani-2017]          # Which sources mention this
related: [concepts/transformers]         # Bidirectional links
mind_map_priority: high                  # high | medium | low
---
```

### MIND_MAP Format

**Purpose:** Grep-friendly knowledge graph. Each node is one line with embedded `[N]` cross-references.

**Status:** Tier 1 / handcrafted. The Python `MindMapCompiler` produces only a 50-node routing stub. The real map has 211+ thematic nodes written and curated over time. Do NOT overwrite with a rebuild.

**Structure:**
```
[1] **Overview** - Top-level context. This wiki covers [2, 3, 4, 5].
[2] **Sources** - Documents ingested. See [6] for first paper, [7] for second...
[3] **Entities** - Key people and organizations. [8] is the lead author...
[4] **Concepts** - Core ideas. Self-attention [9] enables transformers [10]...
[5] **Analyses** - Saved insights. Comparison of architectures [11]...
[6] **Attention Is All You Need** - Vaswani et al (2017) introduced [9]...
...
```

**Search patterns:**
```bash
grep "^\[5\]" MIND_MAP.md              # Get node 5
grep "\[5\]" MIND_MAP.md               # All references to node 5
grep -i "transformer" MIND_MAP.md      # Find by keyword
```

**Nodes 1-5 are routing hubs. Nodes 6+ are detail pages.**

---

## Workflows

### Standard Execution Template

**All wiki operations follow: Design → Work → Verify**

#### Design Phase (Orientation)
- [ ] Read inputs completely (source documents, user query, current wiki state)
- [ ] Identify what to extract/update: entities, concepts, contradictions
- [ ] Discuss key decisions with user: what to emphasize, how to organize
- [ ] Plan which pages to create/update

#### Work Phase (Execution)
- [ ] Create or update wiki pages with complete YAML frontmatter
- [ ] Ensure bidirectional wikilinks (if A links to B, B links to A)
- [ ] Update `wiki/index.md` with new/changed pages
- [ ] Do NOT update MIND_MAP.md inline — MIND_MAP is T1/handcrafted; update deferred to explicit rebuild
- [ ] Maintain link density targets (see [Page Types](#page-types))

#### Verify Phase
- [ ] All pages have required frontmatter fields
- [ ] All wikilinks resolve to existing pages (no broken links)
- [ ] Contradiction check completed and documented (even if result is none found)
- [ ] Operation logged in `manifest.jsonl`
- [ ] Human-readable entry appended to `wiki/log.md`

### Operation-Specific Workflows

#### Ingest a New Source

**Extends standard template with:**

**Design Phase additions:**
- [ ] What is the main thesis or contribution?
- [ ] Which entities (people, orgs, places) are mentioned?
- [ ] Which concepts does this introduce or relate to?
- [ ] Does this contradict existing wiki claims?

**Work Phase additions:**
- [ ] Create summary page in `wiki/sources/` with:
  - One-paragraph summary
  - Key claims (bulleted)
  - Notable quotes
  - Questions raised
- [ ] Create or update entity pages in `wiki/entities/`
- [ ] Create or update concept pages in `wiki/concepts/`
- [ ] Search existing concept pages for claims conflicting with new source's key claims
- [ ] If contradictions found: create page in `wiki/contradictions/` (REQUIRED, not optional)
- [ ] If no contradictions: note "No contradictions found" in ingest log
- [ ] Do NOT update MIND_MAP.md inline — MIND_MAP is T1/handcrafted; update deferred to explicit rebuild

#### Answer a Query

**Extends standard template with:**

**Design Phase:**
- [ ] Read `MIND_MAP.md` first for knowledge graph orientation
- [ ] Read `wiki/index.md` to identify relevant pages
- [ ] Determine which page types are most relevant

**Work Phase:**
- [ ] Read 3-7 relevant wiki pages
- [ ] Synthesize answer with `[[wikilink]]` citations to wiki pages
- [ ] If answer is valuable: offer to save as `wiki/analyses/[topic].md`
- [ ] If saved: create analysis page with links to sources

**Verify Phase:**
- [ ] All claims cite wiki pages (not raw sources directly)
- [ ] Analysis page (if created) has 10+ bidirectional links

#### Maintain the Wiki

**Health check targets:**
- [ ] **Orphan pages** - pages with no inbound links (should be reachable)
- [ ] **Broken links** - wikilinks to non-existent pages
- [ ] **One-way links** - A links to B but B doesn't link back
- [ ] **Contradictions** - unresolved conflicts in `wiki/contradictions/`
- [ ] **Missing pages** - frequently mentioned but no dedicated page
- [ ] **Stale MIND_MAP** - nodes don't reflect current wiki state
- [ ] **Coverage gaps** - important topics with thin content
- [ ] **Unanswered questions** - queries the wiki can't yet address

**Execute:** `wiki_rebuild(wiki, force=True)` to regenerate all T2 artifacts (index.md, log.md only — does NOT touch MIND_MAP).

---

## Integrations

### Obsidian (Visual Frontend)

**Purpose:** Display the wiki. LLM writes; Obsidian visualizes.

**Launch:**
```bash
obsidian  # Open wiki/ as vault on first launch
```

**Pre-configured features:**
- Graph view (Ctrl+G) - Visual knowledge graph, identify hubs and orphans
- Quick switcher (Ctrl+O) - Fast page navigation
- Search in files (Ctrl+Shift+F) - Full-text search
- Dataview plugin - Dynamic tables based on frontmatter

**Workflow integration:**
- Use graph view during "Maintain the Wiki" to find orphans
- Use search to verify no broken references before verify phase

### OMEGA (Cross-Session Memory)

**Purpose:** Remember decisions, lessons, and patterns across sessions.

**Status:** Optional

**Key functions:**
```python
from llm_wiki.integrations.omega import (
    is_omega_available,
    store_wiki_event,
    get_wiki_briefing,
)

if is_omega_available():
    store_wiki_event("decision", "Use ISO dates", "my-wiki")
    briefing = get_wiki_briefing("my-wiki")
```

**Slash commands:**
```
/wiki-remember decision: Use snake_case for page IDs
/wiki-resume  # Get session briefing
```

**Event types:** `decision`, `lesson`, `error`, `summary`

**When to use:** After structure decisions, when discovering patterns, before breaks, after errors

---

## Architecture

### Extensibility (Registry Pattern)

**Built-in verification checks (8):**
Config Exists, Manifest Exists, Directory Structure, Page Frontmatter, Revision Hashes, Page IDs, Wikilinks, Manifest Operations

**Built-in artifact compilers (2):**
IndexCompiler (generates `wiki/index.md`), MindMapCompiler (generates a 50-node routing stub — does NOT replace the handcrafted MIND_MAP)

**Add custom checks or compilers:**
```python
from llm_wiki.registry import default_checks, default_compilers
from llm_wiki.core import VerificationCheck, DerivedArtifactCompiler

class MyCheck:
    @property
    def name(self) -> str:
        return "My Custom Check"

    def execute(self, wiki) -> VerificationResult:
        return VerificationResult(passed=True, message="OK")

default_checks.register("my_check", MyCheck())
```

---

## Appendices

### Linking Conventions

**Syntax:** `[[Page Title]]`, `[[Page Title#Section]]`, `[[Page Title|custom text]]`

**Bidirectional:** When A links to B, ensure B links back to A

**Link density targets:** sources (3-7), entities (5-10), concepts (5-15), analyses (10+), contradictions (3-5)

### CLI Power User Tricks

**Search the mind map:**
```bash
grep "^\[5\]" MIND_MAP.md              # Get node 5
grep "\[5\]" MIND_MAP.md               # All references to node 5
grep -i "keyword" MIND_MAP.md          # Case-insensitive search
```

**View recent operations:**
```bash
grep "^## \[" wiki/log.md | tail -5    # Last 5 operations
grep "ingest" wiki/log.md              # All ingest operations
```

**Find pages by type:**
```bash
find wiki/concepts -name "*.md"        # All concept pages
find wiki/sources -name "*.md"         # All source pages
find wiki -name "*.md" -mtime -7       # Modified in last 7 days
```

**Count pages:**
```bash
find wiki/sources -name "*.md" | wc -l     # Number of sources
find wiki/entities -name "*.md" | wc -l    # Number of entities
find wiki/concepts -name "*.md" | wc -l    # Number of concepts
```

**Batch operations:**
```bash
# Find pages with no frontmatter
for f in wiki/**/*.md; do
    head -1 "$f" | grep -q "^---$" || echo "$f"
done

# Find broken wikilinks (naive check)
grep -r "\[\[.*\]\]" wiki/ | grep -v "^wiki/index.md"
```

---

## File Management

**IMPORTANT: Always use symlinks for source documents, never copy files.**

When adding sources from external directories:
```bash
# CORRECT - create symlink
ln -s "/path/to/source/folder" wiki/raw/topic-name

# WRONG - do not copy files
cp /path/to/files/*.pdf wiki/raw/  # NEVER DO THIS
```

**Why symlinks:**
- Avoids duplicating large PDFs (saves disk space)
- Single source of truth for files
- Changes to originals automatically reflected
- Faster than copying

**Current source locations:**
```
wiki/raw/
└── conformal-prediction -> /home/ak/Documents/Conformal Prediction
```

**Adding new source collections:**
```bash
ln -s "/path/to/papers" wiki/raw/topic-name
```

---

## Getting Help

**Python API:**
```python
from llm_wiki import wiki_help, wiki_guide

wiki_help()              # Command reference
wiki_guide()             # Tutorial
```

**Slash commands:** `/wiki-guide`, `/wiki`, `/wiki-workflow`
