---
title: Conformal Prediction with Conditional Guarantees
page_id: sources/gibbs-2023-conditional-guarantees
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24 18:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Isaac Gibbs
- John J. Cherian
- Emmanuel J. Candès
year: 2023
venue: arXiv:2305.12616
tags:
- conformal-prediction
- conditional-coverage
- covariate-shift
- distribution-free
- group-conditional
- rkhs
related:
- concepts/conditional-coverage
- concepts/conformal-prediction
- concepts/mondrian-conformal-prediction
- concepts/group-balanced-conformal-prediction
- concepts/split-conformal-prediction
- concepts/quantile-regression
- entities/isaac-gibbs
- entities/john-cherian
- entities/emmanuel-candes
- sources/gibbs-2021-aci
- sources/gibbs-2024-online-aci
- sources/tibshirani-2019-covariate-shift
- sources/barber-2023-beyond-exchangeability
mind_map_priority: high
schema_version: 2
uuid: 0ec018a1-cfb5-593c-be10-72991107622f
content_hash: sha256:942cc98f44d6592d5ddfcde4dc88010884e42a0ca3612d7f8df2646bcb00f8ed
---

<!-- AUTHORED REGION START -->
# Conformal Prediction with Conditional Guarantees

**Authors:** [[entities/isaac-gibbs|Isaac Gibbs]], [[entities/john-cherian|John J. Cherian]], [[entities/emmanuel-candes|Emmanuel J. Candès]]

**Year:** 2023

**Venue:** arXiv:2305.12616. Code: `github.com/jjcherian/conditionalconformal`. PyPI: `conditionalconformal`.

## Summary

Bridges the gap between marginal and exact conditional coverage by reformulating [[concepts/conditional-coverage|conditional coverage]] as **coverage over a class of covariate shifts `F`**. For finite-dimensional `F` (e.g., group indicators) the method achieves exact finite-sample coverage over all shifts simultaneously. For infinite-dimensional `F` (e.g., RKHS) it provides a tractable best-effort PAC-style guarantee with quantifiable coverage errors that can be tuned via interpretable hyperparameters.

This is the most direct response to the Lei-Wasserman 2014 / Barber et al. 2021 impossibility result for exact distribution-free conditional coverage — the answer is "you can't have exact, but you can have exact-over-a-shift-class for a useful class."

## Key Contributions

1. **Reformulation: conditional coverage = coverage over a shift class `F`.** Interpolates between marginal (`F = constants`) and full conditional (`F = all measurable`) validity.
2. **Finite-dimensional linear `F` (e.g., `F = {Σ_G β_G 1{x ∈ G}}`).** Randomised conditional calibration achieves exact finite-sample coverage simultaneously over all shifts / groups, with no assumptions on data distribution or group overlap.
3. **Strict improvement over Jung et al. (2023).** Tighter finite-sample coverage than quantile-regression-over-subgroups; no distributional assumptions; allows discrete outcomes; extends beyond the group setting.
4. **Infinite-dimensional `F` (e.g., RKHS).** Shift-agnostic method whose realised coverage is accurately estimable in finite samples, even when exact `1 − α` coverage is unattainable.
5. **Split conformal as a special case.** Re-derives split conformal as intercept-only augmented quantile regression with the pinball loss. Generalises to richer function classes.
6. **Wrapper around any black-box model and any conformity score.** Integrates into existing split-conformal pipelines.
7. **Randomised and unrandomised variants.** Exact-coverage randomised version and conservative non-randomised version.

## Relation to Other Wiki Sources

- [[sources/gibbs-2021-aci]] / [[sources/gibbs-2024-online-aci]] — companion line on online ACI from the same author.
- [[sources/tibshirani-2019-covariate-shift]] — generalises the single-known-shift WCP setting to a *class* of shifts.
- [[sources/barber-2023-beyond-exchangeability]] — companion non-exchangeability framework; this paper handles conditional validity rather than non-exchangeability per se.

## Questions Raised

- How should one choose the function class `F` and its regularisation in practice?
- What is the trade-off between richness of `F` (broader coverage guarantees) and the loss of exactness in finite samples?
- How does computational cost scale with `dim(F)` for the augmented quantile regression?

## See Also

- [[concepts/conditional-coverage]]
- [[concepts/mondrian-conformal-prediction]]
- [[entities/john-cherian]]

<!-- AUTHORED REGION END -->
