---
authors:
- Yiyang Zheng
content_hash: sha256:506e177f2b0175c6a6c8ac4988bbd03c6d4b797f401b04248741bf687a36f135
created: 2026-09-27 01:47:00+00:00
page_id: sources/zheng-2022-order-flow-technical-analysis-neural-network
page_type: source
related:
- concepts/order-flow-prediction
- concepts/order-imbalance
- concepts/deep-learning-for-finance
- concepts/feature-engineering
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/order-flow
- concepts/backtesting
revision_id: 1
schema_version: 2
source_hash: sha256:728c48bdab0dbc63b27f8975b52165a2645cb70035fa4b71eb3d14df95d2ce68
source_path: markdown_output/zheng-2022-order-flow-technical-analysis-neural-network.md
source_type: paper
tags:
- futures
- order-flow
- order-book-features
- technical-analysis
- deep-learning
- tabnet
- backtesting
- market-microstructure
- clock-calendar
- asset-futures
- harvest-relevant
title: 'Neural Network and Order Flow, Technical Analysis: Predicting short-term direction
  of futures contract'
updated: '2026-09-27T01:47:00Z'
uuid: 7f09671c-9086-599e-9e0b-f639cfd4015e
year: 2022
---

<!-- AUTHORED REGION START -->
# Neural Network and Order Flow, Technical Analysis: Predicting short-term direction of futures contract

## Summary

The paper asks whether combining conventional technical-analysis indicators with order-book and order-flow features derived from a futures exchange's snapshot feed can predict the short-term directional movement of a futures contract, using the near-month Silver futures contract on the Shanghai Futures Exchange as the test case.

Its approach builds technical indicators (volume, volatility, trend and momentum indicators) from 1-minute OHLCV bars, plus order-book features, the accumulated bid-ask spread and volume imbalance across the top five book levels, and order-flow features built by classifying each 500-millisecond exchange snapshot into one of four price/open-interest change types and by computing open-versus-closed contract percentages, including a filter meant to isolate larger, presumably institutional, trades; all of these are computed over rolling windows of 5, 10, 15 and 30 minutes. These features feed a TabNet attention-based neural network, trained with a Purged Group Time Series Split, a gap-inserted, non-shuffled time-series cross-validation across five folds meant to stop rolling-window features from leaking future information, and evaluated with AUC-ROC because the label balance can vary over time.

On roughly four years of snapshot data (January 2018 to December 2021), the target, the sign of a 2-minute VWAP-smoothed log return measured 15 minutes ahead, was close to balanced (50.88% versus 49.11% of samples), and the ensembled five-fold model reached an accuracy of 0.601339, a recall of 0.590069, and a Pearson correlation of 0.207273 against the target on a held-out September-December 2021 test period. A simple long/short trading rule, opening a position only when the predicted probability passed a 0.25 confidence margin around 0.5 and holding either 100% cash or the full contract at the minimum 10% margin, turned this into a 20.48% total return over the test period, with a 24.08% maximum drawdown and an annualized Sharpe ratio of 1.2054, despite the underlying futures price ending the period close to unchanged.

What is new, by the paper's own account, is combining technical, order-book and order-flow feature families rather than relying on one alone, adding an institutional-trade filter to the order-flow classification, and using a purged, gapped time-series split rather than a conventional cross-validation so that reported accuracy stays comparatively stable across the sample period rather than reflecting a single lucky split.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The exchange supplies 500-millisecond snapshots of trades, order-book depth and open interest through a proprietary feed rather than a full order-by-order record. Snapshots are aggregated into 1-minute OHLCV bars (120 snapshots) for the technical-analysis features, and order-book and order-flow features use rolling windows of 5, 10, 15 and 30 minutes of snapshots. The prediction target is the sign of the log return of a 2-minute (120-snapshot) rolling VWAP measured 15 minutes ahead, with zero-return and near-zero-return observations (|R(t)| below 0.001) dropped from the training target.

## Data

- **Asset class:** Futures
- **Instruments:** Near-month Silver Futures Contract listed on the Shanghai Futures Exchange, described as one of the most heavily traded precious-metal futures contracts, with a 2021 annual volume of 231,457 thousand contracts versus 26,126 thousand contracts for COMEX silver
- **Venue:** Shanghai Futures Exchange
- **Period:** January 2018 to December 2021 overall; training subset January 2018 to August 2021; validation/test subset September 2021 to December 2021
- **Granularity:** 500-millisecond snapshot feed (CTP protocol) of trades, order-book depth and open interest, aggregated to 1-minute OHLCV bars for the technical-analysis features

## Features and Measures

