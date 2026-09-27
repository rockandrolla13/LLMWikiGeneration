---
authors:
- Nikolaos Passalis
- Anastasios Tefas
- Juho Kanniainen
- Moncef Gabbouj
- Alexandros Iosifidis
content_hash: sha256:3b70afa716b4c0269601568a8ce6e4bd0c090bb1fd14dd64b47fe5889f782ec1
created: 2026-09-27 01:47:00+00:00
page_id: sources/passalis-2019-deep-adaptive-input-normalization-price-forecasting
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/high-frequency-data
- concepts/recurrent-neural-networks
- concepts/order-flow-prediction
- entities/nikolaos-passalis
- entities/anastasios-tefas
- entities/juho-kanniainen
- entities/moncef-gabbouj
- entities/alexandros-iosifidis
revision_id: 1
schema_version: 2
source_hash: sha256:1af478ed885763d2f6041338e0913f4225c35b3959e65f8078eb9f1de44a128c
source_path: markdown_output/passalis-2019-deep-adaptive-input-normalization-price-forecasting.md
source_type: paper
tags:
- deep-learning
- input-normalization
- limit-order-book
- mid-price-prediction
- non-stationary-data
- time-series-forecasting
- clock-event
- asset-equity
- harvest-relevant
title: Deep Adaptive Input Normalization for Time Series Forecasting
updated: '2026-09-27T01:47:00Z'
uuid: 3343ebe4-edbc-5bb3-bee7-55057b66d79a
year: 2019
---

<!-- AUTHORED REGION START -->
# Deep Adaptive Input Normalization for Time Series Forecasting

## Summary

The paper addresses a practical problem in applying deep learning to financial time series: fixed normalization schemes such as z-score normalization use statistics computed once on the training data and cannot adapt when the data are non-stationary or multimodal, for example when training on many stocks with very different price levels.

The proposed Deep Adaptive Input Normalization (DAIN) layer is composed of three trainable sub-layers applied in sequence: an adaptive shifting layer that centers the input using a linear transform of a summary (mean) representation of the current window, an adaptive scaling layer that rescales the shifted input using a summary of its spread, and an adaptive gating layer that nonlinearly suppresses features judged unhelpful for the task. All three sub-layers are trained end-to-end with the rest of the network via back-propagation, with separate learning rates per sub-layer, and the layer can be applied directly to raw, unnormalized data.

On the FI-2010 limit order book dataset the method is evaluated with an MLP, a CNN and a GRU-based RNN, predicting the direction of the mid price several steps ahead, using an anchored (expanding-window, day-by-day) train/test protocol. DAIN with all three sub-layers consistently outperformed no normalization, z-score normalization, sample-average normalization, Batch Normalization and Instance Normalization across all three architectures and both tested prediction horizons, and it also improved results on a household power-consumption forecasting dataset.

The paper also shows DAIN is markedly more robust to an injected distribution shift at test time than z-score normalization, whose accuracy dropped sharply while DAIN's changed only slightly. The main novelty is that the normalization itself is learned and adapts per-input, rather than being a fixed, hand-designed transform computed once from training data.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Each input sample is a window of the 15 most recent limit-order-book feature vectors (144-dimensional, built from event-level order updates in the FI-2010 dataset), and the model predicts the direction of the average mid price 10 or 20 time steps ahead using an anchored, day-by-day expanding train/test split across the dataset's trading days.

## Data

- **Asset class:** Equities
- **Instruments:** Limit order book data from 5 Finnish companies traded on the Helsinki Exchange (FI-2010 dataset); a secondary, non-financial evaluation used a household electric power consumption dataset.
- **Venue:** Helsinki Exchange (operated by Nasdaq Nordic)
- **Period:** 1st June 2010 to 14th June 2010 (10 business days)
- **Granularity:** Event-level order book updates aggregated into 144-dimensional feature vectors; model input windows cover the 15 most recent such vectors.

## Features and Measures

