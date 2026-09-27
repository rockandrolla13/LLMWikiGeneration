---
authors:
- Jun Chen
content_hash: sha256:775897880025dd25697d360438467dd97bc64710c66c9e8954df8fc382156cad
created: 2026-09-27 01:47:00+00:00
page_id: sources/chen-2019-studying-regime-change-directional-change
page_type: source
publication_venue: Centre for Computational Finance and Economic Agents, University
  of Essex (PhD thesis)
related:
- concepts/intrinsic-time
- concepts/stylized-facts
- concepts/high-frequency-data
- concepts/backtesting
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:81d9faaa2cb5a0815c1116c269900f644dd60451390a25d2977aa70b6b06ecf3
source_path: markdown_output/chen-2019-studying-regime-change-directional-change.md
source_type: paper
tags:
- directional-change
- regime-change
- hidden-markov-model
- naive-bayes
- foreign-exchange
- trading-algorithm
- market-volatility
- phd-thesis
- clock-intrinsic
- asset-multi
- harvest-relevant
title: Studying Regime Change using Directional Change
updated: '2026-09-27T01:47:00Z'
uuid: d5c9ff77-d363-5733-9b6f-8706b81840a8
year: 2019
---

<!-- AUTHORED REGION START -->
# Studying Regime Change using Directional Change

## Summary

The thesis asks how a significant shift in the collective trading behaviour of a market ('regime change') can be measured and detected, as an alternative to the conventional approach of tracking changes in the statistical properties of fixed-interval time series. It builds this around Directional Change (DC), an event-based way of sampling price data that only records a new point when price reverses by a pre-set percentage threshold from the last peak or trough, rather than at fixed time intervals.

The first research chapter feeds a DC-derived return indicator (R) into a two-state Hidden Markov Model (HMM) to detect regimes in three FX pairs around the 2016 Brexit referendum, and compares the result against an HMM fed with time-series realised volatility. The second chapter extends the same DC-plus-HMM approach to ten datasets across FX, equity indices and oil, characterising 'normal' and 'abnormal' regimes by plotting each regime's average Total Price Movement (TMV) and Time (T) in a two-dimensional, per-market-normalised indicator space. The third chapter builds a naive Bayes classifier that uses the (TMV, T) values of the still-open (not yet completed) DC trend, together with regime characteristics learned from historical data, to estimate in real time the probability that the market is currently in the normal or abnormal regime, without any forecasting. The fourth chapter designs two DC-based trading algorithms (JC1, JC2) that use these regime-tracking signals to close positions and switch strategy, benchmarked against a plain contrarian control algorithm (CT1) on three stock indices.

The DC-based HMM detected the same Brexit-period regime shift as the time-series HMM, plus an extra short regime spell the time-series approach missed. Across ten markets and ten DC thresholds, normal and abnormal regimes occupied clearly separable regions of the normalised TMV-T indicator space. The naive Bayes tracker picked up both known volatile spells in each of three stock indices, with its signal timing ranging from several days behind to several days ahead of the hindsight-labelled regime change. The two regime-aware trading algorithms had smaller maximum drawdown than the non-regime-aware control algorithm in every setting tested, though also lower final wealth.

What is new is the first use of a DC-derived indicator inside a hidden Markov model for regime detection, the first characterisation of normal and abnormal regimes as separable regions of a DC indicator space across different markets and data frequencies, a real-time (hindsight-free) Bayesian regime-tracking mechanism built from that characterisation, and two simple DC-based trading rules that use regime-tracking signals purely as a stop-loss and strategy-switch device.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Price is sampled only when it reverses by a pre-set percentage threshold from the last extreme point (a peak or trough), producing alternating uptrend/downtrend 'Directional Change (DC) events' and 'Overshoot (OS) events' rather than fixed-interval bars. Three DC indicators are derived per trend: Total Price Movement (TMV, the threshold-normalised percentage price change of the trend), Time (T, the wall-clock time to complete the trend) and Return (R, TMV divided by T). Chapters 3 and 4 use only completed trends; Chapter 5's tracking method instead measures the still-open, unconfirmed trend up to the present so it can be applied without the benefit of hindsight. Chapter 3 also builds a parallel time-series comparison clock: 5-minute log returns aggregated into daily realised volatility.

