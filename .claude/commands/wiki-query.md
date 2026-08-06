Search the wiki and answer a question from what it finds. $ARGUMENTS

If no question is given, ask what the user wants to know.

The wiki is in `wiki/`, not the repo root. Run from the repository root.

`wiki_query` is a **search**, not a question-answerer: it returns ranked pages,
not prose. Read the pages it surfaces, then answer in your own words with
`[[wikilinks]]` back to them. Do not answer from your own knowledge — if the
wiki does not cover it, say so. A gap is a useful result.

```python
import sys
from pathlib import Path

sys.path.insert(0, "src")
from llm_wiki import Wiki, wiki_query

wiki = Wiki(Path("wiki"))

QUESTION = "$ARGUMENTS"

result = wiki_query(wiki, QUESTION, limit=8)

if not result["success"]:
    print(f"Search failed: {result.get('error')}")
else:
    print(f"{result['count']} pages matched (backend: {result['backend']})\n")
    for r in result["results"]:
        print(f"[{r['score']:.2f}] {r['page_id']}  -- {r['title']}")
        print(f"        {r['snippet'][:160]}")
        print()
```

## Then

1. Read the top 3-7 pages returned, by `page_id`.
2. Answer from those pages, citing each claim as `[[page_id|label]]`.
3. If the wiki does not answer it, say so plainly.
4. If the answer is worth keeping, offer to save it under `wiki/wiki/analyses/`.

## Filters

```python
wiki_query(wiki, "carry", page_types=["concept"], limit=5)   # concepts only
wiki_query(wiki, "momentum", tags=["creditETF"], limit=5)     # by tag
```

Page types: `source`, `concept`, `entity`, `analysis`, `contradiction`.

## Notes

- Search is plain term matching, not semantic. Try two or three phrasings
  before concluding the wiki is silent on a topic.
- For a broad question, `wiki/MIND_MAP.md` is a faster way in: 211 curated
  nodes with cross-references. `grep "^\[12\]" wiki/MIND_MAP.md` fetches one.
- `wiki/wiki/index.md` is the lightweight index, one line per page. Do not read
  `index.full.md` for queries; it is large and meant for maintenance.
- `wiki/BACKLOG.md` lists topics the wiki names but has never written up.
