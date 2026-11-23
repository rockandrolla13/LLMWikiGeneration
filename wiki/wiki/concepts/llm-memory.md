---
content_hash: sha256:765ca503e93593155e248227e3e6a88fd6631c4b23933261398cf4076cbed88b
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/llm-memory
page_type: concept
related:
- concepts/llm-knowledge-bases
- sources/karpathy-2026-llm-knowledge-bases-tweets
revision_id: 3
schema_version: 2
sources:
- sources/oshin-2025-learning-langchain
- sources/aryan-2025-llmops
- sources/karpathy-2026-llm-knowledge-bases-tweets
tags:
- ai-engineering
title: LLM Memory
updated: '2026-11-23T14:43:11Z'
updated_by: op_5c91b297008c
uuid: a0840313-c1b3-5dd9-98c0-a53965ffd81d
---

<!-- AUTHORED REGION START -->
# LLM Memory

## Definition

Mechanisms for giving stateless LLMs persistent context across turns and sessions, ranging from raw message-history buffers to summarisation, semantic recall, and LangGraph checkpointers that persist graph state in a key-value store.

## Sources

- [[sources/aryan-2025-llmops|LLMOps]]
- [[sources/oshin-2025-learning-langchain|Learning LangChain]]

## Explicit, File-Based Memory

Karpathy argues for memory as an explicit artifact: a wiki of markdown files the user can inspect and edit, usable with any AI, instead of memory held implicitly inside one provider. He also notes that very long single conversations hurt speed and quality, and suggests a well-implemented memory feature with active, agentic context management. See [[concepts/llm-knowledge-bases|LLM Knowledge Bases]] and [[sources/karpathy-2026-llm-knowledge-bases-tweets|Karpathy on Obsidian, Second Brains and LLM Knowledge Bases]].
<!-- AUTHORED REGION END -->
