---
content_hash: sha256:94106c85b732251c569029333b703e17d945172db304e64750ee6fbf43c83b1f
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/autonomous-ai-agents
page_type: concept
related:
- concepts/autoresearch
- sources/karpathy-2026-autoresearch
revision_id: 3
schema_version: 2
sources:
- sources/taulli-2024-ai-assisted-programming
- sources/marks-2026-ai-hurtles-ahead
- sources/karpathy-2026-autoresearch
tags:
- ai-engineering
title: Autonomous AI Agents
updated: '2026-11-24T23:30:14Z'
updated_by: op_53f181d9343b
uuid: 0a6c2a12-2c77-5717-aa42-789365ab2e3a
---

<!-- AUTHORED REGION START -->
# Autonomous AI Agents

## Definition

Systems that wrap an LLM with planning, memory, and tool-use loops so the model can pursue multi-step coding goals (running shell commands, editing files, reviewing PRs) with limited human guidance; Taulli reviews their failure modes — resource consumption, infinite loops, amnesia, distraction.

## Sources

- [[sources/taulli-2024-ai-assisted-programming|AI-Assisted Programming]]

## In Howard Marks's Memos

- [[sources/marks-2026-ai-hurtles-ahead|AI Hurtles Ahead]] (2026)
## Autoresearch

Karpathy's autoresearch is a worked example of an autonomous agent doing research: it edits one training file, runs 5-minute experiments and keeps only improvements, looping until stopped. He reports that agents implement well-specified ideas well but propose creative ones poorly, and that they resist looping forever. See [[sources/karpathy-2026-autoresearch|Autoresearch (Karpathy, 2026)]] and [[concepts/autoresearch|Autoresearch]].
<!-- AUTHORED REGION END -->
