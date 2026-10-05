---
content_hash: sha256:e658b5a3a0950bfd284de1e9d08ea95ffb07248c25ff926c0ffb7d5b86c49e05
created: 2026-08-06 00:00:00+00:00
mind_map_priority: medium
page_id: concepts/error-correction-model
page_type: concept
related:
- concepts/cointegration
- concepts/vector-error-correction-model
- concepts/mean-reversion
- concepts/half-life-of-adjustment
revision_id: 2
schema_version: 2
sources:
- sources/duasa-2010-predicting-crisis-recovery
- sources/carr-2011-american-puts-credit-protection
tags:
- econometrics
- time-series
- cointegration
- mean-reversion
title: Error Correction Model
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: b1f0b92c-f13d-52ae-ad3e-6fffd86aca9d
---

<!-- AUTHORED REGION START -->
# Error Correction Model

A regression in differences that also carries the previous period's deviation from a long-run equilibrium. Short-run movements are modelled directly; the equilibrium error pulls the system back.

## Where It Comes From

The ECM is not an ad hoc specification — it is implied by [[concepts/cointegration|cointegration]] via the Granger Representation Theorem. If Y and X are each I(1) and the combination Y − beta·X is I(0), then the pair admits a representation of the form

```
Delta(Y_t) = alpha_y * (Y_{t-1} - beta*X_{t-1}) + lagged differences + e_yt
Delta(X_t) = alpha_x * (Y_{t-1} - beta*X_{t-1}) + lagged differences + e_xt
```

The term in brackets is last period's equilibrium error. The coefficients alpha_y and alpha_x are the **adjustment coefficients**: they measure how fast each series moves back toward equilibrium. That speed converts to a [[concepts/half-life-of-adjustment|half-life of adjustment]].

Because the differenced variables are stationary and the error-correction term is stationary by construction, the regression avoids the spurious-regression trap that catches naive levels regressions on I(1) data.

## Multivariate Form

The n-variable version is the [[concepts/vector-error-correction-model|Vector Error Correction Model]] — a cointegrated VAR in which the short-run dynamics of differenced I(1) variables are tied to the long-run relation through error-correction terms. It appears in the wiki through [[sources/duasa-2010-predicting-crisis-recovery|Duasa (2010)]] on crisis recovery periods.

## Why It Shows Up in Trading

The equilibrium error is the tradable object. In [[concepts/pairs-trading|pairs trading]] the spread Y − beta·X is exactly the error-correction term, and the adjustment coefficients are what make it [[concepts/mean-reversion|mean-reverting]] rather than a random walk. See [[concepts/statistical-arbitrage|Statistical Arbitrage]].

## See Also

[[concepts/cointegration|Cointegration]] · [[concepts/vector-error-correction-model|Vector Error Correction Model]] · [[concepts/half-life-of-adjustment|Half-Life of Adjustment]] · [[concepts/mean-reversion|Mean Reversion]] · [[concepts/pairs-trading|Pairs Trading]] · [[concepts/statistical-arbitrage|Statistical Arbitrage]] · [[concepts/structural-vector-autoregression|Structural VAR]]

**Not yet written:** `concepts/vector-autoregression`, `concepts/unit-root`

## Sources

- [[sources/carr-2011-american-puts-credit-protection|A Simple Robust Link Between American Puts and Credit Protection]]
<!-- AUTHORED REGION END -->