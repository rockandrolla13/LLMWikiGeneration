---
title: Insecure Output Handling
page_id: concepts/insecure-output-handling
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
sources:
- sources/wilson-2024-llm-security-playbook
related: []
mind_map_priority: medium
revision_hash: sha256:ba829ffbcf9e0ed0
---

# Insecure Output Handling

## Definition

A vulnerability that arises when an application treats LLM output as trusted and passes it to downstream systems (browsers, shells, databases, code interpreters) without validation, enabling XSS, SQL injection, SSRF, or remote code execution. The fix is to treat every LLM response as untrusted user input crossing a trust boundary.

## Sources

- [[sources/wilson-2024-llm-security-playbook|The Developer's Playbook for Large Language Model Security]]
