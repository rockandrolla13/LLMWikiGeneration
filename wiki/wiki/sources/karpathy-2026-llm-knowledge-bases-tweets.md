---
authors:
- Andrej Karpathy
content_hash: sha256:e8883b9677f6c771ea51a305b5e07027b515f312df7ef9e03a4c5c3a593b7b6c
created: '2026-11-23T14:43:11Z'
mind_map_priority: high
page_id: sources/karpathy-2026-llm-knowledge-bases-tweets
page_type: source
publication_date: '2026-04-02'
publication_venue: X (Twitter), @karpathy
raw_location: raw/karpathy-tweets/
related:
- concepts/llm-knowledge-bases
- concepts/file-over-app
- concepts/llm-memory
- concepts/retrieval-augmented-generation
- concepts/continual-learning
- concepts/context-window
- entities/andrej-karpathy
- entities/obsidian
- entities/chatgpt
revision_id: 1
schema_version: 2
source_hash: sha256:b3ee38287a433ce4dc4e444d966497be78a1379cef0f8343a061c4d6a9ed5c1f
source_path: raw/karpathy-tweets/obsidian-second-brain.md
source_type: notes
source_url: https://x.com/karpathy
sources: []
tags:
- llm-knowledge-bases
- obsidian
- personal-knowledge-management
- andrej-karpathy
title: Karpathy on Obsidian, Second Brains and LLM Knowledge Bases
updated: '2026-11-23T14:43:11Z'
updated_by: op_5c91b297008c
uuid: 477c07a1-ac0f-5974-9cfd-a00429b72312
---

<!-- AUTHORED REGION START -->
# Karpathy on Obsidian, Second Brains and LLM Knowledge Bases

**Author:** Andrej Karpathy · **Dates:** 2024-02-24 to 2026-10-02 · **Type:** curated tweets (notes) · **Original:** [x.com/karpathy](https://x.com/karpathy), one link per tweet in the raw file

## Summary

A curated set of Karpathy's tweets on Obsidian, note taking, reading with LLMs and what he calls "LLM Knowledge Bases". In February 2024 he switched his personal notes to Obsidian and praised it less as a notes app than as a philosophy of software: plain markdown files on your own disk, composable with any tool, no lock-in. By 2025 he used Obsidian mainly for concrete projects and kept day-to-day notes in a single Apple Notes "append-and-review" note. In April 2026 he described the pattern that this wiki also follows: index source documents into a `raw/` directory, have an LLM incrementally "compile" a markdown wiki with summaries, concept articles and backlinks, view it in Obsidian, ask the LLM agent questions against it, file the answers back into the wiki, and run LLM "health checks" to lint it. He then argued that this kind of explicit, file-based memory is a better route to personalization than an AI that silently learns about you. The phrase "second brain" never appears in his tweets.

## Key Ideas

1. Obsidian matters because notes are plain-text markdown files on your own disk. The app is "UI/UX sugar" over files you control (2024-02-24).
2. "File over app": data in universal formats outlives any program and works with any tool, including the whole Unix toolkit an agent can use (2024-02-24, 2026-04-04).
3. LLM Knowledge Bases: sources go into `raw/`, an LLM compiles a `.md` wiki with summaries, concepts and backlinks, and the human rarely edits the wiki directly (2026-04-02).
4. `raw/` is authoritative and kept separate. The derived wiki keeps backlinks to the original content (2026-04-02).
5. At small scale no "fancy RAG" was needed: the LLM maintained index files and brief summaries and read the related data directly (2026-04-02).
6. Outputs (markdown, Marp slides, plots) are filed back into the wiki, so queries "add up" (2026-04-02).
7. Linting with LLM "health checks" finds inconsistent data, imputes missing data and suggests new article candidates (2026-04-02).
8. The process is human-in-the-loop: he adds every source by hand, and the schema lives in an `AGENTS.md` file (2026-04-02).
9. An explicit wiki is a better memory artifact than implicit personalization: it is inspectable, yours, in universal formats, and usable with any AI ("BYOAI") (2026-04-04).
10. It lets you skip writing but not reading and thinking (2026-04-06).
11. Read with LLMs in passes: read manually, then ask for an explanation or summary, then Q&A. Use epub, not pdf, and work chapter by chapter (2025-11-18, 2026-01-11).
12. Day-to-day notes go in one "append-and-review" note: append at the top, review by scrolling down, rescue items back to the top (2025-03-19).

## Notable Claims

- His research wiki reached about ~100 articles and ~400K words, and at that size the LLM handled Q&A without a retrieval system (2026-04-02).
- PDF conversion is the weak link: he found converters "equally terrible" for anything but simple documents and thought it may need to be a Skill run by a strong LLM rather than a program (2026-04-09).
- Some "slop leaks through in the concept space", and it gets harder to spot as the wiki grows (2026-05-01).
- Products built on opaque binary formats with no scripting are at risk in an era of human and AI collaboration. Obsidian, VS Code, Figma and Jupyter are low risk because they are already text (2025-06-04).
- A natural next step is synthetic data and fine-tuning so an LLM "knows" the wiki in its weights, not just its context window (2026-04-02, 2026-04-04).
- He prefers putting whole documents in the context window over RAG, for example when judging NotebookLM (2025-10-01).

## Quotes

> I think there is room here for an incredible new product instead of a hacky collection of scripts.

> The core idea is that this lets you skip writing but it doesn't let you skip reading and thinking.

## How This Wiki Relates

This repository implements the same pattern. Sources sit under `raw/`, the LLM compiles pages under `wiki/wiki/` (sources, concepts, entities, analyses, contradictions), the vault is opened in Obsidian, and `verify_wiki` plays the role of his "health checks". Two differences: this wiki keeps a hand-curated `MIND_MAP.md` as a routing layer on top of the index, and it uses BM25 search rather than relying only on index files. His warning about concept-space slop matches this wiki's numeric-provenance checks.

## Concepts

- [[concepts/llm-knowledge-bases|LLM Knowledge Bases]]
- [[concepts/file-over-app|File Over App]]
- [[concepts/llm-memory|LLM Memory]]
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[concepts/continual-learning|Continual Learning]]
- [[concepts/context-window|Context Window]]

## Entities

- [[entities/andrej-karpathy|Andrej Karpathy]]
- [[entities/obsidian|Obsidian]]
- [[entities/chatgpt|ChatGPT]]

## Notes on the Source Text

- Curated from a corpus of his latest 1,000 tweets collected on 2026-11-23 (`raw/karpathy-tweets/`), plus two Obsidian tweets from 2024-02-24 and two late-2024 tweets outside that window.
- An X search for `from:karpathy "second brain"` returned no results. His own terms are "LLM Knowledge Bases", "Wiki LLM" and personal wiki.
- Several 2026-04-02 items are replies within his own thread, but the collector labelled them "post" because X did not show a "Replying to" line.
- The "idea file" version of the April 2026 post is a GitHub gist. Its link is shortened in the tweet text and was not fetched.

## Source

`raw/karpathy-tweets/obsidian-second-brain.md`
<!-- AUTHORED REGION END -->
