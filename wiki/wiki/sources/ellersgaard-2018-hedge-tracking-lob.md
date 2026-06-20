---
title: Optimal Hedge Tracking Portfolios in a Limit Order Book
page_id: sources/ellersgaard-2018-hedge-tracking-lob
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Simon Ellersgaard
- Martin Tegner
year: 2018
venue: Market Microstructure and Liquidity
tags:
- delta-hedging
- limit-order-book
- hjb-qvi
- optimal-control
- market-making
- transaction-costs
- options
related:
- concepts/limit-order-book
- concepts/market-making
- concepts/delta-hedging
- concepts/optimal-control
- sources/avellaneda-2008-market-making
mind_map_priority: high
schema_version: 2
uuid: 582eca82-d917-5bd5-adb0-64218f01115c
content_hash: sha256:0fb9ddc924ea54a40abfc99b4c160f589013ffd41fd752e1030c9f5fe3d4bcc1
---

<!-- AUTHORED REGION START -->
# Optimal Hedge Tracking Portfolios in a Limit Order Book

**Authors:** Simon Ellersgaard, Martin Tegner

**Year:** 2018

**Venue:** Market Microstructure and Liquidity, Vol. 3, No. 2

**Institutions:** University of Copenhagen, University of Oxford (Mathematical Institute, Oxford-Man Institute)

## Summary

This paper develops an optimal control framework for derivative hedging through a limit order book. The authors propose a model for a wealth-optimizing option seller who hedges using a combination of limit and market orders while tracking a targeted delta strategy (Bachelierian). The problem is formulated as a Hamilton-Jacobi-Bellman quasi-variational inequality (HJB QVI) and solved numerically.

## Key Contributions

### 1. Limit-Market Order Duality for Hedging
- Novel integration of hedging with LOB trading
- Limit orders: slow but cost-effective
- Market orders: quick but costly
- Optimal switching between order types

### 2. HJB QVI Formulation
- Three-dimensional control problem
- Dimensional reduction via linear utility ansatz
- Finite difference numerical scheme
- Proven monotone, stable, and consistent

### 3. Optimal Trade Regions
- "No trade" regions surrounding target delta
- Market buy/sell surfaces define intervention boundaries
- Surfaces converge at option maturity
- Stock-inventory path constrained between surfaces

## Methodology

### Market Model
- Mid-price follows compound Poisson process
- Bid-ask spread time-dependent
- Market orders arrive as inhomogeneous Poisson process
- Limit order execution probability: exp(-κ × spread)

### Control Problem
- Linear utility from terminal wealth
- Quadratic penalization for deviation from target hedge
- Parameter φ captures "readiness" to deviate from delta
- Supremum over limit order spreads and market order stopping times

### Numerical Solution
- Explicit finite difference scheme
- Monotonicity condition: 2λΔt ≤ 1
- Backward iteration from terminal condition
- Similar to American option pricing algorithms

## Key Findings

1. Combined limit-market strategy outperforms naive market-order-only hedging
2. Mean return improved, variance reduced
3. Limit orders placed when close to target delta
4. Market orders triggered when significantly off-target
5. Trading regions shrink as maturity approaches

## Simulation Results

### Performance Comparison (single path example)
| Strategy | Market Orders | Limit Orders | Avg Spread |
|----------|--------------|--------------|------------|
| Naive (market only) | 216 | 0 | N/A |
| Optimal (combined) | 37 | 30 | 2.79 |

### Statistical Properties (10,000 simulations)
- Portfolio return mean: 1.0048 (combined) vs 0.9445 (naive)
- Standard deviation significantly reduced
- Welch t-test rejects equal means at 99% level

## Theoretical Contributions

### Weak Convergence Result
- Jump dynamics converges to Bachelier dynamics in infinite intensity limit
- Justifies Bachelierian delta as tracking target
- Connects discrete LOB dynamics to continuous models

### Numerical Scheme Properties
- Monotonicity ensures stability
- Consistency with viscosity solution
- Convergence modulo comparison principle

## See Also

- [[concepts/limit-order-book|Limit Order Book]]
- [[concepts/market-making|Market Making]]
- [[concepts/delta-hedging|Delta Hedging]]
- [[concepts/optimal-control|Optimal Control]]
- [[sources/avellaneda-2008-market-making|Avellaneda & Stoikov (2008)]]

<!-- AUTHORED REGION END -->
