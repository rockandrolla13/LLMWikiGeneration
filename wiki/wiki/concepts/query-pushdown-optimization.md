---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:4a754476685f6e57c58b18ab080e95100a01f6c8cae2ee39e489f35359e9b997
created: '2026-10-07T18:46:39Z'
page_id: concepts/query-pushdown-optimization
page_type: concept
related:
- concepts/lazy-evaluation
revision_id: 1
schema_version: 2
sources:
- sources/janssens-2025-python-polars-definitive-guide
tags: []
title: Query Pushdown Optimization
updated: '2026-10-07T18:46:39Z'
updated_by: op_9a030901d060
uuid: b5a977a0-087c-50bd-ac9d-ba2109675232
---

<!-- AUTHORED REGION START -->
# Query Pushdown Optimization

## Definition

A family of query-plan rewrites that move work as close to the data source as possible. Predicate pushdown applies row filters at the scan. Projection pushdown reads only the columns needed. Slice pushdown loads only the rows a head or slice needs. In Polars these run on LazyFrames, so unused data is never read into memory.

## Sources

- [[sources/janssens-2025-python-polars-definitive-guide|Python Polars: The Definitive Guide]]

## Related Concepts

- [[concepts/lazy-evaluation|Lazy Evaluation]]
<!-- AUTHORED REGION END -->