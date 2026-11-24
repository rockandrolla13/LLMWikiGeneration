---
content_hash: sha256:c264a12d4759ad19df30aaf56508d4f0c91fdbc76c3662d5a3bdca454c5df202
created: '2026-11-21T02:00:24Z'
entity_type: person
page_id: entities/andrej-karpathy
page_type: entity
related:
- concepts/llm-knowledge-bases
- entities/obsidian
- sources/karpathy-2026-llm-knowledge-bases-tweets
- concepts/autoresearch
- sources/karpathy-2026-autoresearch
revision_id: 3
schema_version: 2
sources:
- sources/liu-2025-build-fine-tune-small-language-model
- sources/karpathy-2026-llm-knowledge-bases-tweets
- sources/karpathy-2026-autoresearch
tags:
- researcher
title: Andrej Karpathy
updated: '2026-11-24T23:30:14Z'
updated_by: op_53f181d9343b
uuid: 551f33e7-9f6c-50b5-a8c2-762210db5737
---

<!-- AUTHORED REGION START -->
# Andrej Karpathy

## Notes

Author of the "Let's build GPT" lecture, nanoGPT and minGPT. Ch 2 of Liu (2025) re-implements his character-level GPT on the Tiny Shakespeare text from his char-rnn repository.

## Sources in This Wiki

- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025)
## On Notes and LLM Knowledge Bases

Switched his personal notes to Obsidian in February 2024 and keeps day-to-day notes in a single "append-and-review" note. In April 2026 he described "LLM Knowledge Bases": an LLM compiles a markdown wiki from a `raw/` folder of sources, answers questions against it and lints it, viewed in Obsidian. This wiki follows the same pattern. See [[sources/karpathy-2026-llm-knowledge-bases-tweets|Karpathy on Obsidian, Second Brains and LLM Knowledge Bases]] and [[concepts/llm-knowledge-bases|LLM Knowledge Bases]].
## Autoresearch

In March 2026 he published autoresearch, a minimal repository in which an AI agent tunes a single-GPU nanochat training script on its own while the human edits only a markdown instruction file. A two-day run found about 20 improvements that cut nanochat's "Time to GPT-2" by about 11%. See [[sources/karpathy-2026-autoresearch|Autoresearch (Karpathy, 2026)]] and [[concepts/autoresearch|Autoresearch]].
<!-- AUTHORED REGION END -->
