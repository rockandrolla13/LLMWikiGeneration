---
content_hash: sha256:58f1407ab5325dabc529e6485729d1eabfcd30c7271f15fee356209bef1b53b9
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/model-compression
page_type: concept
related:
- contradictions/int8-quantization-speedup-small-models
- concepts/small-language-models
revision_id: 2
schema_version: 2
sources:
- sources/huyen-2022-designing-ml-systems
- sources/liu-2025-build-fine-tune-small-language-model
tags:
- ai-engineering
title: Model Compression
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 7fcd694c-37d0-5eff-ae75-a4b3cd95ccbd
---

<!-- AUTHORED REGION START -->
# Model Compression

## Definition

Methods for reducing model size and inference cost without major accuracy loss, including low-rank factorization, knowledge distillation, pruning, and quantization, typically motivated by edge deployment or strict latency budgets.

## Sources

- [[sources/huyen-2022-designing-ml-systems|Designing Machine Learning Systems]]
- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025): Ch 11 surveys quantization, pruning and distillation. Its own INT8 benchmark showed a slowdown (see [[contradictions/int8-quantization-speedup-small-models|the contradiction page]]).

<!-- AUTHORED REGION END -->