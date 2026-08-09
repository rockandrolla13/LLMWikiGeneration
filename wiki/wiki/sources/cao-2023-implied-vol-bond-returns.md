---
title: Implied Volatility Changes and Corporate Bond Returns
page_id: sources/cao-2023-implied-vol-bond-returns
page_type: source
source_path: markdown_output/EBSCO-FullText-08_05_2026.md
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:22:22Z'
authors:
- Jie Cao
- Amit Goyal
- Xiao Xiao
- Xintong Zhan
year: 2023
venue: Management Science
tags:
- corporate-bonds
- implied-volatility
- default-risk
- information-diffusion
- capital-structure-arbitrage
sources: []
related:
- concepts/implied-volatility-surface
- concepts/credit-default-swaps
- concepts/capital-structure-arbitrage
- concepts/structural-models
mind_map_priority: high
schema_version: 2
uuid: a8f506c1-1cec-51da-aa42-e9cdea5110d3
content_hash: sha256:e34666a3a810a1ea906351dfab236e01e5e325e09aa3bc34be5d78c1071aecb4
---

<!-- AUTHORED REGION START -->
# Implied Volatility Changes and Corporate Bond Returns

**Authors:** Jie Cao, Amit Goyal, Xiao Xiao, Xintong Zhan

**Year:** 2023 · **Venue:** Management Science 69(3), 1375–1397

**Institutions:** Hong Kong Polytechnic University; University of Lausanne and Swiss Finance Institute; Bayes Business School, City University London; Fudan University

## Summary

Corporate bonds whose options showed large increases in implied volatility over the past month **underperform those with large decreases by 0.6% per month**. The paper argues this is not the usual fundamental-news story: implied volatility changes carry information about **uncertainty shocks to the firm**, and the corporate bond market underreacts to it.

## The Argument

Options are redundant assets only in perfect markets (Black-Scholes, Merton). Real frictions — transaction costs, short-sale constraints, segmented markets — push informed traders into options rather than stocks or bonds. So the option market prices new information about firm risk first, and the bond market follows late.

The distinction the paper draws matters: prior work reads implied volatility changes as news about **fundamentals**; here they are read as news about **risk**, specifically the volatility of firm value. That is the quantity a [[concepts/structural-models|structural credit model]] cares about, so a rise in implied volatility is a rise in default probability. See [[concepts/merton-model|Merton Model]].

## Why It Sits in the Capital-Structure Arbitrage Cluster

The trade it implies is the equity-to-credit direction: read the option market, act in the bond market. That is the same information channel [[concepts/capital-structure-arbitrage|capital structure arbitrage]] exploits, expressed as a cross-sectional bond strategy rather than a paired hedge.

## Open Questions

- The 0.6% monthly spread is gross. What survives corporate bond transaction costs, given the liquidity problems documented in [[concepts/bond-liquidity|bond liquidity]]?
- Does the underreaction persist after 2023, or has it been arbitraged away?

## See Also

[[concepts/implied-volatility-surface|Implied Volatility Surface]] · [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]] · [[concepts/structural-models|Structural Models]] · [[concepts/merton-model|Merton Model]] · [[concepts/bond-liquidity|Bond Liquidity]]

[[sources/hong-2025-implied-vol-cds-korea|Hong & Park (2025)]] replicates this result in Korean CDS.

<!-- AUTHORED REGION END -->
