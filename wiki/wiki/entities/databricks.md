---
content_hash: sha256:20ae72d0e1ca2a9466ca32e228d9b71d69b27e69bd29941df2e29e27ec55cc1b
created: 2026-08-06 00:00:00+00:00
entity_type: organization
mind_map_priority: low
page_id: entities/databricks
page_type: entity
related: []
revision_id: 3
schema_version: 2
sources:
- sources/girten-2024-building-modern-data-databricks
- sources/databricks-spark-knowledge-base
- sources/sreekumar-2024-datenverwaltung-unity-catalog-databricks
- sources/alhussein-2024-databricks-certified-data-engineer
- sources/pathan-2025-mastering-llm-applications-langchain
- sources/liu-2025-build-fine-tune-small-language-model
tags:
- data-platform
- spark
- lakehouse
- data-governance
- data-engineering
title: Databricks
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 613fbdfb-91d1-5f65-af2c-456218e052d8
---

<!-- AUTHORED REGION START -->
# Databricks

Company behind the data platform of the same name. It appears in this wiki as the subject of four ingested books rather than as a research entity, so what follows describes the platform as those books present it.

## What the Sources Cover

**The lakehouse pattern.** [[sources/girten-2024-building-modern-data-databricks|Girten (2024)]] traces the progression from data warehouses to data lakes to the lakehouse, then covers Delta Live Tables for near-real-time ingestion and transformation, Unity Catalog for governance and lineage, and CI/CD deployment via Terraform and Databricks Asset Bundles.

**Governance.** [[sources/sreekumar-2024-datenverwaltung-unity-catalog-databricks|Sreekumar & Subbarao]] treat Unity Catalog in depth — architecture, identity management, access control, AI governance, observability, data sharing and regulatory compliance — with a fictional organisation used as a running case study. The edition in this wiki is the German translation, machine-translated by the publisher.

**Spark practice.** The [[sources/databricks-spark-knowledge-base|Databricks Spark Knowledge Base]] is a reference on common Apache Spark patterns and pitfalls: preferring `reduceByKey` over `groupByKey`, avoiding large driver-side collects, handling malformed input with `flatMap`, plus troubleshooting for serialisation failures and missing dependencies, and guidance on RDD partitioning and data locality. Its Maven examples reference Spark 1.1.0, so the material is old.

**Certification.** [[sources/alhussein-2024-databricks-certified-data-engineer|Alhussein (2024)]] is a study guide for the Data Engineer Associate certification.

## Caveat

These are vendor-oriented practitioner books, not independent evaluations. They describe how the platform is intended to be used, not how it compares to alternatives.

## See Also

[[sources/girten-2024-building-modern-data-databricks|Building Modern Data Applications Using Databricks Lakehouse]] · [[sources/databricks-spark-knowledge-base|Databricks Spark Knowledge Base]]

## Papers in This Wiki

- [[sources/pathan-2025-mastering-llm-applications-langchain|Mastering LLM Applications with LangChain and Hugging Face]]
- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025)
<!-- AUTHORED REGION END -->