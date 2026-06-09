---
title: "Distribution-Free, Risk-Controlling Prediction Sets"
page_id: sources/bates-2021-rcps
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24T18:00:00Z
updated: 2026-05-24T18:00:00Z
authors: ["Stephen Bates", "Anastasios Angelopoulos", "Lihua Lei", "Jitendra Malik", "Michael I. Jordan"]
year: 2021
venue: "Journal of the ACM 71(1) (2024); arXiv:2101.02703 (2021). DOI 10.1145/3478535."
tags: [conformal-prediction, risk-control, rcps, distribution-free, uncertainty-quantification, tolerance-regions, concentration-inequalities]
related: [
  concepts/risk-controlling-prediction-sets,
  concepts/conformal-risk-control,
  concepts/split-conformal-prediction,
  concepts/conformal-prediction,
  concepts/learn-then-test,
  entities/stephen-bates,
  entities/anastasios-angelopoulos,
  entities/lihua-lei,
  entities/jitendra-malik,
  entities/michael-i-jordan,
  sources/angelopoulos-2021-raps,
  sources/angelopoulos-2021-learn-then-test,
  sources/farinhas-2024-non-exchangeable-crc,
  sources/angelopoulos-2022-gentle-intro
]
mind_map_priority: high
---

# Distribution-Free, Risk-Controlling Prediction Sets (RCPS)

**Authors:** [[entities/stephen-bates|Stephen Bates]], [[entities/anastasios-angelopoulos|Anastasios Angelopoulos]], [[entities/lihua-lei|Lihua Lei]], [[entities/jitendra-malik|Jitendra Malik]], [[entities/michael-i-jordan|Michael I. Jordan]]

**Year:** 2021

**Venue:** *Journal of the ACM* 71(1) (2024); arXiv:2101.02703 (2021). DOI 10.1145/3478535.

## Summary

**Primary source** for the wiki concept [[concepts/risk-controlling-prediction-sets|Risk-Controlling Prediction Sets (RCPS)]] and the foundational paper for [[concepts/conformal-risk-control|conformal risk control]]. Introduces a distribution-free, finite-sample framework that calibrates a nested family of set-valued predictors `{T_λ}` from any black-box model so that the expected loss (risk) `R(T) = E[L(Y, T(X))]` satisfies `R(T) ≤ α` with probability at least `1 − δ` over an i.i.d. calibration set.

The core algorithm is **Upper Confidence Bound (UCB) calibration**: select the smallest `λ` such that a pointwise `(1 − δ)` upper confidence bound `R̂^+(λ)` for the risk lies below `α` for all larger `λ`. Monotonicity of the risk in `λ` turns a pointwise concentration result into a uniform high-probability guarantee.

## Key Contributions

1. **Definition 1: (α, δ)-RCPS.** A random set predictor `T` is an (α, δ)-RCPS if `P(R(T) ≤ α) ≥ 1 − δ`, for any bounded-from-below monotone loss `L` on prediction sets.
2. **Theorem 1 (UCB calibration validity).** Given a nested family `{T_λ}`, monotone loss, and a pointwise `(1 − δ)` UCB `R̂^+(λ)`, choosing `λ̂` as the smallest `λ` such that `R̂^+(λ') ≤ α` for all `λ' ≥ λ` yields an (α, δ)-RCPS.
3. **Concentration-inequality catalogue.** Hoeffding, Bentkus, Hoeffding-Bentkus (HB), Waudby-Smith-Ramdas (WSR) betting bounds for bounded losses; CLT-based bounds for unbounded losses. WSR recommended as default.
4. **Decoupling of model fitting and calibration.** The underlying predictive model `f̂` may be trained on a different distribution; only the calibration data must be exchangeable with test data.
5. **Strict generalisation of split conformal.** Taking `L(y, S) = 1{y ∉ S}` recovers tolerance-region coverage; general monotone losses cover miscoverage, hierarchical mistake cost, false-negative pixel rate, 3D structure errors.

## Empirical Demonstrations

Five large-scale problems:
- Cost-sensitive classification (MRI-style examples).
- Multi-label classification (MS-COCO).
- Hierarchical classification (ImageNet).
- Image segmentation (controlling false-negative pixel rate; polyp / Cityscapes).
- Protein structure prediction.

## Relation to Other Wiki Sources

- [[sources/angelopoulos-2021-raps]] — companion paper from the same Berkeley group.
- [[sources/angelopoulos-2021-learn-then-test]] — extends RCPS from monotone to arbitrary risks via multiple hypothesis testing.
- [[sources/farinhas-2024-non-exchangeable-crc]] — risk-control extension to non-exchangeable data.
- [[sources/angelopoulos-2022-gentle-intro]] — practitioner-facing coverage of conformal risk control.

## Why It Matters

RCPS generalises classical tolerance regions and split conformal prediction to **arbitrary monotone losses**, opening the door to distribution-free, finite-sample control of FNR, IoU, F1, hierarchical mistake cost, and other application-specific risks that classical conformal coverage cannot directly target.

## Questions Raised

- How can the (α, δ) PAC-style guarantee be tightened to a marginal expected-risk guarantee that holds in expectation over the calibration set?
- Can UCB calibration be extended to non-monotone losses or multi-dimensional risk vectors?
- What happens when exchangeability between calibration and test data fails (covariate shift, label shift, time-series dependence)?
- How tight are the Waudby-Smith-Ramdas bounds in finite samples for very small `α` or very imbalanced losses?
- Can RCPS be combined with online / sequential calibration so that `λ` is updated as new labelled data arrives?

## See Also

- [[concepts/risk-controlling-prediction-sets]]
- [[concepts/conformal-risk-control]]
- [[concepts/learn-then-test]]
- [[entities/stephen-bates]], [[entities/lihua-lei]]
