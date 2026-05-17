---
title: "A Pairs Trading Strategy Based on Linear State Space Models and the Kalman Filter"
page_id: sources/moura-2016-pairs-trading-kalman
page_type: source
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [pairs-trading, kalman-filter, state-space-models, statistical-arbitrage, mean-reversion, arma, ornstein-uhlenbeck]
authors: [Carlos Eduardo de Moura, Adrian Pizzinga, Jorge Zubelli]
year: 2016
related: [concepts/kalman-filter, concepts/state-space-models, concepts/statistical-arbitrage, concepts/pairs-trading, concepts/cointegration, concepts/ornstein-uhlenbeck-process, entities/adrian-pizzinga, entities/jorge-zubelli]
---

## Summary

This paper proposes a pairs trading strategy entirely based on linear state space models for modeling the spread between paired assets. The methodology uses the Kalman filter to calculate conditional probabilities that the spread will return to its long-term mean, providing a novel trading rule based on probabilistic assessment of mean reversion.

## Key Contributions

- Extends Elliott et al. (2005) unobserved component model to general ARMA class
- Proves that Elliott et al.'s model is equivalent to ARMA(1,1) process
- Proposes new trading rule based on k-steps-ahead conditional probabilities of mean reversion
- Demonstrates strategy outperforms market benchmarks with single-spread portfolios
- Provides rigorous state-space framework for pairs trading

## Theoretical Framework

### Model Classes

1. **Unobserved Component Model** (Elliott et al. 2005):
   - Observed spread S_t is noisy observation of hidden mean-reverting state x_t
   - Hidden state follows discrete Ornstein-Uhlenbeck process
   - Captures mean-reverting behavior with financial theory support

2. **ARMA Models**:
   - Paper proves ARMA class encompasses Elliott et al. model
   - Allows for more general probabilistic descriptions
   - ARMA(p,q) specifications provide flexible spread dynamics

### Key Proposition

The paper proves that if S_t follows the Elliott et al. unobserved component model, then S_t ~ ARMA(1,1). This theoretical result enables:
- Model selection using standard ARMA diagnostics
- Rejection of Elliott et al. specification if data doesn't fit ARMA(1,1)

## Trading Strategy

### Conditional Probability Approach

1. Estimate state-space model using spread data via MLE
2. Construct augmented state-space for k-steps-ahead prediction
3. Apply Kalman filter to obtain conditional mean and covariance
4. Calculate conditional probability P(spread crosses mean within k steps)
5. Enter position when:
   - Spread significantly deviates from long-term mean
   - Conditional probability of mean reversion exceeds threshold

### Trading Rule

- If spread << mean AND P(spread increases above mean) is large: BUY spread
- If spread >> mean AND P(spread decreases below mean) is large: SELL spread

## Applications

### US Market Example
- PepsiCo (PEP) vs Coca-Cola (KO)
- Both in beverage industry with similar characteristics
- Cointegration confirmed via econometric tests

### Brazilian Market Example
- Vale (VALE3) vs Petrobras (PETR4)
- Both large commodity exporters
- Tests strategy in emerging market context

## Results

Single-spread portfolios outperform main market benchmarks including:
- S&P 500 / Bovespa indices
- Simple distance-based pairs trading (Gatev et al. 2006)

## Related Concepts

- [[concepts/kalman-filter|Kalman Filter]] for state estimation
- [[concepts/state-space-models|State Space Models]] for spread dynamics
- [[concepts/ornstein-uhlenbeck-process|Ornstein-Uhlenbeck Process]] as continuous-time limit
- [[concepts/pairs-trading|Pairs Trading]] strategy framework

## Citations

de Moura, C. E., Pizzinga, A., & Zubelli, J. (2016). A pairs trading strategy based on linear state space models and the Kalman filter. Quantitative Finance, 16(10), 1559-1573.
