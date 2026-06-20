---
title: Limit Order Book
page_id: concepts/limit-order-book
page_type: concept
revision_id: 3
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- market-microstructure
- trading
- order-flow
- price-discovery
- liquidity
sources:
- sources/xu-2020-mlofi
- sources/ellersgaard-2018-hedge-tracking-lob
- sources/wang-2018-cross-responses
- sources/brigida-2019-trade-intensity-liquidity
- sources/abergel-2017-algorithmic-trading-lob
- sources/gould-2016-long-memory-fx
- sources/cartea-2015-optimal-execution
- sources/lokin-2024-fill-probabilities
- sources/cartea-2025-statistical-predictions-trading
related:
- concepts/market-making
- concepts/optimal-execution
- concepts/fill-probability
- concepts/avellaneda-stoikov-model
- concepts/inventory-risk
- entities/alvaro-cartea
- entities/sebastian-jaimungal
mind_map_priority: high
schema_version: 2
uuid: 59895ea7-0832-5d8e-954f-6ecf3a13fb11
content_hash: sha256:3fe4706a6ab3fb4c61f338959efc13f764645e0e983c809383bfa4d64dd3fb7c
---

<!-- AUTHORED REGION START -->
# Limit Order Book

A **Limit Order Book (LOB)** is the fundamental data structure used in modern electronic markets to organize and match buy and sell orders. It maintains a real-time record of all outstanding limit orders, sorted by price and time priority.

## Core Mechanics

### Order Types
- **Limit Order:** Commitment to buy/sell at a specified price or better
- **Market Order:** Immediate execution at best available price
- **Cancellation:** Withdrawal of an active limit order

### Order Matching
- **Price-Time Priority:** Orders matched first by price, then by arrival time
- **Best Bid/Ask:** Highest buy price and lowest sell price define the spread
- **Mid-Price:** Average of best bid and best ask

### Book Structure
```
Ask Side (Sells):
Level 3: Price $101.50 | Volume 500
Level 2: Price $101.25 | Volume 300
Level 1: Price $101.00 | Volume 200  <- Best Ask

--- Spread (25 cents) ---

Level 1: Price $100.75 | Volume 150  <- Best Bid
Level 2: Price $100.50 | Volume 400
Level 3: Price $100.25 | Volume 600
Bid Side (Buys)
```

## Key Quantities

### Spread Measures
- **Quoted Spread:** Best ask - best bid
- **Effective Spread:** 2 × |trade price - mid-price|
- **Realized Spread:** Spread after accounting for price movement

### Depth Measures
- **Level-1 Depth:** Volume at best bid/ask
- **Multi-Level Depth:** Volume across multiple price levels
- **Total Depth:** Aggregate volume in entire book

### Order Flow Imbalance
- **OFI:** Net order flow at best bid/ask (Cont et al., 2014)
- **MLOFI:** Multi-level extension capturing deep book activity [[sources/xu-2020-mlofi|Xu et al. (2020)]]

## Price Formation

The LOB is central to understanding how prices form:

1. **Supply-Demand Balance:** Prices adjust to clear order imbalances
2. **Information Aggregation:** Orders reveal trader beliefs
3. **Liquidity Provision:** Market makers post quotes to profit from spread

### Price Impact
- **Temporary Impact:** Immediate price change from order execution
- **Permanent Impact:** Long-term price shift reflecting information
- **Self vs Cross Impact:** Own-stock vs cross-stock effects [[sources/wang-2018-cross-responses|Wang & Guhr (2018)]]

## Market Microstructure Research

### Stylized Facts
- Order arrivals cluster in time
- Order flow exhibits long memory [[sources/gould-2016-long-memory-fx|Gould et al. (2016)]]
- Trade signs are positively autocorrelated
- Deep LOB activity affects prices [[sources/xu-2020-mlofi|Xu et al. (2020)]]

### Trading Applications
- **Market Making:** Optimal quote placement [[sources/ellersgaard-2018-hedge-tracking-lob|Ellersgaard & Tegner (2018)]]
- **Execution:** Minimize market impact
- **HFT:** Exploit microstructure patterns [[sources/brigida-2019-trade-intensity-liquidity|Brigida & Pratt (2019)]]

## LOB Data Sources

### Equity Markets
- **LOBSTER:** NASDAQ Level 3 data (nanosecond precision)
- **TAQ:** NYSE trades and quotes
- **Direct feeds:** Exchange-specific data

### FX Markets
- **EBS:** FX spot trading
- **Hotspot FX:** Multi-institution platform [[sources/gould-2016-long-memory-fx|Gould et al. (2016)]]

### Futures Markets
- **CME FIX/FAST:** Millisecond-timestamped messages [[sources/brigida-2019-trade-intensity-liquidity|Brigida & Pratt (2019)]]

## Theoretical Models

### Queue Models
- Queuing theory for order flow
- Hawkes processes for self-exciting arrivals
- Zero-intelligence models

### Agent-Based Models
- Strategic market makers
- Informed vs noise traders
- High-frequency vs low-frequency participants

## Optimal Execution in LOB

[[sources/cartea-2015-optimal-execution|Cartea & Jaimungal (2015)]]:
- Mixed limit and market order strategies
- Queue position affects [[concepts/fill-probability|fill probability]]
- Inventory-dependent switching rules

[[sources/lokin-2024-fill-probabilities|Lokin & Yu (2024)]]:
- Sophisticated fill probability models
- Queue dynamics and survival analysis
- Empirical calibration methods

## See Also

- [[concepts/market-making|Market Making]]
- [[concepts/optimal-execution|Optimal Execution]]
- [[concepts/fill-probability|Fill Probability]]
- [[concepts/avellaneda-stoikov-model|Avellaneda-Stoikov Model]]
- [[concepts/inventory-risk|Inventory Risk]]
- [[entities/alvaro-cartea|Alvaro Cartea]]
- [[entities/sebastian-jaimungal|Sebastian Jaimungal]]
- [[sources/abergel-2017-algorithmic-trading-lob|Abergel (2017) Algorithmic Trading]]
- [[sources/cartea-2025-statistical-predictions-trading|Cartea et al. (2025) Statistical Predictions of Trading Strategies]] — algorithm-level order-flow prediction in Euronext Amsterdam LOB

<!-- AUTHORED REGION END -->
