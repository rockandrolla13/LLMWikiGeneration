---
title: Stochastic Optimal Control
page_id: concepts/stochastic-optimal-control
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- optimal-control
- hjb-equation
- market-making
- optimal-execution
sources:
- sources/bergault-2019-multi-asset-market-making
- sources/cartea-2015-optimal-execution
- sources/barzykin-2020-algorithmic-fx-market-making
related:
- concepts/market-making
- concepts/avellaneda-stoikov-model
- concepts/inventory-risk
- concepts/optimal-execution
mind_map_priority: medium
schema_version: 2
uuid: 7fd264a5-bed4-5b79-9838-db985bb0876c
content_hash: sha256:1859194afb30fed2fa0dcf0d6a9d4e40ffa2cc6f5c986693acb16e334f02ceb4
---

<!-- AUTHORED REGION START -->
# Stochastic Optimal Control

Choosing actions over time to maximize an objective when the state evolves randomly. In this wiki it is the mathematical spine of [[concepts/market-making|market making]] and [[concepts/optimal-execution|optimal execution]] — the trader picks quotes or trade rates, the price does what it wants, and the solution comes from a Hamilton-Jacobi-Bellman equation.

## The Standard Setup

The [[concepts/avellaneda-stoikov-model|Avellaneda-Stoikov model]] (2008) is the template. Mid-price follows arithmetic Brownian motion; orders arrive as Poisson processes with intensity A·exp(−k·delta) decaying in quote depth; inventory moves with each fill. The objective is expected CARA utility of terminal wealth, and the value function V(t, x, q, s) satisfies an HJB equation with a maximization over bid and ask depth inside it.

What comes out is interpretable rather than opaque: the optimal half-spread widens with risk aversion, with the size of the inventory, and as the horizon shortens; quotes skew to unwind inventory; and the reservation price sits away from the mid at S − q·gamma·sigma²·(T−t).

The Cartea-Jaimungal variant replaces the utility with a running quadratic inventory penalty, phi·∫q²dt, which is computationally simpler and requires no utility specification. See [[concepts/inventory-risk|Inventory Risk]].

## Execution as the Same Problem

[[sources/cartea-2015-optimal-execution|Cartea & Jaimungal (2015)]] state the execution problem in the same language: state variables are time, remaining quantity, price, and optionally queue position; controls are the rates of market buy and sell orders plus limit order quantities. The output is a set of inventory-dependent trigger boundaries for switching between passive and aggressive orders. The hedging problem in a limit order book takes the further form of an HJB quasi-variational inequality, because orders arrive as impulses rather than flows.

## The Dimensionality Wall

The framework breaks down on portfolios. [[sources/bergault-2019-multi-asset-market-making|Bergault et al. (2019)]] state the problem directly: numerically computing value functions and optimal quotes becomes intractable as the number of assets grows. Their answer is to replace the original Hamilton-Jacobi equation with a simpler one that admits closed-form solutions, giving proxies that can serve as heuristic evaluation functions, as initial value functions for reinforcement learning, or as greedy quoting strategies outright.

[[sources/barzykin-2020-algorithmic-fx-market-making|Barzykin et al. (2020)]] extend the control set rather than reduce it, adding the decision to hedge externally — see [[concepts/internalization-externalization|Internalization vs Externalization]].

## See Also

[[concepts/market-making|Market Making]] · [[concepts/avellaneda-stoikov-model|Avellaneda-Stoikov Model]] · [[concepts/inventory-risk|Inventory Risk]] · [[concepts/optimal-execution|Optimal Execution]] · [[concepts/limit-order-book|Limit Order Book]] · [[entities/olivier-gueant|Olivier Guéant]] · [[entities/philippe-bergault|Philippe Bergault]]

**Not yet written:** `concepts/hamilton-jacobi-bellman`, `concepts/reinforcement-learning`

<!-- AUTHORED REGION END -->
