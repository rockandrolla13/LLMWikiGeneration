---
authors:
- Miguel A. Hernán
- James M. Robins
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/hernan-2020-causal-inference-what-if
page_type: source
publication_date: '2020'
publication_venue: Chapman & Hall/CRC
related:
- concepts/causal-dags-confounding-selection-bias
- concepts/causal-identifiability-conditions
- concepts/doubly-robust-estimation
- concepts/g-methods-time-varying-treatments
- concepts/instrumental-variables
- concepts/ip-weighting-marginal-structural-models
- concepts/potential-outcomes
- entities/chapman-hall-crc
- entities/james-robins
- entities/miguel-hernan
revision_hash: sha256:814b0ef4c50976b2f1dc2d878ddedd8e955aa44d3a06bea9a083f70bcb989e5c
revision_id: 1
source_hash: sha256:55c8b6aeebea5d3a408cd3f9ecffe0f012cd7d9f1c43d5e83e0bc2bf6927d992
source_path: raw/creditmacro/Causal Inference What If (Miguel A. Hernán, James M.
  Robins) (z-library.sk, 1lib.sk, z-lib.sk).md
source_type: book
sources: []
tags:
- causal-inference
- counterfactuals
- g-methods
- confounding
- instrumental-variables
- doubly-robust
- epidemiology
title: 'Causal Inference: What If'
updated: '2026-06-20T01:03:51Z'
updated_by: op_3d8a63fdb139
schema_version: 2
uuid: 1a96e118-01e2-5f09-aaf3-e8307df3c0f3
content_hash: sha256:571610c0dbc140b5d77a7abec2b5a069cdde55c27e30dbc7529922dd3536b883
---

<!-- AUTHORED REGION START -->
# Causal Inference: What If

**Authors:** Miguel A. Hernán, James M. Robins · **Year:** 2020 · **Venue:** Chapman & Hall/CRC · **Type:** book

## Summary

A graduate textbook on the identification and estimation of causal effects from experimental and observational data. The central thesis is that causal inference should be made 'less casual': every analysis must articulate an explicit causal question (a contrast of counterfactual outcomes under interventions) and separate the role of data from unverifiable assumptions. Part I covers nonparametric identification (the three identifiability conditions, randomized experiments, a DAG-based taxonomy of bias). Part II covers estimation under models (IP weighting and marginal structural models, standardization and the g-formula, g-estimation, propensity scores, instrumental variables, doubly robust machine-learning estimators). Part III treats time-varying treatments where treatment-confounder feedback requires the g-methods. The recurring message is that correct method choice depends on the causal question and the assumed causal structure.

## Key Claims

1. Individual causal effects are contrasts of counterfactual outcomes and are generally unidentifiable (a missing-data problem); the average causal effect is the practical target.
2. Causal effects from observational data are identified only under exchangeability (no unmeasured confounding), positivity, and consistency.
3. Bias has a structural classification representable in causal DAGs: confounding, selection bias, and measurement bias, with the backdoor criterion guiding adjustment.
4. With time-varying treatments and treatment-confounder feedback, conventional adjustment is biased; the g-methods (g-formula, IP weighting of marginal structural models, g-estimation) are required.
5. IP weighting and standardization target the same estimand via different models; doubly robust estimators are consistent if either model is correct.
6. Machine learning aids causal estimation only with doubly robust estimators and sample-splitting/cross-fitting; variable selection for causal inference differs from selection for prediction.

## Questions Raised

- How can the no-unmeasured-confounding (exchangeability) assumption be empirically verified rather than assumed?
- How should the bias-variance trade-off be managed when high-dimensional confounders require flexible models?
- How can well-defined interventions (consistency) be specified for vague or compound exposures?

## Concepts

- [[concepts/potential-outcomes|Potential Outcomes and Counterfactual Causal Effects]]
- [[concepts/causal-identifiability-conditions|Identifiability Conditions]]
- [[concepts/causal-dags-confounding-selection-bias|Causal DAGs and Structural Classification of Bias]]
- [[concepts/g-methods-time-varying-treatments|G-Methods for Time-Varying Treatments]]
- [[concepts/ip-weighting-marginal-structural-models|IP Weighting and Marginal Structural Models]]
- [[concepts/doubly-robust-estimation|Doubly Robust ML Causal Estimation]]
- [[concepts/instrumental-variables|Instrumental Variable Estimation]]

## Entities

- [[entities/miguel-hernan|Miguel A. Hernán]]
- [[entities/james-robins|James M. Robins]]
- [[entities/chapman-hall-crc|Chapman & Hall/CRC]]

## Source

- **Path:** `raw/creditmacro/Causal Inference What If (Miguel A. Hernán, James M. Robins) (z-library.sk, 1lib.sk, z-lib.sk).md`
- **Type:** book
- **Hash:** `sha256:55c8b6aeebea5d3a4...`
<!-- AUTHORED REGION END -->
