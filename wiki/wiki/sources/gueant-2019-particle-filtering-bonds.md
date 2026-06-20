---
title: 'Mid-Price Estimation for European Corporate Bonds: A Particle Filtering Approach'
page_id: sources/gueant-2019-particle-filtering-bonds
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Olivier Gueant
- Jiang Pu
year: 2019
venue: Market Microstructure and Liquidity
tags:
- particle-filtering
- smc
- corporate-bonds
- mid-price
- request-for-quotes
- bayesian
- otc-markets
- market-making
related:
- concepts/particle-filtering
- concepts/sequential-monte-carlo
- concepts/market-making
- concepts/request-for-quotes
- sources/fermanian-2017-md2c-corporate-bonds
- entities/olivier-gueant
mind_map_priority: high
schema_version: 2
uuid: 20aca1fd-79cd-50c5-903b-98b28b802a60
content_hash: sha256:d80b55458b639a2c67577418c75ec9ab4446278ad2ba18017fb9290cf236b33d
---

<!-- AUTHORED REGION START -->
# Mid-Price Estimation for European Corporate Bonds: A Particle Filtering Approach

**Authors:** Olivier Gueant, Jiang Pu

**Year:** 2019

**Venue:** Market Microstructure and Liquidity, Vol. 4, Nos. 1&2

**Institutions:** Universite Paris 1 Pantheon-Sorbonne, Institut Europlace de Finance

## Summary

This paper presents a Bayesian method using particle filtering/sequential Monte Carlo (SMC) for estimating mid-prices of European corporate bonds in real-time. The method incorporates information from D2C trades, D2D trades, and "Traded Away" RFQs to provide a distribution over reference prices rather than a single point estimate.

## Key Contributions

### 1. Particle Filtering for OTC Markets
- Novel application of SMC to illiquid bond markets
- Handles censored observations from RFQs
- Overcomes limitations of Kalman filters
- Scales well despite curse of dimensionality

### 2. Multi-Source Information Integration
- Dealer-to-Client (D2C) trades
- Dealer-to-Dealer (D2D) trades
- "Traded Away" RFQs (censored observations)
- Real-time updating capability

### 3. Distributional Output
- Provides full posterior distribution, not just point estimate
- Quantifies uncertainty in mid-price
- Enables probabilistic risk management
- Supports market making optimization

## Methodology

### Model Framework
- Mid-YtB (yield to benchmark) follows Brownian motion
- Half bid-ask spread follows Ornstein-Uhlenbeck process
- d-dimensional system for multiple bonds
- Correlation structure across bonds

### Five Observation Types
1. **D2C Buy:** Client buys from dealer D
2. **D2C Sell:** Client sells to dealer D
3. **Traded Away Buy:** Client buys from competitor (censored)
4. **Traded Away Sell:** Client sells to competitor (censored)
5. **D2D Trade:** Interdealer broker transaction

### SMC Algorithm Steps
1. Draw half bid-ask spreads
2. Compute likelihood weights based on observation type
3. Resample particles (importance sampling)
4. Draw mid-YtB plus noise for observed bond
5. Condition on Gaussian update
6. Draw correlated mid-YtBs for other bonds

### Likelihood Functions
- D2C trades: Gaussian observation model
- Traded Away RFQs: Truncated Gaussian (censored)
- D2D trades: Two-sided truncated Gaussian

## Key Results

### Computational Properties
- Algorithm tested with K = 10,000 particles
- No curse of dimensionality issues for d = 100 bonds
- Real-time capability due to sparse observations
- Correlation structure improves multi-asset estimation

### Parameter Estimation
- Volatility and correlations from CBBT data
- Half bid-ask spread from trade-CBBT differences
- Offline estimation before trading day
- Log-normal distribution for bid-ask spreads

### Illustration
- Tested on 3 corporate bonds from same issuer
- Confidence intervals (25-75%, 10-90%, 5-95%, 1-99%)
- Algorithm detects price dynamics despite sparse observations
- Correlation structure aids cross-asset estimation

## Applications

1. **Market Making:** Provide reference prices for quote optimization
2. **Risk Management:** Quantify uncertainty in mid-prices
3. **Algorithm Trading:** Input for market making algorithms
4. **Valuation:** Mark-to-model for illiquid bonds

## Extensions Discussed

### Model Enhancements
- Ornstein-Uhlenbeck dynamics for mean reversion
- Additional correlated variables (iTraxx, equity indices)
- Volume-dependent bid-ask spreads
- Dealer inventory adjustment

### Technical Extensions
- Post-trade transparency data integration
- SMC² for fully Bayesian parameter estimation
- Z-spread vs YtB alternatives
- High-yield bond adaptation

## Theoretical Framework

### Why Not Kalman Filter?
- Kalman works for linear observations
- RFQs provide censored (nonlinear) information
- Particle filter handles arbitrary observation models
- Flexibility for model extensions

### Curse of Dimensionality
- Traditionally limits particle methods to low dimensions
- Illiquid markets: sparse observations help
- Transactions rarely simultaneous across bonds
- Price diffusion between trades aids scaling

## See Also

- [[concepts/particle-filtering|Particle Filtering]]
- [[concepts/sequential-monte-carlo|Sequential Monte Carlo]]
- [[concepts/market-making|Market Making]]
- [[concepts/request-for-quotes|Request for Quotes]]
- [[sources/fermanian-2017-md2c-corporate-bonds|Fermanian et al. (2017) MD2C]]
- [[entities/olivier-gueant|Olivier Gueant]]

<!-- AUTHORED REGION END -->
