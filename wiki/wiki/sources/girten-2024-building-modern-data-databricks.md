---
title: "Building Modern Data Applications Using Databricks Lakehouse"
page_id: sources/girten-2024-building-modern-data-databricks
page_type: source
revision_id: 1
created: 2026-06-19T00:00:00Z
updated: 2026-06-19T00:00:00Z
updated_by: batch_ingest_technical_books_2026_06_19
tags: [databricks, lakehouse, delta-lake, data-engineering, etl, data-governance]
sources: [sources/girten-2024-building-modern-data-databricks]
related: []
mind_map_priority: high
authors: ["Will Girten"]
year: 2024
source_type: book
---

# Building Modern Data Applications Using Databricks Lakehouse

**Authors:** Will Girten  
**Year:** 2024  
**Type:** book  
**Markdown source:** `markdown_output/girten-2024-building-modern-data-databricks.md`

## Summary

Building Modern Data Applications Using Databricks Lakehouse (Packt, October 2024) by Will Girten is a practitioner-oriented guide to designing and deploying production-ready data pipelines on the Databricks Data Intelligence Platform. It walks through the evolution from data warehouses to data lakes to the lakehouse pattern, then systematically covers the Delta Live Tables (DLT) framework for near-real-time ingestion and transformation, Unity Catalog for data governance and lineage, and CI/CD tooling (Terraform, Databricks Asset Bundles) for pipeline deployment and monitoring across environments.

## Key Claims

- The lakehouse architecture combines fast BI query speeds of a traditional data warehouse with the scalable ETL processing of big data in the cloud, solving the 'data swamp' problem of early data lakes.
- Delta Live Tables (DLT) eliminates the maintenance burden of building streaming solutions from scratch, providing a declarative framework for near-real-time pipeline design.
- Unity Catalog provides fine-grained row- and column-level access control, metadata tagging for data discovery, and end-to-end data lineage tracing within Databricks.
- Databricks was named a Leader in the 2024 Gartner Magic Quadrant for Data Science and Machine Learning Platforms, signaling growing enterprise demand for the platform.
- CI/CD automation via Terraform and Databricks Asset Bundles (DABs) enables reproducible, multi-environment deployment of data pipelines.
- The Lambda architecture (batch + streaming separation) was an early workaround for concurrent write conflicts, but the lakehouse pattern aims to supersede it.
- Beginner-level knowledge of Python and Apache Spark is sufficient to follow the hands-on examples; no advanced background is required.

## Main Concepts

- [[concepts/delta-live-tables-(dlt)-framework|Delta Live Tables (DLT) framework]]
- [[concepts/lakehouse-architecture-and-medallion-architecture-(bronze/silver/gold)|Lakehouse architecture and medallion architecture (bronze/silver/gold)]]
- [[concepts/delta-lake-format|Delta Lake format]]
- [[concepts/unity-catalog-(data-governance,-lineage,-access-control)|Unity Catalog (data governance, lineage, access control)]]
- [[concepts/ci/cd-for-data-pipelines-(terraform,-databricks-asset-bundles)|CI/CD for data pipelines (Terraform, Databricks Asset Bundles)]]
- [[concepts/auto-loader-and-real-time-data-ingestion|Auto Loader and real-time data ingestion]]
- [[concepts/data-quality-monitoring-with-expectations|Data quality monitoring with Expectations]]

## Key Entities

- [[entities/will-girten-author-lead-specialist-solutions-architect-at-databricks-|Will Girten (author, lead specialist solutions architect at Databricks)]]
- [[entities/databricks-platform-provider-|Databricks (platform provider)]]
- [[entities/packt-publishing-publisher-|Packt Publishing (publisher)]]
- [[entities/apache-spark-underlying-processing-engine-|Apache Spark (underlying processing engine)]]
- [[entities/apache-hadoop-historical-big-data-engine-mentioned-in-evolution-narrative-|Apache Hadoop (historical big data engine mentioned in evolution narrative)]]
- [[entities/mlflow-open-source-component-of-databricks-platform-|MLflow (open source component of Databricks platform)]]
- [[entities/gartner-cited-for-2024-magic-quadrant-recognition-of-databricks-|Gartner (cited for 2024 Magic Quadrant recognition of Databricks)]]

## Questions Raised

- How does the DLT framework handle schema evolution and late-arriving data compared to hand-rolled Spark Structured Streaming solutions?
- What are the cost trade-offs between DLT pipeline editions (Core vs. Pro vs. Advanced) in production, given the book references DBU consumption per pipeline run?
- Does Unity Catalog's lineage tracking extend to ML models and feature stores, or is it scoped only to tabular data assets?
