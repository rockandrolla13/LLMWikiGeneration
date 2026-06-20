---
title: Conformal Prediction Under Covariate Shift
page_id: sources/tibshirani-2019-covariate-shift
page_type: source
source_type: paper
revision_id: 2
created: 2026-05-24 18:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Ryan J. Tibshirani
- Rina Foygel Barber
- Emmanuel J. Candès
- Aaditya Ramdas
year: 2019
venue: NeurIPS 2019 (arXiv:1904.06019v3)
revision_note: arXiv v3 (the published NeurIPS version) is now staged at markdown_output/1904.06019v3.md
  alongside the earlier v1 (markdown_output/1904.06019.md). The substantive content
  is unchanged from v1; v3 incorporates typesetting and minor copy-edits for the NeurIPS
  camera-ready. Citation should reference v3.
tags:
- conformal-prediction
- covariate-shift
- weighted-exchangeability
- distribution-free-inference
- likelihood-ratio
related:
- concepts/weighted-conformal-prediction
- concepts/conformal-prediction
- concepts/exchangeability
- concepts/distribution-drift
- concepts/split-conformal-prediction
- concepts/non-exchangeable-conformal-prediction
- entities/ryan-tibshirani
- entities/rina-foygel-barber
- entities/emmanuel-candes
- entities/aaditya-ramdas
- sources/barber-2023-beyond-exchangeability
- sources/angelopoulos-2022-gentle-intro
- sources/vovk-2005-algorithmic-learning
- sources/farinhas-2024-non-exchangeable-crc
- sources/zaffran-2022-aci
mind_map_priority: high
schema_version: 2
uuid: ec484c98-54e8-5817-9c69-3f75110b9678
content_hash: sha256:f3e76653aa285855daa4b7f9c4240a373665787cf11f0d2f33ecfd74563b32c0
---

<!-- AUTHORED REGION START -->
# Conformal Prediction Under Covariate Shift

**Authors:** [[entities/ryan-tibshirani|Ryan J. Tibshirani]], [[entities/rina-foygel-barber|Rina Foygel Barber]], [[entities/emmanuel-candes|Emmanuel J. Candès]], [[entities/aaditya-ramdas|Aaditya Ramdas]]

**Year:** 2019

**Venue:** NeurIPS 2019 (arXiv:1904.06019)

## Summary

**Primary source** for the wiki concept [[concepts/weighted-conformal-prediction|weighted conformal prediction (WCP)]]. The paper extends [[concepts/conformal-prediction|conformal prediction]] beyond the i.i.d./exchangeable setting to handle covariate shift: the conditional law of `Y|X` is shared between training and test, but the marginal covariate distribution differs.

The construction reweights each nonconformity score by the likelihood ratio `w(x) = dP̃_X(x) / dP_X(x)` (normalised across training points and the test point), yielding a weighted empirical distribution whose quantile delivers finite-sample, distribution-free 1−α prediction coverage under covariate shift. The construction reduces to ordinary split conformal when `w ≡ 1`, and is robust to unknown normalising constants in `w`.

The mechanics generalise to a broader notion the authors call **weighted exchangeability**: data are weighted-exchangeable if their joint density factorises through individual weight functions times a symmetric kernel. Covariate shift is a special case; the same framework also covers latent-variable and missing-data settings.

## Key Contributions

1. **Weighted conformal prediction (WCP).** Reweighting of nonconformity scores by `p_i^w(x) ∝ w(X_i)`, restoring exact finite-sample 1−α coverage under covariate shift.
2. **Weighted exchangeability framework (Theorem 2).** Formal definition of a joint distribution being weighted-exchangeable with weight functions `w_1, ..., w_n`, generalising exchangeability and unifying covariate shift, latent-variable, and missing-data settings under one conformal umbrella.
3. **Weighted split conformal.** Computationally efficient split variant using a pre-fit regressor with weighted quantiles, retaining the coverage guarantee at near-linear cost.
4. **Density-ratio estimation via probabilistic classification.** Practical recipe estimating `w(x)` by fitting a classifier (logistic regression, random forests) to discriminate training vs test covariates and taking the conditional odds ratio as `ŵ`.
5. **Effective sample size diagnostic.** Quantifies the variance penalty from weighting via `n_eff = ‖w(X_{1:n})‖_1² / ‖w(X_{1:n})‖_2²`, explaining the observed coverage-histogram overdispersion.

## Empirical Validation

UCI airfoil data with exponential tilting:
- Ordinary split conformal undercovers (82.2% vs. nominal 90%).
- Oracle-weighted split conformal recovers nominal coverage (90.8%) at the cost of reduced effective sample size.
- Estimated weights via logistic regression or random forests achieve ~91% coverage in practice.

## Relation to Other Wiki Sources

- [[sources/barber-2023-beyond-exchangeability]] — extends WCP to fixed-weight, distribution-shift-agnostic settings (NexCP).
- [[sources/vovk-2005-algorithmic-learning]] — the foundational exchangeable-data framework this paper extends.
- [[sources/angelopoulos-2022-gentle-intro]] — practitioner-facing coverage of WCP.
- [[sources/farinhas-2024-non-exchangeable-crc]] — risk-control variant under non-exchangeable data.
- [[sources/zaffran-2022-aci]] — alternative shift-handling approach via online α-adaptation.

## Questions Raised

- How accurately must `w` be estimated for finite-sample coverage to remain near nominal, and what is the price of mis-specified weights?
- Can the weighted-exchangeability framework be extended to label shift, concept drift, or general joint-distribution shift where `Y|X` also changes?
- How does the effective-sample-size penalty interact with adaptive nonconformity scores (CQR, locally weighted residuals)?
- What are the theoretical guarantees when the density-ratio classifier is trained on overlapping data, raising potential leakage concerns?

## See Also

- [[concepts/weighted-conformal-prediction]]
- [[concepts/non-exchangeable-conformal-prediction]]
- [[entities/ryan-tibshirani]]

<!-- AUTHORED REGION END -->
