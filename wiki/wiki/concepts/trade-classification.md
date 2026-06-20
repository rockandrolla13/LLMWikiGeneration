---
title: Trade Classification
page_id: concepts/trade-classification
page_type: concept
created: 2026-04-26 02:20:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- market-microstructure
- trade-signing
- machine-learning
- TRACE
- corporate-bonds
related:
- concepts/market-microstructure-noise
- concepts/trace-data
- sources/fedenia-2021-ml-trade-classifier
schema_version: 2
uuid: e11680ee-4237-5931-9316-7b69c31baaf7
content_hash: sha256:3ab28fb3f01ce3f5cd3ca99acb88eecf901eb18284f86ab5761927f9d30d9a52
---

<!-- AUTHORED REGION START -->
# Trade Classification

## Definition

Trade classification (trade signing) algorithms determine whether a transaction was buyer-initiated or seller-initiated. This is crucial for understanding order flow, price impact, and market dynamics.

## Classical Methods

### Tick Rule (TR)
- Uptick → Buy
- Downtick → Sell
- Zero-tick → Use last non-zero tick
- Accuracy: 62-83%

### Quote Rule (QR)
- Above midpoint → Buy
- Below midpoint → Sell
- Requires quote data

### Lee-Ready (LR)
- Combines TR and QR
- Uses QR when trade outside midpoint
- Uses TR when trade at midpoint

### Bulk Volume Classification (BVC)
- Easley et al. (2016)
- Based on price bars, not individual trades

## Machine Learning Approaches

### Random Forest Classifier
Fedenia, Ronen, and Nam (2021) show RF outperforms traditional methods:

| Comparison | Accuracy Improvement |
|-----------|---------------------|
| RF vs Tick Rule (bonds) | +8.3% |
| RF vs Tick Rule (equities) | +3.3% |
| RF vs Lee-Ready (equities) | +3.6% |

### Key Features
- Trade size
- Time of day
- Volatility measures
- Lagged prices
- Market conditions

## Factors Affecting Accuracy

### Positive Factors
- Higher liquidity
- Higher trade frequency
- Smaller trade size

### Negative Factors
- Information events (earnings)
- Low liquidity
- Large trades

## Corporate Bond Challenges

- No pre-trade transparency
- Lower trade frequency than equities
- Larger bid-ask spreads
- OTC market structure

## Data Sources

### TRACE Enhanced Historical Data
- Includes buy/sell indicators
- Enables supervised learning
- 17+ years of data

## Related Concepts

- [[concepts/market-microstructure-noise|Market Microstructure Noise]]
- [[concepts/trace-data|TRACE Data]]
- [[concepts/random-forest|Random Forest]]

## Sources

- [[sources/fedenia-2021-ml-trade-classifier|Fedenia et al. (2021)]]
- [[sources/dickerson-2024-bond-pitfalls|Dickerson et al. (2024)]]

<!-- AUTHORED REGION END -->
