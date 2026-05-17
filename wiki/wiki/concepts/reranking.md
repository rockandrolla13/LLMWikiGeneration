---
title: Reranking
page_id: concepts/reranking
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
- transformers
sources:
- sources/alammar-2024-hands-on-llm
- sources/mendelevitch-2025-hands-on-rag
related:
- concepts/transformers
mind_map_priority: medium
revision_hash: sha256:4bef03800664ebca
---

# Reranking

## Definition

A second-stage retrieval step that reorders an initial candidate set of passages using a more expensive scoring model (typically a cross-encoder) to surface the most relevant chunks. Production RAG also uses diversity rerankers to reduce redundancy in the top-k results.

## Sources

- [[sources/alammar-2024-hands-on-llm|Hands-On Large Language Models]]
- [[sources/mendelevitch-2025-hands-on-rag|Hands-On RAG for Production]]

## Related Concepts

- [[concepts/transformers]]
