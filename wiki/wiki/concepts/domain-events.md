---
title: Domain Events
page_id: concepts/domain-events
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
revision_hash: sha256:e510ef57a44fd6f5
---

# Domain Events

## Definition

Simple immutable dataclasses raised by the domain model to represent things that have happened in the business (e.g. 'OutOfStock', 'Allocated'); they decouple the recording of an event from the actions triggered in response.

## Sources

- [[sources/percival-2020-architecture-patterns-python|Architecture Patterns with Python]]
