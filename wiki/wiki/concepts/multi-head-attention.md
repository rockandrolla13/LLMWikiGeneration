---
content_hash: sha256:a3fb4bb011866f6da4341bdc2cb1fdad6c1d577bc97e1726f95116cc9bd074b6
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/multi-head-attention
page_type: concept
related:
- concepts/self-attention
- concepts/transformers
revision_id: 1
schema_version: 2
sources:
- sources/raschka-2024-build-llm-from-scratch
- sources/shabani-2022-multi-head-temporal-attention-augmented-bilinear
- sources/yang-2025-efficient-deep-learning-model-predict-stock
tags:
- ai-engineering
- self-attention
- transformers
title: Multi-Head Attention
updated: '2026-09-27T01:47:00Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
uuid: 83f3481a-3acc-56d8-823e-464be89f683f
---

<!-- AUTHORED REGION START -->
# Multi-Head Attention

## Definition

An extension of self-attention where the model runs several attention operations in parallel on different learned projections of the input, concatenates their outputs, and projects them back, allowing the network to attend to information from multiple representation subspaces simultaneously. Raschka contrasts a naive stacking implementation with an efficient weight-split version.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]

## Related Concepts

- [[concepts/self-attention]]
- [[concepts/transformers]]

<!-- AUTHORED REGION END -->