## Data

- **Asset class:** Several asset classes
- **Instruments:** Chapter 3: EUR-GBP, GBP-USD and EUR-USD exchange rates. Chapter 4: ten datasets - DJIA, FTSE 100 and S&P 500 stock indices; Brent and WTI crude oil; EUR-GBP, GBP-USD and EUR-USD; and the Shanghai (SSE) and Shenzhen (SZSE) stock indices. Chapters 5 and 6: DJIA, FTSE 100 and S&P 500 only.
- **Venue:** Chapter 3 FX tick data purchased from data vendor Kibot via the Centre for Computational Finance and Economic Agents (CCFEA), University of Essex; venue/source not stated for the Chapter 4-6 index, oil and Chinese-market closing prices.
- **Period:** Chapter 3: 23 May 2016 to 22 July 2016 (spanning the 23 June 2016 Brexit referendum). Chapter 4: four historical windows - the 2007-2008 global financial crisis, the 2014-2016 oil crash, the 2016 Brexit referendum, and the 2015-16 Chinese stock market turbulence. Chapters 5 and 6: DJIA, FTSE 100 and S&P 500 daily closing prices from January 2007 to December 2012, split into a 03/01/2007-31/12/2009 training period and a 01/01/2010-28/12/2012 test/tracking period.
- **Granularity:** Second-by-second tick data for the Chapter 3 FX study; a mix of daily and minute-by-minute closing prices for the ten Chapter 4 datasets; daily closing prices for the Chapters 5-6 stock indices. DC thresholds used: 0.4% (Chapter 3); ten steps from 0.1% to 1.0% (Chapter 4); 0.3% (Chapter 5); and a 0.003 regime-tracking threshold with 0.03/0.006/0.009 trading thresholds (Chapter 6).

## Features and Measures

- **Total Price Movement (TMV).** The percentage price change of a Directional Change trend, from one extreme point to the next, normalised by the threshold used to sample the trend.
- **Time (T).** The physical (wall-clock) time taken to complete a Directional Change trend, from one extreme point to the next.
- **Time-adjusted Return (R).** TMV divided by T: the absolute percentage price change per unit time in a Directional Change trend, used as the input series to the hidden Markov model for regime detection.
- **realised volatility (time-series comparison indicator).** The sum of squared 5-minute log returns within a trading day, used in Chapter 3 as the conventional time-series counterpart to the DC return indicator R.
- **normalised TMV-T indicator space.** A two-dimensional space, with each axis min-max normalised per data set, in which a detected regime's average TMV and average T values are plotted to compare and separate regimes across different markets, time periods and thresholds.

## Method

