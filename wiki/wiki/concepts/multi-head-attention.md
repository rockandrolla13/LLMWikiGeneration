---
title: Multi-Head Attention
page_id: concepts/multi-head-attention
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
revision_hash: sha256:c0302ab283504df9
---

# Multi-Head Attention

## Definition

An extension of self-attention where the model runs several attention operations in parallel on different learned projections of the input, concatenates their outputs, and projects them back, allowing the network to attend to information from multiple representation subspaces simultaneously. Raschka contrasts a naive stacking implementation with an efficient weight-split version.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]

## Related Concepts

- [[concepts/self-attention]]
- [[concepts/transformers]]
