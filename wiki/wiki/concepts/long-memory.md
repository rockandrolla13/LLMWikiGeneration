---
title: Long Memory
page_id: concepts/long-memory
page_type: concept
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- time-series
- autocorrelation
- hurst-exponent
- fractional-processes
- stylized-facts
sources:
- sources/gould-2016-long-memory-fx
- sources/koukorinis-stylized-facts
- sources/stavroyiannis-2017-bitcoin-multifractal
- sources/guillaume-1997-stylized-facts-fx
related:
- concepts/stylized-facts
- concepts/mfdfa
- concepts/hurst-exponent
- concepts/order-flow
- concepts/volatility-clustering
mind_map_priority: high
schema_version: 2
uuid: 4e52ab02-6398-57ca-8761-d68eb92746a3
content_hash: sha256:8b6c58ff41e7e8f31fc6aa72a95e8f760b3bfd6a55631700bf0cc62e93750339
---

<!-- AUTHORED REGION START -->
# Long Memory

**Long memory** (also called long-range dependence) is a property of time series where autocorrelations decay slowly, typically as a power law, such that their sum diverges. This property has profound implications for forecasting, risk management, and understanding market dynamics.

## Formal Definition

### Short Memory
A stationary time series {Wt} exhibits **short memory** if:
```
Σ |ρ(k)| < ∞
```
where ρ(k) is the autocorrelation at lag k.

### Long Memory
A stationary time series {Wt} exhibits **long memory** if:
```
Σ |ρ(k)| = ∞
```

### Power-Law Decay
For long-memory processes, autocorrelations typically decay as:
```
ρ(k) ~ C × k^(2H-2)  as k → ∞
```
where H is the Hurst exponent (0.5 < H < 1 for long memory).

## The Hurst Exponent

### Interpretation
| H Value | Behavior | Meaning |
|---------|----------|---------|
| 0 < H < 0.5 | Anti-persistent | Mean-reverting |
| H = 0.5 | Random walk | No memory |
| 0.5 < H < 1 | Persistent | Long memory |

### Estimation Methods
1. **R/S Analysis:** Rescaled range statistic
2. **DFA:** Detrended fluctuation analysis
3. **Log-Periodogram:** Geweke-Porter-Hudak regression
4. **Wavelet Methods:** Scale-based estimation

## Financial Applications

### Order Flow
- Trade signs exhibit long memory (H ≈ 0.7)
- Persists across daily boundaries [[sources/gould-2016-long-memory-fx|Gould et al. (2016)]]
- Implications for order splitting detection

### Volatility
- Absolute returns show long memory
- Volatility clustering is a manifestation
- FIGARCH models capture this property

### Returns
- Returns themselves typically show short memory
- Market efficiency implies H ≈ 0.5 for returns
- Slight deviations possible in less liquid markets

## Empirical Evidence

### FX Markets
- Order flow in EUR/USD, GBP/USD, EUR/GBP
- H ≈ 0.7 estimated from single-day data
- Robust across different estimation methods
- [[sources/gould-2016-long-memory-fx|Gould et al. (2016)]]

### Equity Markets
- LSE, NYSE order flow studies
- Similar Hurst exponents observed
- Cross-sectional variation exists

### Cryptocurrency
- Bitcoin shows multifractal properties
- Time-varying Hurst exponents
- [[sources/stavroyiannis-2017-bitcoin-multifractal|Stavroyiannis et al. (2017)]]

## Theoretical Mechanisms

### Order Splitting
- Large orders decomposed into smaller chunks
- Submitted over days or weeks
- Creates persistent order flow patterns

### Herding
- Traders imitate successful strategies
- Common information leads to similar actions
- Less supported by empirical evidence

### Market Maker Inventory
- Inventory cycles create correlation
- Mean-reversion at longer horizons
- Combines with order-splitting effects

## Detection Challenges

### Spurious Long Memory
- Structural breaks can mimic long memory
- Aggregation across regimes problematic
- Axioglou and Skouras (2011) critique

### Testing Approaches
- Lo's modified R/S test
- Berkes' change-point test
- Intra-day vs cross-day analysis

### Resolution
Gould et al. (2016) show long memory in FX:
- Single-day estimation (no aggregation needed)
- Structural break hypothesis rejected
- True long memory confirmed

## Related Concepts

### Multifractal Analysis
- Long memory is monofractal (single H)
- Markets may exhibit multifractality
- MFDFA captures spectrum of exponents
- [[sources/koukorinis-stylized-facts|Koukorinis et al. (2022)]]

### Fractional Processes
- ARFIMA (autoregressive fractionally integrated)
- Fractional Brownian motion
- Parameter d relates to H: d = H - 0.5

## Implications

### Forecasting
- Past values informative about distant future
- Standard models underestimate persistence
- Need long-memory models for accuracy

### Risk Management
- Volatility persistence affects VaR
- Longer-horizon risks systematically different
- Standard models may underestimate tail risks

### Market Efficiency
- Long memory in order flow is compatible with efficiency
- Prices adjust to neutralize predictability
- Information revelation vs execution needs

## See Also

- [[concepts/stylized-facts|Stylized Facts]]
- [[concepts/mfdfa|MFDFA]]
- [[concepts/order-flow|Order Flow]]
- [[sources/gould-2016-long-memory-fx|Gould et al. (2016) Long Memory in FX]]
- [[sources/koukorinis-stylized-facts|Koukorinis et al. Stylized Facts]]

<!-- AUTHORED REGION END -->
