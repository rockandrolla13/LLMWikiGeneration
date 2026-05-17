---
title: Low-Rank Adaptation
page_id: concepts/low-rank-adaptation
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
- transformers
sources:
- sources/raschka-2024-build-llm-from-scratch
related:
- concepts/transformers
mind_map_priority: medium
revision_hash: sha256:af2cfd9120201933
---

# Low-Rank Adaptation

## Definition

A parameter-efficient fine-tuning method (LoRA, Hu et al. 2021) that freezes the pretrained weights and injects trainable low-rank matrices (W = W0 + BA, where B and A are much smaller than W) into selected linear layers. Drastically reduces trainable parameters and memory while matching full fine-tuning quality.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]

## Related Concepts

- [[concepts/transformers]]
