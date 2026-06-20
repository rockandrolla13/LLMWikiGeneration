---
title: Jackknife+ after Bootstrap (J+aB)
page_id: concepts/jackknife-plus-after-bootstrap
page_type: concept
revision_id: 2
created: 2026-05-21 14:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- jackknife
- bootstrap
- ensemble-methods
sources:
- sources/kim-2020-jackknife-plus-after-bootstrap
- sources/xu-2023-enbpi
- sources/angelopoulos-2022-gentle-intro
related:
- concepts/conformal-prediction
- concepts/cross-conformal-prediction
- concepts/enbpi
- concepts/prediction-intervals
mind_map_priority: medium
schema_version: 2
uuid: 9f48676e-d73a-5515-ae0b-2dd7658c9886
content_hash: sha256:6b71b06396e0a4527c8f04c34fc2285b426acabf42dc9299576aaa5f4d48133e
---

<!-- AUTHORED REGION START -->
# Jackknife+ after Bootstrap (J+aB)

## Primary Source

Primary source: [[sources/kim-2020-jackknife-plus-after-bootstrap|Kim, Xu & Barber (2020), "Predictive inference is free with the jackknife+-after-bootstrap"]] (NeurIPS). This paper shows how to obtain leave-one-out predictors essentially "for free" by aggregating only the bootstrap models that excluded each training index, recovering the jackknife+ 1 − 2α coverage bound without explicit retraining — the trick this concept page formalises.

**J+aB** (Kim, Xu, Barber, 2020) combines the Jackknife+ predictive-inference framework with bootstrap aggregation, producing leave-one-out (LOO)-style prediction intervals **without explicit retraining**.

## The Trick

A Jackknife+ implementation would naively retrain the base model `n` times (once per held-out point) — usually prohibitive. J+aB instead:

1. Trains `B` bootstrap point predictors once.
2. For each training index `i`, aggregates **only** the bootstrap models whose sample did not include `i`. This gives `f̂^{−i}` for free.
3. Uses these LOO estimators in the Jackknife+ interval construction.

## Relation to EnbPI

[[concepts/enbpi|EnbPI]] ([[sources/xu-2023-enbpi|Xu & Xie 2023]]) uses essentially the same J+aB construction but:
- Extends coverage guarantees to **non-exchangeable** time series.
- Uses a sliding-window empirical quantile of residuals rather than the Jackknife+ "max-of-LOO" interval.
- Adds asymmetric-interval optimisation via a quantile offset `β`.

The two are operationally similar; EnbPI generalises to the time-series setting.

## Coverage

Marginal coverage holds at 1 − 2α under [[concepts/exchangeability|exchangeability]] (inherited from Jackknife+). EnbPI extends to asymptotic 1 − α under [[concepts/beta-mixing|β-mixing]].

## Sources

- [[sources/xu-2023-enbpi]] — uses J+aB as the closest exchangeable comparator.
- [[sources/angelopoulos-2022-gentle-intro]] — places J+aB in the jackknife-family overview.

## Related Concepts

- [[concepts/cross-conformal-prediction]]
- [[concepts/enbpi]]
- [[concepts/conformal-prediction]]

<!-- AUTHORED REGION END -->
