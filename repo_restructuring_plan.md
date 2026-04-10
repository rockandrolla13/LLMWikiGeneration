# Repo Restructuring Implementation Plan

## Phase 1: Documentation Reorganization (30 minutes)

### Step 1.1: Create docs/ directory structure

```bash
mkdir -p docs/examples/{research,reading,personal}
mkdir -p .claude/skills/llm-wiki
```

### Step 1.2: File migration and splitting

**Current:**
```
CLAUDE.md          (700 lines, 35KB)
llm-wiki.md        (concept doc)
```

**Target:**
```
docs/
├── README.md           (100 lines - quick start + navigation)
├── REFERENCE.md        (500 lines - optimized CLAUDE.md)
├── CONCEPT.md          (current llm-wiki.md)
├── PHILOSOPHY.md       (150 lines - extracted principles)
└── examples/
    ├── research/       (example: paper wiki)
    ├── reading/        (example: book companion)
    └── personal/       (example: journal + goals)
```

### Step 1.3: Split CLAUDE.md

**Extract to PHILOSOPHY.md:**
- "Principles" section (lines ~380-420 in current)
- "Why this works" rationale
- Design decisions

**Extract to README.md:**
- Quick Start (30-second version)
- Installation oneliner
- First 3 commands
- Link directory to other docs

**Optimize remaining as REFERENCE.md:**
- Apply command reference consolidation
- Apply integration consolidation
- Apply workflow template consolidation

---

## Concrete File Examples

### docs/README.md (NEW - optimized entry point)

```markdown
# LLM Wiki

**Build a personal knowledge base maintained by LLMs.**

Instead of re-deriving knowledge from documents on every query (RAG), the LLM incrementally builds and maintains a persistent, interlinked wiki. The wiki compounds over time as you add sources and ask questions.

## 30-Second Start

```bash
# Install
pip install -e ".[dev]"
conda activate llm-wiki

# Initialize
/wiki-init          # Or: wiki_init(Path("."), name="My Wiki", topic="research")

# Add a source
/wiki-ingest raw/paper.pdf

# Ask questions
/wiki-query "What is the main contribution?"
```

## Documentation

| Doc | Purpose | When to read |
|-----|---------|--------------|
| [REFERENCE.md](REFERENCE.md) | Complete command reference, workflows, integrations | Daily use, building wikis |
| [CONCEPT.md](CONCEPT.md) | The idea, why it works, use cases | Understanding the pattern |
| [PHILOSOPHY.md](PHILOSOPHY.md) | Design rationale, principles, trade-offs | Deep understanding, extending system |
| [examples/](examples/) | Starter templates for different domains | First-time setup |

## The Core Idea

**Traditional RAG:** Upload docs → LLM retrieves chunks per query → rediscover knowledge each time

**LLM Wiki:** Upload docs → LLM builds wiki once → knowledge compounds → query synthesizes from maintained structure

See [CONCEPT.md](CONCEPT.md) for full explanation.

## What You Get

```
wiki/
├── sources/        LLM-written summaries of your documents
├── entities/       People, organizations, places extracted across sources
├── concepts/       Ideas and themes synthesized across sources
├── analyses/       Saved answers and comparisons
└── index.md        Master catalog (auto-maintained)
```

You read in Obsidian. The LLM maintains everything.

## Architecture

**3-Tier Data Model:**
- **Tier 1** (Source of Truth): schema.yml, manifest.jsonl, raw/, wiki/
- **Tier 2** (Derived): index.md, log.md, MIND_MAP.md (regenerate with `wiki_rebuild()`)
- **Tier 3** (Ephemeral): Session context, OMEGA memory

If something breaks, regenerate Tier 2 from Tier 1. The wiki is durable.

## Quick Reference

**Most common operations:**
```python
from llm_wiki import Wiki, wiki_ingest, wiki_query, wiki_stats

