---
title: "Databricks Spark Knowledge Base (Chinese Edition)"
page_id: sources/databricks-spark-knowledge-base-cn
page_type: source
revision_id: 1
created: 2026-06-19T00:00:00Z
updated: 2026-06-19T00:00:00Z
updated_by: batch_ingest_technical_books_2026_06_19
tags: [apache-spark, databricks, distributed-computing, rdd, spark-streaming, chinese-translation, best-practices]
sources: [sources/databricks-spark-knowledge-base-cn]
related: []
mind_map_priority: low
authors: ["Databricks"]
year: 2023
source_type: book
---

# Databricks Spark Knowledge Base (Chinese Edition)

**Authors:** Databricks  
**Year:** 2023  
**Type:** book  
**Markdown source:** `markdown_output/databricks-spark-knowledge-base-cn.md`

## Summary

The Databricks Spark Knowledge Base (Chinese Edition) is a translated technical reference compiled from the official Databricks GitBook (http://databricks.gitbooks.io/databricks-spark-knowledge-base/). It is a concise, practitioner-oriented guide covering Apache Spark best practices, common fault troubleshooting, performance optimization, and Spark Streaming diagnostics — written in simplified Chinese for Chinese-speaking data engineers and developers working with Spark clusters. The TOC is present in the first few lines; the remainder of the first 250 lines is the actual chapter content, not a preface or author introduction.

## Key Claims

- Prefer reduceByKey over groupByKey for aggregations on large datasets, because reduceByKey combines values per partition before shuffling, whereas groupByKey moves all key-value pairs across the network unconditionally.
- Never call collect() on a large RDD onto the driver; use take(), takeSample(), or write to a file/database instead to avoid driver OOM.
- Task-not-serializable errors occur when an object initialized on the master is used in a worker lambda without implementing Java Serializable; fixes include implementing Serializable, declaring objects inside lambdas, or using forEachPartition.
- Maven builds do not include dependency JARs by default; use shaded/uber JARs and mark Spark libraries as <scope>provided</scope> to avoid ClassNotFoundException on workers.
- Alternative aggregation functions (combineByKey, foldByKey) should be preferred over groupByKey.
- The book is a translation of the official Databricks GitBook and its copyright belongs to the original authors; the Chinese translation is licensed separately.

## Main Concepts

- [[concepts/rdd-partitioning-and-shuffling|RDD partitioning and shuffling]]
- [[concepts/groupbykey-vs-reducebykey-trade-offs|GroupByKey vs ReduceByKey trade-offs]]
- [[concepts/driver-memory-management-and-collect()-pitfalls|Driver memory management and collect() pitfalls]]
- [[concepts/java-serialization-in-distributed-spark-tasks|Java serialization in distributed Spark tasks]]
- [[concepts/maven-dependency-management-for-spark-(uber/shaded-jars)|Maven dependency management for Spark (uber/shaded JARs)]]
- [[concepts/spark-streaming-fault-handling-(oneforonestrategy-error)|Spark Streaming fault handling (OneForOneStrategy error)]]
- [[concepts/data-locality-in-spark|Data locality in Spark]]

## Key Entities

- [[entities/databricks|Databricks]]
- [[entities/apache-spark|Apache Spark]]
- [[entities/apache-maven|Apache Maven]]
- [[entities/spark-streaming|Spark Streaming]]

## Questions Raised

- How do the best practices described here map to Spark's DataFrame/Dataset API, which supersedes the RDD API covered in this guide?
- What version of Spark does this knowledge base target, and which recommendations have been superseded by later Spark releases?
- Are there equivalent Databricks-published guides for PySpark users, given that all code samples in the first 250 lines are in Scala/Java?
