---
title: "Kernel Two-Sample and Independence Tests for Nonstationary Random Processes"
page_id: sources/laumann-2021-kernel-tests-nonstationary
page_type: source
source_type: conference-paper
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
authors: [Felix Laumann, Julius von Kügelgen, Mauricio Barahona]
year: 2021
venue: Engineering Proceedings (MDPI)
tags: [mmd, hsic, kernel-methods, two-sample-test, independence-test, nonstationary, random-processes, hypothesis-testing]
related: [concepts/kernel-methods, concepts/mmd, concepts/hsic, concepts/nonstationarity, sources/koukorinis-stylized-facts]
mind_map_priority: high
---

# Kernel Two-Sample and Independence Tests for Nonstationary Random Processes

**Authors:** Felix Laumann, Julius von Kügelgen, Mauricio Barahona

**Year:** 2021

**Venue:** Engineering Proceedings, Vol. 5, No. 31 (MDPI)

**Institution:** Imperial College London

## Summary

This paper extends kernel-based hypothesis tests (MMD for two-sample testing and HSIC for independence testing) to handle nonstationary random processes. The authors address the fundamental challenge that classical kernel tests assume i.i.d. observations, which fails for time series and financial data exhibiting temporal dependence and nonstationarity.

## Key Contributions

### 1. Nonstationary MMD Extension
- Maximum Mean Discrepancy for nonstationary processes
- Accounts for time-varying distributions
- Block bootstrap methods for significance testing
- Preserves test consistency under dependence

### 2. Nonstationary HSIC Extension
- Hilbert-Schmidt Independence Criterion for dependent data
- Tests independence between nonstationary processes
- Handles autocorrelated and cross-correlated data
- Wild bootstrap for p-value computation

### 3. Theoretical Guarantees
- Asymptotic distribution theory for dependent samples
- Conditions for test consistency
- Convergence rates under mixing conditions
- Comparison with i.i.d. case

## Methodology

### Maximum Mean Discrepancy (MMD)

**Classical MMD:**
```
MMD²[F,P,Q] = ||μ_P - μ_Q||²_H
```
Where μ_P, μ_Q are kernel mean embeddings in RKHS H.

**Empirical Estimator:**
```
MMD²_u = (1/n(n-1)) Σ_{i≠j} k(x_i,x_j) + (1/m(m-1)) Σ_{i≠j} k(y_i,y_j) - (2/nm) Σ_{i,j} k(x_i,y_j)
```

**Extension for Nonstationarity:**
- Replace i.i.d. assumption with mixing conditions
- Block bootstrap preserves temporal structure
- Overlapping or non-overlapping blocks
- Block size selection via cross-validation

### Hilbert-Schmidt Independence Criterion (HSIC)

**Classical HSIC:**
```
HSIC(P_{XY}) = ||C_{XY} - μ_X ⊗ μ_Y||²_{HS}
```
Tests H_0: X ⊥ Y vs H_1: X ⫫̸ Y

**Extension for Nonstationarity:**
- Wild bootstrap for dependent samples
- Handles serial correlation within and across series
- Preserves test power under dependence
- Robust to heteroscedasticity

### Kernel Choices
- Gaussian RBF: k(x,y) = exp(-||x-y||²/2σ²)
- Median heuristic for bandwidth selection
- Characteristic kernels ensure test consistency

## Key Results

### Simulation Studies
| Test Setting | Classical Test | Proposed Extension |
|--------------|---------------|-------------------|
| i.i.d. data | Valid | Valid |
| AR(1) dependence | Inflated Type I | Valid |
| Nonstationary mean | Invalid | Valid |
| Time-varying variance | Invalid | Valid |

### Empirical Findings
1. Classical tests over-reject under dependence
2. Block bootstrap controls Type I error
3. Wild bootstrap effective for HSIC
4. Power preserved vs classical tests on i.i.d. data

### Block Size Selection
- Too small: fails to capture dependence
- Too large: insufficient bootstrap samples
- Cross-validation or rule-of-thumb methods
- Sensitivity analysis recommended

## Applications

### Financial Time Series
- Test for regime changes (two-sample)
- Test independence between asset returns
- Detect structural breaks
- Compare distributions across periods

### Model Validation
- Test if simulated data matches real data
- Validate time series models
- Assess forecast distribution quality
- Compare model outputs

### Change Point Detection
- Sequential application of MMD test
- Detect when distribution changes
- Online monitoring applications
- Sliding window implementations

## Theoretical Framework

### Mixing Conditions
- α-mixing (strong mixing)
- β-mixing (absolute regularity)
- Allows for "memory decay" in dependence
- Most financial time series satisfy these

### Asymptotic Theory
- Under mixing: √n(MMD²_u - MMD²) → N(0,σ²)
- Variance σ² accounts for dependence
- Bootstrap consistently estimates σ²

## See Also

- [[concepts/kernel-methods|Kernel Methods]]
- [[concepts/mmd|Maximum Mean Discrepancy]]
- [[concepts/hsic|HSIC]]
- [[concepts/nonstationarity|Nonstationarity]]
- [[sources/koukorinis-stylized-facts|Koukorinis et al. Stylized Facts]]
