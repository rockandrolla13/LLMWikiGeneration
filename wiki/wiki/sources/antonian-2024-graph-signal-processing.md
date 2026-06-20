---
title: Bayesian Reconstruction and Regression with Multivariate Graph Signals
page_id: sources/antonian-2024-graph-signal-processing
page_type: source
created: 2026-04-26 02:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- graph-signal-processing
- Bayesian-methods
- Kalman-filter
- tensor-methods
- financial-applications
- NatWest
authors:
- Edward Antonian
year: 2024
journal: PhD Thesis, Heriot-Watt University
institution:
- Heriot-Watt University
- NatWest
supervisors:
- Mike Chantler
- Gareth W. Peters
related:
- concepts/graph-signal-processing
- concepts/bayesian-inference
- concepts/kronecker-products
- concepts/tensor-methods
schema_version: 2
uuid: bfc800ad-d72c-515b-b476-aee2fcbc7c17
content_hash: sha256:6cb0697c327f07e5c90538d305c9eae23f4e06929f8a96d78070f2239a86940f
---

<!-- AUTHORED REGION START -->
# Bayesian Reconstruction and Regression with Multivariate Graph Signals

## Summary

PhD thesis advancing Graph Signal Processing (GSP) theory for Bayesian reconstruction and regression with multivariate graph signals. Develops efficient algorithms for Cartesian product graphs, extends to tensor-valued signals (MWGSP), and applies to financial data including work sponsored by NatWest.

## Key Contributions

1. **Cartesian Product Graph Reconstruction**: Efficient algorithms for signals on 2D product graphs with missing data
2. **Kernel Graph Regression (KGR)**: Generalized for arbitrary missing data patterns
3. **Regression with Network Cohesion (RNC)**: Extended for endogenous variables
4. **Multiway GSP (MWGSP)**: Algorithms for tensor-valued graph signals
5. **PyKronecker Library**: Software for high-dimensional Kronecker-structured matrices

## Methodological Advances

### Reconstruction Algorithms
- Stationary iterative method
- Conjugate gradient method
- Eigendecomposition-free distributed implementation
- Optimal method choice depends on hyperparameters and data sparsity

### Posterior Covariance
- Algorithms for marginal posterior variance estimation
- Active learning strategy for superior estimates (R² > 0.95)
- Perturbation optimization for direct posterior sampling (avoids MCMC)

### Extensions
- Binary and categorical tensor graph signals
- Chebyshev polynomial approximations for graph filters

## Financial Applications

- Developed in partnership with NatWest
- Real-world case studies throughout thesis
- Applications in finance and economics (Chapter 1.3.3)

## Key Concepts

- [[concepts/graph-signal-processing|Graph Signal Processing]]
- [[concepts/bayesian-inference|Bayesian Inference]]
- [[concepts/kronecker-products|Kronecker Products]]
- [[concepts/tensor-methods|Tensor Methods]]

## Technical Framework

### Graph Kernels and Filters
- Bayesian approaches to GSP
- Chebyshev polynomial approximations
- Spectral graph theory foundations

### Multiway GSP
- Tensor-valued signals
- Multiple graph topologies per axis
- PyKronecker abstracted API

## Implications for Finance

1. GSP provides framework for networked financial data
2. Missing data handling crucial for illiquid markets
3. Bayesian uncertainty quantification
4. Industrial application at major bank

## Related Sources

- [[sources/nunes-2022-ml-fixed-income|Nunes (2022)]] - ML in fixed income
- [[sources/saha-2024-muni-bond-ml|Saha et al. (2024)]] - similarity learning

<!-- AUTHORED REGION END -->
