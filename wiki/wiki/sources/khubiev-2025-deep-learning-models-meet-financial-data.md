---
authors:
- Kasymkhan Khubiyev
- Mikhail Semenov
content_hash: sha256:d8fd8a49d983cd18a5645615b4ab812548ba7a32819aa048a243fe12f2ed1620
created: 2026-09-27 01:47:00+00:00
page_id: sources/khubiev-2025-deep-learning-models-meet-financial-data
page_type: source
publication_venue: 'Preprint for the MathAI: Mathematics of Artificial Intelligence
  conference'
related:
- concepts/sampling-clocks
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/high-frequency-trading
- concepts/lstm-networks
- concepts/market-making
- concepts/feature-engineering
- concepts/mid-price-prediction
revision_id: 1
schema_version: 2
source_hash: sha256:b17ae4629d606d334bb2fd39c2cf8571b63ee019064a4fec24c051c74d48b15e
source_path: markdown_output/khubiev-2025-deep-learning-models-meet-financial-data.md
source_type: paper
tags:
- limit-order-book
- cryptocurrency
- deep-learning-for-finance
- cnn-lstm
- market-making
- mid-price-forecasting
- clock-compares
- asset-crypto
- harvest-relevant
title: Deep Learning Models Meet Financial Data Modalities
updated: '2026-09-27T01:47:00Z'
uuid: ff32f8fc-b7cb-5f68-8e3b-ed49a37a8c82
year: 2025
---

<!-- AUTHORED REGION START -->
# Deep Learning Models Meet Financial Data Modalities

## Summary

The paper treats the limit order book (LOB) as its own financial data modality, distinct from candlestick time series, and asks how best to embed sequences of LOB snapshots into a deep-learning-friendly image representation for short-horizon mid-price forecasting and algorithmic trading.

LOB snapshots for nine cryptocurrency perpetual futures (including BTC and ETH) were collected from the ByBit exchange at roughly 200-300 millisecond intervals, with 50 price levels on each side. Ask and bid prices are scaled relative to the current mid-price, and order sizes are min-max scaled within the current snapshot before being mapped to 0-255 pixel-like values. Sequences of snapshots are then embedded either by stacking each snapshot as a separate image channel ('stacked') or by concatenating snapshots side by side into one larger 2D image ('merged'); four CNN-based architectures, including a CNN2LSTM model, are trained to predict either the mid-price delta or its relative return over horizons from 0.2 to 60 seconds.

The stacked CNN2LSTM model achieved the lowest forecasting error overall (MAPE 0.018244%, versus 0.103163% for a simple CNN), and stacked embeddings beat merged embeddings on average (0.060703% vs. 0.361174% MAPE). Forecast error grows by about 10 times as the horizon extends from 0.2 to 60 seconds, and predicting the price delta works better at short horizons while predicting relative return works better at longer horizons. Only BTC and ETH had a volume-change correlation above 0.7 among the nine assets studied; training one model on pooled BTC and ETH data ('one-shot') cut the error to roughly a quarter of the single-asset model's error at short horizons. A simulated market-making strategy built on the CNN2LSTM forecasts showed a positive profit growth rate for both BTC (Sharpe ratio 7.89) and ETH (Sharpe ratio 4.48), while a merged-image CNN model performed poorly and tended to hold a long position.

What is new is treating stacked LOB snapshots as image channels (rather than merging them into one image) as an embedding technique, and pairing that representation with a market-making trading strategy evaluated directly on Sharpe ratio, profit and loss, and drawdown rather than forecasting accuracy alone.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Raw LOB snapshots arrive roughly every 200-300 ms and are aggregated in two competing ways: a non-overlapping scheme that groups snapshots inside fixed real-time windows (e.g. 1 second, 5 seconds), and a sliding-window scheme that groups a fixed number of consecutive snapshots (e.g. 3, 5, 10, or 30 snapshots, denoted 3w/5w/10w/30w) regardless of elapsed calendar time. The prediction horizon is a fixed forward time offset from the end of the input sequence, tested at 0.2s, 1s, 5s, 10s, 30s and 60s ahead, with the model predicting either the mid-price change (delta) or its relative return at that horizon.

## Data

- **Asset class:** Crypto
- **Instruments:** nine cryptocurrency perpetual futures: BTC, ETH, SOL, ADA, TRX, TON, BNB, DOGE, GOAT
- **Venue:** ByBit cryptocurrency exchange
- **Period:** November 27-29, 2024; training data drawn from November 27, 2024, trading-strategy test data from November 28, 2024
- **Granularity:** LOB snapshots roughly every 200-300 ms, depth of 50 unique price levels on each side

