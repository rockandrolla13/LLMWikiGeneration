---
content_hash: sha256:e9f386df71469076798184a1458ecc2c490a2c79f003b6b068349d151e235c6c
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/positional-embeddings
page_type: concept
related:
- concepts/self-attention
- concepts/transformers
- concepts/rotary-position-embeddings
revision_id: 2
schema_version: 2
sources:
- sources/raschka-2024-build-llm-from-scratch
- sources/liu-2025-build-fine-tune-small-language-model
tags:
- ai-engineering
- self-attention
- transformers
title: Positional Embeddings
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 053c8b8c-fa22-50d1-bf75-9e5b46b8c34d
---

<!-- AUTHORED REGION START -->
# Positional Embeddings

## Definition

Vectors added to token embeddings to encode token order, since self-attention is permutation-invariant. Raschka builds absolute learned positional embeddings (GPT-2 style) of the same dimensionality as the token embeddings and sums them element-wise before the first transformer block.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]
- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025): Uses learned position embeddings in Ch 2-7 and replaces them with [[concepts/rotary-position-embeddings|RoPE]] in Ch 8.

## Related Concepts

- [[concepts/self-attention]]
- [[concepts/transformers]]

<!-- AUTHORED REGION END -->