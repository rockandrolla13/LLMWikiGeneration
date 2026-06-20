---
title: Decoding Strategies
page_id: concepts/decoding-strategies
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
- transformers
sources:
- sources/raschka-2024-build-llm-from-scratch
related:
- concepts/transformers
mind_map_priority: medium
revision_hash: sha256:a6a4f2d6f19c5ae8
schema_version: 2
uuid: e195fe84-f098-52cd-aa2f-7573ea62cc9f
content_hash: sha256:3adfd895c33f28a62318e7075f54bdec216e8b798be48cfbc4b7f995719c083b
---

<!-- AUTHORED REGION START -->
# Decoding Strategies

## Definition

Algorithms for sampling tokens from an LLM's output distribution at inference time. Raschka covers greedy decoding, temperature scaling (which rescales logits to control sharpness), and top-k sampling (which restricts sampling to the k most likely tokens) as ways to trade off determinism and diversity.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]

## Related Concepts

- [[concepts/transformers]]

<!-- AUTHORED REGION END -->
