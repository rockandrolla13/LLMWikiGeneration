---
title: "Distribution-Free Predictive Inference for Regression"
page_id: sources/lei-2018-distribution-free-regression
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24T18:00:00Z
updated: 2026-05-24T18:00:00Z
authors: ["Jing Lei", "Max G'Sell", "Alessandro Rinaldo", "Ryan J. Tibshirani", "Larry Wasserman"]
year: 2018
venue: "Journal of the American Statistical Association 113(523), 1094-1111 (DOI 10.1080/01621459.2017.1307116). arXiv:1604.04173."
tags: [conformal-prediction, regression, split-conformal, jackknife, locally-adaptive, distribution-free, high-dimensional, loco]
related: [
  concepts/conformal-prediction,
  concepts/split-conformal-prediction,
  concepts/full-conformal-prediction,
  concepts/nonconformity-score,
  concepts/exchangeability,
  concepts/marginal-coverage,
  concepts/conditional-coverage,
  entities/jing-lei,
  entities/max-gsell,
  entities/alessandro-rinaldo,
  entities/ryan-tibshirani,
  entities/larry-wasserman,
  sources/tibshirani-2019-covariate-shift,
  sources/vovk-2005-algorithmic-learning,
  sources/angelopoulos-2022-gentle-intro,
  sources/romano-2019-cqr,
  sources/barber-2021-jackknife-plus
]
mind_map_priority: high
---

# Distribution-Free Predictive Inference for Regression

**Authors:** [[entities/jing-lei|Jing Lei]], [[entities/max-gsell|Max G'Sell]], [[entities/alessandro-rinaldo|Alessandro Rinaldo]], [[entities/ryan-tibshirani|Ryan J. Tibshirani]], [[entities/larry-wasserman|Larry Wasserman]]

**Year:** 2018

**Venue:** *JASA* 113(523), 1094-1111 (DOI 10.1080/01621459.2017.1307116). arXiv:1604.04173 (2016).

## Summary

The **pre-Angelopoulos canonical reference** for distribution-free predictive inference in regression via [[concepts/conformal-prediction|conformal inference]]. Provides finite-sample marginal coverage guarantees without distributional assumptions on `P`, and works with any base regression estimator.

The paper establishes [[concepts/split-conformal-prediction|split conformal regression]] as the practical workhorse — computationally cheap (cost dominated by a single model fit) while retaining exact finite-sample coverage. Analyses full conformal, split conformal, jackknife, and rank-one-out (ROO) variants; develops **locally-weighted (σ-scaled) conformal inference** for heteroskedastic data; and proposes the **LOCO** (leave-one-covariate-out) model-free notion of variable importance. The accompanying `conformalInference` R package is the de facto practical implementation.

## Key Contributions

1. **Finite-sample marginal coverage for any regression estimator.** `P(Y_{n+1} ∈ C(X_{n+1})) ≥ 1−α` under only the i.i.d. (exchangeability) assumption.
2. **Split conformal as the practical default.** Same finite-sample marginal coverage as full conformal but at a fraction of the computational cost — single model fit vs grid over candidate `y` values.
3. **Locally-weighted (σ-scaled) conformal regression.** Rescales residuals by an estimate of conditional spread `σ(x)`, producing prediction intervals whose width varies with `x` while preserving marginal coverage. Predecessor of [[sources/romano-2019-cqr|CQR]].
4. **Jackknife predictive intervals analysed.** Asymptotic validity only under strong stability/MSE conditions — strictly weaker than split conformal's non-asymptotic guarantee.
5. **Rank-one-out (ROO) conformal inference.** Extension giving valid in-sample prediction intervals at essentially the same computational cost as split.
6. **LOCO variable importance.** Model-free notion based on prediction-error changes when a single covariate is removed. Independent of selective-inference or debiased-lasso machinery.
7. **Estimator-dependent oracle bounds.** Under base-estimator stability, intervals are close to an oracle band (Theorems 3.2, 3.3); under consistency, intervals approach the super-oracle (Theorems 3.4, 3.5).

## Why It Matters

For ~5 years (2018-2022) this was **the** practical reference for CP-in-regression. The σ-scaled locally-adaptive idea here is what [[concepts/conformalized-quantile-regression|CQR]] later generalises by using quantile regression as the underlying predictor. The companion R package `conformalInference` was the dominant CP-in-R implementation before the MAPIE-era Python tools took over.

## Relation to Other Wiki Sources

- [[sources/vovk-2005-algorithmic-learning]] — the foundational framework this paper makes practical for regression.
- [[sources/romano-2019-cqr]] — generalises the σ-scaled locally-adaptive idea via quantile regression.
- [[sources/tibshirani-2019-covariate-shift]] — same author (Tibshirani) extending CP under covariate shift.
- [[sources/barber-2021-jackknife-plus]] — addresses the weakness of the plain jackknife identified here.
- [[sources/angelopoulos-2022-gentle-intro]] — modern practitioner companion.

## Questions Raised

- How tight can conformal intervals be made under conditional (rather than marginal) coverage targets in regression?
- What is the optimal way to estimate the local scale `σ(x)` for locally-adaptive conformal regression?
- Can the jackknife approach be salvaged with weaker stability conditions, or is split conformal strictly preferred in high dimensions?
- How does LOCO-based variable importance compare to selective-inference and debiased-lasso confidence intervals in practice?

## See Also

- [[concepts/split-conformal-prediction]]
- [[concepts/nonconformity-score]]
- [[entities/jing-lei]], [[entities/larry-wasserman]]
