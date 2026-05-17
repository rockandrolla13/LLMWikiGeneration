---
title: Positional Embeddings
page_id: concepts/positional-embeddings
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
- self-attention
- transformers
sources:
- sources/raschka-2024-build-llm-from-scratch
related:
- concepts/self-attention
- concepts/transformers
mind_map_priority: medium
revision_hash: sha256:7b693345d3786df4
---

# Positional Embeddings

## Definition

Vectors added to token embeddings to encode token order, since self-attention is permutation-invariant. Raschka builds absolute learned positional embeddings (GPT-2 style) of the same dimensionality as the token embeddings and sums them element-wise before the first transformer block.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]

## Related Concepts

- [[concepts/self-attention]]
- [[concepts/transformers]]
