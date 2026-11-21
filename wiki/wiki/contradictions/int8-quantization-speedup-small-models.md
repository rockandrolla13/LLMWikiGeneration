---
content_hash: sha256:6031bcbf68d744f67a5dbce5a253f6c643c360ee8bdf6fb1b6a39f44f0cf1ee6
created: '2026-11-21T02:00:24Z'
page_id: contradictions/int8-quantization-speedup-small-models
page_type: contradiction
related:
- concepts/inference-optimization
- concepts/model-compression
- concepts/small-language-models
- entities/llama-cpp
revision_id: 1
schema_version: 2
sources:
- sources/liu-2025-build-fine-tune-small-language-model
- sources/huyen-2025-ai-engineering
- sources/huyen-2022-designing-ml-systems
status: unresolved
tags:
- quantization
- inference-optimization
- small-language-models
title: Does INT8 Quantization Speed Up Small-Model Inference?
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 892009e2-cdb4-570a-b33e-e1e3f6dfe651
---

<!-- AUTHORED REGION START -->
# Does INT8 Quantization Speed Up Small-Model Inference?

**Status:** unresolved

## Claim A: INT8 quantization speeds up inference at little cost

The wiki's [[concepts/inference-optimization|Inference Optimization]] and [[concepts/model-compression|Model Compression]] pages list quantization as a way to cut latency and cost without major accuracy loss, drawing on [[sources/huyen-2025-ai-engineering|AI Engineering]] and [[sources/huyen-2022-designing-ml-systems|Designing Machine Learning Systems]]. Liu's own Ch 11 overview table agrees, claiming 4× smaller models, a 2-3× speedup and under 1% quality loss for INT8.

## Claim B: INT8 quantization made the model slower and worse

The Ch 11 benchmark in [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025) applies PyTorch dynamic INT8 quantization to the linear layers of a 109M MiniMind-style model. It reports 57.7 tokens/s for the FP32 model, 54.7 for the DPO model and 30.2 for the INT8 model, a 0.52× speed. Some INT8 outputs are visibly worse than the FP32 outputs on the same prompts.

## Where exactly they conflict

Both claims concern the same technique. Claim A is a general statement, and the book repeats it. Claim B is a single measured run in the same book that shows the opposite direction for speed and a quality loss larger than "under 1%".

## Points that bear on a resolution

These are editorial observations. The book does not offer them as a resolution.

- The book does not say which device ran the benchmark. Speedups from INT8 depend on hardware kernels, so the run may not generalize either way.
- Dynamic quantization quantizes activations at run time. For a small model generating one token at a time, that overhead may outweigh the savings. This is a hypothesis, not something the book tests.
- Claim A's sources discuss quantization in general, including weight-only and lower-bit formats served by dedicated runtimes such as llama.cpp, which Liu also covers.

## What would settle it

The same model benchmarked FP32 against INT8 on a stated CPU and GPU, with dynamic, static and GGUF quantization side by side and a quality metric such as perplexity. The wiki has no source that does this.
<!-- AUTHORED REGION END -->