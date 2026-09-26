# Second Brain CLI Reference

Complete reference for the `sb` command. Implemented in
`src/llm_wiki/secondbrain/`, installed as the `sb` entry point by
`pyproject.toml`.

Every command accepts a global `--root PATH` to point at a different Second
Brain directory. Without it, the location comes from the environment or the
default (see **File Locations**).

---

## Core Commands

### sb init
Create the database and vault directories. Safe to run twice.

```bash
sb init
```

Every other command fails with exit code 2 until this has run.

### sb capture
Capture a thought. Returns an id and nothing else — classification has not run.

```bash
sb capture "Remember to call Mom"
sb capture "API rate limit is 1000/min" --source email
```

**Options:**
- `--source, -s`: where it came from (cli, slack, email, calendar, file). Free text; nothing validates it.

### sb inbox
List captures, newest first.

```bash
sb inbox
sb inbox --status needs_review
sb inbox --limit 50
```

**Options:**
- `--status, -s`: pending, processing, classified, failed, needs_review
- `--limit, -n`: default 20

### sb process
Classify pending captures and turn them into nodes.

```bash
sb process
sb process --id abc12345
sb process --dry-run
```

**Options:**
- `--id`: process one capture
- `--dry-run`: classify and report, write nothing

Output marks low-confidence rows with `?` and prints why they were unclear.

### sb list
List nodes, most recently updated first.

```bash
sb list
sb list task
sb list --status active --domain work --limit 50
```

**Options:**
- positional type: value, goal, project, task, person, meeting, idea, reference
- `--status, -s`: active, completed, archived
- `--domain, -d`: work, personal, both
- `--limit, -n`: default 20

### sb show
Full detail on one node, including its outgoing links.

```bash
sb show abc12345      # id, or any unique prefix
sb show "Call Mom"    # exact title, if unique
```

An ambiguous prefix is an error, not a guess.

### sb query
Substring search over titles and bodies.

```bash
sb query "authentication"
```

**This is not semantic search.** It matches characters. A note that means the
same thing in different words will not be found, and the output says so.

### sb digest
What to focus on.

```bash
sb digest             # today, under 150 words
sb digest --weekly    # seven days, under 250 words
```

Sections are dropped from the bottom when the text would exceed the limit, so
overdue work survives truncation.

### sb export
Write every node to the vault as markdown, grouped into a folder per type.

```bash
sb export
```

The database is the source of truth. Export overwrites vault files from it, so
hand edits to vault files are lost at the next export.

### sb status
Counts and resolved paths.

```bash
sb status
```

---

## Mutating Commands

These change a node that already exists. Each one writes an audit row to the
event log, and refreshes that node's vault file if the vault exists.

```bash
sb done <ref>                  # mark completed, stamps completed_at
sb reopen <ref>                # back to active, clears completed_at
sb archive <ref>               # out of listings, still in the graph
sb priority <ref> <0-4>        # 0 critical, 2 medium (default), 4 backlog
sb domain <ref> work|personal|both
sb retype <ref> <node-type>    # correct the classifier; clears needs_review
sb link <src> <dst> <relation> # typed edge between two nodes
```

`<ref>` is a full id, a unique id prefix, or an exact title.

Relations: supports, blocks, contains, derived_from, assigned_to, mentioned_in,
related_to, child_of.

`sb retype` is what resolves a `needs_review` capture — correcting the type marks
the underlying capture classified.

---

## Classification

Classification is **rule-based and deterministic**, implemented in
`classify.py`. The same text always produces the same type and the same
confidence. No API call, no key, no network, no cost.

- Explicit prefixes (`Task:`, `Idea:`, `Decision:` …) score 0.95 and win outright.
- Pattern matches score 0.65–0.85.
- Nothing matched scores 0.35 and defaults to `reference`.
- Below the threshold (0.6), the node is still created and the capture is marked
  `needs_review`. Losing the thought would be worse than filing it imperfectly.

It also infers priority, domain and a due date. Dates understood: ISO
`2026-04-15`, `March 15`, `15 March`, `today`, `tomorrow`. A month already past
this year resolves to next year.

---

## Output Examples

### Process
```
? 6bcb6eb2  reference  0.35  hmm
    needs review: nothing matched; defaulted to reference
  4acbbce5  task       0.95  review the PR from Sarah by 2026-08-20
  1011cf7d  idea       0.95  order flow imbalance may lead spread moves
```

### List
```
ID         TYPE       STATUS     PRI  DUE          TITLE
1011cf7d   idea       active     2    -            order flow imbalance may lead spread moves
4acbbce5   task       active     2    2026-08-20   review the PR from Sarah
```

### Status
```
Second Brain Status

Configuration:
  Database: /media/ak/.../LLMWikiGeneration/secondbrain/.data/secondbrain.db
  Vault:    /media/ak/.../LLMWikiGeneration/secondbrain/vault
  Threshold: 0.6

Database:
  Total nodes:    3
  Total edges:    0
  Total captures: 3
  Total events:   9

Inbox:
  Pending:      0
  Needs review: 1
```

---

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECONDBRAIN_ROOT` | Second Brain directory | `secondbrain/` at the repo root |
| `SECONDBRAIN_DB` | SQLite file, overrides root | `<root>/.data/secondbrain.db` |
| `SECONDBRAIN_VAULT` | Markdown vault, overrides root | `<root>/vault` |
| `SECONDBRAIN_CONFIDENCE_THRESHOLD` | Auto-file threshold | 0.6 |

`--root` beats all of them.

No API key is required. Classification does not call a model.

---

## File Locations

| File | Purpose | Path |
|------|---------|------|
| Database | nodes, edges, captures, events | `secondbrain/.data/secondbrain.db` |
| Vault | markdown output for Obsidian | `secondbrain/vault/` |

`secondbrain/` is gitignored. This repository is public and captured notes are
not. The database sits in a dot directory so Obsidian does not show it.

The vault is deliberately **not** inside `wiki/`. That vault has schema-v2
frontmatter, provenance checking and a hand-curated MIND_MAP; untyped captures
dropped among those pages would fail the integrity checks.

---

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | General error — no such node, ambiguous prefix, bad argument |
| 2 | Configuration error — usually `sb init` has not been run |
| 3 | Database error |
