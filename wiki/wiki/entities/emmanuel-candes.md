---
title: Emmanuel Candès
page_id: entities/emmanuel-candes
page_type: entity
entity_type: person
revision_id: 2
created: 2026-04-10T18:00:00Z
updated: 2026-05-24T19:00:00Z
tags: [researcher, statistics, conformal-prediction, compressed-sensing]
sources: [sources/zaffran-2022-aci, sources/tibshirani-2019-covariate-shift, sources/barber-2021-jackknife-plus, sources/barber-2023-beyond-exchangeability, sources/romano-2019-cqr, sources/romano-2020-aps, sources/angelopoulos-2021-learn-then-test, sources/gibbs-2021-aci, sources/gibbs-2024-online-aci, sources/gibbs-2023-conditional-guarantees, sources/angelopoulos-2023-conformal-pid, sources/bates-2021-rcps]
related: [concepts/conformal-prediction, concepts/adaptive-conformal-inference]
mind_map_priority: medium
---

# Emmanuel Candès

**Emmanuel Candès** is a Professor of Mathematics and Statistics at Stanford University, known for foundational work in compressed sensing and, more recently, contributions to [[concepts/conformal-prediction|conformal prediction]].

## Affiliation

- Stanford University, Departments of Mathematics and Statistics

## Contributions to Conformal Prediction

### Adaptive Conformal Inference (with Isaac Gibbs)
Gibbs and Candès (2021) introduced [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference (ACI)]], extending conformal prediction to handle:

- Distribution shift
- Time series data
- Non-exchangeable settings

The key innovation was an adaptive miscoverage rate that adjusts based on recent prediction performance.

### Conformalized Quantile Regression
Romano, Patterson, and Candès (2019) introduced CQR, combining quantile regression with conformal prediction for:

- Heteroskedastic data
- Adaptive interval widths
- Maintained coverage guarantees

## Other Notable Work

- **Compressed Sensing**: Foundational work on sparse signal recovery
- **Matrix Completion**: Netflix Prize problem
- **Robust PCA**: Decomposing low-rank + sparse matrices

## Awards

- MacArthur Fellowship ("Genius Grant")
- Member of the National Academy of Sciences

## See Also

- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[concepts/conformal-prediction|Conformal Prediction]]
