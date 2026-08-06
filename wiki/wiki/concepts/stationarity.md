---
title: Stationarity
page_id: concepts/stationarity
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- econometrics
- time-series
- unit-root
- cointegration
sources:
- sources/laumann-2021-kernel-tests-nonstationary
related:
- concepts/cointegration
- concepts/mean-reversion
- concepts/long-memory
- concepts/ornstein-uhlenbeck-process
mind_map_priority: medium
schema_version: 2
uuid: 663bd3f8-e14c-5faf-92dc-e0d0250b6d9d
content_hash: sha256:c5ee59a37ad3cb6cc6f316182c57f33d5860cdb661447384ab55fc875ca71f98
---

<!-- AUTHORED REGION START -->
# Stationarity

A series whose statistical properties do not depend on when you look at it. In the wiki it is used almost entirely as a precondition: methods assume it, and the interesting work is in what happens when it fails.

## The I(0) / I(1) Distinction

The working vocabulary comes from [[concepts/cointegration|Cointegration]]. A series is I(0) if it is stationary and I(1) if its first difference is. Cointegration is the case where the individual series are I(1) but some linear combination is I(0) — non-stationary components with a stationary relation between them.

The reason this matters is the **spurious regression** problem: regressing one I(1) series on another produces a high R², apparently significant t-statistics, and invalid inference. Testing for stationarity of the residual is what separates a real long-run relation from a coincidence. Where a genuine cointegrating vector exists, OLS is super-consistent — it converges at rate T rather than √T.

## Testing

The wiki names three routes, all appearing on [[concepts/cointegration|Cointegration]] and [[concepts/mean-reversion|Mean Reversion]]:

- **ADF (Augmented Dickey-Fuller)** — null of a unit root; rejection is evidence of stationarity or mean reversion. Applied to cointegration residuals it needs Engle-Granger critical values, not standard ADF ones.
- **Variance ratio** — ratio below 1 indicates mean reversion, 1 a random walk, above 1 trending.
- **Johansen and Phillips-Ouliaris** — multivariate and serial-correlation-robust alternatives for the cointegration case.

## Stationary Does Not Mean Memoryless

[[concepts/long-memory|Long Memory]] is defined *for stationary series*: autocorrelations decay so slowly that their sum diverges, while the series remains stationary. Anti-persistence, random walk and persistence are distinguished by the [[concepts/hurst-exponent|Hurst exponent]], not by stationarity. Separately, structural breaks can mimic long memory, so a rejection can mean either.

The [[concepts/ornstein-uhlenbeck-process|Ornstein-Uhlenbeck process]] is the canonical stationary continuous-time case, converging to N(mu, sigma²/(2·kappa)).

## When It Fails

[[sources/laumann-2021-kernel-tests-nonstationary|Laumann et al. (2021)]] give the clearest statement of the cost. Classical kernel hypothesis tests assume i.i.d. observations. Their simulations show that under AR(1) dependence the classical test has inflated Type I error, and under a nonstationary mean or time-varying variance it is simply invalid. Replacing i.i.d. with mixing conditions and bootstrapping in blocks restores validity — which most financial time series satisfy.

Note also that stationarity is not clock-independent: [[concepts/stylized-facts|Stylized Facts]] records that observed properties change with the sampling scheme.

## See Also

[[concepts/cointegration|Cointegration]] · [[concepts/mean-reversion|Mean Reversion]] · [[concepts/long-memory|Long Memory]] · [[concepts/hurst-exponent|Hurst Exponent]] · [[concepts/ornstein-uhlenbeck-process|Ornstein-Uhlenbeck Process]] · [[concepts/stylized-facts|Stylized Facts]] · [[concepts/heteroskedasticity|Heteroskedasticity]]

**Not yet written:** `concepts/unit-root`, `concepts/adf-test`, `concepts/nonstationarity`

<!-- AUTHORED REGION END -->
