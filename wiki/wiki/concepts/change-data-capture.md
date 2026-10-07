---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:94f1d4c01b2cae8e75eca83dd3229cb0b1208aca0c41254f78b1335175ada073
created: '2026-10-07T18:46:39Z'
page_id: concepts/change-data-capture
page_type: concept
related:
- concepts/idempotent-data-pipeline
revision_id: 1
schema_version: 2
sources:
- sources/konieczny-2025-data-engineering-design-patterns
tags: []
title: Change Data Capture
updated: '2026-10-07T18:46:39Z'
updated_by: op_9a030901d060
uuid: c8d0947b-20a6-561f-b739-c3b3a061b077
---

<!-- AUTHORED REGION START -->
# Change Data Capture

## Definition

Change data capture streams every insert, update and delete from a database's append-only commit log to a broker or other output. It gives lower latency than scheduled incremental queries and sees hard deletes. The cost is extra setup, often needing operations help, and the output must be treated as data in motion.

## Sources

- [[sources/konieczny-2025-data-engineering-design-patterns|Data Engineering Design Patterns]]

## Related Concepts

- [[concepts/idempotent-data-pipeline|Idempotent Data Pipeline]]
<!-- AUTHORED REGION END -->