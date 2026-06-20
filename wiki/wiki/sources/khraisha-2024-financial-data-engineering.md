---
title: 'Financial Data Engineering: Design and Build Data-Driven Financial Products'
page_id: sources/khraisha-2024-financial-data-engineering
page_type: source
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_technical_books_2_2026_06_19
tags:
- financial-data-engineering
- data-engineering
- finance
- data-governance
- data-pipelines
- databases
- cloud-computing
- machine-learning
- big-data
- regulatory-compliance
- python
- sql
- postgresql
- oreilly
- 2024
- practitioner-guide
- fintech
sources:
- sources/khraisha-2024-financial-data-engineering
related: []
mind_map_priority: high
authors:
- Tamer Khraisha
year: 2024
source_type: book
schema_version: 2
uuid: 8707400e-fa9d-5fbf-b7ab-c9924c9c1439
content_hash: sha256:adb3d0a08e44b0ce99f76628470ac79dbae19989f6db542112f8842c49253a33
---

<!-- AUTHORED REGION START -->
# Financial Data Engineering: Design and Build Data-Driven Financial Products

**Authors:** Tamer Khraisha  
**Year:** 2024  
**Type:** book  
**Markdown source:** `markdown_output/khraisha-2024-financial-data-engineering.md`

## Summary

