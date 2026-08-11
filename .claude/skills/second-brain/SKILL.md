---
name: second-brain
description: Capture thoughts, tasks and ideas during a session, then retrieve them later. Use when the user wants to record an idea, task or note; search what they have captured; check their inbox; see a digest; or complete, archive, reprioritise or link an existing item. Triggers include "remember this," "add a task," "what did I say about," "show my inbox," and "mark complete."
license: MIT
---

# Second Brain Skill

Conversational interface to the Second Brain, a capture system that lives in
this repository. It is the companion to the wiki: the wiki holds what you have
read, this holds what you thought while reading it.

## Core Philosophy

**Capture at the point of thinking, not after.**

- Capture thoughts as they emerge
- Retrieve past decisions and notes
- Surface today's priorities
- Track what needs review

**The system remembers so you don't have to.**

---

## Before You Start

**Run `sb status` first.** If it reports a missing database, run `sb init`. If
the `sb` command itself is not found, the package is not installed — from the
repository root, `pip install -e .`, or run it directly as
`python -m llm_wiki.secondbrain.cli`.

**Only ever go through the `sb` CLI.** Never edit
`secondbrain/.data/secondbrain.db` or write into `secondbrain/vault/` by hand.
The database is the source of truth and export overwrites vault files from it,
so hand edits are silently lost. Every capability described here has a command;
if you find yourself wanting to write a file directly, you have misread the
reference.

**Reference files:**
- `references/cli-reference.md` — every command, option and exit code. The
  authority on what the CLI can do.
- `references/node-types.md` — the classification decision tree, type
  definitions, priority levels and domain heuristics.

---

## Where things live

| | |
|---|---|
| Code | `src/llm_wiki/secondbrain/` |
| Database | `secondbrain/.data/secondbrain.db` |
| Vault | `secondbrain/vault/` — plain markdown, open it in Obsidian |
| Tests | `tests/test_secondbrain_*.py` |

`secondbrain/` is gitignored. This repository is public; captured notes are not.

**Never point the vault at `wiki/`.** That vault is schema-v2, provenance-checked
and index-rebuilt, and untyped captures among those pages break the integrity
checks.

---

## Core Capabilities

### 1. Capture

```bash
sb capture "Remember that the API rate limit is 1000 req/min"
sb capture "Idea: order flow imbalance may lead spread moves" --source cli
```

**Recognise capture intent** in ordinary conversation:
- Direct: "Remember this...", "Add a task..."
- Implicit: "I should...", "Don't forget...", "Note to self..."

**Write the type in when you know it.** A capture beginning `Task:`, `Idea:`,
`Decision:`, `Meeting:`, `Goal:`, `Project:`, `Person:` or `Value:` classifies at
0.95 confidence and never needs review. This is the single highest-value thing
you can do at capture time.

**Confirm with the id, and nothing else.** `sb capture` does not classify. The
node type and the confidence score **do not exist yet**, so do not report them.
Say what was captured, give the short id, and mention that `sb process` will
file it.

### 2. Process

```bash
sb process              # classify everything pending
sb process --dry-run    # report without writing
```

Classification is rule-based and deterministic — no API call, no cost. Rows
marked `?` scored below 0.6 and are flagged `needs_review`; the node is still
created, because losing the thought is worse than filing it imperfectly.

Resolve a flagged item with `sb retype <id> <type>`, which also clears the
review flag.

### 3. Retrieve

```bash
sb list task --status active
sb list --domain work --limit 50
sb show abc12345
sb query "authentication"
```

**`sb query` is a substring match, not semantic search.** It matches characters,
so a note that means the same thing in different words will be missed. When you
answer from it, say that — do not present it as an exhaustive search. For a
broader sweep, `sb list` a type and read the titles yourself.

Relationships are real: `sb show` prints a node's outgoing links, and
`sb link <src> <dst> <relation>` creates them.

### 4. Inbox

```bash
sb inbox                        # pending
sb inbox --status needs_review  # low confidence, awaiting a decision
sb status                       # counts only
```

### 5. Digest

```bash
sb digest             # today, under 150 words
sb digest --weekly    # seven days, under 250 words
```

### 6. Actions

All available. Each writes an audit row and refreshes the node's vault file.

```bash
sb done <ref>                  # completed
sb reopen <ref>                # back to active
sb archive <ref>               # out of listings, still in the graph
sb priority <ref> <0-4>        # 0 critical, 2 default, 4 backlog
sb domain <ref> work|personal|both
sb retype <ref> <node-type>    # correct the classifier
sb link <src> <dst> <relation>
```

`<ref>` is a full id, a unique id prefix, or an exact title. An ambiguous prefix
is an error rather than a guess — add characters, do not pick one.

---

## Meeting Transcript Processing

There is no transcript command. Compose it: extract the items, capture each one
with an explicit type prefix, classify, then link them to the meeting.

