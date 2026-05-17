---
title: "Carry and Rolldown"
page_id: concepts/carry-rolldown
page_type: concept
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
tags: [fixed-income, portfolio-management, return-decomposition, trading-strategies]
sources: [sources/martin-2024-credit-curve]
related: [concepts/credit-spread-curve, concepts/z-spread, concepts/nelson-siegel-model]
mind_map_priority: medium
---

# Carry and Rolldown

Carry and rolldown are components of expected bond returns that arise from the passage of time, assuming no change in market conditions.

## Definitions

### Carry
The income return from holding a bond, typically:
- **Coupon income** minus **financing cost**
- For a funded position: yield minus repo rate
- Represents compensation for holding duration/credit risk

### Rolldown
The capital gain (or loss) from a bond "rolling down" the yield curve as it ages:
- If the curve is upward sloping, shorter maturity → lower yield → higher price
- A 5-year bond today becomes a 4-year bond tomorrow

## Mathematical Framework

Total expected return (assuming unchanged curves):

$$\text{Expected Return} = \text{Carry} + \text{Rolldown}$$

**Carry**:
$$\text{Carry} = \text{Yield} - \text{Funding Rate}$$

**Rolldown** (approximation):
$$\text{Rolldown} \approx -\text{Duration} \times \Delta y_{\text{curve shape}}$$

## Applications

1. **Relative value**: Compare carry-adjusted valuations across bonds
2. **Curve positioning**: Identify "sweet spots" with high rolldown
3. **Performance attribution**: Decompose realized returns
4. **Strategy design**: Carry strategies systematically harvest these returns

## Considerations

- Carry/rolldown are **not risk-free**—curves can shift
- High carry often signals high risk (credit, liquidity)
- Rolldown assumes parallel curve dynamics (rarely exact)

## See Also

- [[concepts/credit-spread-curve|Credit Spread Curve]]
- [[concepts/z-spread|Z-Spread]]
- [[sources/martin-2024-credit-curve|The Credit Curve Spread I (Martin, 2024)]]
