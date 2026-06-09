---
authors:
- Michael L. Halls-Moore
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/halls-moore-advanced-algorithmic-trading
page_type: source
publication_date: null
publication_venue: QuantStart
related:
- concepts/algorithmic-trading
- concepts/arima-garch-models
- concepts/backtesting
- concepts/hidden-markov-models
- concepts/kalman-filter
- concepts/mcmc-bayesian-inference
- concepts/pairs-trading
- entities/michael-halls-moore
- entities/quantstart
revision_hash: sha256:7964d856f0d1fc41025248efac8da099cf0ab2dae2a75da2f976c71c2bedb9c9
revision_id: 1
source_hash: sha256:7a40f10a85e12808d1cc6d0ca8fdee2e41282e582570ec332e826d61321ce023
source_path: raw/creditmacro/Advanced Algorithmic Trading (Mike Halls-Moore) (z-library.sk,
  1lib.sk, z-lib.sk).md
source_type: book
sources: []
tags:
- algorithmic-trading
- quantitative-finance
- bayesian-statistics
- time-series
- machine-learning
- backtesting
- pairs-trading
title: Advanced Algorithmic Trading
updated: '2026-06-09T12:00:00Z'
updated_by: op_b7b9ceb47ac6
---

# Advanced Algorithmic Trading

**Authors:** Michael L. Halls-Moore · **Venue:** QuantStart · **Type:** book

## Summary

A practitioner quantitative-trading book by Michael Halls-Moore (QuantStart) teaching three statistical-modelling pillars - Bayesian statistics, time series analysis, and statistical machine learning - then applying them to build and backtest systematic strategies. The stated thesis is the 'hunt for alpha' via rigorous statistical analysis rather than ad hoc technical analysis, while acknowledging that known alpha decays. It develops Bayesian inference (MCMC, PyMC3), time series (ARMA/ARIMA, ARCH/GARCH, cointegration, Kalman filter, Hidden Markov Models for regime detection), and ML, then builds end-to-end strategies in the event-driven QSTrader engine including cointegration pairs trading, Kalman-filter dynamic-hedge-ratio pairs trading, and HMM regime filtering.

## Key Claims

1. Alpha is uncorrelated risk-adjusted return that, once well-known, decays and becomes a risk factor.
2. Serial correlation is the central organising idea of time series analysis; momentum strategies rest on positive serial correlation.
3. Cointegration provides the statistical basis for mean-reversion pairs-trading strategies, tested via ADF, CADF, and Johansen tests.
4. The Kalman filter enables a time-varying (dynamic) hedge ratio between ETF pairs by treating regression coefficients as a latent state.
5. Hidden Markov Models can detect latent market regimes and serve as a risk filter on an underlying strategy.
6. Strategies must be monitored for decay using metrics such as the annualised rolling Sharpe ratio.

## Questions Raised

- How robust are the demonstrated backtested strategies once transaction costs and out-of-sample decay are fully accounted for?
- Does the supervised intraday-return prediction approach adequately address class imbalance and lookahead bias?

## Concepts

- [[concepts/algorithmic-trading|Algorithmic Trading]]
- [[concepts/backtesting|Backtesting]]
- [[concepts/pairs-trading|Cointegration and Pairs Trading]]
- [[concepts/kalman-filter|Kalman Filter for Dynamic Hedge Ratios]]
- [[concepts/hidden-markov-models|Hidden Markov Models for Regime Detection]]
- [[concepts/arima-garch-models|ARIMA and GARCH Volatility Models]]
- [[concepts/mcmc-bayesian-inference|MCMC and Bayesian Inference]]

## Entities

- [[entities/michael-halls-moore|Michael L. Halls-Moore]]
- [[entities/quantstart|QuantStart]]

## Source

- **Path:** `raw/creditmacro/Advanced Algorithmic Trading (Mike Halls-Moore) (z-library.sk, 1lib.sk, z-lib.sk).md`
- **Type:** book
- **Hash:** `sha256:7a40f10a85e12808d...`