1. **Extract** — meeting summary, action items, decisions, people, follow-ups,
   insights.

2. **Capture each one with its type written in**, so nothing lands in review:

   ```bash
   sb capture "Meeting: Daily Standup 2026-01-15. [summary]"
   sb capture "Task: review PR #1234. From standup 2026-01-15. High priority."
   sb capture "Decision: using Postgres instead of MongoDB."
   sb capture "Person: Sarah Chen - VP Engineering"
   ```

3. **Classify:** `sb process`

4. **Link them to the meeting** so the graph is navigable:

   ```bash
   sb link <task-id> <meeting-id> mentioned_in
   sb link <task-id> <person-id> assigned_to
   ```

5. **Report** what was captured, with ids, and flag anything in `needs_review`.

**What this loses.** Due dates are only picked up in recognised formats — ISO,
"March 15", "15 March", "today", "tomorrow". Anything vaguer ("end of next
sprint") survives as words in the note, not as a due date. Say so rather than
implying a date was set.

### Extraction Patterns

**Action items (→ TASK):** "TODO:", "Action:", "Need to...", "Sarah will...",
"I'll...", "We should..."

**Decisions (→ REFERENCE):** "Decided:", "Agreed:", "We're going with...",
"Final decision:"

**Follow-ups (→ MEETING):** "Let's meet again...", "Schedule a follow-up...",
explicit dates and times

**People (→ PERSON):** names in context, @mentions, "talked to...", "asked..."

**Insights (→ IDEA):** "I noticed...", "Interesting that...", observations about
patterns, hypotheses

---

## Graph Model

### Node Types

| Type | Description | Example |
|------|-------------|---------|
| value | Core principle | "Family comes first" |
| goal | Outcome to achieve | "Run a marathon by December" |
| project | Related work collection | "Kitchen renovation" |
| task | Actionable item | "Call dentist to schedule" |
| person | Relationship context | "Sarah - VP Engineering" |
| meeting | Time-bound event | "1:1 with Sarah - Jan 15" |
| idea | Non-actionable insight | "What if AI for onboarding?" |
| reference | Info for retrieval | "API rate limit: 1000/min" |

Full definitions and the decision tree are in `references/node-types.md`.

### Edge Types

| Relation | Meaning | Example |
|----------|---------|---------|
| supports | Provides evidence for | project → goal |
| blocks | Prevents progress on | task → task |
| contains | Hierarchical parent | project → task |
| derived_from | Extracted from | goal → value |
| assigned_to | Assigned to person | task → person |
| mentioned_in | Referenced in context | person → meeting |
| related_to | General relationship | idea → reference |
| child_of | Subtask/child | task → task |

Create them with `sb link`, read them with `sb show`.

---

## Context Awareness

Context goes into the captured text — there is no separate field for it. When
capturing during work, fold in what you were doing: the file under discussion,
the error being debugged, the rationale behind a decision.

Domain is inferred from wording, not set on capture. `--domain` is a filter on
`sb list`, not a flag on `sb capture`. To fix one, use `sb domain <ref> work`.
The heuristics are in `references/node-types.md`.

---

## Example Interactions

### Capture during work

```
User: "The deadline for the API migration is March 15th"
Assistant: [sb capture "Task: API migration deadline - March 15th"]
Captured (4acbbce5). Run `sb process` when you want it filed.
```

### Retrieve

```
User: "What did we decide about authentication?"
Assistant: [sb query "auth"]
Three matches:
- [reference] Use JWT with refresh tokens (1011cf7d)
- [task] Implement OAuth flow (4acbbce5)
- [meeting] Auth design review with Sarah (6bcb6eb2)

Substring match, so anything phrased differently would not surface.
```

### Morning digest

```
User: "What should I focus on today?"
Assistant: [sb digest]

Focus (2026-08-11):
- [OVERDUE] Review PR from Sarah (4acbbce5)
- [DUE TODAY] Call dentist to reschedule (6bcb6eb2)

Needs review:
- hmm (e319a652)
```

---

## Anti-Patterns

**Don't:**
- Capture every single thing mentioned — be selective
- Interrupt flow for minor captures
- Report a node type or confidence score at capture time
- Present `sb query` results as an exhaustive search
- Invent a command that is not in `references/cli-reference.md`
- Edit the database or the vault directly
- Guess which node an ambiguous id prefix meant

**Do:**
- Capture when the user signals intent or importance
- Write the type prefix in at capture time when you know it
- Batch confirmations when capturing several items
- Link related nodes once they exist
- Say plainly when something could not be captured as asked

---

## Success Metrics

**The skill is working when:**
- Captures happen without breaking the user's flow
- Past information is found quickly
- Digests surface what is actually due
- Fewer than ten items sit in `needs_review`

**The user feels:**
- Confident nothing important is lost
- Informed about what matters today
- In control of their knowledge system
