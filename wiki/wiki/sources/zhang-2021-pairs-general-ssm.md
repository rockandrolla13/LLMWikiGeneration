---
title: "Pairs Trading with General State Space Models"
page_id: sources/zhang-2021-pairs-general-ssm
page_type: source
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [pairs-trading, state-space-models, kalman-filter, heteroscedasticity, nonlinear-models, monte-carlo, statistical-arbitrage]
authors: [Guang Zhang]
year: 2021
related: [concepts/kalman-filter, concepts/state-space-models, concepts/pairs-trading, concepts/statistical-arbitrage, concepts/heteroscedasticity, entities/guang-zhang]
---

## Summary

This paper proposes a general state space model framework for pairs trading that accommodates non-Gaussianity, heteroscedasticity, and nonlinearity in the mean-reverting spread. The approach uses Monte Carlo methods to determine optimal trading rules and demonstrates significant improvements over conventional methods.

## Key Contributions

1. **General State Space Framework**: Extends beyond Gaussian linear models to capture realistic asset dynamics
2. **Heteroscedasticity**: Models time-varying volatility and volatility clustering
3. **Nonlinear Mean Reversion**: Allows for nonlinear functions in state equation
4. **Monte Carlo Trading Rule**: Simulates optimal entry/exit thresholds
5. **Flexible Objectives**: Adapts to maximize return, Sharpe ratio, or Calmar ratio

## Model Specification

### Observation Equation
P_A,t - gamma * P_B,t = x_t + epsilon_t

Where:
- P_A, P_B: Prices of securities A and B
- gamma: Hedge ratio
- x_t: Unobservable true spread
- epsilon_t ~ N(0, sigma_epsilon^2)

### State Equation
x_t = f(x_{t-1}; theta) + g(x_{t-1}; theta) * eta_t

Supports multiple specifications:

| Model | f(x; theta) | Application |
|-------|-------------|-------------|
| Linear (O-U) | theta_1 + theta_2*x | Standard mean reversion |
| Quadratic | theta_1 + theta_2*x + theta_3*x^2 | Nonlinear reversion |
| Ait-Sahalia | theta_1 + theta_2/x + theta_3*x + theta_4*x^2 | Interest rate dynamics |

### Innovation Distribution

Supports:
- Gaussian: eta ~ N(0, 1)
- Student-t: eta ~ t(nu) for heavy tails
- Mixture: eta ~ pi*N(0,1) + (1-pi)*N(0,sigma^2) for jumps

## Trading Strategy

### Conventional Approach
- Enter when |z_t| > threshold (e.g., 2 std dev)
- Exit when z_t crosses zero

### Proposed Monte Carlo Approach

1. Estimate model parameters from training data
2. Simulate many spread paths from current state
3. For each candidate threshold pair (entry, exit):
   - Compute expected return, Sharpe ratio, etc.
4. Select optimal threshold maximizing objective
5. Re-optimize periodically

### Using Heteroscedasticity

Key insight: Position sizing based on conditional volatility
- High volatility states: Smaller positions or wider thresholds
- Low volatility states: Larger positions or tighter thresholds

## Empirical Applications

### PEP vs KO (Consumer Beverages)

| Method | Ann. Return | Sharpe Ratio |
|--------|-------------|--------------|
| Conventional | 13.11% | 1.10 |
| Proposed | 21.86% | 2.95 |

### EWT vs EWH (Taiwan/Hong Kong ETFs)

| Method | Ann. Return | Sharpe Ratio |
|--------|-------------|--------------|
| Conventional | 14.80% | 1.13 |
| Proposed | 31.84% | 3.89 |

### Bank Pairs
- Small banks: Higher returns (more volatile spreads)
- Large banks: Lower returns but more liquid

## Related Concepts

- [[concepts/kalman-filter|Kalman Filter]] - extended to nonlinear case
- [[concepts/state-space-models|State Space Models]] - general framework
- [[concepts/pairs-trading|Pairs Trading]] - application domain
- [[concepts/heteroscedasticity|Heteroscedasticity]] - volatility clustering

## Citations

Zhang, G. (2021). Pairs trading with general state space models. Quantitative Finance, 21(9), 1567-1587.
