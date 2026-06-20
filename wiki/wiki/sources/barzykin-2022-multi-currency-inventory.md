---
title: Dealing with multi-currency inventory risk in FX cash markets
page_id: sources/barzykin-2022-multi-currency-inventory
page_type: source
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- market-making
- fx
- multi-currency
- inventory-risk
- riccati-equations
- stochastic-control
authors:
- Alexander Barzykin
- Philippe Bergault
- Olivier Guéant
year: 2022
related:
- concepts/market-making
- concepts/inventory-risk
- concepts/internalization-externalization
- entities/olivier-gueant
- entities/philippe-bergault
- entities/alexander-barzykin
schema_version: 2
uuid: 000a6c91-4d03-5255-9a9c-22cf199f0b2e
content_hash: sha256:88b1e4d93dee8a2e3b320d0bfc3f1faedea532585d7927595914f6eda5b4c1f7
---

<!-- AUTHORED REGION START -->
# Dealing with multi-currency inventory risk in FX cash markets

## Summary

This paper extends [[concepts/market-making]] models to handle the specific challenges of FX dealers who quote multiple currency pairs, including **cross rates**. The key insight is that FX market making differs fundamentally from other asset classes because each currency pair represents a valuation relationship, and crosses introduce both complexity and arbitrage-like opportunities.

## Key Innovation: Cross Rates

The presence of cross rates (non-USD pairs like EURGBP) creates:
- **Complexity**: Multiple ways to achieve the same exposure (e.g., buying EURGBP ≈ buying EURUSD + selling GBPUSD)
- **Opportunities**: Ability to offset risk across correlated pairs
- **Subtle questions**: How should EURGBP spread compare to the sum of leg spreads?

## Mathematical Framework

The model uses inventories measured in reference currency (USD) as state variables:
$$Y_t^i = q_t^i S_t^i$$

This choice enables a tractable formulation where the Hamilton-Jacobi-Bellman equation can be approximated using a **matrix Riccati-like differential equation**. The dimensionality grows only quadratically with the number of currencies (not exponentially with currency pairs).

## Approximation Technique

Following ideas from earlier work, the authors:
1. Approximate Hamiltonian functions with quadratic forms
2. Obtain value function of form: $\theta(t,y) = -y^\top A(t)y - y^\top B(t) - C(t)$
3. Solve the resulting Riccati equation efficiently via Euler scheme

## Numerical Example

The paper illustrates the model with 5 major currencies (USD, EUR, JPY, GBP, CHF), demonstrating:
- How correlated pairs engage through pricing and hedging
- Impact on the [[concepts/internalization-externalization]] dilemma
- Portfolio risk autocorrelation time vs. individual position autocorrelation

## Key Findings

- Observed risk autocorrelation time is much shorter than individual currency pair position autocorrelation
- This leads to cost savings through portfolio-level risk management
- The model is scalable for practical use

## Related Sources

- [[sources/barzykin-2021-fx-dealer-tiers]] - Single currency pair model with tiering
- [[sources/bergault-2019-multi-asset-market-making]] - Closed-form approximations approach

## Citation

Barzykin, A., Bergault, P., & Guéant, O. (2022). Dealing with multi-currency inventory risk in FX cash markets.

<!-- AUTHORED REGION END -->
