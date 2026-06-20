---
created: 2026-04-26 03:00:00+00:00
page_id: concepts/pairs-trading
page_type: concept
related:
- concepts/capital-structure-arbitrage
- concepts/cointegration
- concepts/credit-relative-value
- concepts/kalman-filter
- concepts/mean-reversion
- concepts/spread
- concepts/statistical-arbitrage
revision_id: 2
sources:
- sources/halls-moore-advanced-algorithmic-trading
- sources/he-2023-hf-pairs-chinese-futures
- sources/moura-2016-pairs-trading-kalman
- sources/triantafyllopoulos-2011-mean-reverting-spreads
- sources/zhang-2021-pairs-general-ssm
tags:
- quantitative-finance
- trading-strategies
- mean-reversion
- market-neutral
- statistical-arbitrage
title: Pairs Trading
updated: '2026-06-20T01:03:51Z'
schema_version: 2
uuid: d6c35139-7340-5e64-aa41-2373a885461f
content_hash: sha256:bb51b839dcea5287f1450c67d11f03e52624db44e211cca9e3009c173b3d4e21
---

<!-- AUTHORED REGION START -->
## Definition

Pairs trading is a market-neutral [[concepts/statistical-arbitrage|statistical arbitrage]] strategy that involves taking simultaneous long and short positions in two related securities. The strategy profits from temporary deviations in the price relationship between the pair, assuming mean reversion.

## Historical Origin

Pairs trading was pioneered by Nunzio Tartaglia's quantitative trading group at Morgan Stanley in the mid-1980s. The team, comprising physicists, mathematicians, and computer scientists, developed statistical methods to identify and exploit temporary mispricings between related stocks.

## Strategy Mechanics

### Basic Concept

1. **Pair Selection**: Identify two assets with historical price co-movement
2. **Spread Construction**: Calculate spread = Price_A - gamma * Price_B
3. **Signal Generation**: Monitor spread for significant deviations
4. **Position Taking**:
   - If spread too high: Short A, Long B
   - If spread too low: Long A, Short B
5. **Exit**: Close positions when spread reverts to normal

### Hedge Ratio (gamma)

The hedge ratio determines position sizes:
- Simple ratio: gamma = 1
- Price ratio: gamma = Price_A / Price_B
- Regression-based: gamma from OLS or Kalman filter
- Cointegration vector: from Johansen test

## Pair Selection Methods

### Distance Method (Gatev et al. 2006)
- Normalize price series
- Compute sum of squared deviations (SSD)
- Select pairs with minimum SSD

### Cointegration Method
- Test for [[concepts/cointegration|cointegration]] relationship
- Pairs with stable long-run equilibrium
- Error correction mechanism for mean reversion

### Statistical Properties
- Correlation analysis
- Sector/industry matching
- Fundamental similarity (same business model)

## Trading Rules

### Entry Signals

| Approach | Entry Condition |
|----------|-----------------|
| Z-score | \|z\| > threshold (e.g., 2) |
| Bollinger Bands | Spread outside bands |
| Probability-based | P(reversion) > threshold |
| Half-life based | Expected profit > transaction costs |

### Exit Signals

- Spread crosses zero (mean)
- Time limit reached
- Stop-loss triggered
- Reverse signal (opposite threshold)

## Kalman Filter Applications

State-space models enhance pairs trading:

1. **Dynamic Hedge Ratio**: Time-varying beta estimation ([[sources/montana-2009-flexible-least-squares|Montana et al. 2009]])

2. **Conditional Probabilities**: P(spread crosses mean in k steps) ([[sources/moura-2016-pairs-trading-kalman|de Moura et al. 2016]])

3. **Mean-Reversion Monitoring**: Detect regime changes ([[sources/triantafyllopoulos-2011-mean-reverting-spreads|Triantafyllopoulos & Montana 2011]])

4. **Heteroscedasticity**: Position sizing based on volatility ([[sources/zhang-2021-pairs-general-ssm|Zhang 2021]])

## Mathematical Framework

### Spread Definition
```
S_t = P_A,t - gamma * P_B,t
```

### Mean-Reverting Dynamics
```
dS_t = kappa * (mu - S_t) * dt + sigma * dW_t
```
- kappa: Speed of mean reversion
- mu: Long-term mean
- sigma: Volatility

### Half-Life
```
H = ln(2) / kappa
```
Time for spread to revert halfway to mean.

## Practical Considerations

### Transaction Costs
- Bid-ask spreads
- Commissions
- Market impact
- Borrowing costs for short positions

### Risk Management
- Maximum position size
- Stop-loss levels
- Sector exposure limits
- Correlation monitoring

### Implementation
- Real-time data feeds
- Order management systems
- Execution algorithms
- Performance monitoring

## Empirical Evidence

| Study | Market | Result |
|-------|--------|--------|
| Gatev et al. (2006) | US equities | 11% annualized excess return |
| [[sources/he-2023-hf-pairs-chinese-futures\|He et al. (2023)]] | Chinese futures | 81% in-sample, 21% out-of-sample |
| [[sources/zhang-2021-pairs-general-ssm\|Zhang (2021)]] | US stocks/ETFs | Up to 32% with advanced models |

## Related Concepts

- [[concepts/cointegration|Cointegration]] for pair selection
- [[concepts/mean-reversion|Mean Reversion]] underlying assumption
- [[concepts/kalman-filter|Kalman Filter]] for dynamic estimation
- [[concepts/spread|Spread]] as trading instrument

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/halls-moore-advanced-algorithmic-trading]]
<!-- AUTHORED REGION END -->
