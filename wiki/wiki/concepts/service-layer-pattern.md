---
title: Service Layer Pattern
page_id: concepts/service-layer-pattern
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
sources:
- sources/percival-2020-architecture-patterns-python
related: []
mind_map_priority: medium
revision_hash: sha256:ad302b3a17543d7e
---

# Service Layer Pattern

## Definition

A thin layer that defines the application's use cases and orchestrates the domain model, repository, and unit of work; entrypoints like Flask routes call into the service layer rather than manipulating the domain directly.

## Sources

- [[sources/percival-2020-architecture-patterns-python|Architecture Patterns with Python]]
