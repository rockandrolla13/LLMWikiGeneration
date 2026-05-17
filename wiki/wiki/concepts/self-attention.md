---
title: Self-Attention
page_id: concepts/self-attention
page_type: concept
tags:
- attention
- neural-networks
sources:
- sources/alammar-2024-hands-on-llm
- sources/raschka-2024-build-llm-from-scratch
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
---

# Self-Attention

## Definition

Self-attention computes relationships between all positions in a sequence.

## Formula

`Attention(Q,K,V) = softmax(QK^T / sqrt(d)) * V`

## Sources

- [[attention-paper|Attention Is All You Need]]
- [[Ashish Vaswani]]

## Related

- [[transformers]]
- [[multi-head-attention]]

## See Also (AI Engineering batch)
<!-- wiki-batch-ai-engineering-2026-05-17 -->
- [[sources/alammar-2024-hands-on-llm|alammar-2024-hands-on-llm]]
- [[sources/raschka-2024-build-llm-from-scratch|raschka-2024-build-llm-from-scratch]]
