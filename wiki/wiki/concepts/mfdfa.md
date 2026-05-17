---
title: "Multifractal Detrended Fluctuation Analysis (MFDFA)"
page_id: concepts/mfdfa
page_type: concept
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
tags: [multifractal, time-series, scaling, hurst-exponent, detrending, financial-analysis]
sources: [sources/koukorinis-stylized-facts, sources/stavroyiannis-2017-bitcoin-multifractal, sources/ruan-2016-mfdcca-gold, sources/aslam-2020-covid-mfdfa]
related: [concepts/long-memory, concepts/stylized-facts, concepts/hurst-exponent, concepts/wtmm]
mind_map_priority: high
---

# Multifractal Detrended Fluctuation Analysis (MFDFA)

**MFDFA** is a generalization of Detrended Fluctuation Analysis (DFA) that characterizes the multifractal properties of time series. It reveals how scaling behavior varies across different fluctuation magnitudes, capturing the rich structure of financial time series.

## Background

### From DFA to MFDFA
- **DFA:** Single Hurst exponent H
- **MFDFA:** Spectrum of exponents h(q)
- **Multifractality:** Different scaling for small vs large fluctuations

### Why Multifractal?
Financial time series often exhibit:
- Different scaling for extreme vs typical events
- Time-varying correlation structure
- Fat tails requiring multiple exponents

## Algorithm

### Step 1: Profile Construction
Given time series {xi}, i = 1,...,N:
```
Y(i) = Σ_{k=1}^{i} (x_k - <x>)
```

### Step 2: Segmentation
- Divide profile into Ns = int(N/s) non-overlapping segments of length s
- Repeat from end to get 2Ns segments total

### Step 3: Local Detrending
For each segment v, fit polynomial trend yv(i) and compute variance:
```
F²(v,s) = (1/s) Σ_{i=1}^{s} [Y((v-1)s + i) - y_v(i)]²
```

### Step 4: q-th Order Fluctuation Function
```
F_q(s) = [(1/2Ns) Σ_{v=1}^{2Ns} [F²(v,s)]^{q/2}]^{1/q}
```
For q = 0:
```
F_0(s) = exp{(1/4Ns) Σ_{v=1}^{2Ns} ln[F²(v,s)]}
```

### Step 5: Scaling Analysis
If long-range correlations exist:
```
F_q(s) ~ s^{h(q)}
```
where h(q) is the generalized Hurst exponent.

## Key Quantities

### Generalized Hurst Exponent h(q)
- h(2) = H (classical Hurst exponent)
- h(q) constant → monofractal (single scaling)
- h(q) varying → multifractal

### Mass Exponent τ(q)
```
τ(q) = qh(q) - 1
```

### Singularity Spectrum f(α)
Via Legendre transform:
```
α = dτ/dq = h(q) + qh'(q)
f(α) = qα - τ(q) = q[α - h(q)] + 1
```

### Multifractal Width
```
Δα = α_max - α_min
```
Larger Δα indicates stronger multifractality.

## Interpretation

### q > 0
- Large fluctuations dominate
- h(q) characterizes scaling of extreme events

### q < 0
- Small fluctuations dominate
- h(q) characterizes scaling of typical events

### q = 2
- Standard DFA
- Second-order correlation structure

## Applications

### Bitcoin Analysis
[[sources/stavroyiannis-2017-bitcoin-multifractal|Stavroyiannis et al. (2017)]]:
- Strong multifractality (Δα > 0.5)
- Market inefficiency signature
- Time-varying efficiency

### Gold-Oil Cross-Correlations
[[sources/ruan-2016-mfdcca-gold|Ruan et al. (2016)]]:
- MF-DCCA for bivariate analysis
- Cross-correlation scaling
- Asymmetric dependence

### Stylized Facts
[[sources/koukorinis-stylized-facts|Koukorinis et al. (2022)]]:
- Information clock transformations
- Time-varying inefficiency detection
- Futures market analysis

### COVID-19 Market Analysis
[[sources/aslam-2020-covid-mfdfa|Aslam et al. (2020)]]:
- European stock market multifractality during pandemic
- 5-minute intraday data analysis
- STL preprocessing before MFDFA

## Comparison with WTMM

### Wavelet Transform Modulus Maxima
- Alternative multifractal method
- Based on continuous wavelet transform
- Different numerical properties

### MFDFA Advantages
- Simpler implementation
- More robust to polynomial trends
- Works well for short series

### WTMM Advantages
- Better scale localization
- More direct singularity detection
- Established mathematical foundation

## Practical Considerations

### Parameter Selection
- **q range:** Typically -10 to +10
- **Scale range:** Multiple decades needed
- **Detrending order:** Usually 2-3

### Statistical Significance
- Bootstrap confidence intervals
- Shuffled surrogate comparison
- Multiple realization averaging

### Common Pitfalls
- Insufficient scale range
- Edge effects at extremes of q
- Confusing trend with true multifractality

## Extensions

### MF-DCCA
Multifractal detrended cross-correlation analysis:
- Bivariate extension
- Cross-correlation scaling
- Asymmetric relationships

### MF-DFA Variants
- Different detrending methods
- Wavelet-based detrending
- Adaptive windowing

## See Also

- [[concepts/long-memory|Long Memory]]
- [[concepts/stylized-facts|Stylized Facts]]
- [[concepts/hurst-exponent|Hurst Exponent]]
- [[sources/koukorinis-stylized-facts|Koukorinis et al. Stylized Facts]]
- [[sources/stavroyiannis-2017-bitcoin-multifractal|Stavroyiannis et al. (2017)]]
- [[sources/aslam-2020-covid-mfdfa|Aslam et al. (2020) COVID-19 MFDFA]]
