---
name: second-brain
description: Personal intelligence system for capturing thoughts, managing knowledge, and surfacing insights. Use when user wants to capture an idea, task, or note during conversation; query their knowledge base; check their inbox; review digests; or update task status. Triggers include "remember this," "add a task," "what did I say about," "show my inbox," or "mark complete."
license: MIT
---

# Second Brain Skill

Conversational interface to the Second Brain personal knowledge management system. Capture thoughts naturally during Claude Code sessions, query your knowledge graph, and manage your inbox.

## Core Philosophy

**Capture at the point of thinking, not after.**

This skill enables seamless capture during work sessions without breaking flow:
- Capture thoughts as they emerge
- Query past decisions and notes
- Surface today's priorities
- Track what needs review

**The system remembers so you don't have to.**

---

## Before You Start

**Run `sb status` first.** If it fails or `sb` is not on PATH, Second Brain is not installed
on this machine. Say so and stop. Do not improvise a substitute.

**Only ever go through the `sb` CLI.** Never write to the SQLite database or the Obsidian
vault by hand, even when a command you want does not exist. Direct writes create nodes the
system does not know about and can corrupt the graph. If a capability is missing, say it is
missing.

**Reference files:**
- `references/cli-reference.md` — the complete `sb` command set. This is the authority on
  what the CLI can do.
- `references/node-types.md` — the classification decision tree, node type definitions,
  priority levels and domain heuristics. Read this before classifying anything by hand.

---

## What Works, and How

| Capability | How it works |
|---|---|
| Capture, inbox, process, digest, status, list, show | Direct `sb` commands |
| Query, transcript processing | Composed from `sb list` / `sb show` / `sb capture`, with the limits noted below |
| Complete, reopen, set priority, archive, retag | **Not possible.** The CLI has no command that modifies an existing node. |

---

## Core Capabilities

### 1. Capture

Capture thoughts, tasks, ideas, and references directly from conversation.

**Usage patterns:**
- "Remember that the API rate limit is 1000 req/min"
- "Add a task to review the PR from Sarah"
- "Note: decided to use Supabase for sync"
- "Capture this idea: what if we..."

**Classification:**
The system uses AI to classify captures into types:
- **task**: Actionable item with completion state
- **idea**: Non-actionable insight worth remembering
- **reference**: Information for later retrieval
- **meeting**: Time-bound event with notes
- **goal**: Outcome you're working toward
- **project**: Collection of related work
- **value**: Core principle that guides decisions
- **person**: Relationship context

See `references/node-types.md` for the full decision tree and the boundaries between types.

**Classification happens in `sb process`, not in `sb capture`.** `sb capture` writes the text
to the inbox and returns an ID. Nothing is classified until `sb process` runs. This means the
node type and the confidence score **do not exist at capture time** — do not report them then.

**Confidence threshold:**
- High confidence (≥0.6): Auto-classified
- Low confidence (<0.6): Sent to needs_review

To find out how a capture was classified, run `sb process`, then `sb inbox --status needs_review`.

---

### 2. Query

Search and explore your knowledge graph.

**Usage patterns:**
- "What did I say about authentication?"
- "What projects support the 'shipping velocity' goal?"
- "Show me tasks related to the SecondBrain project"
- "Who did I meet with about the budget?"

**There is no `sb query` command.** Queries are composed:

```bash
sb list task --limit 50      # or the relevant type
sb show <id>                 # for anything that looks relevant
```

Then filter and rank the results yourself, and answer from what you read.

**What this supports:**
- **Filter by type**: `sb list idea`
- **Filter by domain**: `sb list --domain work`
- **Filter by status**: `sb list --status active`

**What this does not support, and you should say so when asked:**
- **Semantic search.** You are reading a listing and matching by meaning yourself. A node
  whose title does not surface in the listing will be missed.
- **Graph traversal.** There is no command that follows `supports`, `blocks` or `contains`
  edges. Questions like "what projects support this goal?" cannot be answered reliably —
  answer from what the listings show and say the edges were not traversed.

This composition is workable while the graph is small. It degrades as the graph grows past
what a listing can hold.

---

### 3. Inbox

Review and triage pending captures.

**Usage patterns:**
- "Show my inbox"
- "What's waiting for review?"
- "How many pending captures?"

```bash
sb inbox                        # pending captures
sb inbox --status needs_review  # low-confidence items
sb status                       # counts only
```

**Inbox states:**
- **pending**: Awaiting AI classification
- **needs_review**: Low confidence, needs human decision
- **processing**: Currently being classified

Triage means reporting what is there. Resolving a `needs_review` item requires changing a
node, which the CLI cannot do — see §5.

