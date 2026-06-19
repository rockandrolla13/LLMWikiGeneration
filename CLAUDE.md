# LLM Wiki Reference

---

## ⚠️ CRITICAL RULES

**1. Do NOT create or change any code unless Andreas confirms clearly.**

Ask first. Wait for explicit approval before writing, editing, or creating files.

**2. No fabricated details.**

Never invent citations, page numbers, equation forms, theorem statements, function names, file paths, API signatures, dates, author affiliations, or any other factual detail. If a fact is not present in source material (wiki pages, files in the repo, web fetch, prior conversation), say so explicitly rather than guess. Flag uncertainty inline (e.g., "wiki summary is thin here; supplementing from paper-level knowledge — verify against the PDF before relying on this").

Compile, don't quote (unless explicitly requested). Synthesize the new information in its own words and merge it seamlessly into existing concept pages.

---

## SESSION STARTUP - DO THIS FIRST

**At the start of EVERY session, Claude MUST:**

1. Call `omega_welcome()` to load context briefing
2. Call `omega_protocol()` to get operating instructions
3. Review which wikis exist (check WIKI_REGISTRY.md or query OMEGA)

**If you "forget" things like:**
- Which wikis exist
- What concepts have been added
- Previous decisions or lessons learned

**→ Query OMEGA memory:** `omega_query("wikis")` or `omega_query("carry strategy")`

**Active Wikis:**
- `LLMWikiGeneration/wiki` - ML/Transformers research
- `CarryStrategyWiki/wiki` - Fixed income carry/roll strategies

---

## MIND_MAP Status

`wiki/MIND_MAP.md` is **Tier 1** (handcrafted, NOT regenerable by `wiki_rebuild()`).
The Python compiler produces a 50-node routing stub; the real map has 211+ thematic nodes curated over time.

- Do NOT update MIND_MAP inline during ingest — defer to an explicit rebuild session.
- If MIND_MAP's "Coverage as of" date is >7 days old, warn the user before running queries.

---

## Quick Start

```
/wiki                      # Hub - status + navigation
/wiki-convert raw/doc.pdf  # Convert PDF to markdown (REQUIRED for PDFs)
/wiki-ingest markdown_output/doc.md  # Ingest the converted markdown
/wiki-query "question?"    # Search and synthesize
/wiki-status               # Check wiki health
```

---

## Navigation

- Full command reference: `docs/REFERENCE.md`
- Design philosophy: `docs/PHILOSOPHY.md`
- Wiki registry: `WIKI_REGISTRY.md`
- PDF conversion: `/wiki-convert` skill
