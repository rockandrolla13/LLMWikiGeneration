---
content_hash: sha256:acff2b235cac04aa2e438806699f25aaf50c3fbbf13963e90a49dcd75bec7921
created: 2026-04-26 02:20:00+00:00
page_id: concepts/market-microstructure-noise
page_type: concept
related:
- concepts/trace-data
- concepts/look-ahead-bias
- sources/dickerson-2024-bond-pitfalls
- entities/alexander-dickerson
revision_id: 1
schema_version: 2
sources:
- sources/angstmann-2026-non-unique-time-market-incompleteness
- sources/bonart-2018-continuous-efficient-fundamental-price-discrete-order
- sources/busetto-2023-continuous-time-modeling-financial-returns-based
- sources/chang-2021-epps-effect-under-alternative-sampling-schemes
- sources/dahlhaus-2013-online-spot-volatility-estimation-decomposition-nonlinear
- sources/dahlhaus-2016-volatility-decomposition-estimation-time-changed-price
- sources/dimitriadis-2022-efficient-sampling-realized-variance-estimation-time
- sources/fayyaz-2026-frequency-controlled-comparison-tick-minute-based
- sources/gebbie-2026-gabor-epps-uncertainty-principle-traders
- sources/hirnschall-2020-deep-learning-approach-analyzing-limit-order
- sources/jonuzaj-2024-information-content-book-trade-order-flow
- sources/kong-2025-volatility-estimation-agricultural-futures-markets-microstructure
- sources/li-2023-empirical-analysis-financial-markets-insights-application
- sources/nousi-2019-machine-learning-forecasting-mid-price-movements
- sources/ntakaris-2019-feature-engineering-mid-price-prediction-deep
- sources/oomen-2004-properties-realized-variance-pure-jump-process
- sources/scaillet-2017-high-frequency-jump-analysis-bitcoin-market
- sources/tunyavetchakit-2016-volatility-decomposition-nonparametric-estimation-spot-volatility
- sources/valenzuela-2015-relative-liquidity-future-volatility
- sources/vlasiuk-2025-push-response-anomalies-high-frequency-s
- sources/wang-2025-exploring-microstructural-dynamics-cryptocurrency-limit-order
tags:
- market-microstructure
- bid-ask-spread
- TRACE
- corporate-bonds
- data-quality
title: Market Microstructure Noise
updated: '2026-09-27T01:47:00Z'
uuid: d928d80a-dbf5-59ff-a024-257fee054902
---

<!-- AUTHORED REGION START -->
# Market Microstructure Noise (MMN)

## Definition

Market microstructure noise refers to deviations between observed transaction prices and true fundamental values, primarily caused by bid-ask bounce and other trading frictions. In corporate bonds, MMN is particularly severe due to lower liquidity compared to equities.

## Sources of MMN

### Bid-Ask Bounce
- Transaction prices alternate between bid and ask
- Creates artificial negative autocorrelation in returns
- Bid-ask averaged prices still contain bias

### Other Sources
- Discrete price changes
- Information asymmetry
- Dealer inventory effects
- Stale prices in illiquid bonds

## Impact on Bond Research

### Spurious Predictability
Price-based signals from month t-1 are mechanically linked to month t returns, creating false predictability.

### Affected Strategies
- **Short-term reversal**: Premium drops >90% after MMN correction
- **Credit spreads**: 50-65% reduction in premia
- **Yields and prices**: Significant bias in signals

### Example: Reversal Strategy
| Metric | Before MMN Correction | After MMN Correction |
|--------|----------------------|---------------------|
| Monthly Premium | 0.90% | ~0% |

## MMN Correction Methods

### Implementation Gap
Use end-of-month t-1 prices with beginning-of-month t prices to purge bid-ask bias.

### Quote-Based Data
Industry-grade dealer quote data (expensive) avoids transaction-based bias.

### Data Resources
- **openbondassetpricing.com**: MMN-corrected TRACE data
- **PyBondLab**: Open-source correction code

## Implications

1. Many published bond anomalies may be spurious
2. Price-based signals require careful handling
3. Ex-ante filtering essential (not ex-post)
4. Corporate bond market inherently noisier than equities

## Related Concepts

- [[concepts/trace-data|TRACE Data]]
- [[concepts/look-ahead-bias|Look-ahead Bias]]
- [[concepts/trade-classification|Trade Classification]]

## Sources

- [[sources/dickerson-2024-bond-pitfalls|Dickerson et al. (2024)]]
- [[sources/fedenia-2021-ml-trade-classifier|Fedenia et al. (2021)]]

<!-- AUTHORED REGION END -->