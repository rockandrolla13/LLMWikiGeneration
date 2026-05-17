---
title: Causal Attention
page_id: concepts/causal-attention
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
revision_hash: sha256:4f4f972540f142fc
---

# Causal Attention

## Definition

A masked variant of self-attention used in autoregressive decoders that zeroes out attention to future positions (typically via an upper-triangular mask before softmax) so each token can only attend to itself and prior tokens, enabling next-token prediction without information leakage.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]

## Related Concepts

- [[concepts/self-attention]]
- [[concepts/transformers]]
