---
title: Command-Query Responsibility Segregation
page_id: concepts/command-query-responsibility-segregation
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
revision_hash: sha256:21abdd29133198d4
---

# Command-Query Responsibility Segregation

## Definition

An architectural pattern that separates the write side (commands mutating a rich domain model) from the read side (queries served by denormalised read models optimised for display), updated asynchronously via event handlers.

## Sources

- [[sources/percival-2020-architecture-patterns-python|Architecture Patterns with Python]]
