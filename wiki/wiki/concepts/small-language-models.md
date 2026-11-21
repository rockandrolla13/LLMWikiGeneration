---
abstraction_level: foundational
concept_type: framework
content_hash: sha256:501508dd31166e5b515d74ec12d84fc015c1dc74414ad9a459529a8f73737832
created: '2026-11-21T02:00:24Z'
page_id: concepts/small-language-models
page_type: concept
related:
- concepts/large-language-models
- concepts/fine-tuning
- concepts/model-compression
- concepts/inference-optimization
- contradictions/int8-quantization-speedup-small-models
revision_id: 2
schema_version: 2
sources:
- sources/liu-2025-build-fine-tune-small-language-model
- sources/thomas-2025-hands-on-small-language-models
tags: []
title: Small Language Models
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: a9b22ed5-ff43-5fa1-a89a-230c63239375
---

<!-- AUTHORED REGION START -->
# Small Language Models

## Definition

Small language models (SLMs) are language models small enough to train, fine-tune and serve on consumer or rented GPUs. Liu puts the range at roughly 125 million to 7 billion parameters. The case for them rests on cost, privacy, control, availability and latency. They suit narrow, well-defined tasks with relevant training data, while giant LLMs stay better for broad knowledge, complex reasoning and current information.

## Across Sources

- Liu (2025) trains SLMs from scratch through pretraining, supervised fine-tuning and preference alignment, then deploys them. He notes that an SLM alone cannot replace a large LLM and that practitioners often combine both.
- Thomas (2025) builds agentic applications on top of existing SLMs, served locally (for example with Ollama). The two books share the SLM framing but not the method.

## Sources

- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model: A Step-by-Step Guide for Beginners, Researchers, and Non-Programmers]]
- [[sources/thomas-2025-hands-on-small-language-models|Hands-on Small Language Models]]

## Related Concepts

- [[concepts/large-language-models|Large Language Models]]
- [[concepts/fine-tuning|Fine-Tuning]]
- [[concepts/model-compression|Model Compression]]
- [[concepts/inference-optimization|Inference Optimization]]
<!-- AUTHORED REGION END -->