wiki = Wiki(Path("."))
wiki_ingest(wiki, Path("raw/paper.pdf"))      # Add source
wiki_query(wiki, "What is self-attention?")   # Ask question
wiki_stats(wiki)                               # Check health
```

Or use slash commands in Claude Code:
```
/wiki              # Main hub
/wiki-ingest       # Add source
/wiki-query        # Ask question
/wiki-status       # Health check
```

Full reference: [REFERENCE.md](REFERENCE.md)

## Integrations

- **Obsidian** (recommended): Visual graph view, search, navigation
- **OMEGA** (optional): Cross-session memory for decisions and lessons
- **Claude Code** (optional): Slash commands for workflow automation

## Examples

**Research wiki:** Track papers, build concept map, synthesize findings
→ See [examples/research/](examples/research/)

**Book companion:** Chapter summaries, character pages, theme analysis
→ See [examples/reading/](examples/reading/)

**Personal knowledge:** Journal entries, goals, psychology, self-improvement
→ See [examples/personal/](examples/personal/)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and testing.

## License

MIT - See [LICENSE](LICENSE)
```

**Improvements:**
- 100 lines vs 700 (86% reduction)
- Clear navigation to other docs
- 30-second start vs buried in text
- Quick reference immediately accessible
- Examples linked upfront

---

### docs/PHILOSOPHY.md (NEW - extracted design rationale)

