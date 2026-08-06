---
title: High-Frequency Factor Models and Regressions
page_id: sources/aitsahalia-2020-hf-factor-models-regressions
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Yacine Aït-Sahalia
- Ilze Kalnina
- Dacheng Xiu
year: 2020
venue: Journal of Econometrics
tags:
- high-frequency-data
- factor-models
- fama-french
- idiosyncratic-risk
- time-varying-betas
sources: []
related:
- concepts/fama-french-factors
- concepts/high-frequency-data
- concepts/factor-models
- concepts/market-microstructure-noise
- concepts/realized-covariance
mind_map_priority: high
schema_version: 2
uuid: 939c0dfe-0e8f-5e55-80c0-18fac0a706a0
content_hash: sha256:3c914f339ffc655d0aaf9abac801032da35592ff81ce7c9e56fdaa94bd3f25ca
---

<!-- AUTHORED REGION START -->
# High-Frequency Factor Models and Regressions

**Authors:** Yacine Aït-Sahalia, Ilze Kalnina, Dacheng Xiu

**Year:** 2020 · **Venue:** Journal of Econometrics 216, 86–105

**Institutions:** Princeton University; North Carolina State University; Booth School of Business, University of Chicago

## Summary

A nonparametric continuous-time regression model in which betas are allowed to vary freely over time, rather than being held piecewise constant. That freedom is what makes the framework usable on individual stocks instead of portfolios. The empirical half rebuilds the [[concepts/fama-french-factors|Fama–French]] factors at intraday frequency over two decades.

## What It Does

The dependent process `Y` is regressed on a `d`-dimensional covariate process `X`, with separate loadings for the continuous and jump parts of `X`. Both `X` and the residual `Z` are Itô semimartingales; jumps in returns and volatilities are allowed, as are continuous and jump leverage effects. The drift is absorbed into `Z` — over a month it is economically negligible and not identifiable over a fixed horizon.

Spot betas are identified by comparing the spot quadratic variation of `X` with its spot quadratic covariation with `Y`, estimated over moving windows and aggregated to integrated beta. Idiosyncratic volatility comes from the same decomposition. Idiosyncratic jumps are identified separately, from the assumption that `X` and `Z` do not jump together, so no windows or regressions are involved; the continuous and jump specifications do not contaminate each other.

Sampling frequency is chosen per stock per month from 5-min, 10-min, 30-min and daily, using the Hausman test of Aït-Sahalia and Xiu for absence of significant [[concepts/market-microstructure-noise|microstructure noise]] plus a zero-return count.

## Findings

All traded NYSE, AMEX and NASDAQ stocks, 1996–2017, averaging 5005 stocks, merging TAQ, CRSP and Compustat to build the five Fama–French factors and momentum at 5-minute frequency.

The selected frequency shifts upward over time, steepest after decimalisation in 2001. High-frequency betas track daily betas but are more stable and free of the large outliers that low-frequency estimates show around bad earnings announcements — those returns are classified as jumps and excluded from beta. For IBM, idiosyncratic risk averages 47.3% of total variance under the six-factor model, of which idiosyncratic jumps average 11.6%. Across the cross-section idiosyncratic jumps average about 10% of idiosyncratic risk, rising to about 20% for a quarter of firms, and slightly more under the CAPM.

Panel regressions on 117,557 stock-months with positive idiosyncratic jumps show earnings surprises raise idiosyncratic jumps, disappointments more than positive surprises.

## Open Questions

- High- and low-frequency beta estimands coincide only under extra assumptions. What is the economically relevant one?
- Many IBM jump spikes are overnight moves after earnings releases. How much of "intraday" idiosyncratic jump risk is really overnight?

## See Also

[[concepts/fama-french-factors|Fama–French Factors]] · [[concepts/high-frequency-data|High-Frequency Data]] · [[concepts/market-microstructure-noise|Market Microstructure Noise]] · [[sources/aitsahalia-2017-pca-hf-factor-model|Aït-Sahalia & Xiu (2017)]] · [[sources/chang-2016-factor-pricing-hf-panels|Chang et al. (2016)]]

**Not yet written:** `time-varying-beta`, `idiosyncratic-volatility`, `integrated-beta`, `ito-semimartingale`, `truncation-jump-estimation`.

<!-- AUTHORED REGION END -->

