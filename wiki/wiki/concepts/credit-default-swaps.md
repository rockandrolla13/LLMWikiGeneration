---
content_hash: sha256:b998c7c2734a9495874e28a173b14d662a726110743c93cfed42c968ccc7e47f
created: 2026-08-06 00:00:00+00:00
mind_map_priority: medium
page_id: concepts/credit-default-swaps
page_type: concept
related:
- concepts/credit-default-swap-spread
- concepts/cds-bond-basis
- concepts/hazard-rate-curve
revision_id: 5
schema_version: 2
sources:
- sources/shi-2022-cds-options-comovement
- sources/ubs-2012-next-gen-credit-curves
- sources/carr-2011-american-puts-credit-protection
- sources/chan-2023-price-convergence-cds-put-option
- sources/finger-2002-creditgrades-technical-document
- sources/lee-2021-cds-momentum-cross-market-spillovers
- sources/shi-2022-cds-implied-volatility-trading-strategies
- sources/yu-2006-how-profitable-capital-structure-arbitrage
- sources/bendor-2021-systematic-investing-in-credit
- sources/whitman-2009-distress-investing
- sources/marks-2006-the-new-paradigm
- sources/marks-2007-its-all-good
- sources/marks-2008-the-tide-goes-out
- sources/marks-2008-the-aviary
- sources/marks-2008-nobody-knows
- sources/marks-2008-plan-b
tags:
- credit-default-swaps
- credit-derivatives
- credit-risk
- CDS
- hazard-rate
title: Credit Default Swaps
updated: '2026-11-21T02:33:09Z'
updated_by: op_f506432cc7df
uuid: 56ee8e83-6a37-510a-a70d-61057edd1005
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

## Sources

- [[sources/whitman-2009-distress-investing|Distress Investing: Principles and Technique]] (2009)
- [[sources/bendor-2021-systematic-investing-in-credit|Systematic Investing in Credit]] (2021)
- [[sources/yu-2006-how-profitable-capital-structure-arbitrage|How Profitable Is Capital Structure Arbitrage?]]
- [[sources/shi-2022-cds-implied-volatility-trading-strategies|The Information Content of CDS Implied Volatility and Associated Trading Strategies]]
- [[sources/lee-2021-cds-momentum-cross-market-spillovers|CDS Momentum: Slow-Moving Credit Ratings and Cross-Market Spillovers]]
- [[sources/finger-2002-creditgrades-technical-document|CreditGrades Technical Document]]
- [[sources/chan-2023-price-convergence-cds-put-option|Price Convergence Between Credit Default Swap and Put Option: New Evidence]]
- [[sources/carr-2011-american-puts-credit-protection|A Simple Robust Link Between American Puts and Credit Protection]]

## In Howard Marks's Memos

- [[sources/marks-2006-the-new-paradigm|The New Paradigm]] (2006)
- [[sources/marks-2007-its-all-good|It's All Good]] (2007)
- [[sources/marks-2008-the-tide-goes-out|The Tide Goes Out]] (2008)
- [[sources/marks-2008-the-aviary|The Aviary]] (2008)
- [[sources/marks-2008-nobody-knows|Nobody Knows]] (2008)
- [[sources/marks-2008-plan-b|Plan B]] (2008)
<!-- AUTHORED REGION END -->