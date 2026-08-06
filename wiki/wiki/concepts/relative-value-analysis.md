---
title: Relative Value Analysis
page_id: concepts/relative-value-analysis
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- relative-value
- credit-analysis
- fundamental-analysis
- creditETF
sources:
- sources/spec-2012-single-name-fundamental
related:
- concepts/spread-per-turn-of-leverage
- concepts/leverage-ratios
- concepts/credit-relative-value
mind_map_priority: medium
schema_version: 2
uuid: 84d0db03-99ee-5449-a88d-178f43c71cf3
content_hash: sha256:f5174c99540e88ac54e83b8cf4345f3ddd1ba0368360dd346a4aceb32708f6a5
---

<!-- AUTHORED REGION START -->
# Relative Value Analysis

Deciding whether a credit is cheap or expensive against comparable credits rather than in absolute terms. The unit of comparison is usually the sector: a name is scored against the average of its peers, and the residual is the signal.

## Static Screens

[[sources/spec-2012-single-name-fundamental|The 2012 single-name fundamental specification]] sets out three, all built the same way — regress or average a spread driver across the sector, then measure the deviation.

- **[[concepts/spread-per-turn-of-leverage|Spread per turn of leverage]]** — five-year CDS spread divided by net debt / EBITDA. Compare a company's ratio to the sector average excluding itself; the predicted spread is sector-average SPL times company leverage, and actual minus predicted is the signal. Run on both trailing and forecast leverage.
- **Spread versus interest coverage** — the same framework with the interest coverage ratio as denominator, where the expected correlation with spreads is negative.
- **Spread versus rating** — map agency ratings to numerical buckets and look for names off the rating-implied spread.

## Dynamic Screens

Two screens in the specification look forward rather than across:

- **Cyclicality versus liquidity** — how far EBITDA has to fall before the company is forced to refinance, using cash, trailing EBITDA, interest expense and capex. Aimed at shorter or more volatile business-cycle themes.
- **Ratings drift** — a regression predicting ratings from fundamentals, used to flag upgrade and downgrade candidates, with trade templates built around rating watch status.

## The Standing Caveat

These screens assume the peer group is the right comparison and that the relationship between spread and the chosen driver is linear. They are point-in-time and do not capture business risk or asset quality. A residual is a question, not an answer.

## See Also

[[concepts/spread-per-turn-of-leverage|Spread Per Turn of Leverage]] · [[concepts/leverage-ratios|Leverage Ratios]] · [[concepts/credit-relative-value|Credit Relative Value]] · [[concepts/credit-spread-curve|Credit Spread Curve]] · [[concepts/hyperscaler-data-center-bond-relative-value|Hyperscaler Data Center Bond Relative Value]] · [[concepts/cds-bond-basis|CDS-Bond Basis]]

**Not yet written:** `concepts/ratings-drift`, `concepts/sector-screening`

<!-- AUTHORED REGION END -->
