---
title: Functional Data Analysis
page_id: concepts/functional-data-analysis
page_type: concept
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- statistics
- time-series
- curves
- econometrics
sources:
- sources/he-2024-functional-regression
related:
- concepts/state-space-models
- concepts/schwartz-smith-model
- concepts/nelson-siegel-model
- entities/gareth-peters
mind_map_priority: medium
schema_version: 2
uuid: 97b63f50-3b00-55cc-984c-57f58c83b22c
content_hash: sha256:e7af8b2ead422dec504987783f805f2babdf90bdb1176635fe6e34d1ae8d4c95
---

<!-- AUTHORED REGION START -->
# Functional Data Analysis

Functional Data Analysis (FDA) treats entire curves, surfaces, or other functions as single observations, rather than reducing them to summary statistics.

## Core Concept

Traditional approach: Observe $y_1, y_2, \ldots, y_n$ (scalars)

FDA approach: Observe $y_1(t), y_2(t), \ldots, y_n(t)$ (functions)

Each observation is a function defined over a continuum (time, space, wavelength, etc.).

## Key Techniques

### Basis Expansion
Represent functions as linear combinations:
$$y_i(t) = \sum_{k=1}^{K} c_{ik} \phi_k(t)$$

Common bases: Fourier, B-splines, wavelets, functional principal components.

### Functional Principal Component Analysis
Decompose functional variance:
$$y_i(t) = \bar{y}(t) + \sum_{k=1}^{\infty} \xi_{ik} \phi_k(t)$$

Where $\phi_k$ are eigenfunctions of the covariance operator.

### Functional Regression
**Scalar-on-function**: $Y = \alpha + \int \beta(t) X(t) dt + \epsilon$

**Function-on-function**: $Y(s) = \alpha(s) + \int \beta(s,t) X(t) dt + \epsilon(s)$

## Applications in Finance

| Application | Functional Object |
|-------------|-------------------|
| Yield curves | Interest rates as function of maturity |
| Volatility smiles | IV as function of strike/moneyness |
| Futures curves | Prices as function of contract month |
| Intraday returns | Returns as function of time-of-day |

## He et al. (2024) Application

Function-on-function regression linking:
- **Response**: Bond yield curves (function of maturity)
- **Predictors**: Commodity futures curves (function of contract month)
- **Method**: State-space representation with Kalman filtering

## See Also

- [[concepts/state-space-models|State-Space Models]]
- [[concepts/schwartz-smith-model|Schwartz-Smith Model]]
- [[concepts/nelson-siegel-model|Nelson-Siegel Model]]
- [[sources/he-2024-functional-regression|Multi-Factor Function-on-Function Regression (2024)]]

<!-- AUTHORED REGION END -->
