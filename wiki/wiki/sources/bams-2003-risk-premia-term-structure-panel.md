---
authors:
- Dennis Bams
- Christian C.P. Wolff
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/bams-2003-risk-premia-term-structure-panel
page_type: source
publication_date: '2003'
publication_venue: Journal of International Financial Markets, Institutions & Money
related:
- concepts/expectations-hypothesis-term-structure
- concepts/forward-rate
- concepts/kalman-filter-state-space
- concepts/one-factor-term-structure-model
- concepts/panel-data-fixed-random-effects
- concepts/term-structure-risk-premium
- entities/christian-wolff
- entities/dennis-bams
revision_hash: sha256:f77f4447fa083a19d1bc737bc9c5fcdd39f011e0f8e75faf4e4fc2954ff97129
revision_id: 1
source_hash: sha256:fc63a9a0cb1f9c91d12de6ade7b1bab58b6bf4d5726bcbd2d7a8845fa8dd2727
source_path: raw/creditmacro/1-s2.0-S1042443102000458-main.md
source_type: paper
sources: []
tags:
- term-structure
- interest-rates
- expectations-hypothesis
- risk-premium
- panel-data
- government-bonds
- kalman-filter
title: 'Risk premia in the term structure of interest rates: a panel data approach'
updated: '2026-06-20T01:03:51Z'
updated_by: op_2de49c1476ac
schema_version: 2
uuid: 56257bcc-88f4-55b8-9307-b107bba29330
content_hash: sha256:328c42afce428e859ec8a4208061657126e9c610a336b1adb410ae9cd0ff6766
---

<!-- AUTHORED REGION START -->
# Risk premia in the term structure of interest rates: a panel data approach

**Authors:** Dennis Bams, Christian C.P. Wolff · **Year:** 2003 · **Venue:** Journal of International Financial Markets, Institutions & Money · **Type:** paper

## Summary

Bams and Wolff propose a panel data approach to modeling the risk premium in the term structure of interest rates, developing a fixed maturity / random time effects model that implies a time-invariant one-factor model. The panel framework lets them disentangle the unobservable risk premium from the unexpected excess return - impossible in standard univariate time-series approaches - while alleviating small-sample bias and improving efficiency. Using monthly US Treasury data (Jan 1970-Dec 1994) for 16 maturities, they reject the expectations hypothesis for the full panel even though it holds at the short end univariately, find considerable mean reversion in risk premia (AR(1) persistence ~0.675), and estimate the forward-rate slope coefficient at about 0.8 (versus 1 under the expectations hypothesis). Risk premia increase with time-to-maturity, consistent with liquidity preference.

## Key Claims

1. A panel fixed-maturity/random-time-effects model implies a time-invariant one-factor model and disentangles the risk premium from the unexpected excess return.
2. The expectations hypothesis is soundly rejected for the full panel even though it cannot be rejected in univariate short-end models.
3. Risk premia exhibit considerable mean reversion, with an AR(1) persistence parameter of approximately 0.675.
4. The slope coefficient in regressions of future yields on current forward rates is estimated at about 0.8 (versus 1 under the expectations hypothesis).
5. Risk premia increase with time-to-maturity, consistent with the liquidity preference theory.
6. Pooling cross-sectional and time-series data mitigates the small-sample bias arising from the extreme persistence of short rates.

## Questions Raised

- Would the panel model yield similar rejections in non-US settings?
- How sensitive are estimated risk premia to the choice of cubic-spline breakpoints in constructing the discount curve?
- Can the time-variation in risk premia be linked to business-cycle or regime variables?

## Concepts

- [[concepts/expectations-hypothesis-term-structure|Expectations Hypothesis of the Term Structure]]
- [[concepts/term-structure-risk-premium|Term Structure Risk Premium]]
- [[concepts/panel-data-fixed-random-effects|Panel Data Fixed/Random Effects]]
- [[concepts/forward-rate|Forward Rate]]
- [[concepts/one-factor-term-structure-model|One-Factor Term Structure Model]]
- [[concepts/kalman-filter-state-space|Kalman Filter State-Space Estimation]]

## Entities

- [[entities/dennis-bams|Dennis Bams]]
- [[entities/christian-wolff|Christian C.P. Wolff]]

## Source

- **Path:** `raw/creditmacro/1-s2.0-S1042443102000458-main.md`
- **Type:** paper
- **Hash:** `sha256:fc63a9a0cb1f9c91d...`
<!-- AUTHORED REGION END -->
