---
title: Conformalized Quantile Regression
page_id: concepts/conformalized-quantile-regression
page_type: concept
revision_id: 1
created: 2026-04-26T12:00:00Z
updated: 2026-04-26T12:00:00Z
tags: [conformal-prediction, quantile-regression, prediction-intervals, uncertainty-quantification]
sources: [sources/zaffran-2023-conformal-missing]
related: [concepts/conformal-prediction, concepts/prediction-intervals, concepts/coverage-guarantee, entities/yaniv-romano]
mind_map_priority: high
---

# Conformalized Quantile Regression (CQR)

**Conformalized Quantile Regression (CQR)** combines quantile regression with [[concepts/conformal-prediction|conformal prediction]] to produce prediction intervals that are both adaptive to local data characteristics and satisfy marginal coverage guarantees.

## Motivation

Standard conformal prediction produces intervals of **constant width** for all predictions, which is inefficient when:
- Some regions have higher uncertainty than others
- The conditional distribution of Y|X is heteroskedastic

CQR addresses this by using quantile regression as the base model, allowing interval width to adapt while maintaining coverage guarantees.

## Method

### Step 1: Train Quantile Regressors

On the proper training set Tr, fit two quantile regressors:
- q̂_low(x): estimates the α/2 quantile of Y|X=x
- q̂_upp(x): estimates the 1-α/2 quantile of Y|X=x

### Step 2: Compute Conformity Scores

On the calibration set Cal, compute scores measuring how well the quantile estimates cover each point:

s(x, y) = max(q̂_low(x) - y, y - q̂_upp(x))

Positive scores indicate the true y falls outside the initial interval.

### Step 3: Compute Correction Term

Calculate the (1-α̃)-quantile of calibration scores:

Q̂_{1-α̃}(S_Cal) where α̃ = ⌈(n+1)(1-α)⌉/n

### Step 4: Form Prediction Intervals

For a new test point x:

Ĉ_α(x) = [q̂_low(x) - Q̂_{1-α̃}(S_Cal), q̂_upp(x) + Q̂_{1-α̃}(S_Cal)]

## Properties

### Marginal Coverage Guarantee

Under exchangeability:

P(Y_{n+1} ∈ Ĉ_α(X_{n+1})) ≥ 1 - α

### Adaptivity

Unlike standard CP, CQR intervals vary in width:
- **Narrow** where model is confident (q̂_low and q̂_upp close)
- **Wide** where model is uncertain (q̂_low and q̂_upp far apart)

The correction term Q̂ uniformly adjusts all intervals to ensure coverage.

### Efficiency

CQR typically produces shorter intervals than constant-width CP methods, especially for heteroskedastic data.

## Relationship to Quantile Regression

### Standard Quantile Regression

Fits model by minimizing pinball loss:

ℓ_β(y, ŷ) = ρ_β(y - ŷ) where ρ_β(u) = β|u|1_{u≥0} + (1-β)|u|1_{u≤0}

No coverage guarantee in finite samples.

### CQR Enhancement

Adds conformal calibration step to ensure coverage:
1. Quantile regression provides adaptivity
2. Conformal correction provides validity

## Application with Missing Data

[[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]] showed:

1. **CQR maintains marginal validity** on imputed data
2. **CQR fails mask-conditional validity (MCV)** without modification
3. **CQR-MDA** (Missing Data Augmentation) achieves MCV

### Recommendations for Missing Data

- Concatenate mask M to features X
- Use CQR-MDA-Exact or CQR-MDA-Nested
- QR handles induced heteroskedasticity better than mean regression

## Implementation Details

### Quantile Regression Models

Common choices:
- **Linear quantile regression**: Fast, interpretable
- **Quantile random forests**: Handles nonlinearity
- **Neural network quantile regression**: For complex patterns

### Training Objective

For a neural network, minimize:

L = (1/n) ∑_i [ℓ_{α/2}(y_i, q̂_low(x_i)) + ℓ_{1-α/2}(y_i, q̂_upp(x_i))]

### Crossing Quantiles

If q̂_low(x) > q̂_upp(x) for some x, intervals can be invalid. Solutions:
- Constrained optimization
- Post-hoc sorting
- Non-crossing quantile regression architectures

## Comparison with Alternatives

| Method | Adaptivity | Coverage | Efficiency |
|--------|------------|----------|------------|
| Mean CP | No | Yes | Low |
| CQR | Yes | Yes | High |
| Quantile Regression | Yes | No | Medium |
| Bayesian Intervals | Yes | Approx | Medium |

## Key References

- Romano et al. (2019) - Original CQR paper
- [[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]] - CQR with missing values
- Sesia & Candès (2020) - Comparison of conformal QR methods

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/prediction-intervals|Prediction Intervals]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/mask-conditional-validity|Mask-Conditional Validity]]
- [[entities/yaniv-romano|Yaniv Romano]]
