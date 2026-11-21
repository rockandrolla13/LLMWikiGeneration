---
content_hash: sha256:41a41ccb57487730ab9f624789940cc8d6b1628cd4614de0a45f9da8af438472
created: 2026-04-25 22:00:00+00:00
mind_map_priority: medium
page_id: concepts/yield-to-maturity
page_type: concept
related:
- concepts/credit-spread-curve
- concepts/z-spread
- concepts/green-bond-spreads
revision_id: 3
schema_version: 2
sources:
- sources/sehatpour-2024-green-bonds
- sources/kricheff-2012-pragmatists-guide-leveraged-finance
- sources/whitman-2009-distress-investing
- sources/marks-2010-hemlines
tags:
- fixed-income
- bond-pricing
- yield-measures
- fundamentals
title: Yield to Maturity
updated: '2026-11-21T02:33:09Z'
updated_by: op_fed0f2b9acba
uuid: acbd6eea-70af-5d69-908c-3f7b1e5f6568
---

<!-- AUTHORED REGION START -->
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

## Sources

- [[sources/whitman-2009-distress-investing|Distress Investing: Principles and Technique]] (2009)
- [[sources/kricheff-2012-pragmatists-guide-leveraged-finance|A Pragmatist's Guide to Leveraged Finance: Credit Analysis for Bonds and Bank Debt]] (2012)

## In Howard Marks's Memos

- [[sources/marks-2010-hemlines|Hemlines]] (2010)
<!-- AUTHORED REGION END -->