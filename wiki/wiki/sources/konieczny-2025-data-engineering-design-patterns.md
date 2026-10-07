---
authors:
- Bartosz Konieczny
content_hash: sha256:df63906cb192d6d3ebc71bb3773a48d91042523defbc994cf16a71ac25278a61
created: '2026-10-07T18:46:39Z'
edition: Early Release
is_early_release: true
mind_map_priority: medium
page_count_estimate: null
page_id: sources/konieczny-2025-data-engineering-design-patterns
page_type: source
publisher: O'Reilly Media
raw_location: wiki/raw/ai-engineering/
related:
- concepts/data-engineering-for-ml
- concepts/batch-vs-online-prediction
- concepts/idempotent-data-pipeline
- concepts/change-data-capture
- concepts/dead-letter-pattern
- concepts/late-data-watermark
- sources/reis-2022-fundamentals-data-engineering
- sources/alhussein-2024-databricks-certified-data-engineer
- sources/girten-2024-building-modern-data-databricks
- sources/huyen-2022-designing-ml-systems
- sources/khraisha-2024-financial-data-engineering
- entities/bartosz-konieczny
- entities/oreilly-media
- entities/apache-spark
- entities/apache-kafka
- entities/apache-airflow
- entities/delta-lake
revision_id: 1
schema_version: 2
source_path: markdown_output/konieczny-2025-data-engineering-design-patterns.md
source_type: book
sources: []
tags:
- data-engineering
- design-patterns
- data-ingestion
- idempotency
- stream-processing
- batch-processing
- error-handling
- data-pipelines
title: Data Engineering Design Patterns
updated: '2026-10-07T18:46:39Z'
updated_by: op_9a030901d060
uuid: 34ec8e42-eeaa-5d8c-9d87-ee6cb24b8abd
year: 2025
---

<!-- AUTHORED REGION START -->
# Data Engineering Design Patterns
*Recipes for Solving the Most Common Data Engineering Problems*

**Authors:** [[entities/bartosz-konieczny|Bartosz Konieczny]]

**Year:** 2025

**Publisher:** O'Reilly Media

**Edition:** Early Release

**Early release.** Only part of the book was available. Chapters present: Chapter 1. Introducing Data Engineering Design Patterns; Chapter 2. Data Ingestion Design Patterns; Chapter 3. Error Management Design Patterns; Chapter 4. Idempotency Design Patterns.

## Summary

This is the third early release of a book that catalogues recurring problems in data engineering and gives each one a named, reusable solution. The author argues that classic software design patterns keep code tidy but say nothing about data issues such as backfilling, duplicates, late data or idempotency. Each pattern follows the same shape: a problem drawn from a running case study (a blog analytics platform built on a Bronze/Silver/Gold Medallion layout), a technology-neutral solution, its consequences and trade-offs, and code examples.

Only four of the planned chapters are in this release. Chapter 1 explains what a data engineering design pattern is, using a recipe analogy. Chapter 2 covers ingestion: full and incremental loading, change data capture, passthrough and transforming replication, compaction of small files, readiness markers that signal when data is complete, and external event-driven triggers. Chapter 3 covers error management: dead-lettering bad records, windowed deduplication, detecting and integrating late data, counting what each filter removes, and checkpointing streaming jobs.

Chapter 4 covers idempotency, meaning a job can be rerun any number of times and still give a consistent result. Its patterns range from fast metadata cleaning (TRUNCATE or DROP instead of DELETE) and full data overwrite, through MERGE-based upserts, to database-side approaches using stable keys or transactions, and finally a view-based proxy that keeps each dataset version immutable. Chapters 5 to 10 (data value, flow, security, storage, quality and observability) and the patterns appendix are listed as not yet available.

## Key Contributions

- Frames data engineering design patterns as reusable templates with an explicit context, solution and consequences, and argues they are needed because software patterns ignore data concerns such as backfilling, idempotency and correctness.
- Sets out a ladder of ingestion patterns: full loader when no change marker exists, incremental loader using a delta column or partitions, and change data capture from the database commit log when latency must be low and hard deletes must be seen (the case study requires changes captured within 30 seconds).
- Shows how to keep consumers from seeing partial data: a single exposure point such as a view over versioned tables for full loads, and readiness markers such as a _SUCCESS file that downstream jobs wait for.
- Describes the Dead-Letter pattern for unprocessable records: wrap risky code, send failures with error metadata to a separate resilient store, monitor its volume, and optionally replay. It warns that replays can trigger a snowball of downstream backfills.
- Treats late data in two steps: detect it with a watermark (maximum event time minus an allowed lateness), then integrate it into batch jobs with a static or dynamic lookback window, with a separate variant for pipelines whose runs overlap.
- Introduces the Filter interceptor, which counts rows removed by each filter condition, motivated by a release where filtered volume jumped to 90% from 15% and the query plan could not show which condition caused it.
- Gives a catalogue of idempotency strategies: metadata-level overwrite, data-level overwrite, MERGE on stable keys, keyed idempotency based on immutable values such as broker append time, transactional writers that hide uncommitted output (motivated by a spot-capacity job that saved 60% of cost but exposed partial data on retries), and an immutable-tables-plus-proxy-view design.

## Key Topics Covered

full and incremental loading, change data capture, data replication with and without transformation, small-file compaction, readiness markers, event-driven triggers, dead-letter queues, deduplication and state stores, late data, watermarks and lookback windows, checkpointing and delivery guarantees, idempotent overwrite and MERGE, transactional writes, immutable datasets behind a proxy view, Medallion architecture

## Questions Raised

- How should a pipeline choose between ignoring, detecting and backfilling late data when late volume is unpredictable?
- When does exactly-once processing fall short of exactly-once delivery, for example after automatic retries?
- How far back should a deduplication window or lookback window reach before cost outweighs correctness?
- Which idempotency pattern fits when the target store has no metadata layer, no transactions, or must stay immutable?

## Intended Audience

Practising data engineers who build batch and streaming pipelines and want a shared vocabulary of tested solutions. Examples assume familiarity with tools such as Apache Spark, Apache Kafka, Apache Airflow and Delta Lake.

## Key Concepts in This Source

- [[concepts/data-engineering-for-ml|Data Engineering for ML]]
- [[concepts/batch-vs-online-prediction|Batch vs Online Prediction]]
- [[concepts/idempotent-data-pipeline|Idempotent Data Pipeline]]
- [[concepts/change-data-capture|Change Data Capture]]
- [[concepts/dead-letter-pattern|Dead-Letter Pattern]]
- [[concepts/late-data-watermark|Late Data Watermark]]

## Entities

- [[entities/bartosz-konieczny|Bartosz Konieczny]]
- [[entities/oreilly-media|O'Reilly Media]]
- [[entities/apache-spark|Apache Spark]]
- [[entities/apache-kafka|Apache Kafka]]
- [[entities/apache-airflow|Apache Airflow]]
- [[entities/delta-lake|Delta Lake]]

## Related Sources

- [[sources/reis-2022-fundamentals-data-engineering|Fundamentals of Data Engineering]]
- [[sources/alhussein-2024-databricks-certified-data-engineer|Databricks Certified Data Engineer Associate Study Guide]]
- [[sources/girten-2024-building-modern-data-databricks|Building Modern Data Applications Using Databricks Lakehouse]]
- [[sources/huyen-2022-designing-ml-systems|Designing Machine Learning Systems]]
- [[sources/khraisha-2024-financial-data-engineering|Financial Data Engineering: Design and Build Data-Driven Financial Products]]
<!-- AUTHORED REGION END -->