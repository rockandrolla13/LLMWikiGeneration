---
authors:
- Yuqi li
content_hash: sha256:e3a014714ea27b8c8715c8d6004dc4ed2a4f236dcbb28c5b1f5dc1af1cd12183
created: 2026-09-27 01:47:00+00:00
page_id: sources/li-2026-research-high-frequency-financial-transaction-behavior
page_type: source
publication_venue: Data and Metadata (journal), volume 5, article 1459
related:
- concepts/trade-clock
- concepts/high-frequency-trading
- concepts/limit-order-book
- concepts/order-flow-imbalance
- concepts/graph-neural-networks
- concepts/lstm-networks
- concepts/deep-learning-for-finance
- concepts/market-microstructure
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
source_hash: sha256:4c41429d5db1335e5754ee5a1e6823f4d3b732519f70144831cf8a2f34245059
source_path: markdown_output/li-2026-research-high-frequency-financial-transaction-behavior.md
source_type: paper
tags:
- high-frequency-trading
- spoofing-detection
- cnn-lstm-gnn
- order-book
- account-graph
- anomaly-detection
- bayesian-optimization
- market-surveillance
- clock-trade
- asset-equity
- harvest-relevant
title: Research on high-frequency financial transaction behavior recognition and prediction
  method integrating machine learning
updated: '2026-09-27T01:47:00Z'
uuid: 460c23e2-de2c-5afe-90ba-71e5d3d8f7bf
year: 2026
---

<!-- AUTHORED REGION START -->
# Research on high-frequency financial transaction behavior recognition and prediction method integrating machine learning

## Summary

The paper asks whether combining tick-by-tick transaction sequences, limit order book snapshots and an account-level trading-relationship graph in one model can recognise high-frequency trading behaviour categories, forecast short-horizon price direction, and flag abnormal or manipulative behaviour more effectively than approaches that use only one of these data sources or a single neural architecture.

The approach builds a multimodal feature set: a time-series tensor of price, volume, return and behaviour statistics over a 100-event sliding window; an order-book depth tensor; and an account interaction graph where accounts are nodes and transaction or repeated-counterparty relationships are edges. These are encoded by parallel CNN, LSTM and GNN branches and fused into a single classifier for five behaviour labels (normal trading, arbitrage, speculation, quote stuffing, spoofing), while separate heads forecast return direction and quantile-based volatility ranges at several horizons, and an autoencoder-plus-isolation-forest anomaly score is built from account-level order-behaviour profiles. Hyperparameters are tuned with Bayesian optimization, with particle swarm search used for structural choices, and the model is evaluated on a chronologically split, out-of-sample test period plus a separate cross-market test.

The main finding is that the full fusion model with Bayesian optimization outperforms a series of baselines, including rule-based surveillance, plain LSTM, CNN-LSTM, Transformer, and several reimplementations of recent order-book and HFT-detection methods from the literature, on behaviour-recognition accuracy and macro-F1, on 10-millisecond directional price accuracy, and on anomaly-detection recall and AUC, while running at single-digit-millisecond inference latency. An ablation study shows that removing the order-book channel or the account-graph (GNN) branch causes the largest drops in performance, and a cross-market test on Nasdaq data (after training on Shanghai/Shenzhen data, with no fine-tuning) shows the model still outperforms the baselines, though at a lower absolute level than within-market.

What is new relative to the cited literature, most of which targets price or mid-price prediction alone, is treating behaviour recognition, short-horizon prediction and anomaly warning as one joint task built on transaction, order-book and account-relationship modalities together, with a Top-K, confidence-thresholded output designed to route uncertain cases to analyst review rather than forcing a single hard label.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

The recognition and prediction model consumes sliding windows of T=100 consecutive event steps (order placements, cancellations, modifications and executions) rather than a fixed span of wall-clock time, so the input sampling is per event rather than per calendar interval. Forecast targets are then defined at fixed wall-clock horizons of 1, 10 and 100 milliseconds ahead of the current mid-price, and behaviour and anomaly labels are assigned per account within short observation windows built on the same event stream.

## Data

- **Asset class:** Equities
- **Instruments:** not stated (specific tickers are not named); training data are described as coming from Shanghai and Shenzhen markets, with a separate cross-market test on Nasdaq data
- **Venue:** not stated precisely; described as Level-2 market data interfaces and institutional order log systems, plus a market replay system for simulated data
- **Period:** 120 trading days from January 2023 to June 2023, of which 116 valid trading days were retained after removing incomplete or interrupted sessions; split chronologically into 80 training days, 16 validation days and 20 out-of-sample test days
- **Granularity:** Tick-by-tick transaction records, order book snapshots at up to 10 depth levels, and per-account order behaviour logs (placement, cancellation, modification, execution), aligned to a microsecond timeline

## Features and Measures

- **Order Book Imbalance (OBIt).** A per-window feature contrasting bid- and ask-side order book depth, used as part of the order-book input channel.
- **Bid-ask spread (Spreadt).** The difference between the best ask price and the best bid price at a given timestamp.
- **Order behaviour profile.** A per-account, per-window vector combining order placement rate, cancellation rate, execution rate, average order lifetime, cancellation-to-execution ratio, order book imbalance, spread change and counterparty concentration, used to flag spoofing and quote stuffing.
- **Account interaction graph.** A graph in which each node is an anonymised trading account and each edge represents a transaction or repeated counterparty relationship within an observation window, used to capture coordinated or relational trading patterns.
- **Reconstruction-based anomaly score.** An autoencoder's reconstruction error on an account's behaviour vector, combined with an isolation-forest anomaly score, used to flag deviation from normal trading behaviour.

