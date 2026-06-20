---
title: Byte Pair Encoding
page_id: concepts/byte-pair-encoding
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
- transformers
sources:
- sources/raschka-2024-build-llm-from-scratch
related:
- concepts/transformers
mind_map_priority: medium
revision_hash: sha256:5d1da1b0670b1c17
schema_version: 2
uuid: 19957008-6a51-5ade-a2fc-1534aef26481
content_hash: sha256:af77c251cd79f5c985c70af11a908ed90a3aa78562a518c4a8114e49b81f477e
---

<!-- AUTHORED REGION START -->
# Byte Pair Encoding

## Definition

A subword tokenization algorithm (used in GPT-2/3 via the tiktoken library) that iteratively merges the most frequent adjacent byte or character pairs into single tokens, producing a fixed-size vocabulary that gracefully handles out-of-vocabulary words by decomposing them into known subword units.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]

## Related Concepts

- [[concepts/transformers]]

<!-- AUTHORED REGION END -->
