---
content_hash: sha256:d61e2abb98fe8d05d1259e4628eb3567fa1e82aadcc519cd2eb3cd330433e2d1
page_id: concepts/self-attention
page_type: concept
revision_id: 2
schema_version: 2
sources:
- sources/alammar-2024-hands-on-llm
- sources/raschka-2024-build-llm-from-scratch
- sources/aryan-2025-llmops
tags:
- attention
- neural-networks
title: Self-Attention
updated: '2026-10-07T18:46:39Z'
updated_by: op_9a030901d060
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

## Related

- [[transformers]]
- [[multi-head-attention]]

## See Also (AI Engineering batch)
<!-- wiki-batch-ai-engineering-2026-05-17 -->
- [[sources/alammar-2024-hands-on-llm|alammar-2024-hands-on-llm]]
- [[sources/raschka-2024-build-llm-from-scratch|raschka-2024-build-llm-from-scratch]]

<!-- AUTHORED REGION END -->