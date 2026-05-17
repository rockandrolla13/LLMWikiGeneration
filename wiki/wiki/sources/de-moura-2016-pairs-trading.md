---
title: "A Pairs Trading Strategy Based on Linear State Space Models"
page_id: sources/de-moura-2016-pairs-trading
page_type: source
created: 2026-04-26T02:00:00Z
updated: 2026-04-26T02:00:00Z
tags: [pairs-trading, state-space-models, Kalman-filter, statistical-arbitrage, mean-reversion, cointegration]
authors: [Carlos Eduardo de Moura, Adrian Pizzinga, Jorge Zubelli]
year: 2016
journal: Quantitative Finance
institution: [IMPA, Fluminense Federal University]
related: [concepts/pairs-trading, concepts/state-space-models, concepts/kalman-filter, concepts/statistical-arbitrage, concepts/cointegration]
---

# A Pairs Trading Strategy Based on Linear State Space Models

## Summary

Proposes a pairs trading strategy based on linear state space models using the Kalman filter to calculate conditional probabilities of spread mean-reversion. Extends Elliott et al. (2005) framework by using ARMA models and conditional probability-based trading rules.

## Key Contributions

1. **ARMA Generalization**: Shows ARMA models encompass Elliott et al.'s mean-reverting model
2. **Probability-Based Trading**: New strategy based on conditional mean-reversion probabilities
3. **Empirical Validation**: Applications to US and Brazilian markets outperform benchmarks

## Methodology

### State Space Framework
- Unobserved component model (Elliott et al. 2005)
- ARMA models in state space form
- Kalman filter for k-steps-ahead prediction
- Conditional probability calculation for mean-reversion

### Trading Rule
Trade activated when:
1. Spread significantly deviates from long-term mean
2. Conditional probability of mean-reversion within k-steps is high
3. Buy (sell) spread when below (above) equilibrium with high reversion probability

## Key Results

- Strategy outperforms main market benchmarks
- Superior to naive pairs trading (Gatev et al. 2006)
- Works on single-spread portfolios
- Robust across US and Brazilian markets

## Theoretical Framework

### Cointegration
Two I(1) series Y_t and X_t are cointegrated if aY_t + bX_t ~ I(0)

### Mean-Reversion Model
Spread modeled as Ornstein-Uhlenbeck process in continuous time, discretized to state space form

## Key Concepts

- [[concepts/pairs-trading|Pairs Trading]]
- [[concepts/state-space-models|State Space Models]]
- [[concepts/kalman-filter|Kalman Filter]]
- [[concepts/cointegration|Cointegration]]

## Implications

1. Statistical framework for pairs trading decisions
2. Probability-based rules more principled than threshold rules
3. ARMA models flexible enough for spread modeling
4. Kalman filter enables optimal filtering and prediction

## Related Sources

- [[sources/krishnan-2007-credit-spread-forecast|Krishnan et al. (2007)]] - term structure forecasting
- [[sources/nunes-2022-ml-fixed-income|Nunes (2022)]] - ML in fixed income
