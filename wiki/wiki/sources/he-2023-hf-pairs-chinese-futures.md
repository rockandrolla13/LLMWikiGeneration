---
title: An Innovative High-Frequency Statistical Arbitrage in Chinese Futures Market
page_id: sources/he-2023-hf-pairs-chinese-futures
page_type: source
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- statistical-arbitrage
- pairs-trading
- kalman-filter
- chinese-futures
- hurst-index
- cointegration
- high-frequency
authors:
- Chengying He
- Tianqi Wang
- Xinwen Liu
- Ke Huang
year: 2023
related:
- concepts/kalman-filter
- concepts/statistical-arbitrage
- concepts/pairs-trading
- concepts/cointegration
- concepts/hurst-exponent
- concepts/mean-reversion
schema_version: 2
uuid: 321c0983-0ac2-5e28-9aa1-b08b12e8ec3e
content_hash: sha256:f211f1f646787d42e05cab8ef2d433209a41c1fe48ad70cb6836a429ecaa9de0
---

<!-- AUTHORED REGION START -->
## Summary

This paper establishes an innovative pairs trading framework for the Chinese commodity futures market using cointegration tests, Kalman filter, and Hurst index filtering. The framework is tested on minute-level data from 47 commodity futures with relatively good liquidity.

## Key Contributions

- Develops comprehensive pairs trading framework combining multiple filtering criteria
- Introduces adaptive Hurst index for confirming mean-reversion characteristics
- Achieves 81% cumulative in-sample returns and 21% out-of-sample returns
- Maximum drawdown of only 1% out-of-sample (vs 15% for buy-and-hold benchmark)
- Provides evidence that Chinese futures market is not weak-form efficient

## Methodology

### Framework Components

1. **Cointegration Test**: Uses Johansen test to identify pairs with long-term equilibrium relationship

2. **ADF Test**: Confirms stationarity of spread series

3. **Kalman Filter Regression**:
   - Estimates dynamic hedge ratio (arbitrage ratio)
   - Calculates mean-reversion half-life from filtered coefficients
   - Adapts to time-varying cointegration relationships

4. **Hurst Index Filtering**:
   - Uses Adaptive Fractal Analysis (AFA) method
   - Confirms mean-reverting behavior (H < 0.5)
   - Filters out pairs with trending characteristics

### Trading Rules

- Open positions when Z-score exceeds threshold
- Close positions on mean reversion
- Uses normalized spread for consistent signal generation

## Data

- 47 commodities from Chinese commodity futures market
- 5-minute frequency data
- Benchmark: Wenhua Commodity Index

## Results

| Metric | Strategy | Benchmark |
|--------|----------|-----------|
| In-sample Return | 81% | 31% |
| Out-of-sample Return | 21% | - |
| Max Drawdown | 1% | 15% |

## Market Efficiency Implications

The paper argues that profitable technical analysis based on machine learning methods provides evidence against weak-form market efficiency in Chinese commodity futures.

## Related Concepts

- [[concepts/kalman-filter|Kalman Filter]] for dynamic parameter estimation
- [[concepts/cointegration|Cointegration]] for pair selection
- [[concepts/hurst-exponent|Hurst Exponent]] for mean-reversion detection
- [[concepts/pairs-trading|Pairs Trading]] strategy

## Citations

He, C., Wang, T., Liu, X., & Huang, K. (2023). An innovative high-frequency statistical arbitrage in Chinese futures market. Journal of Innovation & Knowledge, 8(4), 100429.

<!-- AUTHORED REGION END -->
