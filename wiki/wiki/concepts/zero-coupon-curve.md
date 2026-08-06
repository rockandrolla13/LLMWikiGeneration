---
title: Zero-Coupon Curve
page_id: concepts/zero-coupon-curve
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- yield-curves
- bond-pricing
- credit-spread-risk
- curve-fitting
- creditETF
sources:
- sources/pullirsch-2006-credit-spread-risk
- sources/ubs-2012-next-gen-credit-curves
related:
- concepts/credit-spread-curve
- concepts/yield-curve
- concepts/hazard-rate-curve
mind_map_priority: medium
schema_version: 2
uuid: 28672b18-e949-5ea8-8bd8-39ea2cc59134
content_hash: sha256:ac916679e7cd04f8681e745c714bd8fb68a80c140c6d35dd4467bdffb05bad40
---

<!-- AUTHORED REGION START -->
# Zero-Coupon Curve

A curve of discount rates by maturity, stripped of coupon effects, so that any cash flow at any date can be discounted directly. It is the object you actually need for pricing, and it has to be estimated from coupon-bearing instruments that do not line up with it.

## Estimating a Zero-Coupon Credit-Spread Curve

[[sources/pullirsch-2006-credit-spread-risk|Pullirsch (2006)]] builds one per issuer:

1. Start from a riskless zero-coupon term structure derived from **swap rates** — chosen over government bonds because they are more liquid and reflect the current term structure, at the cost of a slightly higher level from counterparty and LIBOR risk.
2. Add a credit spread s(t) to the discount factors.
3. Minimise pricing error across all of the issuer's bonds, using m grid points for Q bonds, with cubic-spline interpolation between them.

Risk factors sit at t ∈ [0, 1, …, 16, 18, 20, 25] years, capped by the longest actual bond maturity.

## The Stability Trade-Off

More grid points fit prices better and make the curve less stable. Pullirsch controls this with a coupon variation method: compute the maximum sensitivity Δ of the fitted spread curve to coupon changes for each grid scheme, and drop grid points (m → m−1) until the stability criterion is met, allowing at most 5% deviation between model and quoted prices. Fewer points give smoother curves. A condition-number criterion on the linear system is the alternative he describes but does not implement.

What the curve cannot absorb is pushed into **residual variance** — the parallel shift needed to price each bond exactly, capturing currency, liquidity and bond-specific effects.

## The Hazard-Rate Alternative

[[sources/ubs-2012-next-gen-credit-curves|UBS Delta (2012)]] argue for fitting a [[concepts/hazard-rate-curve|hazard-rate curve]] instead of currency-specific spread curves, since hazard rates are directly comparable across instruments and currencies. Same estimation problem, different state variable.

## See Also

[[concepts/credit-spread-curve|Credit Spread Curve]] · [[concepts/yield-curve|Yield Curve]] · [[concepts/hazard-rate-curve|Hazard Rate Curve]] · [[concepts/z-spread|Z-Spread]] · [[concepts/nelson-siegel-model|Nelson-Siegel Model]] · [[concepts/value-at-risk|Value at Risk]] · [[entities/rainer-pullirsch|Rainer Pullirsch]] · [[entities/ubs-delta|UBS Delta]]

**Not yet written:** `concepts/residual-variance`, `concepts/bootstrapping-curves`, `concepts/cubic-spline-interpolation`

<!-- AUTHORED REGION END -->
