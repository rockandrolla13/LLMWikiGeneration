---
title: Market-Implied Ratings
page_id: concepts/market-implied-ratings
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T17:35:34Z'
tags:
- creditETF
- credit-curves
- ratings
- hazard-rate
- market-implied
sources:
- sources/ubs-2012-next-gen-credit-curves
related:
- concepts/hazard-rate-curve
- concepts/credit-spread-curve
- concepts/cds-bond-basis
mind_map_priority: medium
schema_version: 2
uuid: 1efabd02-0243-5ecd-becc-a3133f389a7f
content_hash: sha256:6464f75c60d8012590134439c3197614dd6efdca8a2149bcc5824afa2050dd26
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

<!-- AUTHORED REGION END -->
