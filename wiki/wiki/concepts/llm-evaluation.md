---
content_hash: sha256:f9301c7fd7860a22918776655fa2b1c41f8eb373df353b39c0bb8cdca16ba4c5
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/llm-evaluation
page_type: concept
related:
- concepts/perplexity
revision_id: 3
schema_version: 2
sources:
- sources/berryman-2024-prompt-engineering-llms
- sources/aryan-2025-llmops
- sources/pathan-2025-mastering-llm-applications-langchain
- sources/liu-2025-build-fine-tune-small-language-model
tags:
- ai-engineering
title: LLM Evaluation
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 0a38e0dd-2469-5539-9cbf-e155b93d0d7b
---

<!-- AUTHORED REGION START -->
# LLM Evaluation

## Definition

Combined offline (test suites, LLM-as-judge, surgical code-completion benchmarks) and online (A/B tests, implicit telemetry like acceptance rate) measurement of LLM-application quality. Berryman emphasises measuring user-productivity proxies, not just thumbs-up signals.

## Sources

- [[sources/pathan-2025-mastering-llm-applications-langchain|Mastering LLM Applications with LangChain and Hugging Face]]
- [[sources/aryan-2025-llmops|LLMOps]]
- [[sources/berryman-2024-prompt-engineering-llms|Prompt Engineering for LLMs]]
- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025): Ch 7 evaluates a small model with perplexity, token accuracy, n-gram baselines, repetition and diversity scores and a readiness gate.

<!-- AUTHORED REGION END -->