- **Snapshot type classification.** Each snapshot is labelled Type 1-4 depending on whether price rose or fell and whether open interest rose or fell, meant to proxy whether long or short positions are being opened or closed.
- **Accumulated order-book spread / volume imbalance.** For each snapshot, the bid-ask spread and the ask-minus-bid size imbalance are accumulated across the top five order-book levels and then rolling-averaged over 5, 10, 15 and 30-minute windows.
- **Order-flow percentage features.** The percentage of each of the four snapshot types, plus the ratio of closed to opened contracts and the percentage change in open interest, computed over the same rolling windows, with a filter that excludes snapshots with volume change below 10 contracts to emphasise larger, presumably institutional, activity.
- **Technical analysis indicator set.** A standard set of volume, volatility (Bollinger, Keltner, Donchian bands), trend (MACD, SMA) and momentum (Stochastic RSI) indicators computed from the 1-minute OHLCV bars.

## Method

Raw 500-millisecond exchange snapshots are first used to derive per-snapshot volume and open-interest changes and, from those, the contracts opened and closed at each snapshot, feeding the order-flow features; technical-analysis indicators are computed from 1-minute OHLCV bars built from the same snapshots. All candidate features are screened by Pearson correlation against the target before modelling. The prediction model is TabNet, an attention-based neural network for tabular data (with decision-layer and attention-embedding widths of 32 and 5 decision steps), trained with a five-fold Purged Group Time Series Split that enforces non-shuffled, forward-only validation indices and a gap between training and validation folds to prevent rolling or lagged features from leaking future information. Model quality during training is judged by AUC-ROC because the label balance can vary over time, and once the five fold-models are ensembled, performance on a later out-of-sample period is judged by accuracy, recall and Pearson correlation against the realized label. A simple long/short backtest then converts the ensembled probability into positions using a confidence threshold around 0.5, assuming a single, fully-margined position at a time, fills at the last traded price, and no transaction fees, and reports total return, maximum drawdown and an annualized Sharpe ratio.

## Results

- Filtering out zero-return and near-zero-movement targets shrank the sample from 38,294,652 observations to 24,347,353, split 50.88% versus 49.11% between the two direction labels.
- On the held-out September-December 2021 test period the ensembled five-fold model reached an accuracy of 0.601339, a recall of 0.590069, and a Pearson correlation of 0.207273 between predicted probability and the realized target.
- A simple long/short trading rule using a 0.25 confidence threshold produced a total return of 20.48% over that test period.
- The same backtest showed a maximum drawdown of 24.08% and an annualized Sharpe ratio of 1.2054.
- The order-book spread and volume-imbalance feature groups each generated 20 features (five book levels by four rolling window lengths), and the snapshot-type order-flow features generated 32 features.

## Limitations

- The backtest ignores exchange and broker trading fees and assumes every order fills exactly at the last traded price.
- The backtest uses the exchange's minimum margin ratio of 10%, which implies substantial leverage and which the authors themselves link to the volatility of daily strategy returns.
- Hyper-parameters were fixed rather than tuned, a deliberate choice the authors made to avoid overfitting, but this also means the reported accuracy may not reflect the model's best achievable performance.
- The study covers a single instrument (Shanghai Silver futures) and a single out-of-sample test window (September-December 2021), so generalization to other contracts or periods is untested within the paper.
- Reader note: an accuracy of 0.601339 and Pearson correlation of 0.207273 indicate a fairly weak predictive edge in absolute terms, and the reported profitability depends heavily on the assumed 10% margin (leverage) and zero-fee execution.

## Related

- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-flow|order flow]]
- [[concepts/backtesting|backtesting]]

## Citation

Yiyang Zheng (2022). Neural Network and Order Flow, Technical Analysis: Predicting short-term direction of futures contract.

DOI: 10.36227/techrxiv.19154276

Text ingested: `markdown_output/zheng-2022-order-flow-technical-analysis-neural-network.md`, converted from `raw/ofi-event-clock/zheng-2022-order-flow-technical-analysis-neural-network.pdf`.

Coverage of this summary: Read the entire paper: abstract, introduction, problem statement and target construction (Section 2), data and feature engineering (Sections 3-4), model, training and validation (Sections 5-6), backtesting (Section 6.3), conclusion (Section 7), and the reference list.

Known problems with the input: No explicit publication year is printed on the paper itself; year is taken from the job file's year_hint (2022), which is consistent with the references list's cited access dates of 2022-01-15; year from file metadata; The markdown converts several equations to '==> picture... omitted <==' placeholders and mangles some decimal points and thousands separators with stray spaces (e.g. '38,294,652', '0. 25'); the underlying digit sequences used here are unchanged from the source, only the display spacing was normalized.
<!-- AUTHORED REGION END -->