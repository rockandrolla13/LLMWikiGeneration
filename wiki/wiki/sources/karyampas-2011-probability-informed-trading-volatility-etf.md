---
authors:
- Dimitrios Karyampas
- Paola Paiardini
content_hash: sha256:14c75065a57a03ed6667f2973302ac2d30475ad73120014ecd55d0a305299286
created: 2026-09-27 01:47:00+00:00
page_id: sources/karyampas-2011-probability-informed-trading-volatility-etf
page_type: source
publication_venue: BWPEF 1101, School of Economics, Mathematics and Statistics, Birkbeck,
  University of London
related:
- concepts/volume-clock
- concepts/informed-trading
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/realized-variance
- concepts/market-microstructure
- concepts/trade-classification
- concepts/bid-ask-spread
- concepts/long-memory
- concepts/vpin
revision_id: 1
schema_version: 2
source_hash: sha256:d735524a75930d5cd47c721a56e33dc8bd193d69cacea185d084f5a50aab9e27
source_path: markdown_output/karyampas-2011-probability-informed-trading-volatility-etf.md
source_type: paper
tags:
- vpin
- informed-trading
- volume-clock
- realized-volatility
- jump-detection
- etf
- har-rv
- market-microstructure
- clock-volume
- asset-equity
- harvest-core
title: Probability of Informed Trading and Volatility for an ETF
updated: '2026-09-27T01:47:00Z'
uuid: a722aa21-e2f4-52a5-ab37-2b62ed2897cb
year: 2011
---

<!-- AUTHORED REGION START -->
# Probability of Informed Trading and Volatility for an ETF

## Summary

The paper asks whether the Volume-Synchronized Probability of Informed Trading (VPIN), a measure built from imbalances in buy and sell volume, is related to future volatility, and whether it helps forecast that volatility once jumps are accounted for. The authors apply the VPIN procedure to ten years of TAQ trade and quote data for the SPY exchange-traded fund tracking the S&P 500. Trades are classified as buyer- or seller-initiated with the Lee-Ready algorithm, then grouped into equal-sized volume buckets to compute VPIN, following the method that avoids the numerical maximum-likelihood estimation used by the older PIN model. Volatility is measured with three estimators designed to be robust to microstructure noise and price jumps, and the number of jumps per day is counted with nonparametric jump-detection tests. VPIN is added, together with the jump count, to a Heterogeneous Autoregressive model of Realized Volatility (HAR-RV). The main finding is a large, statistically significant positive correlation between VPIN and future volatility, with Granger-causality results pointing from VPIN to volatility rather than the reverse, matching what the same procedure found for futures contracts. In the HAR-RV regressions, adding both the jump count and VPIN produces the best-fitting specifications. What is new relative to the VPIN paper it builds on is the substitution of jump-robust, noise-robust volatility estimators for the simple absolute-return proxy, and the explicit test of VPIN inside a HAR-RV forecasting model for an ETF rather than a futures contract.

## Clock and Sampling

**Volume clock: one observation per unit of volume traded.**

See [[concepts/volume-clock|Volume Clock]].

VPIN is computed by grouping trades into equal-sized volume buckets and classifying the volume in each bucket as buy- or sell-initiated, so information arrival is measured per unit of traded volume rather than per unit of clock time. The volatility side of the analysis is aggregated to a daily frequency: realized volatility estimators are built from 5-minute (bipower-type estimators) or minute-by-minute (the noise-and-jump-robust MLE-F estimator) intraday returns, then the daily VPIN and daily jump count are used to forecast next-day, weekly and monthly realized volatility in the HAR-RV model.

## Data

- **Asset class:** Equities
- **Instruments:** SPY (S&P 500 SPDR exchange-traded fund), traded on Amex
- **Venue:** TAQ database (Amex-listed SPY)
- **Period:** January 2000 to December 2009 (1998 trading days)
- **Granularity:** Intraday trade and quote data aggregated to 5-minute and 1-minute intervals for volatility estimation, and to volume buckets for VPIN; volatility and VPIN measures are then used at a daily frequency.

## Features and Measures

