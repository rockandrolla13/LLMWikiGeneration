---
title: High Frequency Multifractal Properties of Bitcoin
page_id: sources/stavroyiannis-2017-bitcoin-multifractal
page_type: source
source_type: conference-paper
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Stavros Stavroyiannis
- Vassilios Babalos
- Stelios Bekiros
- Salim Lahmiri
- Gazi Salah Uddin
year: 2017
venue: Econophysics Conference
tags:
- bitcoin
- cryptocurrency
- multifractal
- mfdfa
- wtmm
- high-frequency
- hurst-exponent
- long-memory
related:
- concepts/mfdfa
- concepts/long-memory
- concepts/stylized-facts
- concepts/cryptocurrency
- sources/koukorinis-stylized-facts
mind_map_priority: medium
schema_version: 2
uuid: 8c2b3732-1a7b-5803-9c96-1689555eb8c5
content_hash: sha256:dc4dfecaeb6acfe34f42c6413e2db823d05f59eb5df7de2beda99dd28bc2d3c6
---

<!-- AUTHORED REGION START -->
# High Frequency Multifractal Properties of Bitcoin

**Authors:** Stavros Stavroyiannis, Vassilios Babalos, Stelios Bekiros, Salim Lahmiri, Gazi Salah Uddin

**Year:** 2017

**Venue:** Econophysics and Data Driven Modelling of Market Dynamics, Conference Proceedings

**Institutions:** AGC Heraklion (Greece), IPAG Paris, Polytechnique Montréal, Linköping University

## Summary

This paper applies multifractal analysis techniques (WTMM and MFDFA) to high-frequency Bitcoin data to characterize its statistical properties. The authors find evidence of multifractality in Bitcoin returns, with time-varying Hurst exponents and fat-tailed distributions, suggesting market inefficiency and complex dynamics.

## Key Contributions

### 1. Dual Multifractal Methods
- Wavelet Transform Modulus Maxima (WTMM)
- Multifractal Detrended Fluctuation Analysis (MFDFA)
- Comparison of results from both methods
- Robustness check through methodological triangulation

### 2. High-Frequency Bitcoin Analysis
- Minute-level Bitcoin/USD data
- Characterization of short-term dynamics
- Evidence of multifractality at high frequencies
- Comparison with traditional financial assets

### 3. Market Efficiency Implications
- Multifractality suggests market inefficiency
- Persistent memory in price movements
- Opportunities for predictability
- Evolving market microstructure

## Methodology

### Data
- Bitcoin/USD exchange rate
- High-frequency (minute-level) data
- Multiple time periods analyzed
- Returns computed at various scales

### WTMM Analysis
- Continuous wavelet transform with Morlet wavelet
- Partition function Z(q,a) computed
- Scaling exponent τ(q) estimated
- Singularity spectrum f(α) derived

### MFDFA Analysis
- Detrending with polynomial fitting
- Fluctuation function F_q(s) for different q-orders
- Generalized Hurst exponent h(q)
- Multifractal spectrum width Δα

### Key Parameters
- q-orders: typically -10 to +10
- Scale ranges: multiple decades
- Detrending order: typically 2-3
- Statistical significance tests

## Key Results

### Multifractal Properties
| Measure | Value | Interpretation |
|---------|-------|----------------|
| Δα (spectrum width) | >0.5 | Strong multifractality |
| h(2) (Hurst exponent) | ~0.55 | Slight persistence |
| h(q) variation | Significant | Non-monofractal |

### Comparison with Traditional Assets
- Bitcoin shows stronger multifractality than equities
- More volatile and less efficient market
- Wider singularity spectrum
- Higher kurtosis in returns

### Temporal Dynamics
- Multifractal properties evolve over time
- Market maturation affects efficiency
- Crisis periods show different patterns
- Liquidity impacts scaling properties

## Implications

1. **Market Efficiency:** Bitcoin market shows inefficiency signatures
2. **Risk Management:** Fat tails require non-Gaussian models
3. **Trading Strategies:** Persistence implies predictability potential
4. **Volatility Modeling:** Multifractal models may outperform GARCH

## Technical Details

### WTMM Procedure
1. Compute wavelet transform W_ψ[f](a,b)
2. Find local maxima at each scale
3. Connect maxima into maxima lines
4. Compute partition function along lines
5. Extract scaling exponents

### MFDFA Procedure
1. Compute cumulative sum of returns
2. Divide into non-overlapping segments
3. Fit polynomial trend in each segment
4. Compute fluctuation function F(s)
5. Estimate scaling exponent via regression

### Singularity Spectrum
```
f(α) = α × q - τ(q)
α = dτ/dq
```
Width Δα = α_max - α_min measures multifractal strength

## See Also

- [[concepts/mfdfa|MFDFA]]
- [[concepts/long-memory|Long Memory]]
- [[concepts/stylized-facts|Stylized Facts]]
- [[concepts/cryptocurrency|Cryptocurrency]]
- [[sources/koukorinis-stylized-facts|Koukorinis et al. Stylized Facts]]

<!-- AUTHORED REGION END -->
