---
title: GELU Activation
page_id: concepts/gelu-activation
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
- transformers
sources:
- sources/raschka-2024-build-llm-from-scratch
related:
- concepts/transformers
mind_map_priority: medium
revision_hash: sha256:27aec7085e233c22
---

# GELU Activation

## Definition

The Gaussian Error Linear Unit, a smooth, non-monotonic activation function that weights inputs by their value under the standard normal CDF, providing a stochastic-looking gating effect. GELU is the default nonlinearity in the position-wise feed-forward network of GPT-style transformers.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]

## Related Concepts

- [[concepts/transformers]]
