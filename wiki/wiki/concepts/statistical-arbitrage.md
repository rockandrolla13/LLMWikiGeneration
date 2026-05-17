---
title: "Statistical Arbitrage"
page_id: concepts/statistical-arbitrage
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [quantitative-finance, trading-strategies, mean-reversion, market-neutral]
related: [concepts/pairs-trading, concepts/cointegration, concepts/mean-reversion, concepts/kalman-filter, concepts/market-neutral]
sources: [sources/montana-2009-flexible-least-squares, sources/triantafyllopoulos-2011-mean-reverting-spreads, sources/he-2023-hf-pairs-chinese-futures, sources/zhang-2021-pairs-general-ssm]
---

## Definition

Statistical arbitrage (stat arb) is a class of trading strategies that exploit statistical mispricings between related financial instruments. Unlike true arbitrage, which is theoretically risk-free, statistical arbitrage involves probabilistic bets on price relationships reverting to historical norms.

## Core Principles

### 1. Mean Reversion
The fundamental assumption is that certain price relationships (spreads) are mean-reverting:
- Deviations from equilibrium are temporary
- Prices will correct back toward historical relationship
- Profit from buying undervalued and selling overvalued assets

### 2. Market Neutrality
Statistical arbitrage strategies are typically market-neutral:
- Long and short positions offset market exposure
- Returns largely independent of overall market direction
- Focus on relative value rather than directional bets

### 3. Statistical Edge
Strategies rely on statistical analysis rather than fundamental views:
- Historical price patterns and correlations
- Cointegration relationships
- Time-series econometric models

## Common Strategy Types

### [[concepts/pairs-trading|Pairs Trading]]
The simplest form of statistical arbitrage:
- Two correlated/cointegrated assets
- Trade the spread between them
- Originated at Morgan Stanley in 1980s (Nunzio Tartaglia)

### Index Arbitrage
Exploit discrepancies between:
- Index futures and constituent stocks
- ETFs and underlying baskets
- Related indices

### Statistical Factor Models
Multi-asset strategies based on:
- Principal component analysis (PCA)
- Arbitrage pricing theory (APT)
- Risk factor exposures

## Quantitative Methods

### Cointegration Testing
Identify long-term equilibrium relationships:
- Johansen test
- Engle-Granger two-step
- Error correction models

### State-Space Models
Model spread dynamics using [[concepts/kalman-filter|Kalman filter]]:
- Hidden state represents "true" spread
- Time-varying parameters via [[concepts/state-space-models|state-space models]]
- Probabilistic trading rules

### Machine Learning
Modern approaches incorporate:
- Neural networks for pattern recognition
- Reinforcement learning for optimal execution
- Ensemble methods for signal combination

## Key Risks

| Risk | Description | Mitigation |
|------|-------------|------------|
| Divergence Risk | Equilibrium relationship breaks down | Stop-loss rules, regime detection |
| Horizon Risk | Spread doesn't converge in time | Position sizing, time limits |
| Liquidity Risk | Unable to exit positions | Trade liquid instruments, limit size |
| Model Risk | Statistical model misspecified | Backtesting, out-of-sample validation |

## Performance Metrics

- **Sharpe Ratio**: Risk-adjusted return
- **Maximum Drawdown**: Largest peak-to-trough decline
- **Calmar Ratio**: Return / Maximum Drawdown
- **Half-Life**: Time for spread to revert halfway to mean

## Applications in Literature

Papers in this wiki applying statistical arbitrage:
- [[sources/montana-2009-flexible-least-squares|Montana et al. (2009)]]: FLS for S&P 500 futures
- [[sources/triantafyllopoulos-2011-mean-reverting-spreads|Triantafyllopoulos & Montana (2011)]]: Bayesian spread modeling
- [[sources/he-2023-hf-pairs-chinese-futures|He et al. (2023)]]: Chinese futures market
- [[sources/zhang-2021-pairs-general-ssm|Zhang (2021)]]: General state-space framework

## Historical Context

- **1980s**: Developed at Morgan Stanley by Tartaglia's team
- **1990s**: Widespread adoption by hedge funds
- **2000s**: High-frequency implementation
- **2007-2008**: August 2007 "quant quake" - widespread losses
- **2010s-present**: Machine learning integration
