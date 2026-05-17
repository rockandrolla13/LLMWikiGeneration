---
title: "Conformal Prediction with Missing Values"
page_id: sources/zaffran-2023-conformal-missing
page_type: source
revision_id: 1
created: 2026-04-26T12:00:00Z
updated: 2026-04-26T12:00:00Z
tags: [conformal-prediction, missing-data, imputation, quantile-regression, heteroskedasticity, mask-conditional-validity]
authors: [Margaux Zaffran, Aymeric Dieuleveut, Julie Josse, Yaniv Romano]
venue: NeurIPS 2023
year: 2023
sources: []
related: [concepts/conformal-prediction, concepts/missing-data-imputation, concepts/conformalized-quantile-regression, concepts/coverage-guarantee, concepts/heteroskedasticity, entities/margaux-zaffran]
mind_map_priority: high
---

# Conformal Prediction with Missing Values

**Zaffran, M., Dieuleveut, A., Josse, J., & Romano, Y. (2023).** Conformal Prediction with Missing Values. *NeurIPS 2023*.

## Summary

This paper studies [[concepts/conformal-prediction|conformal prediction]] when covariates have missing values - a ubiquitous real-world challenge previously unexplored in uncertainty quantification. The key insight is that **missing values introduce heteroskedasticity**: prediction uncertainty depends strongly on which features are observed.

The main contributions are:
1. Proving that marginal coverage holds for impute-then-predict approaches
2. Showing that standard methods fail to achieve **mask-conditional validity (MCV)**
3. Introducing **CP-MDA** (Missing Data Augmentation) framework that achieves MCV

## Problem Setting

### Missing Values Notation

- Data: (X, M, Y) where X ∈ ℝᵈ are features, M ∈ {0,1}ᵈ is the missing mask, Y ∈ ℝ is the target
- Mⱼ = 0 when Xⱼ observed, Mⱼ = 1 when Xⱼ missing (NA)
- X_obs(m): observed components given mask m
- X_mis(m): missing components given mask m

### Missingness Mechanisms (Rubin, 1976)

1. **MCAR** (Missing Completely At Random): P(M=m|X) = P(M=m)
2. **MAR** (Missing At Random): P(M=m|X) = P(M=m|X_obs(m))
3. **MNAR** (Missing Not At Random): Otherwise

## Key Theoretical Results

### Proposition 3.3: Marginal Validity of Impute-then-Predict

Under exchangeability (A1) and symmetric imputation (A2), impute-then-predict+conformalization is marginally valid:

P(Y ∈ Ĉ_α(X,M)) ≥ 1 - α

This holds for **any** imputation method and **any** missingness mechanism (MCAR, MAR, or MNAR).

### Proposition 4.2: Induced Heteroskedasticity

Under a Gaussian linear model Y = β^T X + ε with X|M=m ~ N(μᵐ, Σᵐ):

The oracle interval length depends on the mask:

L*_α(m) = 2q_{1-α/2}^{N(0,1)} √(β_mis(m)^T Σᵐ_{mis|obs} β_mis(m) + σ²_ε)

**Key insight**: Even with homoskedastic noise, missing values create heteroskedastic predictions. Uncertainty increases when predictive variables are missing.

### Definition 5.2: Mask-Conditional Validity (MCV)

A method is MCV if for **any** mask m ∈ M:

P(Y ∈ Ĉ_α(X,M) | M=m) ≥ 1 - α

This is stronger than marginal validity and ensures equitable coverage across all missing patterns.

## CP-MDA Framework

### Algorithm 1: CP-MDA-Exact

1. Apply test point's mask to calibration set
2. Keep only calibration points with **exactly** the same missing pattern
3. Compute correction term using these matched points
4. Standard conformal prediction with pattern-specific calibration

**Theorem 5.3**: Under MCAR + exchangeability, CP-MDA-Exact is exactly MCV.

### Algorithm 2: CP-MDA-Nested

1. Apply test point's mask to calibration set
2. Keep **all** calibration points (they now have at least same missing values)
3. For each calibration point, predict on test point with that point's augmented mask
4. Aggregate predictions using quantiles

