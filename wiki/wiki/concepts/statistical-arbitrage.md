---
created: 2026-04-26 03:00:00+00:00
page_id: concepts/statistical-arbitrage
page_type: concept
related:
- concepts/algorithmic-trading
- concepts/alpha-correlation-turnover
- concepts/alpha-signal
- concepts/capital-structure-arbitrage
- concepts/cointegration
- concepts/credit-relative-value
- concepts/cross-sectional-momentum
- concepts/etf-creation-redemption-arbitrage
- concepts/factor-investing
- concepts/factor-signals-in-credit
- concepts/kalman-filter
- concepts/limits-to-arbitrage
- concepts/liquidity-risk
- concepts/market-integration-concordance-measure
- concepts/market-neutral
- concepts/mean-reversion
- concepts/non-fundamental-demand-shocks
- concepts/pairs-trading
- concepts/regime-switching-models
- concepts/relative-value-spread-trading
- concepts/systematic-credit-relative-value
revision_id: 3
sources:
- sources/he-2023-hf-pairs-chinese-futures
- sources/montana-2009-flexible-least-squares
- sources/ms-2018-07-09-em-risk-indicator-regime-switching
- sources/triantafyllopoulos-2011-mean-reverting-spreads
- sources/zhang-2021-pairs-general-ssm
tags:
- quantitative-finance
- trading-strategies
- mean-reversion
- market-neutral
title: Statistical Arbitrage
updated: '2026-06-20T01:03:51Z'
schema_version: 2
uuid: d40cf5c3-b99b-5f99-be94-ada09a3b8816
content_hash: sha256:014f4163807d722a06a9cae19d4e3dbab62ac1ff0ec8068005e239060a3c60d0
---

<!-- AUTHORED REGION START -->
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

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/algorithmic-trading|algorithmic-trading]]
- [[concepts/alpha-correlation-turnover|alpha-correlation-turnover]]
- [[concepts/alpha-signal|alpha-signal]]
- [[concepts/capital-structure-arbitrage|capital-structure-arbitrage]]
- [[concepts/credit-relative-value|credit-relative-value]]
- [[concepts/cross-sectional-momentum|cross-sectional-momentum]]
- [[concepts/etf-creation-redemption-arbitrage|etf-creation-redemption-arbitrage]]
- [[concepts/factor-signals-in-credit|factor-signals-in-credit]]
- [[concepts/limits-to-arbitrage|limits-to-arbitrage]]
- [[concepts/liquidity-risk|liquidity-risk]]
- [[concepts/market-integration-concordance-measure|market-integration-concordance-measure]]
- [[concepts/non-fundamental-demand-shocks|non-fundamental-demand-shocks]]
- [[concepts/pairs-trading|pairs-trading]]
- [[concepts/relative-value-spread-trading|relative-value-spread-trading]]
- [[concepts/systematic-credit-relative-value|systematic-credit-relative-value]]

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/ms-2018-07-09-em-risk-indicator-regime-switching]]
<!-- AUTHORED REGION END -->
