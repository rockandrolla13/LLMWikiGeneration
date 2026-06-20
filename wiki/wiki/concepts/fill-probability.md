---
title: Fill Probability
page_id: concepts/fill-probability
page_type: concept
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- market-making
- limit-order-book
- optimal-execution
- order-flow
sources:
- sources/lokin-2024-fill-probabilities
- sources/cartea-2015-optimal-execution
related:
- concepts/limit-order-book
- concepts/optimal-execution
- concepts/market-making
- concepts/avellaneda-stoikov-model
schema_version: 2
uuid: ad8f411b-f870-525f-b660-d264f349c639
content_hash: sha256:998402e6283668e5c3f5af414e5c2a056fbeaba8114a2652ff11fade0eb6361d
---

<!-- AUTHORED REGION START -->
# Fill Probability

## Overview

**Fill probability** is the likelihood that a limit order will be executed (filled) before being cancelled. It is a critical input for both [[concepts/market-making|market making]] and [[concepts/optimal-execution|optimal execution]] strategies, as it determines the trade-off between passive (limit) and aggressive (market) orders.

## Importance

### For Market Makers
- Determines expected revenue from quotes
- Affects optimal spread setting
- Key input to [[concepts/avellaneda-stoikov-model|Avellaneda-Stoikov model]]

### For Execution Algorithms
- Trade-off: limit order saves spread but may not fill
- [[sources/cartea-2015-optimal-execution|Cartea & Jaimungal (2015)]]: Mixed strategy depends on fill probability
- Determines when to switch to market orders

## Standard Models

### Exponential Model
Most common assumption in academic literature:
$$\lambda(\delta) = A e^{-k\delta}$$

where:
- $\delta$ = distance from mid-price (depth)
- $A$ = baseline arrival intensity
- $k$ = price sensitivity

**Implied Fill Probability:**
$$P(\text{fill in } [0, T]) = 1 - e^{-\lambda(\delta) T}$$

### Power Law Model
Alternative specification:
$$\lambda(\delta) = A \delta^{-\alpha}$$

Better fits some empirical data, especially at small depths.

## Advanced Approaches

### [[sources/lokin-2024-fill-probabilities|Lokin & Yu (2024)]]

More sophisticated analysis considering:

**Queue Position:**
- Not just depth, but position in queue at that price level
- Earlier queue position → higher fill probability
- Queue dynamics affect expected time to fill

**Order Flow Dynamics:**
- Arrival of market orders on opposite side
- Cancellations ahead in queue
- Price movements that make limit order marketable

**Survival Analysis Framework:**
- Model time-to-fill as survival time
- Hazard rate depends on market conditions
- Censoring: orders cancelled before fill

### Key Results
- Fill probability highly dependent on queue position
- Non-linear relationship with depth
- Significant variation across market conditions

## Empirical Calibration

### Data Requirements
- Limit order submissions with timestamps
- Fill events with timestamps
- Cancellation events
- Market state at submission time

### Estimation Methods
1. **Histogram**: Bin by depth, compute fill fraction
2. **Maximum Likelihood**: Fit parametric model
3. **Machine Learning**: Features include depth, spread, volatility, time of day

### Typical Findings (Equity Markets)
| Depth (bps) | Fill Probability |
|-------------|-----------------|
| 0 (at touch) | 60-80% |
| 5 | 30-50% |
| 10 | 15-30% |
| 20+ | <10% |

## Impact on Optimal Strategies

### Market Making
Higher fill probability at tighter spreads:
- More trades but smaller margin per trade
- Must balance fill rate vs. adverse selection
- [[sources/barzykin-2021-fx-dealer-tiers]]: Tier-specific fill rates

### Optimal Execution
[[sources/cartea-2015-optimal-execution]]:
- Use limit orders when fill probability high enough
- Switch to market orders near deadline
- Inventory-dependent thresholds

### Formula for Critical Depth
Indifferent between limit and market order when:
$$\lambda(\delta^*) \cdot \delta^* = \text{market order cost}$$

## Practical Considerations

### Time Decay
- Fill probability increases with time in queue
- But so does adverse selection risk
- Order staleness is a real concern

### Market Conditions
- Volatility: Higher vol → faster fills but more risk
- Spread: Wider spread → limit order more attractive
- News: Fill probability spikes around events

### Venue Selection
Different venues have different fill characteristics:
- Primary exchange vs. dark pools
- Maker-taker vs. taker-maker fee structure
- Retail vs. institutional venues

## See Also

- [[concepts/limit-order-book|Limit Order Book]]
- [[concepts/optimal-execution|Optimal Execution]]
- [[concepts/market-making|Market Making]]
- [[sources/lokin-2024-fill-probabilities|Lokin & Yu (2024)]]
- [[sources/cartea-2015-optimal-execution|Cartea & Jaimungal (2015)]]

<!-- AUTHORED REGION END -->