Financial Data Engineering: Design and Build Data-Driven Financial Products (O'Reilly, first edition October 2024, ISBN 978-1-098-15999-3) by Tamer Khraisha is a comprehensive practitioner guide that bridges data engineering and the financial domain. The book defines "financial data engineering" as a domain-driven specialization of data engineering tailored to the distinct regulatory, governance, security, and data-management requirements of financial markets. It covers the full financial data engineering lifecycle across 12 chapters in two parts: Part I (Chapters 1–5) builds finance-domain foundations (financial data ecosystem, identification/entity systems, data governance), and Part II (Chapters 6–12) covers data engineering practice (storage, modeling, databases, workflows, ingestion, transformation) with finance-specific applications. Chapter 12 presents four hands-on projects using Python, SQL/PostgreSQL, JupyterLab, Pandas, Docker, and Git. The book uses more than 1,000 references and is supplemented by a GitHub repository.

## Key Claims

- Financial data engineering is a domain-driven specialization of data engineering tailored to the security, governance, regulatory, and data-management requirements of the financial sector.
- Data preparation and preprocessing accounts for approximately 50–80% of the time in AI and machine learning projects, making financial data engineering critical to ML workflows.
- JPMorgan Chase manages more than 450 petabytes of data; Bank of New York Mellon manages over 110 million gigabytes of global financial data (cited from McKinsey Global Institute 2011 report).
- The book is structured in two balanced halves: Chapters 1–5 lean toward finance domain knowledge; Chapters 6–12 focus on data engineering practice and technologies.
- The big data era in data engineering began around 2005 with the release of Apache Hadoop, driven by Google, Airbnb, Meta, Microsoft, Amazon, and Netflix.
- Chapter 8 on databases takes an abstract approach focused on data storage models rather than specific technologies to ensure longevity given rapid database evolution.
- PDFs and complex academic papers require a processing pipeline (text extraction, citation parsing, equation OCR) before they can be used in LLM-based workflows — illustrated by the book's own conversion in this repository.
- The book uses more than one thousand references spanning scientific journals, books, blog posts, online articles, opinion pieces, and white papers.

## Main Concepts

- [[concepts/financial-data-engineering-domain-driven-specialization-|Financial data engineering (domain-driven specialization)]]
- [[concepts/financial-data-ecosystem-structure-and-characteristics|Financial data ecosystem structure and characteristics]]
- [[concepts/financial-identification-and-entity-systems|Financial identification and entity systems]]
- [[concepts/data-governance-frameworks-for-financial-institutions|Data governance frameworks for financial institutions]]
- [[concepts/data-storage-models-and-database-selection|Data storage models and database selection]]
- [[concepts/data-modeling-for-financial-data|Data modeling for financial data]]
- [[concepts/data-workflows-and-pipeline-orchestration|Data workflows and pipeline orchestration]]
- [[concepts/data-ingestion-mechanisms|Data ingestion mechanisms]]
- [[concepts/data-transformation|Data transformation]]
- [[concepts/big-data-and-cloud-computing-in-finance|Big data and cloud computing in finance]]
- [[concepts/regulatory-compliance-and-financial-data-management|Regulatory compliance and financial data management]]
- [[concepts/tokenization-in-financial-data|Tokenization in financial data]]
- [[concepts/machine-learning-and-generative-ai-in-financial-context|Machine learning and generative AI in financial context]]
- [[concepts/data-quality-and-data-integrity-frameworks|Data quality and data integrity frameworks]]
- [[concepts/sql-and-data-warehousing-history|SQL and data warehousing history]]

## Key Entities

- [[entities/tamer-khraisha-author-background-in-financial-economics-network-science-fintech-|Tamer Khraisha (author; background in financial economics, network science, fintech)]]
- [[entities/martijn-groot-foreword-author-financial-data-management-expert-author-of-managing-financial-information-in-the-trade-lifecycle-elsevier-2008-and-a-primer-in-financial-data-management-elsevier-2017-|Martijn Groot (foreword author; Financial Data Management expert; author of Managing Financial Information in the Trade Lifecycle, Elsevier 2008, and A Primer in Financial Data Management, Elsevier 2017)]]
- [[entities/brian-buzzelli-afterword-author-head-of-data-practice-meradia-|Brian Buzzelli (afterword author; Head of Data Practice, Meradia)]]
- [[entities/o-reilly-media-publisher-|O'Reilly Media (publisher)]]
- [[entities/mckinsey-global-institute-cited-for-2011-banking-data-report-|McKinsey Global Institute (cited for 2011 banking data report)]]
- [[entities/jpmorgan-chase-data-volume-example-450-petabytes-|JPMorgan Chase (data volume example: 450+ petabytes)]]
- [[entities/bank-of-new-york-mellon-data-volume-example-110m-gigabytes-|Bank of New York Mellon (data volume example: 110M+ gigabytes)]]
- [[entities/apache-hadoop-big-data-era-reference-point-2005-|Apache Hadoop (big data era reference point, ~2005)]]
- [[entities/ibm-and-oracle-early-sql-data-warehousing-pioneers-1970s-1980s-|IBM and Oracle (early SQL/data warehousing pioneers, 1970s–1980s)]]
- [[entities/bloomberg-data-vendor-example-|Bloomberg (data vendor example)]]
- [[entities/london-stock-exchange-group-lseg-data-vendor-example-|London Stock Exchange Group / LSEG (data vendor example)]]
- [[entities/nyse-london-stock-exchange-chicago-mercantile-exchange-security-exchanges-|NYSE, London Stock Exchange, Chicago Mercantile Exchange (security exchanges)]]
- [[entities/federal-reserve-european-central-bank-central-banks-|Federal Reserve, European Central Bank (central banks)]]
- [[entities/securities-and-exchange-commission-regulator-|Securities and Exchange Commission (regulator)]]
- [[entities/blackrock-vanguard-group-asset-managers-|BlackRock, Vanguard Group (asset managers)]]
- [[entities/citadel-renaissance-technologies-hedge-funds-|Citadel, Renaissance Technologies (hedge funds)]]
- [[entities/revolut-wise-betterment-fintech-companies-|Revolut, Wise, Betterment (FinTech companies)]]
- [[entities/amazon-google-apple-big-tech-in-finance-|Amazon, Google, Apple (big tech in finance)]]
- [[entities/morgan-stanley-goldman-sachs-investment-banks-|Morgan Stanley, Goldman Sachs (investment banks)]]
- [[entities/s-p-global-ratings-moody-s-credit-rating-agencies-|S&P Global Ratings, Moody's (credit rating agencies)]]
- [[entities/fannie-mae-freddie-mac-government-sponsored-enterprises-|Fannie Mae, Freddie Mac (government-sponsored enterprises)]]
- [[entities/linkedin-netflix-google-meta-airbnb-open-source-data-framework-contributors-|LinkedIn, Netflix, Google, Meta, Airbnb (open-source data framework contributors)]]
- [[entities/shivani-gole-technical-reviewer-data-engineer-mckinsey-|Shivani Gole (technical reviewer; Data Engineer, McKinsey)]]
- [[entities/pankaj-gupta-technical-reviewer-manager-data-engineering-discover-financial-services-|Pankaj Gupta (technical reviewer; Manager Data Engineering, Discover Financial Services)]]
- [[entities/aakash-atul-alurkar-technical-reviewer-senior-pm-financial-services-zoom-|Aakash Atul Alurkar (technical reviewer; Senior PM Financial Services, Zoom)]]
- [[entities/ganesh-harke-technical-reviewer-tech-lead-citibank-n-a-|Ganesh Harke (technical reviewer; Tech Lead, Citibank N.A.)]]
- [[entities/abdullah-karasan-technical-reviewer-founder-leveragai-adjunct-faculty-umbc-|Abdullah Karasan (technical reviewer; Founder, Leveragai; Adjunct Faculty, UMBC)]]
- [[entities/johnnie-jones-technical-reviewer-director-of-data-engineering-boeing-employee-credit-union-becu-|Johnnie Jones (technical reviewer; Director of Data Engineering, Boeing Employee Credit Union BECU)]]
- [[entities/vipul-bharat-marlecha-technical-reviewer-senior-data-engineer-netflix-|Vipul Bharat Marlecha (technical reviewer; Senior Data Engineer, Netflix)]]
- [[entities/rosario-nunzio-mantegna-acknowledged-contributor-|Rosario Nunzio Mantegna (acknowledged contributor)]]

## Questions Raised

- How does the book's abstract database chapter (Chapter 8) map to specific current technologies such as DuckDB, Apache Iceberg, or cloud-native warehouses?
- What are the four hands-on projects in Chapter 12 and which specific financial market problems do they address?
- How does the book treat tokenization of financial assets in relation to data engineering pipelines?
- What specific regulatory frameworks (e.g., MiFID II, Basel III, GDPR) are covered in the data governance chapter?
- How does the book differentiate financial data engineering from financial ML engineering or quant development roles?
- Does the book cover real-time/streaming data pipelines for market data, or primarily batch processing?

<!-- AUTHORED REGION END -->