Regime detection (Chapter 3) fits a two-state Hidden Markov Model with Gaussian emissions (using the depmixS4 R package's Expectation-Maximization / Baum-Welch algorithm) separately to the log-transformed DC return indicator R and to time-series realised volatility, then compares the two sets of inferred regimes over the Brexit test period. Regime classification (Chapter 4) reuses the same HMM approach on ten market/period combinations, computes the average TMV and average T of the trends assigned to each regime, min-max normalises these per data set, and plots them in the two-dimensional indicator space to test whether 'normal' (Regime 1) and 'abnormal' (Regime 2) regimes are separable across markets and DC thresholds.

Regime tracking (Chapter 5) trains a Gaussian naive Bayes classifier on the (TMV, T) values of completed trends already labelled Regime 1 or Regime 2 in a training period, then applies it to the (TMV, T) of the still-open trend in a later test period to estimate the probability of each regime in real time. Two decision rules combine the two probabilities into a single regime call: B-Simple (pick the higher-probability regime) and B-Strict (only call Regime 2 when its probability exceeds a threshold of 0.8). Tracking performance is judged by comparing signal timing and true/false alarm counts against the hindsight regimes from Chapter 3's method.

Trading (Chapter 6) builds two DC-threshold-based algorithms, JC1 and JC2, that open a contrarian position (or, for JC1 under an abnormal regime, a trend-following position) when the absolute value of TMV reaches 2, and close it at the next DC confirmation point or whenever the Chapter 5 tracker signals a regime change; both are benchmarked against a control contrarian algorithm, CT1, that ignores regime information. All three use identical, simple all-in/all-out money management, and are compared on final wealth and maximum drawdown across three trading thresholds and three stock indices.

## Results

- In the Brexit-period FX test, both the DC-based HMM and the time-series HMM detected a volatile regime beginning on 23 June 2016 (the referendum date), but DC also flagged a short extra regime spell on 14 July 2016 that the time-series indicator did not detect.
- Across ten market-period datasets (equity indices, oil benchmarks, FX pairs and Chinese indices) and ten thresholds from 0.1% to 1.0%, normal (Regime 1) and abnormal (Regime 2) regimes occupied clearly separable regions of the normalised TMV-T indicator space, with only minor overlap concentrated in the oil-crash data.
- The naive Bayes tracker (both B-Simple and B-Strict) detected both hindsight-labelled Regime 2 spells in each of DJIA, FTSE 100 and S&P 500 between 2010 and 2012, with signal timing ranging from 9 days behind to 6 days ahead of the benchmark regime dates.
- B-Strict raised far fewer alarms than B-Simple across the three indices (46 true and 10 false alarms in total, versus 89 true and 52 false alarms for B-Simple), with both rules still catching both known regime spells.
- The regime-aware trading algorithms JC1 and JC2 had smaller maximum drawdown than the non-regime-aware control CT1 in every one of the three trading-threshold settings and three indices tested, for example -5% versus -6% drawdown on DJIA at a 0.03 trading threshold.
- JC1 and JC2 also had lower final wealth than CT1 in almost every setting, for example 113% and 121% versus 131% for CT1 on DJIA at a 0.03 trading threshold, so the tracking signals reduced losses without raising returns for these simple algorithms.
- The regime-tracking threshold used in Chapter 6 was set to 0.003, and three trading thresholds (0.03, 0.006, 0.009) were tested for the JC1/JC2/CT1 comparison, generating between 20 and 82 trades per index depending on the threshold used.

## Limitations

- Reader note: the Chapter 3 Brexit regime study covers only two months of three related FX pairs; the authors themselves state they are not offering a comprehensive analysis of the FX market over this period.
- The authors note that the Chapter 4 study attaches a specific known external event to every chosen data set by design, so it cannot show whether the method ever detects regime change without an identifiable triggering event; they flag this as future work.
- The authors describe the Chapter 6 trading algorithms JC1 and JC2 as 'very naive' with simple all-in/all-out money management and no transaction costs stated; both underperformed the non-regime-aware control CT1 on final wealth in almost every setting tested.
- Reader note: all regime detection in the thesis assumes a fixed two-state HMM (only 'normal' and 'abnormal' regimes); the authors themselves suggest more than two regime types may exist and leave this to future research.
- Reader note: the regime-tracking naive Bayes classifier (Chapter 5) is validated on only three, highly correlated developed-market equity indices (DJIA, FTSE 100, S&P 500) over the same 2007-2012 window, so its generalisation to other assets or periods is untested here.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/backtesting|backtesting]]
- [[concepts/directional-change|Directional Change]]

## Citation

Jun Chen (2019). Studying Regime Change using Directional Change. Centre for Computational Finance and Economic Agents, University of Essex (PhD thesis).

Text ingested: `markdown_output/chen-2019-studying-regime-change-directional-change.md`, converted from `raw/ofi-event-clock/chen-2019-studying-regime-change-directional-change.pdf`.

Coverage of this summary: Read the abstract, thesis structure (Chapter 1), all of the background and literature/methodology chapter (Chapter 2: regime change literature, Directional Change, HMM, naive Bayes), and the full introduction, methodology, experiments, results and conclusion sections of all four research chapters (Chapter 3 regime detection, Chapter 4 regime classification, Chapter 5 regime tracking, Chapter 6 trading algorithms) plus the overall conclusions chapter (Chapter 7). Did not read the appendices or bibliography.

Known problems with the input: Some tables in the PDF-to-markdown conversion have merged or misaligned columns (e.g. Table 3.1's regime period listings); numbers used in this record were only taken from clearly stated running prose and from tables whose row/column structure was unambiguous.
<!-- AUTHORED REGION END -->