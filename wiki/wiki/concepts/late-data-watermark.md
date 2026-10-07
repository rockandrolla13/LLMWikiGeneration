---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:b58ab9c01eed1e65b41625b11f4c2fc6281b7a6fb41a8924925bacd7d3c24679
created: '2026-10-07T18:46:39Z'
page_id: concepts/late-data-watermark
page_type: concept
related:
- concepts/dead-letter-pattern
revision_id: 1
schema_version: 2
sources:
- sources/konieczny-2025-data-engineering-design-patterns
tags: []
title: Late Data Watermark
updated: '2026-10-07T18:46:39Z'
updated_by: op_9a030901d060
uuid: bf030b2f-45ab-5cfb-865d-6c6a64b8522f
---

<!-- AUTHORED REGION START -->
# Late Data Watermark

## Definition

A watermark is the maximum event time seen so far minus an allowed lateness. Records with event times before the watermark count as late. Pipelines use it to decide when to drop late records, route them elsewhere, or reprocess past partitions.

## Sources

- [[sources/konieczny-2025-data-engineering-design-patterns|Data Engineering Design Patterns]]

## Related Concepts

- [[concepts/dead-letter-pattern|Dead-Letter Pattern]]
<!-- AUTHORED REGION END -->