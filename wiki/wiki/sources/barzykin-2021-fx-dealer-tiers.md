---
title: "Market making by an FX dealer: tiers, pricing ladders and hedging rates"
page_id: sources/barzykin-2021-fx-dealer-tiers
page_type: source
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [market-making, fx, foreign-exchange, client-tiering, internalization, externalization, stochastic-control]
authors: [Alexander Barzykin, Philippe Bergault, Olivier Guéant]
year: 2021
related: [concepts/market-making, concepts/internalization-externalization, concepts/client-tiering, concepts/inventory-risk, entities/olivier-gueant, entities/philippe-bergault, entities/alexander-barzykin]
---

# Market making by an FX dealer: tiers, pricing ladders and hedging rates

## Summary

This paper develops a comprehensive [[concepts/market-making]] framework for foreign exchange (FX) dealers that addresses both pricing and hedging decisions. The key innovation is the explicit modeling of the **internalization vs. externalization dilemma** that FX dealers face when managing inventory risk.

## The Internalization-Externalization Dilemma

FX market makers have two primary strategies for managing [[concepts/inventory-risk]]:

1. **Internalization**: Hold risk and skew prices to attract offsetting client flow
2. **Externalization**: Hedge on the dealer-to-dealer (D2D) segment, incurring transaction costs and market impact

The paper proves the existence of a **pure internalization zone** - an inventory threshold below which it is optimal not to externalize.

## Client Tiering

A major contribution is the empirical analysis and modeling of [[concepts/client-tiering]]:
- Using HSBC FX streaming data for EURUSD (Jan-Apr 2021)
- Intensity functions estimated via maximum likelihood
- Two distinct client tiers identified through k-means clustering on intensity parameters
- **Tier 1**: Lower price sensitivity (β = 5 bps⁻¹)
- **Tier 2**: Higher price sensitivity (β = 15 bps⁻¹)

## Model Framework

The market maker:
- Streams pricing ladders for each tier at bid and ask
- Can hedge on D2D platforms with execution rate v(t)
- Faces permanent market impact from externalization
- Maximizes expected P&L minus a running inventory penalty

The intensity functions take a logistic form:
$$\Lambda^{b/a}(\delta) = \frac{\lambda}{1 + e^{\alpha + \beta\delta}}$$

## Key Results

- Optimal quotes and hedging rates derived from Hamilton-Jacobi equation
- Risk neutralization time and internalization ratios consistent with industry figures
- Dealer's efficient frontier analyzed as function of risk aversion

## Related Sources

- [[sources/barzykin-2020-algorithmic-fx-market-making]] - Earlier paper introducing the framework
- [[sources/barzykin-2022-multi-currency-inventory]] - Extension to multiple currency pairs

## Citation

Barzykin, A., Bergault, P., & Guéant, O. (2021). Market making by an FX dealer: tiers, pricing ladders and hedging rates for optimal risk control. *Quantitative Finance*.
