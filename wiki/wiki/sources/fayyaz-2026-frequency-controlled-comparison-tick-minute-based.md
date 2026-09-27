---
authors:
- Muhammad Toheed Fayyaz
- Abdul Jabbar
- Faheem Ahmad Qureshi
- Syed Qaisar Jalil
content_hash: sha256:eb0bc037a812b36e2a3eca3b367edfa5839b135fe3e6f51f050b5dbe417356ee
created: 2026-09-27 01:47:00+00:00
page_id: sources/fayyaz-2026-frequency-controlled-comparison-tick-minute-based
page_type: source
related:
- concepts/sampling-clocks
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/market-microstructure-noise
- concepts/stylized-facts
- concepts/autocorrelation-time-series
- concepts/realized-variance
- concepts/backtesting
- concepts/overfitting-backtesting
revision_id: 1
schema_version: 2
source_hash: sha256:f53f5cadaa569d391d27f4cb6ee4556a51c681c16117744758d4610216a55f81
source_path: markdown_output/fayyaz-2026-frequency-controlled-comparison-tick-minute-based.md
source_type: paper
tags:
- crypto
- information-bars
- tick-data
- bar-construction
- variance-ratio
- bitcoin
- market-microstructure
- machine-learning
- clock-compares
- asset-crypto
- harvest-relevant
title: A Frequency-Controlled Comparison of Tick- and Minute-Based Information Bars
  for Cryptocurrency Markets
updated: '2026-09-27T01:47:00Z'
uuid: 98e32675-12f8-52d8-9deb-25f73da2bda5
year: 2026
---

<!-- AUTHORED REGION START -->
# A Frequency-Controlled Comparison of Tick- and Minute-Based Information Bars for Cryptocurrency Markets

## Summary

Traders and researchers who build information-driven bars (bars that close on accumulated market activity rather than on a clock) usually construct them from cheap, pre-aggregated one-minute OHLCV data rather than raw tick data. The paper asks whether that shortcut actually changes the statistical properties of the resulting bars, since a controlled comparison of the two input resolutions had not previously been done.

Two otherwise identical pipelines are driven from six years of Binance BTCUSDT perpetual futures data (1 January 2020 to 31 December 2025): one built from raw aggTrade tick records, one from one-minute OHLCV bars. Both share an adaptive EMA threshold-calibration framework with minimum and maximum duration bounds, and both construct six bar types (dollar, volume, volatility, range, Renko/displacement, and hybrid OR-logic bars), benchmarked against fixed-interval calendar bars. Bars are scored on eight statistical criteria covering distributional normality, serial independence, and construction quality (uniformity, entropy, timeout rate). A separate matched-frequency analysis coarsens the tick series to the minute series' bar count to separate genuine resolution effects from sampling-frequency artifacts, and a downstream machine-learning experiment trains classifiers to predict three-calendar-day-forward direction from each bar series.

The tick advantage turns out not to be universal: it is concentrated in bar types where minute aggregation throws away the most information, chiefly hybrid bars and, on some criteria, Renko/displacement bars. For dollar, volume, and range bars the minute pipeline is often as good or better in the raw six-year comparison, partly because the six-year sample mixes several market regimes (the 2020 COVID crash, the 2021 bull run, the 2022 bear market) that inflate tail risk for every series. Once bar counts are matched for frequency, tick bars do better across most criteria for dollar, hybrid, and volatility bars, so much of the apparent tick underperformance in the headline scorecard looks like a sampling-frequency artifact rather than a real quality deficit.

What is new here is the controlled, frequency-matched design itself across six bar types at once, the use of timeout rate as an explicit calibration diagnostic, and the connection to a downstream ML test, where statistical bar quality and directional predictability turn out to be largely unrelated: out-of-sample AUC stays near chance (0.498-0.596) for every bar type regardless of how well-conditioned its statistics are.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Each of six bar types (dollar, volume, volatility, range, Renko/displacement, and hybrid OR-logic) closes when an activity measure accumulated since the previous bar reaches an adaptively updated threshold, subject to minimum and maximum duration bounds. The threshold is computed either from exact tick-level accumulation or from one-minute OHLCV approximations, and the two are compared against each other and against fixed-interval calendar bars. The threshold itself updates online after each bar via an EMA of realized bar sizes. In the downstream machine-learning test, each closed bar is labeled +1 or -1 depending on whether price is higher three calendar days after that bar's close.

## Data

- **Asset class:** Crypto
- **Instruments:** BTCUSDT USDT-margined perpetual futures (Bitcoin/Tether perpetual swap)
- **Venue:** Binance
- **Period:** 1 January 2020 to 31 December 2025 (2,192 calendar days)
- **Granularity:** raw Binance aggTrade tick records and one-minute OHLCV bars

## Features and Measures

