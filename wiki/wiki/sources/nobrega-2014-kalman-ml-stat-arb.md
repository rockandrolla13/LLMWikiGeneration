---
title: A Combination Forecasting Model Using Machine Learning and Kalman Filter for
  Statistical Arbitrage
page_id: sources/nobrega-2014-kalman-ml-stat-arb
page_type: source
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- statistical-arbitrage
- pairs-trading
- kalman-filter
- machine-learning
- extreme-learning-machine
- support-vector-regression
authors:
- Jarley P. Nobrega
- Adriano L. I. Oliveira
year: 2014
related:
- concepts/kalman-filter
- concepts/statistical-arbitrage
- concepts/pairs-trading
- concepts/cointegration
schema_version: 2
uuid: 2aa6ed19-0ec0-5ab2-bd79-0666630e6cca
content_hash: sha256:28c9ee540eb1e9215573777152f5605d0714f5dfad5845cc04ec9718a3e54214
---

<!-- AUTHORED REGION START -->
## Summary

This paper evaluates the combination of Extreme Learning Machine (ELM) and Support Vector Regression (SVR) with a Kalman filter regression model for financial time series forecasting in the context of statistical arbitrage. The hybrid approach aims to exploit the strengths of both machine learning and state-space methods.

## Key Contributions

- Proposes combining ELM and SVR individual forecasts using Kalman filter regression
- Compares performance against linear combination methods (Bayesian Average, Granger-Ramanathan, LASSO)
- Demonstrates that Kalman filter combination improves statistical performance of individual forecasts
- Validates impact on annualized returns and volatility using pairs trading strategy

## Methodology

### Forecasting Components

1. **Extreme Learning Machine (ELM)**: Single hidden layer feedforward network with randomly assigned input weights and biases; output weights analytically determined via pseudoinverse

2. **Support Vector Regression (SVR)**: Uses RBF kernel for nonlinear regression with epsilon-insensitive loss function

3. **Kalman Filter Regression**: Combines forecasts using state-space model where combination weights evolve as random walk

### Combination Framework

The Kalman filter treats combination weights as time-varying parameters:
- Measurement equation: observed spread as linear combination of ELM and SVR forecasts
- State equation: weights follow random walk with Gaussian innovations
- Parameters estimated by maximum likelihood

## Application to Statistical Arbitrage

- Applied to Brazilian stock pairs (AMBV3/AMBV4)
- Tests whether price anomalies in correlated pairs can be exploited
- Evaluates trading performance using Sharpe ratio as risk measure
- Extended training period to include different market conditions

## Results

- Kalman filter combination outperforms individual ELM and SVR forecasts
- Improvement in both statistical accuracy and trading returns
- Method robust across different market regimes

## Related Concepts

- [[concepts/kalman-filter|Kalman Filter]] for time-varying parameter estimation
- [[concepts/pairs-trading|Pairs Trading]] strategy framework
- [[concepts/cointegration|Cointegration]] for identifying trading pairs

## Citations

Nobrega, J. P., & Oliveira, A. L. I. (2014). A Combination Forecasting Model Using Machine Learning and Kalman Filter for Statistical Arbitrage. IEEE International Conference on Systems, Man, and Cybernetics.

<!-- AUTHORED REGION END -->
