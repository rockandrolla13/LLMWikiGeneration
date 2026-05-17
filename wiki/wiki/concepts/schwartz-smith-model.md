---
title: "Schwartz-Smith Model"
page_id: concepts/schwartz-smith-model
page_type: concept
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
tags: [commodities, futures-pricing, term-structure, factor-models]
sources: [sources/he-2024-functional-regression]
related: [concepts/state-space-models, concepts/kalman-filter, concepts/functional-data-analysis]
mind_map_priority: medium
---

# Schwartz-Smith Model

The Schwartz-Smith (2000) model decomposes commodity spot prices into two latent factors: a short-term deviation and a long-term equilibrium price level.

## Model Specification

Log spot price:
$$\ln(S_t) = \chi_t + \xi_t$$

Where:
- $\chi_t$ = Short-term deviation (mean-reverting)
- $\xi_t$ = Long-term equilibrium level (random walk with drift)

### Factor Dynamics

Under the physical measure:
$$d\chi_t = -\kappa \chi_t \, dt + \sigma_\chi \, dW_\chi$$
$$d\xi_t = \mu_\xi \, dt + \sigma_\xi \, dW_\xi$$

With correlation: $dW_\chi \cdot dW_\xi = \rho \, dt$

## Futures Pricing

Under the risk-neutral measure, the futures price for delivery at $T$ is:
$$\ln F(t,T) = e^{-\kappa(T-t)}\chi_t + \xi_t + A(T-t)$$

Where $A(\cdot)$ captures risk premia and convexity adjustments.

## Interpretation

| Factor | Economic Meaning |
|--------|------------------|
| $\chi_t$ | Supply/demand shocks, inventory effects |
| $\xi_t$ | Long-run supply cost, technology trends |
| $\kappa$ | Speed of mean reversion (shock persistence) |

## Estimation

Typically via **Kalman filter**:
- States: $(\chi_t, \xi_t)$
- Observations: Futures prices at various maturities
- Handles missing data and irregular observations

## Extensions

- **Three-factor models**: Add stochastic convenience yield
- **Jumps**: Incorporate sudden price moves
- **Regime switching**: Time-varying parameters
- **Multi-commodity**: Joint factor structures

## See Also

- [[concepts/state-space-models|State-Space Models]]
- [[concepts/kalman-filter|Kalman Filter]]
- [[concepts/functional-data-analysis|Functional Data Analysis]]
- [[sources/he-2024-functional-regression|Multi-Factor Function-on-Function Regression (2024)]]
