# LLM Wiki → Second Brain: Implementation Plan

**Target executor:** Claude Code, driven through the `/blueprint` skill library (BCS-1.0 contracts; skills: `architect`, `scaffold`, `code-review`).
**Repo:** `LLMWikiGeneration` (the `llm_wiki` package + Obsidian vault).
**Outcome:** A content-addressable, provenance-grade, self-repairing knowledge base that compiles sources once and keeps them current — a durable second brain rather than a pile of LLM summaries.

---

## Part 0 — Read this first (operating contract for Claude Code)

You are extending an existing system, not greenfielding. Before writing code in any phase:

1. **Read the live state.** Open the current `CLAUDE.md`, the `llm_wiki` package (`core`, `registry`, the existing `wiki_*` functions), `schema.yml`, and a representative `wiki/` page with its frontmatter. The contracts below describe *intended* behaviour; reconcile them against what actually exists and flag drift instead of guessing.
2. **One phase = one `/blueprint` cycle = one PR.** For each phase: `/blueprint architect` to turn the phase spec into a BCS-1.0 contract (preconditions / postconditions / invariants / acceptance tests in the library's native format), then `/blueprint scaffold` to implement against that contract, then `/blueprint code-review` before merge. Do not merge a phase whose acceptance tests are red.
3. **No fabrication.** Every code path that emits a *claim* into the wiki must carry a citation to a source span, or be marked `status: unverified`. This rule from the existing `CLAUDE.md` is now enforced programmatically (Phases 2 and 5), not just by prose.
4. **Markdown + git is the only source of truth.** Every index, BM25 store, graph, or cache you build is a **disposable Tier-2 artifact**, fully reconstructable by `wiki_rebuild()`. Nothing in `.index/` is ever authoritative. If you cannot rebuild it from `raw/` + `wiki/` markdown, you have designed it wrong.
5. **Earn each abstraction.** This plan deliberately adds machinery (hashing, multi-agent gates, BM25, repair loops). Each piece must pay rent in *provenance, reproducibility, or retrieval quality*. If a check or compiler only verifies well-formedness without improving trust or recall, it is overhead — say so in review.

---

## Part 1 — Architecture and the load-bearing invariants

### 1.1 The tier model (unchanged, now fully exploited)

- **T1 — Source of truth (backed up, version-controlled):** `schema.yml`, `manifest.jsonl`, `raw/`, `wiki/*.md` (authored regions only).
- **T2 — Derived artifacts (regenerable, never backed up):** `wiki/index.md`, `wiki/log.md`, `MIND_MAP.md`, **and now** `.index/bm25/*`, the typed-edge graph cache, and `lint_report.md`.
- **T3 — Ephemeral:** session context, OMEGA working set.

The central design move of this whole plan: **the retrieval layer, the knowledge graph, and the lint report are all just T2.** You already have the tier abstraction; we are populating the slots it left empty.

### 1.2 The keystone: content identity

Three of the hardest problems (duplicate ingest, order-dependent merges, unsafe concurrent writes) collapse into **one** mechanism: stable identity at two granularities.

- **Document identity** — a deterministic UUID derived from the *semantic* content of a source, immune to filename and reformatting (Phase 1).
- **Claim identity** — every substantive claim is keyed by `(source_uuid, locator)`, so dedup, contradiction detection, and merge all key on identity rather than on textual proximity (Phase 2).

When both hold, **ingest becomes commutative**: `ingest(A) ∘ ingest(B)` and `ingest(B) ∘ ingest(A)` converge to byte-identical `wiki/` state (modulo the chronological `log.md`). That algebraic property is the foundation for safe multi-agent operation across your `orch` drivers.

### 1.3 The two write-time guarantees

- **Never silently delete prior context.** Concept-page updates run a *structural* markdown merge before any LLM rewrite, so the model can only reorganize within sections, never drop a section it didn't value (Phase 3).
- **Never silently commit an unverified claim.** Generation is split Writer → Evaluator → Editor, and any claim the Evaluator can't tie to a cited span is flagged or routed to a review queue, not auto-committed (Phase 5).

---

## Part 2 — Target repository layout

```
LLMWikiGeneration/
├── CLAUDE.md                      # updated: new workflows + command surface
├── llm_wiki/
│   ├── core.py                    # existing: VerificationCheck, Compiler base
│   ├── registry.py                # existing: default_checks, default_compilers
│   ├── identity.py                # NEW (P1): semantic hashing → uuid5 page_id
│   ├── ingest.py                  # EXTEND (P1/P2): markitdown/pix2text + claim citations
│   ├── merge.py                   # NEW (P3): markdown_merge(dedupe_headings=True)
│   ├── agents/                    # NEW (P5): writer / evaluator / editor sub-agent specs
│   │   ├── writer.md
│   │   ├── evaluator.md
│   │   └── editor.md
│   ├── graph.py                   # NEW (P4): typed-edge model + traversal queries
│   ├── retrieval/                 # NEW (P6): vectorless BM25
│   │   ├── bm25_index.py
│   │   └── chunker.py             # heading-section chunking w/ provenance
│   ├── lint.py                    # EXTEND (P7): markdown AST checks → lint_report.md
│   ├── repair.py                  # NEW (P7): repair loop (sub-agent or LangGraph)
│   ├── staleness.py               # NEW (P7): supersession-based staleness
│   └── compilers/                 # T2 compilers (index, mindmap, +bm25, +graph)
├── eval/
│   ├── questions.jsonl            # NEW (P8): held-out QA set
│   └── harness.py                 # NEW (P8): wiki-vs-raw scoring
├── .index/                        # T2, gitignored or rebuildable
│   ├── bm25/
│   └── graph_cache.json
└── wiki/
    ├── sources/  entities/  concepts/  analyses/  contradictions/
    ├── index.md  log.md
    └── MIND_MAP.md
```

---

## Part 3 — Frontmatter Schema v2 (single consolidated spec)

Every wiki page conforms to this. Backfilled onto existing pages in Phase 9.

```yaml
---
title: Doubly Robust Conformal Inference
page_id: concepts/dr-conformal            # human slug (filename-aligned)
uuid: 7b3e9c1a-...                          # NEW (P1): canonical content-addressable id
page_type: concept                         # source|entity|concept|analysis|contradiction
revision_id: 4
content_hash: sha256:...                    # CHANGED (P4): over AUTHORED region only
created: 2026-06-19T10:00:00Z
updated: 2026-06-19T10:00:00Z
updated_by: op_xyz123
verification:                              # NEW (P5): set by Evaluator/Editor
  status: verified                         # verified | partial | unverified | in_review
  unverified_claims: 0
tags: [conformal, causal-inference]
sources:                                   # source UUIDs this page draws on
  - 7b3e9c1a-...
relations:                                 # NEW (P4): TYPED edges (see Part 4)
  - {target: concepts/dml, rel: extends}
  - {target: concepts/aci-2021, rel: supersedes}
  - {target: concepts/naive-split, rel: contradicts}
mind_map_priority: high
---
<!-- AUTHORED REGION START -->
... LLM-authored prose with inline [[cite: <source_uuid>#sec3.2]] markers ...
<!-- AUTHORED REGION END -->
<!-- MACHINE REGION (backlinks, auto-related) — excluded from content_hash -->
```

**Hash-thrash fix (P4):** `content_hash` is computed over the canonicalized **authored region only**. Machine-maintained backlinks and auto-`related` blocks regenerate on rebuild without churning the hash, so a bidirectional-link update on page B no longer dirties page A.

---

## Part 4 — Controlled relationship vocabulary (typed edges)

Untyped `[[wikilink]]` + a flat `related:` list cannot express *how* two pages relate. Replace with a closed vocabulary. The LLM maintains the `relations:` block on every ingest.

| `rel` value        | Meaning                                              | Inverse (auto-maintained) |
|--------------------|------------------------------------------------------|---------------------------|
| `extends`          | A builds on / generalizes B                          | `extended-by`             |
| `special-case-of`  | A is a restriction of B                              | `generalizes`             |
| `supersedes`       | A replaces B as the current best account             | `superseded-by`           |
| `contradicts`      | A and B assert incompatible claims (symmetric)       | `contradicts`             |
| `refutes`          | A presents evidence against B                        | `refuted-by`              |
| `depends-on`       | A's validity requires B (assumption/lemma)           | `required-by`             |
| `was-response-to`  | A was written in reply to B                          | `prompted`                |

**Research-domain lint inversion (used in P7):** in `concept`/`analysis` space, a *missing* expected `contradicts`/`refutes` edge is the smell, not the presence of one. Two papers disagreeing on whether a DR estimator attains √n under polynomial β-mixing is *content*, not corruption. Queries like "what challenges CL-J1's minimax claim?" become a graph traversal over `refutes`/`contradicts` edges (Phase 4), not a semantic guess.

**Vocabulary governance:** the permitted set lives in `schema.yml`; `architect` should add a contract that rejects any `rel` outside it at lint time, so the vocabulary can't drift.

---

## Part 5 — The phased plan

Each phase is an independent `/blueprint` cycle and PR. Dependency order is given; Phases 4 and 6 can run in parallel with each other.

---

### Phase 0 — Foundations & contracts (architect-only)

**Why:** Freeze the data model before code so later phases don't relitigate identity, schema, or tier boundaries.

**Build:**
- `schema.yml` v2: relationship vocabulary, page-type → required-frontmatter map, tier definitions, hash-scope rule (authored-region-only).
- A BCS-1.0 *master contract* that all subsequent phase contracts inherit (defines the global invariants in Part 1.3 and the "markdown+git is sole truth" rule).

**Contract:**
- *Post:* `schema.yml` validates; master contract committed; no `.py` changes.
- *Invariant:* no behavioural change to the running wiki.

**Acceptance:** `wiki_rebuild()` still produces identical T2 output as before this phase (proves schema additions are non-breaking).

---

### Phase 1 — Content-addressable ingest & universal converters

**Why (intuition):** Today identity is a hand-named path (`sources/vaswani-2017`). Rename the file or re-upload a reformatted copy and you either break links or duplicate work. Make identity a function of *content*, so the same paper is the same node no matter how it arrives.

**Build:**
- `identity.py`:
  - `normalize_text(raw) -> str`: strip markdown/HTML syntax, NFKC-normalize unicode, collapse whitespace, drop page headers/footers/line numbers. Goal: two encodings of the same paper normalize identically.
  - `content_uuid(normalized) -> uuid.UUID`: `uuid.uuid5(NAMESPACE_WIKI, normalized)`. Deterministic, namespaced, collision-safe. This becomes the page `uuid` and the citation key root.
  - `slug_registry`: persisted `slug ↔ uuid` map so a human rename never breaks references (links resolve via `uuid`, display via slug).
- Extend `ingest.py` converter chain:
  - **`markitdown`** (Microsoft) for `.docx` / `.pptx` / `.xlsx` → markdown (directly serves your mid-year reviews, decks, and models).
  - **`pymupdf4llm`** for PDFs (existing).
  - **`pix2text`** — *install it* (currently absent). For a wiki whose whole point is conformal/causal-inference papers, LaTeX-fidelity on equations is load-bearing; lossy math summaries would violate your own no-fabrication rule.
- Ingest precheck: compute `content_uuid` *before* processing. If a page with that uuid exists, switch from "create" to "update" (hands off to Phase 3 merge) instead of creating a duplicate.

**Contract:**
- *Pre:* a file in `raw/` or a converted markdown.
- *Post:* a `uuid`-stamped page; re-ingesting the same content (even renamed/reformatted) updates in place, never duplicates.
- *Invariant:* `content_uuid(normalize(x))` is stable across formatting-only edits.

**Acceptance:**
- Ingest a paper as PDF and as a reformatted `.md` of the same text → identical `uuid`, single page.
- Ingest a `.docx`, `.pptx`, `.xlsx` → each produces a clean source page.
- Renaming a source file leaves all inbound links resolving.

**Depends on:** Phase 0.

---

### Phase 2 — Claim-level provenance & commutative ingest

**Why (intuition):** Page-level `sources:` says *a* page used *a* source, but not which sentence came from where. Pin every claim to a source span. That single change makes dedup, contradiction-detection, and concurrent-write-safety all key on *identity* instead of *word overlap*, and makes ingest order-independent.

**Build:**
- Inline citation grammar: `[[cite: <source_uuid>#<locator>]]` (locator = section/page/para anchor).
- `claim_key(text, source_uuid, locator)`: a stable hash used for dedup.
- Ingest write path: **grep the target page + index for the `claim_key` before writing.** Present → update; absent → append. (This is dedup-on-identity, watsonrm's "shift it left" — reject the duplicate at write time so the nightly lint shrinks to genuine semantic reversals.)
- Multi-writer discipline: writes are append-structured and partitioned by file/section; no advisory locks. Commutative writes make locks unnecessary across your `orch` drivers.

**Contract:**
- *Pre:* a draft with claims.
- *Post:* every committed claim carries a resolvable citation; duplicate claims are idempotent.
- *Invariant (commutativity):* for any source set S, the resulting `wiki/` (excluding `log.md`) is a function of S, independent of ingest order.

**Acceptance:**
- `ingest(A); ingest(B)` and `ingest(B); ingest(A)` produce byte-identical `wiki/` excluding `log.md`. (This is the headline test — automate it in CI.)
- Two agents ingesting overlapping sources concurrently produce zero duplicate claims.
- A claim citing a nonexistent `source_uuid` fails lint (wired in P7).

**Depends on:** Phase 1.

---

### Phase 3 — Structural merge before semantic dedup (the consolidation script)

**Why (intuition):** When you fold a second paper on, say, DML-IV into an existing concept page, a single LLM pass tends to either bloat with repetition or quietly delete a section it didn't appreciate. Do the merge *structurally* first — at the heading-tree level — then let the LLM dedup only *within* sections. The model can reorganize, but it cannot drop a section it never saw as a unit. This is the guarantee that protects older context and slashes token overhead.

**Build:**
- `merge.py::markdown_merge(old_md, new_md, dedupe_headings=True) -> merged_md`:
  - Parse both into heading-path ASTs (use `markdown-it-py`/`mistune` token stream — or `markdown-hero` if you standardize on it in P7).
  - Merge by heading path: same path → union content blocks; new path → insert in document order; **existing path is never deleted**.
  - `dedupe_headings=True`: collapse duplicate heading paths and union their blocks (this is the structural pre-pass that prevents repetitive bloat before the LLM ever runs).
- Update workflow: on any concept-page update, run `markdown_merge` first, then hand the merged outline to the Writer (P5) for *intra-section* semantic dedup only.

**Contract:**
- *Pre:* an existing page + new draft content.
- *Post:* merged page whose heading-path set ⊇ the old page's heading-path set.
- *Invariant (monotonic structure):* no heading/subtree is removed except via an explicit `supersedes` edge recorded in `relations`.

**Acceptance:**
- Merge two DML-IV write-ups → no duplicated headings, every original section present.
- A diff after merge shows additions/reorgs but zero unexplained section deletions.
- Token count of the LLM dedup prompt drops measurably vs. naive full-page rewrite (log the delta).

**Depends on:** Phase 1 (stable identity). Independent of Phase 2.

---

### Phase 4 — Typed knowledge graph

**Why (intuition):** Your knowledge lives in the *edge labels*, not just adjacency. An unlabeled link graph throws the relational semantics away. Promote `related:` to typed `relations:` so the graph becomes queryable as a property graph.

**Build:**
- `graph.py`:
  - Parse `relations:` blocks across `wiki/` into an in-memory typed multigraph; cache to `.index/graph_cache.json` (T2).
  - Auto-maintain inverse edges (Part 4 table) in the machine region (so a `supersedes` on A writes `superseded-by` on B without dirtying A's `content_hash`).
  - Traversal queries: `challenges(page)` → follow `contradicts|refutes`; `lineage(page)` → follow `supersedes|extends`; `assumptions(page)` → follow `depends-on`.
- **Hash-scope change:** finalize `content_hash` computed over authored region only (the fix that makes auto-backlink maintenance hash-stable).
- `schema.yml` vocabulary enforcement check registered into `registry.py`.

**Contract:**
- *Pre:* pages with `relations` blocks.
- *Post:* a rebuildable typed graph; inverse edges consistent; out-of-vocabulary `rel` rejected.
- *Invariant:* graph is a pure function of `relations` blocks (rebuildable, zero hidden state).

**Acceptance:**
- `challenges("concepts/cl-j1")` returns exactly the pages with `refutes`/`contradicts` edges to it.
- Adding a `supersedes` edge auto-creates the `superseded-by` inverse and does **not** change either page's `content_hash`.
- An invalid `rel` fails lint.

**Depends on:** Phase 0. Parallelizable with Phase 6.

---

### Phase 5 — Writer → Evaluator → Editor multi-agent generation + write gates

**Why (intuition):** A single context doing "draft + self-check + finalize" skips its own constraints. Split the roles into isolated sub-agents so the critic never sees the author's rationalizations — only the draft and the raw source. This is your generation-time hallucination gate, and it feeds a commit-time gate so an unverified claim can't slip in silently.

**Build:**
- `agents/writer.md`, `agents/evaluator.md`, `agents/editor.md` as sub-agent prompt specs (spawned via Claude Code sub-agents / your `orch` drivers):
  - **Writer:** given source spans + the post-merge page, produce a draft with inline `[[cite:...]]` markers.
  - **Evaluator (isolated context):** receives the *raw source* + the draft, **not** the writer's reasoning. For each claim emits `{claim, verdict ∈ supported|unsupported|uncited, evidence_span}`. Prompt: "Review this drafted page against the raw source. Flag every claim not entailed by a cited span."
  - **Editor:** consumes draft + verdicts; drops or `status: unverified`-flags unsupported claims, repairs citations, finalizes.
- **Confidence-tiered commit gate:**
  - All claims supported → auto-commit (`verification.status: verified`).
  - Some unsupported/uncited but additive → commit with `status: partial` and inline flags.
  - Any claim that *reverses prior committed content* and is unsupported → **route to `in_review` queue**, do not auto-commit. (Borel–Cantelli intuition: with per-note corruption probability p>0, P(≥1 corrupted page) → 1 over time; the queue is the cheap insurance against a 2:30am batch quietly rewriting something correct.)
- Add `in_review` as an OMEGA event/queue alongside `decision|lesson|error`.

**Contract:**
- *Pre:* merged draft + cited sources.
- *Post:* committed pages are either fully `verified`, or explicitly `partial`/`in_review` — never silently unverified.
- *Invariant:* no committed claim lacks either a resolvable citation or an explicit `unverified` flag.

**Acceptance:**
- Inject a deliberately unsupported claim → Evaluator flags it → it is not silently committed.
- A draft reversing a prior page's conclusion without support lands in `in_review`, not in `wiki/`.
- The three roles run in separate contexts (verify the Evaluator prompt contains the source but not the Writer transcript).

**Depends on:** Phases 2, 3.

---

### Phase 6 — Vectorless retrieval (BM25) and `/wiki-chat`

**Why (intuition):** `index.md` is an O(1) lookup keyed on page *title* — it only finds X if you already know X's name. `grep` over `MIND_MAP.md` can't do semantic recall and `MIND_MAP` itself is an O(n) file the agent must read whole. BM25 gives you Retrieval-Augmented answers across 50+ papers with no vector DB, no embeddings, no cloud cost — and it slots in as just another T2 artifact.

**Build:**
- `retrieval/chunker.py`: chunk `wiki/` by heading section; each chunk carries `(page_uuid, heading_path, source citations)` so retrieved context stays attributable.
- `retrieval/bm25_index.py`: build a local BM25 index (`bm25s` for speed, or `rank_bm25`) over chunks → `.index/bm25/` (T2, rebuildable via `wiki_rebuild`).
- `/wiki-chat <query>`: BM25 top-k chunks → synthesize answer with citations. Use for complex cross-corpus queries; `index.md`/`MIND_MAP` remain for cheap title-routing.
- Register a `BM25Compiler` so `wiki_rebuild()` regenerates the index; index epoch bumps on every ingest/lifecycle change (so stale chunks are never served).
- *Optional upgrade slot:* a dense-vector + reranker compiler can later replace the BM25 compiler behind the same interface. **Default stays vectorless** per the stated preference.

**Contract:**
- *Pre:* a populated `wiki/`.
- *Post:* `/wiki-chat` returns cited answers from BM25-retrieved chunks; index fully rebuildable.
- *Invariant:* deleting `.index/` and running `wiki_rebuild()` restores identical retrieval behaviour (proves it's pure T2).

**Acceptance:**
- A query answerable only by synthesizing 3 separate pages returns the right chunks with citations.
- `rm -rf .index/bm25 && wiki_rebuild()` reproduces the same top-k for a fixed query set.

**Depends on:** Phase 1 (uuids in chunk provenance). Parallelizable with Phase 4.

---

### Phase 7 — Automated lint, repair (`/wiki-repair`), and supersession staleness

**Why (intuition):** Structural rot (skipped heading levels, unclosed fences, broken anchors, dangling citations, orphans, one-way links) and *epistemic* rot (a page whose sources have been superseded) are both maintenance no human will do reliably. Detect statically, repair the structural class automatically, and escalate the semantic class to review.

**Build:**
- `lint.py` (extends existing checks) using a semantic markdown parser (`markdown-hero`, or `markdown-it-py` token stream):
  - **Structural:** skipped heading levels (h1→h3), unclosed code fences, broken anchors/wikilinks.
  - **Referential:** `[[cite:...]]` to a nonexistent `source_uuid`; `relations` target that doesn't resolve; out-of-vocabulary `rel`.
  - **Graph:** orphan pages (no inbound typed edge), one-way links (now auto-fixable via inverse maintenance from P4).
  - Output a greppable `lint_report.md` (T2), each row typed `STRUCTURAL|REFERENTIAL|GRAPH|STALE` with a severity.
- `staleness.py`: a page is **stale** if (a) a source it cites has an inbound `superseded-by` edge from a newer source, or (b) a source with a `contradicts`/`refutes` edge to one of its claims has `created` > the page's `updated`. Computed from the P4 graph + timestamps — not file mtime.
- `repair.py` + **`/wiki-repair`**: loop an agent over `lint_report.md`. Deterministic structural fixes (heading levels, fences, anchors) auto-apply; semantic items (true contradictions, missing pages, stale-due-to-supersession) escalate to the `in_review` queue. Orchestrate the loop as a Claude Code sub-agent by default, or as a **LangGraph** graph if you want it Python-side and resumable.
- **Wire linting into the Verify Phase** of the standard execution template: every ingest/update ends with a lint pass; commit is blocked on unresolved `STRUCTURAL`/`REFERENTIAL` errors.

**Contract:**
- *Pre:* a `wiki/` in any state.
- *Post:* `lint_report.md` enumerates every issue; `/wiki-repair` resolves all auto-fixable structural issues and escalates the rest; Verify Phase blocks on structural errors.
- *Invariant:* `/wiki-repair` never edits an authored region's *meaning* — only structure — and never auto-resolves a flagged contradiction.

**Acceptance:**
- Seed a page with a skipped heading + unclosed fence + a dangling citation → all three appear in `lint_report.md`; `/wiki-repair` fixes the first two and escalates the third.
- Supersede a cited source → the dependent page is reported `STALE` without any mtime change.
- An attempt to commit a page with a broken anchor is blocked at Verify.

**Depends on:** Phases 2, 4.

---

### Phase 8 — Evaluation, MIND_MAP demotion, and cutover

**Why (intuition):** You currently measure the wiki by *counts* (`wiki_stats`), not *quality*. The only way to know the compile-step earns its token cost is to score wiki-grounded answers against a raw-RAG baseline on held-out questions.

**Build:**
- `eval/questions.jsonl`: held-out questions with gold answers or grading rubrics, spanning single-page and cross-page synthesis.
- `eval/harness.py`: run each question through (i) the wiki path (BM25 + pages) and (ii) a raw-RAG baseline (chunk `raw/`, retrieve, answer); score with an LLM judge or rubric; report the wiki-vs-raw delta.
- **Demote `MIND_MAP.md` to human orientation.** With BM25 live, stop relying on it for *agent* routing (it's an O(n) read on every query). Keep it as a navigable human overview; agents route via `index.md` (cheap) + `/wiki-chat` (semantic).
- Final `CLAUDE.md` rewrite: document the new command surface, the v2 frontmatter, the typed-edge vocabulary, the W→E→E workflow, and the Verify-Phase lint requirement.

**Contract:**
- *Post:* a reproducible eval reporting wiki-vs-raw on the held-out set; `CLAUDE.md` reflects the shipped system.
- *Invariant:* eval is deterministic given a fixed model + question set + wiki epoch.

**Acceptance:**
- `eval/harness.py` runs end-to-end and prints a per-question and aggregate wiki-vs-raw score.
- A fresh agent following the updated `CLAUDE.md` can ingest, query via `/wiki-chat`, and repair without referencing this plan.

**Depends on:** Phases 5, 6, 7.

---

### Phase 9 — Migration / backfill

**Why:** Existing pages predate uuids, typed edges, claim citations, and the authored-region marker.

**Build:** a one-shot `migrate.py` that, per existing page: computes and stamps `uuid`; wraps content in authored-region markers; recomputes `content_hash` over the authored region; converts `related:` to best-effort `relations` (default `rel: extends`, queued for human review of edge types); flags pages whose claims lack citations as `verification.status: partial` for incremental backfill.

**Contract:**
- *Post:* every page is Schema-v2 valid; nothing is silently relabeled `verified`.
- *Invariant:* migration is idempotent (re-running changes nothing).

**Acceptance:** post-migration, all P0–P7 checks pass on the full existing vault; a re-run is a no-op.

**Depends on:** all prior phases (run last).

---

## Part 6 — Cross-cutting guardrails

- **Disposability check, every phase:** if a new artifact can't be reproduced by `wiki_rebuild()` from `raw/` + `wiki/`, it must not be authoritative. Add it as a T2 compiler, not as state.
- **No LLM conflict resolution.** Genuine contradictions and decision-reversals go to `in_review`; never let a model silently reconcile them. Determinism beats cleverness for the merge/repair layer.
- **Commutativity is a CI gate, not a hope.** The Phase-2 order-independence test runs on every PR from Phase 2 onward; regressions there mean multi-agent safety has broken.
- **Earned automation.** Keep the manual `ingest → query → lint` loop usable at every step. Machinery that doesn't improve provenance, reproducibility, or recall is overhead — `code-review` should call it out.

---

## Part 7 — Global Definition of Done

The extension is complete when:

1. Re-uploading the same paper (any format, any filename) is a no-op, not a duplicate. *(P1)*
2. Ingest order cannot change the resulting wiki state. *(P2)*
3. A concept-page update provably cannot delete a prior section without a `supersedes` edge. *(P3)*
4. "What challenges X?" / "what does X depend on?" are graph traversals, not guesses. *(P4)*
5. No claim reaches `wiki/` without a citation or an explicit `unverified` flag; reversals are quarantined. *(P5)*
6. A cross-corpus question over 50+ papers is answered from BM25-retrieved, cited chunks with zero vector infra. *(P6)*
7. Structural rot is auto-repaired and epistemic staleness is detected by supersession. *(P7)*
8. A held-out eval shows the wiki path beats raw RAG, and a cold agent can operate the system from `CLAUDE.md` alone. *(P8)*
9. The entire existing vault is migrated, idempotently. *(P9)*

---

## Appendix A — Dependency / execution order

```
P0 ─┬─ P1 ── P2 ──┬── P3 ──┐
    │             │        ├── P5 ──┐
    ├─ P4 ────────┘        │        ├── P8 ── P9
    └─ (P4) ──────── P6 ───┴── P7 ──┘
```
Critical path: P0 → P1 → P2 → P3 → P5 → P8 → P9. P4 and P6 run in parallel off P0/P1 and rejoin at P7/P8.

---

## Appendix B — New command & API surface

| Command / function            | Phase | Purpose                                                        |
|-------------------------------|-------|----------------------------------------------------------------|
| `content_uuid()` / `identity` | P1    | Deterministic, format-immune document id                       |
| `markitdown` / `pix2text` ingest | P1 | `.docx/.pptx/.xlsx` + math-OCR ingestion                        |
| `[[cite: uuid#loc]]` grammar  | P2    | Claim-level provenance → commutative ingest                    |
| `markdown_merge(dedupe_headings=True)` | P3 | Structural merge before semantic dedup; protects old context |
| `agents/{writer,evaluator,editor}` | P5 | Isolated-context generation with verification gate           |
| `in_review` queue             | P5    | Quarantine for unsupported reversals                           |
| `/wiki-chat`                  | P6    | Vectorless BM25 RAG over the vault                             |
| `/wiki-repair` + `lint_report.md` | P7 | Static lint + auto-repair loop                                |
| `staleness` (supersession)    | P7    | Epistemic staleness, not mtime                                 |
| `eval/harness.py`             | P8    | Wiki-vs-raw-RAG quality measurement                            |
| `migrate.py`                  | P9    | Idempotent backfill to Schema v2                               |

---

## Appendix C — Traceability matrix (proof of completeness)

Every earlier recommendation and every supplied input maps to a phase.

| Source item                                                        | Phase(s) |
|--------------------------------------------------------------------|----------|
| **My rec 1** — retrieval layer as a T2 artifact                    | P6       |
| **My rec 2** — typed edges / contradictions-as-information         | P4       |
| **My rec 3** — claim provenance + commutative ingest + multi-writer safety | P2 |
| **My rec 4** — gated writes / hallucination accumulation           | P5       |
| **My rec 5** — staleness as supersession, not mtime                | P7       |
| **My rec 6** — pix2text install                                    | P1       |
| **My rec 6** — MIND_MAP demotion at scale                          | P8       |
| **My rec 6** — hash-thrash fix (authored-region-only hash)         | P4       |
| **My rec 6** — retrieval/answer-quality eval                       | P8       |
| **Input** — consolidation script (programmatic merge before LLM)   | P3       |
| **Input #1** — deterministic UUID content hashing                  | P1       |
| **Input #2** — Writer → Evaluator → Editor multi-agent pattern     | P5       |
| **Input #3** — automated lint + repair agent (`/wiki-repair`)      | P7       |
| **Input #4** — structural merge before semantic dedup              | P3       |
| **Input #5** — vectorless BM25 RAG (`/wiki-chat`)                  | P6       |
| **Quick action** — `markitdown` for office docs                    | P1       |
| **Quick action** — linting step in the Verify Phase                | P7       |
| **Quick action** — Automated Tools table in `CLAUDE.md`            | P1, P8   |

---

*Hand this file to Claude Code. Start at Phase 0 with `/blueprint architect`. Do not skip the commutativity test in Phase 2 or the disposability check in Phase 6 — they are what make this a durable second brain rather than another pile of summaries.*