## Method

The model has three parallel branches: a CNN-LSTM branch over the 100-step transaction time-series tensor to capture local microstructure patterns and temporal dependence, an order-book branch over the depth tensor, and a graph neural network branch over the account interaction graph to capture relational trading structure; the three branch outputs are concatenated and passed through a fully connected classifier with a softmax output over five behaviour labels. Hyperparameters (learning rate, batch size, CNN filter count and kernel size, LSTM and GNN hidden dimensions and depth, dropout rate, weight decay and fusion-layer dimension) are tuned by Bayesian optimization against validation macro-F1, with particle swarm optimization used for lightweight structure search; training uses class weighting and stratified sampling to address label imbalance, plus dropout, L2 regularisation and early stopping after 10 non-improving validation epochs.

Price and volatility forecasting reuses the same multimodal input to predict, at each of three horizons (1, 10 and 100 milliseconds), a point return, a directional label, and a 5th/50th/95th percentile quantile-regression volatility interval. An ensemble of LSTM, CNN-LSTM and Transformer base predictors, weighted by validation loss, is also used to produce final predictions. Evaluation uses a chronological (not random) train/validation/test split, a separate cross-market test on Nasdaq data with no fine-tuning, 10 repeated training runs with different random seeds, and paired two-sided t-tests against the strongest baseline under the same test split.

## Results

- On the out-of-sample test set, the full fusion model with Bayesian optimization reached 95,1 % behaviour recognition accuracy and 94,4 % macro-F1, improving on the strongest baseline (an explainable-HFT-style model) by 3,5 and 3,9 percentage points respectively, with the paired t-test giving t=24,18, p<0,001.
- At the 10 ms price-prediction horizon, the fusion-plus-Bayesian model obtained RMSE 0,013, MAPE 2,00 %, and directional accuracy 67,8 %, 3,6 percentage points above the next-best baseline (t=18,73, p<0,001).
- Prediction accuracy degraded as the horizon lengthened: RMSE rose from 0,009 at 1 ms to 0,013 at 10 ms to 0,021 at 100 ms, directional accuracy fell from 70,2 % to 67,8 % to 62,5 %, while the quantile-based interval coverage stayed close to 90 % across horizons (91,4 %, 90,7 %, 89,3 %).
- In anomaly detection, the fusion-plus-Bayesian model achieved 92,5 % recall and an AUC of 0,967, a 4,4 percentage-point recall gain and 0,042 AUC gain over a spoofability-style probabilistic neural network baseline.
- Ablation experiments showed that removing the order book channel cost 3,3 percentage points of recognition accuracy (the largest single drop), while removing the account-graph (GNN) branch cost 3,1 percentage points of accuracy and lowered anomaly recall.
- The optimized model ran at 9,2 ms average latency and about 50,000 records per second throughput, 1,6 ms faster and 25,0 % higher throughput than a plain Transformer baseline.
- On a Nasdaq cross-market test with no fine-tuning after training on Shanghai/Shenzhen data, accuracy fell to 92,1 % and anomaly recall to 89,6 %, still 3,7 and 5,5 percentage points above the strongest baseline on that test.
- The dataset comprised about 300 million tick-by-tick records and 80 million order book snapshots from 203,746 accounts over 116 valid trading days, with behaviour labels split 72,6 % normal trading, 9,8 % arbitrage, 8,9 % speculation, 5,3 % quote stuffing and 3,4 % spoofing.

## Limitations

- The authors state that training data are drawn from a specific period (120 trading days, January-June 2023) and specific markets, which they say limits generalisation to other markets and periods.
- Behaviour labels rely partly on manual review and on simulation-injected spoofing and quote-stuffing patterns, which the authors acknowledge may carry annotator subjectivity and may not fully reproduce real manipulation strategies.
- The authors describe the framework as a recognition and warning system rather than an evaluated trading strategy: no trading return, Sharpe ratio, drawdown or transaction-cost-adjusted performance is reported.
- Cross-market (Nasdaq) performance was lower than within-market performance, which the authors attribute to differing tick sizes, liquidity structures, order submission frequencies and participant behaviour.
- Reader note: this is a single-author study, and no independent replication of the pipeline, data, or labels is reported in the paper.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/graph-neural-networks|graph neural networks]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]

## Citation

Yuqi li (2026). Research on high-frequency financial transaction behavior recognition and prediction method integrating machine learning. Data and Metadata (journal), volume 5, article 1459.

DOI: 10.56294/dm20261459

Text ingested: `markdown_output/li-2026-research-high-frequency-financial-transaction-behavior.md`, converted from `raw/ofi-event-clock/li-2026-research-high-frequency-financial-transaction-behavior.pdf`.

Coverage of this summary: Read the full markdown file from abstract through conclusions, references and the authorship-contribution statement, including all tables.

Known problems with the input: Many equations in the method sections are rendered as garbled OCR text or omitted images in the markdown conversion (for example the LSTM and GNN update equations), so exact functional forms could not be verified beyond the surrounding prose; The source document prints numbers with a comma as the decimal separator (e.g. '95,1 %'); these are copied verbatim from the markdown rather than converted to a period-decimal format.
<!-- AUTHORED REGION END -->