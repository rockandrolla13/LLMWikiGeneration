---
title: Predictive Inference with the Jackknife+
page_id: sources/barber-2021-jackknife-plus
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-24 18:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Rina Foygel Barber
- Emmanuel J. Candès
- Aaditya Ramdas
- Ryan J. Tibshirani
year: 2021
venue: Annals of Statistics 49(1), 486-507 (DOI 10.1214/20-AOS1965). arXiv:1905.02928.
tags:
- conformal-prediction
- jackknife
- jackknife-plus
- cv-plus
- leave-one-out
- distribution-free
- algorithmic-stability
related:
- concepts/jackknife-plus
- concepts/cross-conformal-prediction
- concepts/conformal-prediction
- concepts/split-conformal-prediction
- concepts/full-conformal-prediction
- concepts/exchangeability
- concepts/jackknife-plus-after-bootstrap
- entities/rina-foygel-barber
- entities/emmanuel-candes
- entities/aaditya-ramdas
- entities/ryan-tibshirani
- sources/tibshirani-2019-covariate-shift
- sources/barber-2023-beyond-exchangeability
- sources/vovk-2012-cross-conformal
- sources/kim-2020-jackknife-plus-after-bootstrap
- sources/angelopoulos-2022-gentle-intro
mind_map_priority: high
schema_version: 2
uuid: ba486bdd-ecc2-5df3-9001-ef8b3db2f500
content_hash: sha256:1241e9627798465681a09670cda650c0648a59d2940e7b8cbb449b34534d6266
---

<!-- AUTHORED REGION START -->
# Predictive Inference with the Jackknife+

**Authors:** [[entities/rina-foygel-barber|Rina Foygel Barber]], [[entities/emmanuel-candes|Emmanuel J. Candès]], [[entities/aaditya-ramdas|Aaditya Ramdas]], [[entities/ryan-tibshirani|Ryan J. Tibshirani]]

**Year:** 2021

**Venue:** *Annals of Statistics* 49(1), 486-507 (DOI 10.1214/20-AOS1965). arXiv:1905.02928 (2019).

## Summary

**Primary source** for the wiki concept [[concepts/jackknife-plus|Jackknife+]]. Introduces the **Jackknife+** predictive interval: replace `μ̂(X_{n+1}) ± R_i^{LOO}` with `μ̂_{−i}(X_{n+1}) ± R_i^{LOO}`, then take lower/upper empirical quantiles across `i`. This one modification turns the classical (unstable) jackknife into a distribution-free, finite-sample 1−2α coverage procedure under [[concepts/exchangeability|exchangeability]], with no algorithm-stability assumptions.

The proof uses a tournament / comparison-matrix argument (Landau 1953) on the `(n+1) × (n+1)` residual matrix. The factor of 2 is shown to be tight by explicit pathological constructions (Theorem 2).

The construction generalises to K-fold via **CV+**, with a 1−2α − √(2/n) coverage bound uniform in K (Theorem 4) — closing the gap left by Vovk's [[concepts/cross-conformal-prediction|cross-conformal]] bound, which becomes vacuous at K = n. The new √(2/n) term comes from a V-statistic variance argument over across-fold comparison-matrix row sums.

## Key Contributions

1. **Jackknife+ interval.** Uses LOO predictions, not just residuals: `Ĉ(x) = [Q^{−}_α(μ̂_{−i}(x) − R_i), Q^{+}_{1−α}(μ̂_{−i}(x) + R_i)]`.
2. **Theorem 1 (1−2α coverage).** Distribution-free, finite-sample lower coverage bound for jackknife+ via tournament argument.
3. **Theorem 2 (tightness).** Pathological constructions showing the factor of 2 is unavoidable in the assumption-free regime.
4. **Jackknife-minmax.** Strictly conservative variant achieving full 1−α distribution-free guarantee at the cost of wider intervals.
5. **CV+ (K-fold analogue).** Theorem 4 proves 1−2α − √(2/n) coverage uniformly in K, combining a Vovk-Wang p-value-averaging bound with a new V-statistic variance bound.
6. **Containment relation.** The cross-conformal prediction set of [[sources/vovk-2012-cross-conformal|Vovk (2015)]] is always contained in the CV+ interval, and the new √(2/n) term tightens that bound at large K.
7. **(ε, ν) stability theory (Theorem 5).** Inflated jackknife and jackknife+ regain ~1−α coverage under out-of-sample stability; (Theorem 6) the naive interval recovers under both in-sample and out-of-sample stability.

## Empirical Validation

Communities and Crime, BlogFeedback, MEPS-2016 datasets with Ridge / Random Forest / Neural Network base learners. Jackknife+ matches the (unstable) jackknife's interval width while preserving coverage where the jackknife collapses.

## Relation to Other Wiki Sources

- [[sources/vovk-2012-cross-conformal]] — the cross-conformal precursor whose K=n coverage bound is tightened here.
- [[sources/kim-2020-jackknife-plus-after-bootstrap]] — extends jackknife+ to ensemble learners via bootstrap, achieving J+ guarantees at the cost of a single ensemble fit.
- [[sources/tibshirani-2019-covariate-shift]] — companion paper from the same author group, addressing the covariate-shift extension.
- [[sources/barber-2023-beyond-exchangeability]] — same author group's extension to non-exchangeable data.
- [[sources/xu-2023-enbpi]] — EnbPI uses the J+aB idea but extends to time series.

## Questions Raised

- Can the K-fold CV+ coverage bound be sharpened beyond 1 − 2α − √(2/n)?
- Can the factor of 2 in the 1−2α bound be removed under intermediate stability assumptions weaker than full in-sample stability?
- How does CV+ behave under non-exchangeable data (distribution shift, time series)? Partially addressed by [[sources/barber-2023-beyond-exchangeability]].

## See Also

- [[concepts/jackknife-plus]]
- [[concepts/cross-conformal-prediction]]
- [[concepts/jackknife-plus-after-bootstrap]]
- [[entities/rina-foygel-barber]]

<!-- AUTHORED REGION END -->
