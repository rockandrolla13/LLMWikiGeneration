---
content_hash: sha256:4c3c12dac5e016d85c45223d2e2ca220780681ca840e19a0a89179bd9169347e
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/decoding-strategies
page_type: concept
related:
- concepts/transformers
revision_id: 2
schema_version: 2
sources:
- sources/raschka-2024-build-llm-from-scratch
- sources/pathan-2025-mastering-llm-applications-langchain
tags:
- ai-engineering
- transformers
title: Decoding Strategies
updated: '2026-10-07T18:46:39Z'
updated_by: op_9a030901d060
uuid: e195fe84-f098-52cd-aa2f-7573ea62cc9f
---

<!-- AUTHORED REGION START -->
# Decoding Strategies

## Definition

Algorithms for sampling tokens from an LLM's output distribution at inference time. Raschka covers greedy decoding, temperature scaling (which rescales logits to control sharpness), and top-k sampling (which restricts sampling to the k most likely tokens) as ways to trade off determinism and diversity.

## Sources

- [[sources/pathan-2025-mastering-llm-applications-langchain|Mastering LLM Applications with LangChain and Hugging Face]]
- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]

## Related Concepts

- [[concepts/transformers]]

<!-- AUTHORED REGION END -->