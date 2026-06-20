---
title: Build a Large Language Model (From Scratch)
page_id: sources/raschka-2024-build-llm-from-scratch
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Sebastian Raschka
year: 2024
publisher: Manning
edition: 1st
is_early_release: false
page_count_estimate: 370
tags:
- ai-engineering
- llm
related:
- concepts/byte-pair-encoding
- concepts/causal-attention
- concepts/classification-fine-tuning
- concepts/decoding-strategies
- concepts/gelu-activation
- concepts/instruction-fine-tuning
- concepts/language-model-pretraining
- concepts/layer-normalization
- concepts/low-rank-adaptation
- concepts/multi-head-attention
- concepts/positional-embeddings
- concepts/self-attention
- concepts/token-embeddings
- concepts/transformers
- entities/alec-radford
- entities/edward-hu
- entities/lightning-ai
- entities/manning-publications
- entities/openai
- entities/pytorch
- entities/sebastian-raschka
- entities/tiktoken
mind_map_priority: medium
revision_hash: sha256:92ac0419f91612c9
schema_version: 2
uuid: 2616b43b-ca78-5a71-9469-01e84f3b6d37
content_hash: sha256:fabab54fc87a9338364fd4c7632742bd101c8b5674e84030b9b71b1455e0ba2f
---

<!-- AUTHORED REGION START -->
# Build a Large Language Model (From Scratch)

**Authors:** [[entities/sebastian-raschka|Sebastian Raschka]]

**Year:** 2024

**Publisher:** Manning

**Edition:** 1st

## Summary

Sebastian Raschka's Build a Large Language Model (From Scratch) is a code-first, end-to-end tutorial that walks the reader through implementing a GPT-style decoder-only LLM in PyTorch, with no reliance on Hugging Face Transformers or other high-level abstractions. The book is organized around three stages: (1) building the architecture and data pipeline — tokenization with [[byte-pair-encoding|byte pair encoding]] via tiktoken, [[token-embeddings|token embeddings]] and learned [[positional-embeddings|positional embeddings]], and the attention stack from naive [[self-attention|self-attention]] up through [[causal-attention|causal attention]] and [[multi-head-attention|multi-head attention]]; (2) [[language-model-pretraining|pretraining]] the resulting GPT model on unlabeled text with cross-entropy loss and loading OpenAI's public GPT-2 weights; and (3) two flavors of fine-tuning — [[classification-fine-tuning|classification fine-tuning]] for spam detection and [[instruction-fine-tuning|instruction fine-tuning]] to produce a small assistant model.

The book's distinctive angle is pedagogical: Raschka deliberately rebuilds every component (a [[transformers|transformer]] block, [[layer-normalization|layer normalization]], [[gelu-activation|GELU activation]], shortcut connections, [[decoding-strategies|temperature scaling and top-k sampling]]) from primitive PyTorch ops, so the reader understands the mechanics rather than treating the model as a black box. Where competitors (Hugging Face cookbooks, applied-LLM books) start at the API surface, this book starts at the matrix-multiply level. Appendix E adds a from-scratch [[low-rank-adaptation|LoRA]] implementation for parameter-efficient fine-tuning, rounding out a complete production-style workflow at toy scale.

The target reader is a Python-fluent ML practitioner — engineer, researcher, or advanced student — who wants conceptual mastery of how modern LLMs work internally, without needing access to industrial-scale compute. All code is laptop-runnable and reuses public GPT-2 weights so the small models trained from scratch are educational rather than competitive with frontier models.

## Key Contributions

- A complete, self-contained PyTorch reimplementation of GPT-2's architecture — attention, MLP, layer norm, residuals, embeddings — built up incrementally so each component is motivated and tested before composition
- A coherent three-stage mental model (architecture+data, pretraining, fine-tuning) that maps cleanly onto the production LLM lifecycle and is used as the spine of every chapter
- A practical demonstration that GPT-2 small can be pretrained, classification-fine-tuned (spam), and instruction-fine-tuned (Alpaca-style) on a single laptop, making LLM internals accessible without GPU clusters
- A from-scratch implementation of LoRA in Appendix E that bridges the gap between the book's vanilla fine-tuning and modern parameter-efficient adaptation

## Key Topics Covered

byte-pair-encoding, token-embeddings, positional-embeddings, self-attention, causal-attention, multi-head-attention, transformers, layer-normalization, gelu-activation, language-model-pretraining, decoding-strategies, instruction-fine-tuning, classification-fine-tuning, low-rank-adaptation

## Questions Raised

- How do the from-scratch GPT-2 design choices (absolute learned positional embeddings, post-LN ordering, GELU) compare empirically to modern alternatives like RoPE, RMSNorm, and SwiGLU used in Llama-style models?
- The book stops at supervised fine-tuning — what would be required to extend the from-scratch approach through RLHF, DPO, or preference optimization?
- How does the educational laptop-scale pretraining loss curve behave compared to scaling-law predictions for full-scale GPT-2/3 runs?
- At what point does building from scratch stop being a useful exercise and how should readers transition to production frameworks like LitGPT or Hugging Face Transformers?

## Intended Audience

Python-fluent ML engineers, researchers, and advanced students who want a mechanistic, code-level understanding of how GPT-style LLMs are tokenized, architected, pretrained, and fine-tuned, without depending on high-level Hugging Face abstractions.

## Key Concepts in This Source

- [[concepts/byte-pair-encoding|Byte Pair Encoding]]
- [[concepts/token-embeddings|Token Embeddings]]
- [[concepts/positional-embeddings|Positional Embeddings]]
- [[concepts/self-attention|Self-Attention]]
- [[concepts/causal-attention|Causal Attention]]
- [[concepts/multi-head-attention|Multi-Head Attention]]
- [[concepts/transformers|Transformers]]
- [[concepts/layer-normalization|Layer Normalization]]
- [[concepts/gelu-activation|GELU Activation]]
- [[concepts/language-model-pretraining|Language Model Pretraining]]
- [[concepts/decoding-strategies|Decoding Strategies]]
- [[concepts/instruction-fine-tuning|Instruction Fine-Tuning]]
- [[concepts/classification-fine-tuning|Classification Fine-Tuning]]
- [[concepts/low-rank-adaptation|Low-Rank Adaptation]]

## Entities

- [[entities/sebastian-raschka|Sebastian Raschka]]
- [[entities/openai|OpenAI]]
- [[entities/alec-radford|Alec Radford]]
- [[entities/manning-publications|Manning Publications]]
- [[entities/pytorch|PyTorch]]
- [[entities/tiktoken|tiktoken]]
- [[entities/lightning-ai|Lightning AI]]
- [[entities/edward-hu|Edward Hu]]

<!-- AUTHORED REGION END -->
