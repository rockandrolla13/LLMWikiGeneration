---
abstraction_level: advanced
concept_type: technique
content_hash: sha256:7c85fe6c32f73715fd4a845fdcb247f6594a5d4431a636a10dfbfb04b98bbfc0
created: '2026-11-21T02:00:24Z'
page_id: concepts/rotary-position-embeddings
page_type: concept
related:
- concepts/positional-embeddings
- concepts/self-attention
- concepts/grouped-query-attention
- concepts/transformers
- sources/alammar-2024-hands-on-llm
- concepts/swiglu
revision_id: 2
schema_version: 2
sources:
- sources/liu-2025-build-fine-tune-small-language-model
tags: []
title: Rotary Position Embeddings (RoPE)
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 8e9c407d-3e8e-5d75-9685-7bd37ae37516
---

<!-- AUTHORED REGION START -->
# Rotary Position Embeddings (RoPE)

## Definition

Rotary position embeddings (RoPE) encode token position by rotating query and key vectors inside attention, by angles that depend on position. Position then enters through the relative angle between a query and a key, so the model needs no learned position-embedding table.

## In Liu (2025)

The English MiniMind model in Ch 8 uses RoPE in place of the learned position embeddings of GPT-2. Its code precomputes complex rotation frequencies with a base θ of 10000. The book credits RoPE with better extrapolation to longer sequences but gives no measurement. [[sources/alammar-2024-hands-on-llm|Hands-On Large Language Models]] also covers RoPE.

## Sources

- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model: A Step-by-Step Guide for Beginners, Researchers, and Non-Programmers]]

## Related Concepts

- [[concepts/positional-embeddings|Positional Embeddings]]
- [[concepts/self-attention|Self-Attention]]
- [[concepts/grouped-query-attention|Grouped-Query Attention]]
- [[concepts/transformers|Transformers]]
<!-- AUTHORED REGION END -->