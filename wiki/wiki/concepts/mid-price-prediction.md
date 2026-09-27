---
content_hash: sha256:401e1420d9423e56e803ff83bbf9ba268fef0594b543726483bf28823f1094b6
created: 2026-09-27 01:47:00+00:00
mind_map_priority: high
page_id: concepts/mid-price-prediction
page_type: concept
related:
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/event-clock
- concepts/order-flow-imbalance
- concepts/queue-imbalance
- concepts/feature-engineering
- concepts/lstm-networks
- concepts/transformers
- concepts/overfitting-backtesting
revision_id: 1
schema_version: 2
sources:
- sources/bileki-2021-uma-abordagem-com-modelo-de-aprendizado
- sources/bilokon-2023-transformers-versus-lstms-electronic-trading
- sources/khubiev-2025-deep-learning-models-meet-financial-data
- sources/kisiel-2022-axial-lob-high-frequency-trading-axial
- sources/kuhrn-2014-calculating-probability-mid-price-increase-based
- sources/lee-2024-price-predictability-limit-order-book-deep
- sources/nousi-2019-machine-learning-forecasting-mid-price-movements
- sources/ntakaris-2018-benchmark-dataset-midprice-forecasting-limit-order
- sources/ntakaris-2020-mid-price-prediction-based-machine-learning
- sources/shabani-2020-low-rank-temporal-attention-augmented-bilinear
- sources/tran-2021-how-informative-order-book-beyond-bestlevels
- sources/tsantekidis-2017-deep-learning-detect-price-change-indications
- sources/tsantekidis-2020-deep-learning-price-prediction-exploiting-stationary
- sources/wang-2025-exploring-microstructural-dynamics-cryptocurrency-limit-order
tags:
- mid-price-prediction
- limit-order-book
- deep-learning
- price-prediction
- event-clock
title: Mid-Price Prediction
updated: '2026-09-27T01:47:00Z'
uuid: fdda6bc3-9753-5bcf-b7df-cb7b8756ea12
---

<!-- AUTHORED REGION START -->
# Mid-Price Prediction

Mid-price prediction is the task of forecasting the direction of the mid-price from the recent state of the limit order book. It is the standard test problem for machine learning on order book data.

## How the task is set up

- **Inputs.** A window of recent book snapshots: prices and sizes at several levels on each side. Hand-built features such as [[concepts/queue-imbalance|queue imbalance]] or [[concepts/order-flow-imbalance|order flow imbalance]] are sometimes added or used in place of the raw book.
- **Target.** A label of up, down or unchanged. It is set by comparing the mid-price now with the mid-price some way ahead, and applying a threshold.
- **Horizon.** Usually a fixed number of future book events, which makes this an [[concepts/event-clock|event clock]] problem.

## Why it matters here

This literature is the largest body of work that builds order book features on an event clock. The models differ, but the sampling, the labelling and the benchmark data are shared.

## What to look for in a paper

- How the horizon is defined, and whether it is in events or in time.
- How the label threshold is chosen, since it controls how many observations fall in each class.
- Whether the test period follows the training period in time.
- Whether trading costs are included.

## Caveats

High classification accuracy does not imply a profitable strategy. Predicted moves are often smaller than the spread. Several sources in this wiki report that models which do well on the standard benchmark do much worse on other data. The risk of [[concepts/overfitting-backtesting|overfitting]] is high, because many models are tuned on the same small dataset.

## Sources in This Wiki

