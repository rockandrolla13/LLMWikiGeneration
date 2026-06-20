---
title: Command-Query Responsibility Segregation
page_id: concepts/command-query-responsibility-segregation
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
sources:
- sources/percival-2020-architecture-patterns-python
related: []
mind_map_priority: medium
revision_hash: sha256:21abdd29133198d4
schema_version: 2
uuid: 6532aaf9-7627-59d1-89e4-b6e8bf8384ab
content_hash: sha256:b0e300d8a2c79d934cc3da0588c1f2d153c2915e4ff722b3b353e215305c248d
---

<!-- AUTHORED REGION START -->
# Command-Query Responsibility Segregation

## Definition

An architectural pattern that separates the write side (commands mutating a rich domain model) from the read side (queries served by denormalised read models optimised for display), updated asynchronously via event handlers.

## Sources

- [[sources/percival-2020-architecture-patterns-python|Architecture Patterns with Python]]

<!-- AUTHORED REGION END -->
