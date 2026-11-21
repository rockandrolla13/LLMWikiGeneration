---
content_hash: sha256:4b4e9362da455df95a730715c227b1f5861273d0e58385e1efce66c1fc47a7ef
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/multi-head-attention
page_type: concept
related:
- concepts/self-attention
- concepts/transformers
- concepts/grouped-query-attention
revision_id: 2
schema_version: 2
sources:
- sources/raschka-2024-build-llm-from-scratch
- sources/shabani-2022-multi-head-temporal-attention-augmented-bilinear
- sources/yang-2025-efficient-deep-learning-model-predict-stock
- sources/liu-2025-build-fine-tune-small-language-model
tags:
- ai-engineering
- self-attention
- transformers
title: Multi-Head Attention
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 83f3481a-3acc-56d8-823e-464be89f683f
---

<!-- AUTHORED REGION START -->
# Multi-Head Attention

## Definition

An extension of self-attention where the model runs several attention operations in parallel on different learned projections of the input, concatenates their outputs, and projects them back, allowing the network to attend to information from multiple representation subspaces simultaneously. Raschka contrasts a naive stacking implementation with an efficient weight-split version.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]
- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025): Ch 2 builds multi-head attention. Ch 8 switches to [[concepts/grouped-query-attention|grouped-query attention]].

## Related Concepts

- [[concepts/self-attention]]
- [[concepts/transformers]]

<!-- AUTHORED REGION END -->