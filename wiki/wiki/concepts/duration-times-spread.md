---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:b893092ecf801d1931348ebaf6e3ce45aae3ffee8c7df3c3230d3b917e38c02d
created: 2026-09-15 00:00:00+00:00
mind_map_priority: high
page_id: concepts/duration-times-spread
page_type: concept
related:
- concepts/credit-spread-changes
- concepts/factor-models
- concepts/volatility-targeting-position-sizing
- concepts/bond-momentum
- concepts/residual-momentum
revision_id: 4
schema_version: 2
sources:
- sources/bendor-2007-dts
- sources/houweling-2017-factor-investing
- sources/bendor-2021-systematic-investing-in-credit
- sources/bendor-2021-onescore-chapter-19
- sources/correia-2012-value-investing-credit-markets
- sources/israel-2017-common-factors-corporate-bond-returns
- sources/kricheff-2012-pragmatists-guide-leveraged-finance
tags:
- duration-times-spread
- spread-volatility
- corporate-bonds
- risk-model
title: Duration Times Spread (DTS)
updated: '2026-10-22T21:10:31Z'
updated_by: op_0cdb8cc1f169
uuid: b7cc11c4-27e0-5d26-ba5b-5f78ea4aca34
---

<!-- AUTHORED REGION START -->
# Duration Times Spread (DTS)

## Definition

DTS is a bond's spread duration multiplied by its spread. Where spread duration measures sensitivity to an absolute spread change (spreads widen 10 bp), DTS measures sensitivity to a relative spread change (spreads widen 10%). At portfolio level, the contribution to DTS is market weight times spread duration times spread.

## Why It Works

[[sources/bendor-2007-dts|Ben Dor et al. (2007)]] show on the Lehman Brothers Credit Index (1989–2005) that spread changes are proportional to spread level:
- **Systematic spread volatility** is about 9% of spread per month.
- **Idiosyncratic spread volatility** is about 11.5% of spread per month.

Excess-return volatility is therefore linear in DTS, with a slope of 8.8% and R² of 98%. Portfolios with different spreads and durations but equal DTS have equal volatility.

Volatility forecasts built as DTS times historical relative spread volatility are close to unbiased: normalised returns have a standard deviation of 1.01. The absolute-spread alternative gives 1.14 or 0.92, depending on the estimation window. The DTS forecast responds at once to spread moves, because it uses today's spread.

## Where It Breaks Down

- **Very tight spreads.** Below roughly 20 bp, volatility flattens to a structural floor from pricing noise and supply-demand effects: about 2.5–3.0 bp a month systematic and 4.0–4.5 bp idiosyncratic, on agency data.
- **Pricing noise.** Small price errors become larger spread errors, so DTS-based measures need clean prices.

## Uses in This Wiki

- **Risk measurement and allocation:** exposures, issuer limits and pair hedging, from [[sources/bendor-2007-dts|Ben Dor et al. (2007)]].
- **Factor definition:** [[sources/houweling-2017-factor-investing|Houweling & van Zundert (2017)]] define an alternative Low-Risk factor (LR3) as the 10% of bonds with the lowest DTS.
- **Signal scaling:** a candidate denominator for scaling bond returns in momentum signals, as a forward-looking alternative to realised volatility ([[concepts/bond-momentum|Bond Momentum]], [[concepts/residual-momentum|Residual Momentum]]). No source in the wiki tests DTS scaling for return prediction.

## Related Concepts

- [[concepts/credit-spread-changes|Credit Spread Changes]]
- [[concepts/factor-models|Factor Models]]
- [[concepts/volatility-targeting-position-sizing|Volatility-Based Position Sizing]]

## Sources

- [[sources/kricheff-2012-pragmatists-guide-leveraged-finance|A Pragmatist's Guide to Leveraged Finance: Credit Analysis for Bonds and Bank Debt]] (2012)
- [[sources/israel-2017-common-factors-corporate-bond-returns|Common Factors in Corporate Bond Returns]] (2017)
- [[sources/correia-2012-value-investing-credit-markets|Value Investing in Credit Markets]] (2012)
- [[sources/bendor-2021-onescore-chapter-19|OneScore: Combining Quantitative and Fundamental Views in Credit]] (2021, chapter 19)
- [[sources/bendor-2021-systematic-investing-in-credit|Systematic Investing in Credit]] (2021)
<!-- AUTHORED REGION END -->