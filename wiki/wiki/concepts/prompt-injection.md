---
title: Prompt Injection
page_id: concepts/prompt-injection
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
sources:
- sources/caelen-2023-developing-apps-gpt4
- sources/mendelevitch-2025-hands-on-rag
- sources/thomas-2025-ai-value-creators
- sources/wilson-2024-llm-security-playbook
related: []
mind_map_priority: high
revision_hash: sha256:d09615a8d30876d4
---

# Prompt Injection

## Definition

An LLM-specific vulnerability in which crafty user or third-party inputs manipulate the model's instructions, causing unintended actions such as leaking confidential data, bypassing safety filters, or executing attacker-chosen tasks. Direct prompt injection comes from the user; indirect prompt injection arrives via untrusted content the LLM ingests from external sources.

## Sources

- [[sources/caelen-2023-developing-apps-gpt4|Developing Apps with GPT-4 and ChatGPT]]
- [[sources/mendelevitch-2025-hands-on-rag|Hands-On RAG for Production]]
- [[sources/thomas-2025-ai-value-creators|AI Value Creators]]
- [[sources/wilson-2024-llm-security-playbook|The Developer's Playbook for Large Language Model Security]]
