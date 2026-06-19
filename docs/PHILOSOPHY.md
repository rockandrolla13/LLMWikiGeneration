# LLM Wiki — Design Philosophy

> Why this system is built the way it is. Read once; consult when making structural decisions.

---

## The Core Idea

Most people's experience with LLMs and documents looks like RAG: upload files, the LLM retrieves relevant chunks at query time, generates an answer. This works, but the LLM is rediscovering knowledge from scratch on every question. There is no accumulation. Ask a subtle question requiring synthesis of five documents, and the LLM must find and piece together the relevant fragments every time.

The idea here is different. Instead of retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files sitting between you and the raw sources. When you add a new source, the LLM reads it, extracts the key information, and integrates it into the existing wiki: updating entity pages, revising topic summaries, noting where new data contradicts old claims. The knowledge is compiled once and kept current, not re-derived on every query.

The wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you have read. The wiki keeps getting richer with every source you add and every question you ask.

You never write the wiki yourself — the LLM writes and maintains all of it. You source, explore, and ask the right questions. The LLM does the summarising, cross-referencing, filing, and bookkeeping.

---

## Design Principles

1. **The wiki is the artifact** — Chat is ephemeral; wiki persists. Focus all maintenance effort on wiki quality, not chat history.

2. **Compile, don't retrieve** — Knowledge is synthesised once and maintained, not re-derived per query. The ingest workflow does more upfront work, but queries are faster and more consistent.

3. **Cross-reference aggressively** — Links are as valuable as content. Every page should have 5–15 links to other pages. If A links to B, B links back to A.

4. **Flag uncertainty** — Mark claims as contested or preliminary. Use `contradictions/` pages to flag conflicts between sources.

5. **Human directs, LLM executes** — User chooses sources and asks questions; LLM does the bookkeeping. Users never write wiki pages directly.

6. **Document execution** — Use checklists; never backfill. Workflows (ingest, query, maintain) document their own execution as they run.

7. **Tiers enforce durability** — Know what is source of truth (T1), what is derived (T2), and what is ephemeral (T3). If something breaks, you can always recover T2 from T1.

8. **Symlink, don't copy** — Use symbolic links for source documents to avoid duplication and maintain a single source of truth.

---

## Why This Works

The tedious part of maintaining a knowledge base is not the reading or the thinking — it is the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value.

LLMs do not get bored, do not forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else.

---

## Architectural Decisions

### Why Markdown Instead of a Database?

**Decision:** Wiki is plain markdown files, not rows in a database.

Reasons: grep-able, version-controlled, portable across machines, human-readable, works with any text editor or Obsidian. The trade-off is less efficiency at large scale (10K+ pages), which is acceptable for personal knowledge bases (typically under 1K pages).

### Why YAML Frontmatter?

**Decision:** Each page has YAML frontmatter at the top, not separate metadata files.

Reasons: atomicity (content and metadata in one file), Obsidian Dataview reads it natively, grep-able (`grep "^tags:" wiki/**/*.md`). The trade-off is harder bulk metadata edits, acceptable because the LLM handles most edits.

### Why Append-Only manifest.jsonl?

**Decision:** Operation log is append-only JSONL compiled to readable `log.md`.

Reasons: never corrupts existing entries, machine-parseable, creates a full audit trail with timestamps and content hashes. `log.md` is T2 (regenerable from manifest).

### Why 3 Tiers Instead of 2?

**Decision:** Separate ephemeral state (T3) from derived artifacts (T2).

Reasons: session context and OMEGA memory are not worth persisting to wiki files. The three-tier mental model makes recovery straightforward: T3 loss is trivial, T2 loss is recoverable, only T1 requires backup.

---

## Comparison to Other Patterns

### vs Traditional RAG

| Aspect | RAG | LLM Wiki |
|--------|-----|----------|
| Knowledge persistence | None (re-derive per query) | Wiki maintained over time |
| Cross-references | Implicit (found per query) | Explicit (pre-compiled links) |
| Contradictions | Detected per query (maybe) | Flagged in dedicated pages |
| Query latency | Higher (chunk retrieval + synthesis) | Lower (read pre-compiled pages) |
| Scalability | 100K+ documents | 100–1000 documents (personal scale) |

Use RAG for enterprise scale or frequently changing documents. Use LLM Wiki for personal knowledge where sources are curated and knowledge compounds over time.

### vs Manual Wiki (Obsidian Vault Maintained by Human)

| Aspect | Manual Wiki | LLM Wiki |
|--------|-------------|----------|
| Writing | Human writes pages | LLM writes pages |
| Maintenance | Human updates cross-refs | LLM updates cross-refs |
| Consistency | Degrades over time | LLM maintains consistency |
| Effort | High (hours per week) | Low (minutes per week) |

Use a manual wiki when writing is thinking and deep personal reflection matters. Use LLM Wiki when you want to focus on reading and thinking, not bookkeeping.

### vs Vannevar Bush's Memex (1945)

LLM Wiki is the closest modern implementation of Bush's vision: a personal knowledge store, curated sources, associative trails between documents, user-directed exploration. The missing piece in Bush's vision was who maintains the connections. The LLM is the answer.

---

## Use Cases

- **Research:** Going deep on a topic over weeks or months — reading papers, articles, reports, incrementally building a comprehensive wiki with an evolving thesis.
- **Reading a book:** Filing each chapter as you go, building pages for characters, themes, plot threads, and how they connect.
- **Personal knowledge:** Tracking goals, health, psychology, self-improvement — filing journal entries, articles, and building a structured picture over time.
- **Competitive analysis, due diligence, course notes, hobby deep-dives** — anything where knowledge accumulates over time and should be organised rather than scattered.
