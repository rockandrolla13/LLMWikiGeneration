> **Archive.** This is a historical planning document. Current operational spec is `CLAUDE.md` + `docs/REFERENCE.md`.

# LLM Wiki: Implementation Plan v2

**Markdown as Single Source of Truth**

---

## Executive Summary

This document defines the architecture for LLM Wiki — a system that compiles knowledge from sources into a persistent, interlinked wiki. The architecture follows a strict **three-tier data ownership model** where markdown files are the only canonical representation of knowledge.

**Core Principle:** If you have `wiki/` + `manifest.jsonl`, you can rebuild everything else.

---

## Table of Contents

1. [Three-Tier Data Ownership](#1-three-tier-data-ownership)
2. [Canonical Data Model (Tier 1)](#2-canonical-data-model-tier-1)
3. [Derived Artifacts (Tier 2)](#3-derived-artifacts-tier-2)
4. [Ephemeral Context (Tier 3)](#4-ephemeral-context-tier-3)
5. [System Integration](#5-system-integration)
6. [Operations & Skills](#6-operations--skills)
7. [Invariants & Verification](#7-invariants--verification)
8. [Failure Modes & Recovery](#8-failure-modes--recovery)
9. [Implementation Phases](#9-implementation-phases)
10. [Test Suite](#10-test-suite)

---

## 1. Three-Tier Data Ownership

### 1.1 The Critical Test

```
Given: manifest.jsonl + wiki/ directory (Tier 1 only)
Can you: Rebuild MIND_MAP, QMD index, and continue work?
Answer: YES → correct architecture
        NO  → something canonical is in wrong tier
```

### 1.2 Tier Classification

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ TIER 1: CANONICAL                                                            │
│ (wiki/*.md + manifest.jsonl)                                                │
│                                                                              │
│ Properties:                                                                  │
│   • Durable: Cannot be lost without data loss                               │
│   • Versioned: Every change creates new revision                            │
│   • Backed up: Regular snapshots required                                   │
│   • Human-readable: Obsidian-compatible markdown                            │
│                                                                              │
│ Contains:                                                                    │
│   wiki/sources/*.md           Source summaries (one per ingested document)  │
│   wiki/entities/*.md          Entity profiles (people, orgs, places)        │
│   wiki/concepts/*.md          Concept explanations (ideas, methods)         │
│   wiki/analyses/*.md          Saved insights (query answers, comparisons)   │
│   wiki/contradictions/*.md    Contradiction records (when sources disagree) │
│   manifest.jsonl              Operation ledger (append-only, NOT markdown)  │
│   schema.yml                  Wiki configuration (profile, taxonomy)        │
│                                                                              │
│ NOT Tier 1:                                                                  │
│   MIND_MAP.md                 → Tier 2 (derived from wiki links)           │
│   index.md                    → Tier 2 (generated table of contents)       │
│   QMD index                   → Tier 2 (search index, rebuildable)         │
│   OMEGA memories              → Tier 3 (session context, ephemeral)        │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ TIER 2: DERIVED                                                              │
│ (Recomputable from Tier 1)                                                  │
│                                                                              │
│ Properties:                                                                  │
│   • Can be regenerated from canonical data                                  │
│   • May be cached for performance                                           │
│   • Loss is inconvenient but not catastrophic                               │
│   • Not backed up (rebuilt instead)                                         │
│                                                                              │
│ Contains:                                                                    │
│   MIND_MAP.md                 Compiled from wiki links + frontmatter        │
│   index.md                    Auto-generated table of contents              │
│   ~/.cache/qmd/index.sqlite   Search index (BM25 + vectors)                │
│   health_report.md            Lint output                                   │
│   stats.json                  Wiki statistics                               │
│   wiki/.cache/                Local derived cache                           │
│                                                                              │
│ Contract: rebuild_derived() reproduces all Tier 2 from Tier 1 alone        │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ TIER 3: EPHEMERAL                                                            │
│ (Session-scoped, not persisted)                                             │
│                                                                              │
│ Properties:                                                                  │
│   • Discarded between sessions (or kept for debugging only)                 │
│   • Adds context but not canonical knowledge                                │
│   • Loss has no impact on wiki correctness                                  │
│                                                                              │
│ Contains:                                                                    │
│   ~/.omega/omega.db           Session decisions, working memory             │
│   /tmp/wiki_cache/            Temp files during operations                  │
│   operation_logs/*.log        Telemetry (observability only)                │
│                                                                              │
│ OMEGA's role: Session context and navigation assistance, NOT knowledge      │
│ If OMEGA is empty, wiki is still 100% functional (just no session memory)  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.3 Data Classification Table

| Artifact | Tier | Rationale |
|----------|------|-----------|
| `wiki/sources/*.md` | 1 | Domain knowledge: source summaries |
| `wiki/entities/*.md` | 1 | Domain knowledge: entity profiles |
| `wiki/concepts/*.md` | 1 | Domain knowledge: concept explanations |
| `wiki/analyses/*.md` | 1 | Domain knowledge: saved insights |
| `wiki/contradictions/*.md` | 1 | Domain knowledge: disagreements between sources |
| `manifest.jsonl` | 1 | Operation provenance (required for audit) |
| `schema.yml` | 1 | Wiki configuration |
| `raw/*` | 1 | Original sources (immutable reference) |
| `MIND_MAP.md` | 2 | Computed from wiki page links and frontmatter |
| `index.md` | 2 | Computed from wiki page titles and paths |
| `~/.cache/qmd/*` | 2 | Search index, rebuildable from wiki/ |
| `health_report.md` | 2 | Computed by lint operation |
| `stats.json` | 2 | Computed from wiki metrics |
| `~/.omega/omega.db` | 3 | Session context, ephemeral |
| `/tmp/*` | 3 | Temporary processing files |
| `*.log` | 3 | Observability, not knowledge |

### 1.4 Decision Rule

```
Question: Where does this data belong?

If data represents domain knowledge      → Tier 1 (markdown in wiki/)
If data is computed from domain knowledge → Tier 2 (derived, rebuildable)
If data is operational context           → Tier 3 (ephemeral, discardable)
```

---

## 2. Canonical Data Model (Tier 1)

### 2.1 Directory Structure

```
project/
├── raw/                        # Original sources (immutable)
│   ├── paper1.pdf
│   ├── article2.md
│   └── assets/
│       └── figure1.png
│
├── wiki/                       # CANONICAL KNOWLEDGE (Tier 1)
│   ├── sources/                # One page per ingested source
│   │   ├── paper1.md
│   │   └── article2.md
│   │
│   ├── entities/               # One page per entity
│   │   ├── john-smith.md
│   │   └── acme-corp.md
│   │
│   ├── concepts/               # One page per concept
│   │   ├── machine-learning.md
│   │   └── attention-mechanism.md
│   │
│   ├── analyses/               # Saved query answers
│   │   └── transformer-comparison.md
│   │
│   ├── contradictions/         # Explicit contradiction records
│   │   └── scaling-disagreement.md
│   │
│   └── .history/               # Optional: revision history
│       └── concepts/
│           └── machine-learning/
│               ├── rev_001.md
│               └── rev_002.md
│
├── manifest.jsonl              # Operation ledger (Tier 1, NOT markdown)
├── schema.yml                  # Wiki configuration
│
├── MIND_MAP.md                 # DERIVED (Tier 2)
├── index.md                    # DERIVED (Tier 2)
└── health_report.md            # DERIVED (Tier 2)
```

### 2.2 Page Schema (Frontmatter)

Every canonical wiki page has revision-tracked frontmatter:

```yaml
---
# Identity
title: "Machine Learning"
page_id: "concepts/machine_learning"

# Revision tracking
revision_id: 47
revision_hash: "sha256:8f3a2c4b..."
created: "2024-01-01T10:00:00Z"
updated: "2024-01-15T14:30:00Z"
updated_by: "op_042"

# Relationships
sources:
  - "sources/ng2023_ml_course"
  - "sources/goodfellow2016_deep_learning"
related:
  - "concepts/neural_networks"
  - "concepts/deep_learning"

# Classification
tags: ["ai", "ml", "core_concept"]
page_type: "concept"  # source | entity | concept | analysis | contradiction

# Derived artifact hints (for MIND_MAP generation)
mind_map_priority: "high"  # high | medium | low | exclude
mind_map_category: 2       # Which routing node [1-5] this belongs under
---
```

**Revision Semantics:**

| Field | Description |
|-------|-------------|
| `revision_id` | Monotonically increasing integer, starts at 1 |
| `revision_hash` | SHA-256 of page body (excluding frontmatter except title) |
| `updated_by` | Reference to `op_id` in manifest.jsonl |

**Constraint:** Every write operation MUST:
1. Increment `revision_id`
2. Recompute `revision_hash`
3. Update `updated` timestamp
4. Set `updated_by` to current operation ID

### 2.3 Page Type Schemas

#### Source Page (`wiki/sources/*.md`)

```yaml
---
title: "Attention Is All You Need (2017)"
page_id: "sources/vaswani2017_attention"
page_type: "source"

# Source-specific
source_path: "raw/vaswani2017_attention.pdf"
source_hash: "sha256:def456..."
source_type: "paper"  # paper | article | book | notes | transcript
authors: ["Ashish Vaswani", "Noam Shazeer", "..."]
publication_date: "2017-06-12"
publication_venue: "NeurIPS 2017"

# Standard fields
revision_id: 1
revision_hash: "sha256:abc123..."
created: "2024-01-15T14:30:00Z"
updated: "2024-01-15T14:30:00Z"
updated_by: "op_001"
tags: ["transformers", "attention", "seminal_paper"]
related:
  - "concepts/attention_mechanism"
  - "concepts/transformer_architecture"
  - "entities/google_brain"
---

# Attention Is All You Need (2017)

## Summary

[One-paragraph summary of the paper]

## Key Claims

1. **Claim:** Attention mechanisms alone suffice for sequence transduction
   - Evidence: [description]
   - Confidence: High

2. **Claim:** Transformer achieves SOTA on translation benchmarks
   - Evidence: BLEU scores on WMT 2014
   - Confidence: High (empirical)

## Methodology

[Description of methods used]

## Limitations

[Acknowledged limitations and caveats]

## Notable Quotes

> "Attention is all you need" (p. 1)

## Questions Raised

- How does this scale to very long sequences?
- What are the memory requirements?

## Extracted Entities

- [[Google Brain]] - Affiliation of authors
- [[Ashish Vaswani]] - First author

## Extracted Concepts

- [[Attention Mechanism]] - Core contribution
- [[Transformer Architecture]] - Proposed model
- [[Self-Attention]] - Key technique
```

#### Entity Page (`wiki/entities/*.md`)

```yaml
---
title: "Andrew Ng"
page_id: "entities/andrew_ng"
page_type: "entity"

# Entity-specific
entity_type: "person"  # person | organization | place | product
aliases: ["Andrew Y. Ng", "吴恩达"]
external_ids:
  google_scholar: "mG4imMEAAAAJ"
  wikipedia: "Andrew_Ng"

# Standard fields
revision_id: 3
revision_hash: "sha256:..."
created: "2024-01-10T09:00:00Z"
updated: "2024-01-15T14:30:00Z"
updated_by: "op_042"
sources:
  - "sources/ng2023_ml_course"
  - "sources/ng2011_deep_learning"
tags: ["person", "researcher", "ai", "education"]
related:
  - "entities/stanford_university"
  - "entities/deeplearning_ai"
  - "concepts/machine_learning"
---

# Andrew Ng

## Overview

[Brief description of the entity]

## Relevance to Wiki

[Why this entity matters in the context of this wiki]

## Appearances in Sources

| Source | Context |
|--------|---------|
| [[ng2023_ml_course]] | Instructor |
| [[ng2011_deep_learning]] | Author |

## Relationships

- **Affiliated with:** [[Stanford University]], [[DeepLearning.AI]]
- **Known for:** [[Machine Learning]], [[Deep Learning]]
```

#### Concept Page (`wiki/concepts/*.md`)

```yaml
---
title: "Attention Mechanism"
page_id: "concepts/attention_mechanism"
page_type: "concept"

# Concept-specific
concept_type: "technique"  # technique | theory | framework | methodology
abstraction_level: "foundational"  # foundational | intermediate | advanced

# Standard fields
revision_id: 12
revision_hash: "sha256:..."
created: "2024-01-05T11:00:00Z"
updated: "2024-01-15T14:30:00Z"
updated_by: "op_042"
sources:
  - "sources/vaswani2017_attention"
  - "sources/bahdanau2015_attention"
tags: ["deep_learning", "nlp", "architecture"]
related:
  - "concepts/transformer_architecture"
  - "concepts/self_attention"
  - "concepts/multi_head_attention"
mind_map_priority: "high"
mind_map_category: 3
---

# Attention Mechanism

## Definition

[Clear, concise definition]

## Key Properties

- Property 1
- Property 2

## How It Works

[Explanation with examples]

## Relationship to Other Concepts

- **Prerequisite for:** [[Transformer Architecture]]
- **Variant of:** [[Self-Attention]], [[Multi-Head Attention]]
- **Contrasts with:** [[Recurrence]], [[Convolution]]

## Claims Across Sources

| Claim | Source | Confidence |
|-------|--------|------------|
| Enables parallel computation | [[vaswani2017_attention]] | High |
| O(n²) complexity with sequence length | [[vaswani2017_attention]] | High |
| Can replace recurrence entirely | [[vaswani2017_attention]] | Medium (debated) |

## Contradictions

See: [[contradictions/attention_scaling_debate]]

## Open Questions

- How to reduce quadratic complexity?
- Optimal number of attention heads?
```

#### Contradiction Page (`wiki/contradictions/*.md`)

```yaml
---
title: "Attention Scaling Debate"
page_id: "contradictions/attention_scaling_debate"
page_type: "contradiction"

# Contradiction-specific
status: "unresolved"  # unresolved | resolved | superseded
topic: "concepts/attention_mechanism"
sources_involved:
  - "sources/vaswani2017_attention"
  - "sources/kitaev2020_reformer"

# Standard fields
revision_id: 2
revision_hash: "sha256:..."
created: "2024-01-12T16:00:00Z"
updated: "2024-01-14T10:00:00Z"
updated_by: "op_038"
tags: ["contradiction", "attention", "scaling"]
---

# Attention Scaling Debate

## The Contradiction

**Source A:** [[vaswani2017_attention]]
- **Claim:** Standard attention is sufficient for practical sequence lengths
- **Evidence:** Strong results on WMT translation (sequence length ~100)

**Source B:** [[kitaev2020_reformer]]
- **Claim:** Standard attention is prohibitively expensive for long sequences
- **Evidence:** Memory analysis showing O(n²) is impractical for n > 4096

## Analysis

[Discussion of why these claims conflict]

## Possible Resolutions

1. Different contexts (short vs long sequences)
2. Different definitions of "practical"
3. Time-dependent (2017 vs 2020 hardware)

## Current Status

**Unresolved** — Both claims appear valid in their respective contexts.

## Impact on Wiki

- [[concepts/attention_mechanism]] notes this limitation
- [[analyses/transformer_comparison]] discusses tradeoffs
```

### 2.4 Manifest Schema

The `manifest.jsonl` is the operation ledger — the only non-markdown canonical artifact.

**Format:** JSON Lines (one JSON object per line)

```jsonl
{"op_id":"op_001","op_type":"init","timestamp":"2024-01-01T10:00:00Z","actor":"user","inputs":{"profile":"research-papers","topic":"transformer architectures"},"outputs":{"created_files":["schema.yml"]},"status":"completed"}
{"op_id":"op_002","op_type":"ingest","timestamp":"2024-01-15T14:30:00Z","actor":"llm","inputs":{"source_path":"raw/vaswani2017.pdf","source_hash":"sha256:abc..."},"outputs":{"created_pages":["sources/vaswani2017_attention","entities/google_brain"],"updated_pages":["concepts/attention_mechanism"],"page_revisions":{"sources/vaswani2017_attention":1,"entities/google_brain":1,"concepts/attention_mechanism":12}},"status":"completed","derived_invalidated":["MIND_MAP.md","index.md","qmd_index"]}
{"op_id":"op_003","op_type":"query","timestamp":"2024-01-15T15:00:00Z","actor":"llm","inputs":{"question":"How does attention scale?"},"outputs":{"answer_saved":false,"pages_consulted":["concepts/attention_mechanism","sources/vaswani2017_attention"]},"status":"completed"}
{"op_id":"op_004","op_type":"rebuild_derived","timestamp":"2024-01-15T15:05:00Z","actor":"llm","inputs":{"artifacts":["MIND_MAP.md","index.md","qmd_index"]},"outputs":{"mind_map_nodes":15,"index_entries":23,"qmd_documents":23},"status":"completed","duration_ms":4500}
```

**Operation Types:**

| op_type | Description | Modifies Tier 1 |
|---------|-------------|-----------------|
| `init` | Initialize wiki | Yes (creates schema.yml) |
| `ingest` | Process source into wiki | Yes (creates/updates pages) |
| `query` | Answer question | Maybe (if answer saved) |
| `lint` | Health check | No |
| `rebuild_derived` | Regenerate Tier 2 | No |
| `edit` | Manual page edit | Yes |
| `delete` | Remove page | Yes |

**Manifest Guarantees:**

1. **Append-only:** Never edit existing entries
2. **Atomic:** Entry written only after canonical data safely on disk
3. **Replayable:** Can rebuild wiki by replaying ops from empty state (with raw/ available)
4. **Auditable:** Full provenance of every change

### 2.5 Schema Configuration

`schema.yml` — Wiki configuration (Tier 1):

```yaml
# Wiki identity
wiki_name: "Transformer Research Wiki"
wiki_id: "transformer_research_2024"
created: "2024-01-01T10:00:00Z"
profile: "research-papers"

# Taxonomy (which folders exist)
taxonomy:
  sources:
    path: "wiki/sources"
    description: "One page per ingested source document"
  entities:
    path: "wiki/entities"
    types: ["person", "organization", "place"]
    description: "Named entities referenced across sources"
  concepts:
    path: "wiki/concepts"
    description: "Ideas, methods, and themes"
  analyses:
    path: "wiki/analyses"
    description: "Saved query answers and comparisons"
  contradictions:
    path: "wiki/contradictions"
    description: "Records of disagreements between sources"

# MIND_MAP generation rules
mind_map:
  routing_nodes:
    1: "Overview — wiki purpose, main themes"
    2: "Key sources — most important papers/documents"
    3: "Core concepts — foundational ideas"
    4: "Open questions — unresolved issues"
    5: "Contradictions — where sources disagree"
  max_nodes: 50
  exclude_tags: ["minor", "stub"]

# QMD search configuration
search:
  collection_name: "wiki"
  contexts:
    "wiki/sources": "Source document summaries"
    "wiki/entities": "Entity profiles (people, organizations)"
    "wiki/concepts": "Concept explanations"
    "wiki/analyses": "Saved analyses and comparisons"
    "wiki/contradictions": "Documented disagreements"

# Ingest behavior
ingest:
  require_confirmation: true
  extract_entities: true
  extract_concepts: true
  flag_contradictions: true

# Derived artifact settings
derived:
  auto_rebuild: false  # If true, rebuild after every operation
  rebuild_on_session_start: true
```

---

## 3. Derived Artifacts (Tier 2)

### 3.1 MIND_MAP.md

**Source:** All `wiki/*.md` files with wikilinks and frontmatter
**Generator:** `compile_mind_map()`
**Determinism:** Same input wiki → identical MIND_MAP (excluding timestamps)

```markdown
<!--
DERIVED ARTIFACT — DO NOT EDIT MANUALLY

Source: wiki/*.md (all pages)
Generated: 2024-01-15T15:05:00Z
Generator: compile_mind_map v1.0.0
Manifest op: op_004
Input hash: sha256:fedcba...

To rebuild: /wiki:rebuild mind_map
Manual edits will be overwritten on next rebuild.
-->

> **For AI Agents:** This mind map is your navigation index. Read overview nodes [1-5] first, then follow links [N] to find what you need. This file is auto-generated from wiki page metadata.

[1] **Wiki Overview** - Research on transformer architectures and attention mechanisms. Key sources include the original Transformer paper [6] and BERT [7]. Core concepts in [3]. Open questions in [4]. Contradictions documented in [5].

[2] **Key Sources** - The foundational papers in this wiki [1]. Vaswani et al. 2017 [6] introduced transformers. Devlin et al. 2018 [7] introduced BERT. See full source list in index.md.

[3] **Core Concepts** - Foundational ideas [1]. Attention mechanisms [8] enable parallel sequence processing. Transformer architecture [9] builds on attention. Self-attention [10] and multi-head attention [11] are key variants.

[4] **Open Questions** - Unresolved issues across the research [1]. Scaling attention to long sequences remains challenging (see [5]). Optimal architecture depth is debated between [6] and [7].

[5] **Contradictions** - Documented disagreements [1]. Attention scaling debate [12] between Vaswani and Kitaev. Architecture depth disagreement between [6] (6 layers) and [7] (12-24 layers).

[6] **Vaswani 2017: Attention Is All You Need** - Original transformer paper [2]. Introduced self-attention [10] and multi-head attention [11]. Argues 6 layers optimal. Source: wiki/sources/vaswani2017_attention.md

[7] **Devlin 2018: BERT** - Bidirectional pre-training [2]. Uses 12-24 transformer layers, contradicting [6] on depth. Source: wiki/sources/devlin2018_bert.md

[8] **Attention Mechanisms** - Core technique [3]. Computes relevance weights over inputs. Has O(n²) complexity (debated in [12]). Concept: wiki/concepts/attention_mechanism.md

[9] **Transformer Architecture** - Dominant NLP architecture [3]. Uses attention [8] instead of recurrence. Concept: wiki/concepts/transformer_architecture.md

[10] **Self-Attention** - Attention within single sequence [8][3]. Query, key, value from same input. Concept: wiki/concepts/self_attention.md

[11] **Multi-Head Attention** - Parallel attention functions [8][3]. Typically 8-16 heads. Concept: wiki/concepts/multi_head_attention.md

[12] **Contradiction: Attention Scaling** - Debate between [6] and Kitaev 2020 [5]. Standard attention: sufficient or prohibitive? Contradiction: wiki/contradictions/attention_scaling_debate.md
```

**Generation Algorithm:**

```
1. Read schema.yml for routing node definitions
2. For each wiki page with mind_map_priority != "exclude":
   a. Extract: title, page_id, wikilinks, tags, mind_map_category
   b. Assign node number based on category and priority
3. Generate routing nodes [1-5] from schema definitions
4. Generate content nodes [6+] for each page
5. Compute cross-references from wikilinks
6. Format as single-line nodes
7. Add generation metadata header
```

**Contract:**

| Property | Guarantee |
|----------|-----------|
| Input | All `wiki/**/*.md` with frontmatter |
| Output | Single markdown file with numbered nodes |
| Determinism | `hash(wiki/) → hash(MIND_MAP)` (excluding timestamps) |
| Regeneration | < 30s for 1000-page wiki |
| Grep-friendly | Each node is single line: `grep "^\[5\]" MIND_MAP.md` |

### 3.2 index.md

**Source:** All `wiki/*.md` file paths and titles
**Generator:** `compile_index()`
**Determinism:** Same input → identical output

```markdown
<!--
DERIVED ARTIFACT — DO NOT EDIT MANUALLY

Generated: 2024-01-15T15:05:00Z
Generator: compile_index v1.0.0
Manifest op: op_004
-->

# Wiki Index

*Auto-generated table of contents. Last updated: 2024-01-15*

## Sources (12 pages)

| Page | Title | Created | Sources |
|------|-------|---------|---------|
| [vaswani2017_attention](sources/vaswani2017_attention.md) | Attention Is All You Need | 2024-01-15 | - |
| [devlin2018_bert](sources/devlin2018_bert.md) | BERT: Pre-training | 2024-01-14 | - |
| ... | ... | ... | ... |

## Entities (8 pages)

| Page | Title | Type | Sources |
|------|-------|------|---------|
| [google_brain](entities/google_brain.md) | Google Brain | organization | 3 |
| [andrew_ng](entities/andrew_ng.md) | Andrew Ng | person | 2 |
| ... | ... | ... | ... |

## Concepts (15 pages)

| Page | Title | Priority | Sources |
|------|-------|----------|---------|
| [attention_mechanism](concepts/attention_mechanism.md) | Attention Mechanism | high | 5 |
| [transformer_architecture](concepts/transformer_architecture.md) | Transformer Architecture | high | 4 |
| ... | ... | ... | ... |

## Analyses (3 pages)

| Page | Title | Created |
|------|-------|---------|
| [transformer_comparison](analyses/transformer_comparison.md) | Transformer Model Comparison | 2024-01-15 |
| ... | ... | ... |

## Contradictions (2 pages)

| Page | Title | Status |
|------|-------|--------|
| [attention_scaling_debate](contradictions/attention_scaling_debate.md) | Attention Scaling Debate | unresolved |
| ... | ... | ... |

---

**Statistics:**
- Total pages: 40
- Sources: 12
- Entities: 8
- Concepts: 15
- Analyses: 3
- Contradictions: 2
```

### 3.3 QMD Search Index

**Location:** `~/.cache/qmd/index.sqlite`
**Source:** All `wiki/**/*.md` files
**Generator:** `qmd update && qmd embed`

**Contract:**

| Property | Guarantee |
|----------|-----------|
| Input | All `wiki/**/*.md` (full text + frontmatter) |
| Output | SQLite database with BM25 + vector embeddings |
| Determinism | Non-deterministic (embedding model variance), functionally equivalent |
| Regeneration | < 5 min for 1000-page wiki |
| Freshness check | `qmd status` returns synced/stale/missing |

**Context Configuration (from schema.yml):**

```bash
qmd collection add wiki/ --name wiki
qmd context add qmd://wiki "Transformer research wiki"
qmd context add qmd://wiki/sources "Source document summaries"
qmd context add qmd://wiki/entities "Entity profiles"
qmd context add qmd://wiki/concepts "Concept explanations"
qmd context add qmd://wiki/analyses "Saved analyses"
qmd context add qmd://wiki/contradictions "Documented disagreements"
```

### 3.4 health_report.md

**Source:** Wiki structure analysis
**Generator:** `lint_wiki()`
**Determinism:** Same wiki state → same report

```markdown
<!--
DERIVED ARTIFACT

Generated: 2024-01-15T16:00:00Z
Generator: lint_wiki v1.0.0
-->

# Wiki Health Report

*Generated: 2024-01-15T16:00:00Z*

## Summary

| Metric | Value | Status |
|--------|-------|--------|
| Total pages | 40 | ✓ |
| Orphan pages | 2 | ⚠ Warning |
| Broken links | 0 | ✓ |
| Missing frontmatter | 1 | ⚠ Warning |
| QMD index | synced | ✓ |
| MIND_MAP | fresh | ✓ |

## Issues

### Warnings (3)

1. **Orphan page:** `wiki/analyses/old_draft.md`
   - No inbound links from other pages
   - Action: Link from relevant pages or delete

2. **Orphan page:** `wiki/entities/minor_author.md`
   - No inbound links
   - Action: Review relevance

3. **Missing frontmatter:** `wiki/concepts/temp_note.md`
   - Missing: revision_id, revision_hash
   - Action: Run `/wiki:fix-frontmatter`

### Info

- QMD index last updated: 2024-01-15T15:05:00Z
- MIND_MAP last generated: 2024-01-15T15:05:00Z
- Manifest operations: 42

## Recommendations

1. Address orphan pages to improve wiki connectivity
2. Consider running `/wiki:rebuild` to ensure all derived artifacts are fresh
```

### 3.5 Rebuild Procedure

**Command:** `/wiki:rebuild [artifact]`

```bash
# Rebuild all derived artifacts
/wiki:rebuild

# Rebuild specific artifact
/wiki:rebuild mind_map
/wiki:rebuild index
/wiki:rebuild qmd
/wiki:rebuild all
```

**Rebuild Algorithm:**

```
1. Verify Tier 1 integrity:
   - All pages have valid frontmatter
   - All revision_hashes match content
   - manifest.jsonl is valid JSON Lines

2. Rebuild MIND_MAP.md:
   - Read all wiki pages
   - Extract links and metadata
   - Generate nodes per algorithm
   - Write with generation header

3. Rebuild index.md:
   - Read all wiki page frontmatter
   - Generate tables per category
   - Write with generation header

4. Rebuild QMD index:
   - qmd collection remove wiki (if exists)
   - qmd collection add wiki/ --name wiki
   - Apply contexts from schema.yml
   - qmd update
   - qmd embed

5. Log operation to manifest.jsonl
```

---

## 4. Ephemeral Context (Tier 3)

### 4.1 OMEGA's Role: Session Context, Not Knowledge

**Critical distinction:**
- OMEGA stores *operational context* (what you're working on, recent decisions)
- Wiki stores *domain knowledge* (what you've learned from sources)

**OMEGA is helpful but not canonical:**
- If OMEGA is empty, wiki is 100% functional
- OMEGA memories are pointers to wiki pages, not duplicates
- Session summaries help continuity but aren't knowledge

### 4.2 OMEGA Memory Types (Ephemeral)

| Type | Purpose | Canonical? |
|------|---------|------------|
| `session_start` | Record session began | No |
| `session_end` | Record session ended with summary | No |
| `navigation` | "User asked about X, consulted pages Y, Z" | No |
| `decision` | "Decided to focus on attention scaling" | No |
| `pointer` | "Key insight in wiki/concepts/attention.md rev 12" | No (pointer only) |

**Key constraint:** OMEGA memories NEVER contain domain knowledge directly. They contain:
- Session metadata
- Navigation history
- Pointers to wiki pages (with revision IDs)

### 4.3 What OMEGA Provides

**Session start:**
```
Welcome back to Transformer Research Wiki.

Last session (2 days ago):
- Ingested 2 papers on attention mechanisms
- Queried about scaling behavior
- Working hypothesis: linear attention may solve scaling

Recent wiki changes:
- wiki/concepts/attention_mechanism.md (rev 12)
- wiki/contradictions/attention_scaling_debate.md (rev 2)

Suggested starting points:
- Continue investigation of linear attention variants
- [[concepts/attention_mechanism]] has open questions
```

**Navigation assistance:**
```
You asked about "attention scaling".

Relevant pages (from QMD):
- [[concepts/attention_mechanism]] (high relevance)
- [[contradictions/attention_scaling_debate]] (directly relevant)

From this session:
- You previously looked at [[sources/vaswani2017_attention]]
- You noted the O(n²) complexity concern
```

### 4.4 What OMEGA Does NOT Provide

- ❌ Canonical knowledge (that's in wiki/)
- ❌ Source summaries (that's in wiki/sources/)
- ❌ Entity information (that's in wiki/entities/)
- ❌ Concept definitions (that's in wiki/concepts/)

**If you want to remember something, it goes in the wiki, not OMEGA.**

### 4.5 OMEGA Lifecycle

```
Session Start:
├── Load recent memories (last 7 days)
├── Query wiki for recent changes
├── Generate welcome context
└── Clear memories older than 30 days

During Session:
├── Log navigation (which pages consulted)
├── Log decisions (user choices)
├── Store pointers to wiki revisions
└── Do NOT duplicate wiki content

Session End:
├── Generate session summary
├── Store summary in OMEGA (ephemeral)
├── Optionally: user can save insights to wiki/analyses/
└── Clear temporary navigation logs
```

---

## 5. System Integration

### 5.1 Four Systems, Clear Roles

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              Claude Code                                     │
│                                                                              │
│  Skills: /wiki:init, /wiki:ingest, /wiki:query, /wiki:lint, /wiki:rebuild  │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           llm-wiki Pattern                                   │
│                                                                              │
│  Defines: Operations, page schemas, revision semantics, tier ownership      │
│  Stored in: This document (reference) + schema.yml (per-project config)    │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
            ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
            │   wiki/     │ │    QMD      │ │   OMEGA     │
            │  (Tier 1)   │ │  (Tier 2)   │ │  (Tier 3)   │
            │             │ │             │ │             │
            │ Canonical   │ │ Search      │ │ Session     │
            │ knowledge   │ │ index       │ │ context     │
            │             │ │             │ │             │
            │ Markdown    │ │ SQLite      │ │ SQLite      │
            │ files       │ │ (derived)   │ │ (ephemeral) │
            └─────────────┘ └─────────────┘ └─────────────┘
                    │               │               │
                    │               │               │
                    ▼               ▼               ▼
            ┌─────────────────────────────────────────────┐
            │              User (Obsidian)                 │
            │                                              │
            │  Reads: wiki/*.md (canonical)               │
            │  Browses: MIND_MAP.md, index.md (derived)   │
            │  Ignores: QMD, OMEGA (infrastructure)       │
            └─────────────────────────────────────────────┘
```

### 5.2 Data Flow: Write Path

```
User: "Ingest this paper"
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 1. OPERATION STARTS                                              │
│                                                                  │
│    Generate op_id: "op_043"                                     │
│    Record in memory: operation started                          │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. WRITE CANONICAL DATA (Tier 1)                                 │
│                                                                  │
│    Create/update wiki pages:                                    │
│    - wiki/sources/paper.md (rev 1)                              │
│    - wiki/entities/author.md (rev 1 or rev N+1)                │
│    - wiki/concepts/topic.md (rev N+1)                           │
│                                                                  │
│    Each page write:                                             │
│    - Increment revision_id                                       │
│    - Compute revision_hash                                       │
│    - Set updated_by: "op_043"                                   │
│                                                                  │
│    Ensure: All writes complete successfully before proceeding   │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. APPEND TO MANIFEST (Tier 1)                                   │
│                                                                  │
│    Append to manifest.jsonl:                                    │
│    {                                                            │
│      "op_id": "op_043",                                         │
│      "op_type": "ingest",                                       │
│      "outputs": {                                               │
│        "created_pages": ["sources/paper"],                      │
│        "updated_pages": ["concepts/topic"],                     │
│        "page_revisions": {...}                                  │
│      },                                                         │
│      "status": "completed",                                     │
│      "derived_invalidated": ["MIND_MAP.md", "index.md", "qmd"]  │
│    }                                                            │
│                                                                  │
│    ATOMIC: Manifest entry written only after pages are safe     │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. INVALIDATE DERIVED ARTIFACTS (Tier 2)                         │
│                                                                  │
│    Mark as stale:                                               │
│    - MIND_MAP.md (needs regeneration)                           │
│    - index.md (needs regeneration)                              │
│    - QMD index (needs update)                                   │
│                                                                  │
│    Option A: Rebuild immediately (if auto_rebuild: true)        │
│    Option B: Mark stale, rebuild on next read/session start     │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. UPDATE EPHEMERAL CONTEXT (Tier 3)                             │
│                                                                  │
│    OMEGA: Store navigation record                               │
│    - "Ingested paper X, created pages Y, Z"                     │
│    - Pointer to wiki/sources/paper.md rev 1                     │
│                                                                  │
│    This is context, not knowledge                               │
└─────────────────────────────────────────────────────────────────┘
```

### 5.3 Data Flow: Read Path

```
User: "What do sources say about attention scaling?"
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 1. CHECK DERIVED FRESHNESS                                       │
│                                                                  │
│    If QMD stale:                                                │
│      - Warn user OR rebuild automatically                       │
│    If MIND_MAP stale:                                           │
│      - Rebuild (fast, < 30s)                                    │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. SEARCH (Tier 2: QMD)                                          │
│                                                                  │
│    qmd query "attention scaling" --json                         │
│                                                                  │
│    Returns ranked list of wiki page paths                       │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. READ CANONICAL PAGES (Tier 1)                                 │
│                                                                  │
│    Read top-N wiki pages:                                       │
│    - wiki/concepts/attention_mechanism.md                       │
│    - wiki/contradictions/attention_scaling_debate.md            │
│    - wiki/sources/vaswani2017_attention.md                      │
│                                                                  │
│    These are the source of truth                                │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. ADD SESSION CONTEXT (Tier 3: OMEGA)                           │
│                                                                  │
│    OMEGA: "In previous session, you noted O(n²) concern"        │
│                                                                  │
│    This is helpful context, not authoritative                   │
│    If OMEGA empty, query still works (just less context)        │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. SYNTHESIZE ANSWER                                             │
│                                                                  │
│    Combine:                                                     │
│    - Canonical knowledge from wiki pages (authoritative)        │
│    - Session context from OMEGA (helpful but not authoritative) │
│                                                                  │
│    Cite wiki pages: "According to [[attention_mechanism]]..."   │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 6. OFFER TO SAVE (Optional)                                      │
│                                                                  │
│    If answer is valuable:                                       │
│    "Save as wiki/analyses/attention_scaling_analysis.md?"       │
│                                                                  │
│    If yes: Write to Tier 1, append to manifest                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5A. Write Pipeline with Transaction Boundaries

### 5A.1 Pipeline Overview

All write operations flow through a 5-stage pipeline with clear transaction boundaries. The critical property: **Stage 3 (COMMIT) is the atomic transaction boundary** — either all canonical data is written or none is.

```
┌────────────────────────────────────────────────────────────┐
│ STAGE 1: VALIDATE (Pre-flight checks)                      │
│ Duration: < 1s                                             │
│ Mutates: Nothing                                           │
├────────────────────────────────────────────────────────────┤
│ • Parse inputs (source file, parameters)                   │
│ • Check schemas (valid frontmatter, etc.)                  │
│ • Verify permissions (if multi-user)                       │
│ • Detect duplicates (source already ingested?)             │
│ • Check available disk space                               │
│ • Estimate cost (tokens, time, storage)                    │
│                                                             │
│ Exit conditions:                                            │
│   - PASS → Proceed to Stage 2                              │
│   - FAIL → Return error, no side effects                   │
└────────────────────────────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────────────────────────┐
│ STAGE 2: COMPUTE (Generate canonical content)              │
│ Duration: Seconds to minutes (LLM calls)                   │
│ Mutates: Only in-memory                                    │
├────────────────────────────────────────────────────────────┤
│ • Extract entities, concepts, claims (LLM)                 │
│ • Generate page content (markdown)                         │
│ • Resolve slugs (check aliases, detect conflicts)          │
│ • Compute revisions (increment IDs, compute hashes)        │
│ • Build manifest entry                                      │
│ • Create write plan (which files to create/update)         │
│                                                             │
│ Exit conditions:                                            │
│   - SUCCESS → Proceed to Stage 3                           │
│   - FAIL → Return error, no side effects (all in-memory)   │
└────────────────────────────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────────────────────────┐
│ STAGE 3: COMMIT (Write canonical data atomically)          │
│ Duration: < 5s                                             │
│ Mutates: wiki/ + manifest.jsonl (Tier 1)                  │
├────────────────────────────────────────────────────────────┤
│ • Acquire locks (if needed for concurrency)                │
│ • Write all markdown files atomically:                     │
│   - Primary: Write-ahead log (WAL)                         │
│   - Alternative: Shadow directory + atomic swap            │
│ • Append manifest entry (only after files committed)       │
│ • Release locks                                             │
│                                                             │
│ *** CRITICAL: This stage must be ALL-OR-NOTHING ***        │
│                                                             │
│ Exit conditions:                                            │
│   - SUCCESS → Canonical data committed, proceed to Stage 4 │
│   - FAIL → Rollback any partial writes, return error       │
│                                                             │
│ Failure handling:                                           │
│   - If crash mid-commit: WAL replay on restart             │
│   - If disk full: Rollback, return error                   │
│   - If conflict detected: Rollback, return conflict error  │
└────────────────────────────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────────────────────────┐
│ STAGE 4: DERIVE (Update indexes asynchronously)            │
│ Duration: Seconds (can run in background)                  │
│ Mutates: QMD index, MIND_MAP (Tier 2)                     │
├────────────────────────────────────────────────────────────┤
│ • Enqueue derived jobs:                                     │
│   - update_mind_map()                                       │
│   - reindex_qmd(page_ids)                                  │
│   - capture_omega_insights() [optional]                    │
│                                                             │
│ • Jobs execute asynchronously                               │
│ • Failures do NOT affect canonical data                    │
│ • Can retry independently                                   │
│                                                             │
│ Exit conditions:                                            │
│   - Jobs queued → Operation complete (from user POV)       │
│   - Actual execution tracked in job queue                  │
└────────────────────────────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────────────────────────┐
│ STAGE 5: VERIFY (Check invariants)                         │
│ Duration: < 2s                                             │
│ Mutates: Nothing (read-only checks)                        │
├────────────────────────────────────────────────────────────┤
│ • Run post-commit invariant checks                         │
│ • Verify wikilinks resolve                                  │
│ • Verify revision IDs incremented correctly                 │
│ • Verify frontmatter schema compliance                      │
│                                                             │
│ Exit conditions:                                            │
│   - PASS → Mark operation "verified" in manifest           │
│   - FAIL → Mark "needs_repair", enqueue repair job         │
│             But operation still "completed" (data written) │
└────────────────────────────────────────────────────────────┘
```

**Transaction Boundary Summary:**

| Stage | Side Effects | Failure Impact |
|-------|--------------|----------------|
| 1. VALIDATE | None | Safe, no cleanup needed |
| 2. COMPUTE | None (in-memory) | Safe, no cleanup needed |
| **3. COMMIT** | **Tier 1 (canonical)** | **Must rollback atomically** |
| 4. DERIVE | Tier 2 (derived) | Retry later, no data loss |
| 5. VERIFY | None | Flag for repair, no data loss |

### 5A.2 Write-Ahead Log (WAL) Implementation

The primary mechanism for atomic commits is a write-ahead log.

**Principle:** Record all intended writes to a log BEFORE executing them. On crash, replay or rollback incomplete entries.

```python
class WriteAheadLog:
    """
    Implements atomic writes using write-ahead logging.

    File: manifest.wal (JSON Lines format)

    Each WAL entry records intended writes before execution.
    On crash, replay or rollback incomplete entries.
    """

    def __init__(self, wiki_path: str):
        self.wiki_path = wiki_path
        self.wal_path = os.path.join(wiki_path, "manifest.wal")

    def begin_transaction(self, op_id: str) -> "Transaction":
        """
        Start transaction, create WAL entry.

        WAL entry structure:
        {
          "op_id": "op_123",
          "status": "in_progress",
          "writes": [],
          "started_at": "2024-01-15T14:30:00Z"
        }
        """
        wal_entry = {
            "op_id": op_id,
            "status": "in_progress",
            "writes": [],
            "started_at": datetime.utcnow().isoformat() + "Z"
        }
        self._append_to_wal(wal_entry)
        return Transaction(op_id, wal_entry, self)

    def record_write(self, tx: "Transaction", path: str, content: str) -> None:
        """
        Record write intent in WAL, then write to temp file.

        Algorithm:
        1. Compute content_hash
        2. Add to WAL entry: {"path": path, "content_hash": hash, "size": len}
        3. Write to temp file: {path}.tmp
        4. fsync temp file to ensure durability
        """
        content_hash = hashlib.sha256(content.encode()).hexdigest()
        content_size = len(content.encode())

        write_record = {
            "path": path,
            "content_hash": content_hash,
            "size": content_size
        }
        tx.wal_entry["writes"].append(write_record)
        self._update_wal(tx.wal_entry)

        # Write to temp file
        tmp_path = f"{path}.tmp"
        os.makedirs(os.path.dirname(tmp_path), exist_ok=True)
        with open(tmp_path, 'w', encoding='utf-8') as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())

    def commit(self, tx: "Transaction") -> None:
        """
        Atomically commit all writes.

        Algorithm:
        1. For each .tmp file: atomic rename to actual path (atomic on POSIX)
        2. fsync parent directories
        3. Append operation to manifest.jsonl
        4. Mark WAL entry status="committed"
        5. Schedule WAL entry cleanup after grace period

        Atomicity guarantee:
        - rename() is atomic on POSIX filesystems
        - If crash after some renames but before manifest append:
          → WAL recovery will detect "in_progress" with some files renamed
          → Complete the remaining renames
        """
        # Phase 1: Rename all temp files to final paths
        for write in tx.wal_entry["writes"]:
            tmp_path = f"{write['path']}.tmp"
            final_path = write['path']

            if os.path.exists(tmp_path):
                os.rename(tmp_path, final_path)

        # Phase 2: fsync directories to ensure renames are durable
        synced_dirs = set()
        for write in tx.wal_entry["writes"]:
            parent_dir = os.path.dirname(write['path'])
            if parent_dir not in synced_dirs:
                self._fsync_dir(parent_dir)
                synced_dirs.add(parent_dir)

        # Phase 3: Append to manifest (the commit point)
        self._append_to_manifest(tx.manifest_entry)

        # Phase 4: Mark WAL entry as committed
        tx.wal_entry["status"] = "committed"
        tx.wal_entry["committed_at"] = datetime.utcnow().isoformat() + "Z"
        self._update_wal(tx.wal_entry)

        # Phase 5: Schedule cleanup (keep WAL for debugging)
        self._schedule_wal_cleanup(tx.op_id, delay_seconds=3600)

    def rollback(self, tx: "Transaction") -> None:
        """
        Discard all temp files, mark WAL entry as rolled back.

        Safe to call multiple times (idempotent).
        """
        for write in tx.wal_entry["writes"]:
            tmp_path = f"{write['path']}.tmp"
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

        tx.wal_entry["status"] = "rolled_back"
        tx.wal_entry["rolled_back_at"] = datetime.utcnow().isoformat() + "Z"
        self._update_wal(tx.wal_entry)

    def recover(self) -> RecoveryResult:
        """
        On startup, check for incomplete WAL entries and resolve.

        For each entry with status="in_progress":
        - If op_id exists in manifest.jsonl:
            → Transaction committed (crash after commit, before WAL update)
            → Clean up any remaining .tmp files
            → Mark WAL entry as "committed"
        - Else:
            → Transaction incomplete
            → Roll back (delete .tmp files)
            → Mark WAL entry as "rolled_back"

        Returns:
            RecoveryResult with counts of recovered/rolled_back transactions
        """
        result = RecoveryResult(recovered=0, rolled_back=0, errors=[])

        wal_entries = self._load_wal()
        manifest_ops = self._load_manifest_op_ids()

        for entry in wal_entries:
            if entry["status"] == "in_progress":
                if entry["op_id"] in manifest_ops:
                    # Transaction completed, WAL not updated (crash after commit)
                    self._cleanup_tmp_files(entry)
                    entry["status"] = "committed"
                    entry["recovered_at"] = datetime.utcnow().isoformat() + "Z"
                    self._update_wal(entry)
                    result.recovered += 1
                else:
                    # Transaction incomplete, roll back
                    self._rollback_from_wal(entry)
                    entry["status"] = "rolled_back"
                    entry["rolled_back_at"] = datetime.utcnow().isoformat() + "Z"
                    self._update_wal(entry)
                    result.rolled_back += 1

        return result

    def _fsync_dir(self, dir_path: str) -> None:
        """fsync a directory to ensure renames are durable."""
        fd = os.open(dir_path, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)

    def _append_to_wal(self, entry: dict) -> None:
        """Append entry to WAL file."""
        with open(self.wal_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry) + '\n')
            f.flush()
            os.fsync(f.fileno())

    def _update_wal(self, entry: dict) -> None:
        """Update existing WAL entry (rewrite entire file)."""
        entries = self._load_wal()
        for i, e in enumerate(entries):
            if e["op_id"] == entry["op_id"]:
                entries[i] = entry
                break

        # Write to temp, then atomic rename
        tmp_path = self.wal_path + ".tmp"
        with open(tmp_path, 'w', encoding='utf-8') as f:
            for e in entries:
                f.write(json.dumps(e) + '\n')
            f.flush()
            os.fsync(f.fileno())
        os.rename(tmp_path, self.wal_path)

    def _load_wal(self) -> List[dict]:
        """Load all WAL entries."""
        if not os.path.exists(self.wal_path):
            return []

        entries = []
        with open(self.wal_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    entries.append(json.loads(line))
        return entries

    def _append_to_manifest(self, entry: dict) -> None:
        """Append operation to manifest.jsonl."""
        manifest_path = os.path.join(os.path.dirname(self.wiki_path), "manifest.jsonl")
        with open(manifest_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry) + '\n')
            f.flush()
            os.fsync(f.fileno())


class Transaction:
    """
    Represents an in-progress write transaction.
    """

    def __init__(self, op_id: str, wal_entry: dict, wal: WriteAheadLog):
        self.op_id = op_id
        self.wal_entry = wal_entry
        self.wal = wal
        self.manifest_entry = None  # Set during COMPUTE stage
        self._committed = False
        self._rolled_back = False

    def write(self, path: str, content: str) -> None:
        """Record a write operation."""
        if self._committed or self._rolled_back:
            raise TransactionError("Transaction already finalized")
        self.wal.record_write(self, path, content)

    def set_manifest_entry(self, entry: dict) -> None:
        """Set the manifest entry for this operation."""
        self.manifest_entry = entry

    def commit(self) -> None:
        """Commit the transaction."""
        if self._committed:
            return  # Idempotent
        if self._rolled_back:
            raise TransactionError("Cannot commit rolled-back transaction")

        if not self.manifest_entry:
            raise TransactionError("Manifest entry not set")

        self.wal.commit(self)
        self._committed = True

    def rollback(self) -> None:
        """Rollback the transaction."""
        if self._rolled_back:
            return  # Idempotent
        if self._committed:
            raise TransactionError("Cannot rollback committed transaction")

        self.wal.rollback(self)
        self._rolled_back = True


@dataclass
class RecoveryResult:
    """Result of WAL recovery operation."""
    recovered: int      # Transactions that were completed but WAL not updated
    rolled_back: int    # Transactions that were incomplete and rolled back
    errors: List[str]   # Any errors encountered during recovery
```

### 5A.3 Alternative: Shadow Directory Commit

For very large wikis where WAL replay might be slow, shadow directory provides an alternative:

```python
class ShadowDirectoryCommit:
    """
    Write to shadow directory, then atomically swap.

    Best for:
    - Large wikis (> 1000 pages)
    - Operations touching many files
    - When copy-on-write filesystem is available (btrfs, ZFS)

    Directory structure:
      wiki/                       # Live data
      .wiki-shadow/{op_id}/       # Staging area for operation
      .wiki-old/{op_id}/          # Backup of replaced files
    """

    def __init__(self, wiki_path: str):
        self.wiki_path = wiki_path
        self.shadow_base = os.path.join(os.path.dirname(wiki_path), ".wiki-shadow")
        self.old_base = os.path.join(os.path.dirname(wiki_path), ".wiki-old")

    def begin_transaction(self, op_id: str) -> "ShadowTransaction":
        """
        Create shadow directory for this transaction.

        Does NOT copy entire wiki - only copies files as they are modified.
        """
        shadow_dir = os.path.join(self.shadow_base, op_id)
        old_dir = os.path.join(self.old_base, op_id)

        os.makedirs(shadow_dir, exist_ok=True)
        os.makedirs(old_dir, exist_ok=True)

        return ShadowTransaction(op_id, shadow_dir, old_dir, self)

    def stage_write(self, tx: "ShadowTransaction", rel_path: str, content: str) -> None:
        """
        Stage a write in shadow directory.

        If file exists in wiki/, copy original to .wiki-old/ first.
        """
        wiki_path = os.path.join(self.wiki_path, rel_path)
        shadow_path = os.path.join(tx.shadow_dir, rel_path)
        old_path = os.path.join(tx.old_dir, rel_path)

        # Backup original if exists
        if os.path.exists(wiki_path):
            os.makedirs(os.path.dirname(old_path), exist_ok=True)
            shutil.copy2(wiki_path, old_path)

        # Write new content to shadow
        os.makedirs(os.path.dirname(shadow_path), exist_ok=True)
        with open(shadow_path, 'w', encoding='utf-8') as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())

        tx.staged_files.append(rel_path)

    def commit(self, tx: "ShadowTransaction") -> None:
        """
        Commit by moving staged files into wiki/.

        Algorithm:
        1. For each staged file: rename from shadow to wiki (atomic)
        2. fsync directories
        3. Append to manifest
        4. Schedule cleanup of .wiki-old/ and .wiki-shadow/
        """
        for rel_path in tx.staged_files:
            shadow_path = os.path.join(tx.shadow_dir, rel_path)
            wiki_path = os.path.join(self.wiki_path, rel_path)

            os.makedirs(os.path.dirname(wiki_path), exist_ok=True)
            os.rename(shadow_path, wiki_path)

        # fsync directories
        self._fsync_modified_dirs(tx.staged_files)

        # Append to manifest
        self._append_to_manifest(tx.manifest_entry)

        # Cleanup
        shutil.rmtree(tx.shadow_dir, ignore_errors=True)
        # Keep .wiki-old/ for a grace period
        self._schedule_cleanup(tx.old_dir, delay_seconds=86400)

    def rollback(self, tx: "ShadowTransaction") -> None:
        """
        Rollback by discarding shadow directory.

        Original wiki/ is untouched.
        """
        shutil.rmtree(tx.shadow_dir, ignore_errors=True)
        shutil.rmtree(tx.old_dir, ignore_errors=True)

    def recover(self) -> RecoveryResult:
        """
        On startup, check for incomplete shadow transactions.

        - If manifest contains op_id: Transaction committed, clean up shadows
        - Else: Transaction incomplete, clean up shadows

        Either way, wiki/ is in consistent state.
        """
        result = RecoveryResult(recovered=0, rolled_back=0, errors=[])

        if not os.path.exists(self.shadow_base):
            return result

        manifest_ops = self._load_manifest_op_ids()

        for op_id in os.listdir(self.shadow_base):
            shadow_dir = os.path.join(self.shadow_base, op_id)
            old_dir = os.path.join(self.old_base, op_id)

            if op_id in manifest_ops:
                # Committed, just clean up
                shutil.rmtree(shadow_dir, ignore_errors=True)
                result.recovered += 1
            else:
                # Incomplete, clean up
                shutil.rmtree(shadow_dir, ignore_errors=True)
                shutil.rmtree(old_dir, ignore_errors=True)
                result.rolled_back += 1

        return result
```

**Choosing Between WAL and Shadow Directory:**

| Factor | WAL | Shadow Directory |
|--------|-----|------------------|
| Small operations (1-10 files) | Preferred | Overkill |
| Large operations (100+ files) | Slower recovery | Preferred |
| Copy-on-write FS (btrfs, ZFS) | No benefit | Near-instant copies |
| Disk space | Minimal overhead | 2x space during commit |
| Recovery complexity | Medium | Simple |

**Recommendation:** Use WAL by default. Switch to shadow directory for batch operations touching >50 files.

### 5A.4 Concurrency Control

#### Single-User Mode (Default)

Simple file-based locking prevents concurrent operations:

```python
class WikiLock:
    """
    File-based locking for single-user wikis.

    Lock file: .wiki-lock
    """

    def __init__(self, wiki_path: str):
        self.lock_path = os.path.join(wiki_path, ".wiki-lock")
        self.lock_fd = None

    def acquire(self, timeout_seconds: float = 30.0) -> bool:
        """
        Acquire exclusive lock on wiki.

        Returns True if lock acquired, False if timeout.
        Uses flock() for advisory locking.
        """
        import fcntl

        self.lock_fd = open(self.lock_path, 'w')
        start_time = time.time()

        while True:
            try:
                fcntl.flock(self.lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)

                # Write lock info
                lock_info = {
                    "pid": os.getpid(),
                    "acquired_at": datetime.utcnow().isoformat() + "Z",
                    "hostname": socket.gethostname()
                }
                self.lock_fd.write(json.dumps(lock_info))
                self.lock_fd.flush()

                return True

            except BlockingIOError:
                if time.time() - start_time > timeout_seconds:
                    self.lock_fd.close()
                    self.lock_fd = None
                    return False
                time.sleep(0.1)

    def release(self) -> None:
        """Release the lock."""
        import fcntl

        if self.lock_fd:
            fcntl.flock(self.lock_fd, fcntl.LOCK_UN)
            self.lock_fd.close()
            self.lock_fd = None

            # Remove lock file
            try:
                os.remove(self.lock_path)
            except FileNotFoundError:
                pass

    def __enter__(self):
        if not self.acquire():
            raise LockTimeoutError("Could not acquire wiki lock")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
        return False
```

#### Multi-User Mode (Future Extension)

For multi-user wikis with concurrent access, use page-level optimistic locking:

```python
class OptimisticLockManager:
    """
    Optimistic locking using revision IDs.

    No locks acquired upfront. Conflict detected at commit time
    by comparing expected revision with actual revision.
    """

    def check_and_update(
        self,
        page_id: str,
        expected_revision: int,
        new_content: str
    ) -> Union[UpdateSuccess, ConflictError]:
        """
        Attempt to update page with optimistic lock.

        Returns:
            UpdateSuccess if revision matched and update applied
            ConflictError if revision changed (concurrent modification)
        """
        current = self._load_page(page_id)

        if current.revision_id != expected_revision:
            return ConflictError(
                page_id=page_id,
                expected_revision=expected_revision,
                actual_revision=current.revision_id,
                conflict_content=current.content
            )

        # Safe to update
        new_revision = current.revision_id + 1
        self._write_page(page_id, new_content, new_revision)

        return UpdateSuccess(
            page_id=page_id,
            new_revision=new_revision
        )

    def resolve_conflict(
        self,
        page_id: str,
        base_revision: int,
        local_content: str,
        remote_content: str,
        strategy: ConflictStrategy
    ) -> ResolutionResult:
        """
        Resolve a conflict using specified strategy.

        Strategies:
        - THREE_WAY_MERGE: Attempt automatic merge if changes don't overlap
        - ACCEPT_REMOTE: Discard local changes, use remote version
        - ACCEPT_LOCAL: Overwrite remote with local (dangerous)
        - ESCALATE: Return both versions for manual resolution
        """
        if strategy == ConflictStrategy.THREE_WAY_MERGE:
            base_content = self._load_revision(page_id, base_revision)
            merged = self._three_way_merge(base_content, local_content, remote_content)

            if merged.has_conflicts:
                return ResolutionResult(
                    success=False,
                    strategy_used="three_way_merge",
                    conflict_markers=merged.conflict_regions
                )
            else:
                return ResolutionResult(
                    success=True,
                    strategy_used="three_way_merge",
                    merged_content=merged.content
                )

        elif strategy == ConflictStrategy.ACCEPT_REMOTE:
            return ResolutionResult(
                success=True,
                strategy_used="accept_remote",
                merged_content=remote_content
            )

        elif strategy == ConflictStrategy.ACCEPT_LOCAL:
            return ResolutionResult(
                success=True,
                strategy_used="accept_local",
                merged_content=local_content,
                warning="Remote changes discarded"
            )

        else:  # ESCALATE
            return ResolutionResult(
                success=False,
                strategy_used="escalate",
                base_content=self._load_revision(page_id, base_revision),
                local_content=local_content,
                remote_content=remote_content,
                message="Manual resolution required"
            )
```

### 5A.5 Derived Job Queue

Tier 2 updates (MIND_MAP, QMD index) run asynchronously via a job queue.

```python
@dataclass
class DerivedJob:
    """A job to update derived artifacts."""
    job_id: str
    job_type: str  # "mind_map_update" | "qmd_reindex" | "omega_capture"
    params: Dict[str, Any]
    status: str  # "pending" | "running" | "completed" | "failed"
    created_at: str
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    attempts: int = 0
    max_attempts: int = 3
    error: Optional[str] = None
    result: Optional[Dict] = None


class DerivedJobQueue:
    """
    Manage async jobs for Tier 2 updates.

    Jobs are stored in jobs.jsonl for persistence across restarts.
    Processing is single-threaded but non-blocking from user's perspective.
    """

    def __init__(self, wiki_path: str):
        self.wiki_path = wiki_path
        self.jobs_path = os.path.join(wiki_path, "jobs.jsonl")

    def enqueue(self, job_type: str, params: Dict[str, Any]) -> str:
        """
        Add job to queue.

        Returns job_id for tracking.
        """
        job = DerivedJob(
            job_id=f"job_{uuid.uuid4().hex[:12]}",
            job_type=job_type,
            params=params,
            status="pending",
            created_at=datetime.utcnow().isoformat() + "Z"
        )

        self._append_job(job)
        return job.job_id

    def enqueue_standard_jobs(self, op_id: str, affected_pages: List[str]) -> Dict[str, str]:
        """
        Enqueue standard derived jobs after a write operation.

        Returns dict of {job_type: job_id}
        """
        jobs = {}

        # Always update MIND_MAP
        jobs["mind_map_update"] = self.enqueue(
            "mind_map_update",
            {"op_id": op_id, "trigger": "write"}
        )

        # Always update index.md
        jobs["index_update"] = self.enqueue(
            "index_update",
            {"op_id": op_id}
        )

        # Reindex affected pages in QMD
        if affected_pages:
            jobs["qmd_reindex"] = self.enqueue(
                "qmd_reindex",
                {"page_ids": affected_pages}
            )

        return jobs

    def process_next(self) -> Optional[DerivedJob]:
        """
        Process next pending job.

        Returns processed job or None if queue empty.
        """
        job = self._get_next_pending()
        if not job:
            return None

        self._mark_running(job.job_id)

        try:
            result = self._execute_job(job)
            self._mark_completed(job.job_id, result)
            job.status = "completed"
            job.result = result

        except Exception as e:
            job.attempts += 1
            job.error = str(e)

            if job.attempts >= job.max_attempts:
                self._mark_failed(job.job_id, str(e))
                job.status = "failed"
            else:
                self._mark_pending(job.job_id)  # Retry later
                job.status = "pending"

        return job

    def process_all(self, max_jobs: int = 100) -> List[DerivedJob]:
        """Process all pending jobs up to max_jobs."""
        processed = []
        for _ in range(max_jobs):
            job = self.process_next()
            if job is None:
                break
            processed.append(job)
        return processed

    def status(self) -> Dict[str, int]:
        """Get queue statistics."""
        jobs = self._load_all_jobs()
        return {
            "pending": sum(1 for j in jobs if j.status == "pending"),
            "running": sum(1 for j in jobs if j.status == "running"),
            "completed": sum(1 for j in jobs if j.status == "completed"),
            "failed": sum(1 for j in jobs if j.status == "failed"),
            "total": len(jobs)
        }

    def retry_failed(self) -> int:
        """Reset all failed jobs to pending for retry."""
        jobs = self._load_all_jobs()
        count = 0
        for job in jobs:
            if job.status == "failed":
                job.status = "pending"
                job.attempts = 0
                job.error = None
                self._update_job(job)
                count += 1
        return count

    def _execute_job(self, job: DerivedJob) -> Dict:
        """Execute a job based on its type."""
        if job.job_type == "mind_map_update":
            return self._execute_mind_map_update(job.params)

        elif job.job_type == "index_update":
            return self._execute_index_update(job.params)

        elif job.job_type == "qmd_reindex":
            return self._execute_qmd_reindex(job.params)

        elif job.job_type == "omega_capture":
            return self._execute_omega_capture(job.params)

        else:
            raise ValueError(f"Unknown job type: {job.job_type}")

    def _execute_mind_map_update(self, params: Dict) -> Dict:
        """Regenerate MIND_MAP.md from wiki pages."""
        from .derived import compile_mind_map

        result = compile_mind_map(self.wiki_path)
        return {
            "nodes_generated": result.node_count,
            "duration_ms": result.duration_ms
        }

    def _execute_index_update(self, params: Dict) -> Dict:
        """Regenerate index.md from wiki pages."""
        from .derived import compile_index

        result = compile_index(self.wiki_path)
        return {
            "pages_indexed": result.page_count,
            "duration_ms": result.duration_ms
        }

    def _execute_qmd_reindex(self, params: Dict) -> Dict:
        """Update QMD search index for affected pages."""
        page_ids = params.get("page_ids", [])

        # Shell out to qmd CLI
        for page_id in page_ids:
            page_path = os.path.join(self.wiki_path, f"{page_id}.md")
            subprocess.run(
                ["qmd", "index", page_path],
                check=True,
                capture_output=True
            )

        return {
            "pages_reindexed": len(page_ids)
        }

    def _execute_omega_capture(self, params: Dict) -> Dict:
        """Capture insights to OMEGA (optional)."""
        # Integration with OMEGA
        from .omega import capture_operation_insights

        return capture_operation_insights(params)
```

### 5A.6 Complete Write Operation Flow

Putting it all together, here's how a write operation flows through the pipeline:

```python
def execute_write_operation(
    wiki: "Wiki",
    operation: WriteOperation
) -> WriteResult:
    """
    Execute a complete write operation through all pipeline stages.

    This is the main entry point for any wiki modification.
    """
    op_id = generate_op_id()

    # ═══════════════════════════════════════════════════════════════
    # STAGE 1: VALIDATE
    # ═══════════════════════════════════════════════════════════════
    validation = validate_operation(wiki, operation)
    if not validation.passed:
        return WriteResult(
            status="validation_failed",
            op_id=op_id,
            errors=validation.errors
        )

    # ═══════════════════════════════════════════════════════════════
    # STAGE 2: COMPUTE
    # ═══════════════════════════════════════════════════════════════
    try:
        write_plan = compute_write_plan(wiki, operation, op_id)
    except ComputeError as e:
        return WriteResult(
            status="compute_failed",
            op_id=op_id,
            errors=[str(e)]
        )

    # ═══════════════════════════════════════════════════════════════
    # STAGE 3: COMMIT (Transaction Boundary)
    # ═══════════════════════════════════════════════════════════════
    with wiki.lock:  # Acquire exclusive lock
        tx = wiki.wal.begin_transaction(op_id)

        try:
            # Write all pages
            for page_write in write_plan.pages:
                tx.write(page_write.path, page_write.content)

            # Archive old revisions
            for archive in write_plan.archives:
                archive_revision(wiki, archive.page_id, archive.revision)

            # Set manifest entry
            tx.set_manifest_entry(write_plan.manifest_entry)

            # Commit (atomic)
            tx.commit()

        except Exception as e:
            # Rollback on any failure
            tx.rollback()
            return WriteResult(
                status="commit_failed",
                op_id=op_id,
                errors=[str(e)]
            )

    # ═══════════════════════════════════════════════════════════════
    # STAGE 4: DERIVE (Async)
    # ═══════════════════════════════════════════════════════════════
    derived_jobs = wiki.job_queue.enqueue_standard_jobs(
        op_id=op_id,
        affected_pages=write_plan.affected_page_ids
    )

    # Optionally process jobs immediately (or let background worker handle)
    if wiki.config.get("sync_derived", False):
        wiki.job_queue.process_all()

    # ═══════════════════════════════════════════════════════════════
    # STAGE 5: VERIFY
    # ═══════════════════════════════════════════════════════════════
    verification = verify_write(wiki, write_plan)

    if not verification.passed:
        # Mark operation as needing repair, but don't fail it
        # (data is already committed)
        wiki.manifest.update_status(op_id, "needs_repair", verification.issues)

    return WriteResult(
        status="completed",
        op_id=op_id,
        created_pages=write_plan.created_pages,
        updated_pages=write_plan.updated_pages,
        derived_jobs=derived_jobs,
        verification=verification
    )
```

### 5A.7 Pipeline Test Scenarios

```python
def test_crash_during_commit_wal_recovery():
    """
    Test: Process killed mid-write recovers correctly via WAL.

    Scenario:
    1. Begin transaction, write 3 files
    2. Crash after 2nd file committed but before manifest append
    3. On restart, WAL recovery completes or rolls back
    4. Wiki is in consistent state (never partial)
    """
    wiki = create_test_wiki()

    # Inject crash after 2nd file rename but before manifest
    with inject_crash_at("manifest_append"):
        try:
            ingest_source(wiki, "test_paper.pdf")
        except CrashInjected:
            pass

    # Restart wiki, run recovery
    wiki_recovered = Wiki(wiki.path)
    recovery_result = wiki_recovered.wal.recover()

    # Either fully committed (all files present, manifest entry exists)
    # or fully rolled back (no temp files, no partial state)
    invariants = check_all_invariants(wiki_recovered)
    assert invariants == [], f"Invariant violations: {invariants}"

    # No .tmp files remaining
    tmp_files = glob.glob(f"{wiki.path}/**/*.tmp", recursive=True)
    assert tmp_files == []


def test_derived_job_failure_doesnt_affect_canonical():
    """
    Test: If MIND_MAP generation fails, canonical data is still committed.
    """
    wiki = create_test_wiki()

    with mock_mind_map_generation_failure():
        result = ingest_source(wiki, "test_paper.pdf")

        # Canonical write succeeded
        assert result.status == "completed"
        assert page_exists(wiki, "sources/test_paper")

        # Derived job queued but failed
        job_status = wiki.job_queue.status()
        assert job_status["failed"] > 0 or job_status["pending"] > 0

        # MIND_MAP may be stale, but wiki is functional
        assert wiki.can_query("test paper")  # Falls back to grep


def test_concurrent_write_blocked_by_lock():
    """
    Test: Second write operation waits for lock, doesn't corrupt data.
    """
    wiki = create_test_wiki()

    results = []

    def write_paper_1():
        result = ingest_source(wiki, "paper1.pdf")
        results.append(("paper1", result))

    def write_paper_2():
        result = ingest_source(wiki, "paper2.pdf")
        results.append(("paper2", result))

    # Run concurrently
    t1 = threading.Thread(target=write_paper_1)
    t2 = threading.Thread(target=write_paper_2)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # Both should succeed (one waits for the other)
    assert len(results) == 2
    assert all(r[1].status == "completed" for r in results)

    # Both pages exist with correct revisions
    assert page_exists(wiki, "sources/paper1")
    assert page_exists(wiki, "sources/paper2")

    # Revision IDs are sequential (no gaps from conflicts)
    p1 = load_page(wiki, "sources/paper1")
    p2 = load_page(wiki, "sources/paper2")
    assert p1.revision_id == 1
    assert p2.revision_id == 1


def test_optimistic_lock_conflict_detection():
    """
    Test: Concurrent updates to same page detected via revision mismatch.
    """
    wiki = create_test_wiki()

    # Create initial page
    create_page(wiki, "concepts/ml", "Initial content", revision=1)

    # Simulate two concurrent reads
    base_revision = 1

    # First update succeeds
    result1 = update_page(
        wiki,
        "concepts/ml",
        "Updated by user 1",
        expected_revision=base_revision
    )
    assert result1.status == "completed"
    assert result1.new_revision == 2

    # Second update (from stale read) detects conflict
    result2 = update_page(
        wiki,
        "concepts/ml",
        "Updated by user 2",
        expected_revision=base_revision  # Stale!
    )
    assert result2.status == "conflict"
    assert result2.expected_revision == 1
    assert result2.actual_revision == 2


def test_job_queue_retry_on_transient_failure():
    """
    Test: Failed jobs retry up to max_attempts.
    """
    wiki = create_test_wiki()

    # Enqueue job that will fail twice then succeed
    failure_count = [0]

    def flaky_job(*args):
        failure_count[0] += 1
        if failure_count[0] < 3:
            raise RuntimeError("Transient failure")
        return {"success": True}

    with mock_job_executor("mind_map_update", flaky_job):
        job_id = wiki.job_queue.enqueue("mind_map_update", {})

        # Process until success or max attempts
        for _ in range(5):
            wiki.job_queue.process_next()

        job = wiki.job_queue.get_job(job_id)

        # Should have succeeded on 3rd attempt
        assert job.status == "completed"
        assert job.attempts == 3
```

---

## 5B. Observability & Telemetry

Production wikis need telemetry, logging, and health monitoring to debug issues, prevent failures, and understand system behavior. This section defines the observability infrastructure.

### 5B.1 Observability Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          OBSERVABILITY LAYERS                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐     │
│  │   LOGGING   │   │   METRICS   │   │   TRACING   │   │   HEALTH    │     │
│  │             │   │             │   │             │   │             │     │
│  │ Structured  │   │ Counters    │   │ Trace IDs   │   │ Liveness    │     │
│  │ JSON logs   │   │ Gauges      │   │ Span trees  │   │ Readiness   │     │
│  │ Log levels  │   │ Histograms  │   │ Timing      │   │ Deep checks │     │
│  └──────┬──────┘   └──────┬──────┘   └──────┬──────┘   └──────┬──────┘     │
│         │                 │                 │                 │             │
│         └────────────┬────┴────────┬────────┴────────┬────────┘             │
│                      │             │                 │                       │
│                      ▼             ▼                 ▼                       │
│              ┌─────────────────────────────────────────────┐                │
│              │           STORAGE & ANALYSIS                │                │
│              │                                              │                │
│              │  logs/wiki.jsonl     # Structured logs      │                │
│              │  logs/metrics.jsonl  # Time-series metrics  │                │
│              │  logs/traces.jsonl   # Distributed traces   │                │
│              │  health_report.md    # Health dashboard     │                │
│              └─────────────────────────────────────────────┘                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Storage Location:** All observability data is stored in `logs/` directory (Tier 3 - ephemeral).

| File | Purpose | Retention |
|------|---------|-----------|
| `logs/wiki.jsonl` | Structured operation logs | 30 days |
| `logs/metrics.jsonl` | Time-series metrics | 7 days |
| `logs/traces.jsonl` | Distributed traces | 7 days |
| `logs/errors.jsonl` | Error-only log (filtered) | 90 days |

### 5B.2 Structured Logging

Every operation produces structured JSON logs that can be queried and analyzed.

```python
import json
import os
import traceback
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union
import threading
import uuid


class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


class EventType(Enum):
    # Operation lifecycle
    OPERATION_START = "operation_start"
    OPERATION_COMPLETE = "operation_complete"
    OPERATION_FAILED = "operation_failed"

    # Pipeline stages
    STAGE_ENTER = "stage_enter"
    STAGE_EXIT = "stage_exit"
    STAGE_FAILED = "stage_failed"

    # Data operations
    PAGE_CREATE = "page_create"
    PAGE_UPDATE = "page_update"
    PAGE_DELETE = "page_delete"
    PAGE_ROLLBACK = "page_rollback"

    # Derived operations
    JOB_ENQUEUE = "job_enqueue"
    JOB_START = "job_start"
    JOB_COMPLETE = "job_complete"
    JOB_FAILED = "job_failed"

    # System events
    WAL_RECOVERY = "wal_recovery"
    LOCK_ACQUIRE = "lock_acquire"
    LOCK_RELEASE = "lock_release"
    LOCK_TIMEOUT = "lock_timeout"

    # Errors and warnings
    ERROR = "error"
    WARNING = "warning"
    INVARIANT_VIOLATION = "invariant_violation"

    # Metrics
    METRIC = "metric"


@dataclass
class LogEntry:
    """A single structured log entry."""
    timestamp: str
    level: str
    event: str
    message: str
    op_id: Optional[str] = None
    trace_id: Optional[str] = None
    span_id: Optional[str] = None
    parent_span_id: Optional[str] = None
    stage: Optional[str] = None
    duration_ms: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = None
    error: Optional[Dict[str, Any]] = None

    def to_json(self) -> str:
        """Serialize to JSON, omitting None values."""
        data = {k: v for k, v in asdict(self).items() if v is not None}
        return json.dumps(data, default=str)


class WikiLogger:
    """
    Structured logging for all wiki operations.

    Features:
    - JSON Lines format for machine parsing
    - Trace IDs for request correlation
    - Stage-aware logging for pipeline visibility
    - Automatic rotation and retention
    - Thread-safe writes
    """

    def __init__(self, wiki_path: str):
        self.wiki_path = wiki_path
        self.logs_dir = os.path.join(wiki_path, "logs")
        self.log_file = os.path.join(self.logs_dir, "wiki.jsonl")
        self.error_file = os.path.join(self.logs_dir, "errors.jsonl")
        self._lock = threading.Lock()

        os.makedirs(self.logs_dir, exist_ok=True)

    def _write(self, entry: LogEntry, also_errors: bool = False) -> None:
        """Write log entry atomically."""
        line = entry.to_json() + "\n"

        with self._lock:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(line)

            if also_errors:
                with open(self.error_file, 'a', encoding='utf-8') as f:
                    f.write(line)

    def _now(self) -> str:
        """Current timestamp in ISO format with milliseconds."""
        return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    # ════════════════════════════════════════════════════════════════
    # OPERATION LIFECYCLE LOGGING
    # ════════════════════════════════════════════════════════════════

    def log_operation_start(
        self,
        op_id: str,
        op_type: str,
        actor: str,
        inputs: Dict[str, Any],
        trace_id: Optional[str] = None
    ) -> str:
        """
        Log operation initiation. Returns trace_id for correlation.

        Example output:
        {
          "timestamp": "2024-01-15T14:30:00.123Z",
          "level": "INFO",
          "event": "operation_start",
          "op_id": "op_123",
          "trace_id": "trace_456",
          "message": "Starting ingest operation",
          "metadata": {
            "op_type": "ingest",
            "actor": "llm",
            "inputs": {"source_path": "raw/paper.pdf"}
          }
        }
        """
        trace_id = trace_id or f"trace_{uuid.uuid4().hex[:12]}"

        entry = LogEntry(
            timestamp=self._now(),
            level=LogLevel.INFO.value,
            event=EventType.OPERATION_START.value,
            message=f"Starting {op_type} operation",
            op_id=op_id,
            trace_id=trace_id,
            metadata={
                "op_type": op_type,
                "actor": actor,
                "inputs": inputs
            }
        )
        self._write(entry)
        return trace_id

    def log_operation_complete(
        self,
        op_id: str,
        trace_id: str,
        duration_ms: int,
        outputs: Dict[str, Any]
    ) -> None:
        """Log successful operation completion."""
        entry = LogEntry(
            timestamp=self._now(),
            level=LogLevel.INFO.value,
            event=EventType.OPERATION_COMPLETE.value,
            message=f"Operation completed successfully",
            op_id=op_id,
            trace_id=trace_id,
            duration_ms=duration_ms,
            metadata={"outputs": outputs}
        )
        self._write(entry)

    def log_operation_failed(
        self,
        op_id: str,
        trace_id: str,
        duration_ms: int,
        error_type: str,
        error_message: str,
        stage: str
    ) -> None:
        """Log operation failure."""
        entry = LogEntry(
            timestamp=self._now(),
            level=LogLevel.ERROR.value,
            event=EventType.OPERATION_FAILED.value,
            message=f"Operation failed at stage {stage}",
            op_id=op_id,
            trace_id=trace_id,
            duration_ms=duration_ms,
            stage=stage,
            error={
                "type": error_type,
                "message": error_message
            }
        )
        self._write(entry, also_errors=True)

    # ════════════════════════════════════════════════════════════════
    # PIPELINE STAGE LOGGING
    # ════════════════════════════════════════════════════════════════

    def log_stage_enter(
        self,
        op_id: str,
        trace_id: str,
        stage: str,
        span_id: Optional[str] = None,
        parent_span_id: Optional[str] = None
    ) -> str:
        """
        Log entering a pipeline stage. Returns span_id.

        Stages: validate, compute, commit, derive, verify
        """
        span_id = span_id or f"span_{uuid.uuid4().hex[:8]}"

        entry = LogEntry(
            timestamp=self._now(),
            level=LogLevel.DEBUG.value,
            event=EventType.STAGE_ENTER.value,
            message=f"Entering stage: {stage}",
            op_id=op_id,
            trace_id=trace_id,
            span_id=span_id,
            parent_span_id=parent_span_id,
            stage=stage
        )
        self._write(entry)
        return span_id

    def log_stage_exit(
        self,
        op_id: str,
        trace_id: str,
        stage: str,
        span_id: str,
        duration_ms: int,
        result: str,  # "success" | "skip" | "partial"
        metadata: Optional[Dict] = None
    ) -> None:
        """Log exiting a pipeline stage."""
        entry = LogEntry(
            timestamp=self._now(),
            level=LogLevel.DEBUG.value,
            event=EventType.STAGE_EXIT.value,
            message=f"Exiting stage: {stage} ({result})",
            op_id=op_id,
            trace_id=trace_id,
            span_id=span_id,
            stage=stage,
            duration_ms=duration_ms,
            metadata={"result": result, **(metadata or {})}
        )
        self._write(entry)

    def log_stage_failed(
        self,
        op_id: str,
        trace_id: str,
        stage: str,
        span_id: str,
        duration_ms: int,
        error_type: str,
        error_message: str,
        stack_trace: Optional[str] = None
    ) -> None:
        """Log stage failure with full error context."""
        entry = LogEntry(
            timestamp=self._now(),
            level=LogLevel.ERROR.value,
            event=EventType.STAGE_FAILED.value,
            message=f"Stage failed: {stage}",
            op_id=op_id,
            trace_id=trace_id,
            span_id=span_id,
            stage=stage,
            duration_ms=duration_ms,
            error={
                "type": error_type,
                "message": error_message,
                "stack_trace": stack_trace
            }
        )
        self._write(entry, also_errors=True)

    # ════════════════════════════════════════════════════════════════
    # DATA OPERATION LOGGING
    # ════════════════════════════════════════════════════════════════

    def log_page_write(
        self,
        op_id: str,
        trace_id: str,
        page_id: str,
        action: str,  # "create" | "update" | "delete" | "rollback"
        revision_id: int,
        previous_revision: Optional[int] = None,
        size_bytes: Optional[int] = None
    ) -> None:
        """Log page modification."""
        event_map = {
            "create": EventType.PAGE_CREATE,
            "update": EventType.PAGE_UPDATE,
            "delete": EventType.PAGE_DELETE,
            "rollback": EventType.PAGE_ROLLBACK
        }

        entry = LogEntry(
            timestamp=self._now(),
            level=LogLevel.INFO.value,
            event=event_map[action].value,
            message=f"Page {action}: {page_id} (rev {revision_id})",
            op_id=op_id,
            trace_id=trace_id,
            metadata={
                "page_id": page_id,
                "action": action,
                "revision_id": revision_id,
                "previous_revision": previous_revision,
                "size_bytes": size_bytes
            }
        )
        self._write(entry)

    # ════════════════════════════════════════════════════════════════
    # ERROR LOGGING
    # ════════════════════════════════════════════════════════════════

    def log_error(
        self,
        op_id: Optional[str],
        trace_id: Optional[str],
        error_type: str,
        error_message: str,
        stage: Optional[str] = None,
        recoverable: bool = True,
        context: Optional[Dict] = None
    ) -> None:
        """
        Log error with full context for debugging.

        error_type values:
        - "validation_error": Input validation failed
        - "llm_error": LLM API call failed
        - "filesystem_error": File I/O failed
        - "conflict": Concurrent modification conflict
        - "timeout": Operation timed out
        - "invariant_violation": Post-commit check failed
        - "qmd_error": Search index error
        - "omega_error": Session memory error
        """
        entry = LogEntry(
            timestamp=self._now(),
            level=LogLevel.ERROR.value,
            event=EventType.ERROR.value,
            message=error_message,
            op_id=op_id,
            trace_id=trace_id,
            stage=stage,
            error={
                "type": error_type,
                "message": error_message,
                "recoverable": recoverable,
                "stack_trace": traceback.format_exc()
            },
            metadata=context
        )
        self._write(entry, also_errors=True)

    def log_warning(
        self,
        message: str,
        op_id: Optional[str] = None,
        trace_id: Optional[str] = None,
        context: Optional[Dict] = None
    ) -> None:
        """Log warning (non-fatal issue)."""
        entry = LogEntry(
            timestamp=self._now(),
            level=LogLevel.WARN.value,
            event=EventType.WARNING.value,
            message=message,
            op_id=op_id,
            trace_id=trace_id,
            metadata=context
        )
        self._write(entry)

    # ════════════════════════════════════════════════════════════════
    # INVARIANT CHECKING
    # ════════════════════════════════════════════════════════════════

    def log_invariant_check(
        self,
        op_id: str,
        trace_id: str,
        invariant_id: str,
        passed: bool,
        check_duration_ms: int,
        violation_details: Optional[str] = None
    ) -> None:
        """
        Log invariant verification result.

        invariant_id examples:
        - "INV-1": Pages have valid frontmatter
        - "INV-2": revision_hash matches content
        - "INV-5": Wikilinks resolve
        """
        level = LogLevel.DEBUG if passed else LogLevel.WARN

        entry = LogEntry(
            timestamp=self._now(),
            level=level.value,
            event=EventType.INVARIANT_VIOLATION.value if not passed else "invariant_check",
            message=f"Invariant {invariant_id}: {'PASS' if passed else 'FAIL'}",
            op_id=op_id,
            trace_id=trace_id,
            duration_ms=check_duration_ms,
            metadata={
                "invariant_id": invariant_id,
                "passed": passed,
                "violation_details": violation_details
            }
        )
        self._write(entry, also_errors=not passed)

    # ════════════════════════════════════════════════════════════════
    # JOB QUEUE LOGGING
    # ════════════════════════════════════════════════════════════════

    def log_job_enqueue(
        self,
        job_id: str,
        job_type: str,
        triggering_op_id: str,
        params: Dict
    ) -> None:
        """Log derived job enqueued."""
        entry = LogEntry(
            timestamp=self._now(),
            level=LogLevel.DEBUG.value,
            event=EventType.JOB_ENQUEUE.value,
            message=f"Job enqueued: {job_type}",
            op_id=triggering_op_id,
            metadata={
                "job_id": job_id,
                "job_type": job_type,
                "params": params
            }
        )
        self._write(entry)

    def log_job_complete(
        self,
        job_id: str,
        job_type: str,
        duration_ms: int,
        result: Dict
    ) -> None:
        """Log derived job completed."""
        entry = LogEntry(
            timestamp=self._now(),
            level=LogLevel.INFO.value,
            event=EventType.JOB_COMPLETE.value,
            message=f"Job completed: {job_type}",
            duration_ms=duration_ms,
            metadata={
                "job_id": job_id,
                "job_type": job_type,
                "result": result
            }
        )
        self._write(entry)

    def log_job_failed(
        self,
        job_id: str,
        job_type: str,
        attempt: int,
        max_attempts: int,
        error_message: str
    ) -> None:
        """Log derived job failure."""
        entry = LogEntry(
            timestamp=self._now(),
            level=LogLevel.ERROR.value,
            event=EventType.JOB_FAILED.value,
            message=f"Job failed: {job_type} (attempt {attempt}/{max_attempts})",
            metadata={
                "job_id": job_id,
                "job_type": job_type,
                "attempt": attempt,
                "max_attempts": max_attempts
            },
            error={
                "message": error_message
            }
        )
        self._write(entry, also_errors=True)
```

### 5B.3 Metrics Collection

Track quantitative measurements for performance analysis and alerting.

```python
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from collections import defaultdict
import time


@dataclass
class MetricPoint:
    """A single metric measurement."""
    timestamp: str
    name: str
    value: float
    unit: str
    tags: Dict[str, str]
    metric_type: str  # "counter" | "gauge" | "histogram"


class MetricsCollector:
    """
    Collects and aggregates wiki metrics.

    Metric types:
    - Counter: Monotonically increasing (e.g., total_operations)
    - Gauge: Point-in-time value (e.g., index_size_mb)
    - Histogram: Distribution of values (e.g., latency percentiles)
    """

    def __init__(self, wiki_path: str):
        self.wiki_path = wiki_path
        self.metrics_file = os.path.join(wiki_path, "logs", "metrics.jsonl")
        self._counters: Dict[str, float] = defaultdict(float)
        self._gauges: Dict[str, float] = {}
        self._histograms: Dict[str, List[float]] = defaultdict(list)
        self._lock = threading.Lock()

    def _write_metric(self, point: MetricPoint) -> None:
        """Persist metric point."""
        with self._lock:
            with open(self.metrics_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(asdict(point), default=str) + '\n')

    def _now(self) -> str:
        return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    # ════════════════════════════════════════════════════════════════
    # COUNTER METRICS (Monotonically increasing)
    # ════════════════════════════════════════════════════════════════

    def increment(
        self,
        name: str,
        value: float = 1.0,
        tags: Optional[Dict[str, str]] = None
    ) -> None:
        """
        Increment a counter metric.

        Examples:
        - increment("operations_total", tags={"op_type": "ingest"})
        - increment("pages_created")
        - increment("errors_total", tags={"error_type": "validation"})
        """
        key = self._metric_key(name, tags)
        with self._lock:
            self._counters[key] += value

        point = MetricPoint(
            timestamp=self._now(),
            name=name,
            value=self._counters[key],
            unit="count",
            tags=tags or {},
            metric_type="counter"
        )
        self._write_metric(point)

    # ════════════════════════════════════════════════════════════════
    # GAUGE METRICS (Point-in-time values)
    # ════════════════════════════════════════════════════════════════

    def gauge(
        self,
        name: str,
        value: float,
        unit: str,
        tags: Optional[Dict[str, str]] = None
    ) -> None:
        """
        Set a gauge metric.

        Examples:
        - gauge("wiki_pages_total", 150, "pages")
        - gauge("index_size", 45.2, "megabytes")
        - gauge("job_queue_depth", 3, "jobs")
        - gauge("memory_usage", 512, "megabytes")
        """
        key = self._metric_key(name, tags)
        with self._lock:
            self._gauges[key] = value

        point = MetricPoint(
            timestamp=self._now(),
            name=name,
            value=value,
            unit=unit,
            tags=tags or {},
            metric_type="gauge"
        )
        self._write_metric(point)

    # ════════════════════════════════════════════════════════════════
    # HISTOGRAM METRICS (Distributions)
    # ════════════════════════════════════════════════════════════════

    def observe(
        self,
        name: str,
        value: float,
        unit: str,
        tags: Optional[Dict[str, str]] = None
    ) -> None:
        """
        Record a histogram observation.

        Examples:
        - observe("operation_duration", 1234, "milliseconds", {"op_type": "ingest"})
        - observe("llm_tokens", 5000, "tokens")
        - observe("page_size", 4500, "bytes")
        """
        key = self._metric_key(name, tags)
        with self._lock:
            self._histograms[key].append(value)

        point = MetricPoint(
            timestamp=self._now(),
            name=name,
            value=value,
            unit=unit,
            tags=tags or {},
            metric_type="histogram"
        )
        self._write_metric(point)

    def get_histogram_stats(
        self,
        name: str,
        tags: Optional[Dict[str, str]] = None
    ) -> Dict[str, float]:
        """Get histogram statistics (p50, p90, p99, min, max, mean)."""
        key = self._metric_key(name, tags)
        values = self._histograms.get(key, [])

        if not values:
            return {}

        sorted_vals = sorted(values)
        n = len(sorted_vals)

        return {
            "count": n,
            "min": sorted_vals[0],
            "max": sorted_vals[-1],
            "mean": sum(sorted_vals) / n,
            "p50": sorted_vals[int(n * 0.50)],
            "p90": sorted_vals[int(n * 0.90)],
            "p99": sorted_vals[min(int(n * 0.99), n - 1)]
        }

    def _metric_key(self, name: str, tags: Optional[Dict[str, str]]) -> str:
        """Create unique key for metric + tags combination."""
        if not tags:
            return name
        tag_str = ",".join(f"{k}={v}" for k, v in sorted(tags.items()))
        return f"{name}{{{tag_str}}}"

    # ════════════════════════════════════════════════════════════════
    # TIMING CONTEXT MANAGER
    # ════════════════════════════════════════════════════════════════

    def timer(
        self,
        name: str,
        tags: Optional[Dict[str, str]] = None
    ) -> "TimerContext":
        """
        Context manager for timing code blocks.

        Usage:
            with metrics.timer("ingest_duration", {"source_type": "pdf"}):
                process_source(...)
        """
        return TimerContext(self, name, tags)


class TimerContext:
    """Context manager for automatic timing."""

    def __init__(
        self,
        collector: MetricsCollector,
        name: str,
        tags: Optional[Dict[str, str]]
    ):
        self.collector = collector
        self.name = name
        self.tags = tags
        self.start_time: float = 0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration_ms = (time.perf_counter() - self.start_time) * 1000
        self.collector.observe(
            self.name,
            duration_ms,
            "milliseconds",
            self.tags
        )
        return False


# ════════════════════════════════════════════════════════════════════
# STANDARD WIKI METRICS
# ════════════════════════════════════════════════════════════════════

STANDARD_METRICS = """
# Counters (total counts)
operations_total{op_type}          # Total operations by type
pages_created_total                # Total pages created
pages_updated_total                # Total page updates
pages_deleted_total                # Total pages deleted
errors_total{error_type,stage}     # Errors by type and stage
jobs_completed_total{job_type}     # Completed derived jobs
jobs_failed_total{job_type}        # Failed derived jobs
wal_recoveries_total               # WAL recovery events
conflicts_total                    # Write conflicts detected

# Gauges (current state)
wiki_pages_total                   # Current page count
wiki_size_bytes                    # Total wiki size
index_size_bytes                   # QMD index size
job_queue_depth                    # Pending jobs
active_operations                  # In-flight operations
stale_derived_artifacts            # Number of stale Tier 2 items

# Histograms (distributions)
operation_duration_ms{op_type}     # Operation latency
stage_duration_ms{stage}           # Per-stage latency
page_write_duration_ms             # File write latency
llm_call_duration_ms               # LLM API latency
llm_tokens_used{model}             # Token usage
page_size_bytes                    # Page sizes
job_duration_ms{job_type}          # Derived job latency
"""
```

### 5B.4 Distributed Tracing

Track request flow through all pipeline stages with trace context.

```python
@dataclass
class Span:
    """
    A single span in a distributed trace.

    Represents one logical unit of work (e.g., one pipeline stage).
    """
    trace_id: str           # Shared across all spans in a trace
    span_id: str            # Unique to this span
    parent_span_id: Optional[str]  # Parent span (None for root)
    operation_name: str     # e.g., "ingest.validate", "ingest.commit"
    start_time: str
    end_time: Optional[str] = None
    duration_ms: Optional[int] = None
    status: str = "in_progress"  # "in_progress" | "success" | "error"
    tags: Dict[str, str] = field(default_factory=dict)
    logs: List[Dict] = field(default_factory=list)
    error: Optional[Dict] = None


class Tracer:
    """
    Distributed tracing for wiki operations.

    Creates hierarchical span trees showing request flow:

    trace_123
    └── ingest (root span)
        ├── validate
        ├── compute
        │   ├── extract_entities
        │   ├── extract_concepts
        │   └── generate_pages
        ├── commit
        │   ├── wal_write
        │   └── manifest_append
        ├── derive
        │   ├── enqueue_mind_map
        │   └── enqueue_qmd
        └── verify
    """

    def __init__(self, wiki_path: str):
        self.wiki_path = wiki_path
        self.traces_file = os.path.join(wiki_path, "logs", "traces.jsonl")
        self._active_spans: Dict[str, Span] = {}
        self._lock = threading.Lock()

    def start_trace(self, operation_name: str) -> Span:
        """
        Start a new trace (root span).

        Returns root span. All child spans share the same trace_id.
        """
        trace_id = f"trace_{uuid.uuid4().hex[:12]}"
        span_id = f"span_{uuid.uuid4().hex[:8]}"

        span = Span(
            trace_id=trace_id,
            span_id=span_id,
            parent_span_id=None,
            operation_name=operation_name,
            start_time=self._now()
        )

        with self._lock:
            self._active_spans[span_id] = span

        return span

    def start_span(
        self,
        operation_name: str,
        parent: Span,
        tags: Optional[Dict[str, str]] = None
    ) -> Span:
        """Start a child span under the given parent."""
        span_id = f"span_{uuid.uuid4().hex[:8]}"

        span = Span(
            trace_id=parent.trace_id,
            span_id=span_id,
            parent_span_id=parent.span_id,
            operation_name=operation_name,
            start_time=self._now(),
            tags=tags or {}
        )

        with self._lock:
            self._active_spans[span_id] = span

        return span

    def end_span(
        self,
        span: Span,
        status: str = "success",
        error: Optional[Dict] = None
    ) -> None:
        """
        End a span and persist it.

        status: "success" | "error"
        """
        span.end_time = self._now()
        span.status = status
        span.error = error

        # Calculate duration
        start = datetime.fromisoformat(span.start_time.replace('Z', '+00:00'))
        end = datetime.fromisoformat(span.end_time.replace('Z', '+00:00'))
        span.duration_ms = int((end - start).total_seconds() * 1000)

        # Persist
        self._write_span(span)

        # Remove from active spans
        with self._lock:
            self._active_spans.pop(span.span_id, None)

    def add_span_log(self, span: Span, message: str, data: Optional[Dict] = None) -> None:
        """Add a log entry to a span."""
        span.logs.append({
            "timestamp": self._now(),
            "message": message,
            "data": data
        })

    def add_span_tag(self, span: Span, key: str, value: str) -> None:
        """Add a tag to a span."""
        span.tags[key] = value

    def _write_span(self, span: Span) -> None:
        """Persist span to trace file."""
        with self._lock:
            with open(self.traces_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(asdict(span), default=str) + '\n')

    def _now(self) -> str:
        return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    # ════════════════════════════════════════════════════════════════
    # CONTEXT MANAGER FOR AUTO-TRACING
    # ════════════════════════════════════════════════════════════════

    def span_context(
        self,
        operation_name: str,
        parent: Optional[Span] = None,
        tags: Optional[Dict[str, str]] = None
    ) -> "SpanContext":
        """
        Context manager for automatic span lifecycle.

        Usage:
            with tracer.span_context("validate", parent=root_span) as span:
                # Do validation
                tracer.add_span_tag(span, "pages_validated", "5")
        """
        return SpanContext(self, operation_name, parent, tags)


class SpanContext:
    """Context manager for automatic span lifecycle."""

    def __init__(
        self,
        tracer: Tracer,
        operation_name: str,
        parent: Optional[Span],
        tags: Optional[Dict[str, str]]
    ):
        self.tracer = tracer
        self.operation_name = operation_name
        self.parent = parent
        self.tags = tags
        self.span: Optional[Span] = None

    def __enter__(self) -> Span:
        if self.parent:
            self.span = self.tracer.start_span(
                self.operation_name,
                self.parent,
                self.tags
            )
        else:
            self.span = self.tracer.start_trace(self.operation_name)
        return self.span

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.tracer.end_span(
                self.span,
                status="error",
                error={
                    "type": exc_type.__name__,
                    "message": str(exc_val)
                }
            )
        else:
            self.tracer.end_span(self.span, status="success")
        return False
```

### 5B.5 Health Monitoring

System health checks and dashboard generation.

```python
@dataclass
class HealthCheck:
    """Result of a single health check."""
    name: str
    status: str  # "healthy" | "degraded" | "unhealthy"
    message: str
    duration_ms: int
    details: Optional[Dict] = None


@dataclass
class HealthReport:
    """Complete health report for the wiki."""
    timestamp: str
    overall_status: str  # "healthy" | "degraded" | "unhealthy"
    checks: List[HealthCheck]
    summary: Dict[str, int]  # {"healthy": N, "degraded": N, "unhealthy": N}


class HealthMonitor:
    """
    Health monitoring for wiki system.

    Checks:
    - Tier 1: Canonical data integrity
    - Tier 2: Derived artifacts freshness
    - Tier 3: Ephemeral systems availability
    - Infrastructure: Disk, memory, external services
    """

    def __init__(self, wiki_path: str):
        self.wiki_path = wiki_path
        self.checks: List[Callable] = [
            self._check_wiki_directory,
            self._check_manifest_integrity,
            self._check_page_frontmatter,
            self._check_revision_hashes,
            self._check_wikilinks,
            self._check_mind_map_freshness,
            self._check_index_freshness,
            self._check_qmd_status,
            self._check_omega_status,
            self._check_disk_space,
            self._check_job_queue,
            self._check_wal_pending,
        ]

    def run_all_checks(self) -> HealthReport:
        """Run all health checks and generate report."""
        results = []
        for check_fn in self.checks:
            start = time.perf_counter()
            try:
                result = check_fn()
            except Exception as e:
                result = HealthCheck(
                    name=check_fn.__name__,
                    status="unhealthy",
                    message=f"Check failed: {str(e)}",
                    duration_ms=int((time.perf_counter() - start) * 1000)
                )
            results.append(result)

        # Calculate summary
        summary = {"healthy": 0, "degraded": 0, "unhealthy": 0}
        for r in results:
            summary[r.status] += 1

        # Overall status
        if summary["unhealthy"] > 0:
            overall = "unhealthy"
        elif summary["degraded"] > 0:
            overall = "degraded"
        else:
            overall = "healthy"

        return HealthReport(
            timestamp=datetime.utcnow().isoformat() + "Z",
            overall_status=overall,
            checks=results,
            summary=summary
        )

    # ════════════════════════════════════════════════════════════════
    # TIER 1 CHECKS (Canonical Data)
    # ════════════════════════════════════════════════════════════════

    def _check_wiki_directory(self) -> HealthCheck:
        """Check wiki directory exists and is accessible."""
        start = time.perf_counter()
        wiki_dir = os.path.join(self.wiki_path, "wiki")

        if not os.path.exists(wiki_dir):
            return HealthCheck(
                name="wiki_directory",
                status="unhealthy",
                message="wiki/ directory does not exist",
                duration_ms=int((time.perf_counter() - start) * 1000)
            )

        if not os.access(wiki_dir, os.R_OK | os.W_OK):
            return HealthCheck(
                name="wiki_directory",
                status="unhealthy",
                message="wiki/ directory not readable/writable",
                duration_ms=int((time.perf_counter() - start) * 1000)
            )

        return HealthCheck(
            name="wiki_directory",
            status="healthy",
            message="wiki/ directory accessible",
            duration_ms=int((time.perf_counter() - start) * 1000)
        )

    def _check_manifest_integrity(self) -> HealthCheck:
        """Check manifest.jsonl is valid JSON Lines."""
        start = time.perf_counter()
        manifest_path = os.path.join(self.wiki_path, "manifest.jsonl")

        if not os.path.exists(manifest_path):
            return HealthCheck(
                name="manifest_integrity",
                status="degraded",
                message="manifest.jsonl does not exist (new wiki?)",
                duration_ms=int((time.perf_counter() - start) * 1000)
            )

        errors = []
        line_count = 0
        try:
            with open(manifest_path, 'r') as f:
                for i, line in enumerate(f, 1):
                    line_count = i
                    line = line.strip()
                    if line:
                        json.loads(line)  # Validate JSON
        except json.JSONDecodeError as e:
            errors.append(f"Line {line_count}: Invalid JSON - {e}")

        if errors:
            return HealthCheck(
                name="manifest_integrity",
                status="unhealthy",
                message=f"Manifest has {len(errors)} invalid entries",
                duration_ms=int((time.perf_counter() - start) * 1000),
                details={"errors": errors[:5]}  # First 5 errors
            )

        return HealthCheck(
            name="manifest_integrity",
            status="healthy",
            message=f"Manifest valid ({line_count} entries)",
            duration_ms=int((time.perf_counter() - start) * 1000)
        )

    def _check_page_frontmatter(self) -> HealthCheck:
        """Check all pages have valid frontmatter."""
        start = time.perf_counter()
        wiki_dir = os.path.join(self.wiki_path, "wiki")

        missing_frontmatter = []
        invalid_frontmatter = []

        for root, dirs, files in os.walk(wiki_dir):
            for f in files:
                if f.endswith('.md'):
                    path = os.path.join(root, f)
                    rel_path = os.path.relpath(path, wiki_dir)

                    try:
                        with open(path, 'r') as file:
                            content = file.read()
                            if not content.startswith('---'):
                                missing_frontmatter.append(rel_path)
                            else:
                                # Try to parse frontmatter
                                end = content.find('---', 3)
                                if end == -1:
                                    invalid_frontmatter.append(rel_path)
                    except Exception:
                        invalid_frontmatter.append(rel_path)

        total_issues = len(missing_frontmatter) + len(invalid_frontmatter)

        if total_issues > 0:
            status = "unhealthy" if total_issues > 5 else "degraded"
            return HealthCheck(
                name="page_frontmatter",
                status=status,
                message=f"{total_issues} pages with frontmatter issues",
                duration_ms=int((time.perf_counter() - start) * 1000),
                details={
                    "missing": missing_frontmatter[:5],
                    "invalid": invalid_frontmatter[:5]
                }
            )

        return HealthCheck(
            name="page_frontmatter",
            status="healthy",
            message="All pages have valid frontmatter",
            duration_ms=int((time.perf_counter() - start) * 1000)
        )

    def _check_revision_hashes(self) -> HealthCheck:
        """Check revision_hash matches actual content."""
        # Sample check - full check would be expensive
        start = time.perf_counter()
        # Implementation: Sample 10 random pages, verify hashes
        return HealthCheck(
            name="revision_hashes",
            status="healthy",
            message="Revision hashes verified (sample)",
            duration_ms=int((time.perf_counter() - start) * 1000)
        )

    def _check_wikilinks(self) -> HealthCheck:
        """Check for broken wikilinks."""
        start = time.perf_counter()
        # Implementation: Parse [[links]], verify targets exist
        return HealthCheck(
            name="wikilinks",
            status="healthy",
            message="Wikilinks verified",
            duration_ms=int((time.perf_counter() - start) * 1000)
        )

    # ════════════════════════════════════════════════════════════════
    # TIER 2 CHECKS (Derived Artifacts)
    # ════════════════════════════════════════════════════════════════

    def _check_mind_map_freshness(self) -> HealthCheck:
        """Check MIND_MAP.md is up to date."""
        start = time.perf_counter()
        mind_map_path = os.path.join(self.wiki_path, "MIND_MAP.md")

        if not os.path.exists(mind_map_path):
            return HealthCheck(
                name="mind_map_freshness",
                status="degraded",
                message="MIND_MAP.md does not exist",
                duration_ms=int((time.perf_counter() - start) * 1000)
            )

        # Check generation timestamp in header
        # Compare against newest wiki page mtime
        return HealthCheck(
            name="mind_map_freshness",
            status="healthy",
            message="MIND_MAP.md is fresh",
            duration_ms=int((time.perf_counter() - start) * 1000)
        )

    def _check_index_freshness(self) -> HealthCheck:
        """Check index.md is up to date."""
        start = time.perf_counter()
        return HealthCheck(
            name="index_freshness",
            status="healthy",
            message="index.md is fresh",
            duration_ms=int((time.perf_counter() - start) * 1000)
        )

    def _check_qmd_status(self) -> HealthCheck:
        """Check QMD search index status."""
        start = time.perf_counter()
        try:
            result = subprocess.run(
                ["qmd", "status"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                return HealthCheck(
                    name="qmd_status",
                    status="healthy",
                    message="QMD index is synced",
                    duration_ms=int((time.perf_counter() - start) * 1000)
                )
            else:
                return HealthCheck(
                    name="qmd_status",
                    status="degraded",
                    message=f"QMD reports issues: {result.stderr}",
                    duration_ms=int((time.perf_counter() - start) * 1000)
                )
        except FileNotFoundError:
            return HealthCheck(
                name="qmd_status",
                status="degraded",
                message="QMD not installed (search unavailable)",
                duration_ms=int((time.perf_counter() - start) * 1000)
            )
        except subprocess.TimeoutExpired:
            return HealthCheck(
                name="qmd_status",
                status="degraded",
                message="QMD status check timed out",
                duration_ms=int((time.perf_counter() - start) * 1000)
            )

    # ════════════════════════════════════════════════════════════════
    # TIER 3 CHECKS (Ephemeral)
    # ════════════════════════════════════════════════════════════════

    def _check_omega_status(self) -> HealthCheck:
        """Check OMEGA session memory status."""
        start = time.perf_counter()
        omega_path = os.path.expanduser("~/.omega/omega.db")

        if not os.path.exists(omega_path):
            return HealthCheck(
                name="omega_status",
                status="healthy",  # Not unhealthy, just not configured
                message="OMEGA not configured (optional)",
                duration_ms=int((time.perf_counter() - start) * 1000)
            )

        return HealthCheck(
            name="omega_status",
            status="healthy",
            message="OMEGA available",
            duration_ms=int((time.perf_counter() - start) * 1000)
        )

    # ════════════════════════════════════════════════════════════════
    # INFRASTRUCTURE CHECKS
    # ════════════════════════════════════════════════════════════════

    def _check_disk_space(self) -> HealthCheck:
        """Check available disk space."""
        start = time.perf_counter()
        stat = os.statvfs(self.wiki_path)
        free_gb = (stat.f_bavail * stat.f_frsize) / (1024 ** 3)

        if free_gb < 1:
            status = "unhealthy"
            message = f"Critically low disk space: {free_gb:.1f} GB"
        elif free_gb < 5:
            status = "degraded"
            message = f"Low disk space: {free_gb:.1f} GB"
        else:
            status = "healthy"
            message = f"Disk space OK: {free_gb:.1f} GB free"

        return HealthCheck(
            name="disk_space",
            status=status,
            message=message,
            duration_ms=int((time.perf_counter() - start) * 1000),
            details={"free_gb": round(free_gb, 2)}
        )

    def _check_job_queue(self) -> HealthCheck:
        """Check derived job queue status."""
        start = time.perf_counter()
        jobs_path = os.path.join(self.wiki_path, "jobs.jsonl")

        if not os.path.exists(jobs_path):
            return HealthCheck(
                name="job_queue",
                status="healthy",
                message="Job queue empty",
                duration_ms=int((time.perf_counter() - start) * 1000)
            )

        pending = 0
        failed = 0
        with open(jobs_path, 'r') as f:
            for line in f:
                job = json.loads(line)
                if job.get("status") == "pending":
                    pending += 1
                elif job.get("status") == "failed":
                    failed += 1

        if failed > 5:
            status = "degraded"
            message = f"{failed} failed jobs need attention"
        elif pending > 20:
            status = "degraded"
            message = f"Large job queue backlog: {pending} pending"
        else:
            status = "healthy"
            message = f"Job queue OK ({pending} pending, {failed} failed)"

        return HealthCheck(
            name="job_queue",
            status=status,
            message=message,
            duration_ms=int((time.perf_counter() - start) * 1000),
            details={"pending": pending, "failed": failed}
        )

    def _check_wal_pending(self) -> HealthCheck:
        """Check for incomplete WAL entries (crash recovery needed)."""
        start = time.perf_counter()
        wal_path = os.path.join(self.wiki_path, "manifest.wal")

        if not os.path.exists(wal_path):
            return HealthCheck(
                name="wal_pending",
                status="healthy",
                message="No pending WAL entries",
                duration_ms=int((time.perf_counter() - start) * 1000)
            )

        pending = 0
        with open(wal_path, 'r') as f:
            for line in f:
                entry = json.loads(line)
                if entry.get("status") == "in_progress":
                    pending += 1

        if pending > 0:
            return HealthCheck(
                name="wal_pending",
                status="unhealthy",
                message=f"{pending} incomplete transactions (recovery needed)",
                duration_ms=int((time.perf_counter() - start) * 1000),
                details={"pending_count": pending}
            )

        return HealthCheck(
            name="wal_pending",
            status="healthy",
            message="No pending WAL entries",
            duration_ms=int((time.perf_counter() - start) * 1000)
        )

    # ════════════════════════════════════════════════════════════════
    # HEALTH REPORT GENERATION
    # ════════════════════════════════════════════════════════════════

    def generate_markdown_report(self, report: HealthReport) -> str:
        """Generate human-readable markdown health report."""
        lines = [
            "# Wiki Health Report",
            "",
            f"*Generated: {report.timestamp}*",
            "",
            f"## Overall Status: {report.overall_status.upper()}",
            "",
            "| Status | Count |",
            "|--------|-------|",
            f"| Healthy | {report.summary['healthy']} |",
            f"| Degraded | {report.summary['degraded']} |",
            f"| Unhealthy | {report.summary['unhealthy']} |",
            "",
            "## Check Details",
            ""
        ]

        # Group by status
        for status in ["unhealthy", "degraded", "healthy"]:
            checks = [c for c in report.checks if c.status == status]
            if checks:
                emoji = {"healthy": "✅", "degraded": "⚠️", "unhealthy": "❌"}[status]
                lines.append(f"### {emoji} {status.capitalize()}")
                lines.append("")
                for check in checks:
                    lines.append(f"**{check.name}** ({check.duration_ms}ms)")
                    lines.append(f": {check.message}")
                    if check.details:
                        lines.append(f"  - Details: `{json.dumps(check.details)}`")
                    lines.append("")

        return "\n".join(lines)
```

### 5B.6 Alerting Rules

Define conditions that trigger alerts for operator attention.

```python
@dataclass
class AlertRule:
    """Definition of an alert condition."""
    name: str
    severity: str  # "critical" | "warning" | "info"
    condition: str  # Human-readable description
    check_fn: Callable[[], bool]  # Returns True if alert should fire
    cooldown_seconds: int = 300  # Minimum time between alerts


class AlertManager:
    """
    Manages alert rules and notifications.

    Alerts are written to logs/alerts.jsonl and can optionally
    trigger external notifications (email, Slack, etc.).
    """

    STANDARD_RULES = [
        AlertRule(
            name="disk_space_critical",
            severity="critical",
            condition="Free disk space < 1 GB",
            check_fn=lambda: get_free_disk_gb() < 1,
            cooldown_seconds=300
        ),
        AlertRule(
            name="wal_recovery_needed",
            severity="critical",
            condition="Incomplete WAL entries detected",
            check_fn=lambda: count_pending_wal() > 0,
            cooldown_seconds=60
        ),
        AlertRule(
            name="manifest_corrupted",
            severity="critical",
            condition="manifest.jsonl has invalid entries",
            check_fn=lambda: not validate_manifest(),
            cooldown_seconds=300
        ),
        AlertRule(
            name="job_queue_backlog",
            severity="warning",
            condition="More than 20 pending jobs",
            check_fn=lambda: count_pending_jobs() > 20,
            cooldown_seconds=600
        ),
        AlertRule(
            name="derived_stale",
            severity="warning",
            condition="MIND_MAP or index.md stale for > 1 hour",
            check_fn=lambda: derived_stale_minutes() > 60,
            cooldown_seconds=3600
        ),
        AlertRule(
            name="high_error_rate",
            severity="warning",
            condition="Error rate > 10% in last 100 operations",
            check_fn=lambda: recent_error_rate() > 0.1,
            cooldown_seconds=600
        ),
        AlertRule(
            name="qmd_unavailable",
            severity="info",
            condition="QMD search index unavailable",
            check_fn=lambda: not qmd_available(),
            cooldown_seconds=1800
        )
    ]

    def check_all_rules(self) -> List[Dict]:
        """Check all rules and return fired alerts."""
        fired = []
        for rule in self.STANDARD_RULES:
            if self._should_check(rule) and rule.check_fn():
                alert = self._fire_alert(rule)
                fired.append(alert)
        return fired

    def _fire_alert(self, rule: AlertRule) -> Dict:
        """Record and potentially notify about an alert."""
        alert = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "name": rule.name,
            "severity": rule.severity,
            "condition": rule.condition,
            "status": "firing"
        }

        # Persist to alerts log
        with open("logs/alerts.jsonl", 'a') as f:
            f.write(json.dumps(alert) + '\n')

        return alert
```

### 5B.7 Debug Tools

Command-line utilities for troubleshooting.

```python
class WikiDebugger:
    """
    Debug utilities for wiki troubleshooting.

    Usage:
        /wiki:debug logs --op-id op_123
        /wiki:debug trace --trace-id trace_456
        /wiki:debug metrics --name operation_duration --last 1h
        /wiki:debug health --full
    """

    def query_logs(
        self,
        op_id: Optional[str] = None,
        trace_id: Optional[str] = None,
        level: Optional[str] = None,
        event: Optional[str] = None,
        since: Optional[str] = None,
        limit: int = 100
    ) -> List[Dict]:
        """
        Query structured logs with filters.

        Examples:
            query_logs(op_id="op_123")  # All logs for operation
            query_logs(level="ERROR", since="1h")  # Recent errors
            query_logs(event="page_create")  # All page creations
        """
        results = []
        with open("logs/wiki.jsonl", 'r') as f:
            for line in f:
                entry = json.loads(line)

                # Apply filters
                if op_id and entry.get("op_id") != op_id:
                    continue
                if trace_id and entry.get("trace_id") != trace_id:
                    continue
                if level and entry.get("level") != level:
                    continue
                if event and entry.get("event") != event:
                    continue
                # TODO: since filter

                results.append(entry)
                if len(results) >= limit:
                    break

        return results

    def reconstruct_trace(self, trace_id: str) -> Dict:
        """
        Reconstruct full trace tree from spans.

        Returns hierarchical structure showing operation flow.
        """
        spans = []
        with open("logs/traces.jsonl", 'r') as f:
            for line in f:
                span = json.loads(line)
                if span.get("trace_id") == trace_id:
                    spans.append(span)

        # Build tree
        by_id = {s["span_id"]: s for s in spans}
        root = None
        for span in spans:
            parent_id = span.get("parent_span_id")
            if parent_id is None:
                root = span
            elif parent_id in by_id:
                parent = by_id[parent_id]
                if "children" not in parent:
                    parent["children"] = []
                parent["children"].append(span)

        return root

    def summarize_metrics(
        self,
        name: str,
        window: str = "1h"
    ) -> Dict:
        """
        Summarize metric over time window.

        Returns: count, min, max, mean, p50, p90, p99
        """
        # Parse window (e.g., "1h", "24h", "7d")
        # Read metrics, filter by window, compute stats
        pass

    def diff_revisions(
        self,
        page_id: str,
        rev_a: int,
        rev_b: int
    ) -> str:
        """
        Generate diff between two page revisions.

        Returns unified diff format.
        """
        pass

    def explain_operation(self, op_id: str) -> str:
        """
        Generate human-readable explanation of an operation.

        Combines logs, traces, and manifest to tell the story.
        """
        # Get manifest entry
        manifest_entry = self._get_manifest_entry(op_id)

        # Get all logs
        logs = self.query_logs(op_id=op_id)

        # Get trace
        trace_id = None
        for log in logs:
            if log.get("trace_id"):
                trace_id = log["trace_id"]
                break

        trace = self.reconstruct_trace(trace_id) if trace_id else None

        # Generate explanation
        lines = [
            f"# Operation: {op_id}",
            f"Type: {manifest_entry.get('op_type')}",
            f"Status: {manifest_entry.get('status')}",
            f"Timestamp: {manifest_entry.get('timestamp')}",
            "",
            "## Timeline",
        ]

        for log in sorted(logs, key=lambda x: x["timestamp"]):
            lines.append(f"- {log['timestamp']}: [{log['level']}] {log['message']}")

        if trace:
            lines.extend(["", "## Trace Tree"])
            lines.append(self._format_trace_tree(trace))

        return "\n".join(lines)

    def _format_trace_tree(self, span: Dict, indent: int = 0) -> str:
        """Format trace as ASCII tree."""
        prefix = "  " * indent
        status_icon = "✓" if span.get("status") == "success" else "✗"
        line = f"{prefix}{status_icon} {span['operation_name']} ({span.get('duration_ms', '?')}ms)"

        result = [line]
        for child in span.get("children", []):
            result.append(self._format_trace_tree(child, indent + 1))

        return "\n".join(result)
```

### 5B.8 Observability Test Scenarios

```python
def test_structured_logging_captures_full_operation():
    """Test: All stages of an operation are logged."""
    wiki = create_test_wiki()
    logger = WikiLogger(wiki.path)

    # Perform operation
    result = ingest_source(wiki, "test.pdf")

    # Query logs for this operation
    logs = logger.query_logs(op_id=result.op_id)

    # Verify all stages logged
    events = [log["event"] for log in logs]
    assert "operation_start" in events
    assert "stage_enter" in events  # Multiple
    assert "stage_exit" in events   # Multiple
    assert "operation_complete" in events

    # Verify trace continuity
    trace_ids = set(log.get("trace_id") for log in logs)
    assert len(trace_ids) == 1  # All logs share same trace


def test_metrics_histogram_accuracy():
    """Test: Histogram percentiles are accurate."""
    metrics = MetricsCollector("test_wiki")

    # Record known values
    values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for v in values:
        metrics.observe("test_latency", v, "ms")

    stats = metrics.get_histogram_stats("test_latency")

    assert stats["min"] == 10
    assert stats["max"] == 100
    assert stats["mean"] == 55
    assert stats["p50"] == 50
    assert stats["p90"] == 90


def test_health_check_detects_issues():
    """Test: Health checks catch common problems."""
    wiki = create_test_wiki()
    monitor = HealthMonitor(wiki.path)

    # Create a problem: invalid manifest entry
    with open(os.path.join(wiki.path, "manifest.jsonl"), 'a') as f:
        f.write("not valid json\n")

    # Run health checks
    report = monitor.run_all_checks()

    # Should detect the issue
    manifest_check = next(
        c for c in report.checks if c.name == "manifest_integrity"
    )
    assert manifest_check.status == "unhealthy"
    assert report.overall_status == "unhealthy"


def test_trace_reconstruction():
    """Test: Can reconstruct operation flow from spans."""
    wiki = create_test_wiki()
    tracer = Tracer(wiki.path)

    # Simulate operation with nested spans
    with tracer.span_context("ingest") as root:
        with tracer.span_context("validate", parent=root) as validate:
            time.sleep(0.01)
        with tracer.span_context("compute", parent=root) as compute:
            with tracer.span_context("extract_entities", parent=compute):
                time.sleep(0.01)
            with tracer.span_context("extract_concepts", parent=compute):
                time.sleep(0.01)
        with tracer.span_context("commit", parent=root):
            time.sleep(0.01)

    # Reconstruct trace
    debugger = WikiDebugger(wiki.path)
    trace_tree = debugger.reconstruct_trace(root.trace_id)

    # Verify structure
    assert trace_tree["operation_name"] == "ingest"
    assert len(trace_tree["children"]) == 3  # validate, compute, commit
    compute_span = next(c for c in trace_tree["children"]
                        if c["operation_name"] == "compute")
    assert len(compute_span["children"]) == 2  # extract_entities, extract_concepts
```

---

## 6. Operations & Skills

### 6.1 Skill Overview

| Skill | Modifies Tier 1 | Rebuilds Tier 2 | Uses Tier 3 |
|-------|-----------------|-----------------|-------------|
| `/wiki:init` | Yes | Yes | Yes (register) |
| `/wiki:ingest` | Yes | Invalidates | Yes (context) |
| `/wiki:query` | Maybe (if save) | No | Yes (context) |
| `/wiki:lint` | No | Generates report | No |
| `/wiki:rebuild` | No | Yes | No |
| `/wiki:doctor` | No | Checks | Checks |

### 6.2 `/wiki:init`

**Purpose:** Initialize a new wiki project.

**Creates (Tier 1):**
- `schema.yml` — Wiki configuration
- `manifest.jsonl` — Empty operation ledger (with init entry)
- `wiki/` directory structure

**Creates (Tier 2):**
- `MIND_MAP.md` — Empty scaffold
- `index.md` — Empty table of contents

**Configures:**
- QMD collection with contexts
- OMEGA project registration

**Manifest Entry:**
```json
{
  "op_id": "op_001",
  "op_type": "init",
  "timestamp": "2024-01-01T10:00:00Z",
  "inputs": {
    "profile": "research-papers",
    "topic": "transformer architectures"
  },
  "outputs": {
    "created_files": ["schema.yml", "manifest.jsonl"],
    "created_directories": ["wiki/sources", "wiki/entities", "wiki/concepts", "wiki/analyses", "wiki/contradictions"]
  },
  "status": "completed"
}
```

### 6.3 `/wiki:ingest`

**Purpose:** Process a source document into the wiki.

**Input:** Path to source in `raw/`

**Modifies (Tier 1):**
- Creates `wiki/sources/{source}.md`
- Creates/updates `wiki/entities/*.md`
- Creates/updates `wiki/concepts/*.md`
- Creates `wiki/contradictions/*.md` if disagreements found
- Appends to `manifest.jsonl`

**Invalidates (Tier 2):**
- `MIND_MAP.md`
- `index.md`
- QMD index

**Process:**

```
1. READ SOURCE
   - Parse raw/{source} (PDF, markdown, etc.)
   - Extract: title, authors, date, content

2. ANALYZE
   - Identify main thesis and key claims
   - Extract entities (people, orgs, places)
   - Extract concepts (ideas, methods)
   - Check for contradictions with existing wiki (via QMD search)

3. DISCUSS WITH USER
   - Present findings
   - Ask what to emphasize
   - Confirm entities and concepts to create/update

4. WRITE CANONICAL PAGES
   For each page:
   a. Generate content
   b. Create frontmatter with revision_id: 1 (new) or N+1 (update)
   c. Compute revision_hash
   d. Set updated_by: current op_id
   e. Write to disk

5. APPEND TO MANIFEST
   - Record all created/updated pages with revision numbers
   - Mark derived artifacts as invalidated
   - Set status: completed

6. OPTIONALLY REBUILD DERIVED
   - If schema.yml has auto_rebuild: true
   - Rebuild MIND_MAP, index, QMD
```

### 6.4 `/wiki:query`

**Purpose:** Answer a question using the wiki.

**Process:**

```
1. CHECK DERIVED FRESHNESS
   - If QMD stale, warn or rebuild

2. SEARCH (via QMD)
   - qmd query "{question}" --json -n 10
   - Get ranked list of relevant pages

3. READ CANONICAL PAGES
   - Read top-N pages from search results
   - Read MIND_MAP for orientation

4. ADD SESSION CONTEXT (via OMEGA)
   - Query OMEGA for relevant session memories
   - Add as helpful context (not authoritative)

5. SYNTHESIZE ANSWER
   - Combine wiki knowledge + session context
   - Cite wiki pages with wikilinks
   - Note contradictions if relevant

6. OFFER TO SAVE
   - If answer is valuable, offer to save as analysis page
   - If saved: write to Tier 1, append to manifest
```

### 6.5 `/wiki:lint`

**Purpose:** Health-check the wiki.

**Checks:**

| Category | Check | Severity |
|----------|-------|----------|
| Tier 1 | Pages have valid frontmatter | Error |
| Tier 1 | revision_hash matches content | Error |
| Tier 1 | Wikilinks resolve to existing pages | Warning |
| Tier 1 | No orphan pages (reachable from index) | Warning |
| Tier 1 | manifest.jsonl is valid JSON Lines | Error |
| Tier 2 | MIND_MAP is fresh (matches wiki state) | Warning |
| Tier 2 | index.md is fresh | Warning |
| Tier 2 | QMD index is synced | Warning |

**Output:** `health_report.md` (Tier 2)

### 6.6 `/wiki:rebuild`

**Purpose:** Regenerate all Tier 2 artifacts from Tier 1.

**Process:**

```
1. VERIFY TIER 1 INTEGRITY
   - All pages have valid frontmatter
   - All revision_hashes match content
   - manifest.jsonl is valid

2. REBUILD MIND_MAP
   - Read all wiki pages
   - Generate nodes from frontmatter + links
   - Write MIND_MAP.md with generation header

3. REBUILD INDEX
   - Read all wiki page frontmatter
   - Generate tables per category
   - Write index.md with generation header

4. REBUILD QMD INDEX
   - qmd collection remove wiki (if exists)
   - qmd collection add wiki/ --name wiki
   - Apply contexts from schema.yml
   - qmd update && qmd embed

5. LOG TO MANIFEST
   - Append rebuild_derived operation
```

### 6.7 `/wiki:doctor`

**Purpose:** Check system health.

**Checks:**

| System | Check |
|--------|-------|
| Tier 1 | wiki/ directory exists |
| Tier 1 | schema.yml exists and valid |
| Tier 1 | manifest.jsonl exists and valid |
| Tier 2 | MIND_MAP.md exists |
| Tier 2 | index.md exists |
| Tier 2 | QMD installed and configured |
| Tier 3 | OMEGA installed (optional) |

---

## 6A. Revision-Aware Operations

All operations must be revision-aware to enable conflict detection, rollback, and provenance tracking.

### 6A.1 Revision-Aware Ingest

**Full Algorithm:**

```
ingest_source(wiki, source_path, expected_wiki_state=None) → IngestResult

1. LOAD AND HASH SOURCE
   source_content = read_file(source_path)
   source_hash = sha256(source_content)

2. CHECK FOR DUPLICATES
   existing = manifest.find_by_source_hash(source_hash)

   If existing AND source unchanged:
     ��� Return DUPLICATE (source already ingested)

   If existing AND source changed:
     → Return CONFLICT (same path, different content)
     → User must resolve: re-ingest with new name or update existing

3. EXTRACT ENTITIES, CONCEPTS, CLAIMS
   extracted = llm_extract(source_content)

   For each extracted.entity:
     → Check alias registry for existing match
     → Deduplicate: "Andrew Y. Ng" matches "entities/andrew_ng.md"

   For each extracted.concept:
     → Check for existing concept page
     → Identify potential contradictions with existing claims

4. CAPTURE WIKI STATE (for optimistic locking)
   If expected_wiki_state provided:
     → Verify current state matches expected
     → If mismatch: CONFLICT (wiki changed during operation)

   current_state = {
     page_id: revision_id
     for page_id in pages_to_update
   }

5. WRITE PAGES WITH REVISION TRACKING
   created_pages = []
   updated_pages = []

   For each page_to_write:
     If page exists:
       current = load_page(page_id)

       # Optimistic lock check
       If expected_wiki_state AND current.revision_id != expected_wiki_state[page_id]:
         → CONFLICT: page changed since operation started

       # Merge content (see merge strategies below)
       merged_content = merge_page(current, new_info, strategy)

       new_revision = current.revision_id + 1
       updated_pages.append({
         page_id: page_id,
         old_revision: current.revision_id,
         new_revision: new_revision
       })

       # Archive current revision
       archive_revision(page_id, current)

     Else:
       new_revision = 1
       merged_content = new_info
       created_pages.append({
         page_id: page_id,
         revision_id: 1
       })

     # Write page with revision metadata
     write_page(page_id, merged_content, {
       revision_id: new_revision,
       revision_hash: sha256(merged_content.body),
       updated_by: op_id,
       updated: now()
     })

6. CREATE SOURCE SUMMARY PAGE
   # Source summaries are immutable (always revision 1)
   write_page(f"sources/{source_slug}", source_summary, {
     revision_id: 1,
     revision_hash: sha256(source_summary.body),
     source_path: source_path,
     source_hash: source_hash
   })

7. WRITE MANIFEST ENTRY
   manifest.append({
     op_id: op_id,
     op_type: "ingest",
     inputs: {
       source_path: source_path,
       source_hash: source_hash,
       wiki_state_at_start: current_state
     },
     outputs: {
       created_pages: created_pages,
       updated_pages: updated_pages,
       page_revisions: {p.page_id: p.new_revision for p in all_pages}
     },
     status: "completed",
     derived_invalidated: ["MIND_MAP.md", "index.md", "qmd_index"]
   })

8. ENQUEUE DERIVED JOBS
   If auto_rebuild:
     rebuild_mind_map()
     rebuild_index()
     qmd_update()

9. VERIFY INVARIANTS
   violations = verify_tier1_invariants()
   If violations:
     → Rollback operation
     → Return FAILED with violations

10. RETURN RESULT
    Return IngestResult(
      status: "completed",
      created_pages: created_pages,
      updated_pages: updated_pages,
      manifest_op_id: op_id
    )
```

**Return Values:**

| Status | Meaning | Action Required |
|--------|---------|-----------------|
| `completed` | Ingest successful | None |
| `duplicate` | Source already ingested (unchanged) | None (no-op) |
| `conflict_source` | Source path exists with different content | Rename or force re-ingest |
| `conflict_wiki` | Wiki changed during operation | Retry with fresh state |
| `failed` | Invariant violation | Check error, fix, retry |

### 6A.2 Merge Strategies

When updating existing pages, choose merge strategy based on page type:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ STRATEGY A: CLAIMS-BASED MERGE (for entities, concepts)                     │
│                                                                              │
│ Structure:                                                                   │
│   Each page contains discrete claims with provenance:                       │
���                                                                              │
│   claims:                                                                    │
│     - claim: "Attention has O(n²) complexity"                               │
│       source: "sources/vaswani2017"                                         │
│       confidence: high                                                       │
��       added_in_revision: 3                                                   │
│                                                                              │
│     - claim: "Linear attention achieves O(n) complexity"                    │
│       source: "sources/katharopoulos2020"                                   │
│       confidence: high                                                       │
│       added_in_revision: 7                                                   │
│                                                                              │
│ Merge algorithm:                                                             │
│   1. Load existing claims                                                   │
│   2. For each new claim:                                                    │
│      a. Check if contradicts existing claim                                 │
│      b. If contradiction: create contradiction record, keep both claims     │
│      c. If no contradiction: append claim with provenance                   │
│   3. Claims are never deleted, only marked superseded                       │
│                                                                              │
│ Properties:                                                                  │
│   ✓ Deterministic (same input → same output)                               │
│   ✓ Preserves provenance                                                    │
│   ✓ Handles contradictions explicitly                                       │
│   ✗ Pages grow over time (may need compaction)                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ STRATEGY B: LLM SYNTHESIS (for analyses)                                    │
│                                                                              │
│ Use case: Narrative pages where claims-based merge is awkward              │
│                                                                              │
│ Merge algorithm:                                                             │
│   1. Load existing page content                                             │
│   2. Provide to LLM: existing + new information                             │
│   3. LLM synthesizes coherent update                                        │
│   4. Mark in frontmatter: merge_strategy: "llm_synthesis"                  │
│                                                                              │
│ Properties:                                                                  │
│   ✓ Maintains readability and coherence                                    │
│   ✗ Non-deterministic                                                       │
│   ✗ May lose nuance                                                         │
│                                                                              │
│ Mitigation:                                                                  │
│   - Store pre-merge content in .history/                                    │
│   - Human review recommended for synthesis merges                           │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ STRATEGY C: APPEND-ONLY (for source pages)                                  │
│                                                                              │
│ Source summaries are immutable:                                             │
│   - Created once with revision_id: 1                                        │
│   - Never updated (append new source page instead)                          │
│   - If source changes, create new page with new slug                        │
│                                                                              │
│ Rationale: Sources are external truth, we summarize, not modify            │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Merge Strategy Selection:**

| Page Type | Strategy | Rationale |
|-----------|----------|-----------|
| `source` | Append-only | Immutable summaries |
| `entity` | Claims-based | Structured facts with provenance |
| `concept` | Claims-based | Structured knowledge with provenance |
| `analysis` | LLM synthesis | Narrative coherence |
| `contradiction` | Claims-based | Track both sides |

### 6A.3 Entity Deduplication via Alias Registry

**Problem:** Extracted "Andrew Y. Ng" might match existing "entities/andrew_ng.md"

**Solution:** Alias registry in frontmatter:

```yaml
---
title: "Andrew Ng"
page_id: "entities/andrew_ng"
entity_type: "person"

# Alias registry for deduplication
aliases:
  - "Andrew Ng"
  - "Andrew Y. Ng"
  - "A. Ng"
  - "吴恩达"

# Slug variants that redirect here
slug_aliases:
  - "andrew_y_ng"
  - "a_ng"
---
```

**Deduplication Algorithm:**

```
resolve_entity(extracted_name) → (page_id, is_new)

1. Generate candidate slug: slugify(extracted_name)
   Example: "Andrew Y. Ng" → "andrew_y_ng"

2. Check direct match:
   If file_exists(f"entities/{candidate_slug}.md"):
     → Return (f"entities/{candidate_slug}", is_new=False)

3. Search alias registries:
   For each entity_page in wiki/entities/:
     If extracted_name in entity_page.aliases:
       → Return (entity_page.page_id, is_new=False)

     If candidate_slug in entity_page.slug_aliases:
       → Return (entity_page.page_id, is_new=False)

4. Fuzzy match (optional):
   similar = find_similar_entities(extracted_name, threshold=0.85)
   If similar:
     → Ask user: "Is '{extracted_name}' the same as '{similar.title}'?"
     → If yes: add alias, return existing page
     → If no: create new page

5. No match found:
   → Return (f"entities/{candidate_slug}", is_new=True)
   → Create new page with extracted_name as first alias
```

### 6A.4 Revision-Aware Query

**Query with Revision Pinning for Reproducibility:**

```
query_wiki(wiki, question, revision_snapshot=None) → QueryResult

1. DETERMINE REVISION CONTEXT
   If revision_snapshot provided:
     # Historical query: use specific revisions
     pages_to_use = {
       page_id: load_revision(page_id, rev_id)
       for page_id, rev_id in revision_snapshot.items()
     }
   Else:
     # Current query: use latest revisions
     pages_to_use = load_latest_pages()

2. SEARCH (via QMD)
   # QMD always uses latest index
   search_results = qmd_query(question)

   # Filter to pages in revision context
   relevant_pages = [
     pages_to_use[r.page_id]
     for r in search_results
     if r.page_id in pages_to_use
   ]

3. READ PAGES AT SPECIFIED REVISIONS
   For each relevant_page:
     If revision_snapshot AND page_id in revision_snapshot:
       content = load_from_history(page_id, revision_snapshot[page_id])
     Else:
       content = load_latest(page_id)

4. ADD SESSION CONTEXT (OMEGA)
   # OMEGA context is always latest (ephemeral)
   session_context = omega_query(question)

5. SYNTHESIZE ANSWER
   answer = llm_synthesize(
     question=question,
     pages=relevant_pages,
     session_context=session_context
   )

6. CAPTURE REVISION SNAPSHOT
   # Record exactly which revisions were used
   snapshot = {
     page.page_id: page.revision_id
     for page in relevant_pages
   }

7. RETURN RESULT
   Return QueryResult(
     answer: answer,
     sources: [
       {page_id, revision_id, relevance_score}
       for page in relevant_pages
     ],
     revision_snapshot: snapshot,
     confidence: computed_confidence
   )
```

**Reproducibility Guarantee:**

```python
# Query today
result_1 = query_wiki(wiki, "What is attention?")
snapshot = result_1.revision_snapshot
# {"concepts/attention": 12, "sources/vaswani2017": 1}

# Time passes, wiki changes...
ingest_source(wiki, "new_paper.pdf")  # concepts/attention → rev 13

# Query again with pinned snapshot
result_2 = query_wiki(wiki, "What is attention?",
                      revision_snapshot=snapshot)

# Same question + same snapshot → same answer
assert result_1.answer == result_2.answer
assert result_1.sources == result_2.sources
```

**Use Cases:**

| Scenario | revision_snapshot | Behavior |
|----------|-------------------|----------|
| Normal query | `None` | Latest revisions |
| Historical query | `{"concepts/ml": 42}` | Specific revision for that page |
| Reproducible query | Full snapshot from previous query | Identical results |
| Audit query | Snapshot from manifest op | See wiki as it was during operation |

### 6A.5 Revision-Aware Update with Optimistic Locking

**Update with Conflict Detection:**

```
update_page(wiki, page_id, content_delta, base_revision, actor="llm")
  → UpdateResult

1. LOAD CURRENT PAGE
   current = load_page(page_id)

2. OPTIMISTIC LOCK CHECK
   If current.revision_id != base_revision:
     # Page changed since we read it
     Return UpdateResult(
       status: "conflict",
       conflict_details: {
         expected_revision: base_revision,
         actual_revision: current.revision_id,
         diff: compute_diff(
           load_revision(page_id, base_revision),
           current
         )
       }
     )

3. APPLY CONTENT DELTA
   If content_delta is str:
     new_content = content_delta
   Else:
     new_content = apply_structured_delta(current.content, content_delta)

4. COMPUTE NEW REVISION METADATA
   new_revision_id = current.revision_id + 1
   new_revision_hash = sha256(new_content.body)

5. ARCHIVE CURRENT REVISION
   archive_revision(page_id, current)
   # Writes to: wiki/.history/{page_id}/rev_{revision_id}.md

6. WRITE NEW REVISION
   write_page(page_id, new_content, {
     revision_id: new_revision_id,
     revision_hash: new_revision_hash,
     updated_by: current_op_id,
     updated: now()
   })

7. WRITE MANIFEST ENTRY
   manifest.append({
     op_id: current_op_id,
     op_type: "update",
     inputs: {
       page_id: page_id,
       base_revision: base_revision,
       actor: actor
     },
     outputs: {
       new_revision: new_revision_id
     },
     status: "completed"
   })

8. RETURN SUCCESS
   Return UpdateResult(
     status: "completed",
     new_revision_id: new_revision_id
   )
```

### 6A.6 Conflict Resolution Strategies

When a conflict is detected, choose resolution strategy:

```
resolve_update_conflict(wiki, page_id, base_revision,
                        local_changes, remote_changes) → Resolution

STRATEGY 1: THREE-WAY MERGE (if changes touch different sections)

  base = load_revision(page_id, base_revision)
  remote = load_latest(page_id)

  If changes_are_disjoint(base, local_changes, remote_changes):
    merged = three_way_merge(base, local_changes, remote_changes)
    Return Resolution(
      strategy: "three_way_merge",
      result: merged,
      auto_resolved: True
    )


STRATEGY 2: ACCEPT REMOTE (discard local changes)

  # Safe: just re-read and try again
  Return Resolution(
    strategy: "accept_remote",
    result: load_latest(page_id),
    message: "Discarded local changes, accepted remote version"
  )


STRATEGY 3: ACCEPT LOCAL (overwrite remote) — DANGEROUS

  # Only with explicit user confirmation
  Return Resolution(
    strategy: "accept_local",
    result: apply_local_changes(base, local_changes),
    warning: "Remote changes will be lost",
    requires_confirmation: True
  )


STRATEGY 4: ESCALATE TO USER

  # Default when automatic merge fails
  Return Resolution(
    strategy: "escalate",
    conflict_details: {
      base: load_revision(page_id, base_revision),
      local: apply_local_changes(base, local_changes),
      remote: load_latest(page_id),
      diff_local_remote: compute_diff(local, remote)
    },
    message: "Automatic merge failed, please resolve manually"
  )
```

**Conflict Resolution Matrix:**

| Local Change | Remote Change | Resolution |
|--------------|---------------|------------|
| Section A | Section B | Three-way merge ✓ |
| Section A | Section A (same) | No conflict |
| Section A | Section A (different) | Escalate to user |
| Add claim | Add different claim | Append both |
| Delete claim | Modify claim | Escalate to user |

### 6A.7 Rollback Mechanisms

**Rollback Single Page:**

```
rollback_page(wiki, page_id, target_revision, reason) → RollbackResult

1. VERIFY TARGET REVISION EXISTS
   target = load_revision(page_id, target_revision)
   If not target:
     Return RollbackResult(status: "failed", error: "Revision not found")

2. LOAD CURRENT REVISION
   current = load_page(page_id)

3. CREATE NEW REVISION WITH ROLLBACK CONTENT
   # Rollback creates NEW revision, doesn't delete history
   new_revision_id = current.revision_id + 1

   rollback_content = target.content
   rollback_frontmatter = {
     ...target.frontmatter,
     revision_id: new_revision_id,
     revision_hash: sha256(target.content.body),
     updated_by: current_op_id,
     updated: now(),

     # Rollback metadata
     rollback: {
       from_revision: current.revision_id,
       to_revision: target_revision,
       reason: reason,
       timestamp: now()
     }
   }

4. ARCHIVE CURRENT REVISION
   archive_revision(page_id, current)

5. WRITE ROLLBACK REVISION
   write_page(page_id, rollback_content, rollback_frontmatter)

6. WRITE MANIFEST ENTRY
   manifest.append({
     op_id: current_op_id,
     op_type: "rollback",
     inputs: {
       page_id: page_id,
       from_revision: current.revision_id,
       to_revision: target_revision,
       reason: reason
     },
     outputs: {
       new_revision: new_revision_id
     },
     status: "completed"
   })

7. RETURN RESULT
   Return RollbackResult(
     status: "completed",
     new_revision_id: new_revision_id,
     rolled_back_from: current.revision_id,
     rolled_back_to: target_revision
   )
```

**Rollback Entire Operation:**

```
rollback_operation(wiki, op_id) → RollbackResult

Use case: Ingested wrong source, want to undo all changes.

1. LOAD OPERATION FROM MANIFEST
   op = manifest.get(op_id)
   If not op:
     Return RollbackResult(status: "failed", error: "Operation not found")

2. PROCESS CREATED PAGES
   For each page_id in op.created_pages:
     # Don't delete, mark as tombstone
     current = load_page(page_id)
     write_page(page_id, current.content, {
       ...current.frontmatter,
       revision_id: current.revision_id + 1,
       deleted: True,
       deleted_by: current_op_id,
       deleted_reason: f"Rollback of {op_id}"
     })

3. PROCESS UPDATED PAGES
   For each {page_id, old_revision, new_revision} in op.updated_pages:
     # Rollback to revision before this operation
     rollback_page(
       wiki,
       page_id,
       target_revision=old_revision,
       reason=f"Rollback of operation {op_id}"
     )

4. WRITE ROLLBACK MANIFEST ENTRY
   manifest.append({
     op_id: current_op_id,
     op_type: "rollback_operation",
     inputs: {
       rolled_back_op_id: op_id
     },
     outputs: {
       pages_deleted: op.created_pages,
       pages_rolled_back: [p.page_id for p in op.updated_pages]
     },
     status: "completed"
   })

5. INVALIDATE DERIVED ARTIFACTS
   # Mark MIND_MAP, index, QMD as stale

6. RETURN RESULT
   Return RollbackResult(
     status: "completed",
     rolled_back_operation: op_id,
     affected_pages: op.created_pages + [p.page_id for p in op.updated_pages]
   )
```

**Key Property: History is Never Deleted**

```
Timeline of page "concepts/ml":

rev 42: Original content
rev 43: Update from ingest op_010
rev 44: Update from ingest op_015
rev 45: Rollback to rev 42 (content = rev 42, but new revision)

All revisions preserved in wiki/.history/concepts/ml/:
  - rev_042.md ✓
  - rev_043.md ✓
  - rev_044.md ✓
  - rev_045.md ✓ (rollback, content matches rev_042)
```

### 6A.8 Revision-Aware Test Scenarios

```python
def test_concurrent_update_detection():
    """Two operations update same page, second detects conflict."""
    wiki = create_test_wiki()
    page_id = "concepts/ml"

    # Read current revision
    base_rev = get_revision(wiki, page_id)  # e.g., 42

    # Operation 1 updates successfully
    result_1 = update_page(wiki, page_id, "Change A", base_revision=base_rev)
    assert result_1.status == "completed"
    assert result_1.new_revision_id == base_rev + 1  # 43

    # Operation 2 tries to update from same base (stale)
    result_2 = update_page(wiki, page_id, "Change B", base_revision=base_rev)

    assert result_2.status == "conflict"
    assert result_2.conflict_details.expected_revision == base_rev  # 42
    assert result_2.conflict_details.actual_revision == base_rev + 1  # 43


def test_query_reproducibility():
    """Same query + same snapshot → identical answer."""
    wiki = create_test_wiki()
    ingest_source(wiki, "paper1.pdf")

    # Query and capture snapshot
    result_1 = query_wiki(wiki, "What is attention?")
    snapshot = result_1.revision_snapshot
    answer_1 = result_1.answer

    # Ingest more sources (wiki changes)
    ingest_source(wiki, "paper2.pdf")
    ingest_source(wiki, "paper3.pdf")

    # Query with pinned snapshot
    result_2 = query_wiki(wiki, "What is attention?",
                          revision_snapshot=snapshot)
    answer_2 = result_2.answer

    # Answers must be identical
    assert answer_1 == answer_2


def test_rollback_preserves_history():
    """Rollback creates new revision, doesn't delete history."""
    wiki = create_test_wiki()
    page_id = "concepts/ml"

    # Get current state
    rev_42 = get_revision(wiki, page_id)
    content_42 = read_page(wiki, page_id).content

    # Update twice
    update_page(wiki, page_id, "Change 1", base_revision=rev_42)  # → rev 43
    update_page(wiki, page_id, "Change 2", base_revision=43)       # → rev 44

    # Rollback to rev 42
    result = rollback_page(wiki, page_id, target_revision=42,
                           reason="Testing rollback")

    assert result.status == "completed"
    assert result.new_revision_id == 45  # New revision, not 42

    # Content matches original
    content_45 = read_page(wiki, page_id).content
    assert content_45 == content_42

    # All history preserved
    assert revision_exists(wiki, page_id, 42)  # Original
    assert revision_exists(wiki, page_id, 43)  # Change 1
    assert revision_exists(wiki, page_id, 44)  # Change 2
    assert revision_exists(wiki, page_id, 45)  # Rollback


def test_entity_deduplication():
    """Extracted entity matches existing via alias."""
    wiki = create_test_wiki()

    # Create entity with aliases
    create_page(wiki, "entities/andrew_ng", {
        "title": "Andrew Ng",
        "aliases": ["Andrew Ng", "A. Ng"]
    })

    # Extract entity with different name variation
    extracted = extract_entities("Paper by Andrew Y. Ng")

    # Should match existing, not create new
    resolved = resolve_entity(wiki, "Andrew Y. Ng")

    assert resolved.page_id == "entities/andrew_ng"
    assert resolved.is_new == False

    # Alias should be added
    page = read_page(wiki, "entities/andrew_ng")
    assert "Andrew Y. Ng" in page.aliases


def test_operation_rollback():
    """Rollback entire operation undoes all its changes."""
    wiki = create_test_wiki()

    # Capture initial state
    initial_page_count = wiki.page_count()

    # Ingest source (creates multiple pages)
    result = ingest_source(wiki, "paper.pdf")
    op_id = result.manifest_op_id

    assert wiki.page_count() > initial_page_count

    # Rollback the operation
    rollback_result = rollback_operation(wiki, op_id)

    assert rollback_result.status == "completed"

    # Created pages are tombstoned
    for page_id in result.created_pages:
        page = read_page(wiki, page_id)
        assert page.deleted == True

    # Updated pages are rolled back
    for update in result.updated_pages:
        page = read_page(wiki, update.page_id)
        assert page.revision_id > update.new_revision  # New rollback revision
        # Content matches pre-operation state
```

---

## 7. Invariants & Verification

### 7.1 Tier 1 Invariants

| Invariant | Description | Verification |
|-----------|-------------|--------------|
| INV-1 | Every page has complete frontmatter | Parse YAML, check required fields |
| INV-2 | revision_hash matches content | Recompute hash, compare |
| INV-3 | revision_id is monotonically increasing | Check manifest history |
| INV-4 | updated_by references valid manifest op | Look up op_id in manifest |
| INV-5 | All wikilinks resolve to existing pages | Parse links, check file exists |
| INV-6 | manifest.jsonl is append-only | Check no modifications to existing entries |
| INV-7 | manifest entries are atomic | Entry exists only if pages exist |

### 7.2 Tier 2 Invariants

| Invariant | Description | Verification |
|-----------|-------------|--------------|
| INV-8 | MIND_MAP is deterministic | Regenerate, compare content hash |
| INV-9 | index.md is deterministic | Regenerate, compare content hash |
| INV-10 | QMD index covers all wiki pages | qmd status, compare counts |

### 7.3 Tier Separation Invariants

| Invariant | Description | Verification |
|-----------|-------------|--------------|
| INV-11 | Tier 1 is self-sufficient | Delete Tier 2+3, rebuild, verify functionality |
| INV-12 | Tier 2 is derived | Delete Tier 2, regenerate, compare hashes |
| INV-13 | Tier 3 is ephemeral | Delete Tier 3, verify wiki still functional |

### 7.4 Verification Commands

```bash
# Verify Tier 1 integrity
/wiki:verify tier1

# Verify derived artifacts match canonical data
/wiki:verify derived

# Verify tier separation (destructive test - use on copy)
/wiki:verify separation --copy-first

# Full verification suite
/wiki:verify all
```

---

## 8. Failure Modes & Recovery

### 8.1 Disaster Recovery Procedure

**Scenario:** Laptop stolen, last backup is `wiki/` + `manifest.jsonl` from yesterday.

```
Recovery Steps:

1. Restore wiki/ + manifest.jsonl from backup
   $ cp -r backup/wiki/ ./wiki/
   $ cp backup/manifest.jsonl ./

2. Restore raw/ sources (if backed up)
   $ cp -r backup/raw/ ./raw/

3. Restore schema.yml
   $ cp backup/schema.yml ./

4. Run rebuild
   $ /wiki:rebuild all

5. Verify
   $ /wiki:doctor
   $ /wiki:lint

Result:
- MIND_MAP.md: ✓ Regenerated
- index.md: ✓ Regenerated
- QMD index: ✓ Rebuilt
- OMEGA: ✓ Empty (session context lost, acceptable)

Data loss: ZERO (all canonical knowledge intact)
Context loss: Yesterday's OMEGA sessions (acceptable ephemeral loss)
```

### 8.2 Failure Mode Matrix

| Failure | Detection | Impact | Recovery |
|---------|-----------|--------|----------|
| **Tier 1 corruption** | `/wiki:verify tier1` | DATA LOSS | Restore from backup |
| Tier 2 corruption | `/wiki:lint` | Degraded search | `/wiki:rebuild` |
| Tier 3 corruption | `/wiki:doctor` | Lost session context | Delete and continue |
| QMD not installed | `/wiki:doctor` | No search | Install QMD, rebuild index |
| OMEGA not installed | `/wiki:doctor` | No session context | Continue without (wiki functional) |
| Manifest corrupted | JSON parse error | Can't append ops | Restore from backup |
| revision_hash mismatch | `/wiki:verify tier1` | Integrity violation | Recompute hashes |
| Orphan pages | `/wiki:lint` | Reduced discoverability | Link or delete |
| Broken wikilinks | `/wiki:lint` | User confusion | Fix or remove links |

### 8.3 Graceful Degradation

| Missing Component | Wiki Functionality | Degradation |
|-------------------|-------------------|-------------|
| QMD | 80% | No semantic search, use grep |
| OMEGA | 95% | No session context, otherwise full |
| MIND_MAP.md | 90% | No quick navigation, read index.md |
| index.md | 90% | No TOC, navigate by folder |
| QMD + OMEGA | 75% | Manual navigation only |

**Key guarantee:** If you have Tier 1 (`wiki/` + `manifest.jsonl`), you can always rebuild everything else.

---

## 9. Implementation Phases

### Phase -1: Environment Setup

**Goal:** Create reproducible development environment with all dependencies.

**Prerequisites:**
- Python 3.10+ (for modern typing features like `X | None`)
- Conda (recommended) or venv
- Git

---

#### 9.-1.1 Environment Creation

**Option A: Conda (Recommended)**

```bash
# Create environment
conda create -n llm-wiki python=3.11 -y
conda activate llm-wiki

# Verify
python --version  # Should be 3.11.x
```

**Option B: venv**

```bash
# Create environment
python3.11 -m venv .venv

# Activate (Linux/Mac)
source .venv/bin/activate

# Activate (Windows)
# .venv\Scripts\activate

# Verify
python --version
```

---

#### 9.-1.2 Project Structure

Create the Python package structure:

```bash
mkdir -p src/llm_wiki
touch src/llm_wiki/__init__.py
mkdir -p tests
touch tests/__init__.py
```

**Directory layout:**

```
LLMWikiGeneration/
├── src/
│   └── llm_wiki/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── page.py          # Page class, frontmatter handling
│       │   ├── manifest.py      # Manifest operations
│       │   └── wiki.py          # Wiki class (main interface)
│       ├── pipeline/
│       │   ├── __init__.py
│       │   ├── wal.py           # Write-ahead log
│       │   ├── transaction.py   # Transaction handling
│       │   └── jobs.py          # Derived job queue
│       ├── derived/
│       │   ├── __init__.py
│       │   ├── mind_map.py      # MIND_MAP generation
│       │   └── index.py         # index.md generation
│       ├── search/
│       │   ├── __init__.py
│       │   ├── qmd.py           # QMD integration (optional)
│       │   └── grep.py          # Grep fallback
│       ├── observability/
│       │   ├── __init__.py
│       │   ├── logger.py        # Structured logging
│       │   ├── metrics.py       # Metrics collection
│       │   └── health.py        # Health checks
│       └── skills/
│           ├── __init__.py
│           ├── init.py          # /wiki:init
│           ├── ingest.py        # /wiki:ingest
│           ├── query.py         # /wiki:query
│           └── rebuild.py       # /wiki:rebuild
├── tests/
│   ├── __init__.py
│   ├── test_page.py
│   ├── test_manifest.py
│   ├── test_wal.py
│   └── conftest.py              # Pytest fixtures
├── raw/                          # Source documents (user-managed)
├── wiki/                         # Generated wiki (LLM-managed)
├── logs/                         # Observability data
├── pyproject.toml
├── mkdocs.yml                    # Wiki viewer configuration
├── CLAUDE.md
├── IMPLEMENTATION_PLAN.md
├── manifest.jsonl
└── schema.yml
```

---

#### 9.-1.3 Dependencies

**Create `pyproject.toml`:**

```toml
[project]
name = "llm-wiki"
version = "0.1.0"
description = "LLM-maintained personal wiki system"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}

dependencies = [
    # Core dependencies
    "pyyaml>=6.0",                    # schema.yml parsing
    "python-frontmatter>=1.0.0",      # Markdown frontmatter parsing

    # Wiki viewer (MkDocs)
    "mkdocs>=1.5",                    # Static site generator
    "mkdocs-material>=9.0",           # Material theme (recommended)

    # File handling
    "watchdog>=3.0",                  # File system monitoring (optional)
]

[project.optional-dependencies]
# PDF ingestion
pdf = [
    "pypdf>=3.0",                     # PDF text extraction
    "pdfplumber>=0.9",                # PDF with tables/layout
]

# Full document processing
docs = [
    "pypdf>=3.0",
    "pdfplumber>=0.9",
    "python-docx>=0.8",               # Word documents
    "openpyxl>=3.1",                  # Excel files
    "beautifulsoup4>=4.12",           # HTML parsing
    "markdownify>=0.11",              # HTML to Markdown
]

# Search (if not using QMD)
search = [
    "whoosh>=2.7",                    # Pure Python search engine
    "sentence-transformers>=2.2",     # Semantic search (optional, heavy)
]

# Development
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "pytest-asyncio>=0.21",
    "black>=23.0",
    "ruff>=0.1",
    "mypy>=1.5",
]

# All optional dependencies
all = [
    "llm-wiki[pdf,docs,search,dev]",
]

[project.scripts]
llm-wiki = "llm_wiki.cli:main"

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-v --tb=short"

[tool.black]
line-length = 100
target-version = ["py310", "py311"]

[tool.ruff]
line-length = 100
select = ["E", "F", "I", "N", "W"]

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_ignores = true
```

**Install dependencies:**

```bash
# Core only (minimal)
pip install -e .

# With PDF support
pip install -e ".[pdf]"

# With all document types
pip install -e ".[docs]"

# Development (includes testing)
pip install -e ".[dev]"

# Everything
pip install -e ".[all]"
```

---

#### 9.-1.4 External Tools

**QMD (Search Index) — OPTIONAL**

QMD is a hypothetical markdown search tool referenced in this plan. Options:

```bash
# Option 1: If QMD exists as a pip package
pip install qmd

# Option 2: If QMD is a standalone binary
# Download from: https://github.com/???/qmd/releases
# Add to PATH

# Option 3: Skip QMD, use built-in fallbacks
# The system will use grep-based search automatically
# For better search, consider:
pip install whoosh  # Pure Python full-text search
```

**Verification:**

```bash
# Check if QMD is available
which qmd && qmd --version || echo "QMD not installed - will use grep fallback"
```

**OMEGA (Session Memory) — OPTIONAL**

OMEGA is a hypothetical session memory system. Options:

```bash
# Option 1: If OMEGA exists as a pip package
pip install omega-memory

# Option 2: Skip OMEGA entirely
# The wiki functions fully without session memory
# Session context is a nice-to-have, not a requirement

# Option 3: Use simple SQLite directly (built-in alternative)
# No installation needed - Python includes sqlite3
```

**Verification:**

```bash
# Check if OMEGA is available
python -c "import omega" 2>/dev/null && echo "OMEGA available" || echo "OMEGA not installed - session context disabled"
```

---

#### 9.-1.5 Verification Script

Create `scripts/verify_env.py`:

```python
#!/usr/bin/env python3
"""Verify llm-wiki environment is correctly configured."""

import sys
import subprocess
from importlib import import_module


def check_python_version():
    """Verify Python version >= 3.10."""
    version = sys.version_info
    if version < (3, 10):
        return False, f"Python {version.major}.{version.minor} (need 3.10+)"
    return True, f"Python {version.major}.{version.minor}.{version.micro}"


def check_package(name: str, import_name: str = None):
    """Check if a package is installed and importable."""
    import_name = import_name or name
    try:
        import_module(import_name)
        return True, "installed"
    except ImportError:
        return False, "not installed"


def check_command(cmd: str):
    """Check if a command is available."""
    try:
        result = subprocess.run(
            [cmd, "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return True, result.stdout.strip().split('\n')[0]
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False, "not found"


def main():
    print("=" * 60)
    print("LLM-Wiki Environment Verification")
    print("=" * 60)

    checks = []

    # Python version
    ok, msg = check_python_version()
    checks.append(("Python version", ok, msg))

    # Core dependencies
    for pkg, imp in [
        ("pyyaml", "yaml"),
        ("python-frontmatter", "frontmatter"),
        ("mkdocs", "mkdocs"),
        ("mkdocs-material", "material"),
    ]:
        ok, msg = check_package(pkg, imp)
        checks.append((f"Package: {pkg}", ok, msg))

    # Optional dependencies
    for pkg, imp in [
        ("pypdf", "pypdf"),
        ("whoosh", "whoosh"),
        ("pytest", "pytest"),
    ]:
        ok, msg = check_package(pkg, imp)
        checks.append((f"Optional: {pkg}", ok, msg))

    # External tools
    for cmd in ["qmd", "git"]:
        ok, msg = check_command(cmd)
        checks.append((f"Command: {cmd}", ok, msg))

    # Print results
    print()
    all_ok = True
    required_ok = True

    for name, ok, msg in checks:
        status = "✓" if ok else "✗"
        print(f"  {status} {name}: {msg}")
        if not ok:
            all_ok = False
            if "Optional" not in name and "qmd" not in name.lower():
                required_ok = False

    print()
    print("=" * 60)

    if required_ok:
        print("✓ All required dependencies satisfied")
        if not all_ok:
            print("  (Some optional dependencies missing - this is OK)")
        return 0
    else:
        print("✗ Missing required dependencies")
        print("  Run: pip install -e .")
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

**Run verification:**

```bash
python scripts/verify_env.py
```

**Expected output (minimal install):**

```
============================================================
LLM-Wiki Environment Verification
============================================================

  ✓ Python version: 3.11.5
  ✓ Package: pyyaml: installed
  ✓ Package: python-frontmatter: installed
  ✓ Package: mkdocs: installed
  ✓ Package: mkdocs-material: installed
  ✗ Optional: pypdf: not installed
  ✗ Optional: whoosh: not installed
  ✓ Optional: pytest: installed
  ✗ Command: qmd: not found
  ✓ Command: git: git version 2.43.0

============================================================
✓ All required dependencies satisfied
  (Some optional dependencies missing - this is OK)
```

---

#### 9.-1.6 QMD and OMEGA Alternatives

Since QMD and OMEGA are referenced but may not exist as real packages, here are concrete alternatives:

**Search Alternatives (instead of QMD):**

| Option | Pros | Cons | Install |
|--------|------|------|---------|
| **grep fallback** | Zero deps, always works | No ranking, slow on large wikis | Built-in |
| **Whoosh** | Pure Python, good BM25 | No vectors, Python-only | `pip install whoosh` |
| **SQLite FTS5** | Built into Python, fast | No semantic search | Built-in |
| **Tantivy** | Rust-based, very fast | Requires compilation | `pip install tantivy` |
| **LanceDB** | Vector + keyword, local | Newer, less tested | `pip install lancedb` |

**Recommendation:** Start with grep fallback, add Whoosh when search becomes slow.

**Session Memory Alternatives (instead of OMEGA):**

| Option | Pros | Cons | Install |
|--------|------|------|---------|
| **Skip entirely** | Simplest, wiki works fine | No session context | None |
| **SQLite directly** | Built-in, simple | Manual schema management | Built-in |
| **TinyDB** | JSON-based, simple API | Not concurrent-safe | `pip install tinydb` |
| **LMDB** | Fast, ACID | Lower-level API | `pip install lmdb` |

**Recommendation:** Skip session memory for MVP. Add SQLite-based session context later if needed.

---

#### 9.-1.7 Deliverables Checklist

- [ ] Conda/venv environment created and activated
- [ ] `pyproject.toml` created with dependencies
- [ ] Core packages installed (`pip install -e .`)
- [ ] `mkdocs.yml` created with wiki configuration
- [ ] `mkdocs serve` runs successfully
- [ ] `src/llm_wiki/` package structure created
- [ ] `scripts/verify_env.py` created and passes
- [ ] Git repository initialized (if not already)
- [ ] `.gitignore` updated for Python/wiki artifacts

**`.gitignore` additions:**

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
.venv/
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/

# LLM-Wiki specific
logs/
*.log
.wiki-lock
.wiki-shadow/
.wiki-old/
manifest.wal
jobs.jsonl

# MkDocs build output
site/

# Keep these (don't ignore)
# wiki/
# raw/
# manifest.jsonl
# schema.yml
# mkdocs.yml
```

---

#### 9.-1.8 Wiki Viewer (MkDocs)

MkDocs is the default viewer for browsing the wiki in your browser. It converts the markdown files into a navigable website with search, navigation, and clean formatting.

**Configuration file `mkdocs.yml`:**

```yaml
# MkDocs configuration for LLM Wiki
site_name: My Research Wiki
site_description: LLM-maintained personal knowledge base
site_url: http://127.0.0.1:8000

# Wiki content directory
docs_dir: wiki

# Build output (gitignored)
site_dir: site

# Theme configuration
theme:
  name: material
  palette:
    # Light mode
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    # Dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.instant      # Fast page loads
    - navigation.tracking     # URL updates with scroll
    - navigation.sections     # Collapsible sections
    - navigation.expand       # Expand all by default
    - navigation.indexes      # Section index pages
    - search.suggest          # Search suggestions
    - search.highlight        # Highlight search terms
    - content.code.copy       # Copy button on code blocks
    - toc.follow              # TOC follows scroll

# Plugins
plugins:
  - search:
      lang: en
  # Uncomment if you want tags support:
  # - tags

# Markdown extensions
markdown_extensions:
  - toc:
      permalink: true         # Anchor links on headings
  - tables                    # Markdown tables
  - fenced_code               # Code blocks with ```
  - attr_list                 # Add attributes to elements
  - md_in_html                # Markdown inside HTML
  - admonition                # Note/warning/tip boxes
  - pymdownx.details          # Collapsible details
  - pymdownx.superfences      # Better code blocks
  - pymdownx.highlight:       # Syntax highlighting
      anchor_linenums: true
  - pymdownx.tasklist:        # Task lists with checkboxes
      custom_checkbox: true
  - wikilinks                 # Support [[wikilinks]]

# Navigation structure (auto-generated from wiki/ folder)
# MkDocs will auto-discover pages. For custom ordering, define nav: here.
# Example:
# nav:
#   - Home: index.md
#   - Sources: sources/
#   - Entities: entities/
#   - Concepts: concepts/
#   - Analyses: analyses/

# Extra configuration
extra:
  social: []  # Add social links if desired
  generator: false  # Hide "Made with MkDocs"
```

**Usage commands:**

```bash
# Serve wiki locally (live reload on changes)
mkdocs serve

# Opens at http://127.0.0.1:8000
# Changes to wiki/ files auto-refresh the browser

# Build static HTML (for sharing/hosting)
mkdocs build

# Output goes to site/ directory
# Can be hosted on GitHub Pages, Netlify, etc.

# Serve on different port
mkdocs serve -a 127.0.0.1:8080

# Serve accessible from network (e.g., view on phone)
mkdocs serve -a 0.0.0.0:8000
```

**What you see in the browser:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 🔍 Search...                                    My Research Wiki    🌙  │
├───────────────────┬─────────────────────────────────────────────────────┤
│                   │                                                     │
│ 📁 Sources        │  # Attention Mechanism                              │
│   └─ vaswani2017  │                                                     │
│   └─ bert2018     │  Self-attention computes relevance weights over     │
│                   │  all input positions, enabling the model to focus   │
│ 📁 Entities       │  on relevant parts of the input sequence.           │
│   └─ google-brain │                                                     │
│   └─ ashish-v...  │  ## Key Properties                                  │
│                   │                                                     │
│ 📁 Concepts       │  - O(n²) complexity with sequence length            │
│   └─ attention  ◀─│  - Fully parallelizable (unlike RNNs)               │
│   └─ transformer  │  - No inherent notion of position                   │
│   └─ self-attn    │                                                     │
│                   │  ## Related Concepts                                │
│ 📁 Analyses       │                                                     │
│   └─ scaling...   │  - [[transformer-architecture]]                     │
│                   │  - [[multi-head-attention]]                         │
│ 📁 Contradictions │                                                     │
│   └─ scaling-...  │  > **Note:** See [[contradictions/scaling-debate]]  │
│                   │  > for discussion of complexity trade-offs.         │
│                   │                                                     │
└───────────────────┴─────────────────────────────────────────────────────┘
```

**Features you get:**

| Feature | How it works |
|---------|--------------|
| **Search** | Press `/` or click search box. Searches all pages instantly. |
| **Dark mode** | Toggle in top-right corner |
| **Navigation** | Sidebar shows all pages organized by folder |
| **Wikilinks** | `[[page-name]]` becomes clickable links |
| **Live reload** | Edit a file, browser updates automatically |
| **Mobile friendly** | Responsive design works on phone/tablet |
| **Code highlighting** | Syntax highlighting for code blocks |
| **Table of contents** | Right sidebar shows headings in current page |

**Wikilinks plugin:**

By default, MkDocs doesn't understand `[[wikilinks]]`. The config above includes the `wikilinks` extension. For full Obsidian-style links, install:

```bash
pip install mkdocs-roamlinks-plugin
```

Then add to `mkdocs.yml`:

```yaml
plugins:
  - search
  - roamlinks  # Converts [[wikilinks]] to proper links
```

**Update deliverables checklist:**

- [ ] `mkdocs.yml` created
- [ ] `mkdocs serve` runs and shows wiki
- [ ] Navigation works between pages
- [ ] Search works

---

### Phase 0: Bootstrap Validation

**Goal:** Verify Claude Code can execute required file operations before writing any implementation code.

**Duration:** 30 minutes

**Tests to run manually:**

```bash
# Test 1: Create directory
mkdir -p test_bootstrap/wiki/sources

# Test 2: Write markdown with frontmatter
cat > test_bootstrap/wiki/sources/test.md << 'EOF'
---
title: Test Page
created: 2024-01-15
revision_id: 1
---

# Test Page

This is a test page with [[wikilinks]].
EOF

# Test 3: Append to JSONL
echo '{"op_id": "op_001", "op_type": "test", "status": "completed"}' >> test_bootstrap/manifest.jsonl

# Test 4: Read and verify
cat test_bootstrap/wiki/sources/test.md
cat test_bootstrap/manifest.jsonl

# Test 5: Compute hash
sha256sum test_bootstrap/wiki/sources/test.md

# Test 6: Atomic rename
echo "new content" > test_bootstrap/wiki/sources/test.md.tmp
mv test_bootstrap/wiki/sources/test.md.tmp test_bootstrap/wiki/sources/test.md

# Cleanup
rm -rf test_bootstrap
```

**Validation criteria:**

- [ ] All 6 tests execute without error
- [ ] File contents are correct when read back
- [ ] JSONL append works (file grows, not overwritten)
- [ ] Atomic rename works

**If any test fails:** Stop and debug before proceeding. The entire implementation depends on these primitives.

---

### Phase 1: Canonical Core

**Goal:** Working wiki with Tier 1 fully specified.

**Deliverables:**
- [ ] Page schemas (frontmatter, revision tracking)
- [ ] Manifest schema and append logic
- [ ] schema.yml configuration
- [ ] `/wiki:init` (creates Tier 1 structure)
- [ ] `/wiki:ingest` (writes canonical pages with revisions)
- [ ] Invariant verification for Tier 1

**Validation:**
- Can create wiki with proper revision tracking
- Manifest records all operations
- revision_hash matches content

**No dependencies on:** QMD, OMEGA, derived artifacts

---

### Phase 2: Derived Artifacts

**Goal:** Automatic generation of Tier 2.

**Deliverables:**
- [ ] `compile_mind_map()` algorithm
- [ ] `compile_index()` algorithm
- [ ] Generation headers with metadata
- [ ] `/wiki:rebuild` skill
- [ ] Freshness tracking (stale detection)

**Validation:**
- MIND_MAP is deterministic (same input → same output)
- index.md is deterministic
- Rebuild produces identical artifacts

**Dependencies:** Phase 1

---

### Phase 3: Search Integration

**Goal:** QMD provides search over wiki.

**Deliverables:**
- [ ] QMD setup in `/wiki:init`
- [ ] Context configuration from schema.yml
- [ ] `/wiki:query` using QMD search
- [ ] `/wiki:rebuild` includes QMD reindex
- [ ] Freshness tracking for QMD

**Validation:**
- QMD search returns relevant wiki pages
- Rebuild recreates functional search index

**Dependencies:** Phase 2

---

### Phase 4: Session Context

**Goal:** OMEGA provides session continuity.

**Deliverables:**
- [ ] OMEGA integration (ephemeral only)
- [ ] Session start context
- [ ] Navigation logging
- [ ] Clear tier separation (OMEGA is Tier 3)

**Validation:**
- Session context helps but isn't required
- Deleting OMEGA doesn't affect wiki functionality

**Dependencies:** Phase 3

---

### Phase 5: Verification & Hardening

**Goal:** Full test suite and recovery procedures.

**Deliverables:**
- [ ] Tier 1 verification tests
- [ ] Tier 2 determinism tests
- [ ] Tier 3 ephemerality tests
- [ ] Disaster recovery procedure
- [ ] `/wiki:verify` command suite

**Validation:**
- All invariants verified
- Recovery from backup works
- Graceful degradation works

---

## 10. Test Suite

### 10.1 Tier 1 Sufficiency Test

```python
def test_tier1_sufficiency():
    """
    Test: Tier 1 alone is sufficient to rebuild everything.

    This is THE critical test for the architecture.
    If this fails, something canonical is in the wrong tier.
    """
    # Setup: Create wiki with content
    wiki = create_test_wiki()
    ingest_sources(wiki, ["paper1.pdf", "paper2.pdf", "paper3.pdf"])

    # Capture Tier 1
    tier1_backup = {
        "wiki": copy_directory(wiki.wiki_path),
        "manifest": copy_file(wiki.manifest_path),
        "schema": copy_file(wiki.schema_path),
        "raw": copy_directory(wiki.raw_path)
    }

    # Delete ALL derived and ephemeral data
    delete_file(wiki.mind_map_path)      # Tier 2
    delete_file(wiki.index_path)          # Tier 2
    delete_directory("~/.cache/qmd/")     # Tier 2
    delete_directory("~/.omega/")         # Tier 3

    # Restore only Tier 1
    restore_from_backup(tier1_backup)

    # Rebuild derived
    wiki.rebuild_derived()

    # Verify: ALL functionality works
    assert wiki.can_query("attention mechanisms")
    assert wiki.can_ingest("paper4.pdf")
    assert wiki.can_lint()
    assert wiki.verify_invariants() == []

    # Verify: Content is correct
    assert wiki.page_count() == expected_page_count
    assert wiki.mind_map_node_count() == expected_node_count
```

### 10.2 Tier 2 Determinism Test

```python
def test_tier2_determinism():
    """
    Test: Tier 2 artifacts are deterministic.

    Same Tier 1 input → identical Tier 2 output (excluding timestamps).
    """
    wiki = create_test_wiki()
    ingest_sources(wiki, ["paper1.pdf", "paper2.pdf"])

    # Generate MIND_MAP twice
    wiki.rebuild_mind_map()
    mind_map_1 = read_file(wiki.mind_map_path)
    content_hash_1 = compute_content_hash(mind_map_1)  # Excludes timestamps

    # Delete and regenerate
    delete_file(wiki.mind_map_path)
    wiki.rebuild_mind_map()
    mind_map_2 = read_file(wiki.mind_map_path)
    content_hash_2 = compute_content_hash(mind_map_2)

    # Must be identical
    assert content_hash_1 == content_hash_2

    # Same for index.md
    wiki.rebuild_index()
    index_hash_1 = compute_content_hash(read_file(wiki.index_path))
    delete_file(wiki.index_path)
    wiki.rebuild_index()
    index_hash_2 = compute_content_hash(read_file(wiki.index_path))

    assert index_hash_1 == index_hash_2
```

### 10.3 Tier 3 Ephemerality Test

```python
def test_tier3_ephemerality():
    """
    Test: Tier 3 can be deleted without data loss.

    Wiki must be fully functional with empty OMEGA.
    """
    wiki = create_test_wiki()
    ingest_sources(wiki, ["paper1.pdf", "paper2.pdf"])

    # Use OMEGA for session context
    omega_store("Working on attention scaling research")
    omega_store("Noted contradiction between paper1 and paper2")

    # Verify OMEGA has content
    memories = omega_query("attention")
    assert len(memories) > 0

    # DELETE OMEGA ENTIRELY
    delete_directory("~/.omega/")

    # Wiki MUST still work
    assert wiki.can_query("attention mechanisms")
    assert wiki.can_ingest("paper3.pdf")
    assert wiki.can_lint()

    # Verify invariants still hold
    violations = wiki.verify_invariants()
    assert violations == []

    # OMEGA is empty (expected)
    memories_after = omega_query("attention")
    assert len(memories_after) == 0  # Fresh start, no data loss
```

### 10.4 Revision Integrity Test

```python
def test_revision_integrity():
    """
    Test: Revision tracking is consistent.
    """
    wiki = create_test_wiki()

    # Create page
    wiki.ingest("paper1.pdf")
    page = wiki.read_page("sources/paper1")
    assert page.revision_id == 1
    assert page.revision_hash == compute_hash(page.body)

    # Update page
    wiki.update_page("sources/paper1", new_content="Updated content")
    page = wiki.read_page("sources/paper1")
    assert page.revision_id == 2  # Incremented
    assert page.revision_hash == compute_hash(page.body)  # Recomputed
    assert page.updated_by in wiki.manifest.op_ids  # Valid reference

    # Verify hash matches
    recomputed_hash = compute_hash(page.body)
    assert page.revision_hash == recomputed_hash
```

### 10.5 Manifest Replayability Test

```python
def test_manifest_replayability():
    """
    Test: Wiki can be rebuilt by replaying manifest from empty state.

    Given: raw/ sources + manifest.jsonl
    Can you: Rebuild wiki/ entirely?
    """
    # Create wiki and record operations
    wiki = create_test_wiki()
    ingest_sources(wiki, ["paper1.pdf", "paper2.pdf", "paper3.pdf"])
    wiki.query("attention mechanisms", save_answer=True)

    # Capture final state
    final_page_count = wiki.page_count()
    final_page_hashes = {p.page_id: p.revision_hash for p in wiki.pages()}

    # Delete wiki/ but keep manifest and raw/
    manifest_backup = copy_file(wiki.manifest_path)
    raw_backup = copy_directory(wiki.raw_path)
    delete_directory(wiki.wiki_path)

    # Replay manifest
    wiki = create_empty_wiki()
    restore_file(manifest_backup, wiki.manifest_path)
    restore_directory(raw_backup, wiki.raw_path)
    wiki.replay_manifest()

    # Verify identical state
    assert wiki.page_count() == final_page_count
    for page in wiki.pages():
        assert page.revision_hash == final_page_hashes[page.page_id]
```

---

## Appendix A: Glossary

| Term | Definition |
|------|------------|
| **Canonical** | Authoritative source of truth; if lost, data is lost |
| **Derived** | Computed from canonical data; can be regenerated |
| **Ephemeral** | Temporary; can be discarded without data loss |
| **Tier 1** | Canonical data: wiki/*.md + manifest.jsonl |
| **Tier 2** | Derived artifacts: MIND_MAP, index, QMD index |
| **Tier 3** | Ephemeral context: OMEGA memories, temp files |
| **Revision** | A specific version of a page (revision_id + revision_hash) |
| **Manifest** | Append-only operation ledger (manifest.jsonl) |
| **Invariant** | Property that must always be true |

---

## Appendix B: Quick Reference

### Tier Classification Cheat Sheet

```
Is it domain knowledge?
├── YES → Tier 1 (wiki/*.md)
└── NO
    ├── Is it computed from domain knowledge?
    │   ├── YES → Tier 2 (derived, rebuildable)
    │   └── NO → Tier 3 (ephemeral, discardable)
```

### Critical Test

```
Given: wiki/ + manifest.jsonl + raw/ (Tier 1)
Delete: MIND_MAP, index.md, QMD index, OMEGA (Tier 2+3)
Run: /wiki:rebuild
Result: Full functionality restored?
        YES → Architecture is correct
        NO  → Something canonical is in wrong tier
```

### Recovery Commands

```bash
# Full rebuild from Tier 1
/wiki:rebuild all

# Verify integrity
/wiki:verify tier1

# Check system health
/wiki:doctor

# Generate health report
/wiki:lint
```

---

*Document version: 2.0*
*Last updated: 2024-01-15*
*Architecture: Markdown as Single Source of Truth*
