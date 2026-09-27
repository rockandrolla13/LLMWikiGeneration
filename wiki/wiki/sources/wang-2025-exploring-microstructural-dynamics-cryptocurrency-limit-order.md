---
authors:
- Haochuan (Kevin) Wang
content_hash: sha256:97aab9af5fe7e16b443f81c56dad0ed5292cde224e1f98a4c2691a806655e3bc
created: 2026-09-27 01:47:00+00:00
page_id: sources/wang-2025-exploring-microstructural-dynamics-cryptocurrency-limit-order
page_type: source
related:
- concepts/limit-order-book
- concepts/order-imbalance
- concepts/high-frequency-trading
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/feature-engineering
- concepts/market-microstructure-noise
- concepts/high-frequency-data
- concepts/mid-price-prediction
revision_id: 1
schema_version: 2
source_hash: sha256:8d0c3e1d27123cd3d27a17b93854a846486fe7866337abb6333a7ef942134eb6
source_path: markdown_output/wang-2025-exploring-microstructural-dynamics-cryptocurrency-limit-order.md
source_type: paper
tags:
- cryptocurrency
- limit-order-book
- deep-learning
- xgboost
- denoising
- mid-price-prediction
- high-frequency-trading
- bybit
- clock-calendar
- asset-crypto
- harvest-relevant
title: 'Exploring Microstructural Dynamics in Cryptocurrency Limit Order Books: Better
  Inputs Matter More Than Stacking Another Hidden Layer'
updated: '2026-09-27T01:47:00Z'
uuid: 4c35551a-43b5-509d-b1f3-9225d82d948d
year: 2025
---

<!-- AUTHORED REGION START -->
# Exploring Microstructural Dynamics in Cryptocurrency Limit Order Books: Better Inputs Matter More Than Stacking Another Hidden Layer

## Summary

The paper asks whether adding hidden layers or parameters to deep limit-order-book (LOB) models genuinely improves short-horizon price direction forecasting, or whether reported gains mainly come from data preprocessing and feature engineering rather than architectural depth. It works with raw, publicly available BTC/USDT top-of-book snapshots from Bybit taken every 100 ms, and compares six models -- logistic regression, XGBoost, CatBoost, a simpler single-layer CNN+LSTM, a CNN+XGBoost hybrid, and DeepLOB -- on both binary (up/down) and ternary (up/flat/down) mid-price direction labels at 100ms, 500ms and 1second prediction horizons.

Before modeling, the author applies and compares two denoising pipelines against the raw data: a Kalman filter that treats each LOB feature series as a noisy observation of a latent random-walk state, and a Savitzky-Golay filter that fits a rolling cubic polynomial over a window to smooth curvature while suppressing high-frequency noise. Every model is trained and evaluated on all three versions of the data (raw, Kalman, Savitzky-Golay) using the same architecture and pipeline, scored by per-class F1 and overall accuracy, with separate experiments that vary the required order-book depth (40, 10 or 5 levels) and the number of past snapshots stacked as input (a single 100 ms snapshot versus ten stacked snapshots spanning one second).

Savitzky-Golay smoothing improved every model at every horizon, while Kalman-filtered data sometimes underperformed even the raw data, which the author attributes to the Kalman filter's noise-covariance parameters being fixed after only a limited grid search rather than tuned as flexibly as the Savitzky-Golay window. Simple models (logistic regression, XGBoost) matched or slightly beat the deep architectures despite training and running far faster; requiring deeper order-book levels raised accuracy but sharply reduced the number of usable snapshots, and stacking ten past snapshots instead of one raised accuracy modestly at the cost of much longer training time.

What is new relative to prior LOB deep-learning work is the direct, controlled comparison of the same architectures across raw and two denoised versions of un-preprocessed, publicly sourced crypto data, arguing that for high-frequency LOB direction forecasting, input quality, prediction horizon and required book depth matter more than stacking extra convolutional or recurrent layers.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Limit order book snapshots (the top 200 Bybit bid and ask levels) are sampled at fixed 100 ms intervals rather than per event or per trade. Each model input is a window of T consecutive snapshots (T=1, a single 100 ms snapshot, or T=10, spanning one second of history), used to predict the direction of the mid-price 100ms, 500ms or 1second after the end of that window.

## Data

- **Asset class:** Crypto
- **Instruments:** BTC/USDT (Bybit)
- **Venue:** Bybit
- **Period:** single trading day, 2025-01-30
- **Granularity:** 100 ms LOB snapshots (top 200 bid/ask levels), with most experiments restricted to 40, 10 or 5 levels due to missing-depth filtering

## Features and Measures

- **Cumulative order book depth.** Bid and ask quantities aggregated across successive price levels into a cumulative order book, on the reasoning that cumulative supply-demand asymmetries tend to precede short-horizon mid-price moves.
- **Weighted level imbalance feature.** A hand-crafted feature combining level-i bid and ask prices and sizes with weights that sum to one, used as input to the logistic regression and XGBoost baselines rather than to the CNN-based models, which learn feature combinations automatically.

