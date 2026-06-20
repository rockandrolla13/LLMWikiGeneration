---
title: Cross-correlations between price and volume in Chinese gold markets
page_id: sources/ruan-2016-mfdcca-gold
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Qingsong Ruan
- Wei Jiang
- Guofeng Ma
year: 2016
venue: Physica A
tags:
- multifractal-analysis
- mf-dcca
- gold-markets
- price-volume
- cross-correlation
- chinese-markets
related:
- concepts/multifractal-analysis
- concepts/mf-dcca
- concepts/detrended-fluctuation-analysis
- concepts/long-range-correlation
mind_map_priority: medium
schema_version: 2
uuid: 747e49c8-bb63-5076-b89c-7899ee5e961c
content_hash: sha256:edbf60f80d1406f7ee7fd0f196862238419d44c7d26c98fb0d05d7a0ef471512
---

<!-- AUTHORED REGION START -->
# Cross-correlations between Price and Volume in Chinese Gold Markets

**Authors:** Qingsong Ruan, Wei Jiang, Guofeng Ma

**Year:** 2016

**Venue:** Physica A 451, 10-22

**Institution:** Tongji University, Shanghai

## Summary

This paper applies Multifractal Detrended Cross-Correlation Analysis (MF-DCCA) to investigate cross-correlation behaviors between price and volume in Chinese gold spot and futures markets. The study reveals significant multifractal features and examines time-varying properties using rolling windows.

## Key Contributions

### 1. Qualitative Analysis
- Cross-correlation test statistics Qcc(m)
- DCCA coefficients rho_DCCA
- Significant cross-correlations between price and volume

### 2. Quantitative MF-DCCA Results
- Power-law cross-correlation confirmed
- Significant multifractal features in both markets
- Different multifractality sources for spot vs. futures

### 3. Multifractality Sources
- **Gold spot market:** Fat-tail distribution is the main contributor
- **Gold futures market:** Both long-range correlations and fat-tail distributions contribute

### 4. Time-varying Analysis
- Rolling window methodology
- Short-term: obvious fluctuations due to exogenous shocks
- Long-term: cross-correlation tends to metastable level
- Generally antipersistent cross-correlations

## Methodology

### MF-DCCA Steps
1. Construct profile of time series
2. Divide into non-overlapping windows
3. Calculate local polynomial trends
4. Compute detrended covariance
5. Calculate q-order fluctuation function
6. Determine generalized Hurst exponent

### Comparative Analysis
- Original series vs. shuffled series (destroys long-range correlations)
- Original series vs. surrogated series (destroys fat-tails)
- Isolates contribution of each multifractality source

## Key Findings

1. Price and volume are significantly cross-correlated in Chinese gold markets
2. Multifractal features are present in both spot and futures markets
3. Different mechanisms drive multifractality in spot vs. futures
4. Cross-correlations are generally antipersistent (H < 0.5)
5. Dynamic mechanisms lead to metastable long-term relationships

## Market Context

- Shanghai Futures Exchange (SHFE): 47,730 tons traded (2014)
- Shanghai Gold Exchange (SGE): 18,490 tons traded (2014)
- China: world's largest producer, second-largest consumer
- Gold used for hedging, investment, and industrial purposes

## See Also

- [[concepts/multifractal-analysis|Multifractal Analysis]]
- [[concepts/mf-dcca|MF-DCCA]]
- [[concepts/detrended-fluctuation-analysis|Detrended Fluctuation Analysis]]
- [[concepts/long-range-correlation|Long-range Correlation]]

<!-- AUTHORED REGION END -->