```markdown
# LLM Wiki: Design Philosophy

## Core Principles

### 1. The Wiki is the Artifact

**Principle:** Chat is ephemeral; the wiki persists.

**Rationale:** Conversations with LLMs are disposable. Every answer must be re-derived. A wiki accumulates knowledge over time. The more you use it, the richer it gets.

**Implication:** Focus all maintenance effort on wiki quality, not chat history.

### 2. Compile, Don't Retrieve

**Principle:** Knowledge is synthesized once and maintained, not re-derived per query.

**Rationale:** RAG systems re-discover knowledge from chunks on every question. If a question requires synthesizing 5 documents, RAG does this work repeatedly. A wiki compiles the synthesis once, then keeps it current.

**Implication:** Ingest workflow does more upfront work, but queries are faster and more consistent.

### 3. Cross-Reference Aggressively

**Principle:** Links are as valuable as content. Bidirectional by default.

**Rationale:** A fact in isolation is less useful than a fact connected to related concepts, sources, and entities. The connections form a knowledge graph. The more links, the more paths to knowledge.

**Implication:** Every page should have 5-15 links to other pages. If A links to B, B should link back to A.

### 4. Flag Uncertainty

**Principle:** Mark claims as contested, preliminary, or needing verification.

**Rationale:** Not all knowledge is equally certain. Sources contradict. Claims may be speculative. Highlighting uncertainty prevents false confidence.

**Implication:** Use `contradictions/` pages to flag conflicts. Mark preliminary claims explicitly.

### 5. Human Directs, LLM Executes

**Principle:** User chooses sources and asks questions; LLM does the bookkeeping.

**Rationale:** Humans are good at curation, questions, and synthesis. LLMs are good at summarization, cross-referencing, and maintenance. Division of labor.

**Implication:** User never writes wiki pages directly. User adds sources, asks questions, and reviews LLM output.

### 6. The Document is the Execution Trace

**Principle:** Check boxes as you go, annotate outcomes, never backfill.

**Rationale:** Workflows (ingest, query, maintain) should document their own execution. Checklists show what was done. Annotations capture decisions. This creates an audit trail.

**Implication:** Use Design → Work → Verify phases. Don't skip verification.

### 7. Tiers Enforce Durability

**Principle:** Know what's source of truth, what's derived, what's ephemeral.

**Rationale:** Systems fail. Files corrupt. Sessions end unexpectedly. If you know what's durable (Tier 1), what can be regenerated (Tier 2), and what's transient (Tier 3), you can recover from any failure.

**Implication:** 
- Tier 1: Must backup, never delete without reason
- Tier 2: Can regenerate with `wiki_rebuild()`
- Tier 3: Can lose without data loss

---

## Design Decisions

### Why Markdown Instead of a Database?

**Decision:** Wiki is plain markdown files, not rows in PostgreSQL or documents in MongoDB.

**Rationale:**
1. **Grep-able:** `grep "transformer" wiki/**/*.md` works. Query languages don't.
2. **Version control:** Git tracks every change. Database dumps don't.
3. **Portable:** Move wiki to any machine. No database setup.
4. **Readable:** Humans can read markdown. Database dumps are opaque.
5. **Tooling:** Obsidian, VS Code, any text editor works. Databases need clients.

**Trade-off:** Less efficient for large-scale search (10K+ pages). Acceptable for personal knowledge bases (<1K pages typical).

### Why YAML Frontmatter Instead of Separate Metadata Files?

**Decision:** Each page has YAML frontmatter at the top, not separate `.meta.json` files.

**Rationale:**
1. **Atomicity:** Page content and metadata in one file. No orphan metadata.
2. **Obsidian native:** Obsidian Dataview plugin reads frontmatter directly.
3. **Grep-able:** `grep "^tags:" wiki/**/*.md` finds all tags.
4. **Simplicity:** One file type, not two.

**Trade-off:** Harder to bulk-edit metadata. Acceptable because LLM handles most edits.

### Why Append-Only manifest.jsonl Instead of Editing log.md?

**Decision:** Operation log is append-only JSONL (`manifest.jsonl`), then compiled to readable markdown (`log.md`).

**Rationale:**
1. **Durability:** JSONL is never edited, only appended. Can't corrupt existing entries.
2. **Parseable:** Machines can parse JSONL easily. Markdown is ambiguous.
3. **Audit trail:** Every operation logged with timestamp, SHA256 hash, author.
4. **Compile log.md:** Human-readable log derived from manifest.

**Trade-off:** Two files instead of one. Acceptable because log.md is Tier 2 (regenerable).

### Why 3 Tiers Instead of 2?

**Decision:** Separate ephemeral state (Tier 3) from derived artifacts (Tier 2).

**Rationale:**
1. **Session context:** Navigation history, working pages, current focus. Not worth persisting to disk.
2. **OMEGA memory:** Cross-session memory lives in external database, not wiki files.
3. **Clarity:** "What happens if I close Claude?" → T3 lost, T1+T2 intact.

**Trade-off:** More concepts to learn. Acceptable because mental model is clearer.

---

## Comparison to Other Patterns

### vs Traditional RAG (Retrieval-Augmented Generation)

| Aspect | RAG | LLM Wiki |
|--------|-----|----------|
| Knowledge persistence | None (re-derive per query) | Wiki maintained over time |
| Cross-references | Implicit (found per query) | Explicit (pre-compiled links) |
| Contradictions | Detected per query (maybe) | Flagged in dedicated pages |
| Maintenance | None | LLM updates wiki on each source |
| Query latency | Higher (chunk retrieval + synthesis) | Lower (read pre-compiled pages) |
| Scalability | 100K+ documents | 100-1000 documents (personal scale) |

**Use RAG when:** Enterprise scale, documents change frequently, no human curation

**Use LLM Wiki when:** Personal knowledge, curated sources, knowledge compounds over time

### vs Manual Wiki (Obsidian Vault Maintained by Human)

| Aspect | Manual Wiki | LLM Wiki |
|--------|-------------|----------|
| Writing | Human writes pages | LLM writes pages |
| Maintenance | Human updates cross-refs | LLM updates cross-refs |
| Consistency | Degrades over time | LLM maintains consistency |
| Personalization | Highly personal voice | LLM mimics user's style |
| Effort | High (hours per week) | Low (minutes per week) |

**Use Manual Wiki when:** Writing is thinking, deep personal reflection

**Use LLM Wiki when:** Focus on reading/thinking, not bookkeeping

### vs Vannevar Bush's Memex (1945)

LLM Wiki is the closest modern implementation of Bush's vision:
- Personal knowledge store (not public like the web)
- Curated sources (not algorithmic feed)
- Associative trails between documents (wikilinks)
- User-directed exploration (not search engine ranking)

The missing piece in Bush's vision: **who maintains the connections?** The LLM is the answer.

---

## Future Directions

### Multi-User Wikis

**Current:** Single user owns and curates wiki

**Possible:** Team wiki where LLM integrates contributions from multiple humans
- Slack integration: LLM maintains wiki from team conversations
- Meeting transcripts: LLM extracts decisions and updates wiki
- Document sharing: Team members upload sources, LLM synthesizes

**Challenge:** Conflict resolution when humans disagree

### LLM as Wiki Editor, Not Author

**Current:** LLM writes entire wiki pages

**Possible:** Human writes, LLM maintains cross-references and consistency
- Human writes concept page
- LLM scans wiki for related pages
- LLM suggests bidirectional links
- LLM flags contradictions with existing pages

**Benefit:** More personal voice, less LLM-generated prose

### Wiki Forking and Merging

**Current:** Linear wiki evolution

**Possible:** Git-like branching for exploratory work
- Fork wiki to explore controversial hypothesis
- If hypothesis validates, merge branch back
- If hypothesis fails, discard branch

**Use case:** "What if we assume X instead of Y?" → Fork wiki, test implications, merge or discard

---

## Why This Works

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value.

LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else.
```

