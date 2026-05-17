---
title: "RFQ Markets"
page_id: concepts/rfq-markets
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [market-structure, fixed-income, fx, trading, dealer-markets]
sources: [sources/bergault-2023-rfq-pricing, sources/fermanian-2017-md2c-corporate-bonds, sources/gueant-2019-particle-filtering-bonds]
related: [concepts/market-making, concepts/adverse-selection, entities/olivier-gueant, entities/philippe-bergault]
---

# RFQ Markets

## Overview

**Request-for-Quote (RFQ)** markets are trading venues where clients request prices from one or more dealers rather than submitting orders to a central limit order book. This market structure dominates in corporate bonds, FX options, swaps, and other OTC products.

## Market Structure

### RFQ Process
1. **Client Request**: Specify instrument, size, direction (buy/sell)
2. **Dealer Response**: Each queried dealer provides a price
3. **Client Decision**: Accept best quote, negotiate, or walk away
4. **Execution**: Trade at agreed price

### Key Features
- **Dealer Competition**: Multiple dealers quote simultaneously
- **Information Asymmetry**: Dealer learns client intent
- **Customization**: Can trade exact desired quantity
- **Relationship**: Pricing reflects ongoing business

## Types of RFQ Platforms

### Multi-Dealer-to-Client (MD2C)
- Client sees quotes from multiple dealers
- Competition drives tighter spreads
- Examples: MarketAxess, Tradeweb, Bloomberg

### Single-Dealer Platform
- Client trades with preferred dealer
- Relationship pricing
- Lower information leakage

### All-to-All
- Any participant can provide liquidity
- Blurs dealer/client distinction
- Growing in corporate bonds

## Mathematical Models

### [[sources/fermanian-2017-md2c-corporate-bonds|Fermanian et al. (2017)]]

**Dealer Competition Model:**
- $N$ dealers receive RFQ
- Each quotes price $p_i$
- Client has reservation value $V$

**Dealer's Problem:**
$$\max_{p_i} (p_i - c_i) \cdot P(\text{win} | p_i)$$

where $c_i$ = dealer's cost (inventory, hedging, etc.)

**Equilibrium:**
- Dealers shade quotes above cost
- More competitors → tighter spreads
- Winner's curse considerations

### [[sources/bergault-2023-rfq-pricing|Bergault et al. (2023)]]

**RFQ Impact and Liquidity:**
- RFQ activity affects market liquidity
- Information in RFQ flow
- Dynamic pricing across sequential RFQs

**Fair Transfer Price:**
Price at which informed and uninformed flow have equal expected value:
$$p^* = \mathbb{E}[S_T | \text{information set}]$$

## Mid-Price Estimation

A critical challenge in RFQ markets: determining fair value when no continuous price exists.

### CBBT (Composite Bloomberg Bond Trader)
- Aggregates dealer quotes
- Widely used benchmark
- May be stale in fast markets

### Particle Filtering
[[sources/gueant-2019-particle-filtering-bonds]]:
- Sequential Monte Carlo for latent price
- Handles censored observations (rejected RFQs)
- Real-time distribution updates

### Cross-Sectional Models
- Price relative to similar bonds
- Factor model approach
- Credit curve interpolation

## Practical Considerations

### Information Leakage
- RFQ reveals client's intent
- Dealers may front-run or adjust quotes
- Trade-off: competition vs. information cost

### Dealer Selection
- Query too many → information leakage
- Query too few → worse prices
- Optimal: 3-5 dealers for most products

### Trade Size
- Large trades get wider spreads
- Information content of size
- May need to work order over time

### Timing
- Market conditions affect spreads
- Around announcements: wider
- End of day: wider

## Corporate Bond RFQ

### Market Characteristics
- Highly fragmented: ~1M ISINs
- Low liquidity per bond
- Inventory costs high for dealers

### Pricing Challenges
- Many bonds don't trade daily
- Credit risk assessment
- Duration and curve risk

### Electronic Evolution
- Growing share via platforms
- Still significant voice trading
- Hybrid workflows common

## FX Options RFQ

### Characteristics
- Standardized but OTC
- Multiple strike/expiry combinations
- Volatility surface implications

### Pricing
- Black-Scholes + vol surface
- Skew and term structure
- Hedging cost in bid-ask

## See Also

- [[concepts/market-making|Market Making]]
- [[concepts/adverse-selection|Adverse Selection]]
- [[entities/olivier-gueant|Olivier Guéant]]
- [[sources/bergault-2023-rfq-pricing|Bergault et al. (2023)]]
- [[sources/fermanian-2017-md2c-corporate-bonds|Fermanian et al. (2017)]]
