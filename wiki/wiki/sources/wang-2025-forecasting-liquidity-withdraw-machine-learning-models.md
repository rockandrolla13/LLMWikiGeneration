---
authors:
- Haochuan (Kevin) Wang
content_hash: sha256:64a7423be36f8e3640483930a7bd28ed0d93459c15b6e1635dd281806f8f92b7
created: 2026-09-27 01:47:00+00:00
page_id: sources/wang-2025-forecasting-liquidity-withdraw-machine-learning-models
page_type: source
related:
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/limit-order-book
- concepts/high-frequency-data
- concepts/order-flow-prediction
- concepts/liquidity-risk
- concepts/bid-ask-spread
revision_id: 1
schema_version: 2
source_hash: sha256:b82974bbe4c9dc5d43f8aa600ef02016b594a0c13b91be68d9a177e153262f98
source_path: markdown_output/wang-2025-forecasting-liquidity-withdraw-machine-learning-models.md
source_type: paper
tags:
- liquidity-withdrawal
- order-book
- market-microstructure
- machine-learning
- xgboost
- forecasting-horizon
- mbo-data
- reproducibility
- clock-calendar
- asset-equity
- harvest-relevant
title: Forecasting Liquidity Withdrawal with Machine Learning Models
updated: '2026-09-27T01:47:00Z'
uuid: 4e71b0d2-eb5b-5f83-979e-ad8f9ca3550f
year: 2025
---

<!-- AUTHORED REGION START -->
# Forecasting Liquidity Withdrawal with Machine Learning Models

## Summary

The paper asks how far ahead, and how well, short-horizon liquidity withdrawal in equity limit order books can be forecast. It defines a new Liquidity Withdrawal Index (LWI): the ratio of order cancellations to the sum of smoothed prior top-of-book depth and new additions at the best quotes. The book is reconstructed from Nasdaq market-by-order data, resampled to a fixed 250 millisecond grid, and a feature panel is built around LWI, spreads, depth, order flow imbalance, and queue imbalance.

Two model families are compared at four horizons (250 ms, 1 s, 2 s, 5 s): linear AR and HAR benchmarks, and a non-linear XGBoost tree ensemble, evaluated with walk-forward cross-validation and an embargo to avoid look-ahead leakage. A closed-form AR(1)-plus-noise benchmark separates the mechanical R-squared gain that comes from averaging the target over more bins at longer horizons from genuine multi-scale predictability, with its parameters identifiable directly from the series' own autocovariances.

Forecastability is horizon-dependent: 250 ms forecasts are noise-dominated, XGBoost wins at 1 s and 5 s, and HAR is competitive, and best for most symbols, at 2 s. In a separate, fully public replication on 2012 LOBSTER AAPL data, the horizon-dependent structure and the value of multi-scale predictors carry over, but the level of predictability and which model wins do not: in that wider-spread, thinner-book regime the top-of-book LWI is close to noise, and a regularized linear (Ridge) model matches or beats the tree ensemble.

What is new is targeting liquidity withdrawal itself, rather than mid-price direction, as the forecasting object; packaging it as an interpretable, scale-free index; and pairing every empirical claim with a theoretical aggregation bound and an independent public-data replication that separates structural findings from sample-specific ones.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Market-by-order messages are aligned to a uniform 250 millisecond Eastern-Time grid and the book is reconstructed at each bin. The forecast target is the mean LWI over the next k bins, where k = 1 corresponds to the 250 ms horizon and k = 20 to the 5 s horizon, so longer horizons predict an average of several future bins rather than a single future value. The same 250 ms-grid protocol, with a 10 s embargo between train and test folds, is used in both the commercial sample and the public-data replication.

## Data

- **Asset class:** Equities
- **Instruments:** seven actively traded Nasdaq-listed US equities across two liquidity tiers: three large-cap names (AAPL, NVDA, TSLA) and four mid-cap names (HIMS, NBIS, RKLB, SNAP); the robustness check uses AAPL only
- **Venue:** Nasdaq (Databento market-by-order feed); the robustness check reconstructs the book from Nasdaq TotalView-ITCH via the public LOBSTER dataset
- **Period:** 30 July 2025, 14:00-15:00 ET (one hour) for the main sample; 21 June 2012, evaluated over 10:00-15:30 ET, for the public robustness sample
- **Granularity:** market-by-order (MBO) messages resampled onto a 250 ms grid; top-of-book depth in the main sample, plus a 10-level book-wide LWI variant in the robustness check

## Features and Measures

