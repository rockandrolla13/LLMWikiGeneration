---
title: Insecure Output Handling
page_id: concepts/insecure-output-handling
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
revision_hash: sha256:ba829ffbcf9e0ed0
schema_version: 2
uuid: 8c03141a-6fd3-5d5f-8dc3-947dd58db8b5
content_hash: sha256:79f675a3d78c4628099b8a05cee9dff0556f464556758b81e55aa6ea62eafa5d
---

<!-- AUTHORED REGION START -->
# Insecure Output Handling

## Definition

A vulnerability that arises when an application treats LLM output as trusted and passes it to downstream systems (browsers, shells, databases, code interpreters) without validation, enabling XSS, SQL injection, SSRF, or remote code execution. The fix is to treat every LLM response as untrusted user input crossing a trust boundary.

## Sources

- [[sources/wilson-2024-llm-security-playbook|The Developer's Playbook for Large Language Model Security]]

<!-- AUTHORED REGION END -->
