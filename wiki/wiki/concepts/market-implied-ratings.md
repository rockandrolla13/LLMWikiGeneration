---
content_hash: sha256:56d25ffa133b899d2aa8ae7575e8661f20000446aa6a1a41aafe10f533cfdb3a
created: 2026-08-06 00:00:00+00:00
mind_map_priority: medium
page_id: concepts/market-implied-ratings
page_type: concept
related:
- concepts/hazard-rate-curve
- concepts/credit-spread-curve
- concepts/cds-bond-basis
revision_id: 2
schema_version: 2
sources:
- sources/ubs-2012-next-gen-credit-curves
- sources/chan-2023-price-convergence-cds-put-option
- sources/lee-2021-cds-momentum-cross-market-spillovers
tags:
- creditETF
- credit-curves
- ratings
- hazard-rate
- market-implied
title: Market-Implied Ratings
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: 1efabd02-0243-5ecd-becc-a3133f389a7f
---

<!-- AUTHORED REGION START -->
# Market-Implied Ratings

A credit assessment inferred from traded prices — bond spreads, CDS quotes, or a fitted [[concepts/hazard-rate-curve|hazard rate curve]] — rather than from an agency's published rating. The market's view, read off the instruments, instead of the agency's view read off a committee decision.

## The Problem They Address

[[sources/ubs-2012-next-gen-credit-curves|Matthews & Bosatta (2012)]] set out the limitations of building credit curves the traditional way:

- Spread curves built separately by currency, and bond curves kept separate from CDS curves.
- Correlation of only around **30%** between curves for the same issuer in different currencies.
- Rating-based proxy curves miss issuer idiosyncrasies.
- Ratings migrations introduce **artificial jumps** into curves, since the agency rating moves in discrete steps at discrete times while the market's view moves continuously.

That last point is the core motivation: an agency rating is a lagging, step-valued signal. A market-implied measure updates continuously.

## How They Are Derived Here

The UBS Delta "D-Curves" approach estimates a **single hazard-rate curve per issuer**, jointly using bond prices across all issued currencies and CDS quotes referencing the entity, while simultaneously estimating the currency and instrument basis. Bonds are treated consistently with CDS via default and no-default scenarios, discounted at market funding rates (OIS plus cross-currency basis swaps).

Once an issuer has one hazard-rate curve, its implied credit quality can be expressed on a rating-like scale and compared against the agency rating — the gap between the two being the signal.

## Caveats

A market-implied rating inherits everything priced into the instruments, including liquidity premia, technical flows and risk appetite. It is not a cleaner measure of default probability than an agency rating; it is a different measure, faster-moving and noisier.

## See Also

[[concepts/hazard-rate-curve|Hazard Rate Curve]] · [[concepts/credit-spread-curve|Credit Spread Curve]] · [[concepts/cds-bond-basis|CDS-Bond Basis]] · [[entities/ubs-delta|UBS Delta]]

## Sources

- [[sources/lee-2021-cds-momentum-cross-market-spillovers|CDS Momentum: Slow-Moving Credit Ratings and Cross-Market Spillovers]]
- [[sources/chan-2023-price-convergence-cds-put-option|Price Convergence Between Credit Default Swap and Put Option: New Evidence]]
<!-- AUTHORED REGION END -->