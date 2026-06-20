---
title: Domain Events
page_id: concepts/domain-events
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
revision_hash: sha256:e510ef57a44fd6f5
schema_version: 2
uuid: 34fe9c5d-c00e-5939-982c-70cda994af60
content_hash: sha256:f85af0b6d7f0253c92c67222c52bb1634338e335e30e9028f14d29c1495c6785
---

<!-- AUTHORED REGION START -->
# Domain Events

## Definition

Simple immutable dataclasses raised by the domain model to represent things that have happened in the business (e.g. 'OutOfStock', 'Allocated'); they decouple the recording of an event from the actions triggered in response.

## Sources

- [[sources/percival-2020-architecture-patterns-python|Architecture Patterns with Python]]

<!-- AUTHORED REGION END -->
