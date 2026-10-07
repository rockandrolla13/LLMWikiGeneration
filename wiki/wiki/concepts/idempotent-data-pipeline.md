---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:656dbb3af5781a1857a8846661aefb839a1e43e1453d5200f549e239096e7bb7
created: '2026-10-07T18:46:39Z'
page_id: concepts/idempotent-data-pipeline
page_type: concept
related:
- concepts/change-data-capture
- concepts/dead-letter-pattern
revision_id: 1
schema_version: 2
sources:
- sources/konieczny-2025-data-engineering-design-patterns
tags: []
title: Idempotent Data Pipeline
updated: '2026-10-07T18:46:39Z'
updated_by: op_9a030901d060
uuid: 7615a326-58c0-5d84-9d07-f72f52e10733
---

<!-- AUTHORED REGION START -->
# Idempotent Data Pipeline

## Definition

A data pipeline is idempotent when running it again on the same input gives the same output, with no duplicates or with duplicates that are clearly identifiable. This matters because retries and backfills are routine. Common ways to get it are overwriting the target, merging on stable keys, deriving keys from immutable values, or writing inside a transaction.

## Sources

- [[sources/konieczny-2025-data-engineering-design-patterns|Data Engineering Design Patterns]]

## Related Concepts

- [[concepts/change-data-capture|Change Data Capture]]
- [[concepts/dead-letter-pattern|Dead-Letter Pattern]]
<!-- AUTHORED REGION END -->