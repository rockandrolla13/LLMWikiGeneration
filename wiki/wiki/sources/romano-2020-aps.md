---
title: "Classification with Valid and Adaptive Coverage"
page_id: sources/romano-2020-aps
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24T18:00:00Z
updated: 2026-05-24T18:00:00Z
authors: ["Yaniv Romano", "Matteo Sesia", "Emmanuel J. Candès"]
year: 2020
venue: "NeurIPS 2020 (arXiv:2006.02544)"
tags: [conformal-prediction, classification, adaptive-coverage, conditional-coverage, cv-plus, jackknife-plus]
related: [
  concepts/adaptive-prediction-sets,
  concepts/regularized-adaptive-prediction-sets,
  concepts/conditional-coverage,
  concepts/marginal-coverage,
  concepts/conformal-prediction,
  concepts/split-conformal-prediction,
  concepts/jackknife-plus,
  concepts/cross-conformal-prediction,
  entities/yaniv-romano,
  entities/matteo-sesia,
  entities/emmanuel-candes,
  sources/angelopoulos-2021-raps,
  sources/romano-2019-cqr,
  sources/angelopoulos-2022-gentle-intro
]
mind_map_priority: high
---

# Classification with Valid and Adaptive Coverage (APS)

**Authors:** [[entities/yaniv-romano|Yaniv Romano]], [[entities/matteo-sesia|Matteo Sesia]], [[entities/emmanuel-candes|Emmanuel J. Candès]]

**Year:** 2020

**Venue:** NeurIPS 2020 (arXiv:2006.02544)

## Summary

**Primary source** for the wiki concept [[concepts/adaptive-prediction-sets|Adaptive Prediction Sets (APS)]]. Introduces APS, a conformal classification procedure built on a novel **generalized inverse quantile conformity score**.

Starting from an oracle that would form smallest randomized prediction sets by including class labels in decreasing order of estimated probability until cumulative mass reaches `1 − α`, the authors define a conformity score equal to the smallest generalized quantile level that contains the true label. Calibrated via split-conformal, [[concepts/cross-conformal-prediction|cross-validation+]], or [[concepts/jackknife-plus|jackknife+]], the resulting sets provide finite-sample [[concepts/marginal-coverage|marginal coverage]] for any exchangeable data and any black-box classifier, while approximating [[concepts/conditional-coverage|conditional coverage]] far better than homogeneous conformal classification.

## Why It Matters

Homogeneous Conformal Classification (HCC) applies a single probability threshold to all inputs, so it over-covers easy inputs and under-covers hard ones. APS adapts the effective threshold per input through the cumulative-probability construction, yielding substantially better worst-slice conditional coverage. This is the direct precursor of [[sources/angelopoulos-2021-raps|RAPS]] which addresses APS's set-size inflation at ImageNet scale.

## Key Contributions

1. **Generalized inverse quantile conformity score.** Defined as the smallest oracle-quantile level whose set contains the true label. Scores are uniformly distributed conditional on `X` when the base classifier equals the true `P(Y|X)`, making them comparable across inputs (unlike earlier adaptive conformal scores).
2. **Theorem 1 (marginal coverage).** Split-conformal calibration with this score yields finite-sample marginal coverage `≥ 1 − α` for any exchangeable data and any permutation-invariant black-box, with near-tight upper bound when scores are a.s. distinct.
3. **Theorem 2 (CV+ / jackknife+ extension).** Achieves coverage `≥ 1 − 2α` in theory but empirically covers at level `1 − α`, providing tighter sets than split-conformal at higher computational cost.
4. **Worst-slice conditional coverage diagnostic.** Empirical proxy for conditional coverage used to demonstrate APS's advantage over HCC across SVC, random forest, and oracle backbones.

## Empirical Validation

APS variants achieve worst-slice conditional coverage near the nominal `1 − α` level across SVC, random forest, and oracle backbones on multinomial inhomogeneous-feature data and real classification benchmarks, where HCC and CQC fall significantly below `1 − α` even with oracle probabilities.

## Relation to Other Wiki Sources

- [[sources/angelopoulos-2021-raps]] — direct successor that adds regularisation for ImageNet-scale problems where APS sets become unnecessarily large.
- [[sources/romano-2019-cqr]] — same authors' regression analogue.
- [[sources/angelopoulos-2022-gentle-intro]] — practitioner exposition of APS and RAPS.

## Questions Raised

- How does APS perform when the base classifier's probability estimates are systematically biased or poorly calibrated (e.g., overconfident deep networks)?
- Can the randomized tie-breaking through `Uniform(0, 1)` variables be avoided or derandomized without sacrificing efficiency?
- What is the gap between APS's worst-slice conditional coverage and true conditional coverage as the number of classes `C` grows large?
- Could the generalized inverse quantile conformity score principle extend beyond classification to structured prediction or multi-label settings?

## See Also

- [[concepts/adaptive-prediction-sets]]
- [[concepts/regularized-adaptive-prediction-sets]]
- [[entities/matteo-sesia]]
