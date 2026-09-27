---
authors:
- Boyue Fang
- Yutong Feng
content_hash: sha256:c643a4de80e34ca05f6aa636c12105b0052ac63efcf044599778ea648dcd9f2f
created: 2026-09-27 01:47:00+00:00
page_id: sources/fang-2019-design-high-frequency-trading-algorithm-based
page_type: source
related:
- concepts/sampling-clocks
- concepts/informed-trading
- concepts/high-frequency-trading
- concepts/market-making
- concepts/backtesting
- concepts/high-frequency-data
- concepts/order-flow-imbalance
- concepts/vpin
- concepts/volume-clock
revision_id: 1
schema_version: 2
source_hash: sha256:11d22b2f67f0d15dbe2f188c70b2c4c2a77a30ad6445b769d717a6d8921c9754
source_path: markdown_output/fang-2019-design-high-frequency-trading-algorithm-based.md
source_type: paper
tags:
- informed-trading
- vpin
- garch
- support-vector-machine
- csi300-futures
- market-making
- high-frequency-trading
- clock-compares
- asset-futures
- harvest-core
title: Design of High-Frequency Trading Algorithm Based on Machine Learning
updated: '2026-09-27T01:47:00Z'
uuid: 48e37edb-ecc1-5ac7-9861-d2e7801f7201
year: 2019
---

<!-- AUTHORED REGION START -->
# Design of High-Frequency Trading Algorithm Based on Machine Learning

## Summary

This paper asks whether combining order-book information from Volume-synchronized Probability of Informed Trading (VPIN), volatility forecasts from GARCH, and a machine-learning filter (SVM) can improve a high-frequency market-making strategy on CSI300 stock index futures, compared with using any one of these signals alone.

The authors first set out a simple microstructure liquidity-premium model to motivate why market makers need a measure of informed trading, then use VPIN, computed from bulk-volume-classified trading baskets, to flag periods of heavy informed trading. A GARCH(1,1) model on the futures log-return series sets a trading threshold that is loosened or tightened depending on the VPIN level, and an SVM trained on recent GARCH predictions and price data can veto a signalled trade. Wavelet denoising with a Haar basis is also applied to ultra-high-frequency data before recomputing VPIN.

A Granger causality test supports VPIN as a predictor of the logarithmic return of CSI300 futures. The backtested strategy combining GARCH, VPIN, and SVM produced the best total return, annualized return, alpha, and Sharpe ratio among the tested variants, and also had the smallest maximum drawdown, though adding SVM alone (without VPIN) sometimes underperformed the GARCH+VPIN combination in isolated periods.

The contribution is the specific assembly of VPIN, GARCH, and SVM into one adaptive threshold-and-veto trading rule, plus the finding that the strategy's edge is not sensitive to the choice between 500-millisecond and one-minute sampling, motivating a wavelet-denoising extension intended to make VPIN itself more usable at ultra-high frequency.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

VPIN buckets trading volume into 50 equal-volume baskets, a volume clock, to estimate order imbalance and the probability of informed trading; separately, the GARCH volatility model and the trading algorithm run on calendar-time log-return series, and the paper explicitly tests both 500-millisecond and one-minute calendar sampling for the trading strategy, finding little difference between them. The stated horizon in the VPIN threshold rule is two 'basket' times ahead, while the trading algorithm decides direction from the most recent GARCH one-step-ahead variance forecast.

## Data

- **Asset class:** Futures
- **Instruments:** CSI300 stock index futures (IF.CFE)
- **Venue:** China Financial Futures Exchange
- **Period:** VPIN data: October 2015 to September 2018. GARCH data: January to October 2018. Strategy backtest: January 2016 to September 2018.
- **Granularity:** Minute-level data for the main backtest; 500-millisecond and one-minute transaction data compared for sensitivity; VPIN computed over 50 volume baskets.

## Features and Measures

- **VPIN.** Volume-synchronized Probability of Informed Trading: transaction volume is split into equal-volume baskets, buy/sell volume in each basket is estimated from price changes via a normal-distribution split, and the resulting imbalance across baskets is aggregated into a measure of informed-trading intensity.
- **GARCH(1,1) volatility forecast.** A generalized autoregressive conditional heteroscedasticity model fit to the futures logarithmic return series, used to forecast one-step-ahead variance and set a rolling trading threshold.
- **HAR-VPIN model.** A heterogeneous-autoregressive extension that regresses VPIN-related volatility on realized volatility measured at multiple horizons (5-minute, 1-hour, 1-day) to allow hedging across investment time scales.
- **SVM trade filter.** A support vector machine with a radial basis function kernel, trained on recent GARCH predictions and futures prices, that can veto a GARCH-signalled trade if it predicts the trade would lose money.
- **Wavelet-denoised UHF signal.** Ultra-high-frequency price data denoised with a level-6 Haar wavelet and soft thresholding before being used to recompute VPIN, intended to reduce VPIN's noise sensitivity at very high frequency.

