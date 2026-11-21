---
content_hash: sha256:91c14ea10ad9801d0eb0abf58c068e6b86e6a7e05d6c3ed937f919c505130ece
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/low-rank-adaptation
page_type: concept
related:
- concepts/transformers
revision_id: 2
schema_version: 2
sources:
- sources/raschka-2024-build-llm-from-scratch
- sources/liu-2025-build-fine-tune-small-language-model
tags:
- ai-engineering
- transformers
title: Low-Rank Adaptation
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 44466d0b-7ada-5ae2-8366-c182cddb238d
---

<!-- AUTHORED REGION START -->
# Low-Rank Adaptation

## Definition

A parameter-efficient fine-tuning method (LoRA, Hu et al. 2021) that freezes the pretrained weights and injects trainable low-rank matrices (W = W0 + BA, where B and A are much smaller than W) into selected linear layers. Drastically reduces trainable parameters and memory while matching full fine-tuning quality.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]
- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025): Appendix B gives a LoRA cheat sheet (rank 8-16, alpha usually 2 × r). The LoRA chapters promised in the text do not appear.

## Related Concepts

- [[concepts/transformers]]

<!-- AUTHORED REGION END -->