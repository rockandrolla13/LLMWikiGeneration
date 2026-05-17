---
title: ReAct Agent
page_id: concepts/react-agent
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
sources:
- sources/oshin-2025-learning-langchain
related: []
mind_map_priority: medium
revision_hash: sha256:fbd8e80d31d1f0b1
---

# ReAct Agent

## Definition

Agent architecture proposed by Shunyu Yao et al. that interleaves reasoning (thought) traces with actions (tool calls) and observations in a loop until the task is complete. Forms the canonical agent pattern implemented by LangGraph's prebuilt ToolNode and tools_condition.

## Sources

- [[sources/oshin-2025-learning-langchain|Learning LangChain]]
