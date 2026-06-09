---
title: "Cross-conformal predictors"
page_id: sources/vovk-2012-cross-conformal
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24T16:00:00Z
updated: 2026-05-24T16:00:00Z
authors: ["Vladimir Vovk"]
year: 2012
venue: "arXiv:1208.0806 (also Annals of Mathematics and Artificial Intelligence 74, 2015)"
tags: [conformal-prediction, cross-validation, cross-conformal-prediction, vovk, foundational]
related: [
  concepts/conformal-prediction,
  concepts/cross-conformal-prediction,
  concepts/split-conformal-prediction,
  concepts/exchangeability,
  concepts/jackknife-plus,
  entities/vladimir-vovk,
  sources/vovk-2005-algorithmic-learning,
  sources/shafer-2007-cp-tutorial,
  sources/angelopoulos-2022-gentle-intro
]
mind_map_priority: medium
---

# Cross-conformal predictors

**Authors:** [[entities/vladimir-vovk|Vladimir Vovk]]

**Year:** 2012 (arXiv); 2015 (*Annals of Mathematics and Artificial Intelligence*)

**Venue:** arXiv:1208.0806

## Summary

Vovk introduces [[concepts/cross-conformal-prediction|cross-conformal prediction (CCP)]], a hybrid of inductive conformal prediction (ICP) and K-fold cross-validation. CCP keeps ICP's computational efficiency while recovering some of the predictive efficiency that ICP loses by holding out a calibration set.

The construction. Partition the training set into K folds. For each fold k, fit an inductive nonconformity measure on the other K−1 folds (the proper training set) and score the examples in fold k together with the test example under each postulated label `y`. The per-fold p-values `p^y_k` are merged into a combined p-value `p^y`. Vovk shows that under equal-sized folds and K ≪ ℓ, the merge reduces essentially to the arithmetic mean of the per-fold p-values. Confidence, credibility, and set predictors are defined exactly as for ICP.

The crucial design choice is averaging, not Fisher-combining. Appendix A demonstrates that Fisher's method (the standard combiner for independent p-values) produces severely miscalibrated "naive CCP" predictions because the per-fold p-values are heavily dependent.

## Key Contributions

1. Defines [[concepts/cross-conformal-prediction|cross-conformal prediction (CCP)]] as a K-fold hybrid of inductive CP and cross-validation that uses the full training set for calibration.
2. Shows that averaging per-fold p-values (equivalently, pooling ranks across folds) is the correct combination rule. Derives `p^y ≈ mean of p^y_k` under equal fold sizes and K ≪ ℓ.
3. Demonstrates empirically on Spambase + MART that CCP is well-calibrated despite the absence of a theoretical validity proof.
4. Quantifies CCP's efficiency gain over ICP: dramatically reduced variance of confidence across seeds (std dev ~0.05% for CCP vs 0.109% for ICP), and slightly higher mean confidence.
5. Shows in Appendix A that Fisher's method for combining p-values produces a "naive CCP" that is badly miscalibrated, motivating averaging as the correct combiner.
6. Poses the open problem (Section 4) of establishing theoretical validity guarantees for CCP, framed in the language of tolerance regions.

## Why This Source Matters

This is the primary reference for [[concepts/cross-conformal-prediction|cross-conformal prediction]]. It's also the conceptual precursor to the [[concepts/jackknife-plus|Jackknife+]] and CV+ work by Barber, Candès, Ramdas, and Tibshirani (2021), which gave the family the rigorous theoretical guarantees Vovk's original paper left open.

Empirical setup. Spambase dataset (4601 examples, binary spam/email classification), MART gradient boosting via the R `gbm` package, 3600/1001 train/test split, K ∈ {5, 10}. The Spambase + MART combination is small enough to reproduce in minutes — useful for testing CP intuitions on a real, non-toy dataset.

## Relation to Other Wiki Sources

- [[sources/vovk-2005-algorithmic-learning]] — book in which ICP was formalised.
- [[sources/shafer-2007-cp-tutorial]] — companion theoretical tutorial.
- [[sources/angelopoulos-2022-gentle-intro]] — modern tutorial; covers Jackknife+ / CV+ as descendants of this paper.
- [[sources/xu-2023-enbpi]] — EnbPI uses the same bootstrap-LOO idea to achieve cross-conformal-style intervals on time-series data.

## Questions Raised

- Can theoretical validity guarantees (e.g., marginal coverage bounds) be established for cross-conformal predictors, as they are for ICP via Proposition 1? *Vovk's explicit open problem in Section 4.* (Partially addressed by Barber et al. 2021 for the closely-related Jackknife+ / CV+.)
- What is the optimal number of folds K, and how does this depend on the learning curve of the underlying algorithm?
- Why exactly does p-value averaging yield well-calibrated combined p-values despite the per-fold p-values being dependent — what is the precise dependency structure?
- How does CCP behave on regression and multi-class classification, beyond the binary Spambase setting?

## See Also

- [[concepts/cross-conformal-prediction]]
- [[concepts/jackknife-plus]]
- [[entities/vladimir-vovk]]
