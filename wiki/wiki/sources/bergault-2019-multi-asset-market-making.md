---
title: "Closed-form approximations in multi-asset market making"
page_id: sources/bergault-2019-multi-asset-market-making
page_type: source
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [market-making, multi-asset, stochastic-control, closed-form, avellaneda-stoikov]
authors: [Philippe Bergault, David Evangelista, Olivier Guéant, Douglas Vieira]
year: 2019
related: [concepts/market-making, concepts/avellaneda-stoikov-model, concepts/inventory-risk, concepts/stochastic-optimal-control, entities/olivier-gueant, entities/philippe-bergault]
---

# Closed-form approximations in multi-asset market making

## Summary

This paper addresses the computational challenge of implementing [[concepts/market-making]] algorithms for portfolios of multiple assets. While the [[concepts/avellaneda-stoikov-model]] and its extensions provide a solid theoretical foundation for optimal quoting, the numerical computation of value functions and optimal quotes becomes intractable as the number of assets increases due to the curse of dimensionality.

The authors propose **closed-form proxy approximations** for the value function by replacing the original Hamilton-Jacobi equation with a simpler one that admits analytical solutions. These approximations capture the essential financial effects while remaining computationally tractable.

## Key Contributions

- **Closed-form value function proxies**: The paper derives analytical approximations that can be computed without numerical schemes
- **Interpretable quoting strategies**: The resulting optimal quotes have closed-form expressions that reveal the influence of model parameters
- **Multiple applications**: The proxies can serve as:
  1. Heuristic evaluation functions
  2. Initial value functions for reinforcement learning
  3. Direct quoting strategies via a greedy approach
- **Extensions to practical cases**: The framework covers drift in prices, client tiering, multiple request sizes, and fixed transaction costs

## Model Framework

The model extends the [[concepts/avellaneda-stoikov-model]] to multiple correlated assets where:
- Asset prices follow correlated geometric Brownian motions
- Transaction intensities depend on the distance between quotes and reference prices
- The market maker maximizes expected CARA utility (Model A) or risk-adjusted expected P&L (Model B)

The Hamilton-Jacobi equation characterizing the value function is approximated by another equation whose solution can be computed in closed form.

## Notable Quotes

> "Having a proxy of a value function is known to be useful in the community of reinforcement learning... An important use of a closed-form proxy of a value function is as a heuristic evaluation function."

## Related Concepts

- [[concepts/inventory-risk]] - Central to the market maker's optimization problem
- [[concepts/bid-ask-spread]] - Determined by the optimal quoting strategy
- [[concepts/stochastic-optimal-control]] - Mathematical framework for the optimization

## Citation

Bergault, P., Evangelista, D., Guéant, O., & Vieira, D. (2019). Closed-form approximations in multi-asset market making. *Applied Mathematical Finance*.
