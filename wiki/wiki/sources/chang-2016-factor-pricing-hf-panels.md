---
title: Evaluating Factor Pricing Models Using High-Frequency Panels
page_id: sources/chang-2016-factor-pricing-hf-panels
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Yoosoon Chang
- Yongok Choi
- Hwagyun Kim
- Joon Y. Park
year: 2016
venue: Quantitative Economics
tags:
- factor-models
- fama-french
- panel-data
- stochastic-volatility
- asset-pricing-tests
sources: []
related:
- concepts/fama-french-factors
- concepts/panel-data-fixed-random-effects
- concepts/factor-models
- concepts/high-frequency-data
- concepts/realized-covariance
mind_map_priority: high
schema_version: 2
uuid: 7475642f-88ab-52c3-b1b7-f9dc62e3dd11
content_hash: sha256:7c844d5a8438bb5f743c36b84a8bb2e04c18b20ed928cea0656a9676fbb9f689
---

<!-- AUTHORED REGION START -->
# Evaluating Factor Pricing Models Using High-Frequency Panels

**Authors:** Yoosoon Chang, Yongok Choi, Hwagyun Kim, Joon Y. Park

**Year:** 2016 · **Venue:** Quantitative Economics 7, 889–933

**Institutions:** Indiana University; Korea Development Institute; Mays Business School, Texas A&M; Indiana University and Sungkyunkwan University

## Summary

An econometric argument with an asset-pricing payoff. Running [[concepts/fama-french-factors|Fama–French]] regressions on returns sampled at fixed calendar intervals gives, in the authors' words, misleading and inconsistent test results, because return volatilities are non-stationary and endogenous. Sampling on a volatility clock fixes the inference, and the standard factor models fare noticeably worse once it does.

## What It Does

The multifactor model is written in continuous time with a corresponding panel regression. The error is a martingale differential in two independent parts: a common component whose volatility is driven by the market but otherwise unrestricted, possibly with endogenous non-stationarity; and a cross-sectionally independent idiosyncratic component with asymptotically stationary volatility. The only substantive restriction is that non-stationary volatility comes exclusively from the market — only market risk is non-diversifiable over time.

The estimation device is the Dambis–Dubins–Schwarz theorem: a continuous martingale is a Brownian motion when read on a clock running inversely proportional to its quadratic variation, so sampling at **random** intervals set by that clock tames general martingale differentials. Realized variance at a higher frequency supplies the variance estimate. Asymptotics require the sampling interval to shrink and the horizon to grow, the interval small relative to the horizon. Jumps are located by the Lee–Mykland test and affected samples discarded.

## Findings

Data are daily returns from Kenneth French's library, July 1963 to December 2008: size and B/M decile portfolios, the 25 size-B/M portfolios, and 30 industry portfolios.

Fixed-time OLS fails to reject the two-factor models with even higher p-values than the CAPM on the same data — a contradiction the authors attribute to imprecise method. Under random sampling, market plus B/M is not rejected on B/M deciles (p = 11%), but market plus size fails on size deciles. The three-factor model is rejected on the 25 portfolios under both schemes, driven largely by the small-growth (1,1) portfolio.

Adding a consumer-goods industry factor (CMR) raises p-values throughout; market plus B/M plus CMR is not rejected at 14% on the deciles and shrinks the (1,1) pricing error, though it is still rejected on the 25 portfolios.

## Caveats

Despite the title, the empirical work uses daily observations over roughly 45 years. The authors say the theory admits intraday ultra-high frequencies but that these add more microstructure noise than signal over a long horizon. The jump pretest also distorts test size, which they ignore for simplicity.

## Open Questions

- Is CMR a genuine priced factor or a proxy for something the size factor misses?
- Would the conclusions change at intraday frequency with a noise-robust variance estimator?

## See Also

[[concepts/fama-french-factors|Fama–French Factors]] · [[concepts/panel-data-fixed-random-effects|Panel Data: Fixed and Random Effects]] · [[concepts/factor-models|Factor Models]] · [[concepts/high-frequency-data|High-Frequency Data]] · [[sources/aitsahalia-2020-hf-factor-models-regressions|Aït-Sahalia, Kalnina & Xiu (2020)]]

**Not yet written:** `dambis-dubins-schwarz-theorem`, `time-change-sampling`, `realized-variance`, `nonstationary-volatility`, `capital-asset-pricing-model`.

<!-- AUTHORED REGION END -->

