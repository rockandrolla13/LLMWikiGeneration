# LLM Wiki → Second Brain: Design Document (rev 3)

> Approved design for executing LLM_WIKI_SECOND_BRAIN_BUILD_PLAN.md.
> Pre-check result: `frontmatter.parse_page` accessible without importing `wiki.py`. ✓

---

## Core Abstraction

**Content identity over file identity.** UUID derived from semantic content (not path/filename)
unlocks dedup-on-identity, commutative ingest, hash-stable graph edges, and BM25 provenance.

---

## Implementation Sequence (re-ordered from BUILD_PLAN for minimum blast radius)

```
P0  schema.yml v2         — zero code; adds relations vocab + schema_version discriminator
P4  graph.py              — COST-1: relations: targets are slugs, not UUIDs yet
P6  retrieval/            — BM25; commutativity CI gate not yet open
P1  identity.py           — commutativity CI gate opens here
P7  lint_extended.py      — COST: lint flags rot that P3 prevents at source
P3  merge.py              — lint report should shrink noticeably after this
P5  agents/               — markdown prompt specs only
P8  eval/                 — quality measurement
P9  migrate.py            — slug→UUID graph rewrite + schema v2 backfill in one idempotent pass
```

---

## COST-1: Slug→UUID Rewrite (accepted)

Running P4 before P1 means `relations:` blocks written during P4→P6→P1 window use
`page_id` slugs as targets, not UUIDs. P9 migration does two jobs: (a) backfill schema v2
fields + authored-region markers, (b) resolve every `relations.target` slug → UUID.
Accepted: P4+P6 are lowest blast-radius, highest query-ROI phases.

---

## Inverse Edge Decision

**Computed, not persisted.** Inverse edges (superseded-by, extended-by, etc.) are computed
at graph-build time from forward `relations:` blocks. Cached in `.index/graph_cache.json` (T2).
NOT written to any page frontmatter. This avoids authored-region markers being required
before P4 ships, and avoids content_hash thrash during the P4→P9 window.

---

## Literal Split

```python
# ForwardRelType — valid in page frontmatter (what authors write)
ForwardRelType = Literal[
    "extends", "special-case-of", "supersedes",
    "contradicts", "refutes", "depends-on", "was-response-to",
]

# EdgeRelType — returned by graph traversal (forward + computed inverses)
EdgeRelType = Literal[
    "extends", "extended-by",
    "special-case-of", "generalizes",
    "supersedes", "superseded-by",
    "contradicts",
    "refutes", "refuted-by",
    "depends-on", "required-by",
    "was-response-to", "prompted",
]
```

---

## Key Protocols

```python
class ContentHashable(Protocol):
    @property
    def uuid(self) -> UUID: ...
    @property
    def authored_region(self) -> str: ...
    @property
    def content_hash(self) -> str: ...

class TypedEdge(Protocol):
    @property
    def source_id(self) -> str: ...    # slug pre-P1/P9; UUID post-migration
    @property
    def target_id(self) -> str: ...
    @property
    def rel(self) -> EdgeRelType: ...
    @property
    def is_computed(self) -> bool: ... # True = inverse edge

class WikiCompiler(Protocol):
    @property
    def output_path(self) -> Path: ...
    def compile(self, wiki: "Wiki") -> None: ...
    def is_stale(self, wiki: "Wiki") -> bool: ...
```

---

## PageFrontmatterV2

```python
class PageFrontmatterV2(BaseModel):
    schema_version: int = 1    # 1 = v1 (default); 2 = stamped by P9 migrate
    title: str
    page_id: str
    uuid: str | None = None
    page_type: str
    revision_id: int = 1
    content_hash: str | None = None  # authored-region-only hash (P4)
    created: str
    updated: str
    updated_by: str
    verification: VerificationSpec = VerificationSpec()
    tags: list[str] = []
    sources: list[str] = []
    relations: list[RelationSpec] = []  # forward edges only; ForwardRelType
    mind_map_priority: str = "medium"
```

---

## File Structure (new files only — existing files unchanged except schema.yml)

```
src/llm_wiki/
├── identity.py              # P1
├── merge.py                 # P3
├── graph.py                 # P4
├── staleness.py             # P7
├── lint_extended.py         # P7
├── repair.py                # P7
├── agents/
│   ├── writer.md            # P5
│   ├── evaluator.md         # P5
│   └── editor.md            # P5
├── retrieval/
│   ├── __init__.py          # P6
│   ├── chunker.py           # P6
│   └── bm25_index.py        # P6
└── io/
    └── authored_hash.py     # P4 — io/hashing.py NOT modified

eval/
├── questions.jsonl          # P8
└── harness.py               # P8

scripts/migrate.py           # P9

wiki/schema.yml              # MODIFY P0
.index/                      # T2, gitignored
```

---

## P7 Before P3 — Expected Behaviour

Between P7 ship and P3 ship, lint reports will flag structural rot (dropped sections)
that P3 would have prevented at the source. This is correct: P7 is a safety net for the
pre-merge world. After P3 lands, the lint STRUCTURAL row count should shrink noticeably.
If it does not shrink, P3 is not working.

---

## wiki.py Scope

Out of scope. Pre-check confirmed `frontmatter.parse_page` and `frontmatter.get_frontmatter`
are accessible without importing `wiki.py`. All new modules import from `frontmatter` or
`io/page_io` directly.

---

## Available Packages (verified)

- `pydantic` 2.12.5 ✓
- `rank_bm25` ✓ (installed)
- `markdown_it` ✓
- `uuid` (built-in) ✓
