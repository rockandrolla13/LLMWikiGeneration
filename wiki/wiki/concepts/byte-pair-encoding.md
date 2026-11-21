---
content_hash: sha256:2c58a1206ae9051d798f47179681f7b9c807f19503fd21282efcd6191a06a3c7
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/byte-pair-encoding
page_type: concept
related:
- concepts/transformers
revision_id: 2
schema_version: 2
sources:
- sources/raschka-2024-build-llm-from-scratch
- sources/liu-2025-build-fine-tune-small-language-model
tags:
- ai-engineering
- transformers
title: Byte Pair Encoding
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 19957008-6a51-5ade-a2fc-1534aef26481
---

<!-- AUTHORED REGION START -->
# Byte Pair Encoding

## Definition

A subword tokenization algorithm (used in GPT-2/3 via the tiktoken library) that iteratively merges the most frequent adjacent byte or character pairs into single tokens, producing a fixed-size vocabulary that gracefully handles out-of-vocabulary words by decomposing them into known subword units.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]
- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025): Demonstrates GPT-2's byte-level BPE and trains a 32,000-token ByteLevel BPE on OpenWebText (5.64 characters per token).

## Related Concepts

- [[concepts/transformers]]

<!-- AUTHORED REGION END -->