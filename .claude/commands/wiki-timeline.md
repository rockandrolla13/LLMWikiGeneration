Record how a fact changed over time, and when the wiki learned it. $ARGUMENTS

Run from the repository root. The wiki lives in `wiki/`, not `.`.

The wiki has no memory. When a claim is revised, the old value is overwritten and
the fact that it ever changed is gone. That costs you two things a research wiki
needs: you cannot ask "what did the literature say in 2022", and you cannot tell
a *correction* from a *revision* — whether a number changed because we were wrong
or because the field moved.

This command records both clocks:

- **Event time** (`from` / `until`) — when the fact was true in the world.
- **Transaction time** (`learned`) — when this wiki found out.

Keeping them apart is what makes "we believed X until we read Y" expressible.
Different facts at different times are not a contradiction; the same fact
asserted two ways at the same time is.

## Read this before using it

**This convention is not in the schema.** `schemas_v2.py` has no timeline field,
and `verify_wiki` will not check it. That makes it exactly the kind of
unenforced convention that caused this vault's worst failure — provenance was
recorded three different ways and only one was ever checked.

So: use this on a small number of high-value pages first. If it earns its keep,
the right next step is adding it to `PageMeta` in `schemas_v2.py` with a check in
`verify.py`, not spreading it across 1,595 pages unenforced.

## The shape

```yaml
# Top-level field is ALWAYS the current state -- readers and search see this.
result: "94% coverage at rho=0.99"

timeline:
  - fact: "67% coverage predicted at rho=0.99"
    from: 2026-02-01        # event time: when this was the standing claim
    until: 2026-04-22       # when it stopped being current
    learned: 2026-02-01     # transaction time: when the wiki recorded it
    source: "[[sources/koukorinis-2026-draci]]"
    why: "theoretical switch-coefficient bound"
  - fact: "94% coverage measured at rho=0.99"
    from: 2026-04-22
    until: present
    learned: 2026-04-22
    source: "[[sources/koukorinis-2026-draci]]"
    why: "200 supplementary Monte Carlo trials; bound is conservative"
```

Rules:

- **Append, never overwrite.** The old entry keeps its `until` date and stays.
- **Every entry carries a `source`.** An entry you cannot source does not go in.
- **`why` is short and factual** — what caused the change, not commentary.
- The top-level field mirrors the entry whose `until` is `present`. Exactly one
  entry may be `present`.

## Step 1 — see the current state

```python
import sys
from pathlib import Path

sys.path.insert(0, "src")
from llm_wiki import Wiki
from llm_wiki.io import parse_page

wiki = Wiki(Path("wiki"))
TARGET = "$ARGUMENTS".strip()

matches = [p for p in wiki.list_pages() if TARGET.lower() in p.stem.lower()]
if len(matches) != 1:
    print(f"{len(matches)} pages match {TARGET!r}:")
    for p in matches[:20]:
        print("   ", p.stem)
    raise SystemExit
page = matches[0]

meta, body = parse_page(page)
tl = meta.get("timeline") or []
print(f"page     : {page.relative_to(wiki.wiki_dir)}")
print(f"timeline : {len(tl)} entries")
for e in tl:
    print(f"   {e.get('from')} -> {e.get('until')}  (learned {e.get('learned')})  {e.get('fact')}")
```

## Step 2 — add an entry

Establish, and state to the user, three things before writing:

1. **What the fact was**, in the page's own words, as it currently stands.
2. **What it is now**, and the source that changed it.
3. **Which kind of change this is** — a correction (we were wrong) or a revision
   (the world moved). Say which; they mean different things to a later reader.

Then close the open entry and append the new one:

```python
from llm_wiki.io import update_frontmatter

tl = list(meta.get("timeline") or [])
for e in tl:
    if e.get("until") == "present":
        e["until"] = "2026-08-07"          # today

tl.append({
    "fact":    "the new claim, stated plainly",
    "from":    "2026-08-07",
    "until":   "present",
    "learned": "2026-08-07",
    "source":  "[[sources/whatever-page]]",
    "why":     "short reason",
})

update_frontmatter(page, {"timeline": tl, "result": "the new claim"})
```

If the page had no timeline, seed it with the *existing* value as the first
entry before appending — otherwise you lose the very history you came to record.
Set that first entry's `learned` to the page's `created` date, not today, and say
in your report that it is inferred.

## What to use it on

Not everything. Facts worth versioning are ones where being out of date would
mislead:

- A result that was corrected — today's DR-ACI width, 4.9 corrected to 3.38.
- A theoretical bound later shown to be loose — the 67% bound versus 94% measured.
- A method superseded by later work. Pair with `/wiki-relate`'s `supersedes` edge:
  the edge says *which* page replaced it, the timeline says *when and why*.
- An entity's affiliation, when a paper's claims depend on it.

Do not version prose, definitions, or anything whose old value nobody would ask for.

## Next actions

- `/wiki-relate` — record which page superseded this one
- `/wiki-verify` — confirm the new value against its source before recording it
