---
title: "Inventory Risk"
page_id: concepts/inventory-risk
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [market-making, risk-management, optimal-control, hedging]
sources: [sources/bergault-2019-multi-asset-market-making, sources/barzykin-2020-algorithmic-fx-market-making, sources/barzykin-2021-fx-dealer-tiers, sources/barzykin-2022-multi-currency-inventory, sources/barzykin-2024-precious-metals, sources/cartea-2015-optimal-execution]
related: [concepts/market-making, concepts/avellaneda-stoikov-model, concepts/internalization-externalization, concepts/optimal-execution, entities/olivier-gueant]
---

# Inventory Risk

## Overview

**Inventory risk** is the risk that a market maker's accumulated position (inventory) will lose value due to adverse price movements. It is the central risk in [[concepts/market-making|market making]] and drives optimal quote placement strategies.

## Sources of Inventory Risk

### Price Volatility
- Inventory gains/loses value as prices move
- Higher volatility → higher inventory risk
- Scales with position size and holding period

### Order Flow Imbalance
- Persistent one-sided flow builds inventory
- May signal informed trading (adverse selection)
- Creates correlation between inventory and future price moves

### Hedging Costs
- Closing positions incurs transaction costs
- Urgency to reduce inventory → worse execution
- Trade-off between holding risk and liquidation cost

## Mathematical Framework

### Value at Risk
For inventory $q$ with price volatility $\sigma$:
$$\text{VaR}_{1-\alpha}(q) = q \cdot z_\alpha \cdot \sigma \cdot \sqrt{\Delta t}$$

### Running Inventory Penalty
In the [[concepts/avellaneda-stoikov-model|Avellaneda-Stoikov model]] and extensions, inventory risk is penalized via:

**CARA Utility:**
$$U(W) = -e^{-\gamma W}$$ where $\gamma$ = risk aversion

**Running Penalty (Cartea-Jaimungal):**
$$\phi \int_0^T q_t^2 \, dt$$

This quadratic penalty discourages large positions without requiring utility specification.

## Inventory Management Strategies

### Quote Skewing
Adjust quotes based on inventory position:
- **Long inventory**: Lower ask to encourage selling
- **Short inventory**: Lower bid to encourage buying

From [[sources/barzykin-2021-fx-dealer-tiers|Barzykin et al. (2021)]]:
$$\delta^{a*}(q) = \delta^{b*}(q) + 2\gamma\sigma^2(T-t)q$$

### Inventory Limits
Hard constraints on maximum position:
- Position limits by asset
- Portfolio-level VaR limits
- Concentration limits

### Hedging (Externalization)
Active risk reduction via external market:
- [[concepts/internalization-externalization|Internalization vs externalization]] decision
- Optimal timing of hedge trades
- [[sources/barzykin-2020-algorithmic-fx-market-making]]: When to hedge in FX

## Multi-Asset Inventory

### Correlation Effects
Correlated assets provide natural hedging:
- Long asset A, short correlated asset B → reduced net risk
- [[sources/barzykin-2022-multi-currency-inventory]]: Multi-currency FX portfolios
- [[sources/barzykin-2024-precious-metals]]: Cointegrated gold/silver positions

### Portfolio-Level Constraints
- Aggregate VaR across positions
- Cross-asset margining
- Dimensionality challenges in large portfolios

### Closed-Form Solutions
[[sources/bergault-2019-multi-asset-market-making|Bergault et al. (2019)]]:
- Riccati equation approach
- Approximations for high-dimensional problems
- Monte-Carlo validation

## Empirical Observations

### Inventory Half-Life
How quickly market makers reduce positions:
- HFT: Seconds to minutes
- Traditional dealers: Hours to days
- Depends on market liquidity and risk tolerance

### Inventory-Price Relationship
- Market makers skew quotes → inventory predicts short-term returns
- Information content of dealer positions
- [[sources/barzykin-2021-fx-dealer-tiers]]: Client-specific inventory dynamics

## See Also

- [[concepts/market-making|Market Making]]
- [[concepts/avellaneda-stoikov-model|Avellaneda-Stoikov Model]]
- [[concepts/internalization-externalization|Internalization vs Externalization]]
- [[concepts/optimal-execution|Optimal Execution]]
- [[concepts/adverse-selection|Adverse Selection]]
