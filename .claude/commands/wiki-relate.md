Record *how* pages relate, not just that they link, and lint the result. $ARGUMENTS

Run from the repository root. The wiki lives in `wiki/`, not `.`.

Your graph is 1,595 pages joined by untyped `[[wikilinks]]`. A link tells you two
pages mention each other. It does not tell you that Bao (2025) **supersedes**
Angelopoulos & Bates (2022), or that two sources **contradict** each other — and
in a research wiki those are the two most valuable facts you can store.

**This machinery is already built and completely unused.** `schemas_v2.py`
defines the vocabulary, `graph.py` reads a `relations:` frontmatter block and
computes the inverse edge automatically, and `KnowledgeGraph` exposes
`lineage()`, `challenges()` and `assumptions()`. As of 2026-08-07, **zero of
1,595 pages carry a `relations:` block**. This command fills them in.

## The vocabulary — use these exact strings

Forward relations, from `src/llm_wiki/schemas_v2.py`. Do not invent others; the
graph builder validates against this list.

| Forward | Computed inverse | Use when |
|---|---|---|
| `supersedes` | `superseded-by` | later work replaces earlier |
| `contradicts` | `contradicts` (symmetric) | the two disagree on a claim |
| `refutes` | `refuted-by` | one demonstrates the other is wrong |
| `extends` | `extended-by` | builds on without replacing |
| `special-case-of` | `generalizes` | narrower instance of a general result |
| `depends-on` | `required-by` | needs the other to hold |
| `was-response-to` | `prompted` | written in reply to |

You only ever write the forward edge. `build_graph` computes the inverse — never
hand-write `superseded-by`.

## Step 1 — see what is already there

```python
import sys
from pathlib import Path

sys.path.insert(0, "src")
from llm_wiki import Wiki
from llm_wiki.io import parse_page
from llm_wiki.graph import load_or_build_graph

wiki = Wiki(Path("wiki"))

have = [p for p in wiki.list_pages() if parse_page(p)[0].get("relations")]
print(f"pages carrying relations: {len(have)} / {len(list(wiki.list_pages()))}")

g = load_or_build_graph(wiki.wiki_dir)
edges = g.to_dict()
print(f"graph edges: {len(edges.get('edges', []))}")
```

## Step 2 — propose relations for a page

Given a page (from `$ARGUMENTS`, else ask), read it and the pages it already
links to. Propose relations only where you can point at the sentence that
justifies them. Show the user each proposal with its evidence:

```
bao-2025-...            supersedes      angelopoulos-bates-2022-...
   evidence: "we relax the exchangeability requirement of [AB22]" (page 3)
```

Rules that keep this honest:

- **Never infer a relation from topic overlap.** Two conformal-prediction papers
  are not `related` in any typed sense just because they share a subject. If you
  cannot quote the justification, do not propose the edge.
- **`contradicts` is a finding, not a defect.** Record it and leave both pages
  standing. Do not "reconcile" them by rewriting either one. If the conflict is
  substantive, open a page under `wiki/wiki/contradictions/`.
- **`supersedes` needs a date check.** Confirm the superseding page is actually
  the later work before writing it.

## Step 3 — write, after approval

```python
from llm_wiki.io import update_frontmatter

update_frontmatter(page, {
    "relations": [
        {"rel": "supersedes", "target": "sources/angelopoulos-bates-2022-gentle-intro"},
        {"rel": "contradicts", "target": "sources/some-other-page"},
    ]
})
```

`target` must be a real `page_id`. Verify each one resolves before writing —
a dangling target is a broken edge that no wikilink check will catch.

## Step 4 — lint

Run after any batch of edits. These are the failure modes that matter:

```python
import sys
from pathlib import Path

sys.path.insert(0, "src")
from llm_wiki import Wiki
from llm_wiki.io import parse_page
from llm_wiki.schemas_v2 import INVERSE_MAP

wiki = Wiki(Path("wiki"))
ids = {parse_page(p)[0].get("page_id") for p in wiki.list_pages()}

problems = []
for p in wiki.list_pages():
    meta, _ = parse_page(p)
    me = meta.get("page_id")
    for e in (meta.get("relations") or []):
        rel, tgt = e.get("rel"), e.get("target")
        if rel not in INVERSE_MAP:
            problems.append(f"UNKNOWN REL  {me}: {rel!r}")
        if tgt not in ids:
            problems.append(f"DANGLING     {me} -{rel}-> {tgt}")
        if tgt == me:
            problems.append(f"SELF EDGE    {me} -{rel}-> itself")

print(f"{len(problems)} problems")
for x in problems[:30]:
    print("  ", x)
```

Also look for **supersession cycles** — if A supersedes B and B supersedes A,
one of them is wrong. A cycle in `supersedes` is always an error; a cycle in
`contradicts` is expected, because it is symmetric.

## Where to start

The highest-value edges first, not a bulk sweep:

1. Your `wiki/wiki/contradictions/` pages — they already assert a conflict in
   prose. Make it a typed edge so `KnowledgeGraph.challenges()` can find it.
2. Papers with an obvious lineage: a 2025 method paper and the 2018-2022 work it
   relaxes an assumption from.
3. Anything where a later source changed your mind.

Do not attempt all 1,595 pages. An edge you cannot justify is worse than no edge.

## Next actions

- `/wiki-verify` — check a page's claims against its source before relating it
- `/wiki-query` — the graph makes "what superseded this?" answerable
