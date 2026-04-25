# Wiki Registry

**Last updated:** 2026-04-10

This file tracks all LLM Wiki installations on this system.

---

## Active Wikis

| Wiki | Path | Topic | Obsidian Vault? |
|------|------|-------|-----------------|
| **LLM Wiki** | `/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/wiki` | ML/Transformers | ✓ Yes |
| **Carry Strategy** | `/media/ak/10E1026C4FA6006E/GitRepos/CarryStrategyWiki/wiki` | Fixed Income | ✗ Not added |

---

## How This System Works

```
┌─────────────────────────────────────────────────────────────────┐
│                        YOUR WORKFLOW                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. YOU have PDFs in folders (e.g., /home/ak/Documents/...)    │
│                         │                                       │
│                         ▼                                       │
│  2. CLAUDE converts PDFs to markdown                           │
│     /wiki-convert path/to/paper.pdf                            │
│                         │                                       │
│                         ▼                                       │
│  3. CLAUDE ingests markdown into wiki pages                    │
│     /wiki-ingest markdown_output/paper.md                      │
│                         │                                       │
│                         ▼                                       │
│  4. Wiki pages are plain markdown files in wiki/ folder        │
│                         │                                       │
│                         ▼                                       │
│  5. OBSIDIAN displays the wiki/ folder as a visual vault       │
│     - Graph view shows connections                              │
│     - Click [[links]] to navigate                              │
│     - Obsidian reads files, doesn't modify them                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Why Obsidian Doesn't Update

Obsidian watches the folder for file changes. If it's not updating:

1. **Wrong folder open** - Make sure you opened the `wiki/` subfolder, not the parent
2. **Need to refresh** - Press `Ctrl+R` to reload the vault
3. **Vault not added** - The new wiki needs to be added as a vault

---

## Adding a New Vault to Obsidian

1. In Obsidian, click the vault icon (bottom left) or press `Ctrl+O` then click "Open another vault"
2. Click "Open folder as vault"
3. Navigate to the wiki folder (e.g., `/media/ak/10E1026C4FA6006E/GitRepos/CarryStrategyWiki/wiki`)
4. Click "Open"

Now you can switch between vaults using the vault switcher.

---

## Quick Commands

```bash
# See what wikis exist
find /media/ak/10E1026C4FA6006E/GitRepos -name "schema.yml" | xargs dirname

# Convert a PDF
/wiki-convert path/to/paper.pdf

# Ingest the converted markdown
/wiki-ingest markdown_output/paper.md

# Check wiki status
/wiki-status
```

---

## Source Document Locations

| Topic | Source Folder | Linked In Wiki |
|-------|---------------|----------------|
| Conformal Prediction | `/home/ak/Documents/Conformal Prediction` | LLMWikiGeneration |
| Carry Strategy | `/home/ak/Documents/CARRY STRATEGY` | CarryStrategyWiki |

---

## OMEGA Memory

Claude stores important decisions in OMEGA memory so they persist across sessions.
If Claude "forgets" something, it may need to query OMEGA at session start.

At the start of each session, Claude should run:
- `omega_welcome()` - Get context briefing
- `omega_protocol()` - Get operating instructions
