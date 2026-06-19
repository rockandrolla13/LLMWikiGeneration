---
title: "Datenverwaltung mit Unity Catalog auf Databricks"
page_id: sources/sreekumar-2024-datenverwaltung-unity-catalog-databricks
page_type: source
revision_id: 1
created: 2026-06-19T00:00:00Z
updated: 2026-06-19T00:00:00Z
updated_by: batch_ingest_technical_books_2_2026_06_19
tags: [data-governance, unity-catalog, databricks, lakehouse, data-engineering, ai-governance, access-control, identity-management, gdpr, compliance, delta-sharing, open-source, data-platform, o'reilly, german-translation, practical-guide]
sources: [sources/sreekumar-2024-datenverwaltung-unity-catalog-databricks]
related: []
mind_map_priority: medium
authors: ["Kiran Sreekumar", "Karthik Subbarao"]
year: 2024
source_type: book
---

# Datenverwaltung mit Unity Catalog auf Databricks

**Authors:** Kiran Sreekumar, Karthik Subbarao  
**Year:** 2024  
**Type:** book  
**Markdown source:** `markdown_output/sreekumar-2024-datenverwaltung-unity-catalog-databricks.md`

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

- [[concepts/data-governance|Data Governance]]
- [[concepts/unity-catalog|Unity Catalog]]
- [[concepts/lakehouse-architecture|Lakehouse architecture]]
- [[concepts/databricks-data-intelligence-platform|Databricks Data Intelligence Platform]]
- [[concepts/identity-management-sso-identity-provisioning-|Identity Management (SSO, identity provisioning)]]
- [[concepts/access-controls-and-permissions-model|Access Controls and Permissions Model]]
- [[concepts/ai-ml-governance|AI/ML Governance]]
- [[concepts/observability-and-data-discoverability|Observability and Data Discoverability]]
- [[concepts/data-sharing-and-collaboration-delta-sharing-|Data Sharing and Collaboration (Delta Sharing)]]
- [[concepts/open-access-open-source-catalog|Open Access / Open Source Catalog]]
- [[concepts/regulatory-compliance-gdpr-|Regulatory Compliance (GDPR)]]
- [[concepts/hive-metastore-hms-migration|Hive Metastore (HMS) migration]]
- [[concepts/compute-access-modes-standard-dedicated-serverless-|Compute access modes (Standard, Dedicated, Serverless)]]
- [[concepts/cross-metastore-governance|Cross-Metastore Governance]]
- [[concepts/open-formats-delta-apache-iceberg-|Open Formats (Delta, Apache Iceberg)]]
- [[concepts/etl-pipeline-governance|ETL Pipeline Governance]]
- [[concepts/data-quality|Data Quality]]

## Key Entities

- [[entities/kiran-sreekumar-author-|Kiran Sreekumar (author)]]
- [[entities/karthik-subbarao-also-cited-as-karthikeya-sampa-subbarao-author-|Karthik Subbarao (also cited as Karthikeya Sampa Subbarao, author)]]
- [[entities/matei-zaharia-cto-and-co-founder-of-databricks-foreword-author-|Matei Zaharia (CTO and co-founder of Databricks, foreword author)]]
- [[entities/databricks-platform-company-|Databricks (platform company)]]
- [[entities/o-reilly-media-publisher-|O'Reilly Media (publisher)]]
- [[entities/nexa-boutique-fictional-case-study-organization-|Nexa Boutique (fictional case-study organization)]]
- [[entities/ashok-singamaneni-senior-software-engineer-at-nike-endorser-|Ashok Singamaneni (Senior Software Engineer at Nike, endorser)]]
- [[entities/tristen-wentling-lead-solutions-architect-at-databricks-endorser-|Tristen Wentling (Lead Solutions Architect at Databricks, endorser)]]
- [[entities/lars-george-lead-product-specialist-at-databricks-endorser-|Lars George (Lead Product Specialist at Databricks, endorser)]]
- [[entities/arup-nanda-managing-director-head-of-data-and-ai-at-jpmorganchase-endorser-|Arup Nanda (Managing Director, Head of Data and AI at JPMorganChase, endorser)]]
- [[entities/nike-mentioned-in-endorsements-|Nike (mentioned in endorsements)]]
- [[entities/jpmorganchase-mentioned-in-endorsements-|JPMorganChase (mentioned in endorsements)]]
- [[entities/aaron-black-acquisitions-editor-|Aaron Black (Acquisitions Editor)]]
- [[entities/corbin-collins-development-editor-|Corbin Collins (Development Editor)]]

## Questions Raised

- How does Unity Catalog's open-source governance model compare to competing catalogs such as Apache Polaris or AWS Glue?
- What are the concrete migration steps from Hive Metastore (HMS) to Unity Catalog described in Chapter 11?
- How does Unity Catalog handle AI model governance differently from traditional data governance?
- What specific GDPR compliance mechanisms does the book describe in Chapter 10?
- How does the Delta Sharing Protocol integrate with Unity Catalog's cross-metastore governance?
- What are the trade-offs between Standard, Dedicated, and Serverless compute access modes in Unity Catalog?
