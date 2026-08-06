---
title: Data Distribution Shift
page_id: concepts/data-distribution-shift
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- machine-learning
- production-ml
- monitoring
- ai-engineering
sources:
- sources/huyen-2022-designing-ml-systems
related:
- concepts/distribution-drift
- concepts/ml-monitoring-and-observability
- concepts/continual-learning
mind_map_priority: medium
schema_version: 2
uuid: c85fb804-6449-5128-8f10-780c6d41f596
content_hash: sha256:7c57cffa9e4e14ccd6c1d27adce94e6068731ce1fa026582044b4133bf27c20b
---

<!-- AUTHORED REGION START -->
# Data Distribution Shift

The data a deployed model sees stops resembling the data it was trained on. This is the production-systems framing of the same phenomenon the wiki also records, from the statistics side, as [[concepts/distribution-drift|Distribution Drift]].

## The Taxonomy

[[sources/huyen-2022-designing-ml-systems|Huyen (2022)]] splits shift three ways:

- **Covariate shift** — the input distribution P(X) changes, the relationship P(Y|X) does not.
- **Label shift** — the outcome distribution P(Y) changes, P(X|Y) does not.
- **Concept drift** — P(Y|X) itself changes; the mapping the model learned no longer holds.

The [[concepts/distribution-drift|Distribution Drift]] page carries the same taxonomy plus the full-shift case where both P(X) and P(Y|X) move.

## Detecting It in Production

Huyen's practical recommendation is statistical tests over rolling windows applied to three things: input and feature distributions, prediction distributions, and accuracy proxies. This is the core job of [[concepts/ml-monitoring-and-observability|ML Monitoring and Observability]], which exists to catch silent failures — degradation that shows up in the data long before anyone reports a broken product.

The book flags an unresolved problem here: univariate tests are weak on high-dimensional feature spaces and embeddings, and it is not settled which tests reliably detect shift in that setting.

## Responding to It

Shift is the main reason [[concepts/continual-learning|Continual Learning]] infrastructure exists — the ability to update a deployed model on demand, by stateless retraining or stateful fine-tuning, at whatever cadence data freshness demands. Huyen keeps the cadence question open too, particularly when label feedback loops are long and imbalanced, as in fraud detection where an A/B window may run two weeks.

## Why It Matters Beyond Accuracy

Shift breaks the exchangeability assumption behind [[concepts/conformal-prediction|conformal prediction]], which is why the wiki's conformal literature treats it as a first-class problem rather than a monitoring nuisance. See [[concepts/distribution-drift|Distribution Drift]] for the coverage bounds and adaptive methods.

## See Also

[[concepts/distribution-drift|Distribution Drift]] · [[concepts/ml-monitoring-and-observability|ML Monitoring and Observability]] · [[concepts/continual-learning|Continual Learning]] · [[concepts/conformal-prediction|Conformal Prediction]] · [[concepts/exchangeability|Exchangeability]] · [[entities/chip-huyen|Chip Huyen]]

<!-- AUTHORED REGION END -->
