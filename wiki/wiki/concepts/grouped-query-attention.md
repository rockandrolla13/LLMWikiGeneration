---
abstraction_level: advanced
concept_type: technique
content_hash: sha256:aa21833d6cb63784198b8b354ab33423459676aa4828b3e0bfc57e60e812faa5
created: '2026-11-21T02:00:24Z'
page_id: concepts/grouped-query-attention
page_type: concept
related:
- concepts/multi-head-attention
- concepts/self-attention
- concepts/rotary-position-embeddings
- concepts/inference-optimization
- sources/alammar-2024-hands-on-llm
revision_id: 1
schema_version: 2
sources:
- sources/liu-2025-build-fine-tune-small-language-model
tags: []
title: Grouped-Query Attention
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: f2f18c64-5100-5bfd-9098-29ec3e2059db
---

<!-- AUTHORED REGION START -->
# Grouped-Query Attention

## Definition

Grouped-query attention (GQA) is a variant of multi-head attention in which several query heads share one key-value head. Fewer key-value heads than query heads shrink the KV cache and speed up inference, with little loss of accuracy.

## In Liu (2025)

The 109M English MiniMind model in Ch 8 uses 16 query heads and 8 key-value heads. The code repeats each key-value head to match the query heads before computing attention. [[sources/alammar-2024-hands-on-llm|Hands-On Large Language Models]] also covers GQA.

## Sources

- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model: A Step-by-Step Guide for Beginners, Researchers, and Non-Programmers]]

## Related Concepts

- [[concepts/multi-head-attention|Multi-Head Attention]]
- [[concepts/self-attention|Self-Attention]]
- [[concepts/rotary-position-embeddings|Rotary Position Embeddings (RoPE)]]
- [[concepts/inference-optimization|Inference Optimization]]
<!-- AUTHORED REGION END -->