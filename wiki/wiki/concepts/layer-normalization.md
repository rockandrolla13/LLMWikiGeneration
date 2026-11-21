---
content_hash: sha256:2ef53b8ea41b4fed07689c6bf9b90edc737ee4ddcf2e65ec4e0619ae698efa3e
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/layer-normalization
page_type: concept
related:
- concepts/transformers
- concepts/rmsnorm
revision_id: 2
schema_version: 2
sources:
- sources/raschka-2024-build-llm-from-scratch
- sources/liu-2025-build-fine-tune-small-language-model
tags:
- ai-engineering
- transformers
title: Layer Normalization
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 942f27d5-964a-5992-b9e1-c7b8fdb446f4
---

<!-- AUTHORED REGION START -->
# Layer Normalization

## Definition

A normalization technique that rescales activations to zero mean and unit variance across the feature dimension per sample (independent of batch size), with learned scale and shift parameters. Used inside each transformer block to stabilize gradients and accelerate training of deep networks.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]
- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025): Uses pre-LayerNorm in the GPT-2-style chapters and replaces it with [[concepts/rmsnorm|RMSNorm]] in Ch 8.

## Related Concepts

- [[concepts/transformers]]

<!-- AUTHORED REGION END -->