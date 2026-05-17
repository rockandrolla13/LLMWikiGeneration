---
title: "Yield to Maturity"
page_id: concepts/yield-to-maturity
page_type: concept
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
tags: [fixed-income, bond-pricing, yield-measures, fundamentals]
sources: [sources/sehatpour-2024-green-bonds]
related: [concepts/credit-spread-curve, concepts/z-spread, concepts/green-bond-spreads]
mind_map_priority: medium
---

# Yield to Maturity (YTM)

Yield to maturity is the internal rate of return of a bond, assuming it is held until maturity and all payments are made as scheduled.

## Definition

YTM ($y$) solves:

$$P = \sum_{t=1}^{T} \frac{C}{(1+y)^t} + \frac{F}{(1+y)^T}$$

Where:
- $P$ = Current price
- $C$ = Coupon payment
- $F$ = Face value
- $T$ = Time to maturity

## Interpretation

YTM represents:
- **Expected return** if held to maturity (under assumptions)
- **Discount rate** that equates price to present value of cash flows
- **Comparison metric** across bonds with different characteristics

## Assumptions and Limitations

| Assumption | Reality |
|------------|---------|
| Hold to maturity | Often sold early |
| Reinvest coupons at YTM | Rates change over time |
| No default | Credit risk exists |
| Pay on schedule | Callables may be called |

## YTM vs Other Measures

| Measure | Use Case |
|---------|----------|
| YTM | Overall return measure |
| Current yield | Income focus (coupon/price) |
| Yield to call | Callable bonds |
| Yield to worst | Conservative measure |
| Spread measures | Relative value |

## Applications

- Bond comparison and ranking
- Valuation and trading
- Green bond spread calculation (YTM-based)
- Performance measurement

## See Also

- [[concepts/credit-spread-curve|Credit Spread Curve]]
- [[concepts/z-spread|Z-Spread]]
- [[concepts/green-bond-spreads|Green Bond Spreads]]
- [[sources/sehatpour-2024-green-bonds|Anatomy of Municipal Green Bond Yield Spreads (2024)]]
