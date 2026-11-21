---
content_hash: sha256:608f25bea4a440168ca8fa528d7c40cbcef560e5a97ce72afe846d75297e23b2
page_id: concepts/self-attention
page_type: concept
related:
- concepts/rotary-position-embeddings
- concepts/grouped-query-attention
revision_id: 3
schema_version: 2
sources:
- sources/alammar-2024-hands-on-llm
- sources/raschka-2024-build-llm-from-scratch
- sources/aryan-2025-llmops
- sources/liu-2025-build-fine-tune-small-language-model
tags:
- attention
- neural-networks
title: Self-Attention
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 5507fdbd-74c5-53c4-ad1d-2ce157bc6528
---

<!-- AUTHORED REGION START -->
# Self-Attention

## Definition

Self-attention computes relationships between all positions in a sequence.

## Formula

`Attention(Q,K,V) = softmax(QK^T / sqrt(d)) * V`

## Sources

- [[sources/aryan-2025-llmops|LLMOps]]
- [[attention-paper|Attention Is All You Need]]
- [[Ashish Vaswani]]
- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025): Ch 2 builds masked self-attention step by step, following Karpathy's character-level GPT.

## Related

- [[transformers]]
- [[multi-head-attention]]

## See Also (AI Engineering batch)
<!-- wiki-batch-ai-engineering-2026-05-17 -->
- [[sources/alammar-2024-hands-on-llm|alammar-2024-hands-on-llm]]
- [[sources/raschka-2024-build-llm-from-scratch|raschka-2024-build-llm-from-scratch]]

<!-- AUTHORED REGION END -->