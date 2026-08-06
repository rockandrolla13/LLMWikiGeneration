---
title: Vasicek Model
page_id: concepts/vasicek-model
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- interest-rates
- stochastic-processes
- mean-reversion
sources: []
related:
- concepts/ornstein-uhlenbeck-process
- concepts/mean-reversion
mind_map_priority: low
schema_version: 2
uuid: 0a809e54-239f-5dbc-b0eb-8f7a797ce084
content_hash: sha256:25357ce46ed3fb3111d30321ffb9a39ad4d87802184f55b769c11e9007f98b0b
---

<!-- AUTHORED REGION START -->
# Vasicek Model

A short-rate model (Vasicek, 1977) in which the instantaneous interest rate follows a mean-reverting diffusion:

```
dr_t = kappa*(theta - r_t)*dt + sigma*dW_t
```

kappa is the speed of reversion, theta the long-run level, sigma the volatility.

## What This Is

It is an [[concepts/ornstein-uhlenbeck-process|Ornstein-Uhlenbeck process]] applied to the short rate. The wiki records exactly three properties: it is analytically tractable, giving closed-form bond prices; it permits negative rates; and it is the leading interest-rate application of the O-U process.

Everything else follows from the O-U page. The rate is stationary with limiting distribution N(theta, sigma²/(2·kappa)); autocorrelation decays as exp(−kappa·h); the half-life of a deviation is ln(2)/kappa; and exact discretization gives an AR(1) with phi = exp(−kappa·Delta), which is why the model can be estimated by OLS, maximum likelihood on the exact transition density, GMM on moments, or a [[concepts/kalman-filter|Kalman filter]] when the rate is treated as latent.

The O-U limitations carry over too: Gaussian increments with no jumps, constant volatility, and linear mean reversion.

## Thinness Note

This page is short because the wiki is thin here. No source page in the wiki takes the Vasicek model as its subject — the entire treatment above comes from a single section of [[concepts/ornstein-uhlenbeck-process|Ornstein-Uhlenbeck Process]]. In particular the wiki says nothing about the closed-form bond price formula, calibration to an observed curve, or the CIR and Hull-White successors that address the negative-rate and fitting problems. Do not treat this page as coverage of the short-rate literature.

Note that "Vasicek" also appears in the wiki as [[entities/borek-vasicek|Borek Vasicek]], a co-author on the crisis early-warning papers. Unrelated.

## See Also

[[concepts/ornstein-uhlenbeck-process|Ornstein-Uhlenbeck Process]] · [[concepts/mean-reversion|Mean Reversion]] · [[concepts/kalman-filter|Kalman Filter]] · [[concepts/nelson-siegel-model|Nelson-Siegel Model]]

[[concepts/yield-curve|Yield Curve]]

**Not yet written:** `concepts/short-rate-models`, `concepts/affine-term-structure`

<!-- AUTHORED REGION END -->