**Theorem 5.3**: Under MCAR + stochastic domination assumption (A4), CP-MDA-Nested is MCV.

**Advantage**: Avoids discarding calibration points in high dimensions where exact pattern matching is rare.

### Assumption A4: Stochastic Domination of Quantiles

If m̊ ⊂ m̆ (m̆ has more missing values), then for any δ ∈ [0, 0.5]:

q^{Y|X_obs(m̊),M=m̊}_δ ≤ q^{Y|X_obs(m̆),M=m̆}_δ ≤ q^{Y|X_obs(m̆),M=m̆}_{1-δ} ≤ q^{Y|X_obs(m̊),M=m̊}_{1-δ}

Intuition: More missing values → wider conditional distribution.

## Asymptotic Results

### Proposition 6.1: Bayes Consistency of Quantile Regression

For almost all imputation functions Φ ∈ F^I_∞:
- g*_{ℓβ,Φ} ∘ Φ is ℓ_β-Bayes-optimal for pinball loss
- Any universally consistent QR algorithm on imputed data achieves Bayes consistency

### Corollary 6.2: Asymptotic Conditional Coverage

A universally consistent quantile regressor trained on imputed data yields **asymptotic conditional coverage** for any missingness mechanism.

## Empirical Results

### Synthetic Gaussian Linear Data (d=10)

| Method | Lowest Mask Coverage | Highest Mask Coverage |
|--------|---------------------|----------------------|
| QR | Far below 90% | Above 90% |
| CQR | Below 90% | Near 90% |
| **CQR-MDA-Exact** | ~90% | ~90% |
| **CQR-MDA-Nested** | ≥90% | >90% (conservative) |

### Semi-Synthetic Benchmarks (MEPS, Bio, Concrete, Bike)

- CQR: marginally valid but not MCV (lowest mask coverage far below target)
- CQR-MDA-Exact: exactly MCV
- CQR-MDA-Nested: MCV but slightly conservative

### TraumaBase Medical Data

Predicting platelet levels in trauma patients (7 features, 7% missing overall):
- CQR-MDA improves both coverage and efficiency (smaller intervals)
- Critical for medical applications where missing patterns correlate with patient characteristics

## Design Choices

1. **Use quantile regression**: Handles heteroskedasticity induced by missing values
2. **Concatenate mask to features**: Allows model to adapt interval length to missing pattern
3. **Missing data augmentation**: Ensures calibration accounts for test point's pattern

## Practical Implications

- **Equity**: Patients with missing data should not receive prediction intervals less likely to cover true values
- **Medical applications**: Missing patterns often correlate with hospital procedures, patient conditions
- **High-dimensional data**: CP-MDA-Nested preferred over Exact when exact pattern matching is rare

## Code Availability

Available on GitHub (link in paper).

## Key Concepts

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/conformalized-quantile-regression|Conformalized Quantile Regression]]
- [[concepts/missing-data-imputation|Missing Data Imputation]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/heteroskedasticity|Heteroskedasticity]]
- [[concepts/exchangeability|Exchangeability]]
- [[concepts/mask-conditional-validity|Mask-Conditional Validity]]

## Related Entities

- [[entities/margaux-zaffran|Margaux Zaffran]] (EDF R&D, INRIA, École Polytechnique)
- [[entities/aymeric-dieuleveut|Aymeric Dieuleveut]] (École Polytechnique)
- [[entities/julie-josse|Julie Josse]] (INRIA)
- [[entities/yaniv-romano|Yaniv Romano]] (Technion)

## Related Papers

- [[sources/zaffran-2022-aci|Zaffran et al. (2022)]] - Adaptive Conformal Predictions for Time Series
- Romano et al. (2019) - Conformalized Quantile Regression
- Le Morvan et al. (2021) - Imputation for supervised learning
- [[sources/farinhas-2024-non-exchangeable-crc|Farinhas et al. (2024)]] - Non-exchangeable CRC

## See Also

- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[concepts/split-conformal-prediction|Split Conformal Prediction]]
