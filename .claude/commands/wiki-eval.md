Measure whether wiki search actually finds the right page. $ARGUMENTS

Run from the repository root. The wiki lives in `wiki/`, not `.`.

`/wiki-query` warns users that search is plain term matching. Nobody knows how
bad that is, so nobody can tell whether a change made it better. This turns
retrieval quality into a number you can move.

There is a second reason to run it. `src/llm_wiki/retrieval/bm25_index.py`
implements `BM25WikiIndex`, but `get_search_backend` in `src/llm_wiki/search.py`
only ever returns the grep or QMD backend. A better index is sitting unplugged.
Do not wire it in on faith — measure both, then decide.

## Step 1 — build an eval set from the wiki itself

Sample pages, and for each write one question whose answer is that page. The
question must **avoid the page's title words**, or you are testing string match
rather than retrieval.

```python
import sys, json, random
from pathlib import Path

sys.path.insert(0, "src")
from llm_wiki import Wiki
from llm_wiki.io import parse_page

wiki = Wiki(Path("wiki"))
random.seed(0)                      # reproducible: same sample every run

N = 40
pages = [p for p in wiki.list_pages() if p.stem not in ("index", "index.full")]
sample = random.sample(pages, min(N, len(pages)))

for p in sample:
    meta, body = parse_page(p)
    print("=" * 70)
    print("PAGE_ID:", meta.get("page_id"))
    print("TITLE  :", meta.get("title"))
    print(body[:600])
```

Read each one and write a question a person would actually ask. Save them:

```python
CASES = [
    {"q": "which method keeps interval width bounded under both dependence and drift?",
     "gold": "sources/koukorinis-2026-draci"},
    # ... one per sampled page
]
Path("eval_cases.json").write_text(json.dumps(CASES, indent=2))
```

Keep the file out of the wiki — it belongs in the repo root or `eval/`, not in
`wiki/`. It is test data, not knowledge.

## Step 2 — score the current backend

```python
import sys, json
from pathlib import Path

sys.path.insert(0, "src")
from llm_wiki import Wiki, wiki_query

wiki = Wiki(Path("wiki"))
cases = json.loads(Path("eval_cases.json").read_text())

def rank_of(gold, results):
    for i, r in enumerate(results, 1):
        if r["page_id"] == gold:
            return i
    return None

ranks = []
for c in cases:
    res = wiki_query(wiki, c["q"], limit=10)
    ranks.append(rank_of(c["gold"], res.get("results", []) if res.get("success") else []))

def recall_at(k):
    return sum(1 for r in ranks if r and r <= k) / len(ranks)

mrr = sum(1 / r for r in ranks if r) / len(ranks)

print(f"cases      : {len(ranks)}")
for k in (1, 3, 5, 10):
    print(f"recall@{k:<3}: {recall_at(k):.0%}")
print(f"MRR        : {mrr:.3f}")
print(f"missed     : {sum(1 for r in ranks if r is None)}")

print("\nFailures (gold never returned, or buried below 3):")
for c, r in zip(cases, ranks):
    if r is None or r > 3:
        print(f"  rank={r}  {c['gold']}")
        print(f"      q: {c['q']}")
```

## Step 3 — score BM25 against the same cases

```python
from llm_wiki.retrieval.bm25_index import BM25WikiIndex

idx = BM25WikiIndex.build(wiki.wiki_dir)
# Inspect what query() returns before trusting the field names:
probe = idx.query(cases[0]["q"])
print(type(probe), probe[:1])
```

Read that output, then score BM25 with the same `recall_at` and MRR code. Same
cases, same seed — otherwise the comparison means nothing.

## Step 4 — interpret, then act

Report the two backends side by side and say plainly which wins and by how much.

Expect the first number to be bad, and do not flinch from reporting it. Long
source pages and index files tend to dominate term-frequency ranking, which is a
structural problem, not a mystery. Check the cheap structural fixes before
reaching for anything clever:

- Are `index.md` and `index.full.md` in the candidate pool? They should not be.
- Are long `sources/` pages crowding out the shorter `concepts/` page that
  actually answers the question?
- Does title matching carry enough weight?

Each fix is a hypothesis. Change one thing, re-run the same cases, report the
delta. A change that does not move the number is not an improvement.

**Only wire BM25 into `get_search_backend` if it wins on these cases.** It is
currently unreachable code; making it reachable is a real change to how every
query behaves, and it should be justified by a measurement, not a preference.

## Honesty rules

- Report the number you got, including 0%. The point of a baseline is to be
  beaten, and a flattering baseline is useless.
- Never edit a case because search failed it. That is fitting the test to the
  system.
- Say how many cases you ran. Recall@5 on 12 questions is a hint, not a result.

## Next actions

- `/wiki-query` — the command this measures
- `/wiki-status` — corpus size, which sets what a fair sample looks like
