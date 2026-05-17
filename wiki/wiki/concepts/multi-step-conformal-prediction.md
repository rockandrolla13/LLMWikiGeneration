---
title: Multi-step Conformal Prediction
page_id: concepts/multi-step-conformal-prediction
page_type: concept
revision_id: 1
created: 2026-04-26T10:00:00Z
updated: 2026-04-26T10:00:00Z
tags: [conformal-prediction, time-series, multi-step-forecasting, uncertainty-quantification]
sources: [sources/xu-2022-spci, sources/sun-2022-copula-cpts]
related: [concepts/conformal-prediction, concepts/prediction-intervals, concepts/coverage-guarantee, concepts/copulas, concepts/spci]
mind_map_priority: high
---

# Multi-step Conformal Prediction

**Multi-step conformal prediction** extends [[concepts/conformal-prediction|conformal prediction]] to provide valid uncertainty quantification for forecasting multiple time steps into the future. The key challenge is providing a [[concepts/coverage-guarantee|coverage guarantee]] for the **entire forecast horizon**, not just individual steps.

## Problem Formulation

Given input x₁:ₜ (t time steps of history), predict k future steps y₁:ₖ with confidence regions Γ₁,...,Γₖ such that:

**Step-wise validity**: P[yⱼ ∈ Γⱼ] ≥ 1-α for each j

**Full-horizon validity** (stronger): P[∀j ∈ {1,...,k}: yⱼ ∈ Γⱼ] ≥ 1-α

The full-horizon requirement is crucial for applications where the entire trajectory must be covered (e.g., autonomous vehicle planning, medical treatment paths).

## Approaches

### 1. Bonferroni Correction (CF-RNN)
Apply conformal prediction to each step with adjusted coverage 1-α/k:

P[∀j: yⱼ ∈ Γⱼ^{1-α/k}] ≥ 1-α (by union bound)

**Pros**: Simple, guaranteed validity
**Cons**: Highly conservative, especially for large k (confidence regions grow linearly with horizon)

### 2. Copula-based Methods ([[sources/sun-2022-copula-cpts|CopulaCPTS]])
Model the joint distribution of nonconformity scores across time steps using [[concepts/copulas|copulas]]:

1. Calibrate marginal CDFs F̂₁,...,F̂ₖ for each step's scores
2. Construct empirical copula C on transformed scores
3. Find u* such that C(u*) ≥ 1-α
4. Construct Γⱼ using F̂ⱼ⁻¹(u*ⱼ)

**Pros**: Captures dependency, much tighter regions
**Cons**: Requires split calibration, more data needed

### 3. Divide-and-Conquer ([[sources/xu-2022-spci|SPCI]])
Apply [[concepts/spci|SPCI]] separately to each horizon:
- Train S quantile regressors on lagged data (Xₜ, Yₜ₊ₛ) for s = 0,...,S-1
- Each provides step-wise coverage

**Pros**: Simple extension of univariate method
**Cons**: Doesn't capture joint distribution, only step-wise validity

## Comparison

| Method | Validity | Efficiency | Data Required |
|--------|----------|------------|---------------|
| Bonferroni | Full-horizon | Poor (O(k) wider) | Standard |
| CopulaCPTS | Full-horizon | Good | 2× calibration |
| SPCI multi-step | Step-wise only | Good | Standard |

## Theoretical Considerations

### Frechet-Hoeffding Bounds
The Bonferroni correction corresponds to the lower Frechet-Hoeffding bound for copulas. Any valid copula-based method must produce at least as tight regions:

max(Σuᵢ - k + 1, 0) ≤ C(u₁,...,uₖ)

This guarantees CopulaCPTS is at least as efficient as Bonferroni.

### Exchangeability Requirements
- **Single time series methods** (EnbPI, ACI, SPCI): Cannot provide full-horizon guarantees due to non-exchangeability
- **Multiple independent series** (CopulaCPTS): Exchangeability holds across series, enabling full-horizon validity

## Practical Guidance

**Use CopulaCPTS when**:
- Multiple independent time series available
- Full-horizon coverage is critical
- Forecast horizon k is long (k > 10)

**Use Bonferroni when**:
- Limited calibration data
- Simplicity is prioritized
- Short horizons (k < 5)

**Use SPCI multi-step when**:
- Single time series
- Step-wise coverage is sufficient
- Computational efficiency matters

## Applications

- **Autonomous vehicles**: Trajectory prediction must cover full path
- **Healthcare**: Treatment plans with uncertainty bounds
- **Energy**: Multi-day ahead power forecasting
- **Finance**: Multi-period portfolio risk

## Example: Horizon Length Scaling

From CopulaCPTS experiments (particle simulation, 90% confidence):

| Horizon k | CF-RNN Area | CopulaCPTS Area | Reduction |
|-----------|-------------|-----------------|-----------|
| 10 | 3.2 | 2.5 | 22% |
| 20 | 5.8 | 3.8 | 34% |
| 25 | 8.1 | 4.0 | 51% |

The advantage of copula-based methods grows with horizon length.

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/copulas|Copulas]]
- [[concepts/spci|SPCI]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/prediction-intervals|Prediction Intervals]]
