---
title: Bond Liquidity
page_id: concepts/bond-liquidity
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- liquidity
- corporate-bonds
- otc-markets
- credit-spreads
- market-microstructure
sources:
- sources/huang-2025-global-credit-spread-puzzle
- sources/fermanian-2017-md2c-corporate-bonds
- sources/dickerson-2024-bond-pitfalls
- sources/kumar-2022-liquidity-adjusted-afns
related:
- concepts/credit-spread-puzzle
- concepts/structural-models
- concepts/corporate-bond-liquidity-premium
- concepts/liquidity-risk
mind_map_priority: medium
schema_version: 2
uuid: 98af7bca-952d-5087-b72a-c1d874f057a6
content_hash: sha256:734f6339fac9478832b387cec548e6ae58a419cf9b9f49e770cf4cf0298afaa0
---

<!-- AUTHORED REGION START -->
# Bond Liquidity

How readily a bond can be traded, and at what cost. In corporate credit this is a first-order pricing input rather than a refinement, because the market is over-the-counter, fragmented across many bonds per issuer, and mostly untraded on any given day.

## How Thin the Market Is

[[sources/fermanian-2017-md2c-corporate-bonds|Fermanian, Guéant & Pu (2017)]] record the scale of the problem: SIFMA estimates roughly six times more listed corporate bonds than stocks, and only about **1% of TRACE-eligible bonds traded on a given day in 2012**. Bonds are illiquid and heterogeneous, with several instruments outstanding per issuer. Basel III has also affected how much inventory dealers are willing to hold.

## Liquidity in the Price

[[sources/huang-2025-global-credit-spread-puzzle|Huang, Nozawa & Shi (2025)]] make liquidity the resolution rather than a residual. Standard [[concepts/structural-models|structural models]] underpredict investment-grade spreads; the He-Milbradt model, which puts search and bargaining frictions into the secondary debt market, lifts cross-sectional R² from 19–35% to 34–79%. The unexplained part of the spread is substantially a liquidity component. See [[concepts/credit-spread-puzzle|Credit Spread Puzzle]] and [[concepts/corporate-bond-liquidity-premium|Corporate Bond Liquidity Premium]].

The same conclusion arrives from the government-bond side. [[sources/kumar-2022-liquidity-adjusted-afns|Kumar & Virmani (2022)]] extend an arbitrage-free Nelson-Siegel model with both security-specific liquidity (turnover, bond age, duration) and a latent systematic funding-liquidity factor; a likelihood ratio test rejects the standard model in favour of the liquidity-adjusted one.

## Liquidity as a Measurement Hazard

Illiquidity does not only widen spreads — it corrupts the data. [[sources/dickerson-2024-bond-pitfalls|Dickerson, Robotti & Rossetti (2024)]] show that bid-ask contamination in TRACE transaction prices manufactures apparent predictability: after correcting for market microstructure noise, the monthly short-term reversal premium falls from 0.90% to roughly zero. Any strategy built on price-based signals in an illiquid market has to clear this bar first.

## See Also

[[concepts/credit-spread-puzzle|Credit Spread Puzzle]] · [[concepts/structural-models|Structural Models]] · [[concepts/corporate-bond-liquidity-premium|Corporate Bond Liquidity Premium]] · [[concepts/liquidity-risk|Liquidity Risk]] · [[concepts/illiquidity-premium|Illiquidity Premium]] · [[concepts/market-microstructure-noise|Market Microstructure Noise]] · [[concepts/request-for-quotes|Request for Quotes]] · [[concepts/corporate-bonds|Corporate Bonds]]

**Not yet written:** `concepts/search-and-bargaining-frictions`, `concepts/dealer-inventory`

<!-- AUTHORED REGION END -->
