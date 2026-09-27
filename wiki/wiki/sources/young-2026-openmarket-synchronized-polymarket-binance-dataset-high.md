---
authors:
- Gregory Young
content_hash: sha256:bd6582f0b981472cb14c3a455bb4adc85add4a30009ea589611a0a8c4529ea5c
created: 2026-09-27 01:47:00+00:00
page_id: sources/young-2026-openmarket-synchronized-polymarket-binance-dataset-high
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/high-frequency-trading
- concepts/order-flow-imbalance
- concepts/backtesting
revision_id: 1
schema_version: 2
source_hash: sha256:b059769296ba998fe3a2a28b07bb0be5938cba533e762491dc78d5be2220d4d4
source_path: markdown_output/young-2026-openmarket-synchronized-polymarket-binance-dataset-high.md
source_type: paper
tags:
- prediction-markets
- crypto-microstructure
- clock-synchronization
- lead-lag
- polymarket
- walk-forward-forecasting
- null-result
- clock-event
- asset-multi
- harvest-relevant
title: 'OpenMarket: A Synchronized Polymarket–Binance Dataset for High-Frequency Prediction-Market
  Research'
updated: '2026-09-27T01:47:00Z'
uuid: 95ff95db-d205-5c2d-a5f8-f035734d268a
year: 2026
---

<!-- AUTHORED REGION START -->
# OpenMarket: A Synchronized Polymarket–Binance Dataset for High-Frequency Prediction-Market Research

## Summary

OpenMarket investigates whether Binance BTC/USDT order flow and microstructure signals can predict the outcome of Polymarket's 15-minute BTC binary markets better than the market's own implied probability. It began as an attempt to trade this edge, using WebSocket collectors for both venues, a millisecond-precision recorder, order-book and price features, and a walk-forward calibrated logistic model.

The released corpus pairs Polymarket and Binance events inside a bounded millisecond window and stores both the exchange-emitted and collector-received timestamp for every event, so that clock drift and pairing-window sensitivity can be measured directly rather than assumed away. Forty-three microstructure features are exported per market and fed into a walk-forward logistic regression with Platt scaling, evaluated against a naive Polymarket mid-price prior sampled at the same timestamp.

Out-of-sample, the logistic model does not beat, and slightly underperforms, the naive mid prior, and a simulated positive-EV trading rule loses money once fees and slippage are applied. The paper also reports descriptive microstructure facts: Polymarket top-of-book spreads are almost always one tick wide, cross-venue lead-lag has a compact median but heavy tails, and quotes only move roughly a third of a second after large Binance price moves.

What is new is not the trading result but the public infrastructure: a deduplicated, versioned corpus of hundreds of millions of paired rows, explicit lag-pairing metadata with quality flags, and reproducible Rust exporters and trainers, positioned as a data-and-methods release whose central empirical result is a negative one.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are individual exchange events, Polymarket order-book ticks and Binance trades, each carrying both a source (exchange) and an ingest (collector) timestamp in milliseconds; each Polymarket tick is paired with its nearest untaken Binance tick inside a 750 ms window to compute a lead-lag time difference. For the forecasting benchmark, 43 microstructure features are sampled at a single feature-cutoff timestamp per rolling 15-minute BTC market, and the prediction target is that market's own settlement outcome, so the horizon is fixed by each market's expiry rather than a uniform clock step.

## Data

- **Asset class:** Several asset classes
- **Instruments:** Polymarket BTC 15-minute UP/DOWN binary contracts; Binance BTC/USDT spot
- **Venue:** Polymarket (decentralized, Polygon-settled) and Binance (centralized crypto exchange)
- **Period:** Event data spans 2026-02-12 to 2026-05-15 (54 observed Polymarket days, 57 Binance days); archival snapshots were published 2026-03-14 to 2026-07-01.
- **Granularity:** Millisecond-level ticks and trades, paired within a 750 ms window; forecasting features computed at market-level feature-cutoff timestamps for rolling 15-minute markets.

## Features and Measures

