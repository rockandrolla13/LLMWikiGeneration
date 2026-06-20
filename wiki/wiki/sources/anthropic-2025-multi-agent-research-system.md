---
title: How We Built Our Multi-Agent Research System
page_id: sources/anthropic-2025-multi-agent-research-system
page_type: source
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_technical_books_2_2026_06_19
tags:
- multi-agent-systems
- llm-agents
- prompt-engineering
- agent-evaluation
- orchestrator-worker
- claude
- anthropic
- research-automation
- tool-use
- mcp
- production-ai-systems
- context-management
- parallel-tool-calling
- llm-as-judge
- extended-thinking
- browsecomp
- rainbow-deployment
- ai-infrastructure
sources:
- sources/anthropic-2025-multi-agent-research-system
related: []
mind_map_priority: high
authors:
- Anthropic
year: 2025
source_type: article
schema_version: 2
uuid: ab2c599b-c540-545a-9cc6-28e2f9580f51
content_hash: sha256:ac46f42564c74fea04daf52097aa8048efdebb06a67efc1d9e93881a7885ace9
---

<!-- AUTHORED REGION START -->
# How We Built Our Multi-Agent Research System

**Authors:** Anthropic  
**Year:** 2025  
**Type:** article  
**Markdown source:** `markdown_output/anthropic-2025-multi-agent-research-system.md`

## Summary

A technical blog post / short report by Anthropic (2025) describing how they built the "Research" feature for Claude: a production multi-agent system in which a lead orchestrator agent (Claude Opus 4) plans and delegates parallel subagent workers (Claude Sonnet 4) to search the web, Google Workspace, and integrated tools in order to answer complex, open-ended research queries. The document covers architecture decisions, prompt engineering principles, evaluation strategies, and production engineering challenges, and is authored by Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, and Daniel Ford.

## Key Claims

- A multi-agent system with Claude Opus 4 as lead and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on Anthropic's internal research eval.
- Token usage alone explains 80% of the performance variance in the BrowseComp evaluation; number of tool calls and model choice are the two other major factors (together the three explain 95%).
- Multi-agent agents typically consume ~15x more tokens than standard chat interactions; single agents use ~4x more.
- Parallel tool calling (lead agent spawning 3-5 subagents simultaneously plus subagents calling 3+ tools in parallel) cut research time by up to 90% for complex queries.
- A tool-testing agent that rewrote MCP tool descriptions produced a 40% decrease in task completion time for future agents using the improved descriptions.
- Extended (interleaved) thinking improved instruction-following, reasoning, and efficiency for both the lead agent and subagents.
- LLM-as-judge with a single prompt outputting scores 0.0-1.0 plus pass/fail was the most consistent evaluation method, aligning well with human judgements.
- The architecture uses rainbow deployments to avoid disrupting in-flight long-running agents during code updates.
- Subagent output written to a filesystem (artifact system) minimises the 'game of telephone' through the coordinator and reduces token overhead.
- Human testers discovered that early agents consistently preferred SEO-optimised content farms over authoritative sources such as academic PDFs; prompt-level source quality heuristics resolved this.

## Main Concepts

- [[concepts/multi-agent-system|Multi-agent system]]
- [[concepts/orchestrator-worker-lead-agent-subagent-pattern|Orchestrator-worker (lead agent / subagent) pattern]]
- [[concepts/parallel-subagent-spawning|Parallel subagent spawning]]
- [[concepts/interleaved-extended-thinking|Interleaved / extended thinking]]
- [[concepts/prompt-engineering-for-agents|Prompt engineering for agents]]
- [[concepts/tool-design-and-mcp-tool-descriptions|Tool design and MCP tool descriptions]]
- [[concepts/llm-as-judge-evaluation|LLM-as-judge evaluation]]
- [[concepts/browsecomp-evaluation-benchmark|BrowseComp evaluation benchmark]]
- [[concepts/rag-vs-multi-step-dynamic-search|RAG vs. multi-step dynamic search]]
- [[concepts/token-budget-and-context-window-management|Token budget and context window management]]
- [[concepts/rainbow-deployments|Rainbow deployments]]
- [[concepts/end-state-evaluation|End-state evaluation]]
- [[concepts/long-horizon-conversation-and-context-compression|Long-horizon conversation and context compression]]
- [[concepts/subagent-artifact-filesystem-output-pattern|Subagent artifact / filesystem output pattern]]
- [[concepts/observability-and-production-tracing-for-agents|Observability and production tracing for agents]]
- [[concepts/breadth-first-vs-depth-first-research-strategies|Breadth-first vs. depth-first research strategies]]

## Key Entities

- [[entities/anthropic|Anthropic]]
- [[entities/claude-ai-assistant-|Claude (AI assistant)]]
- [[entities/claude-opus-4|Claude Opus 4]]
- [[entities/claude-sonnet-4|Claude Sonnet 4]]
- [[entities/claude-sonnet-3-7|Claude Sonnet 3.7]]
- [[entities/jeremy-hadfield|Jeremy Hadfield]]
- [[entities/barry-zhang|Barry Zhang]]
- [[entities/kenneth-lien|Kenneth Lien]]
- [[entities/florian-scholz|Florian Scholz]]
- [[entities/jeremy-fox|Jeremy Fox]]
- [[entities/daniel-ford|Daniel Ford]]
- [[entities/anthropic-apps-engineering-team|Anthropic apps engineering team]]
- [[entities/anthropic-console|Anthropic Console]]
- [[entities/anthropic-cookbook-open-source-prompts-|Anthropic Cookbook (open-source prompts)]]
- [[entities/mcp-model-context-protocol-servers|MCP (Model Context Protocol) servers]]
- [[entities/google-workspace|Google Workspace]]
- [[entities/browsecomp-evaluation|BrowseComp evaluation]]
- [[entities/clio-mentioned-as-section-heading-likely-internal-tool-|Clio (mentioned as section heading, likely internal tool)]]
- [[entities/z-library-document-source-distribution-channel-|Z-Library (document source/distribution channel)]]

## Questions Raised

- How does Anthropic's asynchronous execution roadmap (agents spawning new subagents dynamically) compare to current synchronous orchestration, and what engineering complexity does it introduce?
- What is 'Clio' referenced as a section heading — an internal observability or privacy tool?
- How does the BrowseComp benchmark compare to other agent evaluation benchmarks such as WebArena or GAIA?
- At what point does adding more subagents stop improving performance (diminishing returns on parallelism)?
- How does the 'rainbow deployment' strategy interact with stateful agent checkpoints during model version upgrades?
- What specific rubric dimensions did the LLM judge use, and how were calibration and inter-rater reliability assessed?

<!-- AUTHORED REGION END -->
