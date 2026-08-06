---
title: Time-Varying Regression
page_id: concepts/time-varying-regression
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- econometrics
- adaptive-estimation
- kalman-filter
- statistical-arbitrage
sources:
- sources/montana-2009-flexible-least-squares
- sources/triantafyllopoulos-2011-mean-reverting-spreads
related:
- concepts/flexible-least-squares
- concepts/kalman-filter
- concepts/state-space-models
- concepts/statistical-arbitrage
mind_map_priority: medium
schema_version: 2
uuid: ee699079-3771-5248-a02d-676c3bfc67d5
content_hash: sha256:292aed922e88f1ef49acc80c3b4da1c1c65ee5f0b228b0aa66995965a21c13f7
---

<!-- AUTHORED REGION START -->
# Time-Varying Regression

A regression whose coefficients are allowed to change over time rather than being fixed across the sample. The modelling question is not whether to allow change but how much: entirely free coefficients are just a sequence of unrelated fits, entirely fixed ones are OLS.

## Two Framings of the Same Thing

The wiki's main result here is that the two obvious ways to write the problem are the same problem.

**Penalized optimization.** [[concepts/flexible-least-squares|Flexible Least Squares]] minimizes squared residuals plus mu times the squared period-to-period change in the coefficient vector. At mu = 0 the coefficients jump freely; as mu → ∞ they are constant and FLS reduces to pooled OLS.

**State-space.** Write the coefficients as a random walk, beta_t = beta_{t−1} + eta_t, observed through y_t = x_t'·beta_t + epsilon_t, and run a [[concepts/kalman-filter|Kalman filter]].

[[sources/montana-2009-flexible-least-squares|Montana, Triantafyllopoulos & Tsagaris (2009)]] prove these are algebraically equivalent, with mu equal to the ratio R/Q of observation noise variance to state noise variance. The smoothness penalty and the noise ratio are the same knob.

The equivalence is practically useful, not just tidy. Original FLS needs a backward pass — the recursion for beta_t references beta_{t+1} — which makes it offline. The Kalman recursions run forward, so the same estimates are available on-line, and they are numerically more stable. They also come with confidence intervals and a route to incorporate prior information through initial conditions.

## The Trading Application

Montana et al. apply it to [[concepts/statistical-arbitrage|statistical arbitrage]]: the S&P 500 futures index as target, sector ETFs as predictors, time-varying betas defining a synthetic tracking portfolio. The residual is the mispricing, and trades are taken when it is extreme. Time-varying coefficients are what let the synthetic portfolio follow regime changes in factor exposures, which they report improves on static OLS.

[[sources/triantafyllopoulos-2011-mean-reverting-spreads|Triantafyllopoulos & Montana (2011)]] push the same idea into the spread model itself, letting the mean-reversion parameters vary and estimating them by Bayesian on-line methods — which additionally makes it possible to detect when mean reversion is breaking down.

## Choosing the Smoothness

Three routes: cross-validation on out-of-sample prediction error (expensive), maximum likelihood on the state-space form, or domain judgement about how fast the relationship should be allowed to move.

## See Also

[[concepts/flexible-least-squares|Flexible Least Squares]] · [[concepts/kalman-filter|Kalman Filter]] · [[concepts/state-space-models|State-Space Models]] · [[concepts/statistical-arbitrage|Statistical Arbitrage]] · [[concepts/mean-reversion|Mean Reversion]] · [[entities/giovanni-montana|Giovanni Montana]] · [[entities/kostas-triantafyllopoulos|Kostas Triantafyllopoulos]]

<!-- AUTHORED REGION END -->
