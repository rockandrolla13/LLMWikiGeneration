---
title: "Practical MLOps: Operationalizing Machine Learning Models"
page_id: sources/gift-2021-practical-mlops
page_type: source
revision_id: 1
created: 2026-06-19T00:00:00Z
updated: 2026-06-19T00:00:00Z
updated_by: batch_ingest_5_2026_06_19
tags: [mlops, devops, machine-learning-engineering, ci/cd, automl, cloud-computing, aws, azure, gcp, containers, edge-computing, onnx, model-deployment, monitoring, microservices, python, o'reilly, 2021]
sources: [sources/gift-2021-practical-mlops]
related: []
mind_map_priority: high
authors: ["Noah Gift", "Alfredo Deza"]
year: 2021
source_type: book
---

# Practical MLOps: Operationalizing Machine Learning Models

**Authors:** Noah Gift, Alfredo Deza  
**Year:** 2021  
**Type:** book  
**Markdown source:** `markdown_output/gift-2021-practical-mlops.md`

## Summary

Practical MLOps: Operationalizing Machine Learning Models (O'Reilly, September 2021, first edition, ISBN 978-1-098-10301-9) by Noah Gift and Alfredo Deza is a practitioner-oriented book on deploying and operating machine learning models in production. Its central argument is that the ML industry is failing to deliver business value because models are not reaching production reliably or quickly, and that applying DevOps-style automation — extended with ML-specific tooling — can close that gap by an order of magnitude. The book covers the full operationalization lifecycle across AWS, Azure, and GCP, including CI/CD pipelines, containers, edge deployment, AutoML, monitoring/drift detection, model interoperability, microservices, and command-line tooling, with real-world case studies from the authors' industry experience. The preface explicitly frames democratization of ML as a core motivation: "programming is a human right" and MLOps/AutoML should put these capabilities into the hands of doctors, lawyers, mechanics, and teachers, not just ML specialists.

## Key Claims

- The ML industry fails to deliver ROI because models do not reach production — operationalization is the missing link.
- Automation is the core pillar of MLOps, just as it is in DevOps; every example in the book should be read through the lens of future automation.
- ML can be made 10X faster to deploy in production — this claim originated from a discussion at O'Reilly Foo Camp with Tim O'Reilly and Mike Loukides.
- MLOps and AutoML together democratize AI/ML, moving it beyond a specialist priesthood to practitioners in many professional fields.
- KaizenML extends the Japanese manufacturing concept of continuous improvement to the full ML pipeline, including feature stores and AutoML.
- Model interoperability (via ONNX and Apple Core ML) is critical for deploying models across heterogeneous environments.
- Lack of operational excellence, focus on prediction accuracy over business value, and HiPPO (Highest Paid Person's Opinions) are identified as critical challenges in MLOps.

## Main Concepts

- [[concepts/mlops|MLOps]]
- [[concepts/devops-applied-to-ml|DevOps applied to ML]]
- [[concepts/continuous-integration-continuous-delivery-ci-cd-for-ml|Continuous Integration / Continuous Delivery (CI/CD) for ML]]
- [[concepts/kaizenml-continuous-improvement-applied-to-ml-pipelines-|KaizenML (continuous improvement applied to ML pipelines)]]
- [[concepts/automl|AutoML]]
- [[concepts/feature-stores|Feature stores]]
- [[concepts/containers-and-edge-deployment|Containers and edge deployment]]
- [[concepts/model-drift-monitoring-and-observability|Model drift monitoring and observability]]
- [[concepts/model-interoperability-onnx-core-ml-|Model interoperability (ONNX, Core ML)]]
- [[concepts/infrastructure-as-code-for-ml|Infrastructure as Code for ML]]
- [[concepts/serverless-ml-microservices-aws-lambda-|Serverless ML microservices (AWS Lambda)]]
- [[concepts/dataops-and-data-engineering|DataOps and data engineering]]
- [[concepts/mlops-design-patterns|MLOps design patterns]]
- [[concepts/data-governance-and-cybersecurity|Data governance and cybersecurity]]
- [[concepts/mlops-hierarchy-of-needs|MLOps hierarchy of needs]]

## Key Entities

- [[entities/noah-gift-author-adjunct-professor-at-duke-northwestern-uc-davis-former-cto-engineering-manager-at-bay-area-startups-|Noah Gift (author, adjunct professor at Duke, Northwestern, UC Davis; former CTO/engineering manager at Bay Area startups)]]
- [[entities/alfredo-deza-author-microsoft-developer-advocate-systems-administration-background-|Alfredo Deza (author, Microsoft developer advocate, systems administration background)]]
- [[entities/o-reilly-media-publisher-|O'Reilly Media (publisher)]]
- [[entities/tim-o-reilly-o-reilly-foo-camp-discussion-participant-|Tim O'Reilly (O'Reilly Foo Camp discussion participant)]]
- [[entities/mike-loukides-o-reilly-foo-camp-discussion-participant-|Mike Loukides (O'Reilly Foo Camp discussion participant)]]
- [[entities/roger-magoulas-o-reilly-foo-camp-participant-|Roger Magoulas (O'Reilly Foo Camp participant)]]
- [[entities/fei-fei-li-stanford-ai-head-mentioned-in-preface-anecdote-|Fei-Fei Li (Stanford AI head, mentioned in preface anecdote)]]
- [[entities/david-baltimore-nobel-prize-winning-scientist-at-caltech-mentioned-in-preface-|David Baltimore (Nobel Prize-winning scientist at Caltech, mentioned in preface)]]
- [[entities/david-goodstein-physicist-at-caltech-mentioned-in-preface-|David Goodstein (physicist at Caltech, mentioned in preface)]]
- [[entities/joseph-bogen-neurosurgeon-and-mentor-at-caltech-mentioned-in-preface-|Joseph Bogen (neurosurgeon and mentor at Caltech, mentioned in preface)]]
- [[entities/jonathan-haber-author-of-critical-thinking-mit-press-cited-in-preface-|Jonathan Haber (author of Critical Thinking, MIT Press, cited in preface)]]
- [[entities/caltech-california-institute-of-technology-mentioned-as-formative-institution-for-noah-gift-|Caltech (California Institute of Technology, mentioned as formative institution for Noah Gift)]]
- [[entities/sqor-sports-social-network-case-study-organization-in-chapter-12-|Sqor Sports Social Network (case study organization in Chapter 12)]]
- [[entities/aws-amazon-web-services-|AWS (Amazon Web Services)]]
- [[entities/microsoft-azure|Microsoft Azure]]
- [[entities/google-cloud-platform-gcp-|Google Cloud Platform (GCP)]]
- [[entities/apple-automl-via-create-ml-and-core-ml-|Apple (AutoML via Create ML and Core ML)]]
- [[entities/github-actions-ci-cd-tooling-mentioned-|GitHub Actions (CI/CD tooling mentioned)]]
- [[entities/onnx-open-neural-network-exchange-|ONNX (Open Neural Network Exchange)]]
- [[entities/aws-sagemaker|AWS SageMaker]]
- [[entities/ludwig-open-source-automl-framework-|Ludwig (open-source AutoML framework)]]
- [[entities/flaml-open-source-automl-framework-from-microsoft-|FLAML (open-source AutoML framework from Microsoft)]]
- [[entities/tfhub-tensorflow-hub-|TFHub (TensorFlow Hub)]]
- [[entities/coral-google-edge-device-|Coral (Google edge device)]]
- [[entities/azure-percept-microsoft-edge-device-|Azure Percept (Microsoft edge device)]]

## Questions Raised

- How does KaizenML differ from standard AutoML in practice, and what does the full pipeline look like when feature stores are included?
- What specific metrics or thresholds does the book recommend for detecting model drift in production?
- How does the book treat model governance and auditability across cloud platforms — are there platform-neutral patterns?
- The preface cites a Forbes article by Noah Gift claiming organizations are not seeing ROI from data science — what evidence or data is provided for this claim?
- What is the book's concrete definition of the 'MLOps hierarchy of needs' and how does it map to Maslow's hierarchy?
- Chapter 12 references a case study at Sqor Sports Social Network — how generalizable are those lessons to non-social-media ML use cases?