**Improvements:**
- Philosophy separated from daily reference
- Design rationale explicit and justified
- Comparison to alternatives clarifies positioning
- Future directions suggest extensibility

---

## Phase 2: Create .claude/skills/llm-wiki/ Skill

### .claude/skills/llm-wiki/SKILL.md

```markdown
# LLM Wiki Skill

**When to use:** User mentions "wiki", "knowledge base", "ingest", "mind map", references `/wiki*` slash commands, or wants to track sources and synthesize knowledge over time.

**Do NOT use:** General wikis (Wikipedia), static site generation, standard RAG/document QA without persistent knowledge compilation.

---

## Quick Context Load

Before executing any wiki operation, load these mental models:

### 3-Tier Data Model
- **T1 (Source of Truth):** schema.yml, manifest.jsonl, raw/, wiki/ - Never lose this
- **T2 (Derived):** index.md, log.md, MIND_MAP.md - Regenerate with `wiki_rebuild()`
- **T3 (Ephemeral):** Session context, navigation - Lost on session end, that's OK

### Standard Execution Template
Every wiki operation follows: **Design → Work → Verify**

**Design Phase** (Orientation):
- [ ] Read inputs completely
- [ ] Identify: entities, concepts, contradictions
- [ ] Discuss key decisions with user

**Work Phase** (Execution):
- [ ] Create/update wiki pages with frontmatter
- [ ] Ensure bidirectional links
- [ ] Update index.md and MIND_MAP.md

**Verify Phase**:
- [ ] All pages have complete frontmatter
- [ ] No broken wikilinks
- [ ] Log operation in manifest.jsonl + log.md

---

## Command Quick Reference

| Operation | Slash | Python | Tier Effect |
|-----------|-------|--------|-------------|
| Initialize | `/wiki-init` | `wiki_init(root, name, topic)` | Creates T1 |
| Ingest | `/wiki-ingest <file>` | `wiki_ingest(wiki, path, title)` | Writes T1+T2 |
| Query | `/wiki-query <q>` | `wiki_query(wiki, query)` | Reads T1+T2, writes T3 |
| Status | `/wiki-status` | `wiki_stats(wiki)` | Reads T1+T2 |
| Rebuild | — | `wiki_rebuild(wiki, force=True)` | Regenerates T2 |

---

## Integration Detection

**Check on skill load:**
```python
from llm_wiki.integrations.omega import is_omega_available
from pathlib import Path

omega_enabled = is_omega_available()
current_wiki = Wiki(Path.cwd()) if (Path.cwd() / "schema.yml").exists() else None
```

**If OMEGA available:**
- Use `/wiki-remember` to store decisions
- Use `/wiki-resume` to get session briefing
- Store lessons learned for future sessions

**If wiki detected in pwd:**
- Load schema.yml to understand topic
- Scan index.md to understand current state
- Check log.md for recent operations

---

## Core Principles (Keep in Mind)

1. **The wiki is the artifact** - Chat is ephemeral, wiki persists
2. **Compile, don't retrieve** - Build knowledge once, maintain it
3. **Cross-reference aggressively** - Links are as valuable as content
4. **Human directs, LLM executes** - User curates, you maintain
5. **Document execution** - Use checklists, never backfill

---

## Page Type Templates

### Source Page (wiki/sources/*.md)
```yaml
---
title: Paper Title
page_id: sources/vaswani-2017
page_type: source
tags: [nlp, attention]
created: 2024-01-15T10:00:00Z
---

## Summary
[One paragraph overview]

## Key Claims
- [Bullet points]

