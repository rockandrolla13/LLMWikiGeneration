---
title: Duration Times Spread (DTS)
page_id: concepts/duration-times-spread
page_type: concept
concept_type: technique
abstraction_level: intermediate
revision_id: 1
created: 2026-09-15 00:00:00+00:00
updated: '2026-09-15T00:00:00Z'
tags:
- duration-times-spread
- spread-volatility
- corporate-bonds
- risk-model
sources:
- sources/bendor-2007-dts
- sources/houweling-2017-factor-investing
related:
- concepts/credit-spread-changes
- concepts/factor-models
- concepts/volatility-targeting-position-sizing
- concepts/bond-momentum
- concepts/residual-momentum
mind_map_priority: high
schema_version: 2
uuid: b7cc11c4-27e0-5d26-ba5b-5f78ea4aca34
content_hash: sha256:8069ded7c105939439244cfc441727b5da6d70515dd3f17c55a2b00be1aec872
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
<!-- AUTHORED REGION END -->
