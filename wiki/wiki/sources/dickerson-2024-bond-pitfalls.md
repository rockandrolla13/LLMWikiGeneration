---
title: "Common Pitfalls in the Evaluation of Corporate Bond Strategies"
page_id: sources/dickerson-2024-bond-pitfalls
page_type: source
created: 2026-04-26T01:45:00Z
updated: 2026-04-26T01:45:00Z
tags: [corporate-bonds, market-microstructure, bid-ask-bias, momentum, TRACE]
authors: [Alexander Dickerson, Cesare Robotti, Giulio Rossetti]
year: 2024
journal: Working Paper (SSRN)
related: [concepts/market-microstructure-noise, concepts/bond-momentum, concepts/trace-data, entities/alexander-dickerson]
---

# Common Pitfalls in the Evaluation of Corporate Bond Strategies

## Summary

A critical methodological paper demonstrating that large abnormal returns documented for many corporate bond strategies are artifacts of (1) ignoring market microstructure noise in TRACE transaction prices and (2) applying ex-post asymmetric data filtering with look-ahead bias.

## Key Findings

- **Short-term Reversal Illusion**: After MMN adjustment, the monthly reversal premium drops from 0.90% to approximately 0% - a >90% reduction
- **Bid-Ask Bias**: Price-based signals mechanically linked to next-month returns create spurious predictability
- **Look-ahead Bias**: Ex-post winsorization artificially inflates strategy returns, especially during crises
- **IG vs NIG**: After adjustment, IG bonds show weak reversal; NIG bonds show momentum

## Methodology

- Introduces MMN-correction using implementation gap to purge bid-ask bias
- Analyzes 100+ ex-ante data filtering methods
- Provides open-source PyBondLab software for replication
- Tests across dozens of bond strategies

## Critical Contributions

1. **Data Uncertainty Framework**: No single "truth" for corporate bond data handling
2. **Public Resources**: openbondassetpricing.com with corrected data and code
3. **Replication Crisis**: Explains failures in corporate bond research replication

## Key Concepts

- [[concepts/market-microstructure-noise|Market Microstructure Noise]] - bid-ask contamination
- [[concepts/trace-data|TRACE Data]] - transaction reporting system
- [[concepts/look-ahead-bias|Look-ahead Bias]] - ex-post filtering problems

## Notable Quotes

> "The vast majority of all corporate bond pricing related research that utilizes TRACE employs bond price-based signals that have not been adjusted for MMN"

## Implications

1. Many published bond anomalies may be spurious
2. Ex-ante filtering essential for valid out-of-sample tests
3. Quote-based data preferable but expensive
4. Simple MMN correction restores validity

## Related Sources

- [[sources/houweling-2017-factor-investing|Houweling & van Zundert (2017)]] - factor investing
- [[sources/jostova-2013-momentum|Jostova et al. (2013)]] - momentum in bonds
