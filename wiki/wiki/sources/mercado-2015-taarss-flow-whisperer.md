---
authors:
- Sebastian Mercado
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/mercado-2015-taarss-flow-whisperer
page_type: source
publication_date: '2015'
publication_venue: Deutsche Bank Markets Research (Global Synthetic Equity & Index
  Strategy)
related:
- concepts/cross-asset-rotation
- concepts/etf-flow-anomalies
- concepts/etf-flow-tactical-asset-allocation
- concepts/taarss
- entities/deutsche-bank
- entities/sebastian-mercado
revision_hash: sha256:c05708d01d168a5a2908d79e66aede9d6c020b06804af3c5297a3df8ccff5a4f
revision_id: 1
source_hash: sha256:98b1403fad221c780a768d0f8a470369d8ea9e9649881e35a79b9c14b9fdd30a
source_path: raw/creditmacro/Taars.md
source_type: article
sources: []
tags:
- tactical-asset-allocation
- etf-flows
- cross-asset-rotation
- sell-side-research
- market-timing
title: 'The Flow Whisperer: TAARSS says prefer a mix of bonds and equities in Q1'
updated: '2026-06-09T12:00:00Z'
updated_by: op_a565c113018a
---

# The Flow Whisperer: TAARSS says prefer a mix of bonds and equities in Q1

**Authors:** Sebastian Mercado · **Year:** 2015 · **Venue:** Deutsche Bank Markets Research (Global Synthetic Equity & Index Strategy) · **Type:** report

## Summary

A Deutsche Bank sell-side strategy note (5 January 2015) presenting the monthly update of the Tactical Asset Allocation Relative Strength Signal (TAARSS), branded 'The Flow Whisperer'. TAARSS infers asset-allocation preferences from US-listed long-only ETF/ETV flow trends to drive monthly/quarterly cross-asset rotation. The methodology normalizes each ETF's cumulative cash-flow trend to AUM, then characterizes it by a regression-through-origin slope (magnitude) and a line-of-best-fit R-squared (path consistency); the TAARSS strength score is slope times R-squared, so only steep AND steady trends score highly. Signals are z-scored across 181 investment segments. The note flags create-to-lend / speculative ETF flow anomalies as false-positive risks.

## Key Claims

1. Short-term market moves are driven by supply/demand technical forces; ETF flow trends proxy shifts in the investment-demand curve.
2. TAARSS strength = slope of single linear regression through the origin (magnitude) multiplied by R-squared of the line-of-best-fit (path consistency).
3. Flow trends must be normalized to AUM, not measured in absolute dollars, to compare asset classes.
4. The universe is restricted to US-listed long-only, non-levered ETFs/ETVs; ETNs and leveraged/inverse products are excluded.
5. Speculative create-to-lend ETF inflows produce strong but misleading flow signals that should be discounted.

## Questions Raised

- How does TAARSS perform out-of-sample net of transaction costs given the short live track record?
- How are formation and rebalancing frequencies chosen, and how sensitive is performance to window lengths?
- Does ETF flow lead, lag, or merely coincide with the underlying asset price move?

## Concepts

- [[concepts/etf-flow-tactical-asset-allocation|ETF Flow-Based Tactical Asset Allocation]]
- [[concepts/taarss|Tactical Asset Allocation Relative Strength Signal (TAARSS)]]
- [[concepts/cross-asset-rotation|Cross-Asset Rotation Strategy]]
- [[concepts/etf-flow-anomalies|ETF Flow Anomalies (Create-to-Lend)]]

## Entities

- [[entities/sebastian-mercado|Sebastian Mercado]]
- [[entities/deutsche-bank|Deutsche Bank]]

## Source

- **Path:** `raw/creditmacro/Taars.md`
- **Type:** article
- **Hash:** `sha256:98b1403fad221c780...`