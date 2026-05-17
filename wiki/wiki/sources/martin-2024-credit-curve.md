---
title: "The credit curve spread I: Fundamental concepts, fitting, par-adjusted spread, and expected return"
page_id: sources/martin-2024-credit-curve
page_type: source
source_type: working-paper
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
authors: [Richard J. Martin]
year: 2024
venue: arXiv preprint
tags: [credit-spread, fixed-income, survival-probability, carry-rolldown, cds, bond-pricing]
related: [sources/dickerson-2023-bond-risk, sources/sehatpour-2024-green-bonds, concepts/credit-spread-curve, concepts/z-spread, concepts/carry-rolldown, concepts/survival-probability, entities/richard-martin]
mind_map_priority: high
---

# The Credit Curve Spread I: Fundamental Concepts

**Author:** [[entities/richard-martin|Richard J. Martin]]

**Year:** 2024

**Venue:** arXiv preprint

**Institution:** Imperial College London

## Summary

A comprehensive treatment of credit spread curve construction for fixed income investing, correcting fundamental errors in academic literature including Duffie & Singleton (1997). Develops proper methods for survival curve fitting, par-adjusted spread, and expected return calculation.

## Motivation

Credit investors need to answer:
- How has a sector/issuer traded historically?
- Is the curve flat or steep vs. history?
- How to determine carry, rolldown, and relative value?

## Key Contributions

### 1. Critique of Existing Literature
- Duffie & Singleton (1997) is "fundamentally incorrect"
- Default-adjusted discount rate R = r + hL has wrong loss mechanism
- Bonds can only default once; loss is proportion of par value
- Academic literature lacks connection to real market practice

### 2. Correct Valuation Framework
Bond price formula:
```
P = c·Π(T) + B(T)Q(T) + ℜΞ
```
Where:
- Π(T) = RPV01 (risky PV01)
- Q(T) = survival probability
- B(T) = riskfree discount factor
- ℜ = recovery rate
- Ξ = expected recovery value

### 3. Par/Non-Par Problem
- High dollar price bonds trade at higher yield than discount bonds
- Z-spread unsuitable for bonds trading away from par
- Coupon stream riskier than principal (partially recoverable)
- Explains Colombia bond example (4% vs 8.125% 2024s)

### 4. Par-Adjusted Spread
- Removes the par/non-par effect
- Enables proper curve fitting across bonds
- Compatible with CDS spread

### 5. Expected Return Components
- **Carry:** P&L if yield fixed (includes pull-to-par effect)
- **Rolldown:** P&L from maturity reduction with fixed curve
- **Relative Value:** Rich/cheap to the fitted curve

## Practical Applications

- Rating-by-rating curve fitting for sectors
- Single issuer curve construction
- CDS curve stripping
- Accreting bond valuation
- Bond forwards pricing

## Key Claims

1. Must discount with riskfree factors, survival probabilities, and recoveries
2. Z-spread is unsuitable for bonds trading away from par
3. No need for hazard rate models; survival function Q(T) sufficient
4. Fractional recovery of par (FRP) is only sensible assumption
5. Continuous coupon approximation loses little accuracy

## See Also

- [[concepts/credit-spread-curve|Credit Spread Curve]]
- [[concepts/z-spread|Z-Spread]]
- [[concepts/carry-rolldown|Carry and Rolldown]]
- [[concepts/survival-probability|Survival Probability]]
