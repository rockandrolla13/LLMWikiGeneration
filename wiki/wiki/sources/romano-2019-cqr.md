---
title: Conformalized Quantile Regression
page_id: sources/romano-2019-cqr
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24 18:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Yaniv Romano
- Evan Patterson
- Emmanuel J. Candès
year: 2019
venue: NeurIPS 2019 (arXiv:1905.03222)
tags:
- conformal-prediction
- quantile-regression
- heteroskedasticity
- prediction-intervals
- distribution-free
related:
- concepts/conformalized-quantile-regression
- concepts/quantile-regression
- concepts/split-conformal-prediction
- concepts/nonconformity-score
- concepts/conformal-prediction
- concepts/marginal-coverage
- entities/yaniv-romano
- entities/evan-patterson
- entities/emmanuel-candes
- sources/lei-2018-distribution-free-regression
- sources/romano-2020-aps
- sources/tibshirani-2019-covariate-shift
- sources/angelopoulos-2022-gentle-intro
- sources/chernozhukov-2021-distributional-cp
mind_map_priority: high
schema_version: 2
uuid: 57f5348b-5747-536c-be6d-828238485d9b
content_hash: sha256:af7169553bb2847bf4482d25b650c0d1cca4a3919b2b814b69bb353adeb464cf
---

<!-- AUTHORED REGION START -->
# Conformalized Quantile Regression

**Authors:** [[entities/yaniv-romano|Yaniv Romano]], [[entities/evan-patterson|Evan Patterson]], [[entities/emmanuel-candes|Emmanuel J. Candès]]

**Year:** 2019

**Venue:** NeurIPS 2019 (arXiv:1905.03222). Code: `github.com/yromano/cqr`.

## Summary

**Primary source** for the wiki concept [[concepts/conformalized-quantile-regression|CQR]]. Combines [[concepts/split-conformal-prediction|split conformal prediction]] with [[concepts/quantile-regression|quantile regression]] to produce prediction intervals that are simultaneously distribution-free with finite-sample marginal coverage **and** adaptive to heteroskedasticity.

The CQR conformity score is symmetric:

```
E_i = max{q̂_{α_lo}(X_i) − Y_i, Y_i − q̂_{α_hi}(X_i)}
```

This single score accounts for both undercoverage and overcoverage. The `(1−α)(1 + 1/|I_2|)` empirical quantile of these scores adjusts the lower and upper quantile estimates to produce a valid prediction interval.

## Theorem 1 (CQR Coverage)

If `(X_i, Y_i)` are exchangeable, `P{Y_{n+1} ∈ C(X_{n+1})} ≥ 1 − α`. If conformity scores are a.s. distinct, coverage is also upper-bounded by `1 − α + 1/(|I_2| + 1)`.

## Why It Matters

CQR is **the canonical CP-meets-QR synthesis** and the workhorse for HFT-style use cases. Standard split conformal intervals have fixed length `2 · Q_{1−α}(R, I_2)` independent of `X_{n+1}`, while CQR intervals vary in width based on the underlying quantile estimates. Width adapts to local variability while marginal validity is automatic.

## Key Contributions

1. **CQR conformity score.** Symmetric `E_i = max(q̂_lo − Y_i, Y_i − q̂_hi)`, generalising to asymmetric per-tail variants.
2. **Theorem 1 (coverage).** Finite-sample, distribution-free marginal coverage with both lower and upper bounds.
3. **Algorithm-agnostic.** Wraps any quantile regression method: quantile random forests, quantile neural networks, gradient-boosted quantile regressors.
4. **Empirical efficiency.** On simulated heteroscedastic data with outliers, CQR achieves 91.06% coverage with average length 1.99 vs split conformal (91.4%, length 2.91) and locally weighted split conformal (91.7%, length 2.86).
5. **Cross-dataset validation.** Across 11 real regression datasets, CQR produces shorter intervals than competing CP methods while maintaining target coverage.

## Relation to Other Wiki Sources

- [[sources/lei-2018-distribution-free-regression]] — introduces σ-scaled locally-adaptive CP that CQR generalises via quantile regression.
- [[sources/romano-2020-aps]] — same authors' classification analogue.
- [[sources/tibshirani-2019-covariate-shift]] — CQR-compatible weighted variants follow from WCP.
- [[sources/angelopoulos-2022-gentle-intro]] — practitioner exposition.
- [[sources/chernozhukov-2021-distributional-cp]] — extends to full distributional output.

## Questions Raised

- How does CQR perform under covariate shift or distribution shift where exchangeability fails?
- Can the symmetric two-sided conformity score be replaced with asymmetric per-tail scores for improved efficiency?
- How does CQR interact with conditional coverage — does adaptivity translate into approximate conditional validity?
- What is the optimal split ratio between proper training set and calibration set?
- How sensitive is interval efficiency to the quality of the underlying quantile estimator?

## See Also

- [[concepts/conformalized-quantile-regression]]
- [[concepts/quantile-regression]]
- [[entities/yaniv-romano]]

<!-- AUTHORED REGION END -->
