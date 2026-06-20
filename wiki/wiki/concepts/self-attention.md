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
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
schema_version: 2
uuid: 5507fdbd-74c5-53c4-ad1d-2ce157bc6528
content_hash: sha256:5cf2b5679af81e289b2a584380350d40382dd38829d37901dbaf5751258b4e27
---

<!-- AUTHORED REGION START -->
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

<!-- AUTHORED REGION END -->
