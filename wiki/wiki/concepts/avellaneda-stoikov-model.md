---
title: "Avellaneda-Stoikov Model"
page_id: concepts/avellaneda-stoikov-model
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [market-making, optimal-control, stochastic-control, hjb-equation, inventory-risk]
sources: [sources/bergault-2019-multi-asset-market-making, sources/barzykin-2020-algorithmic-fx-market-making, sources/barzykin-2021-fx-dealer-tiers]
related: [concepts/market-making, concepts/inventory-risk, concepts/optimal-execution, concepts/limit-order-book, entities/olivier-gueant]
---

# Avellaneda-Stoikov Model

## Overview

The **Avellaneda-Stoikov model** (2008) is the foundational continuous-time optimal control framework for market making. It formulates the market maker's problem as choosing optimal bid and ask quotes to maximize expected utility while managing [[concepts/inventory-risk|inventory risk]].

## Model Setup

### Price Dynamics
The mid-price $S_t$ follows arithmetic Brownian motion:
$$dS_t = \sigma dW_t$$

### Order Arrival
Orders arrive as Poisson processes with intensity depending on quote depth:
$$\lambda^{b/a}(\delta) = A e^{-k\delta}$$

where:
- $\delta$ = distance from mid-price (quote depth)
- $A$ = baseline arrival intensity
- $k$ = price sensitivity parameter

### Inventory Dynamics
Inventory $q_t$ evolves with trades:
$$dq_t = dN_t^b - dN_t^a$$

### Objective
Maximize expected CARA utility of terminal wealth:
$$\max_{\delta^b, \delta^a} \mathbb{E}\left[-e^{-\gamma(X_T + q_T S_T)}\right]$$

## Hamilton-Jacobi-Bellman Equation

The value function $V(t, x, q, s)$ satisfies:
$$\partial_t V + \frac{\sigma^2}{2}\partial_{ss}V + \max_{\delta^b}\left[\lambda^b(\delta^b)(V(t, x-s+\delta^b, q+1, s) - V)\right] + \max_{\delta^a}\left[\lambda^a(\delta^a)(V(t, x+s+\delta^a, q-1, s) - V)\right] = 0$$

## Key Results

### Optimal Spread
The optimal half-spread increases with:
- Risk aversion $\gamma$
- Inventory position $|q|$
- Time to horizon (less time = wider spread)

### Quote Skewing
Optimal quotes are skewed based on inventory:
- Long inventory → lower ask (eager to sell)
- Short inventory → lower bid (eager to buy)

### Reservation Price
The indifference price differs from mid-price:
$$r(t, q) = S - q\gamma\sigma^2(T-t)$$

## Extensions

### Guéant Closed-Form Solutions
[[entities/olivier-gueant|Olivier Guéant]] derived tractable approximations making the model practically implementable.

### Cartea-Jaimungal Framework
Risk-adjusted expected PnL with running inventory penalty:
$$\max \mathbb{E}\left[X_T + q_T S_T - \phi \int_0^T q_t^2 dt\right]$$

This is computationally simpler and used in [[sources/cartea-2015-optimal-execution|Cartea & Jaimungal (2015)]].

### Multi-Asset Extension
[[sources/bergault-2019-multi-asset-market-making|Bergault et al. (2019)]]:
- Multiple correlated assets
- Dimensionality reduction via Riccati equations
- Closed-form approximations

### FX Market Making
[[sources/barzykin-2020-algorithmic-fx-market-making|Barzykin et al. (2020)]]:
- Added externalization (hedging) decision
- Markov-modulated Poisson arrival processes
- Client tiering ([[sources/barzykin-2021-fx-dealer-tiers]])

## Practical Considerations

### Parameter Estimation
- $A$, $k$: Fit from historical fill rates
- $\sigma$: Realized volatility
- $\gamma$ or $\phi$: Calibrated to risk limits

### Implementation
- Discretize inventory levels
- Pre-compute optimal quotes for each state
- Real-time lookup during trading

## Limitations

- Assumes no permanent price impact
- Ignores adverse selection (informed traders)
- Poisson arrivals may not capture clustering
- Single-asset focus in original formulation

## See Also

- [[concepts/market-making|Market Making]]
- [[concepts/inventory-risk|Inventory Risk]]
- [[concepts/optimal-execution|Optimal Execution]]
- [[entities/olivier-gueant|Olivier Guéant]]
- [[sources/bergault-2019-multi-asset-market-making|Bergault et al. (2019)]]
