---
title: "Credit Spread Curve"
page_id: concepts/credit-spread-curve
page_type: concept
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
tags: [fixed-income, credit-risk, bond-pricing, yield-curves]
sources: [sources/martin-2024-credit-curve]
related: [concepts/z-spread, concepts/survival-probability, concepts/carry-rolldown, concepts/nelson-siegel-model]
mind_map_priority: high
---

# Credit Spread Curve

The credit spread curve represents the term structure of credit spreads—the additional yield investors require above risk-free rates to hold a risky bond.

## Definition

A credit spread curve maps maturity (or duration) to credit spread, providing a complete picture of how credit risk is priced across different time horizons for a given issuer or rating category.

## Key Concepts

### Par vs Non-Par Problem
A critical distinction in credit spread construction:
- **Par bonds** trade at face value; their yields directly reflect current market spreads
- **Non-par bonds** have coupons that differ from current market rates, requiring adjustment

### Construction Approaches

1. **Z-spread method**: Constant spread added to the risk-free curve
2. **Survival probability method**: Derive spreads from default probability curves
3. **Interpolation methods**: Nelson-Siegel, splines, or piecewise linear

## Applications

- **Relative value analysis**: Identifying mis-priced bonds
- **Portfolio construction**: Systematic spread positioning
- **Risk management**: Duration and spread risk decomposition
- **Carry and rolldown**: Projecting returns from spread curve dynamics

## Mathematical Framework

The credit spread $s(t)$ at maturity $t$ relates to the survival probability $Q(t)$ and recovery rate $R$:

$$s(t) \approx -\frac{\ln Q(t)}{t} \cdot (1 - R)$$

## See Also

- [[concepts/z-spread|Z-Spread]]
- [[concepts/survival-probability|Survival Probability]]
- [[concepts/carry-rolldown|Carry and Rolldown]]
- [[sources/martin-2024-credit-curve|The Credit Curve Spread I (Martin, 2024)]]
