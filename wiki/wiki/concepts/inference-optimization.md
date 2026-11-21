---
content_hash: sha256:fc4ad4e1e04e6ffe0ce3022b9401a6f859e9b7531381e8503e07c03614254449
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/inference-optimization
page_type: concept
related:
- contradictions/int8-quantization-speedup-small-models
- concepts/small-language-models
- concepts/grouped-query-attention
revision_id: 3
schema_version: 2
sources:
- sources/huyen-2025-ai-engineering
- sources/aryan-2025-llmops
- sources/liu-2025-build-fine-tune-small-language-model
tags:
- ai-engineering
title: Inference Optimization
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: a7dcc9d0-4007-57c8-b359-8e7f9ba0747b
---

<!-- AUTHORED REGION START -->
# Inference Optimization

## Definition

Techniques for reducing the latency, cost, and resource footprint of foundation-model serving — including quantisation, batching, KV-caching, speculative decoding, model and service-level optimisations — measured by TTFT, TPOT, throughput, goodput, MFU, and MBU.

## Sources

- [[sources/aryan-2025-llmops|LLMOps]]
- [[sources/huyen-2025-ai-engineering|AI Engineering]]
- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025): Ch 11 covers INT8 quantization, GGUF with llama.cpp, Ollama, FastAPI, vLLM, ONNX, request batching and caching (see [[contradictions/int8-quantization-speedup-small-models|the INT8 contradiction]]).

<!-- AUTHORED REGION END -->