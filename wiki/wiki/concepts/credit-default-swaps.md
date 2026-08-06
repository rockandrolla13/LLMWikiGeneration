---
title: Credit Default Swaps
page_id: concepts/credit-default-swaps
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- credit-default-swaps
- credit-derivatives
- credit-risk
- CDS
- hazard-rate
sources:
- sources/shi-2022-cds-options-comovement
- sources/ubs-2012-next-gen-credit-curves
related:
- concepts/credit-default-swap-spread
- concepts/cds-bond-basis
- concepts/hazard-rate-curve
mind_map_priority: medium
schema_version: 2
uuid: 56ee8e83-6a37-510a-a70d-61057edd1005
content_hash: sha256:03c49bebc20458a102a846ae7fcf1a8e182f4a2ad5c02802282e3a339370e793
---

<!-- AUTHORED REGION START -->
# Credit Default Swaps

Contracts that transfer default risk on a reference entity from protection buyer to protection seller. The price is the [[concepts/credit-default-swap-spread|CDS spread]] — the annualised cost of insuring the entity's debt. The wiki's standard input is the five-year senior unsecured spread.

## The Curve, Not the Point

CDS quotes exist across tenors, so the object of interest is a curve. [[sources/shi-2022-cds-options-comovement|Shi et al. (2022)]] model the CDS curve through the hazard rate rather than the spread directly, fitting a Nelson-Siegel form

h(τ) = β₁ + β₂·exp(−λτ) + β₃·(λτ)·exp(−λτ)

with β₁ the long-term default intensity (level), β₂ the term-structure steepness (slope), and β₃ the hump (curvature). They justify this by linking Carr & Wu's (2010) no-arbitrage model on hazard rates to the Nelson-Siegel form. Factors are extracted with an [[concepts/unscented-kalman-filter|unscented Kalman filter]], because the spread is a nonlinear function of the factors. See [[concepts/hazard-rate-curve|Hazard Rate Curve]].

## Link to Equity Options

Working on the investment-grade CDX index and S&P 500 options over 2002–2019 (939 weekly observations), Shi et al. find CDS level correlates with volatility level — the direct channel predicted by Carr & Wu's unit recovery claim argument, where deep out-of-the-money puts capture default probability. Slope co-movement runs indirectly through the stock return. Co-movement strengthened after the 2008–09 crisis, but once stock return is controlled for the relationship between the two markets becomes insignificant.

## Relation to Cash Bonds

CDS and bonds price the same credit differently; the gap is the [[concepts/cds-bond-basis|CDS-bond basis]], driven by funding (CDS is unfunded), delivery optionality, liquidity and counterparty risk. [[sources/ubs-2012-next-gen-credit-curves|UBS Delta (2012)]] treats both in one hazard-rate framework, which lets bond-implied CDS be derived for issuers with no traded CDS.

## See Also

[[concepts/credit-default-swap-spread|Credit Default Swap Spread]] · [[concepts/cds-bond-basis|CDS-Bond Basis]] · [[concepts/hazard-rate-curve|Hazard Rate Curve]] · [[concepts/nelson-siegel-model|Nelson-Siegel Model]] · [[concepts/unscented-kalman-filter|Unscented Kalman Filter]] · [[concepts/survival-probability|Survival Probability]] · [[concepts/spread-per-turn-of-leverage|Spread Per Turn of Leverage]]

**Not yet written:** `concepts/cdx-index`, `concepts/recovery-rate`, `concepts/unit-recovery-claim`


## CDS and the Equity/Options Markets

- [[sources/amadori-2014-relative-informational-efficiency|Amadori et al. (2014)]] -- CDS leads stocks and options, but only during the crisis
- [[sources/dafonseca-2020-cds-equity-volatility-comovement|Da Fonseca & Gottschalk (2020)]] -- equity returns lead CDS at firm level
- [[sources/hong-2025-implied-vol-cds-korea|Hong & Park (2025)]] -- option IV predicts CDS spread changes

<!-- AUTHORED REGION END -->
