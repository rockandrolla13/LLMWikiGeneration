---
content_hash: sha256:91176fc36e55d5e881f8c35a1a00bde5cb1355aeabda199d2ab9a3befe146900
created: 2026-09-27 01:47:00+00:00
mind_map_priority: high
page_id: concepts/event-clock
page_type: concept
related:
- concepts/sampling-clocks
- concepts/trade-clock
- concepts/volume-clock
- concepts/intrinsic-time
- concepts/limit-order-book
- concepts/order-flow-imbalance
- concepts/mid-price-prediction
- concepts/hawkes-processes
revision_id: 1
schema_version: 2
sources:
- sources/angstmann-2026-non-unique-time-market-incompleteness
- sources/bileki-2021-uma-abordagem-com-modelo-de-aprendizado
- sources/briola-2020-deep-learning-modeling-limit-order-book
- sources/briola-2021-deep-reinforcement-learning-active-high-frequency
- sources/briola-2024-hlobinformation-persistence-structure-limit-order-books
- sources/briola-2025-deep-limit-order-book-forecasting-microstructural
- sources/cestari-2023-hawkes-based-cryptocurrency-forecasting-limit-order
- sources/cestari-2025-univariate-hawkes-based-cryptocurrency-forecasting-limit
- sources/chomei-2023-empirical-analysis-limit-order-book-modeling
- sources/dixon-2017-sequence-classification-limit-order-book-recurrent
- sources/dixon-2018-deep-learning-spatiotemporal-modeling-dynamic-traffic
- sources/eisler-2011-price-impact-order-book-events-market
- sources/eisler-2012-models-impact-all-order-book-events
- sources/fabre-2025-learning-spoofability-limit-order-books-interpretable
- sources/gontis-2023-discrete-q-exponential-limit-order-cancellation
- sources/gould-2016-queue-imbalance-one-tick-ahead-price
- sources/gu-2007-empirical-distributions-chinese-stock-returns-different
- sources/hirnschall-2020-deep-learning-approach-analyzing-limit-order
- sources/jaddu-2023-combining-deep-learning-order-books-reinforcement
- sources/jong-2026-order-book-dynamics-two-dimensional-exit
- sources/kamm-2026-quantum-weighted-moving-average-predicting-limit
- sources/khadira-2026-path-signatures-universal-feature-extractors-limit
- sources/kijima-2016-svm-enhanced-filtering-model-limit-order
- sources/kisiel-2022-axial-lob-high-frequency-trading-axial
- sources/kolm-2023-deep-order-flow-imbalance-extracting-alpha
- sources/kuhrn-2014-calculating-probability-mid-price-increase-based
- sources/lee-2024-price-predictability-limit-order-book-deep
- sources/li-2026-systematic-hyperparameter-analysis-deep-learning-models
- sources/linna-2025-lobert-generative-ai-foundation-model-limit
- sources/linna-2026-repurposing-deep-limit-order-book-forecasting
- sources/lipton-2013-trade-arrival-dynamics-quote-imbalance-limit
- sources/lucchese-2024-short-term-predictability-returns-order-book
- sources/magris-2023-bayesian-bilinear-neural-network-predicting-midprice
- sources/makinde-2026-temporal-kolmogorov-arnold-networks-t-kan
- sources/miranda-2019-order-flow-dynamics-prediction-order-cancelation
- sources/nortier-2016-second-order-proximal-methods-applied-elastic
- sources/nousi-2019-machine-learning-forecasting-mid-price-movements
- sources/ntakaris-2018-benchmark-dataset-midprice-forecasting-limit-order
- sources/ntakaris-2019-feature-engineering-mid-price-prediction-deep
- sources/ntakaris-2020-mid-price-prediction-based-machine-learning
- sources/ntakaris-2023-optimum-output-long-short-term-memory
- sources/ntakaris-2024-minimal-batch-adaptive-learning-policy-engine
- sources/ntakaris-2024-online-high-frequency-trading-stock-forecasting
- sources/passalis-2019-deep-adaptive-input-normalization-price-forecasting
- sources/passalis-2020-temporal-logistic-neural-bag-features-financial
- sources/prata-2024-lob-based-deep-learning-models-stock
- sources/qureshi-2018-investigating-limit-order-book-characteristics-short
- sources/raffaelli-2026-forecasting-bitcoin-price-movements-multivariate-hawkes
- sources/sfendourakis-2020-lob-modeling-hawkes-processes-state-dependent
- sources/shabani-2020-low-rank-temporal-attention-augmented-bilinear
- sources/shabani-2022-multi-head-temporal-attention-augmented-bilinear
- sources/shi-2021-lob-recreation-model-predicting-limit-order
- sources/stoikov-2016-reducing-transaction-costs-low-latency-trading
- sources/tran-2018-temporal-attention-augmented-bilinear-network-financial
- sources/tran-2019-data-driven-neural-architecture-learning-financial
- sources/tran-2021-data-normalization-bilinear-structures-high-frequency
- sources/tran-2021-how-informative-order-book-beyond-bestlevels
- sources/tsantekidis-2017-deep-learning-detect-price-change-indications
- sources/tsantekidis-2020-deep-learning-price-prediction-exploiting-stationary
- sources/vlasiuk-2025-push-response-anomalies-high-frequency-s
- sources/wilinski-2026-classifying-clustering-trading-agents
- sources/wu-2021-how-robust-limit-order-book-representations
- sources/wu-2022-towards-robust-representations-limit-orders-books
- sources/xiao-2025-lit-limit-order-book-transformer
- sources/xu-2026-when-quotes-crumble-detecting-transient-mechanical
- sources/young-2026-openmarket-synchronized-polymarket-binance-dataset-high
- sources/zainal-2021-optimal-limit-order-book-prediction-analysis
- sources/zaznov-2024-intraday-dynamics-predictor-trioflow-fusion-convolutional
- sources/zhang-2019-deeplob-deep-convolutional-neural-networks-limit
- sources/zhang-2021-multi-horizon-forecasting-limit-order-books
- sources/zheng-2013-price-jump-prediction-limit-order-book
tags:
- event-time
- limit-order-book
- sampling
- market-microstructure
- high-frequency-data
title: Event Clock
updated: '2026-09-27T01:47:00Z'
uuid: b08789df-9cf3-5fef-9594-50f55817f716
---

