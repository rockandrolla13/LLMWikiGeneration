---
title: Using Principal Component Analysis to Estimate a High Dimensional Factor Model
  with High-Frequency Data
page_id: sources/aitsahalia-2017-pca-hf-factor-model
page_type: source
source_path: markdown_output/1-s2.0-S0304407617301677-main.md
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Yacine Aït-Sahalia
- Dacheng Xiu
year: 2017
venue: Journal of Econometrics
tags:
- high-frequency-data
- factor-models
- pca
- covariance-estimation
- portfolio-allocation
sources: []
related:
- concepts/principal-components-analysis
- concepts/approximate-factor-models
- concepts/factor-models
- concepts/high-frequency-data
- concepts/realized-covariance
- concepts/minimum-variance-portfolio
mind_map_priority: high
schema_version: 2
uuid: 2b7b7ca2-346b-5676-ba1f-8adbff04b09b
content_hash: sha256:b12b1626dd52a533c636188ec8ba9a5beb3cdecbe5d0a27d0126332ab2e2a29a
---

<!-- AUTHORED REGION START -->
# Using Principal Component Analysis to Estimate a High Dimensional Factor Model with High-Frequency Data

**Authors:** Yacine Aït-Sahalia, Dacheng Xiu

**Year:** 2017 · **Venue:** Journal of Econometrics 201, 384–399

**Institutions:** Princeton University and NBER; Booth School of Business, University of Chicago

## Summary

A theory paper with an empirical illustration. It builds a [[concepts/principal-components-analysis|PCA]]-based estimator of a large covariance matrix from intraday returns, plus an estimator of the number of latent factors, and proves both consistent under asymptotics where the sampling interval shrinks *and* the cross-section grows.

## What It Does

The model is continuous-time and semiparametric: observed log-prices follow `Y_t = βX_t + Z_t`, where the `r` latent factors `X` and the idiosyncratic part `Z` are continuous Itô semimartingales, the loading matrix `β` is constant, and quadratic covariation between factors and residuals is zero. Jumps are excluded and left to future work. The horizon `T` is fixed (one month empirically), `r` is finite but unknown, the cross-section `d` grows as the sampling interval goes to zero.

The number of factors is estimated by minimising a penalised eigenvalue criterion — the Bai and Ng (2002) idea, but stated on individual eigenvalues rather than sums, which the authors argue is easier to use and simpler to prove. Consistency is established without random matrix theory, which the paper says is unavailable for semimartingales. The residual matrix is assumed sparse; the covariance estimator is positive-definite and well-conditioned by construction.

## Findings

S&P 500 constituents from TAQ, January 2004 to December 2012, sampled every 15 minutes, over 491 names per month. Three to five factors are identified in most subperiods. After removing as few as four latent factors, the residual correlation matrix shows a clear block-diagonal pattern once stocks are sorted by GICS code — the low-rank-plus-sparse structure the theory assumes. Latent factors explain slightly more in-sample variation than the same number of observable factors, and the R² are higher than comparable daily-data results, which the paper attributes to a better intraday signal-to-noise ratio. Out-of-sample, PCA with sector-blocked residuals beats the sample covariance matrix in constrained portfolio allocation; the equal-weight benchmark has 17.9% annualised risk.

## Caveats

The constant-`β` assumption and the exclusion of jumps are acknowledged restrictions. Portfolio risk explodes with zero factors and rises again with tens of factors, so `r` behaves as a tuning parameter. Survivorship bias is present but bounded at one month ahead.

## Open Questions

- How much of the out-of-sample gain survives once jumps are added to the model?
- The penalty tuning constants are conceded to be arbitrary. What chooses them in practice beyond the scree plot?

## See Also

[[concepts/principal-components-analysis|Principal Components Analysis]] · [[concepts/approximate-factor-models|Approximate Factor Models]] · [[concepts/high-frequency-data|High-Frequency Data]] · [[concepts/realized-covariance|Realized Covariance]] · [[concepts/minimum-variance-portfolio|Minimum Variance Portfolio]] · [[sources/pelger-2019-large-dimensional-hf-factor-model|Pelger (2019)]] · [[sources/dai-2019-knowing-factors-or-loadings|Dai, Lu & Xiu (2019)]]

**Not yet written:** `low-rank-plus-sparse-covariance`, `ito-semimartingale`, `infill-asymptotics`, `number-of-factors-estimation`, `thresholding-estimators`.

<!-- AUTHORED REGION END -->

