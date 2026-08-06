---
title: Dynamic Factor Model
page_id: concepts/dynamic-factor-model
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- econometrics
- factor-models
- state-space-models
- yield-curve
- forecasting
sources:
- sources/omrane-2017-yield-curve-forecasting
- sources/bodilsen-2025-hf-dynamic-factor-portfolio
related:
- concepts/state-space-models
- concepts/kalman-filter
- concepts/nelson-siegel-model
- concepts/approximate-factor-models
mind_map_priority: medium
schema_version: 2
uuid: b938e847-8d8b-5370-936a-11eb3fd24302
content_hash: sha256:141b83ba372de49fdae4e5a694957f8e2b46a29331b2aa981f49e14feb3d5a91
---

<!-- AUTHORED REGION START -->
# Dynamic Factor Model

Many observed series driven by a small number of latent factors that themselves evolve over time. The cross-section is explained by factor loadings; the time dimension is explained by the factors' own dynamics.

As [[concepts/state-space-models|State-Space Models]] records, the pattern recurs across yield curve factors (level, slope, curvature), credit cycle indicators, and volatility factors.

## The Yield Curve Case

[[sources/omrane-2017-yield-curve-forecasting|Ben Omrane et al. (2017)]] is the wiki's worked example. The three [[concepts/nelson-siegel-model|Nelson-Siegel]] factors are treated as latent states:

- **State equation** — the factor vector follows a VAR(1) with intercept.
- **Measurement equation** — observed yields equal the Nelson-Siegel loading matrix times the factors, plus noise.

The loading matrix depends on a decay parameter lambda. Their innovation is estimating lambda from the data rather than fixing it, as earlier work did, and estimating everything jointly by maximum likelihood with the [[concepts/kalman-filter|Kalman filter]] extracting the factors.

The forecasting result is horizon-dependent: the dynamic factor approach dominates at 6 and 12 months but trails a random walk at one month. Their stated reason is an efficiency-robustness tradeoff — the Kalman filter adapts slowly to sudden economic breaks.

## The Large-Dimensional Case

[[sources/bodilsen-2025-hf-dynamic-factor-portfolio|Bodilsen (2025)]] applies the same idea to forecasting large [[concepts/realized-covariance|realized covariance]] matrices of S&P 500 constituents. Here the factors are **observable** ETF returns rather than latent states, and the modelling effort goes into the idiosyncratic covariance: a block structure inferred by [[concepts/hierarchical-clustering|hierarchical clustering]] on idiosyncratic correlations, which recovers the structure better than sector groupings. The model is OLS-estimable and scales linearly, and beats HEAVY, HAR-DRD and DCC-style benchmarks in out-of-sample [[concepts/minimum-variance-portfolio|minimum-variance portfolio]] selection.

Its theoretical footing is [[concepts/approximate-factor-models|Approximate Factor Models]] — the Chamberlain-Rothschild setting that permits weak cross-sectional dependence in the idiosyncratic errors rather than requiring a diagonal covariance.

## See Also

[[concepts/state-space-models|State-Space Models]] · [[concepts/kalman-filter|Kalman Filter]] · [[concepts/nelson-siegel-model|Nelson-Siegel Model]] · [[concepts/approximate-factor-models|Approximate Factor Models]] · [[concepts/factor-models|Factor Models]] · [[concepts/realized-covariance|Realized Covariance]] · [[concepts/har-model|HAR Model]]

[[concepts/yield-curve|Yield Curve]]

**Not yet written:** `concepts/vector-autoregression`

<!-- AUTHORED REGION END -->