---

### 4. Digest

Get actionable summaries of what matters.

**Usage patterns:**
- "What should I focus on today?"
- "Show me today's digest"
- "What's overdue?"

```bash
sb digest
```

**Digest includes:**
- Due tasks (today and overdue)
- High priority items
- Today's meetings
- Items needing review
- Recent insights

**Constraints:**
- Daily digest: <150 words
- Weekly review: <250 words

**There is no weekly review command.** `sb digest` produces the daily digest only. A weekly
summary has to be composed from `sb list` output, under the same word limit.

---

### 5. Actions

**Not available.** The `sb` CLI has no command that modifies a node once it exists. There is
no way to mark a task complete, reopen it, change its priority, change its status, or add a
domain tag.

When the user asks for one of these:
- "Mark the PR review task done"
- "Complete task abc123"
- "Archive the old project"
- "Set priority to high for..."

Say the CLI cannot do it yet. Do not edit the database or the vault to fake it. If it helps,
offer to capture a note recording the intent, and be clear that this creates a new node rather
than changing the existing one.

---

## Workflow Integration

### During Work Sessions

When user mentions something capture-worthy during natural conversation:

1. **Recognize capture intent:**
   - Direct: "Remember this...", "Add a task..."
   - Implicit: "I should...", "Don't forget...", "Note to self..."

2. **Capture with context:**
   - Include relevant context from current conversation
   - Tag with source: `--source cli` (Claude Code session)
   - Put any relationships in the captured text itself; there is no flag for edges

3. **Confirm capture:**
   - Brief confirmation with the returned ID
   - Do not state a node type or a confidence score — neither exists until `sb process` runs

### Quick Actions

```bash
sb capture "thought or idea"   # Capture immediately
sb inbox                       # Show pending items
sb process                     # Classify what is pending
sb digest                      # Today's actionable summary
sb list task                   # List nodes of a type
sb show <id>                   # Full detail on one node
sb status                      # System health check
```

There is no `sb query` and no `sb done`.

---

## Meeting Transcript Processing

**Use case:** Paste meeting transcripts to automatically extract and capture structured content.

There is no transcript command. This is composed: you do the extraction, then one
`sb capture` per extracted item, then `sb process`.

### Workflow

1. **User pastes transcript:**
   ```
   "Here's the transcript from today's standup:
   [transcript content]"
   ```

2. **Extract the items yourself** — meeting summary, action items, decisions, people,
   follow-ups, insights.

3. **Capture each one**, writing the type and context into the text so classification has
   something to work with:

   ```bash
   sb capture "Meeting: Daily Standup - Jan 15. [summary]" --source cli
   sb capture "Task: Review PR #1234. From standup Jan 15. High priority." --source cli
   sb capture "Decision: using Postgres instead of MongoDB. From standup Jan 15." --source cli
   ```

4. **Classify:** run `sb process`, then `sb inbox --status needs_review` to see what did not
   land confidently.

5. **Report what was captured**, with IDs.

**What this loses, and you should say so.** Captures are independent. You cannot create the
edges linking tasks to the meeting, assign a task to a person, or set a due date — the CLI has
no flags for any of that. Everything is encoded in text and inferred by the classifier.
Assignments and dates survive only as words in the note.

### Extraction Patterns

**Action items (→ TASK):**
- "TODO: ...", "Action: ...", "Need to..."
- "Sarah will...", "I'll...", "We should..."
- "@mentions with action verbs"

**Decisions (→ REFERENCE):**
- "Decided: ...", "Agreed: ..."
- "We're going with...", "The plan is..."
- "Final decision: ..."

**Follow-ups (→ MEETING):**
- "Let's meet again...", "Schedule a follow-up..."
- "Next week we'll discuss..."
- Explicit dates/times mentioned

**People (→ PERSON links):**
- Names mentioned in context
- @mentions
- "talked to...", "asked..."

**Insights (→ IDEA):**
- Observations about patterns
- Hypotheses mentioned
- "I noticed...", "Interesting that..."

### Configuration

A `~/.config/secondbrain/daemons.yml` with `transcript_processing` settings has been proposed
but is not documented in `references/cli-reference.md`. Treat it as unverified — check whether
it exists before relying on it.

```yaml
# ~/.config/secondbrain/daemons.yml — UNVERIFIED
transcript_processing:
  auto_assign_unassigned: true  # Assign to self
  default_task_priority: 2
  flag_low_confidence: true     # Mark uncertain extractions
  link_to_meeting: true         # Connect all items to meeting node
```

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

Full definitions, boundaries and the classification decision tree are in
`references/node-types.md`.

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

