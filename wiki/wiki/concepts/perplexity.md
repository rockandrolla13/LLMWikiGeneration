---
abstraction_level: foundational
concept_type: methodology
content_hash: sha256:68fdf4b652b20abc37faeb563dda6f6b99812a32ee3d1c7de4c801fa12130fee
created: '2026-11-21T02:00:24Z'
page_id: concepts/perplexity
page_type: concept
related:
- concepts/llm-evaluation
- concepts/language-model-pretraining
- concepts/tokenization
revision_id: 1
schema_version: 2
sources:
- sources/liu-2025-build-fine-tune-small-language-model
tags: []
title: Perplexity
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 4110b055-f36b-5016-8e94-fb6969af561d
---

<!-- AUTHORED REGION START -->
# Perplexity

## Definition

Perplexity is the exponential of a language model's average cross-entropy loss per token: perplexity = exp(loss). It reads as the effective number of equally likely choices the model faces at each step, so lower is better. A uniform guess over a vocabulary of V tokens gives perplexity V.

## Caveats

Perplexity is only comparable between models that share a tokenizer and a test domain. Liu (2025) warns that it is domain-dependent. His own comparison of a 32K-vocabulary model with GPT-2 under its 50,257-token tokenizer breaks the shared-tokenizer condition. In the book, a 77.2M GPT-2-style model reaches perplexity 111.05 on Wikipedia text (Ch 7), and the 109M MiniMind-style model reaches 17.37 on OpenWebText validation data (Ch 8).

## Sources

- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model: A Step-by-Step Guide for Beginners, Researchers, and Non-Programmers]]

## Related Concepts

- [[concepts/llm-evaluation|LLM Evaluation]]
- [[concepts/language-model-pretraining|Language Model Pretraining]]
- [[concepts/tokenization|Tokenization]]
<!-- AUTHORED REGION END -->