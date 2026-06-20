---
authors:
- Andreas Koukorinis
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/koukorinis-2024-xantium-business-plan
page_type: source
publication_date: '2024'
publication_venue: null
related:
- concepts/etf-creation-redemption-arbitrage
- concepts/factor-signals-in-credit
- concepts/fractional-kelly-position-sizing
- concepts/non-fundamental-demand-shocks
- concepts/systematic-credit-relative-value
- entities/andreas-koukorinis
- entities/xantium
revision_hash: sha256:b6c1ec84d780908b5bd5efb9bd00485dbb37feff24ae78ee68e13f1ce1e17ccd
revision_id: 1
source_hash: sha256:5620d7a2b54082356e8b54953ff368d23f503fad9fe9918c6af0267d1cd9b411
source_path: raw/creditmacro/XantimumBizPlan.md
source_type: notes
sources: []
tags:
- business-plan
- systematic-trading
- credit
- etf-arbitrage
- relative-value
- fixed-income
- risk-management
title: 'Business Plan Details for Xantium: Systematic Spread Fixed Income Trading'
updated: '2026-06-20T01:03:51Z'
updated_by: op_0d00a43bc19a
schema_version: 2
uuid: 653c8d5d-33aa-55e5-8f4f-8992799b830f
content_hash: sha256:bddb0961be6b13b5207e9458e2348fe951b5be6d20b7228035cbae6a6a7154c5
---

<!-- AUTHORED REGION START -->
# Business Plan Details for Xantium: Systematic Spread Fixed Income Trading

**Authors:** Andreas Koukorinis · **Year:** 2024 · **Type:** business-plan

## Summary

A business plan by Andreas Koukorinis (11 April 2024) proposing Xantium, a systematic trading team focused on liquid credit relative value and cross-asset signals, with an overlay of listed equity options and interest-rate instruments. The core idea is to leverage the corporate bond ETF ecosystem, using the ETF creation/redemption framework to access liquidity and exploit episodic dislocations, framing ETF flows as symptomatic of non-fundamental demand shocks that authorized participants correct. Strategies span balance-sheet-intensive micro relative value (ETF vs basket, bond basket vs index/CDS/equity option) and macro RV (CDS index vs ETF basis, index compression). Signals include factor signals (momentum, value via distance-to-default, quality, liquidity via bond-CDS basis), technical signals, and create-to-lend episodic trades. Sizing uses an adapted fractional Kelly criterion; risk management emphasizes trade/portfolio construction over stop-losses.

## Key Claims

1. ETF flows have medium-term memory (momentum) driven by clientele differences between ETF-share and underlying-bond traders.
2. The ETF creation/redemption mechanism provides a liquidity conduit to thinly-traded underlying bonds.
3. ETF flows are symptomatic of non-fundamental demand shocks that deviate prices from fundamental value, with APs correcting law-of-one-price violations.
4. The core ETF-vs-basket strategy is market-neutral and delivers relative value alpha largely orthogonal to credit beta.
5. Trade sizing uses an adapted fractional Kelly criterion with gradient-based optimization of expected log-utility.
6. Risk is best managed through trade and portfolio construction rather than stop-loss discipline alone; no position has a stop wider than 2x its historical VaR.

## Questions Raised

- How many components are in the main strategy and which signals/sub-strategies are used?
- How are positions and the portfolio constructed and sized?
- How is residual curve/basis risk managed over longer holds?

## Concepts

- [[concepts/etf-creation-redemption-arbitrage|ETF Creation/Redemption Arbitrage]]
- [[concepts/systematic-credit-relative-value|Systematic Credit Relative Value]]
- [[concepts/factor-signals-in-credit|Factor Signals in Credit]]
- [[concepts/fractional-kelly-position-sizing|Fractional Kelly Position Sizing]]
- [[concepts/non-fundamental-demand-shocks|Non-Fundamental Demand Shocks]]

## Entities

- [[entities/andreas-koukorinis|Andreas Koukorinis]]
- [[entities/xantium|Xantium]]

## Source

- **Path:** `raw/creditmacro/XantimumBizPlan.md`
- **Type:** notes
- **Hash:** `sha256:5620d7a2b54082356...`
<!-- AUTHORED REGION END -->