- **Adaptive shifting layer.** A linear layer that centers each measurement dimension of the current window using a transform of the window's own average (summary) representation, instead of a fixed, precomputed mean.
- **Adaptive scaling layer.** A linear layer applied after shifting that rescales each dimension using a transform of a summary representation of the window's spread, playing the role that dividing by standard deviation plays in z-score normalization.
- **Adaptive gating layer.** A nonlinear, sigmoid-based layer applied after shifting and scaling that suppresses input features judged irrelevant or harmful for the forecasting task, using a third summary representation of the window.

## Method

Three deep architectures are evaluated: a multilayer perceptron (MLP) with one 512-unit hidden layer, a convolutional neural network (CNN) with a 1-D convolution layer of 256 filters and kernel size 3, and a recurrent network (RNN) with a 256-unit GRU layer, each followed by the same fully connected output layers and trained with the cross-entropy loss using RMSProp. Performance is judged using macro-averaged precision, recall and F1 across the three price-direction classes (up, stationary, down) plus Cohen's kappa, computed under an anchored evaluation scheme where the model is trained on data from one or more early days and tested on the following day, repeated across the dataset's trading days. An ablation study first isolates the contribution of each DAIN sub-layer (shifting only, shifting plus scaling, and all three) against no normalization, z-score normalization, sample-average normalization, Batch Normalization and Instance Normalization; the best-performing normalization schemes are then compared on the full training data at two prediction horizons, and again on a second, non-financial forecasting dataset.

## Results

- In the ablation study (10-step horizon, first three days), DAIN with all three sub-layers reached a macro F1 of 66.92 and Cohen's kappa of 0.4934 for the MLP, versus 53.76 F1 and 0.3059 kappa for z-score normalization and near-zero kappa (0.0010) for no normalization.
- For the CNN, DAIN with all three sub-layers reached 63.02 macro F1 and 0.4327 kappa, versus 50.94 F1 and 0.2570 kappa for z-score normalization.
- In the full evaluation with the MLP at a 10-step horizon, DAIN reached 68.26 macro F1 and 0.5145 Cohen's kappa, ahead of Instance Normalization (59.67 F1, 0.3827 kappa) and z-score normalization (54.65 F1, 0.3206 kappa).
- On the household power consumption dataset, DAIN with the MLP reached 78.83% accuracy versus 77.93% for Instance Normalization, 75.39% for z-score normalization and 71.57% for no normalization.
- Under an injected distribution shift at test time (adding three times the average value to each measurement), the z-score-normalized MLP's accuracy fell from 75.39% to 56.56%, while the DAIN-normalized MLP's accuracy fell less than 0.5%, from 78.59% to 78.21%.
- The adaptive gating (third) sub-layer improved results further for the MLP and CNN by about 2.5% relative improvement, but did not improve the GRU-based RNN, which the authors attribute to the GRU already having its own internal gating mechanisms.

## Limitations

- The authors note that separate, carefully tuned learning rates were required for each DAIN sub-layer, and propose alternative learning rules such as multiplicative weight updates as future work to reduce this tuning burden.
- The authors state that the current design discards mode information from the input, which could be recovered by future extensions that also encode the mode explicitly.
- Reader note: the financial evaluation uses a single limit order book dataset covering 10 trading days from 5 Finnish stocks; generalization to other markets, instruments or longer periods is untested here.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[entities/nikolaos-passalis|Nikolaos Passalis]]
- [[entities/anastasios-tefas|Anastasios Tefas]]
- [[entities/juho-kanniainen|Juho Kanniainen]]
- [[entities/moncef-gabbouj|Moncef Gabbouj]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]

## Citation

Nikolaos Passalis, Anastasios Tefas, Juho Kanniainen, Moncef Gabbouj, Alexandros Iosifidis (2019). Deep Adaptive Input Normalization for Time Series Forecasting.

Text ingested: `markdown_output/passalis-2019-deep-adaptive-input-normalization-price-forecasting.md`, converted from `raw/ofi-event-clock/passalis-2019-deep-adaptive-input-normalization-price-forecasting.pdf`.

Coverage of this summary: Read the full markdown file including abstract, introduction, the normalization method section, the entire experimental evaluation section (ablation, main results, robustness test, hyper-parameters), conclusions and reference list.

Known problems with the input: year from file metadata.
<!-- AUTHORED REGION END -->