---
title: Do Changes in the Implied Volatility of Stock Options Predict Future Changes
  in CDS Spreads?
page_id: sources/hong-2025-implied-vol-cds-korea
page_type: source
source_path: markdown_output/jdqs-12-2024-0048.md
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:22:22Z'
authors:
- Changsoo Hong
- Yuen Jung Park
year: 2025
venue: Journal of Derivatives and Quantitative Studies
tags:
- cds
- implied-volatility
- default-risk
- korea
- cross-sectional-prediction
sources: []
related:
- concepts/credit-default-swaps
- concepts/implied-volatility-surface
- concepts/capital-structure-arbitrage
mind_map_priority: medium
schema_version: 2
uuid: 49a7bc11-3962-57df-9e09-8e4cf59c20e4
content_hash: sha256:c051e4150c81e025cd12de0972a70f7ef1226b71aafc84ced944c9b4bfeee115
---

<!-- AUTHORED REGION START -->
# Do Changes in Implied Volatility Predict Future Changes in CDS Spreads?

**Authors:** Changsoo Hong (NICE Pricing & Information), Yuen Jung Park (Hallym University)

**Year:** 2025 · **Venue:** Journal of Derivatives and Quantitative Studies 33(2), 150–

## Summary

Tests whether changes in stock-option implied volatility predict future CDS spread changes **in the Korean market**, cross-sectionally. Two results:

1. **Portfolio sort.** Buy the portfolio with the largest implied volatility increases, sell the largest decreases, rebalance monthly: the average future CDS spread change is positive and statistically significant.
2. **Predictive regression.** Coefficients on implied volatility changes are significant in most specifications, and their magnitude is broadly stable across control sets.

## What It Adds

It is an out-of-sample check on [[sources/cao-2023-implied-vol-bond-returns|Cao et al. (2023)]], and the authors frame it that way. Cao et al. argue that rising implied volatility signals higher default risk through higher firm-value volatility; this paper finds the same relationship in a different market and a different credit instrument — CDS rather than corporate bonds.

Two changes at once (market and instrument) make it a genuine replication test rather than a re-run. That it survives both is the interesting part.

## Context

The starting premise is the Easley et al. (1998) claim that informed traders reach the options market before others. This paper follows the resulting information from options into credit rather than into equity.

## Open Questions

- Korean CDS liquidity is thinner than US. How much of the significance survives realistic bid-offer?
- The paper tests prediction, not a tradeable strategy. Whether the signal nets out after costs is untested here.

## See Also

[[sources/cao-2023-implied-vol-bond-returns|Cao et al. (2023)]] · [[concepts/credit-default-swaps|Credit Default Swaps]] · [[concepts/implied-volatility-surface|Implied Volatility Surface]] · [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]]

<!-- AUTHORED REGION END -->