**Edges exist in the data model but not in the CLI.** No documented command creates, reads or
follows an edge. Treat the table above as the schema, not as something you can act on.

---

## Implementation

### CLI Integration

This skill wraps the `sb` CLI. The full command set, with options and exit codes, is in
`references/cli-reference.md`.

```bash
sb init                   # Initialize database and directories
sb capture "content"      # Capture a thought
sb inbox                  # List pending captures
sb process                # Classify pending captures
sb digest                 # Generate daily digest
sb list [type]            # List nodes
sb show <id>              # Show node details
sb status                 # System health check
```

That is the whole set. Anything not on this list does not exist.

### Database

- Local SQLite at `~/.local/share/secondbrain/secondbrain.db`
- Obsidian vault for markdown output
- Graph model: nodes + typed edges

Read-only concern for this skill. Never write to either directly.

### Configuration

There are two configuration surfaces and the precedence between them is not documented.
`references/cli-reference.md` lists the environment variables, including `ANTHROPIC_API_KEY`,
`DATABASE_PATH` and `LOG_LEVEL`, which do not appear in the YAML below.

```yaml
# ~/.config/secondbrain/config.yml
node_id: "home"
vault_path: "/path/to/vault"
classification:
  model: "claude-sonnet-4-20250514"
  confidence_threshold: 0.6
```

The pinned classification model is a Claude 4 identifier. Newer models exist. Leave it alone
unless the user asks — the pin may be deliberate.

---

## Context Awareness

### Use Session Context

When capturing, leverage current conversation context:

- **File being discussed**: Link to related codebase notes
- **Error being debugged**: Capture as reference with solution
- **Decision being made**: Note with rationale
- **Meeting notes mentioned**: Parse for action items

Context goes into the captured text. There is no separate field for it.

### Domain Detection

Infer domain from context:
- In work project directory → domain: work
- Personal topics mentioned → domain: personal
- Both contexts mixed → domain: both

Domain cannot be set on capture. `--domain` is a filter on `sb list`, not a flag on
`sb capture`. Write the domain signal into the captured text and let classification infer it.
See the heuristics in `references/node-types.md`.

---

## Example Interactions

### Capture During Work

```
User: "The deadline for the API migration is March 15th"
Assistant: [runs: sb capture "API migration deadline - due March 15th" --source cli]
Captured (ID: abc12345). Not classified yet — run sb process when you want it filed.
```

### Query Knowledge

```
User: "What did we decide about authentication?"
Assistant: [runs: sb list reference --limit 50, then sb show on the relevant ones]
Found 3 related items:
- [reference] "Use JWT with refresh tokens" (Jan 5)
- [task] "Implement OAuth flow" (in_progress)
- [meeting] "Auth design review with Sarah" (Jan 3)

Read from a listing, not a semantic search — there may be more I did not surface.
```

### Morning Digest

```
User: "What should I focus on today?"
Assistant: [runs: sb digest]

📋 Today's Focus (Wed, Jan 15):
- [OVERDUE] Review PR from Sarah (due Jan 14)
- [HIGH] Prepare API migration plan
- [DUE TODAY] Call dentist to reschedule

📅 Meetings:
- 10:00 1:1 with Mike

⚠️ Needs Review: 2 items in inbox
```

---

## Anti-Patterns

**Don't:**
- Capture every single thing mentioned (be selective)
- Force classification when context is unclear
- Interrupt flow for minor captures
- Create duplicate entries for same concept
- Over-classify simple notes
- Invent a command that is not in `references/cli-reference.md`
- Write to the database or the vault directly when a command is missing
- Report a node type or confidence score at capture time

**Do:**
- Capture when user expresses intent or importance
- Ask for clarification if capture intent is ambiguous
- Batch confirmations when capturing multiple items
- Link to existing nodes when relationships are clear
- Respect user's domain boundaries
- Say plainly when a capability does not exist

---

## Integration Points

None of these have a documented CLI surface. Treat them as intended design, not as things
this skill can do today.

**With beads issue tracker:**
- Cross-reference tasks with beads issues
- Import epic/task relationships

**With Obsidian vault:**
- Generated markdown syncs via Obsidian Sync
- Wikilinks enable navigation
- Daily notes include digest

**With SiliconDoppelgangerActual:**
- Deep queries via agent conversation
- Complex graph traversals
- Multi-step reasoning about priorities

---

## Success Metrics

**Skill succeeds when:**
- Captures happen naturally without flow interruption
- User finds past information quickly
- Daily digests surface actionable items
- Inbox stays manageable (<10 items needing review)
- Classification accuracy >85%

**User feels:**
- Confident nothing important is lost
- Informed about what matters today
- In control of their knowledge system
