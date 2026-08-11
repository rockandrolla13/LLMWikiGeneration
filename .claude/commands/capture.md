Capture a thought into the Second Brain. $ARGUMENTS

Records it instantly and gets out of the way. Nothing is classified at capture
time, so nothing can block or fail.

## What to run

From the repository root:

```bash
PYTHONPATH=src python -m llm_wiki.secondbrain.cli capture "$ARGUMENTS" --source cli
```

If that reports no database, run `PYTHONPATH=src python -m llm_wiki.secondbrain.cli init`
once and try again.

## Add the type prefix when you know it

A capture beginning `Task:`, `Idea:`, `Decision:`, `Reference:`, `Meeting:`,
`Goal:`, `Project:`, `Person:` or `Value:` classifies at 0.95 confidence and
never lands in review. Without one, the classifier guesses from wording, and
anything it cannot read goes to `needs_review`.

So if the user's words make the type obvious but they did not say it, prepend it.
"remember the rate limit is 1000/min" becomes `Reference: the rate limit is
1000/min`. If the type is genuinely unclear, capture the text as written — a
wrong prefix is worse than no prefix, because it classifies confidently and wrong.

Keep the user's own wording otherwise. Do not rewrite, summarise or tidy it.

## What to report back

One line. The short id, and that it is not filed yet:

```
Captured (4acbbce5). Run /wiki-inbox or `sb process` to file it.
```

Do not state a node type or a confidence score. Neither exists until
`sb process` runs — claiming one is inventing a fact.

## Context is worth folding in

If the capture refers to something in the current session — a file, an error, a
paper being read, a decision just made — add that context to the captured text.
There is no separate field for it, and a note that says "this breaks under
NTFS" is worth much more than one that says "this breaks".

## Related

- `sb process` — classify what is pending
- `sb inbox --status needs_review` — what the classifier was unsure about
- `sb digest` — what is due
- Full command reference: `.claude/skills/second-brain/references/cli-reference.md`
