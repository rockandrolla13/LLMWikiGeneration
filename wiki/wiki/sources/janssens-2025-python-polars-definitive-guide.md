---
authors:
- Jeroen Janssens
- Thijs Nieuwdorp
content_hash: sha256:9ac63b1fc644a4ad9a49392733307dde3d137545360daf154a5504536e373095
created: '2026-10-07T18:46:39Z'
edition: First Edition
is_early_release: false
mind_map_priority: medium
page_count_estimate: 504
page_id: sources/janssens-2025-python-polars-definitive-guide
page_type: source
publisher: O'Reilly Media
raw_location: wiki/raw/ai-engineering/
related:
- concepts/data-engineering-for-ml
- concepts/feature-engineering
- concepts/lazy-evaluation
- concepts/query-pushdown-optimization
- concepts/as-of-join
- sources/reis-2022-fundamentals-data-engineering
- sources/khraisha-2024-financial-data-engineering
- sources/nelson-2024-swe-for-data-scientists
- sources/percival-2020-architecture-patterns-python
- sources/alhussein-2024-databricks-certified-data-engineer
- entities/jeroen-janssens
- entities/thijs-nieuwdorp
- entities/oreilly-media
- entities/polars
- entities/ritchie-vink
- entities/pandas
- entities/apache-arrow
revision_id: 1
schema_version: 2
source_path: markdown_output/janssens-2025-python-polars-definitive-guide.md
source_type: book
sources: []
tags:
- polars
- dataframes
- python
- lazy-evaluation
- query-optimization
- data-engineering
- etl
- gpu-acceleration
title: 'Python Polars: The Definitive Guide'
updated: '2026-10-07T18:46:39Z'
updated_by: op_9a030901d060
uuid: 48c7bb40-1764-55d2-b038-faa5dfc942fd
year: 2025
---

<!-- AUTHORED REGION START -->
# Python Polars: The Definitive Guide
*Transforming, Analyzing, and Visualizing Data with a Fast and Expressive DataFrame API*

**Authors:** [[entities/jeroen-janssens|Jeroen Janssens]], [[entities/thijs-nieuwdorp|Thijs Nieuwdorp]]

**Year:** 2025

**Publisher:** O'Reilly Media

**Edition:** First Edition

## Summary

This book teaches Polars, a DataFrame package written in Rust and used from Python. Polars is built on Apache Arrow's columnar memory format. It uses many CPU cores and SIMD vector instructions, and it can optionally run on NVIDIA GPUs. The authors met Polars through its creator, Ritchie Vink, when they were all colleagues at Xomnia. They then used it to rebuild a client pipeline that had become too slow and too memory-hungry in pandas and R.

The book has 18 chapters in five parts and an appendix. Part I introduces Polars, setup, and moving over from pandas. Part II covers data structures and types, the eager and lazy APIs, and reading and writing CSV, Excel, Parquet, JSON and databases. Part III is the core: expressions, defined as a tree of operations that describes how to build one or more Series. Part IV applies expressions to selecting, filtering, text and time data, group-by and window aggregations, joins (including as-of joins), and reshaping. Part V covers plotting, custom Python functions and Rust plugins, and the engine internals.

The internals chapter explains the layers. Your code is a declarative language. It becomes an intermediate plan shaped as a graph. An optimizer rewrites the plan, and an engine runs it. The optimizer pushes filters, column choices and row slices down to the file scan. It also caches repeated sub-plans, orders joins, and estimates group sizes. The appendix benchmarks the GPU engine on a TPC-H-style suite. It finds the GPU helps for compute-heavy queries on larger data, but not for small data or queries limited by disk reads.

## Key Contributions

