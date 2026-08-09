---
title: Estimation of Common Factors for Microstructure Noise and Efficient Price in
  a High-Frequency Dual Factor Model
page_id: sources/li-2023-microstructure-noise-efficient-price
page_type: source
source_path: markdown_output/1-s2.0-S0304407623000131-main.md
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Yu-Ning Li
- Jia Chen
- Oliver Linton
year: 2023
venue: Journal of Econometrics
tags:
- high-frequency-data
- market-microstructure-noise
- factor-models
- pca
- non-stationarity
sources: []
related:
- concepts/market-microstructure-noise
- concepts/market-microstructure
- concepts/principal-components-analysis
- concepts/high-frequency-data
- concepts/cointegration
- concepts/factor-models
mind_map_priority: high
schema_version: 2
uuid: 20aac9cb-414d-5f3e-86d5-2ccb0bee7cd0
content_hash: sha256:d1e47dadc7da2632e00c5f7f27559802e178bec53ee8dfd9e80e0720716ebd13
---

<!-- AUTHORED REGION START -->
# Estimation of Common Factors for Microstructure Noise and Efficient Price in a High-Frequency Dual Factor Model

**Authors:** Yu-Ning Li, Jia Chen, Oliver Linton

**Year:** 2023 · **Venue:** Journal of Econometrics

**Institutions:** University of York; University of Cambridge

## Summary

Most high-frequency work treats [[concepts/market-microstructure-noise|microstructure noise]] as a nuisance to be removed. This paper treats it as an object with its own factor structure, and estimates the two structures — one for efficient prices, one for the noise — separately from the same observed returns.

## What It Does

The dual factor model is Bollerslev et al.'s (2019); the estimation is new. The method, Double Principal Component Analysis (DPCA), runs in two steps and adapts Bai and Ng's (2004) PANIC procedure to an infill setting.

Step one: a single [[concepts/principal-components-analysis|PCA]] on observed returns recovers all common factors and loadings, signal and noise together. Step two: a second PCA on the *cumulative* form of those factors separates them. The logic is a stationarity contrast — cumulated efficient-price components are non-stationary and dominate in magnitude, while cumulated noise components stay stationary. The alternative route (noise-robust covolatility matrix, noise covariance, then PCA on each) exists but the authors argue it loses efficiency.

Uniform consistency is proved as both the number of assets and the sampling frequency go to infinity. The framework deliberately allows a range of relative magnitudes between efficient price and noise, and between common and idiosyncratic noise, since noise can be small in liquid assets. Weak factors are permitted. The Epps effect is representable when idiosyncratic noise is elementwise larger than the common component.

## Findings

505 S&P 500 constituents, Thomson Reuters Eikon, 29 March to 30 June 2021, at 1-minute and 5-minute frequencies over 66 trading days. Missing observations are filled by carry-forward, carry-backward or linear interpolation.

Factor counts vary by day. At 1-minute frequency the mean total is 13.0, of which about 4.2 are noise factors under the 1% PANIC test. At 5-minute frequency the noise count collapses to about 0.9. Contemporaneous correlations between factor counts and nine risk variables are insignificant, but lagged ones appear — strongest is lag-1 SMB with the 1-minute efficient-price count at 0.329 (p = 0.007). Counts fall when VIX or high-low volatility spikes.

## Why It Matters

The empirical claim is modest but specific: there is co-movement in microstructure noise distinct from latent systematic risk factors. The authors suggest a noise-only mimicking portfolio as a hedging or mean-reversion vehicle, subject to costs.

## Open Questions

- The sample is one quarter of 2021. Does the noise factor count survive different volatility regimes?
- How much do the interpolation rules for missing data drive the estimated noise factors?

## See Also

[[concepts/market-microstructure-noise|Market Microstructure Noise]] · [[concepts/market-microstructure|Market Microstructure]] · [[concepts/cointegration|Cointegration]] · [[concepts/principal-components-analysis|Principal Components Analysis]] · [[sources/dai-2019-knowing-factors-or-loadings|Dai, Lu & Xiu (2019)]] · [[sources/pelger-2019-large-dimensional-hf-factor-model|Pelger (2019)]]

**Not yet written:** `epps-effect`, `efficient-price`, `panic-test`, `weak-factors`, `infill-asymptotics`.

<!-- AUTHORED REGION END -->

