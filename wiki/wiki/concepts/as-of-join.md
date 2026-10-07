---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:9118be63e13c38d9c18110688b7ad3385fae03e14a1522d771953da913839e3b
created: '2026-10-07T18:46:39Z'
page_id: concepts/as-of-join
page_type: concept
related: []
revision_id: 1
schema_version: 2
sources:
- sources/janssens-2025-python-polars-definitive-guide
tags: []
title: As-of Join
updated: '2026-10-07T18:46:39Z'
updated_by: op_9a030901d060
uuid: f10b1f33-b2fb-5a3e-a690-4cc5fea306d4
---

<!-- AUTHORED REGION START -->
# As-of Join

## Definition

An inexact join that matches each row to the nearest key in another table, rather than an exact match. It is typically used on timestamps or numeric columns. In Polars, df.join_asof() supports backward, forward or nearest strategies, optional exact-match by-groups, and a tolerance. It aligns sources whose timestamps differ, such as a sale's recording time versus its payment time.

## Sources

- [[sources/janssens-2025-python-polars-definitive-guide|Python Polars: The Definitive Guide]]
<!-- AUTHORED REGION END -->