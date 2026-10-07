---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:5e89818dcc8c34f74aafe65ed58912407abcea981cfdbc354fb8e99e6fe5c56b
created: '2026-10-07T18:46:39Z'
page_id: concepts/dead-letter-pattern
page_type: concept
related:
- concepts/idempotent-data-pipeline
- concepts/late-data-watermark
revision_id: 1
schema_version: 2
sources:
- sources/konieczny-2025-data-engineering-design-patterns
tags: []
title: Dead-Letter Pattern
updated: '2026-10-07T18:46:39Z'
updated_by: op_9a030901d060
uuid: 3100797a-3905-5b55-9876-66232a37efd0
---

<!-- AUTHORED REGION START -->
# Dead-Letter Pattern

## Definition

The Dead-Letter pattern keeps a job running when some records cannot be processed. Failing records, with their error details, go to a separate resilient store that is monitored and can later be replayed. Replaying them can force backfills in every downstream consumer.

## Sources

- [[sources/konieczny-2025-data-engineering-design-patterns|Data Engineering Design Patterns]]

## Related Concepts

- [[concepts/idempotent-data-pipeline|Idempotent Data Pipeline]]
- [[concepts/late-data-watermark|Late Data Watermark]]
<!-- AUTHORED REGION END -->