## Features and Measures

- **Stacked LOB image embedding.** Represents a sequence of L consecutive LOB snapshots as an image with L channels (like RGB channels), each channel holding one snapshot's scaled ask/bid price and volume levels.
- **Merged LOB image embedding.** Concatenates L consecutive LOB snapshots side by side into a single 2-dimensional image rather than treating them as separate channels.
- **Min-max domain scaling.** Scales order sizes to the 0-1 range using the minimum and maximum order quantity observed on that side (ask or bid) of the current snapshot, then rescales to 0-255 so LOB frames resemble image pixel values.
- **Delta vs. relative-return target.** The model predicts either the absolute mid-price change (delta) or the relative percentage price growth over the forecast horizon; delta performs better at short horizons and relative return performs better at longer horizons.

## Method

Four CNN-based architectures are compared: a simple CNN, a deeper CNN with more convolutional blocks for merged 2D LOB images, and a CNN2LSTM model that embeds each stacked LOB snapshot via CNN layers before feeding the resulting sequence to an LSTM. Models are trained to predict either the mid-price delta or relative return at horizons from 0.2 to 60 seconds ahead, using historical windows defined either by a fixed number of consecutive snapshots (sliding window) or by a fixed real-time interval. Forecast quality is measured with mean absolute percentage error (MAPE); the resulting mid-price forecasts then drive a simulated automated market-making strategy that posts simultaneous buy and sell limit orders around the predicted mid-price, evaluated with Sharpe ratio, profit and loss, and maximum drawdown, under the simplifying assumption that minimum-size orders always execute.

## Results

- The lowest error (MAPE 0.001511%) was achieved by the CNN2LSTM model on a 30-snapshot sliding window predicting price delta.
- Averaged across horizons, CNN2LSTM with stacked LOB images had the best mean forecasting performance (MAPE 0.018244%), ahead of SimpleCNN (0.103163%) and the merged-image CNN models.
- Stacked LOB image embeddings outperformed merged embeddings on average (0.060703% vs. 0.361174% MAPE).
- Forecast error grows about 10 times as the prediction horizon extends from 0.2s to 60s.
- Predicting mid-price delta worked better for short horizons, while predicting relative return worked better for longer horizons.
- Only BTC and ETH had a volume-change correlation above 0.7 among the assets studied; a single model trained on both assets ('one-shot') reduced MAPE to roughly a quarter of the single-asset model's error at the 0.2s and 1s horizons.
- In the market-making simulation, the CNN2LSTM-based strategy showed a positive PnL growth rate for both BTC (Sharpe ratio 7.89) and ETH (Sharpe ratio 4.48), while a merged-image CNN model with a delta-regression task performed poorly and tended to hold a long position.

## Limitations

- The authors state their trading simulation assumes minimum-size orders always execute, ignoring order-queue position and the possibility of non-execution.
- The authors note no hyperparameter tuning was performed for the 8-feature model variant, so they cannot conclude whether the added features are actually beneficial.
- Reader note: the trading simulation covers only a single test day per asset (November 28, 2024) and does not model transaction costs beyond the assumed maker/taker fee structure.
- Reader note: training uses only 5,000 samples per interval, drawn from a single day (November 27, 2024), a short window for a deep-learning model.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/market-making|market making]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]

## Citation

Kasymkhan Khubiyev, Mikhail Semenov (2025). Deep Learning Models Meet Financial Data Modalities. Preprint for the MathAI: Mathematics of Artificial Intelligence conference.

DOI: 10.1007/s10958-025-08149-6

Text ingested: `markdown_output/khubiev-2025-deep-learning-models-meet-financial-data.md`, converted from `raw/ofi-event-clock/khubiev-2025-deep-learning-models-meet-financial-data.pdf`.

Coverage of this summary: Read the whole paper: introduction and related work, data description, sampling/embedding methodology, model architectures, trading-strategy design, evaluation metrics, all results tables, and the conclusion.

Known problems with the input: Several equations, the model-architecture diagram, and the aggregation-interval/horizon lists are rendered as picture placeholders in the markdown, so their exact mathematical form could not be verified beyond the surrounding prose and the table headers that restate the same values.
<!-- AUTHORED REGION END -->