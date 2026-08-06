---
title: Factors Affecting the Valuation of Corporate Bonds
page_id: sources/elton-2004-valuation-corporate-bonds
page_type: source
source_path: markdown_output/1-s2.0-S0378426604001074-main.md
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Edwin J. Elton
- Martin J. Gruber
- Deepak Agrawal
- Christopher Mann
year: 2004
venue: Journal of Banking & Finance
tags:
- corporate-bonds
- credit-ratings
- spot-curve-estimation
- liquidity
- taxes
sources: []
related:
- concepts/corporate-bonds
- concepts/reduced-form-credit-models
- concepts/nelson-siegel-model
- concepts/credit-spread-curve
- concepts/bond-liquidity
- concepts/zero-coupon-curve
mind_map_priority: medium
schema_version: 2
uuid: 27406a67-09ac-5393-ba21-4fa937499a83
content_hash: sha256:f768a19d42f0df02f51dfff7b34439709cd63e2ab4cccb6d9acd9c3136b91d55
---

<!-- AUTHORED REGION START -->
# Factors Affecting the Valuation of Corporate Bonds

**Authors:** Edwin J. Elton, Martin J. Gruber, Deepak Agrawal, Christopher Mann

**Year:** 2004 · **Venue:** Journal of Banking & Finance 28 (2004) 2747–2767

**Institutions:** Stern School of Business, NYU; KMV Moody's; Moody's

## Summary

A rating is not a sufficient description of a corporate bond. Much of the
rating-based pricing literature assumes bonds sharing a Moody's or S&P letter
grade are homogeneous in risk, and fits one spot curve per grade. This paper
shows that assumption fails, and identifies which extra bond characteristics the
market actually prices.

The method is plain. Bonds are grouped by Moody's rating, monthly spot curves are
fitted with the [[concepts/nelson-siegel-model|Nelson-Siegel]] procedure,
promised cash flows are discounted at those rates in the spirit of Duffie and
Singleton, and the residual — model price minus invoice price — is sorted on
candidate characteristics. Data is the Lehman Brothers Fixed Income database
(Warga), investment grade only, 1987–1996, excluding matrix-priced bonds and
bonds with options or odd coupon structures.

## Findings

Five influences produce systematic pricing errors within a rating class:

- **Notching.** Plus-rated bonds are priced above the model, minus-rated below,
  and the gap widens with maturity and with lower ratings.
- **Agency disagreement.** When S&P rates a bond below Moody's, investors price
  it as riskier than the Moody's grade implies. Neither agency dominates.
- **Coupon.** High-coupon bonds carry positive errors that grow with maturity,
  low-coupon bonds negative — the pattern a tax-timing effect would produce.
- **Bond versus issuer rating.** Where a bond is rated above its issuer,
  investors price it below model. They weight default probability more heavily,
  and expected recovery less, than the rating agency does.
- **New issues.** Bonds in their first year sell at a premium to model prices.
  Beyond that first year there is no age effect at all.

Note what did **not** work: dollar amount outstanding and the share of months a
bond was matrix-priced showed no significant pattern. Only the new-issue premium
carried a [[concepts/bond-liquidity|liquidity]] signal.

Building these five into the spot-rate estimation reduces mean absolute pricing
error in every one of the six sector-rating categories over the full period.
Relative to the improvement obtainable by simply subtracting each bond's own
recent average error, the characteristic adjustment captures 38–49% for
industrial bonds and 2–45% for financials.

## Why It Matters

Any rating-based model — whether it discounts cash flows or works through
risk-neutral probabilities, as in [[concepts/reduced-form-credit-models|reduced
form credit models]] — inherits these biases unless corrected. The authors argue
the resulting models are not merely inefficient but biased against identifiable
classes of bonds.

## Open Questions

- The sample is investment grade only and ends in 1996. Does notching still carry
  independent pricing information after TRACE-era transparency?
- The paper reads coupon effects as taxes but concedes coupon may proxy for
  something else.

## See Also

[[concepts/corporate-bonds|Corporate Bonds]] ·
[[concepts/credit-spread-curve|Credit Spread Curve]] ·
[[concepts/zero-coupon-curve|Zero Coupon Curve]] ·
[[concepts/bond-liquidity|Bond Liquidity]]

**Not yet written:** `rating-agency-notching`, `tax-timing-option`,
`recovery-rate-estimation`, `matrix-pricing`, `duffie-singleton-model`.
<!-- AUTHORED REGION END -->

