---
title: "Conformal Prediction Beyond Exchangeability"
page_id: sources/barber-2023-beyond-exchangeability
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24T18:00:00Z
updated: 2026-05-24T18:00:00Z
authors: ["Rina Foygel Barber", "Emmanuel J. Candès", "Aaditya Ramdas", "Ryan J. Tibshirani"]
year: 2023
venue: "Annals of Statistics 51(2), 816-845 (DOI 10.1214/23-AOS2276). arXiv:2202.13415."
tags: [conformal-prediction, non-exchangeable, distribution-drift, weighted-quantiles, time-series, coverage-gap, total-variation, nex-cp]
related: [
  concepts/non-exchangeable-conformal-prediction,
  concepts/weighted-conformal-prediction,
  concepts/conformal-prediction,
  concepts/exchangeability,
  concepts/distribution-drift,
  concepts/split-conformal-prediction,
  concepts/full-conformal-prediction,
  concepts/jackknife-plus,
  concepts/online-conformal-prediction,
  entities/rina-foygel-barber,
  entities/emmanuel-candes,
  entities/aaditya-ramdas,
  entities/ryan-tibshirani,
  sources/tibshirani-2019-covariate-shift,
  sources/barber-2021-jackknife-plus,
  sources/farinhas-2024-non-exchangeable-crc,
  sources/stocker-2025-conformal-timeseries-intro,
  sources/gibbs-2021-aci,
  sources/zaffran-2022-aci
]
mind_map_priority: high
---

# Conformal Prediction Beyond Exchangeability

**Authors:** [[entities/rina-foygel-barber|Rina Foygel Barber]], [[entities/emmanuel-candes|Emmanuel J. Candès]], [[entities/aaditya-ramdas|Aaditya Ramdas]], [[entities/ryan-tibshirani|Ryan J. Tibshirani]]

**Year:** 2023

**Venue:** *Annals of Statistics* 51(2), 816-845 (DOI 10.1214/23-AOS2276). arXiv:2202.13415.

## Summary

Generalises split, full, and [[concepts/jackknife-plus|jackknife+]] [[concepts/conformal-prediction|CP]] to non-exchangeable data via **fixed, non-data-dependent weights** `w_i ∈ [0, 1]` on training points. Introduces **Non-Exchangeable Conformal Prediction (NexCP)** as a named family — see [[concepts/non-exchangeable-conformal-prediction|NexCP]].

The headline result is a distribution-free coverage-gap bound:

```
P(miscoverage) ≤ α + Σ_i w_i · d_TV(Z, Z^i) / (1 + Σ_i w_i)
```

where `Z^i` is the data sequence with the test point swapped with training point `i`, and `d_TV` is total variation distance. The bound holds with no assumption on the joint distribution of the `n+1` points.

A strictly stronger **residual-level** bound is also provided, computing `d_TV` on residual vectors `R(Z)` vs `R(Z^i)` rather than the data vectors directly — much tighter in high dimensions.

A **randomisation technique** is introduced to allow non-symmetric fitting algorithms `A` (e.g., recency-weighted models) without breaking the guarantee.

Critically, the construction **recovers standard CP coverage exactly** when data are exchangeable, regardless of the weight choice. There is no penalty for using weighted procedures even on exchangeable data.

## Key Contributions

1. **NexCP family.** Split, full, and jackknife+ variants of conformal prediction with fixed weights, requiring no knowledge of the shift mechanism (unlike [[concepts/weighted-conformal-prediction|WCP]] which needs the likelihood ratio).
2. **Coverage-gap bound.** Distribution-free upper bound on miscoverage in terms of a weighted sum of total-variation distances.
3. **Residual-level bound.** Strictly stronger version computing `d_TV` on residual vectors; can be orders of magnitude tighter.
4. **Lemma 1.** For independent data, `d_TV(Z, Z^i) ≤ d_TV(Z_i, Z_{n+1})`, connecting the bound to pairwise marginal drift.
5. **Randomisation for non-symmetric algorithms.** Allows recency-weighted fits without symmetry assumption.
6. **Exchangeable recovery.** When data are exchangeable, `d_TV(Z, Z^i) = 0` so the bound matches standard CP — using NexCP never hurts.

## Empirical Validation

ELEC2 electricity data and US election forecasting: standard CP fails to cover under known temporal drift; NexCP with simple exponential weights recovers near-nominal coverage.

## Why It Matters

This is the **theoretical foundation** for most of the modern non-exchangeable CP work. [[sources/farinhas-2024-non-exchangeable-crc|Farinhas et al. 2024]] (non-exchangeable CRC) builds directly on this; [[sources/stocker-2025-conformal-timeseries-intro|Stocker et al. 2025]]'s four-family taxonomy cites this paper as the formal underpinning of the "reweight calibration" family.

## Relation to Other Wiki Sources

- [[sources/tibshirani-2019-covariate-shift]] — earlier weighted-CP paper from the same author group, but requires known likelihood ratio.
- [[sources/barber-2021-jackknife-plus]] — the foundation that this paper extends to non-exchangeable data.
- [[sources/farinhas-2024-non-exchangeable-crc]] — risk-control extension under the same non-exchangeability framework.
- [[sources/stocker-2025-conformal-timeseries-intro]] — taxonomy where NexCP anchors the "reweight calibration" family.
- [[sources/gibbs-2021-aci]] / [[sources/zaffran-2022-aci]] — alternative shift-handling via online α-adaptation.

## Tension With Tibshirani 2019

NexCP uses fixed weights without knowing the likelihood ratio and retains coverage under exchangeability. WCP needs the likelihood ratio and loses validity under exchangeability if weights are misspecified. The two papers solve different problems: WCP is optimal under known covariate shift; NexCP is robust under unknown shift.

## Questions Raised

- How should weights `w_i` be chosen adaptively in practice without violating the fixed-weight assumption?
- Can the residual-level TV bound be estimated empirically to give actionable coverage diagnostics?
- How does NexCP compare to ACI / AgACI / online conformal in finite-sample regimes under abrupt vs gradual drift?
- Can the bound be tightened under specific dependence structures (e.g., β-mixing time series)?

## See Also

- [[concepts/non-exchangeable-conformal-prediction]]
- [[concepts/weighted-conformal-prediction]]
- [[entities/rina-foygel-barber]]