## Method

The paper builds a market-making/statistical-arbitrage algorithm in three layers. First, a GARCH(1,1) model forecasts return variance and a threshold rule, searched in steps of 0.02 to maximize trailing one-hour return, decides whether to buy or sell CSI300 futures. Second, VPIN is compared against two thresholds tuned by stochastic gradient descent to widen or tighten the GARCH threshold when informed trading is judged to be heavy or light. Third, an SVM trained on the last 30 trading days of GARCH predictions and futures prices can cancel a trade the GARCH(+VPIN) layer would otherwise take.

Statistical validity of the VPIN signal is checked with a Granger causality test on the logarithmic return series at a two-period lag, and GARCH model choice is checked with stationarity (ADF), autocorrelation, and residual tests across GARCH(1,1), GARCH(1,2), GARCH(2,1) and TGARCH specifications.

Strategy performance is judged with total and annualized returns, relative return versus benchmark, alpha, beta, maximum drawdown, and Sharpe ratio, backtested with an initial capital of 10 million, 25% margin, and a stated transaction fee, comparing four variants: GARCH only, GARCH plus SVM, GARCH plus VPIN, and GARCH plus VPIN plus SVM.

## Results

- The Granger causality test rejected the null that VPIN does not Granger-cause CSI300 futures log returns, with an F-statistic of 3.82724 and a P-value of 0.0222 at a two-period lag.
- GARCH(1,1) coefficients passed the residual test with alpha plus beta equal to 0.93, indicating a stable, slowly decaying volatility process.
- The TGARCH model showed a positive leverage effect, meaning bad news raised volatility more than good news of the same size.
- The combined GARCH plus VPIN plus SVM strategy achieved total returns of 24.23%, annualized returns of 8.42%, a relative return of 32.06%, alpha of 9.88%, and a Sharpe ratio of 0.310.
- GARCH plus VPIN plus SVM had the smallest maximum drawdown among the four variants, at -17.70%, versus -32.01% for GARCH alone.
- GARCH alone lost money over the backtest, with total returns of -25.85% and a Sharpe ratio of -0.693.
- Strategy performance changed very little between 500-millisecond and one-minute sampling, indicating the strategy is not sensitive to ultra-high-frequency data granularity.

## Limitations

- The strategy is backtested on a single instrument, CSI300 futures, over one historical sample period, so results may not generalize to other markets or regimes.
- VPIN is reported to work poorly at very high frequency because it combines bid and ask volume into a single imbalance measure, motivating the wavelet-denoising extension that the paper illustrates on a single day rather than validating inside the backtest itself.
- Reader note: threshold parameters for GARCH and VPIN are tuned using the same historical window used to report backtest performance, which risks overstating out-of-sample returns.
- Reader note: the transaction fee is printed as '6.87%%' in the source, an unusual figure that may reflect a formatting artifact; it is reported as-is.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-making|market making]]
- [[concepts/backtesting|backtesting]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/vpin|VPIN]]
- [[concepts/volume-clock|Volume Clock]]

## Citation

Boyue Fang, Yutong Feng (2019). Design of High-Frequency Trading Algorithm Based on Machine Learning.

DOI: 10.48550/arxiv.1912.10343

Text ingested: `markdown_output/fang-2019-design-high-frequency-trading-algorithm-based.md`, converted from `raw/ofi-event-clock/fang-2019-design-high-frequency-trading-algorithm-based.pdf`.

Coverage of this summary: Read the full markdown paper, including introduction, background microstructure model, VPIN and GARCH theoretical sections, data inspection on CSI300 futures, study design and algorithms, model section on wavelet denoising and HAR-VPIN, conclusion, and appendix tables.

Known problems with the input: Transaction fee is printed with a doubled percent sign as '6.87%%' in the source markdown; reported as-is without correction; No journal or conference venue name is present in the provided markdown (only an 'ARTICLE HISTORY: Compiled December 24, 2019' line), so venue is left blank.
<!-- AUTHORED REGION END -->