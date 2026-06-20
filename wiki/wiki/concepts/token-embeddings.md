---
title: Token Embeddings
page_id: concepts/token-embeddings
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
- self-attention
- transformers
sources:
- sources/alammar-2024-hands-on-llm
- sources/raschka-2024-build-llm-from-scratch
related:
- concepts/self-attention
- concepts/transformers
mind_map_priority: medium
revision_hash: sha256:c8b211139b95c79b
schema_version: 2
uuid: 90323176-9e30-5935-9a02-c6fa896fb58d
content_hash: sha256:6f32c1fa01404ecabb0f6a3ceacc6ad1d216fddc0b9f8e759e4ab5eefc943a36
---

<!-- AUTHORED REGION START -->
# Token Embeddings

## Definition

Learned dense vector representations that map discrete token IDs into a continuous high-dimensional space (e.g. 768 for GPT-2 small, 12,288 for GPT-3) so that downstream layers can operate on semantically meaningful inputs. Implemented in PyTorch as a trainable lookup table updated during pretraining.

## Sources

- [[sources/alammar-2024-hands-on-llm|Hands-On Large Language Models]]
- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]

## Related Concepts

- [[concepts/self-attention]]
- [[concepts/transformers]]

<!-- AUTHORED REGION END -->
