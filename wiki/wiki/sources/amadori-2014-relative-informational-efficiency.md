---
title: The Relative Informational Efficiency of Stocks, Options and Credit Default
  Swaps During the Financial Crisis
page_id: sources/amadori-2014-relative-informational-efficiency
page_type: source
source_path: markdown_output/jrf-04-2014-0044.md
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:22:22Z'
authors:
- Maria Chiara Amadori
- Lamia Bekkour
- Thorsten Lehnert
year: 2014
venue: Journal of Risk Finance
tags:
- cds
- implied-volatility
- price-discovery
- lead-lag
- financial-crisis
- europe
sources: []
related:
- concepts/credit-default-swaps
- concepts/implied-volatility-surface
- concepts/capital-structure-arbitrage
mind_map_priority: medium
schema_version: 2
uuid: efa7a90d-7aab-5f86-a84e-b08ae8ad7480
content_hash: sha256:3769553a2d8559b809e08cecccef0e83166469028aad123ed1bb36d6a09c27a5
---

<!-- AUTHORED REGION START -->
# Relative Informational Efficiency of Stocks, Options and CDS

**Authors:** Maria Chiara Amadori (Maastricht), Lamia Bekkour and Thorsten Lehnert (Luxembourg School of Finance)

**Year:** 2014 · **Venue:** Journal of Risk Finance 15(5), 510–

## Summary

Asks which of three markets — stocks, equity options, CDS — learns first, using European names. The design identifies what unique information each market holds about the future movements of the other two.

## Findings

**CDS leads.** Changes in CDS spreads consistently forecast both stock prices and equity option implied volatilities. The authors read this as the CDS market playing a special role in price discovery.

**But stocks lead too** — and this contradicts the US literature. Changes in stock prices forecast the other two markets, which suggests investors also act on information in equities before moving to CDS and options, rather than uniformly preferring derivatives.

**It is a crisis effect.** These lead-lag patterns emerge only during the financial crisis. Before it, the option market was the dominant one.

## Why That Last Point Matters

The information hierarchy between these markets is **not stable**. Any strategy built on "market X leads market Y" is conditioning on a regime, and this paper shows the regime changed.

That is a direct caution to the results in [[sources/cao-2023-implied-vol-bond-returns|Cao et al. (2023)]] and [[sources/hong-2025-implied-vol-cds-korea|Hong & Park (2025)]], both of which run options → credit. Amadori et al. find that direction dominant only in one period, and in Europe find credit → options instead.

## Open Questions

- Is the crisis-period reversal about information, or about which market stayed liquid enough to trade?
- Does the European stocks-lead result reflect market structure, or the sample?

## See Also

[[concepts/credit-default-swaps|Credit Default Swaps]] · [[concepts/implied-volatility-surface|Implied Volatility Surface]] · [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]] · [[sources/cao-2023-implied-vol-bond-returns|Cao et al. (2023)]]

**Not yet written:** `concepts/price-discovery`, `concepts/lead-lag-relationships`

<!-- AUTHORED REGION END -->
