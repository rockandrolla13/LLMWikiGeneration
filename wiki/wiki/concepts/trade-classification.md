---
content_hash: sha256:3ab28fb3f01ce3f5cd3ca99acb88eecf901eb18284f86ab5761927f9d30d9a52
created: 2026-04-26 02:20:00+00:00
page_id: concepts/trade-classification
page_type: concept
related:
- concepts/market-microstructure-noise
- concepts/trace-data
- sources/fedenia-2021-ml-trade-classifier
revision_id: 1
schema_version: 2
sources:
- sources/anantha-2024-forecasting-high-frequency-order-flow-imbalance
- sources/andersen-2013-assessing-measures-order-flow-toxicity-early
- sources/andersen-2013-reflecting-vpin-dispute
- sources/balagan-2026-learning-polymarket-taker-trade-direction-chain
- sources/bambade-2019-assessment-prediction-quality-vpin
- sources/barardehi-2025-revisiting-shaped-patterns-volatility-price-impacts
- sources/bongaerts-2025-cross-sectional-identification-private-information
- sources/calcada-2016-microstructural-changes-befor-macroeconomic-announcements-predictability
- sources/eisler-2011-price-impact-order-book-events-market
- sources/feigin-2015-assessing-informed-trading-measures-against-material
- sources/he-2016-volume-synchronised-probability-informed-trading-chinese
- sources/jiang-2015-volume-synchronized-probability-informed-trading-vpin
- sources/kalev-2025-lietf-trading-behavior-during-u-s
- sources/kang-2019-flow-toxicity-highfrequency-trading-its-impact
- sources/karyampas-2011-probability-informed-trading-volatility-etf
- sources/lee-2017-informed-trading-futures-markets-during-financial
- sources/lu-2009-essays-behavioral-finance-market-microstructure
- sources/lu-2023-trade-co-occurrence-trade-flow-decomposition
- sources/nieduzak-2014-ekonometryczna-analiza-prawdopodobienstwa-zawarcia-transakcji-wynikajacych
- sources/nittoor-2025-order-flow-filtration-directional-association-short
- sources/peng-2025-prediction-high-frequency-futures-return-directions
- sources/qin-2026-polymarket-v1-database
- sources/scalia-1998-information-transmission-causality-italian-treasury-bond-market
- sources/siqueira-2023-analise-dos-algoritmos-tick-rule-e
- sources/siqueira-2023-analysis-tick-rule-bulk-volume-classification
- sources/song-2014-parameter-analysis-vpin-volume-synchronized-probability
- sources/toke-2022-marked-point-processes-intensity-ratios-limit
- sources/turkoglu-2015-natural-time-crash-risk
- sources/wu-2013-big-data-approach-analyzing-market-volatility
- sources/zheng-2013-price-jump-prediction-limit-order-book
tags:
- market-microstructure
- trade-signing
- machine-learning
- TRACE
- corporate-bonds
title: Trade Classification
updated: '2026-09-27T01:47:00Z'
uuid: e11680ee-4237-5931-9316-7b69c31baaf7
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