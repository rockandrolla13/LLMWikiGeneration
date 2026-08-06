---
title: Yield Curve
page_id: concepts/yield-curve
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- yield-curve
- term-structure
- fixed-income
- rates
- bond-pricing
sources:
- sources/omrane-2017-yield-curve-forecasting
- sources/krishnan-2007-credit-spread-forecast
- sources/ms-2017-01-28-rates-strategist-duration-and-curves
related:
- concepts/nelson-siegel-model
- concepts/yield-curve-forecasting
- concepts/yield-curve-steepeners-flatteners
- concepts/zero-coupon-curve
mind_map_priority: medium
schema_version: 2
uuid: b1d71818-36f9-50f2-b3c5-57456308b30c
content_hash: sha256:fc894ac19b366dfbb6076458d3e21386960839d6f07c9f785746b713f40a401c
---

<!-- AUTHORED REGION START -->
# Yield Curve

Yield plotted against maturity for a single issuer class, usually government bonds. Almost everything done with it reduces to describing its shape with a few numbers and then tracking how those numbers move.

## Three Factors

The standard description is level, slope and curvature. In the Nelson-Siegel form used by [[sources/omrane-2017-yield-curve-forecasting|Ben Omrane et al. (2017)]],

y(τ) = β₁ + β₂·[(1−e^(−λτ))/(λτ)] + β₃·[(1−e^(−λτ))/(λτ) − e^(−λτ)]

where β₁ is long-term level, β₂ the spread between long and short, β₃ a medium-term hump, and λ sets the decay of the factor loadings. Most implementations fix λ; Ben Omrane et al. estimate it. See [[concepts/nelson-siegel-model|Nelson-Siegel Model]].

The same three-factor description carries over to credit. [[sources/krishnan-2007-credit-spread-forecast|Krishnan, Ritchken & Thomson (2007)]] fit a modified Diebold-Li model to firm-level credit-spread curves and find the shape improves on spot and forward models. Their more interesting result is cross-market: the **riskless** yield curve's level, slope and curvature significantly improve credit spread forecasts, and once you have both curves, additional macro, market and firm variables add nothing.

## Trading the Shape

Slope changes are traded directly as steepeners and flatteners — 5s30s, 10s30s and similar. [[sources/ms-2017-01-28-rates-strategist-duration-and-curves|Morgan Stanley (January 2017)]] is the worked example in this wiki: rising equity-bond yield correlations turned their Bond Market Indicators negative on duration across G4, and the recommended expression was curve, not level — UST and Bund 5s30s steepeners, short 10y gilts, receiving front-end rates in Australia and New Zealand. See [[concepts/yield-curve-steepeners-flatteners|Yield Curve Steepeners and Flatteners]].

## Related Constructions

For discounting you want the [[concepts/zero-coupon-curve|zero-coupon curve]] rather than the par yield curve. For the expected excess return on holding longer maturities, see [[concepts/term-structure-risk-premium|Term Structure Risk Premium]].

## See Also

[[concepts/nelson-siegel-model|Nelson-Siegel Model]] · [[concepts/yield-curve-forecasting|Yield Curve Forecasting]] · [[concepts/yield-curve-steepeners-flatteners|Yield Curve Steepeners and Flatteners]] · [[concepts/zero-coupon-curve|Zero-Coupon Curve]] · [[concepts/term-structure-risk-premium|Term Structure Risk Premium]] · [[concepts/credit-spread-curve|Credit Spread Curve]] · [[concepts/forward-rate|Forward Rate]] · [[concepts/government-bond-spreads|Government Bond Spreads]]

**Not yet written:** `concepts/diebold-li-model`, `concepts/affine-term-structure-models`, `concepts/term-structure`

<!-- AUTHORED REGION END -->
