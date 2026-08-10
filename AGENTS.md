# LLM Wiki — Agent Conventions

This file is for coding agents (Codex, and any other tool that reads `AGENTS.md`).
Claude Code reads `CLAUDE.md`; the two are kept consistent on purpose.

---

## Two rules that override everything else

**1. Do not create or change code unless Andreas confirms clearly.** Ask first.
Wait for explicit approval before writing, editing or creating files. Reading,
searching and reporting are always fine.

**2. No fabricated details.** Never invent citations, page numbers, equation
forms, theorem statements, function names, file paths, API signatures, dates or
author affiliations. If a fact is not in the source material — a wiki page, a
file in this repo, a fetched page, or earlier in the conversation — say so
instead of guessing. Flag thin evidence inline rather than smoothing over it.

Two invented Sharpe-ratio tables have already reached wiki pages and had to be
corrected against the source paper. That is why rule 2 is a rule and not advice.

---

## This repository is public

`/research/` is gitignored and stays that way. So are root-level PDFs and
`.obsidian/`. Some source documents are copyrighted; none of them are published.
Before adding anything to git, check it is not a source document, a private
research design, or a local path.

---

## `wiki/MIND_MAP.md` is hand-curated

It holds 414 nodes built up by hand over time. The Python compiler produces a
much smaller routing stub — it is not a substitute.

- Never pass `overwrite_curated=True`.
- Never update MIND_MAP inline during an ingest; defer to an explicit rebuild.
- `wiki_rebuild(wiki, force=True)` is safe: it regenerates `index.md` and
  `index.full.md` and refuses to touch MIND_MAP.

This already went wrong once. An unguarded rebuild replaced 211 curated nodes
with 28 generated ones, which is why `tests/test_curated_guard.py` exists — a
warning comment in a file cannot stop a program.

---

## Layout

| Path | What it is |
|---|---|
| `src/llm_wiki/` | the package (src layout) |
| `wiki/` | the vault — holds `schema.yml`, `manifest.jsonl`, and `wiki/` |
| `wiki/wiki/` | the pages themselves: sources, concepts, entities, analyses |
| `markdown_output/` | converted PDFs, gitignored, regenerable |
| `research/` | local research designs, gitignored, never published |
| `scripts/` | maintenance scripts, not part of the package |
| `docs/` | `REFERENCE.md` (commands), `PHILOSOPHY.md` (why) |

Scripts that are run from the repo root use `sys.path.insert(0, "src")`.

**Run everything from the repository root.** Provenance checking resolves source
paths relative to the working directory, so from anywhere else most sources
silently stop resolving and the checks still report a pass.

---

## Tests

```
python -m pytest -q
```

431 tests. Run them after every change.

---

## Things that will waste your time if you do not know them

**The drive is NTFS.** Git sees phantom `100644 → 100755` mode changes on
thousands of files. `core.fileMode=false` is set locally, which handles it — but
still stage by explicit path. `git add -A` and bare directory adds have both
swept up hundreds of mode-only changes here.

**Search is BM25, not grep.** `wiki/schema.yml` selects it and `rank-bm25` is a
required dependency, not an optional one. If the import is missing the backend
reports itself unavailable and silently falls back to grep, which scored
recall@1 of 0% on `eval/eval_cases.json` against BM25's 80%. A silent 0% is
worse than an import error.

**`chunk_wiki` wants the vault root**, i.e. `wiki/`, not `wiki.wiki_dir` — it
appends `/wiki` itself. Passing the wrong one yields zero chunks and a
`ZeroDivisionError` inside BM25. Pinned by `tests/test_search_backend.py`.

**Manifest operations are keyed `op_type`,** not `operation_type`. The wrong key
returns zero rows without erroring.

**Some `wiki/raw/` entries are symlinks to local paths.** They resolve on this
machine only. Broken ones drop source pages out of provenance checking while all
the integrity checks still pass.

---

## Working on the wiki content

Compile, don't quote. Synthesise new information in its own words and merge it
into the existing concept pages, rather than pasting extracts.

Pages are schema v2: `page_id`, `page_type`, `source_path`,
`verification: {status, unverified_claims}`, `mind_map_priority`.

A page with no `source_path` cannot be provenance-checked. Adding
`source_path: markdown_output/<file>.md` is what brings it back into checking.

PDF ingestion is two steps: convert to markdown into `markdown_output/`, then
run the semantic extraction that creates the source, concept and entity pages.
**Always ask where the input PDFs are.** Never assume a location.

---

## Related

- `CLAUDE.md` — the same rules, for Claude Code
- `docs/REFERENCE.md` — full command reference
- `WIKI_REGISTRY.md` — which wikis exist
