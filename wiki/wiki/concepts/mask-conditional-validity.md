---
title: Mask-Conditional Validity
page_id: concepts/mask-conditional-validity
page_type: concept
revision_id: 1
created: 2026-04-26 12:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- missing-data
- conditional-coverage
- fairness
sources:
- sources/zaffran-2023-conformal-missing
related:
- concepts/conformal-prediction
- concepts/coverage-guarantee
- concepts/missing-data-imputation
- entities/margaux-zaffran
mind_map_priority: high
schema_version: 2
uuid: 58f666ac-c3bf-5e66-83d9-2c6d62a25e5d
content_hash: sha256:321a97b11bac2d2ea9d8ad818a045f140dba5c2a970f7cb80abd22dee97bf679
---

<!-- AUTHORED REGION START -->
# Mask-Conditional Validity (MCV)

**Mask-Conditional Validity (MCV)** is a coverage guarantee for [[concepts/conformal-prediction|conformal prediction]] that ensures valid prediction intervals **conditionally on the pattern of missing values**.

## Definition

A method is MCV if for **any** missing pattern m ∈ M:

P(Y ∈ Ĉ_α(X, M) | M = m) ≥ 1 - α

A method is **exactly MCV** if additionally:

P(Y ∈ Ĉ_α(X, M) | M = m) ≤ 1 - α + O(1/n)

## Comparison with Marginal Validity

### Marginal Validity (Standard)

P(Y ∈ Ĉ_α(X, M)) ≥ 1 - α

This averages over all missing patterns. A method can be marginally valid while:
- Dramatically **undercovering** for some patterns
- **Overcovering** for others

### Why MCV Matters

[[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]] showed that standard conformal methods fail MCV:

| Pattern | QR Coverage | CQR Coverage |
|---------|-------------|--------------|
| All observed | >90% | ~90% |
| Important var missing | <80% | <85% |
| Multiple missing | <70% | <80% |

Methods achieve marginal validity by overcovering on "easy" patterns while undercovering on "hard" ones.

## Equity and Fairness Implications

MCV ensures **equitable treatment** across missing patterns:

1. **Medical applications**: Patients with incomplete records (due to equipment failure, different hospital protocols) should not receive prediction intervals less likely to contain the true outcome

2. **Socioeconomic fairness**: If missing patterns correlate with socioeconomic factors, MCV prevents disparate uncertainty quantification

3. **No pattern should be penalized**: Unlike marginal validity, MCV prevents systematically undercovering any subgroup

## Why Standard Methods Fail MCV

### Induced Heteroskedasticity

Missing values create pattern-dependent uncertainty:

Oracle interval length: L*_α(m) ∝ √(β_{mis(m)}^T Σ_{mis|obs} β_{mis(m)} + σ²_ε)

Uncertainty increases when **predictive variables** are missing.

### Pattern-Independent Calibration

Standard CQR computes a **single correction term** for all test points, regardless of their missing patterns. This fails when:
- Some patterns need wider intervals
- Some patterns need narrower intervals

## Achieving MCV: CP-MDA Framework

[[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]] introduced **CP-MDA** (Missing Data Augmentation):

### CP-MDA-Exact

1. Apply test point's mask to calibration set
2. Keep only calibration points with **exactly the same pattern**
3. Compute pattern-specific correction term

**Guarantee**: Exactly MCV under MCAR + exchangeability

**Limitation**: May discard many calibration points in high dimensions

### CP-MDA-Nested

1. Apply test point's mask to calibration set
2. Keep **all** calibration points (now have at least same missing values)
3. For each calibration point, predict on test with that point's augmented mask
4. Aggregate via quantiles

**Guarantee**: MCV under MCAR + stochastic domination assumption (A4)

**Advantage**: Uses all calibration data; more robust in high dimensions

## Stochastic Domination Assumption (A4)

If m̊ ⊂ m̆ (m̆ has more missing values), then for any δ ∈ [0, 0.5]:

q^{Y|X_obs(m̊),M=m̊}_δ ≤ q^{Y|X_obs(m̆),M=m̆}_δ

Intuition: Observing fewer variables leads to wider conditional distributions.

## Relationship to Conditional Coverage

MCV is a **group-conditional** guarantee intermediate between:

- **Marginal validity**: Average over all (X, M)
- **Full conditional validity**: P(Y ∈ C(x) | X=x) ≥ 1-α for all x (impossible to achieve informationally)

MCV conditions on M but not on X_obs, making it achievable while still meaningful.

## Empirical Evidence

From [[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]]:

| Method | Lowest Mask Cov | Highest Mask Cov | MCV? |
|--------|-----------------|------------------|------|
| QR | ~70% | >95% | No |
| CQR | ~80% | ~92% | No |
| CQR-MDA-Exact | ~90% | ~90% | Yes |
| CQR-MDA-Nested | ≥90% | >90% | Yes |

## Key References

- [[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]] - Introduced MCV concept
- Romano et al. (2020) - Equalized coverage for protected groups
- Barber et al. (2021) - Limits of conditional coverage

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/missing-data-imputation|Missing Data Imputation]]
- [[concepts/conformalized-quantile-regression|Conformalized Quantile Regression]]

<!-- AUTHORED REGION END -->