- **VPIN (Volume-Synchronized Probability of Informed Trading).** The average absolute imbalance between buy and sell volume across equal-sized volume buckets, used as a proxy for the rate at which informed traders arrive, without needing to estimate the unobservable arrival-rate parameters of the original PIN model.
- **Threshold Bipower Variation (TBPV).** A jump-robust extension of bipower variation that applies a vanishing threshold to products of adjacent absolute returns so that large, jump-driven returns are excluded from the volatility estimate.
- **MLE-F semi-parametric volatility estimator.** A two-step estimator that first removes returns flagged as jumps by nonparametric jump-detection tests, then applies maximum likelihood to the remaining, irregularly spaced return series to estimate the diffusive volatility and the microstructure noise variance jointly.
- **Number of jumps (NJ).** The count of statistically detected price jumps in a trading day, obtained from the Lee-Mykland and Lee-Hannig nonparametric jump-detection tests, used as an explanatory variable in the HAR-RV regressions.

## Method

The paper first summarizes the sequential-trade PIN framework and then implements the VPIN procedure, which classifies trades with the Lee-Ready rule (checking sensitivity to 5-second, 1-second, and zero-second quote-matching delays), sorts volume into equal buckets, and computes the average absolute buy-sell imbalance per bucket. Three volatility estimators (bipower variation, threshold bipower variation, and the MLE-F semi-parametric estimator) are computed from intraday SPY prices, using jump-detection tests to separate the continuous and jump components of returns. The relationship between VPIN and volatility is judged first via simple correlation and Granger-causality regressions, and then via a Heterogeneous Autoregressive Realized Volatility (HAR-RV) model in the Corsi/Corsi-Renò tradition, which regresses future daily realized volatility on lagged daily, weekly and monthly realized volatility, the number of jumps, and current and lagged VPIN; model fit is compared across specifications using adjusted R-squared.

## Results

- VPIN and future volatility have a large, positive, statistically significant correlation of 0.3292.
- Granger-causality tests support a causal link running from VPIN to volatility rather than from volatility to VPIN, matching results previously reported for futures contracts.
- The historical distribution of VPIN for SPY is well approximated by a log-normal distribution, mirroring earlier findings for futures.
- In the HAR-RV regressions, the specifications that add both the number of jumps and VPIN to the daily/weekly/monthly realized-volatility lags reach the highest adjusted R-squared values reported (0.8800 for the TBPV-based specification and 0.8681 for the MLE-F-based specification), higher than the corresponding specifications without VPIN (0.7999 and 0.8358).
- The VPIN coefficients in the HAR-RV regressions are negative for the contemporaneous VPIN term and positive for the lagged VPIN term, and are reported as statistically significant.
- The paper concludes that VPIN improves the forecast of realized volatility once jumps are also accounted for.

## Limitations

- The empirical analysis covers a single instrument, the SPY ETF, over one ten-year sample period.
- The Lee-Ready trade-classification algorithm used to build VPIN is only approximately accurate; the paper itself notes that estimates of its accuracy in the literature range from 72% to 93% depending on the study.
- Reader note: no out-of-sample volatility-forecast evaluation is reported; the HAR-RV comparison is based on in-sample adjusted R-squared only.
- Reader note: the paper states its own further work (VPIN versus liquidity measures) as still to be done, so the VPIN-liquidity link is not tested here.

## Related

- [[concepts/volume-clock|Volume Clock]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/long-memory|long memory]]
- [[concepts/vpin|VPIN]]

## Citation

Dimitrios Karyampas, Paola Paiardini (2011). Probability of Informed Trading and Volatility for an ETF. BWPEF 1101, School of Economics, Mathematics and Statistics, Birkbeck, University of London.

Text ingested: `markdown_output/karyampas-2011-probability-informed-trading-volatility-etf.md`, converted from `raw/ofi-event-clock/karyampas-2011-probability-informed-trading-volatility-etf.pdf`.

Coverage of this summary: Read the entire markdown file, including the abstract, the PIN and VPIN model sections, the volatility-estimator and jump-detection sections, the data section, the empirical results section with its HAR-RV and Granger-causality tables, and the conclusion.

Known problems with the input: Most equations are rendered as omitted pictures in the markdown, so exact formula forms could not be verified beyond what is described in prose; Table 1 (HAR-RV estimation) has garbled cell alignment from the PDF-to-markdown conversion; the adjusted R-squared values were matched to model labels by their left-to-right order in the row, which appears consistent with the paper's own conclusion that models combining jumps and VPIN fit best.
<!-- AUTHORED REGION END -->