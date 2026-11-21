---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:e7832a838694fdce8760dcb781770edcc3f8d15f90188f717501cde80cb6a2d2
created: '2026-11-21T02:00:24Z'
page_id: concepts/learning-rate-warmup-cosine-decay
page_type: concept
related:
- concepts/language-model-pretraining
- concepts/fine-tuning
revision_id: 1
schema_version: 2
sources:
- sources/liu-2025-build-fine-tune-small-language-model
tags: []
title: Learning-Rate Warmup and Cosine Decay
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 04d52628-5d56-5770-a483-4c324d9c62c9
---

<!-- AUTHORED REGION START -->
# Learning-Rate Warmup and Cosine Decay

## Definition

Warmup plus cosine decay is a learning-rate schedule for training neural networks. The rate rises linearly from near zero to a peak over the first warmup steps, then falls along a cosine curve to a floor by the end of training. Warmup avoids unstable early updates. The slow decay lets the model settle as training ends.

## In Liu (2025)

The Ch 6 production loop and the Ch 8 MiniMind pretraining both use this schedule, with a peak rate of 3e-4, a floor of 3e-5 (10% of the peak) and 2,000 warmup steps over 100,000 iterations. The book pairs it with gradient accumulation, gradient-norm clipping at 1.0 and AdamW weight decay that skips biases and norms.

## Sources

- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model: A Step-by-Step Guide for Beginners, Researchers, and Non-Programmers]]

## Related Concepts

- [[concepts/language-model-pretraining|Language Model Pretraining]]
- [[concepts/fine-tuning|Fine-Tuning]]
<!-- AUTHORED REGION END -->