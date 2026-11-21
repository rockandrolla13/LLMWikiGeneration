---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:450136782a4cc49c82d9bb9dfbd9e47edb3b700b0e5db91e3f61a1381558abc3
created: '2026-11-21T02:00:24Z'
page_id: concepts/rmsnorm
page_type: concept
related:
- concepts/layer-normalization
- concepts/transformers
- concepts/swiglu
revision_id: 1
schema_version: 2
sources:
- sources/liu-2025-build-fine-tune-small-language-model
tags: []
title: RMSNorm
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 1026b4e5-4842-5e28-91e1-5217cca2adb4
---

<!-- AUTHORED REGION START -->
# RMSNorm

## Definition

RMSNorm normalizes each activation vector by its root mean square, then multiplies by a learned scale: y = x / sqrt(mean(x²) + ε) × weight. Unlike layer normalization it does not subtract the mean and has no bias term.

## In Liu (2025)

The English MiniMind model in Ch 8 uses RMSNorm in place of the LayerNorm used in the GPT-2-style chapters. The book calls it simpler and more stable than LayerNorm but does not measure the difference.

## Sources

- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model: A Step-by-Step Guide for Beginners, Researchers, and Non-Programmers]]

## Related Concepts

- [[concepts/layer-normalization|Layer Normalization]]
- [[concepts/transformers|Transformers]]
- [[concepts/swiglu|SwiGLU]]
<!-- AUTHORED REGION END -->