## Method

Six models are compared: a logistic regression and an XGBoost classifier trained on flattened or hand-crafted LOB features; a CNN+CatBoost pipeline where a 1D CNN produces a 64-dimensional embedding later classified by CatBoost; a CNN+XGBoost variant using the same embedding idea with an XGBoost classifier instead; a simpler single-Conv2D-layer CNN followed by a bidirectional LSTM; and DeepLOB, which stacks three Conv2D blocks before an LSTM(64) layer and is trained with focal loss and class weights to focus on minority up/down movements.

All models are evaluated with an 80%/20% train-test split, holding out 20% of the training set for validation, and are scored by per-class F1 (the harmonic mean of precision and recall) and by overall accuracy. To isolate the effect of denoising from architecture, every model is run three times on the same train/test split -- once on raw snapshots, once on Kalman-filtered snapshots, and once on Savitzky-Golay-smoothed snapshots -- holding the model and training pipeline fixed across the three runs. Additional experiments vary the minimum required order-book depth (discarding snapshots missing bid/ask levels below a chosen depth) and the number of stacked past snapshots (T=1 versus T=10) to trade off sample coverage, temporal context, accuracy and training/inference latency.

## Results

- Savitzky-Golay-smoothed data produced the best out-of-sample F1 scores across every model and horizon in both the ternary and binary classification tables, with no significant difference in accuracy between the six model types once smoothed.
- For ternary classification at the 500 ms horizon with a 40-level book, logistic regression on Savitzky-Golay-smoothed data reached an F1 score of 0.5434, the best result in that table.
- For binary classification at the 500 ms horizon with a 40-level book, logistic regression on Savitzky-Golay-smoothed data reached an F1 score of 0.7284, the best result in that table.
- Kalman-filtered data sometimes performed worse than the raw, unsmoothed data because its process- and measurement-noise parameters were fixed after only a limited grid search on a smaller sample, unlike the more flexibly tunable Savitzky-Golay window.
- Reducing the required order-book depth from 40 to 5 levels raised the number of usable test snapshots from 5,442 to 18,336 but lowered accuracy and F1 (accuracy fell from 0.715 to 0.580), showing a trade-off between market coverage and predictive performance.
- Stacking ten 100 ms snapshots (T=10) instead of one (T=1) raised both XGBoost's and logistic regression's accuracy by about 2%, but training time rose sharply -- for XGBoost, from 1 m 36 s to 7 m 04 s.
- Across all horizons, depths and filters tested, binary and ternary classification accuracy ranged from 0.42 to 0.71, and the simpler models (XGBoost, logistic regression) matched or slightly outperformed the deep architectures (DeepLOB, CNN+LSTM) while running much faster.

## Limitations

- The analysis is restricted to a single BTC/USDT trading day (2025-01-30) on one exchange (Bybit); the author states further testing across additional days and market conditions is needed to assess robustness.
- The Kalman filter's parameters were tuned only via a limited grid search on a smaller sample due to computation constraints, which the author notes may understate its true potential relative to Savitzky-Golay smoothing.
- The author did not test CNN architectures deeper than three convolutional layers or wider than 128 dimensions per layer, reasoning that the added inference latency would likely erase any predictive edge.
- All experiments were run offline in Python; the author states that real-time deployment would require further evaluation, strategy development and hardware acceleration.
- Reader note: the paper studies only a single, highly liquid crypto pair (BTC/USDT); the author himself flags that results may not transfer to less liquid cryptocurrencies or other asset classes without further testing.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]

## Citation

Haochuan (Kevin) Wang (2025). Exploring Microstructural Dynamics in Cryptocurrency Limit Order Books: Better Inputs Matter More Than Stacking Another Hidden Layer.

DOI: 10.48550/arxiv.2506.05764

Text ingested: `markdown_output/wang-2025-exploring-microstructural-dynamics-cryptocurrency-limit-order.md`, converted from `raw/ofi-event-clock/wang-2025-exploring-microstructural-dynamics-cryptocurrency-limit-order.pdf`.

Coverage of this summary: Read the entire markdown file front to back, including the introduction, literature review, data, methods, all results tables, and the conclusion.

Known problems with the input: Several equations and figures are rendered only as 'picture... intentionally omitted' by the PDF-to-markdown conversion, so exact formula details (e.g. the imbalance/weight formula, the F1 formula, the Kalman and Savitzky-Golay update equations) could not be verified beyond the surrounding prose description; The converted text contains occasional OCR/typo artifacts (e.g. 'bais cuased' for 'bias caused', split subscripts) that did not appear to change the reported numbers or findings.
<!-- AUTHORED REGION END -->