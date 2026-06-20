---
title: Designing Machine Learning Systems
page_id: sources/huyen-2022-designing-ml-systems
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Chip Huyen
year: 2022
publisher: O'Reilly Media
edition: 1st
is_early_release: false
page_count_estimate: 386
tags:
- ai-engineering
- software-engineering
related:
- concepts/batch-vs-online-prediction
- concepts/class-imbalance-handling
- concepts/continual-learning
- concepts/data-engineering-for-ml
- concepts/data-leakage
- concepts/distribution-drift
- concepts/feature-engineering
- concepts/feature-store
- concepts/ml-monitoring-and-observability
- concepts/ml-system-design
- concepts/model-compression
- concepts/model-offline-evaluation
- concepts/responsible-ai
- concepts/test-in-production
- entities/apache-flink
- entities/apache-kafka
- entities/chip-huyen
- entities/claypot-ai
- entities/oreilly-media
- entities/snorkel-ai
- entities/stanford-cs-329s
- entities/tvm
mind_map_priority: medium
revision_hash: sha256:760cdc827eb6074b
schema_version: 2
uuid: b51ab7f3-ad8e-561b-9b71-4c43d0a2afe1
content_hash: sha256:1271f8e774211f04887e8bc83662fa877dceeece5a436a885178623a5c473f6c
---

<!-- AUTHORED REGION START -->
# Designing Machine Learning Systems
*An Iterative Process for Production-Ready Applications*

**Authors:** [[entities/chip-huyen|Chip Huyen]]

**Year:** 2022

**Publisher:** O'Reilly Media

**Edition:** 1st

## Summary

Designing Machine Learning Systems is Chip Huyen's holistic, engineering-first textbook on building production ML applications. Rather than teaching algorithms, the book argues that an ML system's success is determined by how its data engineering, [[feature-engineering|feature engineering]], modeling, deployment, and monitoring components are designed together against business objectives. The iterative framework is anchored in case studies from Netflix, Stitch Fix, Booking.com, TikTok, Alibaba, and other companies operating ML 'at reasonable scale,' and it is grounded in the lectures Huyen developed for Stanford CS 329S.

The book moves end-to-end through the lifecycle: framing ML problems and choosing objective functions; building data infrastructure (sources, formats, OLTP/OLAP, [[data-engineering-for-ml|ETL and dataflow]], batch vs streaming); generating training data through sampling, labeling, weak supervision, and [[class-imbalance-handling|class-imbalance handling]]; engineering features while preventing [[data-leakage|data leakage]]; offline evaluation and ensembling; and then deployment trade-offs around [[batch-vs-online-prediction|batch vs online prediction]], [[model-compression|model compression]], and edge vs cloud inference. The second half is unusually strong on what comes after deployment — [[data-distribution-shift|data distribution shifts]], [[ml-monitoring-and-observability|monitoring and observability]], [[continual-learning|continual learning]], and [[test-in-production|testing in production]] via shadow deployments, A/B tests, canaries, interleaving, and bandits — and on the MLOps platform layer (model store, [[feature-store|feature store]], orchestration).

Its angle versus competing MLOps books is the insistence on first principles over tools and the foregrounding of [[responsible-ai|responsible AI]], team structure, and the 'end-to-end data scientist' debate. It is aimed at ML engineers, data scientists, data engineers, ML platform engineers, and engineering managers at medium-to-large organizations who already know basic ML and now need to ship and maintain it.

## Key Contributions

- An iterative ML systems framework that ties every design decision (data, features, model, infra, monitoring) back to business and ML objectives rather than treating them in isolation
- A clear taxonomy of data distribution shifts (covariate, label, concept drift) plus practical detection methods (statistical tests over rolling windows on inputs, outputs, accuracy proxies)
- A pragmatic distinction between stateless retraining and stateful fine-tuning as the two infrastructure modes of continual learning, with a maturity model of four stages from manual retraining to fully automated updates
- A 'test in production' menu (shadow deployment, A/B testing, canary release, interleaving experiments, bandits) framed by risk and statistical efficiency rather than as interchangeable techniques
- A debunking of common deployment myths (one model per system, static performance, scale doesn't matter) and a defense of the end-to-end data scientist with a separate ML platform team
- A responsible-AI framework that operationalizes fairness, privacy, transparency, and accountability through model cards, slice-based evaluation, and stakeholder review during system design

## Key Topics Covered

ml-system-design, data-engineering-for-ml, training-data-sampling-and-labeling, feature-engineering, data-leakage, class-imbalance-handling, model-offline-evaluation, batch-vs-online-prediction, model-compression, edge-vs-cloud-inference, data-distribution-shift, ml-monitoring-and-observability, continual-learning, test-in-production, mlops-infrastructure, feature-store, responsible-ai

## Questions Raised

- How should organizations choose the optimal retraining cadence for continual learning when label feedback loops are long and imbalanced (e.g., fraud detection requiring two-week A/B windows)?
- What concrete statistical tests reliably detect data distribution shifts on high-dimensional feature spaces and embeddings, where univariate tests are weak?
- How can model iteration (architecture changes) be made compatible with stateful training without falling back to full retraining each time?
- Where should the boundary sit between data scientists owning end-to-end production versus a dedicated ML platform team — and how does this change with company scale?
- How can subject matter experts be meaningfully integrated into ML system development beyond the labeling phase, including no-code/low-code pathways for non-engineers?

## Intended Audience

ML engineers, data scientists, data engineers, ML platform engineers, and engineering managers at medium-to-large enterprises and fast-growing startups who already understand basic ML and now need to design, deploy, and maintain ML systems in production.

## Key Concepts in This Source

- [[concepts/ml-system-design|ML System Design]]
- [[concepts/data-engineering-for-ml|Data Engineering for ML]]
- [[concepts/feature-engineering|Feature Engineering]]
- [[concepts/data-leakage|Data Leakage]]
- [[concepts/class-imbalance-handling|Class Imbalance Handling]]
- [[concepts/model-offline-evaluation|Model Offline Evaluation]]
- [[concepts/batch-vs-online-prediction|Batch vs Online Prediction]]
- [[concepts/model-compression|Model Compression]]
- [[concepts/distribution-drift|Data Distribution Shift]]
- [[concepts/ml-monitoring-and-observability|ML Monitoring and Observability]]
- [[concepts/continual-learning|Continual Learning]]
- [[concepts/test-in-production|Test in Production]]
- [[concepts/feature-store|Feature Store]]
- [[concepts/responsible-ai|Responsible AI]]

## Entities

- [[entities/chip-huyen|Chip Huyen]]
- [[entities/claypot-ai|Claypot AI]]
- [[entities/stanford-cs-329s|Stanford CS 329S]]
- [[entities/oreilly-media|O'Reilly Media]]
- [[entities/snorkel-ai|Snorkel AI]]
- [[entities/apache-flink|Apache Flink]]
- [[entities/apache-kafka|Apache Kafka]]
- [[entities/tvm|TVM]]

<!-- AUTHORED REGION END -->