- **lead_lag_ms.** Millisecond difference between the source timestamp of a paired Polymarket event and its nearest matched Binance event, used to characterize apparent cross-venue timing.
- **quality_flag.** Categorical tag (tight, medium or wide) assigned to each lead-lag pair based on the absolute value of lead_lag_ms relative to 100 ms and 300 ms cutoffs within the 750 ms search window.
- **step3 microstructure features.** Forty-three features exported per market from order-book metrics (spread, best bid/ask, microprice, imbalance, depth, book update velocity), price metrics (returns, realized volatility, momentum, VWAP deviation, candle shape) and technical indicators, used as inputs to the walk-forward logistic model.
- **imbalance_60s.** A 60-second order-flow imbalance feature tested on its own as a simple forecast baseline against the pooled logistic model and the naive mid prior.
- **drift_prob_up.** A drift-based probability-of-up feature evaluated alone as a diagnostic baseline against the naive Polymarket mid prior.

## Method

The system is a Rust pipeline with separate WebSocket collectors for Binance and Polymarket, a synchronizer that pairs events across venues, and downstream feature, training, and backtesting stages. Order-book, price, and technical-indicator features are exported into a canonical Parquet table of microstructure features per market, and a walk-forward logistic regression is trained per market with Platt-scaled probability calibration, using only pre-cutoff rows for fitting within each window.

Performance is judged by both predictive metrics (AUC, Brier score, expected calibration error, log loss) computed on strictly out-of-sample scored rows across walk-forward windows, and by simulated economic metrics (win rate, PnL, Sharpe, drawdown) under stated fee and slippage assumptions. The primary comparison is the pooled out-of-sample model against a naive Polymarket mid-price prior sampled at the identical feature-cutoff timestamp, so both use the same information timing.

Synchronization quality is assessed separately from the forecasting question: per-venue transport-delay envelopes (ingest minus source timestamp) are used to bound relative clock drift, and a synchronization-free causal-ordering test, based only on the collector's own clock, checks whether Polymarket quotes move after large Binance price moves without relying on any cross-venue timestamp comparison.

## Results

- The unified corpus contains 727,098,247 deduplicated rows across 202 archival snapshots, with event data on 54 Polymarket days (57 Binance days) between 2026-02-12 and 2026-05-15.
- Lead-lag pairing produced 2,936,031 matched event pairs with a median apparent lead-lag of 16 ms and 5th/95th percentiles of -186 ms and 316 ms.
- Per-venue transport-delay envelopes bound relative clock drift to at most 6 ms across the archive but leave an unresolved single-vantage constant-offset ambiguity of about 99 ms.
- Measured only on the collector's own clock, Polymarket quotes moved one tick a median of 347 ms after Binance moves of at least 5 basis points.
- Pooled out-of-sample walk-forward logistic regression scored AUC 0.8377, Brier 0.165, and ECE 0.026, versus the naive Polymarket mid prior's AUC 0.8405, Brier 0.163, and ECE 0.014, so the model did not beat the market prior.
- Simulated positive-EV trading under 1% fees and 0.5% slippage produced -0.116 normalized payoff units per attempted trade.
- Polymarket top-of-book spreads were one tick wide (median 0.01 probability points) in 91.9% of observations.
- Median lead-lag stayed within a narrow 16-19 ms band across both price-disagreement quintiles and regime terciles, so cross-venue timing did not shift with the size of price disagreement.

## Limitations

- A single collection vantage point cannot separate the constant component of cross-venue clock offset from network latency, leaving roughly a 99 ms ambiguity in lead-lag values.
- Findings come from one niche, high-activity market (BTC 15-minute Polymarket binaries) and may not transfer to slower political or macro prediction markets with thinner books.
- The step3 feature export covers only 2,251 of 4,450 tracked markets because of missing ticks, insufficient Binance trades, or other data gaps.
- Only a single walk-forward logistic-Platt model is benchmarked as a frozen release; tree-ensemble and neural sequence model comparisons are left as future work.
- Reader note: the paper's central result is itself a null finding, no walk-forward model beat the market prior net of costs, so it should not be read as evidence of a usable trading edge.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/backtesting|backtesting]]

## Citation

Gregory Young (2026). OpenMarket: A Synchronized Polymarket–Binance Dataset for High-Frequency Prediction-Market Research.

Text ingested: `markdown_output/young-2026-openmarket-synchronized-polymarket-binance-dataset-high.md`, converted from `raw/ofi-event-clock/young-2026-openmarket-synchronized-polymarket-binance-dataset-high.pdf`.

Coverage of this summary: Read the full markdown paper end to end, including abstract, introduction, background, system architecture, synchronization methodology, features and machine learning, backtesting framework, dataset description, microstructure findings, discussion, limitations, and conclusion.
<!-- AUTHORED REGION END -->