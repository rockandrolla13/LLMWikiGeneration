---
content_hash: sha256:f89721a8c6ecf3a592af588980d3f6afd8e41a2aebdff5484dabcc92359ae55c
created: 2026-04-26 03:00:00+00:00
page_id: concepts/optimal-execution
page_type: concept
related:
- concepts/market-making
- concepts/limit-order-book
- concepts/inventory-risk
- entities/alvaro-cartea
- entities/sebastian-jaimungal
revision_id: 1
schema_version: 2
sources:
- sources/cartea-2015-optimal-execution
- sources/lokin-2024-fill-probabilities
- sources/anantha-2025-event-time-anchor-selection-multi-contract
- sources/bacidore-2012-cluster-analysis-evaluating-trading-strategies
- sources/besson-2016-cross-or-not-cross-spread-that
- sources/ferreira-2020-machine-learning-algorithmic-trading-leading-reinforced
- sources/lehalle-2019-incorporating-signals-into-optimal-trading
- sources/lipton-2013-trade-arrival-dynamics-quote-imbalance-limit
- sources/mans-2025-en-lokalt-konkav-och-transient-prispaverkningsmodell
- sources/rubisov-2015-statistical-arbitrage-limit-order-book-imbalance
- sources/stoikov-2016-reducing-transaction-costs-low-latency-trading
- sources/wurzer-2026-execution-alpha-intraday-liquidity-provision-versus
tags:
- algorithmic-trading
- market-impact
- stochastic-control
- transaction-costs
title: Optimal Execution
updated: '2026-09-27T01:47:00Z'
uuid: 6305caf8-be81-5252-9dc9-8c625ccf5722
---

<!-- AUTHORED REGION START -->
# Optimal Execution

## Overview

**Optimal execution** is the problem of trading a large position while minimizing transaction costs, primarily market impact. It is the dual problem to [[concepts/market-making|market making]]: market makers provide liquidity, while optimal execution consumes it.

## The Execution Problem

### Objective
Trade quantity $Q$ over horizon $[0, T]$ to minimize:
$$\mathbb{E}\left[\text{Implementation Shortfall}\right] + \lambda \cdot \text{Var}[\text{Cost}]$$

where implementation shortfall = difference between execution price and arrival price.

### Trade-offs
- **Speed vs Cost**: Fast execution → high impact; slow → timing risk
- **Certainty vs Optimality**: Market orders guarantee fills; limit orders may miss
- **Passive vs Aggressive**: Limit orders save spread but face fill risk

## Order Types

### Market Orders
- Immediate execution at best available price
- Guaranteed fill but incurs spread
- Creates immediate price impact

### Limit Orders
- Execute only at specified price or better
- No spread cost but uncertain fill
- Risk of missing execution if price moves away

### Mixed Strategies
[[sources/cartea-2015-optimal-execution|Cartea & Jaimungal (2015)]] showed optimal strategies combine both:
- **Limit orders**: Passive liquidity provision during execution
- **Market orders**: Aggressive completion near deadline or adverse moves
- **Trigger boundaries**: Inventory-dependent switching rules

## Mathematical Framework

### Almgren-Chriss Model
Classic deterministic framework:
- Linear temporary impact: $\Delta p = \eta \cdot v$ (rate of trading)
- Linear permanent impact: $\Delta p = \gamma \cdot \Delta q$ (quantity traded)
- Optimal trajectory: Time-weighted interpolation between TWAP and immediate

### Stochastic Optimal Control
[[sources/cartea-2015-optimal-execution]]: HJB equation approach with:

**State Variables:**
- $t$: time
- $q$: remaining quantity
- $S$: asset price
- $Y$: limit order queue position (optional)

**Controls:**
- $\nu^+$: rate of market buy orders
- $\nu^-$: rate of market sell orders
- $\ell^b, \ell^a$: limit order quantities

**Value Function:**
$$V(t, q, S) = \sup \mathbb{E}\left[X_T + q_T S_T - \phi \int_0^T q_t^2 dt\right]$$

## Fill Probability

A critical input for limit order strategies:

### Exponential Model
$$P(\text{fill}) = e^{-\kappa \delta}$$
where $\delta$ = depth from best quote

### Queue-Based Models
[[sources/lokin-2024-fill-probabilities|Lokin & Yu (2024)]]:
- Fill depends on queue position
- Order flow dynamics
- Sophisticated survival analysis approach

## Key Results from Cartea-Jaimungal

### Optimal Strategy Structure
1. **Interior region**: Use limit orders, no market orders
2. **Trigger boundaries**: Switch to market orders when inventory extreme
3. **Terminal condition**: Market order to clear remaining position

### Explicit Solutions
For specific parameter choices:
$$\ell^*(t, q) = \frac{\kappa_0 - \phi q}{2\kappa_1}$$

### Practical Insights
- More aggressive (market orders) when:
  - Far from target inventory
  - Close to deadline
  - High urgency parameter $\phi$
- More passive (limit orders) when:
  - Near target inventory
  - Low urgency
  - Wide spreads (limit order advantage)

## Extensions

### Multi-Asset Execution
- Portfolio rebalancing
- Pairs trading execution
- Cross-impact effects

### Adaptive Strategies
- Learning fill probabilities
- Real-time impact estimation
- Reinforcement learning approaches

### Dark Pools
- Hidden liquidity venues
- Optimal routing across lit and dark
- Information leakage concerns

## Connection to Market Making

Optimal execution and market making are related:
- Both involve inventory management
- Both use HJB/stochastic control
- Market maker = "reverse" execution (accumulate then unwind)

[[sources/cartea-2015-optimal-execution]] notes the MM problem is a special case where the agent both buys and sells.

## See Also

- [[concepts/market-making|Market Making]]
- [[concepts/limit-order-book|Limit Order Book]]
- [[concepts/inventory-risk|Inventory Risk]]
- [[entities/alvaro-cartea|Álvaro Cartea]]
- [[entities/sebastian-jaimungal|Sebastian Jaimungal]]
- [[sources/cartea-2015-optimal-execution|Cartea & Jaimungal (2015)]]
- [[sources/lokin-2024-fill-probabilities|Lokin & Yu (2024)]]

<!-- AUTHORED REGION END -->