---
title: Layer Normalization
page_id: concepts/layer-normalization
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
revision_hash: sha256:089cc0453f23cd95
schema_version: 2
uuid: 942f27d5-964a-5992-b9e1-c7b8fdb446f4
content_hash: sha256:346b718c68b21952d62dd4962bcb4649ffe5e911b468535f5a823ef2cf03a5e6
---

<!-- AUTHORED REGION START -->
# Layer Normalization

## Definition

A normalization technique that rescales activations to zero mean and unit variance across the feature dimension per sample (independent of batch size), with learned scale and shift parameters. Used inside each transformer block to stabilize gradients and accelerate training of deep networks.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]

## Related Concepts

- [[concepts/transformers]]

<!-- AUTHORED REGION END -->
