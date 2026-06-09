---
title: "Predictive Inference Is Free with the Jackknife+-after-Bootstrap"
page_id: sources/kim-2020-jackknife-plus-after-bootstrap
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24T18:00:00Z
updated: 2026-05-24T18:00:00Z
authors: ["Byol Kim", "Chen Xu", "Rina Foygel Barber"]
year: 2020
venue: "NeurIPS 2020 (arXiv:2002.09025)"
tags: [conformal-prediction, jackknife-plus, bootstrap, ensemble-learning, bagging, out-of-bag, distribution-free]
related: [
  concepts/jackknife-plus-after-bootstrap,
  concepts/jackknife-plus,
  concepts/enbpi,
  concepts/conformal-prediction,
  concepts/exchangeability,
  concepts/prediction-intervals,
  entities/byol-kim,
  entities/chen-xu,
  entities/rina-foygel-barber,
  sources/barber-2021-jackknife-plus,
  sources/xu-2023-enbpi,
  sources/xu-2022-spci,
  sources/vovk-2012-cross-conformal,
  sources/angelopoulos-2022-gentle-intro
]
mind_map_priority: high
---

# Predictive Inference Is Free with the Jackknife+-after-Bootstrap (J+aB)

**Authors:** [[entities/byol-kim|Byol Kim]], [[entities/chen-xu|Chen Xu]], [[entities/rina-foygel-barber|Rina Foygel Barber]]

**Year:** 2020

**Venue:** NeurIPS 2020 (arXiv:2002.09025)

## Summary

**Primary source** for the wiki concept [[concepts/jackknife-plus-after-bootstrap|J+aB]]. Introduces the **jackknife+-after-bootstrap (J+aB)**, a distribution-free wrapper that produces predictive intervals for ensemble (bagging / subagging) methods at **no extra model-fitting cost** beyond a single ensemble, with a worst-case `1 − 2α` coverage guarantee.

The core trick: replace leave-one-out refits in [[sources/barber-2021-jackknife-plus|Jackknife+]] with **out-of-bag aggregations** from already-fitted bootstrap models. For each training index `i`, define `μ̂_{φ\i} = φ({μ̂_b : S_b does not contain i})`, reusing existing bootstrap members.

J+aB is the direct precursor to [[sources/xu-2023-enbpi|EnbPI]], which extends the same construction to time-series data without the exchangeability assumption.

## Theorem 1 (J+aB Coverage)

Under i.i.d. data and a symmetric base regressor `R` and aggregator `φ`, the J+aB prediction interval satisfies `P[Y_{n+1} ∈ C^{J+aB}_{α, n, B}(X_{n+1})] ≥ 1 − 2α` when `B` is drawn `Binomial(B̃, (1 − 1/(n+1))^m)` for sampling with replacement.

## Key Contributions

1. **J+aB construction.** Turns any bagging / subagging ensemble into a distribution-free predictive-interval method by reusing OOB aggregations as leave-one-out models.
2. **Coverage guarantee at no extra cost.** O(B) calls to the base regressor (same as a single ensemble) versus O(Bn) for jackknife+ wrapped around an ensemble.
3. **Stability variant.** Appendix B gives a stability condition on the aggregator `φ` under which valid coverage holds for any fixed `B`, justifying use with deterministic `B` in practice.
4. **General nonconformity scores.** Generalises beyond absolute residuals — CQR-style quantile scores and weighted residuals all work.
5. **Empirical validation.** Communities and Crime, BlogFeedback, MEPS-2016 with Ridge / Random Forest / Neural Network base learners. J+aB matches J+ensemble interval width while being far cheaper.

## Methodology Notes

- Built on jackknife+ (Barber et al. 2021) but replaces explicit leave-one-out refits with OOB aggregations.
- Proof uses a "lifted" construction (Algorithm 3) over `n+1` augmented points with leave-two-out residuals; the Binomial `B` is needed to symmetrise the count of bootstrap samples excluding each index.

## Limitations

- Worst-case coverage is `1 − 2α` rather than `1 − α`. Empirically coverage is close to nominal.
- The strict theorem requires `B` to be Binomially distributed (random rather than fixed). Deterministic `B` is justified only under the additional stability condition.
- Coverage is marginal, not conditional on `X_{n+1}`.
- Assumes i.i.d. / exchangeable data. Time-series extension is the motivation for [[sources/xu-2023-enbpi|EnbPI]].
- Experiments use small `n = 40`, limited by the cost of the J+ensemble baseline.

## Relation to Other Wiki Sources

- [[sources/barber-2021-jackknife-plus]] — the Jackknife+ foundation J+aB approximates without extra cost.
- [[sources/xu-2023-enbpi]] — extends J+aB to non-exchangeable time-series data.
- [[sources/xu-2022-spci]] — same authors' follow-up replacing residual quantiles with learned quantile regression for heteroskedastic time series.
- [[sources/vovk-2012-cross-conformal]] — cross-conformal lineage of bootstrap-aware CP.

## Questions Raised

- Can the `1 − 2α` bound be tightened to `1 − α` under mild additional assumptions on the aggregator `φ`?
- How does J+aB extend to non-exchangeable data? (Addressed by [[sources/xu-2023-enbpi|EnbPI]] and [[sources/xu-2022-spci|SPCI]].)
- What is the optimal choice of `B` and `m` for finite-sample efficiency?
- Can J+aB be combined with conditional-coverage methods (CQR, Mondrian) while preserving the cost-free property?

## See Also

- [[concepts/jackknife-plus-after-bootstrap]]
- [[concepts/enbpi]]
- [[entities/byol-kim]]
