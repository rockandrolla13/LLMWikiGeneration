---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:ef92717f0fca8b358be11d86a7b93c23a296a5f0c93075411b008846782731b2
created: '2026-11-21T02:00:24Z'
page_id: concepts/swiglu
page_type: concept
related:
- concepts/transformers
- concepts/rmsnorm
- concepts/rotary-position-embeddings
revision_id: 1
schema_version: 2
sources:
- sources/liu-2025-build-fine-tune-small-language-model
tags: []
title: SwiGLU
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: e338474a-9b3c-5a5e-8578-a8fc78e35692
---

<!-- AUTHORED REGION START -->
# SwiGLU

## Definition

SwiGLU is a gated feed-forward layer for transformer blocks. One linear projection passes through the Swish activation and gates a second linear projection elementwise, and a third projection maps the result back to the model width. Liu writes the gate as SwiGLU(x) = Swish(W1·x) ⊗ (W2·x).

## In Liu (2025)

The English MiniMind model in Ch 8 uses SwiGLU feed-forward blocks instead of the GELU blocks of GPT-2, with the hidden size rounded to a multiple of 64. The book states that PaLM and LLaMA use SwiGLU and calls it better than ReLU or GELU without measuring this.

## Sources

- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model: A Step-by-Step Guide for Beginners, Researchers, and Non-Programmers]]

## Related Concepts

- [[concepts/transformers|Transformers]]
- [[concepts/rmsnorm|RMSNorm]]
- [[concepts/rotary-position-embeddings|Rotary Position Embeddings (RoPE)]]
<!-- AUTHORED REGION END -->