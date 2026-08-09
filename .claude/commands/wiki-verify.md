Check one page against its source document, claim by claim, and record the result. $ARGUMENTS

Run from the repository root. The wiki lives in `wiki/`, not `.`.

This is the hand-check made durable. `verify_wiki`'s Numeric Provenance check
matches figures *literally*, so it cannot see a number that was computed rather
than quoted, and it says nothing about prose claims at all. This command reads
the source and writes down what a human actually confirmed.

The schema has been waiting for this. `VerificationSpec` in
`src/llm_wiki/schemas_v2.py` defines `status: verified | partial | unverified |
disputed` and an `unverified_claims` count. As of 2026-08-07, **zero of 1,595
pages carry it**. Every page you check with this command fills one in.

## Step 1 — find the page and its source

```python
import sys, re
from pathlib import Path

sys.path.insert(0, "src")
from llm_wiki import Wiki
from llm_wiki.io import parse_page
from llm_wiki.provenance import resolve_source_path, extract_numeric_claims

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
print(f"page   : {page.relative_to(wiki.wiki_dir)}")
print(f"status : {(meta.get('verification') or {}).get('status', 'none recorded')}")

# Frontmatter first, body line as fallback -- both conventions exist in this vault.
src = meta.get("source_path")
origin = "frontmatter source_path"
if not src:
    m = re.search(r"Markdown source:\**\s*`([^`]+)`", body)
    if m:
        src, origin = m.group(1), "body **Markdown source:** line"

if not src:
    print("\nNo source recorded. STOP -- do not verify from memory.")
else:
    resolved = resolve_source_path(wiki.root, src)
    print(f"source : {src}  ({origin})")
    print(f"on disk: {resolved if resolved else 'NOT FOUND'}")

print(f"\nfigures on page: {sorted(extract_numeric_claims(body))}")
```

**If the source is missing, stop.** Refusing is the useful answer. Say the page
cannot be verified and why. Never fall back to your own knowledge of the paper —
that is precisely how the 11 fabrications in commit `7ecd005` got written.

## Step 2 — segment the source into citable blocks

Read the resolved source document. Number its sections `B1`, `B2`, `B3` … —
paragraphs, table blocks, or figure captions, whatever the natural unit is.
Keep the numbering stable for the whole check; you will cite it.

## Step 3 — walk the claims

For each claim in the page's `## Key Claims` section, and each figure found
above, classify it as exactly one of:

- **quoted** — appears verbatim in the source. Cite the block: `(B7)`.
- **derived** — computed from values in the source. Cite the blocks *and write
  the arithmetic down*: `(B4, B9: 225.50 / 4.94 = 45.6x)`.
- **unsupported** — you could not locate it in the source.

The derived category is the point. On 2026-08-07 a page reported `Split: -29pp`
and `Bootstrap: 46x wider`; neither string appears anywhere in the paper, because
both are arithmetic on real numbers (90% − 60.58%, and 225.50 / 4.94). A literal
matcher cannot tell that apart from invention. Writing the derivation down is
what makes it auditable next time.

**Never silently drop a claim.** Anything you cannot place goes in the report as
unsupported. A claim that quietly disappears looks identical to one that was
checked and passed.

## Step 4 — record the verdict

Show the user the full claim list with verdicts and get approval before writing.
Then set the frontmatter block:

```python
from llm_wiki.io import update_frontmatter
from llm_wiki.io.hashing import compute_file_hash

update_frontmatter(page, {
    "verification": {
        "status": "verified",        # or partial | unverified | disputed
        "unverified_claims": 0,      # count of unsupported claims
    },
    "verified_on": "YYYY-MM-DD",
    "verified_against": str(resolved),
    "verified_source_hash": compute_file_hash(resolved),
})
```

Use the statuses honestly:

- `verified` — every claim traced to a block.
- `partial` — most traced, some unsupported. Set `unverified_claims`.
- `disputed` — the source contradicts the page. Fix the page, or open a
  contradiction page under `wiki/wiki/contradictions/`.
- `unverified` — leave as-is if you could not do the check.

The source hash is what lets a later run notice the source changed underneath a
stamp that still says `verified`.

## Then

1. If you found a wrong figure, correct it and say what it should be. On
   2026-08-07 this found a Regime D width copied into the adjacent
   dependence-only row, which made the table look internally consistent.
2. Re-run `verify_wiki` to confirm 9/9 still pass.
3. If the page has no `source_path` but the body names one, offer to promote it
   into frontmatter so the automated check can see it too.

## Next actions

- `/wiki-status` — how many pages carry a verification stamp
- `/wiki-relate` — record how this page relates to the ones it agrees or conflicts with
