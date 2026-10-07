---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:d51efdf15282015050c9e76a3e5a34427823d9ebdb861cb6f35bab1df92e1398
created: '2026-10-07T18:46:39Z'
page_id: concepts/lazy-evaluation
page_type: concept
related:
- concepts/query-pushdown-optimization
revision_id: 1
schema_version: 2
sources:
- sources/janssens-2025-python-polars-definitive-guide
tags: []
title: Lazy Evaluation
updated: '2026-10-07T18:46:39Z'
updated_by: op_9a030901d060
uuid: b2e9b461-13d2-58f9-808b-d996e170db38
---

<!-- AUTHORED REGION START -->
# Lazy Evaluation

## Definition

Operations are recorded as a query plan, not run straight away. The plan runs only when results are requested, for example with collect() on a Polars LazyFrame. Waiting lets an optimizer rewrite the whole plan first. The catch is that each collect recomputes the plan unless intermediate results are cached.

## Sources

- [[sources/janssens-2025-python-polars-definitive-guide|Python Polars: The Definitive Guide]]

## Related Concepts

- [[concepts/query-pushdown-optimization|Query Pushdown Optimization]]
<!-- AUTHORED REGION END -->