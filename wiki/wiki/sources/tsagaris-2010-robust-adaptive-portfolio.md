---
title: Robust and Adaptive Algorithms for Online Portfolio Selection
page_id: sources/tsagaris-2010-robust-adaptive-portfolio
page_type: source
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- portfolio-selection
- adaptive-filtering
- algorithmic-trading
- mean-variance
- kalman-filter
authors:
- Theodoros Tsagaris
- Ajay Jasra
- Niall Adams
year: 2010
related:
- concepts/kalman-filter
- concepts/statistical-arbitrage
- concepts/mean-variance-optimization
- entities/theodoros-tsagaris
- entities/giovanni-montana
schema_version: 2
uuid: 5db58c04-6359-515c-9787-38dea3b795d9
content_hash: sha256:2caf5b16dca9b5ccdddbabceab7baa8d48fcc61bb7d5928b81d6b158bd395c5d
---

<!-- AUTHORED REGION START -->
## Summary

This paper presents online approaches to portfolio selection within the context of algorithmic trading, which demands fast and recursive updates of portfolio allocations as new data arrives. The authors develop two online algorithms: Robust-Exponentially Weighted Least Squares (R-EWRLS) and a regularized Online minimum Variance algorithm (O-VAR).

## Key Contributions

- Establishes algebraic connection between mean-variance theory and recursive least squares estimation
- Introduces R-EWRLS: combines M-estimation with exponential forgetting for robustness to outliers
- Introduces O-VAR: online minimum variance algorithm with L2-regularization
- Both algorithms are adaptive to non-stationary market environments
- Demonstrates computational efficiency suitable for high-frequency algorithmic trading

## Methodology

The paper links classical mean-variance portfolio optimization to Ordinary Least Squares (OLS), enabling the use of recursive estimation algorithms from signal processing. Key features include:

- **Adaptive filtering**: Uses forgetting factors (lambda) for time-varying parameter estimation
- **Robustness**: M-estimation with Huber loss function to handle outliers
- **Regularization**: L2 constraints equivalent to shrinkage toward naive (equal-weighted) portfolio
- **Efficiency**: Sequential, one-pass methods processing data in real-time

## Mathematical Framework

The portfolio allocation is framed as a sliding window regression problem:

- Target variable set to 1 (representing ideal risk-free positive returns)
- Portfolio weights emerge as regression coefficients
- Forgetting factor lambda downweights older observations
- Regularization parameter delta controls shrinkage toward naive allocation

## Related Work

The paper builds on flexible least squares methodology developed in collaboration with [[entities/giovanni-montana|Giovanni Montana]] and connects to [[concepts/kalman-filter|Kalman filter]] estimation through the equivalence between recursive least squares and Kalman filtering.

## Applications

- Algorithmic trading systems requiring millisecond-level decisions
- Real-time portfolio rebalancing
- Market-neutral statistical arbitrage strategies

## Citations

Tsagaris, T., Jasra, A., & Adams, N. (2010). Robust and Adaptive Algorithms for Online Portfolio Selection. arXiv:1005.2979.

<!-- AUTHORED REGION END -->
