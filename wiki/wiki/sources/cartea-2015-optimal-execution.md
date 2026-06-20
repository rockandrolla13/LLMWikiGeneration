---
title: Optimal execution with limit and market orders
page_id: sources/cartea-2015-optimal-execution
page_type: source
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- optimal-execution
- limit-orders
- market-orders
- algorithmic-trading
- stochastic-control
authors:
- Álvaro Cartea
- Sebastian Jaimungal
year: 2015
related:
- concepts/optimal-execution
- concepts/limit-order-book
- concepts/market-making
- entities/alvaro-cartea
- entities/sebastian-jaimungal
schema_version: 2
uuid: eea92f79-e746-518c-8a82-9904e4833cef
content_hash: sha256:315b901476d50691c71fa2180dd20a698ad34a9e94ba58958d7e9a006b8c2055
---

<!-- AUTHORED REGION START -->
# Optimal execution with limit and market orders

## Summary

This paper develops an [[concepts/optimal-execution]] strategy that optimally combines limit orders and market orders. Unlike traditional execution models (e.g., Almgren-Chriss) that only use market orders, this framework allows traders to earn the spread through limit orders while using market orders to stay on schedule.

## Key Contributions

- **Mixed order strategy**: Optimal combination of limit and market orders
- **Depth optimization**: Determining how deep in the book to post limit orders
- **Performance improvement**: 1-2.5x the spread savings over Almgren-Chriss

## Model Framework

**Price dynamics:**
$$dS_t = \sigma(dZ_t^+ - dZ_t^-)$$

where $Z_t^\pm$ are Poisson processes representing tick-level price movements.

**Limit order fill probability:** Exponential in depth: $e^{-\kappa\delta_t}$

**Execution intensity:** $\lambda e^{-\kappa\delta_t}$ where $\lambda$ is the market order arrival rate

## Three Strategy Types Analyzed

1. **Strategy (i)**: Choose depth, unit size for both order types
2. **Strategy (ii)**: Post only at best bid/ask, unit size
3. **Strategy (iii)**: Post at best bid/ask, unrestricted volume

## Key Results

- **Trigger boundary**: Market orders executed when inventory deviates too far from target
- **Optimal depth formula:**
$$\delta^*(t,q) = \frac{1}{\kappa} + h(t, q-1) - h(t, q)$$
where $h$ is the value function

- **Average savings**: 1-2.5 times the spread vs. Almgren-Chriss benchmark

## Quasi-Variational Inequality

The value function solves a QVI that determines:
1. When to post limit orders (continuation region)
2. When to execute market orders (stopping times)
3. Optimal depth of limit orders

## Numerical Analysis

Using NASDAQ ITCH data for various liquidity levels:
- Different arrival rates of market orders
- Various target penalty parameters
- Comparison with TWAP and Almgren-Chriss schedules

## Related Concepts

- [[concepts/limit-order-book]] - Market structure
- [[concepts/fill-probability]] - Key input for limit order execution
- [[concepts/market-making]] - Related optimization problem

## Citation

Cartea, Á., & Jaimungal, S. (2015). Optimal execution with limit and market orders. *Quantitative Finance*, 15(8), 1279-1291.

<!-- AUTHORED REGION END -->
