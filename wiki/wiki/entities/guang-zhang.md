---
title: "Guang Zhang"
page_id: entities/guang-zhang
page_type: entity
entity_type: researcher
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [researcher, pairs-trading, state-space-models, econometrics, boston-university]
affiliations: [Boston University]
related: [sources/zhang-2021-pairs-general-ssm]
---

## Biography

Guang Zhang is a researcher in the Department of Economics at Boston University. His research focuses on econometric methods for financial applications, particularly state-space models and pairs trading strategies.

## Research Contributions

### General State Space Models for Pairs Trading

Zhang's 2021 paper in Quantitative Finance ([[sources/zhang-2021-pairs-general-ssm|Zhang 2021]]) makes several important contributions:

1. **Non-Gaussian Models**: Extends pairs trading beyond Gaussian assumptions to handle heavy-tailed distributions (Student-t) and mixture models

2. **Heteroscedasticity**: Incorporates time-varying volatility and volatility clustering, which are essential features of financial data

3. **Nonlinear Mean Reversion**: Allows for quadratic and Ait-Sahalia type nonlinear mean-reverting processes

4. **Monte Carlo Optimization**: Develops simulation-based approach for optimal trading rule selection

### Key Innovations

- Trading strategy that exploits heteroscedasticity information
- Flexible objective functions (return, Sharpe ratio, Calmar ratio)
- Significant improvements over conventional approaches

## Empirical Results

Testing on various pairs:
- PEP vs KO: 21.86% annualized return (vs 13.11% conventional)
- EWT vs EWH: 31.84% annualized return (vs 14.80% conventional)
- Bank pairs: Small banks more profitable than large banks

## Selected Publications

1. Zhang, G. (2021). Pairs trading with general state space models. Quantitative Finance, 21(9), 1567-1587.

## Impact

His framework provides:
- More realistic modeling of spread dynamics
- Practical algorithms for computing optimal trading rules
- Evidence that heteroscedasticity information is economically valuable
