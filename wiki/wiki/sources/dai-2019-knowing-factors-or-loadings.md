---
title: Knowing Factors or Factor Loadings, or Neither? Evaluating Estimators of Large
  Covariance Matrices with Noisy and Asynchronous Data
page_id: sources/dai-2019-knowing-factors-or-loadings
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Chaoxing Dai
- Kun Lu
- Dacheng Xiu
year: 2019
venue: Journal of Econometrics
tags:
- high-frequency-data
- covariance-estimation
- market-microstructure-noise
- factor-models
- portfolio-allocation
sources: []
related:
- concepts/market-microstructure-noise
- concepts/factor-models
- concepts/principal-components-analysis
- concepts/high-frequency-data
- concepts/realized-covariance
- concepts/minimum-variance-portfolio
mind_map_priority: high
schema_version: 2
uuid: ae941929-4231-52ec-b604-cf4e0fcf693c
content_hash: sha256:963d5a7b79e4c0be58dd026bc9b511727445ef246a47729d5ef5f1c01504d0c0
---

<!-- AUTHORED REGION START -->
# Knowing Factors or Factor Loadings, or Neither?

**Authors:** Chaoxing Dai, Kun Lu, Dacheng Xiu

**Year:** 2019 · **Venue:** Journal of Econometrics 208, 43–79

**Institutions:** Booth School of Business, University of Chicago; Department of ORFE, Princeton University

## Summary

A horse race. To get a large covariance matrix from intraday transaction prices you must decide what you claim to know — factors, loadings, or neither — and how you handle noise and asynchronous trading. The paper works out convergence rates for each choice, then tests all combinations on out-of-sample portfolio risk.

## What It Does

The factor structure gives a low-rank plus sparse covariance matrix, keeping the estimator well-conditioned and its inverse usable. Three ways to recover the low-rank part:

- **TSR** (time-series regression) — factors known, estimate loadings; portfolios and ETFs proxy for factors.
- **CSR** (cross-sectional regression) — loadings known, estimate factors; stock characteristics proxy for exposures. The paper identifies this as MSCI Barra's method for low-frequency data.
- **PCA** — neither known.

Microstructure problems are handled by the pre-averaging estimator of Jacod et al. (2009) at refresh times. The sparse component uses one of several thresholding schemes, including a "location" scheme that keeps within-GICS-group entries. Consistency comes from large deviation theory for martingales, under joint in-fill and increasing-dimension asymptotics.

The rate comparison is the theoretical payload: TSR converges as the sample size grows whether the dimension is fixed or increasing, whereas **CSR and PCA need the dimension to grow as well** — the "blessings of dimensionality".

## Findings

TAQ data, January 2004 to December 2013, for Dow Jones 30, S&P 100 and S&P 500 constituents (42, 152 and 735 stocks over the period). Refresh-time sampling yields on average 284 observations per day for the S&P 500 — roughly every 90 seconds — against 905 for S&P 100 and 2105 for Dow 30.

Across almost all 30 combinations, pre-averaging beats subsampling at a fixed 15-minute frequency. TSR or PCA plus location thresholding dominates for the S&P 500 and S&P 100; TSR alone dominates for the Dow 30. CSR performs considerably worse nearly everywhere, which the authors attribute to misspecified exposures rather than to the method itself.

## Why It Matters

A practical ranking, not just a rate theorem: knowing the loadings is the weakest of the three positions to be in.

## Open Questions

- Would a better characteristic set rescue CSR, as the authors suggest?
- Jumps are deliberately left in the intraday returns because they "do not seem to matter" here. Does that hold for other universes?

## See Also

[[concepts/market-microstructure-noise|Market Microstructure Noise]] · [[concepts/factor-models|Factor Models]] · [[concepts/principal-components-analysis|Principal Components Analysis]] · [[concepts/minimum-variance-portfolio|Minimum Variance Portfolio]] · [[sources/aitsahalia-2017-pca-hf-factor-model|Aït-Sahalia & Xiu (2017)]] · [[sources/li-2023-microstructure-noise-efficient-price|Li, Chen & Linton (2023)]]

**Not yet written:** `pre-averaging-estimator`, `refresh-time-sampling`, `low-rank-plus-sparse-covariance`, `thresholding-estimators`, `asynchronous-trading`.

<!-- AUTHORED REGION END -->

