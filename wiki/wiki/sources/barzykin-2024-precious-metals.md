---
title: "Algorithmic Market Making in Spot Precious Metals"
page_id: sources/barzykin-2024-precious-metals
page_type: source
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [market-making, precious-metals, gold, cointegration, ornstein-uhlenbeck, efp-spread, stochastic-control]
authors: [Alexander Barzykin, Philippe Bergault, Olivier Guéant]
year: 2024
related: [concepts/market-making, concepts/cointegration, concepts/inventory-risk, entities/olivier-gueant, entities/philippe-bergault, entities/alexander-barzykin]
---

# Algorithmic Market Making in Spot Precious Metals

## Summary

This paper introduces a novel [[concepts/market-making]] framework for spot precious metals that leverages the **cointegration** between spot and futures prices. The key innovation is modeling the Exchange for Physical (EFP) spread using a **nested Ornstein-Uhlenbeck process** to capture multiple relaxation timescales.

## Key Innovation: Cointegration for Hedging

Unlike standard multi-asset models that assume only correlation, this paper exploits **cointegration**:
- Futures are considerably more liquid than spot (tighter spreads, higher volumes)
- EFP spread is driven by swap rates, which are stable over intraday horizons
- Mean reversion in the EFP spread provides hedging opportunities

## The Nested OU Model

The EFP spread exhibits multiple modes of relaxation:
- Intraday mean reversion (hours)
- Longer-term reversion (days)

This is modeled via nested Ornstein-Uhlenbeck dynamics:
$$dE_t = -k_E(E_t - D_t)dt + \sigma_E dW_t^E$$
$$dD_t = -k_D(D_t - \bar{D})dt + \sigma_D dW_t^D$$

## Model Framework

The spot market maker:
- Streams pricing ladders to clients
- Can hedge in both spot and futures markets
- Faces execution costs and market impact
- Maximizes CARA utility of terminal wealth minus inventory penalty

## Practical Considerations

The paper addresses implementation challenges:
- $D_t$ process is not directly observable
- Can be treated as hyperparameters for confidence modulation
- Or estimated via Bayesian filtering techniques

## Approximation Technique

The method from closed-form approximations papers is adapted:
- Quadratic approximation of Hamiltonian
- Riccati-like equations for value function
- Near real-time strategy optimization

## Numerical Analysis

Focused on the gold market:
- EFP spreads from four active futures contracts
- Demonstration of intraday and weekly mean reversion
- Practical implications for market makers

## Related Sources

- [[sources/barzykin-2022-multi-currency-inventory]] - Similar approximation techniques
- [[sources/bergault-2019-multi-asset-market-making]] - Closed-form approximation methodology

## Citation

Barzykin, A., Bergault, P., & Guéant, O. (2024). Algorithmic Market Making in Spot Precious Metals.
