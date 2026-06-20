---
title: Fundamentals of Data Engineering
page_id: sources/reis-2022-fundamentals-data-engineering
page_type: source
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_technical_books_2_2026_06_19
tags:
- data-engineering
- data-lifecycle
- etl
- cloud-first
- data-architecture
- data-governance
- security-privacy
- big-data
- streaming
- orchestration
- data-warehousing
- data-lakes
- o'reilly
- 2022
- textbook
sources:
- sources/reis-2022-fundamentals-data-engineering
related: []
mind_map_priority: medium
authors:
- Joe Reis
- Matt Housley
year: 2022
source_type: book
schema_version: 2
uuid: 3c78378e-fc71-51ad-8790-57bb7ecade39
content_hash: sha256:39427c26167eb636299f431862df34d0fce382cd5881792300fd98c65ef6b5c6
---

<!-- AUTHORED REGION START -->
# Fundamentals of Data Engineering

**Authors:** Joe Reis, Matt Housley  
**Year:** 2022  
**Type:** book  
**Markdown source:** `markdown_output/reis-2022-fundamentals-data-engineering.md`

## Summary

Fundamentals of Data Engineering (O'Reilly, June 2022, First Edition) by Joe Reis and Matt Housley is a technology-agnostic, cloud-first reference book that defines the data engineering lifecycle — generation, storage, ingestion, transformation, and serving — and shows practitioners how to assemble disparate tools and technologies into coherent, production-grade data systems. The authors, self-described "recovering data scientists," wrote the book to fill a gap between narrow tool-specific guides and real-world end-to-end system design. The book is organised into four parts: foundational concepts and architecture principles (Part I), a deep-dive into each lifecycle stage (Part II), security/privacy and the future of data engineering (Part III), and appendices on cloud networking and serialisation/compression. It takes a deliberately cloud-first stance, treating infrastructure as ephemeral and scalable, while aiming to articulate principles that will remain relevant for a decade or more.

## Key Claims

- The central organizing framework is the data engineering lifecycle: generation, storage, ingestion, transformation, and serving — stages that have remained essentially unchanged despite constant tool churn.
- Data engineering is positioned as the foundation that data science and analytics in production depend on; many data science failures trace back to missing data engineering infrastructure.
- The book is deliberately technology-agnostic and cloud-first; it avoids tool-specific instruction in favour of durable principles applicable to any relevant technology.
- Security and privacy (GDPR, CCPA, state-sponsored cyber threats) are framed as top-priority concerns, not afterthoughts, in modern data engineering work.
- Good architecture and technology choice are treated as distinct topics that are frequently (and incorrectly) conflated in the industry.
- The authors argue that most on-premises data systems will eventually migrate to cloud hosting, and that managed cloud services are the default deployment target for data engineers.

## Main Concepts

- [[concepts/data-engineering-lifecycle-generation-storage-ingestion-transformation-serving-|Data engineering lifecycle (generation, storage, ingestion, transformation, serving)]]
- [[concepts/data-architecture-principles|Data architecture principles]]
- [[concepts/technology-selection-framework|Technology selection framework]]
- [[concepts/cloud-first-infrastructure-and-ephemeral-scalable-systems|Cloud-first infrastructure and ephemeral/scalable systems]]
- [[concepts/data-governance-security-and-privacy-gdpr-ccpa-|Data governance, security, and privacy (GDPR, CCPA)]]
- [[concepts/etl-and-data-pipeline-design|ETL and data pipeline design]]
- [[concepts/big-data-frameworks-mapreduce-spark-flink-|Big Data frameworks (MapReduce, Spark, Flink)]]
- [[concepts/data-warehousing-and-data-lakes|Data warehousing and data lakes]]
- [[concepts/batch-and-streaming-systems|Batch and streaming systems]]
- [[concepts/orchestration|Orchestration]]
- [[concepts/serialisation-and-compression|Serialisation and compression]]
- [[concepts/cloud-networking|Cloud networking]]

## Key Entities

- [[entities/joe-reis-author-co-founder-ternary-data-|Joe Reis (author, co-founder Ternary Data)]]
- [[entities/matt-housley-author-co-founder-ternary-data-|Matt Housley (author, co-founder Ternary Data)]]
- [[entities/o-reilly-media-publisher-|O'Reilly Media (publisher)]]
- [[entities/bill-inmon-technical-reviewer-and-industry-expert-|Bill Inmon (technical reviewer and industry expert)]]
- [[entities/zhamak-dehghani-data-mesh-architect-mentioned-as-expert-consulted-|Zhamak Dehghani (data mesh architect, mentioned as expert consulted)]]
- [[entities/jordan-tigani-expert-consulted-|Jordan Tigani (expert consulted)]]
- [[entities/maxime-beauchemin-quoted-expert-defined-data-engineering-as-superset-of-bi-data-warehousing-software-engineering-|Maxime Beauchemin (quoted expert, defined data engineering as superset of BI/data warehousing + software engineering)]]
- [[entities/jesse-anderson-quoted-expert-two-type-taxonomy-sql-focused-vs-big-data-focused-|Jesse Anderson (quoted expert, two-type taxonomy: SQL-focused vs Big Data-focused)]]
- [[entities/lewis-gavin-quoted-expert-|Lewis Gavin (quoted expert)]]
- [[entities/alexsoft-quoted-definition-source-|AlexSoft (quoted definition source)]]
- [[entities/aws-azure-google-cloud-platform-cloud-platforms-referenced-for-prerequisites-|AWS, Azure, Google Cloud Platform (cloud platforms referenced for prerequisites)]]
- [[entities/snowflake-databricks-data-platforms-referenced-for-prerequisites-|Snowflake, Databricks (data platforms referenced for prerequisites)]]
- [[entities/hadoop-cassandra-hbase-spark-flink-big-data-technologies-cited-in-definitions-|Hadoop, Cassandra, HBase, Spark, Flink (Big Data technologies cited in definitions)]]

## Questions Raised

- How does the data engineering lifecycle framework apply to streaming-first architectures where the generation-ingestion-transformation boundary is blurred?
- The book promises principles that will last a decade — which specific architectural choices made in 2022 are most at risk of aging poorly?
- How does the framework handle the boundary between data engineering and ML engineering / MLOps, especially around feature stores and model serving pipelines?
- The authors dismiss on-premises systems as transitional — how does the framework adapt for regulated industries (finance, healthcare) with persistent on-premises or hybrid requirements?
- What concrete operationalisation of data governance does the book provide beyond naming GDPR and CCPA as motivators?

<!-- AUTHORED REGION END -->
