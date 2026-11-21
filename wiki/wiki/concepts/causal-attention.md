---
content_hash: sha256:61bf1c31fc8d2bb87b120c23a0d3e3bcfcd73316eb57f51f51529f620cc452bc
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/causal-attention
page_type: concept
related:
- concepts/self-attention
- concepts/transformers
revision_id: 2
schema_version: 2
sources:
- sources/raschka-2024-build-llm-from-scratch
- sources/liu-2025-build-fine-tune-small-language-model
tags:
- ai-engineering
- self-attention
- transformers
title: Causal Attention
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 118bac1e-bddf-5bf3-a477-34af50b2b597
---

<!-- AUTHORED REGION START -->
# Causal Attention

## Definition

A masked variant of self-attention used in autoregressive decoders that zeroes out attention to future positions (typically via an upper-triangular mask before softmax) so each token can only attend to itself and prior tokens, enabling next-token prediction without information leakage.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]
- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025): Ch 2 implements the causal mask in a character-level GPT.

## Related Concepts

- [[concepts/self-attention]]
- [[concepts/transformers]]

<!-- AUTHORED REGION END -->