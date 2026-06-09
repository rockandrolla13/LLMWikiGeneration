---
title: Marginal Coverage
page_id: concepts/marginal-coverage
page_type: concept
revision_id: 1
created: 2026-05-21T14:00:00Z
updated: 2026-05-21T14:00:00Z
tags: [conformal-prediction, coverage, validity, uncertainty-quantification]
sources: [sources/angelopoulos-2022-gentle-intro, sources/xu-2023-enbpi, sources/stocker-2025-conformal-timeseries-intro, sources/zaffran-2022-aci]
related: [concepts/conformal-prediction, concepts/coverage-guarantee, concepts/conditional-coverage, concepts/split-conformal-prediction, concepts/exchangeability]
mind_map_priority: high
---

# Marginal Coverage

**Marginal coverage** is the basic validity property of [[concepts/conformal-prediction|conformal prediction]]:

```
P(Y_test ∈ Ĉ(X_test)) ≥ 1 − α
```

where the probability is **averaged (marginalised)** over the joint randomness of the calibration set and the test point.

## Contrast with Conditional Coverage

Marginal coverage says nothing about how coverage is distributed across the covariate space. The stronger notion is [[concepts/conditional-coverage|conditional coverage]]:

```
P(Y_test ∈ Ĉ(X_test) | X_test = x) ≥ 1 − α   for all x
```

Conditional coverage is provably **impossible** to attain in finite samples without further distributional assumptions (Barber et al., 2019a; Lei & Wasserman, 2014). Modern CP research therefore targets *approximations* — feature-stratified, size-stratified, group-balanced (see [[concepts/group-balanced-conformal-prediction]]), or class-conditional (see [[concepts/class-conditional-conformal-prediction]]) coverage.

## Why It Holds for Split CP

Under [[concepts/exchangeability|exchangeability]] of `(X_1, Y_1), ..., (X_n, Y_n), (X_test, Y_test)`, the rank of the test [[concepts/nonconformity-score|nonconformity score]] among the calibration scores is uniform on `{1, ..., n+1}`. The empirical `⌈(n+1)(1−α)⌉/n` quantile therefore gives a prediction set covering `Y_test` with probability ≥ 1 − α, regardless of the underlying model or distribution.

The `+1` in `(n+1)` is the finite-sample adjustment that makes the inequality hold **non-asymptotically**.

## Sources

- [[sources/angelopoulos-2022-gentle-intro]] — Theorem 1 and the four-step recipe.
- [[sources/xu-2023-enbpi]] — extends marginal coverage to β-mixing time-series via EnbPI.
- [[sources/stocker-2025-conformal-timeseries-intro]] — formalises marginal coverage under weak dependence.
- [[sources/zaffran-2022-aci]] — discusses marginal coverage as ACI's target.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/coverage-guarantee]]
- [[concepts/conditional-coverage]]
- [[concepts/worst-case-coverage]]
