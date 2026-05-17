---
title: "Machine Learning in Fixed Income Markets: Forecasting and Portfolio Management"
page_id: sources/nunes-2022-ml-fixed-income
page_type: source
created: 2026-04-26T02:00:00Z
updated: 2026-04-26T02:00:00Z
tags: [machine-learning, fixed-income, yield-curve, LSTM, reinforcement-learning, portfolio-management, MLP]
authors: [Manuel Clemente Mendonça Nunes]
year: 2022
journal: PhD Thesis, University of Southampton
institution: University of Southampton
related: [concepts/yield-curve-forecasting, concepts/lstm, concepts/reinforcement-learning, concepts/neural-networks]
---

# Machine Learning in Fixed Income Markets: Forecasting and Portfolio Management

## Summary

PhD thesis applying machine learning to fixed income markets, covering yield curve forecasting with MLPs and LSTMs, and portfolio management with reinforcement learning. Demonstrates ML superiority over classical models for yield curve prediction and explores RL for bond ETF portfolio management.

## Three Main Topics

### 1. MLP Yield Curve Forecasting
- Multivariate linear regression vs MLP comparison
- Five forecasting horizons
- Rigorous feature selection process
- MLPs with relevant features achieve best results
- Artificially-generated data from linear models improves accuracy

### 2. LSTM Bond Yield Forecasting
- Dynamic LSTM for 10-year bond yield prediction
- Lower prediction errors with higher confidence than static MLPs
- Novel **LSTM-LagLasso** method for interpretability
- Studies internal gating signals using exogenous variables
- Shows how hidden units dynamically switch across temporal regimes

### 3. Reinforcement Learning Portfolio Management
- Purpose-built environment for fixed income
- Deep Deterministic Policy Gradient (DDPG) algorithm
- Four bond ETFs as inputs
- Outperforms buy-and-hold and best single asset
- Novel methodology with principled agent selection

## Key Results

| Model | Application | Performance |
|-------|-------------|-------------|
| MLP | European yield curve | Superior to benchmarks |
| LSTM | 10-year bond yield | Lower error, higher confidence |
| DDPG | Bond ETF portfolio | Beats buy-and-hold |

## Methodological Contributions

- Custom-built models for each target/horizon
- LSTM-LagLasso for black-box interpretability
- Agent selection criteria during RL training
- Feature selection identifying relevant predictors

## Key Concepts

- [[concepts/yield-curve-forecasting|Yield Curve Forecasting]]
- [[concepts/lstm|Long Short-Term Memory]]
- [[concepts/reinforcement-learning|Reinforcement Learning]]
- [[concepts/neural-networks|Neural Networks]]

## Implications

1. ML superior to classical models for yield curve forecasting
2. Feature selection crucial - different features matter for different targets
3. LSTM internal signals can be interpreted
4. RL viable for bond portfolio management despite instability

## Related Sources

- [[sources/feng-2025-predicting-bond-returns|Feng et al. (2025)]] - ML corporate bond prediction
- [[sources/krishnan-2007-credit-spread-forecast|Krishnan et al. (2007)]] - yield curve forecasting
- [[sources/antonian-2024-graph-signal-processing|Antonian (2024)]] - Bayesian methods