<!-- AUTHORED REGION START -->
# Event Clock

An event clock advances by one each time something happens in the order book: a new limit order, a cancellation, or a trade. Time between events is ignored. It is the finest of the [[concepts/sampling-clocks|sampling clocks]], because every change to the book is an observation.

## How it is used

- **As the index of the data.** Order book records are kept one row per update, and features are computed over a fixed number of rows.
- **As the forecast horizon.** The target is the price change after a fixed number of future events. This keeps the horizon comparable across assets that trade at very different speeds.
- **As the unit of a model.** Point-process models of the book, such as [[concepts/hawkes-processes|Hawkes processes]], describe the arrival of each event type directly.

## Relation to order flow imbalance

[[concepts/order-flow-imbalance|Order flow imbalance]] is built from individual book events, so it is an event-level quantity by construction. Most papers then sum it over wall-clock intervals. Summing it over a fixed number of events instead is the event-clock version of the same measure.

## Caveats

Quote updates far outnumber trades, so an event clock is dominated by limit order activity. A fixed number of events can span a fraction of a second in a liquid asset and much longer in a quiet one. Results stated in events therefore need the typical event rate alongside them before they can be read as a trading horizon.

## Sources in This Wiki

- [[sources/angstmann-2026-non-unique-time-market-incompleteness|Non-unique time and market incompleteness]] (Chris Angstmann, Tim Gebbie, 2026). Argues that financial markets' event-driven, asynchronous nature means the map from discrete event time to a continuous calendar-time price process is not unique, implying deeper market incompleteness.
- [[sources/bileki-2021-uma-abordagem-com-modelo-de-aprendizado|Uma abordagem com modelo de aprendizado de máquina híbrido para predição de movimentos de preço médio de ativos pelo livro de ofertas]] (Guilherme Augusto Bileki, 2021). Master's thesis testing whether a CNN order-book feature extractor combined with a CatBoost classifier, plus B3's broker-identity message data, improves short-horizon Brazilian mid-price direction prediction.
- [[sources/briola-2020-deep-learning-modeling-limit-order-book|Deep Learning Modelling of the Limit Order Book: A Comparative Perspective]] (Antonio Briola, Jeremy Turiel, Tomaso Aste, 2020). Compares Random, Logistic Regression, MLP, Shallow LSTM, Self-Attention LSTM and CNN-LSTM models for limit order book return classification, finding the MLP matches state-of-the-art CNN-LSTM performance.
- [[sources/briola-2021-deep-reinforcement-learning-active-high-frequency|Deep Reinforcement Learning for Active High Frequency Trading]] (Antonio Briola, Jeremy Turiel, Riccardo Marcaccioli and others, 2021). Trains a Proximal Policy Optimization deep reinforcement learning agent to actively trade single units of Intel Corporation stock directly from limit order book data.
- [[sources/briola-2024-hlobinformation-persistence-structure-limit-order-books|HLOB – Information Persistence and Structure in Limit Order Books]] (Antonio Briola, Silvia Bartolucci, Tomaso Aste, 2024). Introduces HLOB, a deep learning architecture that uses an information filtering network (TMFG) over LOB volume levels to forecast mid-price change direction on NASDAQ stocks.
- [[sources/briola-2025-deep-limit-order-book-forecasting-microstructural|Deep Limit Order Book Forecasting: A microstructural guide]] (Antonio Briola, Silvia Bartolucci, Tomaso Aste, 2025). Links 15 NASDAQ stocks' tick-size-driven microstructural properties to how well a deep learning model (DeepLOB) forecasts mid-price direction, and whether those forecasts are actually tradeable.
- [[sources/cestari-2023-hawkes-based-cryptocurrency-forecasting-limit-order|Hawkes-based cryptocurrency forecasting via Limit Order Book data]] (Raffaele Giuseppe Cestari, Filippo Barchi, Riccardo Busetto and others, 2023). Combines a Hawkes point-process model of limit order book event timing with a continuous-output-error model of the base-imbalance regressor to forecast cryptocurrency return signs and drive a trading strategy.
- [[sources/cestari-2025-univariate-hawkes-based-cryptocurrency-forecasting-limit|Univariate Hawkes-based cryptocurrency forecasting via Limit Order Book data]] (Raffaele G. Cestari, Filippo Barchi, Riccardo Busetto and others, 2025). Predicts the timing of the next limit order book event with a univariate Hawkes process, then feeds that predicted timing into a continuous output error model to forecast cryptocurrency return sign and improve trading profit.
- [[sources/chomei-2023-empirical-analysis-limit-order-book-modeling|Empirical analysis in limit order book modeling for Nikkei 225 Stocks with Cox-type intensities]] (Shunya Chomei, 2023). Extends Muni Toke and Yoshida's Cox-type intensity ratio model with new order-book imbalance covariates to predict the sign of the next market order for 222 Tokyo Stock Exchange stocks.
- [[sources/dixon-2017-sequence-classification-limit-order-book-recurrent|Sequence Classification of the Limit Order Book using Recurrent Neural Networks]] (Matthew Dixon, 2017). Uses a recurrent neural network to predict the next limit-order-book price-flip from book depths and order flow, benchmarked against a Kalman filter and logistic regression on E-mini S&P 500 futures.
- [[sources/dixon-2018-deep-learning-spatiotemporal-modeling-dynamic-traffic|Deep Learning for Spatio-Temporal Modeling: Dynamic Traffic Flows and High Frequency Trading]] (Matthew F. Dixon, Nicholas G. Polson, Vadim O. Sokolov, 2018). Applies deep feed-forward and recurrent networks to two spatio-temporal prediction problems: highway traffic-flow speeds and next-tick E-mini S&P 500 futures mid-price direction from order-book depth.
- [[sources/eisler-2011-price-impact-order-book-events-market|The price impact of order book events: market orders, limit orders and cancellations]] (Zoltan Eisler, Jean-Philippe Bouchaud, Julien Kockelkoren, 2018). Empirically decomposes the price impact of market orders, limit orders and cancellations into bare per-event propagators, and models the history dependence of quote gaps for small-tick stocks via linear regression on past order flow.
- [[sources/eisler-2012-models-impact-all-order-book-events|Models for the impact of all order book events]] (Zoltán Eisler, Jean-Philippe Bouchaud, Julien Kockelkoren, 2018). Proposes and compares two frameworks, transient impact (TIM) and history-dependent impact (HDIM), for modeling how six types of order book events move prices, testing them against high-frequency stock data.
- [[sources/fabre-2025-learning-spoofability-limit-order-books-interpretable|Learning the Spoofability of Limit Order Books With Interpretable Probabilistic Neural Networks]] (Timothée Fabre, Damien Challet, 2025). Builds Hawkes-inspired order flow features and a probabilistic neural network for the mid-price-move distribution, then uses it to detect spoofing in cryptocurrency limit order books.
- [[sources/gontis-2023-discrete-q-exponential-limit-order-cancellation|Discrete q-Exponential Limit Order Cancellation Time Distribution]] (Vygintas Gontis, 2023). Shows limit-order cancellation times on ten NASDAQ stocks follow a discrete Tsallis q-exponential distribution and uses it to build an order-disbalance time-series model.
- [[sources/gould-2016-queue-imbalance-one-tick-ahead-price|Queue Imbalance as a One-Tick-Ahead Price Predictor in a Limit Order Book]] (Martin D. Gould, Julius Bonart, 2015). Tests whether best-bid/ask queue imbalance predicts the direction of the very next mid-price move for 10 Nasdaq stocks, using logistic and local logistic regression.
- [[sources/gu-2007-empirical-distributions-chinese-stock-returns-different|Empirical distributions of Chinese stock returns at different microscopic timescales]] (Gao-Feng Gu, Wei Chen, Wei-Xing Zhou, 2018). Studies the distribution of intraday returns for 23 Chinese stocks at several trade-count and minute-based sampling scales, finding an inverse cubic tail law at the single-trade scale that thins out as the scale grows.
- [[sources/hirnschall-2020-deep-learning-approach-analyzing-limit-order|A Deep Learning Approach for Analyzing the Limit Order Book]] (David Hirnschall, 2020). A TU Wien diploma thesis that trains deep feedforward neural networks on handcrafted limit order book features to classify midprice direction and forecast realized volatility for four NASDAQ stocks.
- [[sources/jaddu-2023-combining-deep-learning-order-books-reinforcement|Combining Deep Learning on Order Books with Reinforcement Learning for Profitable Trading]] (Koti S. Jaddu, Paul A. Bilokon, 2023). Combines a supervised deep-learning alpha-extraction model using order flow imbalance with three temporal-difference reinforcement-learning agents to trade five retail instruments, tested via backtesting and short forward tests.
- [[sources/jong-2026-order-book-dynamics-two-dimensional-exit|Order Book Dynamics - Two-Dimensional Exit Problems on a Cryptocurrency Exchange]] (J.M. de Jong, 2020). Fits drift-diffusion and diffusion-only exit-problem models to Level-1 BitMEX Bitcoin-USD order book data to predict price direction and tests a resulting trading strategy.
- [[sources/kamm-2026-quantum-weighted-moving-average-predicting-limit|Quantum Weighted Moving Average for Predicting Limit Order Book Trends]] (Matthias Kamm, Dinh-Long Vu, Patrick Rebentrost, 2026). Introduces a quantum model (QWMA) that embeds LOB time steps as unitaries combined via a linear combination of unitaries to predict FI-2010 price-trend labels, benchmarked against classical MLP and BiNTABL models.
- [[sources/khadira-2026-path-signatures-universal-feature-extractors-limit|Path Signatures as Universal Feature Extractors for Limit Order Book Mid-Price Prediction]] (Mamoune Khadira, 2026). Applies the path signature transform, truncated at order 4, to bid/ask price and volume paths from limit order book data, showing it outperforms hand-crafted and deep-learning features for short-horizon mid-price direction prediction.
- [[sources/kijima-2016-svm-enhanced-filtering-model-limit-order|SVM-Enhanced Filtering Model for Limit Order Book Dynamics]] (Hayato Kijima, Hideyuki Takada, Takayuki Tomiya, 2015). Extends a Cont-style order book queueing model with unobservable buy/sell pressure factors, and steers those latent factors with an SVM that reads the current book shape to predict mid-price direction.
- [[sources/kisiel-2022-axial-lob-high-frequency-trading-axial|Axial-LOB: High-Frequency Trading with Axial Attention]] (Damian Kisiel, Denise Gorse, 2022). Introduces Axial-LOB, an attention-only deep learning model that predicts limit-order-book mid-price direction, beating CNN/LSTM baselines on the FI-2010 benchmark with far fewer parameters.
- [[sources/kolm-2023-deep-order-flow-imbalance-extracting-alpha|Deep order flow imbalance: Extracting alpha at multiple horizons from the limit order book]] (Petter N. Kolm, Jeremy Turiel, Nicholas Westray, 2023). Trains LSTM-based networks on order-flow features from 115 Nasdaq stocks to forecast returns at 10 horizons; order-flow beats raw order-book inputs, with predictability peaking near two average price changes.
- [[sources/kuhrn-2014-calculating-probability-mid-price-increase-based|Calculating the probability of a mid-price increase based on a stochastic model for order book dynamics]] (Sabrina Kuhrn, 2014). A diploma thesis tests whether a birth-and-death Markov chain model of the limit order book, in the style of Cont-Stoikov-Talreja, predicts the probability of a mid-price increase on Istanbul Stock Exchange data.
- [[sources/lee-2024-price-predictability-limit-order-book-deep|Price predictability in limit order book with deep learning model]] (Kyungsub Lee, 2024). Trains a DeepLOB-style neural network on 2022 AAPL order-book data and shows most of its apparent price-direction accuracy stems from volume imbalance rather than the price process itself.
- [[sources/li-2026-systematic-hyperparameter-analysis-deep-learning-models|A Systematic Hyperparameter Analysis of Deep Learning Models for Limit Order Book Mid-price Prediction]] (Hongyi Li, 2026). Benchmarks eleven neural-network architectures on the FI-2010 order-book dataset, finds BiNTABL best, then runs ablations showing bilinear layers, learning rate and forecast horizon matter most.
- [[sources/linna-2025-lobert-generative-ai-foundation-model-limit|LOBERT: Generative AI Foundation Model for Limit Order Book Messages]] (Eljas Linna, Kestutis Baltakys, Alexandros Iosifidis and others, 2025). Introduces LOBERT, a BERT-style encoder-only foundation model that tokenizes whole limit order book messages, pretrains via masked reconstruction, and fine-tunes for next-message and mid-price prediction.
- [[sources/linna-2026-repurposing-deep-limit-order-book-forecasting|Repurposing Deep Limit Order Book Forecasting for Scenario-Conditioned Market Impact Modeling]] (Eljas Linna, Kestutis Baltakys, Derrick Manoharan and others, 2027). Repurposes a pretrained Transformer LOB forecaster, without retraining, to estimate short-horizon market impact of counterfactual order-book messages, validated against simulation and real events.
- [[sources/lipton-2013-trade-arrival-dynamics-quote-imbalance-limit|Trade arrival dynamics and quote imbalance in a limit order book]] (Alexander Lipton, Umberto Pesavento, Michael G Sotiropoulos, 2013). Models how the imbalance between the bid and ask queues at the top of a limit order book jointly drives price moves and trade-arrival timing, calibrated to VOD.L quote and trade data.
- [[sources/lucchese-2024-short-term-predictability-returns-order-book|The Short-Term Predictability of Returns in Order Book Markets: A Deep Learning Perspective]] (Lorenzo Lucchese, Mikko S. Pakkanen, Almut E. D. Veraart, 2023). Tests, using deep learning models and model confidence sets on ten Nasdaq stocks, how far ahead order-book information predicts mid-price returns and which order-book representation works best.
- [[sources/magris-2023-bayesian-bilinear-neural-network-predicting-midprice|Bayesian Bilinear Neural Network for Predicting the Mid-price Dynamics in Limit-Order Book Markets]] (Martin Magris, Mostafa Shabani, Alexandros Iosifidis, 2023). Trains a Bayesian version of the Temporal Attention-augmented Bilinear network to classify mid-price direction in limit order book data and shows Bayesian training gives usable predictive uncertainty.
- [[sources/makinde-2026-temporal-kolmogorov-arnold-networks-t-kan|Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha-Decay]] (Ahmad Makinde, 2026). T-KAN replaces an LSTM's fixed weights with learnable B-spline activations to forecast limit order book price direction, cutting alpha decay and improving profitability versus a DeepLOB baseline.
- [[sources/miranda-2019-order-flow-dynamics-prediction-order-cancelation|Order flow dynamics for prediction of order cancelation and applications to detect market manipulation]] (Enrique Martínez Miranda, Steve Phelps, Matthew J. Howard, 2019). An SVM classifier uses reconstructed limit order book states in event time to detect and predict the cancelation of large orders, as a step toward identifying spoofing-style manipulation.
- [[sources/nortier-2016-second-order-proximal-methods-applied-elastic|Second Order Proximal Methods Applied to Elastic Net Penalised Vector Generalised Linear Models]] (Bertrand Nortier, 2016). Develops a proximal Fisher scoring algorithm for elastic-net penalised vector generalised linear models and applies it to predicting limit order book mid-price changes and a health-care count model.
- [[sources/nousi-2019-machine-learning-forecasting-mid-price-movements|Machine Learning for Forecasting Mid Price Movement using Limit Order Book Data]] (Paraskevi Nousi, Avraam Tsantekidis, Nikolaos Passalis and others, 2019). Builds and compares handcrafted and machine-learned (autoencoder, Bag-of-Features) limit order book features, tested with SVM, SLFN and MLP classifiers to forecast the direction of stock mid-price moves at three horizons.
- [[sources/ntakaris-2018-benchmark-dataset-midprice-forecasting-limit-order|Benchmark Dataset for Mid-Price Forecasting of Limit Order Book Data with Machine Learning Methods]] (Adamantios Ntakaris, Martin Magris, Juho Kanniainen and others, 2018). Releases the first public NASDAQ Nordic limit order book benchmark dataset for mid-price movement forecasting, with an anchored cross-validation protocol and baselines.
- [[sources/ntakaris-2019-feature-engineering-mid-price-prediction-deep|Feature Engineering for Mid-Price Prediction with Deep Learning]] (Adamantios Ntakaris, Giorgio Mirone, Juho Kanniainen and others, 2019). Proposes an extensive econometric handcrafted feature set for limit order book mid-price prediction and compares it to other handcrafted and autoencoder-derived features across nine deep learning models.
- [[sources/ntakaris-2020-mid-price-prediction-based-machine-learning|Mid-price Prediction Based on Machine Learning Methods with Technical and Quantitative Indicators]] (Adamantios Ntakaris, Juho Kanniainen, Moncef Gabbouj and others, 2020). Compares over 270 hand-crafted technical, quantitative and order-book features, using wrapper feature-selection methods to find which small subset best predicts short-horizon mid-price direction on Nasdaq Nordic limit order book data.
- [[sources/ntakaris-2023-optimum-output-long-short-term-memory|Optimum Output Long Short-Term Memory Cell for High-Frequency Trading Forecasting]] (Adamantios Ntakaris, Moncef Gabbouj, Juho Kanniainen, 2023). Introduces the Optimum Output LSTM (OPTM-LSTM) cell, which online-selects its best internal gate or state as output, for tick-by-tick limit order book mid-price forecasting in high-frequency trading.
- [[sources/ntakaris-2024-minimal-batch-adaptive-learning-policy-engine|Minimal Batch Adaptive Learning Policy Engine for Real-Time Mid-Price Forecasting in High-Frequency Trading]] (Adamantios Ntakaris, Gbenga Ibikunle, 2024). Introduces ALPE, a lightweight reinforcement-learning agent that forecasts LOB mid-price event-by-event without batch training, beating ARIMA, MLP, CNN, LSTM, GRU and RBFNN on 100 NASDAQ stocks.
- [[sources/ntakaris-2024-online-high-frequency-trading-stock-forecasting|Online High-Frequency Trading Stock Forecasting with Automated Feature Clustering and Radial Basis Function Neural Networks]] (Adamantios Ntakaris, Gbenga Ibikunle, 2023). An online, fully autonomous pipeline that lets gradient descent and mean-decrease impurity compete as feature-importance methods, auto-selects a cluster count, and feeds a radial basis function network to forecast limit order book mid-price tick by tick.
- [[sources/passalis-2019-deep-adaptive-input-normalization-price-forecasting|Deep Adaptive Input Normalization for Time Series Forecasting]] (Nikolaos Passalis, Anastasios Tefas, Juho Kanniainen and others, 2019). Proposes a trainable neural layer (DAIN) that learns to shift, scale and gate its input, replacing fixed normalization schemes for non-stationary financial time series.
- [[sources/passalis-2020-temporal-logistic-neural-bag-features-financial|Temporal Logistic Neural Bag-of-Features for Financial Time series Forecasting leveraging Limit Order Book Data]] (Nikolaos Passalis, Anastasios Tefas, Juho Kanniainen and others, 2020). Proposes a logistic Neural Bag-of-Features layer with adaptive scaling, combined with deep feature extractors, to forecast limit-order-book mid-price direction.
- [[sources/prata-2024-lob-based-deep-learning-models-stock|LOB-Based Deep Learning Models for Stock Price Trend Prediction: A Benchmark Study]] (Matteo Prata, Giuseppe Masi, Leonardo Berti and others, 2024). Benchmarks 15 deep-learning limit-order-book models for predicting ternary stock price trends, testing whether their published results reproduce and generalize to unseen market data.
- [[sources/qureshi-2018-investigating-limit-order-book-characteristics-short|Investigating Limit Order Book Characteristics for Short Term Price Prediction: a Machine Learning Approach]] (Faisal Qureshi, 2018). Evaluates six classifiers, with class-imbalance fixes, for predicting the next-event direction of NASDAQ stock mid-quote prices from LOBSTER order-book and order-message features.
- [[sources/raffaelli-2026-forecasting-bitcoin-price-movements-multivariate-hawkes|Forecasting Bitcoin price movements using multivariate Hawkes processes and limit order book data]] (Davide Raffaelli, Raffaele Giuseppe Cestari, Daniele Marazzina and others, 2026). Compares two multivariate-Hawkes pipelines for forecasting BTC/USD mid-price return timing and sign from LOB events; the hybrid Hawkes-plus-continuous-time model beats the pure-Hawkes classifier on accuracy and profit.
- [[sources/sfendourakis-2020-lob-modeling-hawkes-processes-state-dependent|LOB Hawkes modeling using processes with a state-dependent factor]] (Emmanouil Sfendourakis, Ioane Muni Toke, 2021). Proposes a Hawkes process for limit order book flows whose intensity is multiplied by an exponential factor of observable state, such as imbalance and spread, fit by fast likelihood or EM methods.
- [[sources/shabani-2020-low-rank-temporal-attention-augmented-bilinear|Low-Rank Temporal Attention-Augmented Bilinear Network for financial time-series forecasting]] (Mostafa Shabani, Alexandros, 2020). Proposes a low-rank tensor approximation of the TABL layer for limit order book mid-price direction forecasting, matching TABL's accuracy with far fewer parameters.
- [[sources/shabani-2022-multi-head-temporal-attention-augmented-bilinear|MULTI-HEAD TEMPORAL ATTENTION-AUGMENTED BILINEAR NETWORK FOR FINANCIAL TIME SERIES PREDICTION]] (Mostafa Shabani, Dat Thanh Tran, Martin Magris and others, 2022). Extends the TABL bilinear neural layer with multiple parallel attention heads and tests it on limit-order-book mid-price direction forecasting.
- [[sources/shi-2021-lob-recreation-model-predicting-limit-order|The LOB Recreation Model: Predicting the Limit Order Book from TAQ History Using an Ordinary Differential Equation Recurrent Neural Network]] (Zijian Shi, Yu Chen, John Cartlidge, 2021). Reconstructs the top five limit order book price levels for small-tick stocks from only trade-and-quote data, using a GRU history compiler plus an ODE-RNN market-events simulator.
- [[sources/stoikov-2016-reducing-transaction-costs-low-latency-trading|Reducing transaction costs with low-latency trading algorithms]] (Sasha Stoikov, Rolf Waeber, 2015). Formulates optimal single-lot liquidation as an optimal-stopping problem using top-of-book order imbalance, showing low-latency execution saves close to a third of the bid-ask spread versus TWAP in Treasury bond backtests.
- [[sources/tran-2018-temporal-attention-augmented-bilinear-network-financial|Temporal Attention augmented Bilinear Network for Financial Time-Series Data Analysis]] (Dat Thanh Tran, Alexandros Iosifidis, Juho Kanniainen and others, 2018). Proposes a bilinear neural-network layer with a temporal attention mechanism that predicts limit-order-book mid-price movements more accurately, and far more cheaply, than deep RNN/CNN baselines.
- [[sources/tran-2019-data-driven-neural-architecture-learning-financial|Data-driven Neural Architecture Learning for Financial Time-series Forecasting]] (Dat Thanh Tran, Juho Kanniainen, Moncef Gabbouj and others, 2019). Proposes HeMLGOP, a progressively grown heterogeneous neural network of Generalized Operational Perceptrons with a class-reweighted loss, to predict LOB mid-price movement, beating progressive-learning and tensor-based baselines.
- [[sources/tran-2021-data-normalization-bilinear-structures-high-frequency|Data Normalization for Bilinear Structures in High-Frequency Financial Time-series]] (Dat Thanh Tran, Juho Kanniainen, Moncef Gabbouj and others, 2021). Introduces Bilinear Normalization (BiN), a lightweight learnable layer that normalizes limit order book input along both time and feature axes, improving TABL network accuracy for mid-price movement forecasting.
- [[sources/tran-2021-how-informative-order-book-beyond-bestlevels|How informative is the Order Book Beyond the Best Levels? Machine Learning Perspective]] (Dat Thanh Tran, Juho Kanniainen, 2021). Tests whether limit order book data beyond the best bid/ask levels improves nonlinear machine-learning predictions of mid-price movements, using feature selection on DeepLOB and TABL across US and Nordic stocks.
- [[sources/tsantekidis-2017-deep-learning-detect-price-change-indications|Using Deep Learning to Detect Price Change Indications in Financial Markets]] (Avraam Tsantekidis, Nikolaos Passalis, Anastasios Tefas and others, 2017). Trains an LSTM on high-frequency limit order book depth data to predict short-term mid-price direction, outperforming SVM and MLP baselines across three horizons.
- [[sources/tsantekidis-2020-deep-learning-price-prediction-exploiting-stationary|Using Deep Learning for price prediction by exploiting stationary limit order book features]] (Avraam Tsantekidis, Nikolaos Passalis, Anastasios Tefas and others, 2020). Proposes stationary limit order book features (price-level differences from mid-price, mid-price returns, cumulative depth) that let deep learning models predict mid-price direction more accurately than raw LOB inputs.
- [[sources/vlasiuk-2025-push-response-anomalies-high-frequency-s|Push-response anomalies in high-frequency S&P 500 price series]] (Dmitrii Vlasiuk, Mikhail Smirnov, 2025). Tests SPY NBBO tick data for a lag-resolved conditional relationship between backward price 'pushes' and forward 'responses', finding a shift from short-term efficiency to longer-lag predictable anomalies.
- [[sources/wilinski-2026-classifying-clustering-trading-agents|Classifying and clustering trading agents]] (Mateusz Wilinski, Anubha Goel, Alexandros Iosifidis and others, 2026). Uses a synthetic agent-based limit order book market with known agent types to compare how well supervised classifiers and unsupervised clustering can recover investors' true behavioral categories.
- [[sources/wu-2021-how-robust-limit-order-book-representations|How Robust are Limit Order Book Representations under Data Perturbation?]] (Yufei Wu, Mahmoud Mahfouz, Daniele Magazzeni and others, 2021). Tests whether the standard level-based limit order book representation is robust to small, mid-price-neutral order placements, and finds deep learning price-forecasting models degrade sharply under this perturbation.
- [[sources/wu-2022-towards-robust-representations-limit-orders-books|Towards Robust Representations of Limit Orders Books for Deep Learning Models]] (Yufei Wu, Mahmoud Mahfouz, Daniele Magazzeni and others, 2022). Shows that the standard compressed representation of limit order books is fragile to small adversarial order placements, and proposes moving-window and market-depth representations that are more accurate and robust.
- [[sources/xiao-2025-lit-limit-order-book-transformer|LiT: limit order book transformer]] (Yue Xiao, Carmine Ventre, Yuhan Wang and others, 2025). Proposes LiT, a CNN-free transformer over structured order-book patches plus LSTM layers, to forecast short-horizon crypto mid-price direction and adapt via fine-tuning.
- [[sources/xu-2026-when-quotes-crumble-detecting-transient-mechanical|When Quotes Crumble: Detecting Transient Mechanical Liquidity Erosion in Limit Order Books]] (Haohan Xu, Jason Bohne, Paweł Polak and others, 2026). Uses a simulated limit order book market with known ground truth to detect transient mechanical quote erosion and produce calibrated crumbling probabilities via a neural labeling model.
- [[sources/young-2026-openmarket-synchronized-polymarket-binance-dataset-high|OpenMarket: A Synchronized Polymarket–Binance Dataset for High-Frequency Prediction-Market Research]] (Gregory Young, 2026). Releases a public millisecond-paired Polymarket-Binance BTC dataset and Rust pipeline, showing that a 43-feature walk-forward logistic model does not beat the market's own mid-price forecast out-of-sample.
- [[sources/zainal-2021-optimal-limit-order-book-prediction-analysis|An Optimal Limit Order Book Prediction Analysis Based on Deep Learning and Pigeon-Inspired Optimizer]] (Mohammad Zainal, Ibrahim Gad, Hameed AlQaheri, 2021). Uses a pigeon-inspired swarm optimizer to select limit-order-book features, then classifies each new order-book event with a CNN/Inception deep network across five NASDAQ stocks.
- [[sources/zaznov-2024-intraday-dynamics-predictor-trioflow-fusion-convolutional|The Intraday Dynamics Predictor: A TrioFlow Fusion of Convolutional Layers and Gated Recurrent Units for High-Frequency Price Movement Forecasting]] (Ilia Zaznov, Julian Martin Kunkel, Atta Badii and others, 2024). Combines convolutional and GRU layers on limit order book and order flow features to classify intraday stock price direction, and tests the resulting signals through simulated trading.
- [[sources/zhang-2019-deeplob-deep-convolutional-neural-networks-limit|DeepLOB: Deep Convolutional Neural Networks for Limit Order Books]] (Zihao Zhang, Stefan Zohren, Stephen Roberts, 2019). Introduces DeepLOB, a CNN plus Inception plus LSTM network that predicts short-horizon price direction from raw limit order book snapshots and tests it on FI-2010 and a year of LSE data.
- [[sources/zhang-2021-multi-horizon-forecasting-limit-order-books|Multi-Horizon Forecasting for Limit Order Books: Novel Deep Learning Approaches and Hardware Acceleration using Intelligent Processing Units]] (Zihao Zhang, Stefan Zohren, 2021). Adapts sequence-to-sequence and attention encoder-decoder deep learning models to forecast limit order book price moves at multiple horizons at once, and benchmarks IPU versus GPU training speed.
- [[sources/zheng-2013-price-jump-prediction-limit-order-book|Price jump prediction in Limit Order Book]] (Ban Zheng, Eric Moulines, Frédéric Abergel, 2012). Uses logistic regression with LASSO variable selection on limit order book depth, gap, and trade-through features to predict inter-trade price jumps for 40 CAC40 stocks.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/trade-clock|Trade Clock]]
- [[concepts/volume-clock|Volume Clock]]
- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]
- [[concepts/hawkes-processes|hawkes processes]]
<!-- AUTHORED REGION END -->