- [[sources/bileki-2021-uma-abordagem-com-modelo-de-aprendizado|Uma abordagem com modelo de aprendizado de máquina híbrido para predição de movimentos de preço médio de ativos pelo livro de ofertas]] (Guilherme Augusto Bileki, 2021). Master's thesis testing whether a CNN order-book feature extractor combined with a CatBoost classifier, plus B3's broker-identity message data, improves short-horizon Brazilian mid-price direction prediction.
- [[sources/bilokon-2023-transformers-versus-lstms-electronic-trading|Transformers versus LSTMs for Electronic Trading]] (Paul Bilokon, Yitao Qiu, 2023). Compares LSTM- and Transformer-based models on high-frequency limit order book prediction tasks and introduces DLSTM, a decomposition-based LSTM that wins on price-movement classification and simulated trading profitability.
- [[sources/khubiev-2025-deep-learning-models-meet-financial-data|Deep Learning Models Meet Financial Data Modalities]] (Kasymkhan Khubiyev, Mikhail Semenov, 2025). Proposes image-based embeddings of limit order book snapshots (stacked vs. merged) and CNN/CNN-LSTM models to forecast cryptocurrency perpetual futures mid-price and drive a market-making strategy.
- [[sources/kisiel-2022-axial-lob-high-frequency-trading-axial|Axial-LOB: High-Frequency Trading with Axial Attention]] (Damian Kisiel, Denise Gorse, 2022). Introduces Axial-LOB, an attention-only deep learning model that predicts limit-order-book mid-price direction, beating CNN/LSTM baselines on the FI-2010 benchmark with far fewer parameters.
- [[sources/kuhrn-2014-calculating-probability-mid-price-increase-based|Calculating the probability of a mid-price increase based on a stochastic model for order book dynamics]] (Sabrina Kuhrn, 2014). A diploma thesis tests whether a birth-and-death Markov chain model of the limit order book, in the style of Cont-Stoikov-Talreja, predicts the probability of a mid-price increase on Istanbul Stock Exchange data.
- [[sources/lee-2024-price-predictability-limit-order-book-deep|Price predictability in limit order book with deep learning model]] (Kyungsub Lee, 2024). Trains a DeepLOB-style neural network on 2022 AAPL order-book data and shows most of its apparent price-direction accuracy stems from volume imbalance rather than the price process itself.
- [[sources/nousi-2019-machine-learning-forecasting-mid-price-movements|Machine Learning for Forecasting Mid Price Movement using Limit Order Book Data]] (Paraskevi Nousi, Avraam Tsantekidis, Nikolaos Passalis and others, 2019). Builds and compares handcrafted and machine-learned (autoencoder, Bag-of-Features) limit order book features, tested with SVM, SLFN and MLP classifiers to forecast the direction of stock mid-price moves at three horizons.
- [[sources/ntakaris-2018-benchmark-dataset-midprice-forecasting-limit-order|Benchmark Dataset for Mid-Price Forecasting of Limit Order Book Data with Machine Learning Methods]] (Adamantios Ntakaris, Martin Magris, Juho Kanniainen and others, 2018). Releases the first public NASDAQ Nordic limit order book benchmark dataset for mid-price movement forecasting, with an anchored cross-validation protocol and baselines.
- [[sources/ntakaris-2020-mid-price-prediction-based-machine-learning|Mid-price Prediction Based on Machine Learning Methods with Technical and Quantitative Indicators]] (Adamantios Ntakaris, Juho Kanniainen, Moncef Gabbouj and others, 2020). Compares over 270 hand-crafted technical, quantitative and order-book features, using wrapper feature-selection methods to find which small subset best predicts short-horizon mid-price direction on Nasdaq Nordic limit order book data.
- [[sources/shabani-2020-low-rank-temporal-attention-augmented-bilinear|Low-Rank Temporal Attention-Augmented Bilinear Network for financial time-series forecasting]] (Mostafa Shabani, Alexandros, 2020). Proposes a low-rank tensor approximation of the TABL layer for limit order book mid-price direction forecasting, matching TABL's accuracy with far fewer parameters.
- [[sources/tran-2021-how-informative-order-book-beyond-bestlevels|How informative is the Order Book Beyond the Best Levels? Machine Learning Perspective]] (Dat Thanh Tran, Juho Kanniainen, 2021). Tests whether limit order book data beyond the best bid/ask levels improves nonlinear machine-learning predictions of mid-price movements, using feature selection on DeepLOB and TABL across US and Nordic stocks.
- [[sources/tsantekidis-2017-deep-learning-detect-price-change-indications|Using Deep Learning to Detect Price Change Indications in Financial Markets]] (Avraam Tsantekidis, Nikolaos Passalis, Anastasios Tefas and others, 2017). Trains an LSTM on high-frequency limit order book depth data to predict short-term mid-price direction, outperforming SVM and MLP baselines across three horizons.
- [[sources/tsantekidis-2020-deep-learning-price-prediction-exploiting-stationary|Using Deep Learning for price prediction by exploiting stationary limit order book features]] (Avraam Tsantekidis, Nikolaos Passalis, Anastasios Tefas and others, 2020). Proposes stationary limit order book features (price-level differences from mid-price, mid-price returns, cumulative depth) that let deep learning models predict mid-price direction more accurately than raw LOB inputs.
- [[sources/wang-2025-exploring-microstructural-dynamics-cryptocurrency-limit-order|Exploring Microstructural Dynamics in Cryptocurrency Limit Order Books: Better Inputs Matter More Than Stacking Another Hidden Layer]] (Haochuan (Kevin) Wang, 2025). Benchmarks logistic regression, XGBoost, CatBoost, and CNN/LSTM/DeepLOB networks on Bybit BTC/USDT limit order book snapshots to test whether denoising, not model depth, drives short-horizon price forecasting accuracy.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/event-clock|Event Clock]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/queue-imbalance|Queue Imbalance]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/transformers|transformers]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
<!-- AUTHORED REGION END -->