---
title: A Practical Guide to Building Agents
page_id: sources/openai-2025-practical-guide-building-agents
page_type: source
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_technical_books_2026_06_19
tags:
- agents
- llm
- orchestration
- openai
- multi-agent
- tool-use
sources:
- sources/openai-2025-practical-guide-building-agents
related: []
mind_map_priority: high
authors:
- OpenAI
year: 2025
source_type: book
schema_version: 2
uuid: baa84f6b-f80c-5dc2-b417-eb55ea6b8141
content_hash: sha256:98257d06983d736c09b85e20546202baaaeb7384d0aa18ae71f6328dd0e5fd91
---

<!-- AUTHORED REGION START -->
# A Practical Guide to Building Agents

**Authors:** OpenAI  
**Year:** 2025  
**Type:** book  
**Markdown source:** `markdown_output/openai-2025-practical-guide-building-agents.md`

## Summary

A Practical Guide to Building Agents (OpenAI, 2025) is a concise technical guide aimed at product and engineering teams building LLM-powered autonomous systems for the first time. It distills insights from customer deployments into actionable best practices covering how to identify agent-worthy use cases, design agent logic using models, tools, and instructions, orchestrate single- and multi-agent workflows, and apply guardrails for safe and predictable operation. The guide uses OpenAI's Agents SDK for code examples but explicitly notes the concepts apply to any library or from-scratch implementation.

## Key Claims

- Agents are systems that independently accomplish tasks on behalf of users by combining an LLM for decision-making with tools and explicit instructions, distinguishing them from simpler LLM apps like chatbots or classifiers.
- Agents are best suited to workflows with complex nuanced judgment, difficult-to-maintain rule sets, or heavy reliance on unstructured data — where deterministic automation falls short.
- The three core components of any agent are: a model (LLM for reasoning), tools (external APIs or functions), and instructions (guardrails and guidelines).
- Model selection should start with the most capable model to establish a baseline, then swap in smaller models where acceptable to optimize for cost and latency.
- Orchestration patterns fall into two categories: single-agent systems (one model with tools in a loop) and multi-agent systems (workflow distributed across coordinated agents); starting single-agent and scaling incrementally is the recommended approach.
- High-quality, unambiguous instructions are critical for agent performance; existing SOPs, support scripts, or policy documents can be converted into agent routines using advanced models like o1 or o3-mini.
- Tools fall into three types: data tools (retrieve context), action tools (interact with external systems), and orchestration tools (agents acting as tools for other agents).

## Main Concepts

- [[concepts/llm-powered-agents|LLM-powered agents]]
- [[concepts/agent-orchestration-(single-agent-and-multi-agent-patterns)|Agent orchestration (single-agent and multi-agent patterns)]]
- [[concepts/tool-definition-and-tool-types-(data,-action,-orchestration)|Tool definition and tool types (data, action, orchestration)]]
- [[concepts/model-selection-and-cost-latency-optimization|Model selection and cost-latency optimization]]
- [[concepts/agent-instructions-and-prompt-templates|Agent instructions and prompt templates]]
- [[concepts/guardrails-for-safe-agent-execution|Guardrails for safe agent execution]]

## Key Entities

- [[entities/openai|OpenAI]]
- [[entities/openai-agents-sdk|OpenAI Agents SDK]]
- [[entities/o1-model-|o1 (model)]]
- [[entities/o3-mini-model-|o3-mini (model)]]
- [[entities/runner-run-method-agents-sdk-|Runner.run() method (Agents SDK)]]

## Questions Raised

- How do guardrails (chapter 4) constrain agent behavior in practice, and what failure modes do they address?
- At what scale or complexity threshold does a single-agent system need to be refactored into a multi-agent architecture?
- How should teams design and run evaluations (evals) to establish the performance baselines needed before optimizing model selection?

<!-- AUTHORED REGION END -->