- Defines a Polars expression as a lazy, reusable tree of operations that describes how to build one or more Series. Expressions do nothing until a context such as select, filter or group_by runs them. The book presents expressions as the idiomatic core of the API.
- Contrasts the eager DataFrame API with the lazy LazyFrame API. On a taxi-trip Parquet query, the lazy version returned the same result about ten times faster than the eager one. It also warns that each collect() call recomputes the plan from scratch unless the intermediate result is cached.
- Lists the optimizations the query planner applies: predicate, projection and slice pushdown; common subplan elimination; expression simplification; join ordering; type coercion; and cardinality estimation. Query plans can be inspected with lf.explain() and lf.show_graph(). In one example, the planner reads only 1 of the 19 columns in the taxi data.
- Reports a real migration from a mixed pandas and R pipeline to Polars. Memory use fell from over 500 GB to 40 GB, and the pipeline ran much faster.
- Covers time-based aggregation and alignment: Expr.over() for window functions, group_by_dynamic() for time-window groups, rolling() for rolling aggregations, set_sorted() and upsample(). For inexact matches on time or numeric keys, it covers join_asof() with optional by-groups, strategies and a tolerance setting.
- Describes an experimental streaming mode for out-of-core work on data larger than RAM. It is triggered with collect(streaming=True) or with sink_parquet() and similar sink methods. The book flags the mode as experimental and does not cover it further.
- Benchmarks the GPU engine on 22 TPC-H-derived queries at scale factors from 0.1 to 50. The CPU engine wins at the smallest size because moving data to the GPU costs time. From about 5 GB upwards, the GPU engine is over twice as fast as the CPU engine. Against cuDF, which shares the same libcudf base, the Polars optimizer gives a consistent 4x speedup.

## Key Topics Covered

polars-expressions, lazy-evaluation, query-pushdown-optimization, as-of-join, data-engineering-for-ml, feature-engineering, Apache Arrow columnar memory, Parquet I/O, window functions and rolling aggregation, out-of-core streaming, GPU acceleration (NVIDIA RAPIDS / cuDF), Rust plugins, migrating from pandas

## Questions Raised

- How much of the lazy-API speedup survives on narrow, already-filtered data, given that the ETL showcase gained little on one month of data and 33% on a year?
- When will the streaming engine be stable enough to rely on for larger-than-RAM jobs, given that the book calls it experimental?
- How well do the GPU results carry over beyond TPC-H-style queries, since disk-bound queries gain little and GPU memory is limited?
- Benchmarks change quickly between releases. How stable are these comparisons with pandas, DuckDB, Dask and PySpark?

## Intended Audience

Python users who wrangle data: analysts moving from pandas, data engineers who want fast single-machine pipelines without a cluster, and data scientists and software engineers. No prior Polars knowledge is assumed.

## Relevance Here

Directly useful for building bond-signal pipelines on one machine. Lazy scans of Parquet with filter and column pushdown keep memory low. join_asof aligns trades and quotes that have mismatched timestamps. Expr.over, rolling and group_by_dynamic cover per-issuer and time-window features.

## Key Concepts in This Source

- [[concepts/data-engineering-for-ml|Data Engineering for ML]]
- [[concepts/feature-engineering|Feature Engineering]]
- [[concepts/lazy-evaluation|Lazy Evaluation]]
- [[concepts/query-pushdown-optimization|Query Pushdown Optimization]]
- [[concepts/as-of-join|As-of Join]]

## Entities

- [[entities/jeroen-janssens|Jeroen Janssens]]
- [[entities/thijs-nieuwdorp|Thijs Nieuwdorp]]
- [[entities/oreilly-media|O'Reilly Media]]
- [[entities/polars|Polars]]
- [[entities/ritchie-vink|Ritchie Vink]]
- [[entities/pandas|pandas]]
- [[entities/apache-arrow|Apache Arrow]]

## Related Sources

- [[sources/reis-2022-fundamentals-data-engineering|Fundamentals of Data Engineering]]
- [[sources/khraisha-2024-financial-data-engineering|Financial Data Engineering: Design and Build Data-Driven Financial Products]]
- [[sources/nelson-2024-swe-for-data-scientists|Software Engineering for Data Scientists]]
- [[sources/percival-2020-architecture-patterns-python|Architecture Patterns with Python]]
- [[sources/alhussein-2024-databricks-certified-data-engineer|Databricks Certified Data Engineer Associate Study Guide]]
<!-- AUTHORED REGION END -->