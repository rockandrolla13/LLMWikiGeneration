---
title: Nelson-Siegel Model
page_id: concepts/nelson-siegel-model
page_type: concept
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- yield-curves
- fixed-income
- econometrics
- term-structure
sources:
- sources/technical-2025-bond-similarity
related:
- concepts/credit-spread-curve
- concepts/z-spread
- concepts/state-space-models
mind_map_priority: medium
schema_version: 2
uuid: 602bad2d-4f43-5b11-8554-a8c0a24b8f12
content_hash: sha256:a9692945a3235a0c7bf0ac87a406c9ce05cb88fada88b4cecb5aeed6cad208d4
---

<!-- AUTHORED REGION START -->
# Nelson-Siegel Model

The Nelson-Siegel model is a parsimonious parametric model for fitting yield curves using just three factors that correspond to level, slope, and curvature.

## Specification

The yield at maturity $\tau$ is:

$$y(\tau) = \beta_0 + \beta_1 \left(\frac{1 - e^{-\lambda\tau}}{\lambda\tau}\right) + \beta_2 \left(\frac{1 - e^{-\lambda\tau}}{\lambda\tau} - e^{-\lambda\tau}\right)$$

Where:
- $\beta_0$ = Long-term level (asymptote)
- $\beta_1$ = Short-term component (slope)
- $\beta_2$ = Medium-term component (curvature)
- $\lambda$ = Decay parameter (controls hump location)

## Factor Interpretation

| Factor | Interpretation | Typical Range |
|--------|----------------|---------------|
| $\beta_0$ | Long-run yield level | 3-6% |
| $\beta_1$ | Yield curve slope | -2 to +2% |
| $\beta_2$ | Curvature (hump/trough) | -2 to +2% |

## Extensions

### Svensson Extension
Adds a fourth factor for better fit at longer maturities:
$$+ \beta_3 \left(\frac{1 - e^{-\lambda_2\tau}}{\lambda_2\tau} - e^{-\lambda_2\tau}\right)$$

### Dynamic Nelson-Siegel
Treats $\beta_t$ as time-varying state variables:
- Enables forecasting via state-space models
- Captures yield curve dynamics

## Applications

- Central bank curve fitting (ECB, Fed)
- Bond pricing and valuation
- Interest rate risk management
- Yield curve forecasting

## See Also

- [[concepts/credit-spread-curve|Credit Spread Curve]]
- [[concepts/state-space-models|State-Space Models]]
- [[sources/technical-2025-bond-similarity|Bond Similarity Framework (2025)]]

<!-- AUTHORED REGION END -->
