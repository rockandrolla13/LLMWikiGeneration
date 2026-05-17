---
title: "Algorithmic market making in foreign exchange cash markets"
page_id: sources/barzykin-2020-algorithmic-fx-market-making
page_type: source
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [market-making, fx, foreign-exchange, internalization, externalization, viscosity-solutions, stochastic-control]
authors: [Alexander Barzykin, Philippe Bergault, Olivier Guéant]
year: 2020
related: [concepts/market-making, concepts/internalization-externalization, concepts/inventory-risk, concepts/avellaneda-stoikov-model, entities/olivier-gueant, entities/philippe-bergault, entities/alexander-barzykin]
---

# Algorithmic market making in foreign exchange cash markets

## Summary

This foundational paper introduces the concept of **active market making** where dealers can not only set quotes but also actively trade in liquidity pools. This extends the [[concepts/avellaneda-stoikov-model]] framework to capture the reality of FX cash markets where market makers have access to dealer-to-dealer (D2D) platforms.

## Key Innovation: Active Trading

Unlike previous OTC market making models where dealers only set quotes and wait for clients, this model allows:
- Continuous trading in liquidity pools
- Trading rate as an additional control variable
- Execution costs and permanent market impact from active trading

## The Internalization Threshold

The paper's main contribution is proving the existence of a **pure internalization zone**:

> "In a certain inventory range the market maker does not actually want to capitalize on this active trading opportunity but should rather 'internalize' the flow by appropriately adjusting the quotes."

The larger the market making franchise, the wider the inventory range suitable for [[concepts/internalization-externalization|internalization]].

## Model Framework

**Price dynamics with market impact:**
$$dS_t = \sigma dW_t + k w_t dt$$

where:
- $w_t$ is the trading rate in the liquidity pool
- $k$ is the permanent market impact parameter

**Execution costs:** Modeled via a penalty function $L(w)$ satisfying convexity conditions

**Inventory constraints:** Hard constraints on inventory range $[-\tilde{q}, \tilde{q}]$

## Mathematical Analysis

The paper:
1. Formulates the stochastic optimal control problem
2. Characterizes the value function as the unique continuous viscosity solution
3. Derives a Partial Integro-Differential Equation (PIDE) of Hamilton-Jacobi type
4. Provides numerical illustrations for USDCNH spot market

## Numerical Results

Using realistic parameters for USDCNH:
- Clear identification of internalization vs. externalization regions
- Optimal quote skewing behavior as function of inventory
- Trade-off between execution costs and market impact

## Related Sources

- [[sources/barzykin-2021-fx-dealer-tiers]] - Extension with client tiering
- [[sources/barzykin-2022-multi-currency-inventory]] - Multi-currency extension

## Citation

Barzykin, A., Bergault, P., & Guéant, O. (2020). Algorithmic market making in foreign exchange cash markets: a new model for active market makers.
