---
title: Chunking
page_id: concepts/chunking
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
- working-memory-in-programming
sources:
- sources/hermans-2024-code-reading-in-practice
- sources/mendelevitch-2025-hands-on-rag
related:
- concepts/working-memory-in-programming
mind_map_priority: medium
revision_hash: sha256:72504b7364df9bd5
---

# Chunking

## Definition

The process of splitting source documents into smaller units (fixed-size, sentence-aware, semantic, or layout-aware) before embedding so that retrieval returns appropriately-sized passages. Chunking strategy materially affects retrieval quality and is a key knob in production RAG.

## Sources

- [[sources/hermans-2024-code-reading-in-practice|Code Reading in Practice]]
- [[sources/mendelevitch-2025-hands-on-rag|Hands-On RAG for Production]]

## Related Concepts

- [[concepts/working-memory-in-programming]]
