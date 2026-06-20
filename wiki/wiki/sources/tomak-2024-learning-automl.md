---
title: Learning AutoML
page_id: sources/tomak-2024-learning-automl
page_type: source
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_3_2026_06_19
tags:
- automl
- machine-learning
- autogluon
- mlops
- hyperparameter-optimisation
- neural-architecture-search
- tabular-data
- nlp
- time-series
- computer-vision
- production-ml
- fairness
- explainability
- healthcare-ai
- fraud-detection
- demand-forecasting
- oreilly
- python
- citizen-data-science
- analytical-ai
sources:
- sources/tomak-2024-learning-automl
related: []
mind_map_priority: high
authors:
- Kerem Tomak
year: 2024
source_type: book
schema_version: 2
uuid: fb1e393d-08ec-5354-8135-737086f70910
content_hash: sha256:ac1877f20f319a29355b107b897b22bf700aa51b7dbddae9b584a6f3b2ace0f7
---

<!-- AUTHORED REGION START -->
# Learning AutoML

**Authors:** Kerem Tomak  
**Year:** 2024  
**Type:** book  
**Markdown source:** `markdown_output/tomak-2024-learning-automl.md`

## Summary

Learning AutoML by Kerem Tomak (published April 2026 by O'Reilly Media, ISBN 979-8-341-64318-5) is a comprehensive guide to automated machine learning covering everything from foundational concepts through production deployment. The book bridges organisational/business and technical perspectives, with a strong focus on AutoGluon as the primary hands-on framework. It addresses the gap between proof-of-concept models and production-ready systems, and is structured in five parts: Foundations, Core Techniques, AutoML for Different Data Types, Production/MLOps, and Industry Case Studies.

## Key Claims

- AutoML democratises machine learning, enabling domain experts to build sophisticated models in days rather than months.
- Most AutoML documentation focuses on specific tools or high-level overviews; practical, end-to-end production guidance is missing.
- Getting a model into production is not the end of the story — monitoring, drift detection, CI/CD, and governance are equally critical.
- Removing protected attributes (e.g., race) does not prevent proxy discrimination through correlated variables such as ZIP codes and insurance type.
- Analytical AI (structured numerical data, predictive modelling) typically delivers more economic value to organisations today than generative AI.
- AutoGluon was used by the author in production at medessence.de, giving the book grounding in real deployment experience.
- The 'citizen developer' trend is accelerating but a gap between available tools and practical knowledge remains substantial.
- Vibe data science (using LLM prompts to generate ML models) is emerging but early-stage; prompt sensitivity limits reliability.

## Main Concepts

- [[concepts/automl-automated-machine-learning-|AutoML (Automated Machine Learning)]]
- [[concepts/hyperparameter-optimisation-hpo-|Hyperparameter Optimisation (HPO)]]
- [[concepts/neural-architecture-search-nas-|Neural Architecture Search (NAS)]]
- [[concepts/automated-feature-engineering-and-data-preprocessing|Automated Feature Engineering and Data Preprocessing]]
- [[concepts/tabular-data-modelling|Tabular Data Modelling]]
- [[concepts/nlp-text-automl|NLP / Text AutoML]]
- [[concepts/time-series-forecasting|Time Series Forecasting]]
- [[concepts/computer-vision-automl|Computer Vision AutoML]]
- [[concepts/mlops-and-workflow-integration-mlflow-kubeflow-|MLOps and Workflow Integration (MLflow, Kubeflow)]]
- [[concepts/apache-airflow-data-pipelines|Apache Airflow Data Pipelines]]
- [[concepts/ci-cd-for-machine-learning|CI/CD for Machine Learning]]
- [[concepts/model-monitoring-and-drift-detection|Model Monitoring and Drift Detection]]
- [[concepts/fairness-aware-machine-learning-and-bias-mitigation-adversarial-debiasing-fairness-aware-ensembles-post-hoc-calibration-|Fairness-Aware Machine Learning and Bias Mitigation (adversarial debiasing, fairness-aware ensembles, post-hoc calibration)]]
- [[concepts/explainability-and-governance-in-regulated-industries|Explainability and Governance in Regulated Industries]]
- [[concepts/hipaa-compliance-in-healthcare-ai|HIPAA Compliance in Healthcare AI]]
- [[concepts/real-time-fraud-detection-at-scale|Real-time Fraud Detection at Scale]]
- [[concepts/retail-demand-forecasting-omnichannel-|Retail Demand Forecasting (omnichannel)]]
- [[concepts/patient-readmission-prediction|Patient Readmission Prediction]]
- [[concepts/citizen-developer-democratisation-of-data-science|Citizen Developer / Democratisation of Data Science]]
- [[concepts/analytical-ai-vs-generative-ai|Analytical AI vs Generative AI]]

## Key Entities

- [[entities/kerem-tomak-author-|Kerem Tomak (author)]]
- [[entities/thomas-h-davenport-foreword-author-distinguished-professor-babson-college-fellow-mit-initiative-on-the-digital-economy-|Thomas H. Davenport (foreword author; Distinguished Professor, Babson College; Fellow, MIT Initiative on the Digital Economy)]]
- [[entities/gregory-wheeler-foreword-author-professor-of-computational-science-and-philosophy-frankfurt-school-of-finance-and-management-|Gregory Wheeler (foreword author; Professor of Computational Science and Philosophy, Frankfurt School of Finance and Management)]]
- [[entities/ashkan-roshanayi-endorser-ceo-datachef-|Ashkan Roshanayi (endorser; CEO, DataChef)]]
- [[entities/baris-kavakli-endorser-ceo-portera-|Baris Kavakli (endorser; CEO, Portera)]]
- [[entities/ian-barkin-collaborator-on-citizen-developer-research-|Ian Barkin (collaborator on citizen developer research)]]
- [[entities/o-reilly-media-publisher-|O'Reilly Media (publisher)]]
- [[entities/medessence-de-author-s-company-used-autogluon-in-production-|medessence.de (author's company; used AutoGluon in production)]]
- [[entities/autogluon-primary-automl-framework-covered-|AutoGluon (primary AutoML framework covered)]]
- [[entities/tpot-automl-framework-mentioned-|TPOT (AutoML framework mentioned)]]
- [[entities/mlflow|MLflow]]
- [[entities/kubeflow|Kubeflow]]
- [[entities/apache-airflow|Apache Airflow]]
- [[entities/babson-college|Babson College]]
- [[entities/mit-initiative-on-the-digital-economy|MIT Initiative on the Digital Economy]]
- [[entities/frankfurt-school-of-finance-and-management|Frankfurt School of Finance and Management]]
- [[entities/aaron-black-acquisitions-editor-|Aaron Black (Acquisitions Editor)]]
- [[entities/shira-evans-development-editor-|Shira Evans (Development Editor)]]

## Questions Raised

- How does AutoGluon compare quantitatively to other AutoML frameworks (e.g., H2O AutoML, Auto-sklearn, TPOT) in the benchmarks covered?
- What specific techniques are presented for handling concept drift in production AutoML pipelines?
- How does the book treat the governance and audit trail requirements for AutoML in financial services regulation (beyond HIPAA)?
- What are the latency and throughput numbers achieved in the GlobalBank fraud-detection case study, and which AutoML configuration delivered them?
- How does the book address the reproducibility of AutoML pipelines across different infrastructure environments?
- At what point does the book recommend professional data scientists over citizen developers, and what criteria are used?

<!-- AUTHORED REGION END -->
