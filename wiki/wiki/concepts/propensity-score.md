---
abstraction_level: intermediate
concept_type: technique
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/propensity-score
page_type: concept
related:
- concepts/causal-identifiability-conditions
- concepts/causal-inference
- concepts/confounding
- concepts/ip-weighting-marginal-structural-models
revision_hash: sha256:7b7c16517f11f920624fb79cdd9b45dcd016e04f936a8daf82bdd9f7e2d1c84c
revision_id: 1
sources:
- sources/cai-2023-testing-conditional-independence-time-series
- sources/hill-2011-bart-causal-inference
tags: []
title: Propensity Score
updated: '2026-06-20T01:03:51Z'
updated_by: creditmacro-batch
schema_version: 2
uuid: 0acab4e3-462d-58a0-8ed9-84262a3201fe
content_hash: sha256:951cf8b8142d30ce51d0d00f6a54ad0adc7ef50688adc5581144dc8ec86e6b84
---

<!-- AUTHORED REGION START -->
# Propensity Score

## Definition

The conditional probability of treatment assignment given observed covariates, e(x) = Pr(Z=1|X), used to balance treatment and control groups via matching, subclassification, or weighting in observational causal inference.

## Sources

- [[sources/cai-2023-testing-conditional-independence-time-series|Testing Conditional Independence in Causal Inference for Time Series Data]]
- [[sources/hill-2011-bart-causal-inference|Bayesian Nonparametric Modeling for Causal Inference]]

## Related Concepts

- [[concepts/causal-identifiability-conditions|causal-identifiability-conditions]]
- [[concepts/causal-inference|causal-inference]]
- [[concepts/confounding|confounding]]
- [[concepts/ip-weighting-marginal-structural-models|ip-weighting-marginal-structural-models]]
<!-- AUTHORED REGION END -->
