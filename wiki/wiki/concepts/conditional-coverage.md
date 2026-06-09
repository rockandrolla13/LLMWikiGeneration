---
title: Conditional Coverage
page_id: concepts/conditional-coverage
page_type: concept
revision_id: 1
created: 2026-05-21T14:00:00Z
updated: 2026-05-21T14:00:00Z
tags: [conformal-prediction, coverage, validity, conditional-validity]
sources: [sources/angelopoulos-2022-gentle-intro, sources/xu-2023-enbpi, sources/stocker-2025-conformal-timeseries-intro, sources/dieuleveut-zaffran-2025-cp-tutorial]
related: [concepts/conformal-prediction, concepts/marginal-coverage, concepts/conditional-validity, concepts/group-balanced-conformal-prediction, concepts/class-conditional-conformal-prediction]
mind_map_priority: high
---

# Conditional Coverage

**Conditional coverage** is the stronger validity property:

```
P(Y_test ∈ Ĉ(X_test) | X_test = x) ≥ 1 − α   for all x
```

In contrast to [[concepts/marginal-coverage|marginal coverage]], it requires the prediction set to cover with probability ≥ 1 − α **at every covariate value**, not just on average.

## Impossibility (Distribution-Free)

Barber, Candès, Ramdas, Tibshirani (2019a) and Lei & Wasserman (2014) proved that **exact** conditional coverage cannot be attained in finite samples without distributional assumptions: the only intervals with this guarantee under no assumptions are vacuous (infinite length almost everywhere).

This forces practical CP work to target weaker, *approximate* notions of conditional coverage.

## Approximate Notions

Modern variants partition the covariate space and require marginal coverage within each partition:

- **Group-balanced.** [[concepts/group-balanced-conformal-prediction]] — partition by an observed discrete feature.
- **Class-conditional.** [[concepts/class-conditional-conformal-prediction]] — partition by the response class (classification).
- **Size-stratified / feature-stratified.** Diagnostics from [[sources/angelopoulos-2022-gentle-intro|Angelopoulos & Bates]] that measure deviation from conditional coverage.
- **Mask-conditional.** [[concepts/mask-conditional-validity]] — partition by missing-data pattern.

## Asymptotic Conditional Coverage

[[concepts/enbpi|EnbPI]] ([[sources/xu-2023-enbpi]]) achieves **asymptotic** conditional coverage under [[concepts/beta-mixing|β-mixing]] dependence — one of the few constructive results in this direction. The guarantee vanishes as `T → ∞` under mild conditions on the error process.

## Sources

- [[sources/angelopoulos-2022-gentle-intro]] — Section on size-stratified coverage diagnostics.
- [[sources/xu-2023-enbpi]] — asymptotic conditional coverage for time series.
- [[sources/stocker-2025-conformal-timeseries-intro]] — proofs under β-mixing.
- [[sources/dieuleveut-zaffran-2025-cp-tutorial]] — impossibility result and PAC alternatives.

## Related Concepts

- [[concepts/marginal-coverage]]
- [[concepts/conditional-validity]]
- [[concepts/coverage-guarantee]]
