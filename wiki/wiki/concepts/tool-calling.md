---
title: Tool Calling
page_id: concepts/tool-calling
page_type: concept
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
sources:
- sources/oshin-2025-learning-langchain
related: []
mind_map_priority: medium
---

# Tool Calling

## Definition

Mechanism by which an LLM emits a structured request to invoke an external function (search, calculator, database query, API call), receives the result, and continues generation. LangChain exposes tools through a uniform decorator and binds them to chat models via bind_tools.

## Sources

- [[sources/oshin-2025-learning-langchain|Learning LangChain]]
