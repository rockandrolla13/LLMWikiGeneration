---
title: LLM Application Architecture
page_id: concepts/llm-application-architecture
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
sources:
- sources/wilson-2024-llm-security-playbook
related: []
mind_map_priority: medium
revision_hash: sha256:75d983e897885e5c
schema_version: 2
uuid: 16ac2c70-b107-593f-a23e-90cc86403910
content_hash: sha256:9e9e55e0575a0cf43a28dbad707a48dc7a66ac580fc1c82f8d5fd8b8a2f9abf5
---

<!-- AUTHORED REGION START -->
# LLM Application Architecture

## Definition

A reference decomposition of an LLM-powered system into the model, user interaction layer, training data pipeline, live external data feeds, and internal services. Treating the LLM as one cog inside this architecture, rather than a standalone oracle, is the prerequisite for threat modeling and applying defense in depth.

## Sources

- [[sources/wilson-2024-llm-security-playbook|The Developer's Playbook for Large Language Model Security]]

<!-- AUTHORED REGION END -->