## Questions Raised
- [What's unclear or needs investigation]

## Related
[[concepts/attention]], [[concepts/transformers]]
```

### Concept Page (wiki/concepts/*.md)
```yaml
---
title: Self-Attention
page_id: concepts/self-attention
page_type: concept
tags: [nlp, mechanism]
sources: [sources/vaswani-2017]
---

[Dense explanation with cross-references]
```

---

## Common Patterns

### Pattern 1: Ingest New Paper
```
1. Read PDF completely
2. Discuss with user: key contributions, new entities/concepts
3. Create source page in wiki/sources/
4. Update/create entity pages (authors, institutions)
5. Update/create concept pages (ideas, methods)
6. Update index.md
7. Update MIND_MAP.md nodes
8. Verify bidirectional links
9. Log to manifest.jsonl
```

### Pattern 2: Answer Complex Query
```
1. Read MIND_MAP.md for orientation
2. Read index.md to find relevant pages
3. Read 3-7 relevant wiki pages
4. Synthesize answer with [[wikilink]] citations
5. Offer to save answer as analysis page
6. If saved: create wiki/analyses/[topic].md
7. Update index.md and MIND_MAP.md
```

### Pattern 3: Health Check Wiki
```
1. Run wiki_stats() to get counts
2. Scan for: orphan pages, broken links, one-way links
3. Check contradictions/ directory for unresolved conflicts
4. Look for missing pages (frequently mentioned but no dedicated page)
5. Report findings to user with prioritized recommendations
```

---

## Error Recovery

**If wiki rebuild needed:**
```python
from llm_wiki import wiki_rebuild
wiki_rebuild(wiki, force=True)  # Regenerates all T2 artifacts
```

**If frontmatter validation fails:**
- Check wiki/sources/*.md, wiki/entities/*.md, etc. for missing fields
- Required: title, page_id, page_type, created, updated
- Fix and re-verify

**If MIND_MAP out of sync:**
- Included in wiki_rebuild()
- Or manually: read all pages, regenerate nodes, maintain cross-references

---

## Performance Notes

- Small wikis (<100 pages): index.md sufficient for search
- Medium wikis (100-500 pages): Consider qmd or similar search tool
- Large wikis (500+ pages): Full embedding-based search recommended

Current expected scale: 50-200 pages typical for personal knowledge base

---

## Remember

You're not just answering questions — you're a disciplined wiki maintainer. Every ingest should improve the wiki structure. Every query should strengthen connections. The wiki compounds over time.
```

**Improvements:**
- Skill loads automatically in Claude Code when relevant
- Condensed essential information from 700-line doc
- Action-oriented (templates, patterns, commands)
- Self-contained (can execute without reading full docs)

---

## Phase 3: Implementation Timeline

### Week 1: Documentation (Low Risk)

**Day 1-2:** Split CLAUDE.md
```bash
# Backup original
cp CLAUDE.md CLAUDE.md.backup

# Create structure
mkdir -p docs/examples/{research,reading,personal}

# Extract Philosophy
grep -A 50 "^## Principles" CLAUDE.md > docs/PHILOSOPHY.md
# Edit to expand and polish

# Create README
# Use template above

# Create REFERENCE
# Use optimized version (command consolidation, integration consolidation)
```

**Day 3:** Move llm-wiki.md
```bash
mv llm-wiki.md docs/CONCEPT.md
```

**Day 4:** Create skill
```bash
mkdir -p .claude/skills/llm-wiki
# Use template above for .claude/skills/llm-wiki/SKILL.md
```

**Day 5:** Update repo root
```bash
# Add README.md pointing to docs/
# Update pyproject.toml if needed
# Test all internal links
```

### Week 2: Example Content (Medium Effort)

Create starter templates in docs/examples/:
- research/: Paper tracking wiki
- reading/: Book companion wiki
- personal/: Journal + goals wiki

Each with:
- Pre-populated schema.yml
- Example source in raw/
- Example wiki pages
- README explaining use case

### Week 3: Validation (Critical)

1. Test all commands work after split
2. Verify no broken internal doc links
3. User test: Can new user complete first workflow in <5 min?
4. Integration test: OMEGA, Obsidian, slash commands
5. Performance test: Large wiki rebuild

---

## Success Metrics

**Quantitative:**
- [ ] Total doc size: 700 lines → ~500 lines (30% reduction)
- [ ] Time to first command: >60s → <10s
- [ ] Command reference tables: 5 → 1

**Qualitative:**
- [ ] New user can initialize wiki in <5 min
- [ ] 80% of daily queries answered without full doc read
- [ ] Clear entry points for: beginner, daily user, developer
- [ ] No information overlap >10% between docs

**Validation:**
- [ ] All slash commands work
- [ ] All Python API calls work
- [ ] OMEGA integration works
- [ ] Obsidian integration works
- [ ] Tests pass (325 tests)
- [ ] No broken internal links
