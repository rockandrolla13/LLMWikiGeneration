---
title: Datenverwaltung mit Unity Catalog auf Databricks
page_id: sources/sreekumar-2024-datenverwaltung-unity-catalog-databricks
page_type: source
verification:
  status: unverified
  unverified_claims: 0
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_technical_books_2_2026_06_19
tags:
- data-governance
- unity-catalog
- databricks
- lakehouse
- data-engineering
- ai-governance
- access-control
- identity-management
- gdpr
- compliance
- delta-sharing
- open-source
- data-platform
- o'reilly
- german-translation
- practical-guide
sources:
- sources/sreekumar-2024-datenverwaltung-unity-catalog-databricks
related: []
mind_map_priority: medium
authors:
- Kiran Sreekumar
- Karthik Subbarao
year: 2024
source_type: book
schema_version: 2
uuid: 6c59d15a-39ec-5a8f-9b9d-0dc2ff407f12
content_hash: sha256:ba68f62fee1e3d1e8b151bab346fe6142e09f351e4ef1066d83d3faa44fb908f
---

<!-- AUTHORED REGION START -->
# Datenverwaltung mit Unity Catalog auf Databricks

**Authors:** Kiran Sreekumar, Karthik Subbarao  
**Year:** 2024  
**Type:** book  
**Markdown source:** none retained. This page was written by a 2026-06-19 batch ingest that recorded `markdown_output/sreekumar-2024-datenverwaltung-unity-catalog-databricks.md`, which was never produced. Claims here are not machine-checkable until the document is converted.
## Summary

A German-language O'Reilly book (first edition, September 2025) titled "Datenverwaltung mit Unity Catalog auf Databricks" (original English title: "Data Governance with Unity Catalog on Databricks") by Kiran Sreekumar and Karthik Subbarao, with a foreword by Matei Zaharia (CTO and co-founder of Databricks). The book provides a comprehensive practical guide to implementing data and AI governance using Databricks Unity Catalog, covering its architecture, identity management, access controls, AI governance, observability, data sharing, regulatory compliance, and adoption strategies. A fictional organization called "Nexa Boutique" is used as a case study throughout. The book was translated into German by AI (O'Reilly). ISBN 978-1-098-17963-2.

## Key Claims

- Unity Catalog is the first unified governance system for both data and AI in the industry, developed by Databricks starting in 2020.
- The book argues that the next era of data management will be defined by catalogs, following a decade dominated by file format development.
- Unity Catalog became open source during the writing of this book, enabling new governance innovation beyond traditional proprietary tools.
- Unity Catalog is described as a true multimodal catalog supporting Delta and Iceberg REST catalogs, tables, views, cloud storage, AI models, and functions.
- The authors had over three years of hands-on experience with Unity Catalog before writing the book.
- Delta Sharing Protocol, pioneered by Databricks, is described as one of the largest ecosystems for cross-enterprise data sharing.
- The majority of Databricks workloads now run on Unity Catalog, with customers reporting significant improvements from Unified Governance simplicity.
- Official Databricks documentation takes precedence over the book in case of discrepancies — the book is not written by or on behalf of Databricks.

## Main Concepts

- Data Governance
- Unity Catalog
- Lakehouse architecture
- Databricks Data Intelligence Platform
- Identity Management (SSO, identity provisioning)
- Access Controls and Permissions Model
- AI/ML Governance
- Observability and Data Discoverability
- Data Sharing and Collaboration (Delta Sharing)
- Open Access / Open Source Catalog
- Regulatory Compliance (GDPR)
- Hive Metastore (HMS) migration
- Compute access modes (Standard, Dedicated, Serverless)
- Cross-Metastore Governance
- Open Formats (Delta, Apache Iceberg)
- ETL Pipeline Governance
- Data Quality

## Key Entities

- Kiran Sreekumar (author)
- Karthik Subbarao (also cited as Karthikeya Sampa Subbarao, author)
- Matei Zaharia (CTO and co-founder of Databricks, foreword author)
- Databricks (platform company)
- O'Reilly Media (publisher)
- Nexa Boutique (fictional case-study organization)
- Ashok Singamaneni (Senior Software Engineer at Nike, endorser)
- Tristen Wentling (Lead Solutions Architect at Databricks, endorser)
- Lars George (Lead Product Specialist at Databricks, endorser)
- Arup Nanda (Managing Director, Head of Data and AI at JPMorganChase, endorser)
- Nike (mentioned in endorsements)
- JPMorganChase (mentioned in endorsements)
- Aaron Black (Acquisitions Editor)
- Corbin Collins (Development Editor)

## Questions Raised

- How does Unity Catalog's open-source governance model compare to competing catalogs such as Apache Polaris or AWS Glue?
- What are the concrete migration steps from Hive Metastore (HMS) to Unity Catalog described in Chapter 11?
- How does Unity Catalog handle AI model governance differently from traditional data governance?
- What specific GDPR compliance mechanisms does the book describe in Chapter 10?
- How does the Delta Sharing Protocol integrate with Unity Catalog's cross-metastore governance?
- What are the trade-offs between Standard, Dedicated, and Serverless compute access modes in Unity Catalog?

<!-- AUTHORED REGION END -->
