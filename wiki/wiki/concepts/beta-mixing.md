---
title: "β-Mixing"
page_id: concepts/beta-mixing
page_type: concept
revision_id: 1
created: 2026-04-28T12:45:00Z
updated: 2026-04-28T12:45:00Z
sources: [sources/koukorinis-2026-draci, sources/lee-2024-kowcpi]
related: [concepts/long-memory, concepts/state-space-models, concepts/conformal-prediction, concepts/adaptive-conformal-inference, concepts/doubly-robust-estimation, concepts/temporal-cross-fitting, concepts/causal-inference]
tags: [time-series, dependence, statistics]
---

# β-Mixing (Absolute Regularity)

## Definition

β-mixing (also called absolute regularity) measures how quickly dependence between past and future observations decays in a stochastic process. For a stationary process {Z_t}, the β-mixing coefficient at lag k is:

$$\beta(k) = \sup_{j \geq 1} d_{TV}\left(\mathcal{L}(Z_1^j, Z_{j+k+1}^\infty), \mathcal{L}(Z_1^j) \otimes \mathcal{L}(Z_{j+k+1}^\infty)\right)$$

Where:
- $Z_a^b$ = subsequence from index a to b
- $d_{TV}$ = total variation distance
- $\otimes$ = product measure (independence)

**Interpretation:** β(k) measures how close the "past" and "future" are to independence when separated by k time steps.

## Mixing Hierarchy

β-mixing is one of several mixing conditions, ordered by strength:

**Strong → Weak:**
- α-mixing (strong mixing) ⊂ β-mixing ⊂ ρ-mixing ⊂ ψ-mixing

β-mixing is stronger than α-mixing, meaning fewer processes satisfy it, but stronger results are available.

## Common Processes

Many standard time series models are geometrically β-mixing (β(k) ≤ Cρ^k for ρ < 1):

- **AR(p)** with stable roots
- **ARMA(p,q)** with stable roots
- **GARCH(p,q)** under moment conditions
- **Markov chains** with geometric ergodicity

## Decay Rates

- **Geometric:** β(k) ≤ Cρ^k (most common in practice)
- **Polynomial:** β(k) ≤ Ck^{-r} (weaker condition)

Geometric mixing is typical for financial time series (AR, GARCH models).

## Applications in Conformal Prediction

[[sources/koukorinis-2026-draci|DR-ACI]] uses β-mixing to quantify coverage gaps under temporal dependence:

### Switch Coefficients

For stationary β-mixing processes, the coverage gap of conformal prediction includes a **mixing gap** term:

$$\text{mixing gap} = \min_{\tau \geq 1}\left\{\frac{\tau}{T} + 2\beta(\tau)\right\}$$

Under geometric mixing (β(k) = ρ^k), the optimal lag τ* and resulting gap depend on ρ:
- ρ = 0.90 → gap ≈ 0.033
- ρ = 0.95 → gap ≈ 0.062
- ρ = 0.99 → gap ≈ 0.23 (coverage may degrade significantly)

### Guard Bands

Temporal block cross-fitting with guard bands of size g ensures training-calibration coupling error is O(β(g)^{δ/(2+δ)}).

## Rio's Coupling Inequality

A key technical tool for working with β-mixing data. Allows bounding deviations from independence in terms of mixing coefficients and moment conditions.

## Empirical Notes

From [[sources/koukorinis-2026-draci|DR-ACI simulations]]:
- Theoretical bounds are often conservative
- Empirical coverage at ρ=0.99 exceeds the ≤67% theoretical bound
- The switch coefficient bound over-estimates actual distributional shift

## See Also

- [[concepts/long-memory|Long Memory]]
- [[sources/koukorinis-2026-draci|DR-ACI Paper]]
- [[concepts/conformal-prediction|Conformal Prediction]]
