---
title: "Uncertainty Sets for Image Classifiers using Conformal Prediction"
page_id: sources/angelopoulos-2021-raps
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24T18:00:00Z
updated: 2026-05-24T18:00:00Z
authors: ["Anastasios N. Angelopoulos", "Stephen Bates", "Jitendra Malik", "Michael I. Jordan"]
year: 2021
venue: "ICLR 2021 (arXiv:2009.14193)"
tags: [conformal-prediction, image-classification, uncertainty-quantification, prediction-sets, deep-learning, imagenet, regularization, raps]
related: [
  concepts/regularized-adaptive-prediction-sets,
  concepts/adaptive-prediction-sets,
  concepts/cp-for-vision,
  concepts/split-conformal-prediction,
  concepts/conformal-prediction,
  concepts/marginal-coverage,
  concepts/nonconformity-score,
  entities/anastasios-angelopoulos,
  entities/stephen-bates,
  entities/jitendra-malik,
  entities/michael-i-jordan,
  sources/romano-2020-aps,
  sources/angelopoulos-2022-gentle-intro,
  sources/angelopoulos-2021-learn-then-test,
  sources/bates-2021-rcps
]
mind_map_priority: high
---

# Uncertainty Sets for Image Classifiers using Conformal Prediction (RAPS)

**Authors:** [[entities/anastasios-angelopoulos|Anastasios N. Angelopoulos]], [[entities/stephen-bates|Stephen Bates]], [[entities/jitendra-malik|Jitendra Malik]], [[entities/michael-i-jordan|Michael I. Jordan]]

**Year:** 2021

**Venue:** ICLR 2021 (arXiv:2009.14193)

## Summary

**Primary source** for the wiki concept [[concepts/regularized-adaptive-prediction-sets|RAPS]]. Introduces **Regularized Adaptive Prediction Sets**, a [[concepts/conformal-prediction|conformal prediction]] algorithm that produces small, stable, and adaptive prediction sets for image classifiers with finite-sample marginal coverage guarantees.

RAPS modifies the [[concepts/adaptive-prediction-sets|APS]] procedure of [[sources/romano-2020-aps|Romano et al. 2020]] by adding a regularization penalty `λ · (o_x(y) − k_reg)_+` on classes deep in the predicted-probability tail. This mitigates the **permutation problem** caused by miscalibrated tail probabilities in CNN softmax outputs.

## Why It Matters

Without regularisation, APS sets on ImageNet are huge (~19 classes on average for ResNeXt-101 at α = 0.1) because the long tail of low-probability classes drags out the cumulative-sum cutoff. RAPS sets at the same coverage drop to ~2 classes — a 10× reduction while preserving the finite-sample coverage guarantee.

## Key Contributions

1. **RAPS conformity score.** `s_RAPS(x, y) = s_APS(x, y) + λ · max(0, r_y(x) − k_reg)` where `r_y(x)` is the rank of class `y` in the sorted softmax output.
2. **Top-k dominance (Proposition 2).** With `k_reg ≤ k*` and `λ = 1`, RAPS sets are no larger on average than the optimal fixed-size top-k procedure while maintaining coverage.
3. **Permutation-problem analysis.** Identifies the failure mode of APS on large-class problems: 5% of true classes land deep in the softmax tail due to miscalibration, forcing APS to expand sets to maintain coverage.
4. **ImageNet-scale validation.** Demonstrated across 9 pretrained classifiers: ResNeXt-101, ResNet-152/101/50/18, DenseNet-161, VGG16, Inception, ShuffleNet.
5. **ImageNet-V2 distribution-shift robustness.** Results replicate under the ImageNet-V2 distribution-shift benchmark.

## Empirical Validation

ImageNet with ResNeXt-101 at α = 0.1:
- Naive top-k: undercovers.
- APS: covers, mean set size ~19.
- RAPS: covers, mean set size ~2.

## Relation to Other Wiki Sources

- [[sources/romano-2020-aps]] — the APS paper this regularises.
- [[sources/angelopoulos-2022-gentle-intro]] — same first author's later tutorial putting RAPS in context.
- [[sources/angelopoulos-2021-learn-then-test]] / [[sources/bates-2021-rcps]] — companion papers from the same Berkeley group on risk-control extensions.

## Questions Raised

- How should `k_reg` and `λ` be chosen adaptively per dataset/classifier beyond the heuristic in Appendix E?
- Can the regularization idea be extended beyond marginal coverage to class-conditional or group-conditional coverage?
- How does RAPS interact with distribution shift (e.g., ImageNet → ImageNet-V2 gap) when exchangeability fails?
- Can RAPS be combined with calibration alternatives beyond Platt / temperature scaling?

## See Also

- [[concepts/regularized-adaptive-prediction-sets]]
- [[concepts/cp-for-vision]]
- [[entities/jitendra-malik]], [[entities/michael-i-jordan]]
