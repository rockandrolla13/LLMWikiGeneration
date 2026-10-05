---
content_hash: sha256:8acde5355f39b084565e03a596950bc915cb62e1ccb2ae1327bf46b3ea07d399
created: 2026-04-26 02:25:00+00:00
page_id: concepts/trace-data
page_type: concept
related:
- concepts/market-microstructure-noise
- concepts/trade-classification
- sources/dickerson-2024-bond-pitfalls
- sources/fedenia-2021-ml-trade-classifier
revision_id: 2
schema_version: 2
sources:
- sources/dickerson-2026-corporate-bond-factor-replication-crisis
tags:
- TRACE
- corporate-bonds
- data
- FINRA
- transaction-data
- market-microstructure
title: TRACE Data
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: 00820d48-f707-5df4-b4da-406a6fc26ac4
---

<!-- AUTHORED REGION START -->
# TRACE Data

## Definition

TRACE (Trade Reporting and Compliance Engine) is FINRA's mandatory reporting system for over-the-counter corporate bond transactions. It provides the primary data source for US corporate bond research.

## Data Versions

### Standard TRACE
- Publicly available
- Transaction price and volume
- Capped volume reporting (large trades masked)

### Enhanced TRACE
- Academic/research access
- Uncapped trade sizes
- Buy/sell indicators (post-2012)
- Dealer identification

### TRACE Enhanced Historical
- 17+ years of data (2002-present)
- Enables supervised learning for trade classification
- Buy/sell labels for training ML models

## Key Fields

| Field | Description |
|-------|-------------|
| CUSIP | Bond identifier |
| Trade Date/Time | When transaction occurred |
| Price | Transaction price |
| Volume | Trade size (capped in standard) |
| Buy/Sell | Direction (Enhanced only) |
| Dealer | Reporting party (Enhanced only) |

## Data Quality Issues

### Market Microstructure Noise
- Bid-ask bounce creates spurious patterns
- [[concepts/market-microstructure-noise|Market Microstructure Noise]]

### Stale Prices
- Infrequently traded bonds have outdated prices
- Month-end pricing particularly affected

### Reporting Delays
- Some trades reported with lag
- Reversals and corrections

## Cleaning Procedures

Standard filtering (Dickerson et al. 2024):
1. Remove canceled/corrected trades
2. Filter extreme prices (< $5, > $200)
3. Require minimum trading frequency
4. Remove special conditions

## Research Resources

### Open Data
- **openbondassetpricing.com**: MMN-corrected returns
- **WRDS**: Enhanced TRACE access
- **PyBondLab**: Open-source processing code

## Related Concepts

- [[concepts/market-microstructure-noise|Market Microstructure Noise]]
- [[concepts/trade-classification|Trade Classification]]
- [[concepts/look-ahead-bias|Look-ahead Bias]]

## Sources

- [[sources/dickerson-2026-corporate-bond-factor-replication-crisis|The Corporate Bond Factor Replication Crisis]]
- [[sources/dickerson-2024-bond-pitfalls|Dickerson et al. (2024)]]
- [[sources/fedenia-2021-ml-trade-classifier|Fedenia et al. (2021)]]

<!-- AUTHORED REGION END -->