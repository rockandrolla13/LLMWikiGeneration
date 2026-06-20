---
title: Trade Intensity and Liquidity
page_id: sources/brigida-2019-trade-intensity-liquidity
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Matt Brigida
- William Pratt
year: 2019
venue: Market Microstructure and Liquidity
tags:
- high-frequency-trading
- market-making
- liquidity-provision
- natural-gas
- futures-markets
- adverse-selection
- orderbook
related:
- concepts/high-frequency-trading
- concepts/market-making
- concepts/liquidity
- concepts/adverse-selection
- concepts/limit-order-book
mind_map_priority: medium
schema_version: 2
uuid: d688ecd1-8688-5da8-80c9-8ef4a0869d3b
content_hash: sha256:bf379091aedd6eab01d4b591605dd0b1eb3dc4649590dcbf5cf740c4f5a2be4a
---

<!-- AUTHORED REGION START -->
# Trade Intensity and Liquidity

**Authors:** Matt Brigida, William Pratt

**Year:** 2019

**Venue:** Market Microstructure and Liquidity, Vol. 4, Nos. 1&2

**Institutions:** SUNY Polytechnic Institute, Oklahoma City University

## Summary

This paper investigates how liquidity is affected by periods of high trade intensity using millisecond-timestamped orderbook data from CME FIX/FAST messages for natural gas futures. The authors find that HFT liquidity provision increases with orderbook activity and wider bid-ask spreads, but decreases with more trades, consistent with adverse selection concerns.

## Key Contributions

### 1. Millisecond-Resolution Analysis
- Orderbook reconstructed from CME FIX/FAST messages
- Sub-millisecond timestamp precision
- 100ms post-trade window for HFT identification
- Natural gas futures (NG) as study subject

### 2. HFT Liquidity Provision Patterns
- HFT provides more liquidity when orderbook is active
- Wider spreads attract more HFT liquidity provision
- More trades lead to reduced liquidity (adverse selection)
- Liquidity follows liquidity

### 3. Pre-Trade Predictors
- Number of orderbook changes (positive effect on liquidity)
- Average bid-ask spread (positive effect on liquidity)
- Number of trades (negative effect on liquidity)

## Methodology

### Data
- CME Market Depth Data for natural gas futures (ticker: NG)
- September 16-27, 2013 (10 trading days)
- FIX/FAST message encoding
- Orderbook reconstructed to 10 levels deep
- Millisecond timestamps

### HFT Identification
- Based on Hasbrouck and Saar (2013) methodology
- Activity in 100ms window after trade
- Focuses on liquidity-providing HFT subset
- Correlation >0.8 with NASDAQ low-latency identification

### Regression Model
```
ΔL = β₀ + β₁×numC + β₂×avgBA + β₃×numT + ε
```
Where:
- ΔL = change in post-trade liquidity
- numC = number of orderbook changes
- avgBA = average bid-ask spread
- numT = number of trades

### Analysis Design
- 30 different pre-trade intervals (100ms to 3000ms)
- 100 different post-trade intervals (1ms to 100ms)
- 18,000 regressions per trading day
- Separate analysis for buy/sell trades

## Key Results

### Orderbook Changes
| Finding | Frequency | Interpretation |
|---------|-----------|----------------|
| Positive relationship | 7/10 days | Liquidity follows liquidity |
| No relationship | 2/10 days | Neutral |
| Negative relationship | 1/10 days | Rare exception |

### Trade Count
| Finding | Frequency | Interpretation |
|---------|-----------|----------------|
| Negative relationship | 5/10 days | Adverse selection |
| No relationship | 5/10 days | Neutral |
| Positive relationship | 0/10 days | Never observed |

### Bid-Ask Spread
| Finding | Frequency | Interpretation |
|---------|-----------|----------------|
| Positive relationship | 7/10 days | HFT attracted by profit opportunity |
| No relationship | 1/10 day | Neutral |
| Mixed/negative | 2/10 days | Context-dependent |

## Implications

1. **Market Stability:** HFT reduces liquidity after many trades, confirming concerns about flash crashes
2. **Liquidity Dynamics:** Liquidity provision is conditional on recent orderbook activity
3. **Adverse Selection:** Private information in trades causes market makers to withdraw
4. **Market Making:** HFT lacks affirmative obligation to provide liquidity like traditional market makers

## Theoretical Framework

### Kyle (1985) Connection
- Informed traders only trade if profitable
- Many trades signal informed trading
- Market makers reduce liquidity to avoid adverse selection

### Consistent with:
- Hendershott and Riordan (2013): Algorithmic traders react faster when liquidity is low
- Biais et al. (1995): Liquidity offering increases when spread widens
- Hasbrouck and Saar (2013): Low-latency trading methodology

## See Also

- [[concepts/high-frequency-trading|High-Frequency Trading]]
- [[concepts/market-making|Market Making]]
- [[concepts/liquidity|Liquidity]]
- [[concepts/adverse-selection|Adverse Selection]]
- [[concepts/limit-order-book|Limit Order Book]]

<!-- AUTHORED REGION END -->