- **Dollar bars.** Bars that close once cumulative dollar turnover (price times quantity) since the last bar reaches an adaptive threshold; computed exactly per trade in the tick pipeline and approximated as close price times minute volume in the minute pipeline.
- **Volume bars.** Bars that close once cumulative traded quantity reaches an adaptive threshold; the tick and minute signals are arithmetically equivalent since total minute volume is the sum of within-minute trade sizes.
- **Volatility bars.** Bars that close once accumulated absolute price movement reaches an adaptive threshold; the tick pipeline sums absolute log-returns across every consecutive trade pair, while the minute pipeline sums absolute close-to-close changes, discarding intra-minute reversals.
- **Range bars.** Bars that close once the within-bar high-low price excursion reaches an adaptive threshold; the tick pipeline tracks the exact running high and low of trade prices, while the minute pipeline sums per-minute high-low spans.
- **Renko (displacement) bars.** Bars that close once price has moved a minimum relative distance from the bar's reference price, checked at every trade in the tick pipeline versus only at minute boundaries in the minute pipeline; this implementation lets the displacement shrink on reversal, unlike classical Renko.
- **Hybrid bars.** Bars that close when either a dollar-volume threshold or a realized-volatility threshold is first reached (OR logic), so at least one of two activity signals always drives closure.
- **Adaptive EMA threshold.** The bar-closing threshold is updated after each bar via an exponentially weighted moving average of realized bar sizes, with the EMA rate itself adjusted from the recent coefficient of variation of thresholds; a cap prevents one extreme bar from permanently inflating the threshold.
- **Timeout percentage.** The fraction of bars force-closed by the maximum-duration guard rather than by their activity threshold; a rate above 10% is treated as a sign the threshold is miscalibrated for prevailing conditions.
- **Matched-frequency robustness check.** Coarsening a tick bar series by aggregating consecutive bars until its bar count matches the minute series, to separate genuine resolution effects from the confound that tick pipelines simply sample more often.

## Method

Both pipelines share a two-stage calibration: an initial threshold and duration bounds are estimated from a 14-day lookback window of minute data, then (for the tick pipeline) the threshold is replaced by a tick-native equivalent; thereafter the threshold adapts online via the EMA update. Eight statistical criteria (excess kurtosis, Jarque-Bera, Ljung-Box p-value at 10 lags, variance-ratio deviation |VR(4)-1|, lag-1 autocorrelation |AC1|, bar-size coefficient of variation, Shannon entropy, and timeout percentage) are computed per bar type and pipeline and compared against a frequency-matched fixed-interval time-bar baseline; stationarity (ADF, KPSS) is checked as a prerequisite. Because sample sizes range from roughly thirty thousand to over two hundred thousand bars, the authors treat significance tests as descriptive and lean on effect-size magnitudes rather than p-values for comparative claims.

The matched-frequency analysis re-runs the comparison after coarsening each tick series to the minute pipeline's bar count. The downstream ML experiment builds a common 28-feature set (technical indicators plus microstructure features) for every bar type, trains Random Forest, Gradient Boosting, and SVM classifiers (default hyperparameters, fixed random state) under five-fold walk-forward cross-validation with an embargo gap, and evaluates AUC-ROC, accuracy, annualized Sharpe ratio, and trade count on concatenated out-of-sample predictions; trading signals use a 0.55 confidence threshold, Kelly-fractioned position sizing, and a 0.04% round-trip fee.

## Results

- Tick Renko bars recorded |VR(4)-1|=0.020 and lag-1 autocorrelation=0.002, the strongest random-walk conformance of any series in the study.
- Tick volatility bars cut |VR(4)-1| to 0.028 versus 0.089 for minute volatility bars, a 69% reduction, the largest relative VR improvement of any bar type.
- Dollar bars produced 29,835 bars from the minute pipeline versus 81,683 from the tick pipeline over the six-year sample; the tick pipeline had a 0.0% timeout rate versus 0.9% for minute.
- In the raw six-year scorecard the minute pipeline led on approximately 27 criteria, tick led on about 18, and the time-bar baseline led on 7; time bars were competitive on variance-ratio conformance at short horizons.
- Range bars were the one type where tick underperformed minute on most criteria, with tick excess kurtosis of 150.699 versus 8.191 for minute.
- Tick hybrid bars had the lowest kurtosis (6.77) and Jarque-Bera statistic (174,557) among all tick-source series, 40-fold below the time-bar baseline.
- After coarsening tick series to match minute bar counts, tick dollar bars led on all six matched criteria and matched tick volatility bars reached Ljung-Box p=0.51, recovering serial independence.
- In the downstream ML test, out-of-sample AUC-ROC ranged 0.498-0.596 across every bar type (near chance), with no consistent relationship between statistical bar quality and classifier AUC.

## Limitations

- The study covers a single instrument (BTCUSDT perpetual futures on Binance) over six years; the authors say generalisability to other assets, exchanges and asset classes is untested.
- Renko/displacement bars are calibrated under a shared framework, but the tick and minute pipelines operate at very different resolution scales (a 26-fold difference in bar count), so cross-pipeline Renko comparisons are treated as only indicative.
- The downstream ML experiment used a single unified feature set for all bar types, so tick-native features (VWAP, buy-sell imbalance, tick count) were not exploited, which the authors say may understate the tick pipeline's ML advantage.
- No formal multiple-testing correction is applied across the 48 primary comparisons; the authors treat the test results descriptively rather than as accept/reject decisions.
- Reader note: the adaptive EMA calibration and the tick/minute resolution difference are confounded in this design; the authors state that no ablation isolates the calibration's own contribution from the resolution effect.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/backtesting|backtesting]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]

## Citation

Muhammad Toheed Fayyaz, Abdul Jabbar, Faheem Ahmad Qureshi, Syed Qaisar Jalil (2026). A Frequency-Controlled Comparison of Tick- and Minute-Based Information Bars for Cryptocurrency Markets.

DOI: 10.48550/arxiv.2608.26158

Text ingested: `markdown_output/fayyaz-2026-frequency-controlled-comparison-tick-minute-based.md`, converted from `raw/ofi-event-clock/fayyaz-2026-frequency-controlled-comparison-tick-minute-based.pdf`.

Coverage of this summary: Read the full paper from abstract through conclusion, including the literature review, the calibration and bar-construction methodology (Sections III-IV), the complete empirical results and scorecard table (Section V), the downstream machine-learning experiment (Section VI), and the discussion and matched-frequency robustness analysis (Section VII).

Known problems with the input: year from file metadata.
<!-- AUTHORED REGION END -->