---
title: "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"
page_id: sources/angelopoulos-2022-gentle-intro
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-21T14:00:00Z
updated: 2026-05-21T14:00:00Z
authors: ["Anastasios N. Angelopoulos", "Stephen Bates"]
year: 2022
venue: "Foundations and Trends in Machine Learning (arXiv:2107.07511)"
tags: [conformal-prediction, tutorial, uncertainty-quantification, distribution-free, prediction-sets, risk-control]
related: [
  concepts/conformal-prediction,
  concepts/split-conformal-prediction,
  concepts/conformalized-quantile-regression,
  concepts/conformal-risk-control,
  concepts/coverage-guarantee,
  concepts/exchangeability,
  concepts/prediction-intervals,
  concepts/uncertainty-quantification,
  concepts/conditional-validity,
  concepts/calibration,
  concepts/adaptive-prediction-sets,
  concepts/regularized-adaptive-prediction-sets,
  concepts/full-conformal-prediction,
  concepts/cross-conformal-prediction,
  concepts/weighted-conformal-prediction,
  concepts/conformal-outlier-detection,
  concepts/learn-then-test,
  concepts/marginal-coverage,
  concepts/conditional-coverage,
  concepts/nonconformity-score,
  concepts/group-balanced-conformal-prediction,
  concepts/class-conditional-conformal-prediction,
  concepts/conformal-predictive-distribution,
  entities/anastasios-angelopoulos,
  entities/stephen-bates,
  sources/zaffran-2022-aci,
  sources/xu-2022-spci,
  sources/chernozhukov-2021-distributional-cp
]
mind_map_priority: high
---

# A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification

**Authors:** [[entities/anastasios-angelopoulos|Anastasios N. Angelopoulos]], [[entities/stephen-bates|Stephen Bates]]

**Year:** 2022 (arXiv v6, December 2022)

**Venue:** *Foundations and Trends in Machine Learning* (arXiv:2107.07511)

## Summary

A monograph-length, hands-on tutorial on [[concepts/conformal-prediction|conformal prediction]] (CP) and distribution-free uncertainty quantification. The authors distill CP into a four-step recipe — heuristic uncertainty → [[concepts/nonconformity-score|nonconformity score]] → empirical `⌈(n+1)(1−α)⌉/n` quantile → prediction set `{y : s(x,y) ≤ q̂}` — and prove a finite-sample [[concepts/marginal-coverage|marginal coverage]] guarantee that holds for any model and any exchangeable data. Each method is paired with Python code and Jupyter notebooks.

Beyond the basic recipe, the paper surveys major extensions: [[concepts/adaptive-prediction-sets|Adaptive Prediction Sets (APS)]] and [[concepts/regularized-adaptive-prediction-sets|RAPS]] for classification, [[concepts/conformalized-quantile-regression|Conformalized Quantile Regression (CQR)]], conformalized scalar uncertainty (σ(x)), conformalized Bayes, [[concepts/group-balanced-conformal-prediction|group-balanced]] and [[concepts/class-conditional-conformal-prediction|class-conditional CP]], [[concepts/conformal-risk-control|conformal risk control]], [[concepts/conformal-outlier-detection|conformal outlier detection]], [[concepts/weighted-conformal-prediction|weighted CP under covariate shift]] and [[concepts/distribution-drift|distribution drift]], [[concepts/learn-then-test|Learn Then Test]] for non-monotone risks, and the [[concepts/full-conformal-prediction|full]] / [[concepts/cross-conformal-prediction|cross-conformal / CV+ / Jackknife+]] family.

## Key Contributions

1. **Unified split-conformal recipe.** Distills CP into a four-step protocol with a finite-sample marginal coverage theorem that holds for any model and any exchangeable data.

2. **Catalog of nonconformity scores.** Documents canonical score designs for classification (1−softmax, APS, RAPS), regression (CQR, σ-scaled residuals), and Bayes (posterior predictive density), and shows how score choice governs adaptivity and set size while validity is automatic.

3. **Extensions to non-standard settings.** Algorithms and theorems for group-balanced and class-conditional CP, [[concepts/conformal-risk-control|conformal risk control]] for general bounded monotone losses, [[concepts/conformal-outlier-detection|outlier detection]], [[concepts/weighted-conformal-prediction|weighted CP under covariate shift]], and [[concepts/learn-then-test|Learn Then Test]] for arbitrary risks.

4. **Diagnostics and evaluation.** Feature-stratified and size-stratified coverage metrics for approximate [[concepts/conditional-coverage|conditional coverage]]; the Beta distribution of empirical coverage conditional on the calibration set; calibration-set sizing tables (n ≈ 1000 for typical settings).

5. **Full conformal and historical synthesis.** Presents [[concepts/full-conformal-prediction|full (transductive) CP]], [[concepts/cross-conformal-prediction|cross-conformal / CV+ / Jackknife+]] as a computational/statistical-efficiency spectrum, and gives an extensive oral history of CP from Kolmogorov complexity through Vovk, Gammerman, Vapnik, Shafer, Papadopoulos, Lei, Wasserman, Barber, Romano, Tibshirani, Candès, and Ramdas.

## Why This Source Matters

This is the **canonical practitioner reference** for CP. It bridges the gap between the technical CP literature (Vovk-Gammerman-Shafer 2005) and applied ML deployments. Most subsequent CP papers cite it as their introductory pointer. The companion Jupyter notebooks make it the de facto starting point for engineers adopting CP.

## Relation to Other Wiki Sources

- [[sources/zaffran-2022-aci|Zaffran 2022 — Adaptive Conformal Predictions for Time Series]]: addresses the time-series gap left by the tutorial's i.i.d./exchangeable framing.
- [[sources/xu-2022-spci|Xu & Xie 2022 — SPCI]]: builds on the tutorial's score-design framework with sequential predictive scores.
- [[sources/chernozhukov-2021-distributional-cp|Chernozhukov 2021 — Distributional CP]]: extends the tutorial's interval-prediction view to full predictive distributions.
- [[sources/stocker-2025-conformal-timeseries-intro|Stocker et al. 2025]]: cites this as the companion tutorial for the i.i.d. case.

## Questions Raised

- When exact [[concepts/conditional-coverage|conditional coverage]] is impossible without distributional assumptions, what is the right notion of *approximate* conditional validity (size-stratified, group-balanced, multivalid) for high-stakes deployments?
- How should weights be designed for [[concepts/weighted-conformal-prediction|weighted CP]] under unknown or hard-to-estimate distribution drift, given the variance penalty of small effective sample size?
- Can [[concepts/nonconformity-score|nonconformity scores]] be *learned* (rather than hand-designed) to optimise adaptivity, set size, or risk-control objectives without sacrificing finite-sample validity?
- What is the right computational/statistical trade-off between [[concepts/split-conformal-prediction|split]], [[concepts/cross-conformal-prediction|cross-conformal / CV+ / Jackknife+]], and [[concepts/full-conformal-prediction|full]] CP in modern deep-learning workflows?

## See Also

- [[concepts/conformal-prediction]]
- [[concepts/uncertainty-quantification]]
- [[entities/anastasios-angelopoulos]], [[entities/stephen-bates]]
