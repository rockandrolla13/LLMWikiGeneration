---
title: "Optimal Quoting under Adverse Selection and Price Reading"
page_id: sources/barzykin-2025-adverse-selection
page_type: source
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [market-making, adverse-selection, price-reading, informational-risk, stochastic-control]
authors: [Alexander Barzykin, Philippe Bergault, Olivier Guéant, Malo Lemmel]
year: 2025
related: [concepts/market-making, concepts/adverse-selection, concepts/inventory-risk, entities/olivier-gueant, entities/philippe-bergault, entities/alexander-barzykin]
---

# Optimal Quoting under Adverse Selection and Price Reading

## Summary

This paper tackles two critical but often overlooked challenges in [[concepts/market-making]]: **adverse selection** from informed traders and **price reading** (or skew sniffing) where the market maker's quotes reveal inventory information. The framework provides first-order adjustments to optimal quotes that account for informational risk.

## Key Challenges Addressed

### Adverse Selection
- Market maker trades against participants with superior information
- Risk of being hit at bid just before price drops (winner's curse)
- Different tiers of clients have different informativeness

### Price Reading / Skew Sniffing
- Market maker's quotes reveal inventory direction
- Sophisticated traders extract signals from quote asymmetry
- Creates feedback loop affecting reference price

## Model Framework

**Reference price dynamics with informational effects:**
$$dS_t = \sigma dB_t + \sum_{n,k} \tilde{\zeta}^{n,k}(\delta_t^{n,k,b/a})\Delta^k dN_t^{n,k,b/a} + \sum_n \tilde{J}^n(\text{skew}_t^n) dt$$

where:
- $\tilde{\zeta}^{n,k}$ captures adverse selection by tier and size
- $\tilde{J}^n$ captures price reading effects from quote asymmetry

## First-Order Analysis

Rather than solving the full problem, the paper uses **Taylor expansions** to compute first-order adjustments:
1. Start with baseline (no informational risk)
2. Introduce perturbation parameter $\varepsilon$
3. Derive corrections to value function and optimal quotes

## Key Results

**Baseline optimal quotes** (without informational risk):
$$\delta^{n,k,b/a*}(q) = \bar{\delta}^{n,k,b/a*}(q, D^{+}_k\theta(q), D^{-}_k\theta(q))$$

**First-order corrections** account for:
- How executions by informed traders move prices
- How quote asymmetry is detected and exploited
- Tier-specific and size-specific adjustments

## Practical Implications

Market makers should:
1. Widen spreads for more informed client tiers
2. Reduce quote skewing when price reading risk is high
3. Balance inventory management with information leakage

## Related Sources

- [[sources/barzykin-2021-fx-dealer-tiers]] - Foundation model with client tiering
- [[sources/barzykin-2020-algorithmic-fx-market-making]] - Internalization-externalization framework

## Citation

Barzykin, A., Bergault, P., Guéant, O., & Lemmel, M. (2025). Optimal Quoting under Adverse Selection and Price Reading.