- **Liquidity Withdrawal Index (LWI).** the ratio of order cancellations to the sum of smoothed prior top-of-book depth and new additions at the best quotes over a 250 ms bin, a non-negative, scale-free measure of transient liquidity removal stabilized with a short moving average and a positive floor.
- **Order flow imbalance (OFI).** a feature built from the MBO stream capturing the net directional pressure of order additions and cancellations, used as a predictor of future LWI.
- **Queue imbalance (QI).** a feature describing the relative buy/sell depth imbalance at the top of book, used as a predictor of LWI.
- **Consensus feature set.** features that rank consistently across mutual information, XGBoost importance, and LASSO shrinkage in at least 60% of tickers, dominated by short-horizon LWI lags and rolling volatilities of spread, depth, and order flow.

## Method

The pipeline reconstructs the book from Databento MBO events, resamples to a 250 ms grid, and builds a feature panel of spreads, top-of-book depth, order flow imbalance, queue imbalance, rolling means and volatilities, and add/cancel activity rates. A cross-ticker feature-selection procedure combining mutual information, XGBoost importance, and LASSO on four of the seven symbols yields a consensus feature set that is then applied to all seven symbols. Two model families are compared at four horizons (250 ms, 1 s, 2 s, 5 s): linear AR(5) and HAR benchmarks, and a non-linear XGBoost tree ensemble, evaluated with five-fold expanding-window walk-forward cross-validation with an embargo to prevent look-ahead leakage.

A closed-form AR(1)-plus-noise state-space benchmark gives an upper bound on the population R-squared attainable from a series' own history at each aggregation horizon, with parameters identified from the first two sample autocovariances of LWI, letting the author separate mechanical smoothing gains from genuine multi-scale predictability. The whole pipeline is then replicated end-to-end on the public LOBSTER AAPL 2012 sample, adding a trailing-mean persistence baseline, a Ridge regression on the full feature set, and Diebold-Mariano tests with Newey-West standard errors to check statistical significance and which findings generalize.

## Results

- At the 250 ms horizon, out-of-sample R-squared is near zero or negative for every model in the July 2025 sample: forecasts are noise-dominated.
- At 1 s, XGBoost is the best model for all seven symbols; HAR only improves on AR for three of seven symbols (AAPL, NVDA, TSLA) at this horizon.
- At 2 s, HAR improves on AR for every symbol and is the best model for five of seven symbols.
- At 5 s, XGBoost dominates for all seven symbols, with R-squared above 0.90 for six of seven, while AR(5) turns negative for four symbols.
- In the public LOBSTER AAPL 2012 robustness check, the top-of-book LWI is essentially unforecastable (best R-squared 0.053, from Ridge at 1 s), while the book-wide (10-level) LWI variant is moderately forecastable with R-squared rising from 0.114 at 250 ms to 0.153 at 5 s for Ridge.
- In the robustness check, a Ridge regression on the same features matches or beats XGBoost at every horizon in both LWI variants, with the difference statistically significant in Ridge's favor at 5 s for the top-of-book variant (Diebold-Mariano statistic 2.59, p = 0.010).
- The book-wide LWI's HAR R-squared exceeds the calibrated single-component aggregation bound at 2 s and 5 s, rejecting a single-component model and indicating genuine multi-scale cancellation dynamics; the top-of-book variant's univariate forecasts stay below the bound at every horizon.
- The estimated signal share (variance from the persistent component versus noise) is 9.1% for the top-of-book LWI and 41.7% for the book-wide LWI in the robustness sample.

## Limitations

- The main (July 2025) sample covers a single hour of a single trading day across seven symbols on one venue; the commercial data cannot be redistributed, so those results are not independently reproducible.
- R-squared at longer horizons is partly a mechanical artefact of averaging the target over more bins, not purely additional model skill.
- The public robustness sample covers a single symbol-day (AAPL, 21 June 2012) in a different, wider-spread liquidity regime, so its magnitudes and model ranking do not necessarily apply to the 2025 sample.
- Neither sample evaluates economic value, such as execution-cost savings, from acting on the forecasts.
- Reader note: the consensus feature-selection step was fit on only four of the seven symbols before being applied to all seven.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/liquidity-risk|liquidity risk]]
- [[concepts/bid-ask-spread|bid ask spread]]

## Citation

Haochuan (Kevin) Wang (2025). Forecasting Liquidity Withdrawal with Machine Learning Models.

Text ingested: `markdown_output/wang-2025-forecasting-liquidity-withdraw-machine-learning-models.md`, converted from `raw/ofi-event-clock/wang-2025-forecasting-liquidity-withdraw-machine-learning-models.pdf`.

Coverage of this summary: Read the whole markdown file, abstract through conclusion, including all tables and appendices.

Known problems with the input: Table 1 (consensus feature ranking) has corrupted/truncated feature-name formatting in the markdown conversion; exact per-feature names were not relied on for this reason.
<!-- AUTHORED REGION END -->