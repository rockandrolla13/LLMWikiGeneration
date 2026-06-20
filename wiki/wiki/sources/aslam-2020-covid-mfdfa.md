---
title: Evidence of Intraday Multifractality in European Stock Markets during COVID-19
  (2020)
page_id: sources/aslam-2020-covid-mfdfa
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-04-25 23:30:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Faheem Aslam
- Wahbeeah Mohti
- Paulo Ferreira
year: 2020
venue: International Journal of Financial Studies
tags:
- mfdfa
- covid-19
- multifractal
- stock-markets
- european-markets
- high-frequency
- market-efficiency
- econophysics
related:
- concepts/mfdfa
- concepts/stylized-facts
- concepts/hurst-exponent
- concepts/long-memory
- sources/stavroyiannis-2017-bitcoin-multifractal
- sources/koukorinis-stylized-facts
mind_map_priority: medium
schema_version: 2
uuid: 1a0d342f-1fd3-5fc8-b00a-6c05a452c346
content_hash: sha256:3f7ad73bd41255954af64388592bc9179bbd94d8e9113d1266dccddd1cbb85f3
---

<!-- AUTHORED REGION START -->
# Evidence of Intraday Multifractality in European Stock Markets during COVID-19

## Summary

Aslam et al. (2020) apply Multifractal Detrended Fluctuation Analysis (MFDFA) to high-frequency (5-minute) data from eight European stock markets during the COVID-19 outbreak (January-March 2020). The study demonstrates that the pandemic significantly affected market efficiency, with varying degrees of multifractality across different markets.

## Key Contributions

### Methodology
- Uses 5-minute intraday index data (5916 observations per market)
- Applies Seasonal and Trend Decomposition using Loess (STL) before MFDFA
- Computes generalized Hurst exponents h(q) for q ∈ [-10, 10]
- Measures multifractal width Δh = h(qmin) - h(qmax)

### Markets Analyzed
Eight European stock indices during COVID-19 outbreak:
- Italy (FTSMIB)
- France (FCHI)
- Germany (GDAXI)
- Spain (IBEX)
- Belgium (BFX)
- Austria (ATX)
- Netherlands (AAX)
- United Kingdom (FTSE)

### Key Findings

**Multifractal Width Rankings:**
| Country | Δh | Efficiency Rank |
|---------|-----|-----------------|
| Spain | 0.56 | Most efficient |
| Belgium | 0.58 | - |
| Italy | 0.59 | - |
| Germany | 0.59 | - |
| France | 0.60 | - |
| Netherlands | 0.61 | - |
| UK | 0.63 | - |
| Austria | 0.68 | Least efficient |

### Interpretation
- Larger Δh indicates stronger multifractality (market inefficiency)
- Austria and UK showed highest levels of multifractality
- Spain maintained relative efficiency during the pandemic
- Results align with findings from other Central and Eastern European markets

## Methodology Details

### STL Decomposition
Applied to remove seasonal patterns from intraday data:
```
ri = Ti + Si + Ri
```
- Ti: Deterministic trend component
- Si: Seasonal component (102 = observations per day)
- Ri: Stochastic remainder

### MFDFA Steps
1. **Profile construction:** Y(i) = Σ(xk - <x>)
2. **Segmentation:** Divide into 2Ns non-overlapping segments
3. **Local detrending:** Polynomial fit and variance calculation
4. **q-th order fluctuation:** Fq(s) averaging
5. **Scaling analysis:** h(q) from log-log plots

### Multifractal Spectrum
- Renyi exponent: τ(q) = qh(q) - 1
- Singularity spectrum: f(α) via Legendre transform
- Single-humped f(α) confirms multifractality

## Connections to Prior Work

### Methodological Foundation
- [[concepts/mfdfa|MFDFA]] as developed by Kantelhardt et al. (2002)
- Extension of DFA by Peng et al. (1994)

### Related Studies
- [[sources/stavroyiannis-2017-bitcoin-multifractal|Stavroyiannis et al. (2017)]]: Bitcoin multifractality
- [[sources/koukorinis-stylized-facts|Koukorinis et al. (2022)]]: Stylized facts with MFDFA

### Crisis Period Analysis
- Confirms multifractal behavior during market stress
- Aligns with Caraiani (2012) on CEE markets during 2008 crisis
- Supports Rizvi et al. (2014) on crisis-period efficiency changes

## Practical Implications

1. **Market efficiency varies during crises** - Regulators should monitor multifractal properties
2. **High-frequency analysis reveals intraday patterns** - Not captured by daily data
3. **Cross-market heterogeneity** - Different markets respond differently to global shocks
4. **STL preprocessing recommended** - Important for high-frequency MFDFA

## Data Period Context

Study period: January 1 - March 23, 2020
- January: Limited COVID-19 impact in Europe
- Late February: Cases surge (Italy: 888 on Feb 28)
- March: Market crash period (53,578 cases in Italy by Mar 21)

## See Also

- [[concepts/mfdfa|MFDFA]]
- [[concepts/hurst-exponent|Hurst Exponent]]
- [[concepts/stylized-facts|Stylized Facts]]
- [[sources/stavroyiannis-2017-bitcoin-multifractal|Bitcoin Multifractal Analysis]]
- [[sources/koukorinis-stylized-facts|Koukorinis Stylized Facts]]

<!-- AUTHORED REGION END -->
