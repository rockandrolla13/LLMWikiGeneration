---
title: Tool Calling
page_id: concepts/tool-calling
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
sources:
- sources/oshin-2025-learning-langchain
related: []
mind_map_priority: medium
revision_hash: sha256:85ce6b0961881673
schema_version: 2
uuid: e9e79c6b-83c2-599d-9cd1-f7479d25d0cb
content_hash: sha256:5ae0ebcf4c4db21bee0e3e2797472da26a69059779371600a3246997cf86ca5f
---

<!-- AUTHORED REGION START -->
# Tool Calling

## Definition

Mechanism by which an LLM emits a structured request to invoke an external function (search, calculator, database query, API call), receives the result, and continues generation. LangChain exposes tools through a uniform decorator and binds them to chat models via bind_tools.

## Sources

- [[sources/oshin-2025-learning-langchain|Learning LangChain]]

<!-- AUTHORED REGION END -->
