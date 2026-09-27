---
authors:
- Taiki Yamamoto
- Haruhi Enomoto
- Junsuke Senoguchi
content_hash: sha256:eddd31bd1efd222fd5f28679d0357732673f7a85b8c4d22c9ce82d9880df1ea9
created: 2026-09-27 01:47:00+00:00
page_id: sources/yamamoto-2025-hybrid-cnn-lstm-model-bitcoin-limit
page_type: source
related:
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/order-flow-prediction
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
source_hash: sha256:e7b8e8311d5cf7e10841ec6460dcfa134c2a7d720d0b14f02497d2bfe41b250c
source_path: markdown_output/yamamoto-2025-hybrid-cnn-lstm-model-bitcoin-limit.md
source_type: paper
tags:
- cryptocurrency
- limit-order-book
- cnn-lstm
- deep-learning
- bitcoin
- price-direction-prediction
- high-frequency-data
- clock-calendar
- asset-crypto
- harvest-relevant
title: Hybrid CNN-LSTM Model for Bitcoin Limit Order Book Prediction
updated: '2026-09-27T01:47:00Z'
uuid: 88a1162c-9c73-5b49-940d-c8cb922da6e0
year: 2025
---

<!-- AUTHORED REGION START -->
# Hybrid CNN-LSTM Model for Bitcoin Limit Order Book Prediction

## Summary

The paper asks whether combining convolutional and recurrent layers can improve short-horizon direction prediction from cryptocurrency limit order book (LOB) data, building on an earlier ternary-classification approach that the authors say suffered from a labeling method letting past data leak into the prediction target. They restrict the task to binary up/down classification and change the labeling rule so the label at time t is formed only from prices strictly after the input window, not from data already inside it.

Using one-second LOB snapshots (top 25 levels) for the XBT/USD pair on BitMEX from March 1, 2022 to January 31, 2023, they build input sequences from the top 10 bid/ask price and volume levels, normalize each day's features using the previous day's mean and standard deviation, and balance the up/down classes by subsampling the majority class while preserving each sample's continuous time-step sequence rather than shuffling individual snapshots. The model is a hybrid CNN-LSTM: a 2D convolution over the time and feature axes, two stages of 1D convolution with batch normalization and max pooling, a bidirectional LSTM, and two fully connected layers before a softmax output, trained with the Adam optimizer and cross-entropy loss.

The hybrid model reached 61% overall accuracy and an AUC-ROC of 0.6180, and was noticeably stronger on the upward class (71% precision, 68% recall, 69% F1) than the downward class (44% precision, 47% recall, 45% F1). A simple trading strategy built on the model's predictions produced a Sharpe ratio of 0.2158 and a profit factor of 1.5347, which the authors read as a small but positive risk-adjusted edge.

The main claimed contributions are the leakage-free labeling scheme, contrasted with the past-data-inclusive labeling of the prior method they build on, and the temporally-consistent class-balancing procedure, which the authors say improved accuracy relative to conventional random balancing while keeping the sequential structure of the data intact.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Limit order book snapshots are taken once per second (top 25 price levels) for the BitMEX XBT/USD pair; at each time step t, a window of data from t to t+T is used as the input, and the binary up/down label compares the price at t+T to the price at t+T+1, so the label is generated strictly from data after the input window rather than from data inside it.

## Data

- **Asset class:** Crypto
- **Instruments:** XBT/USD (BitMEX)
- **Venue:** BitMEX exchange (data purchased via TARDIS.DEV)
- **Period:** March 1, 2022 to January 31, 2023
- **Granularity:** 1-second limit order book snapshots, top 25 bid/ask levels; top 10 bid/ask price and volume levels used as model input

## Features and Measures

- **Leakage-free binary labeling.** A labeling rule that forms the up/down label for a window ending at time t+T by comparing prices at t+T and t+T+1, so the label depends only on data after the input window rather than data used as model input.
- **Temporally-consistent class balancing.** A data-balancing method that randomly subsamples the majority class down to the minority class size while keeping each sample's T-step sequence intact and re-sorting by time index, so balancing does not break the sequential structure of the series.
- **Hybrid CNN-LSTM architecture.** A model that first applies 2D and 1D convolutional layers (with batch normalization and max pooling) to extract local spatial patterns from LOB snapshots, then passes the resulting features through a bidirectional LSTM to capture temporal dependencies before a fully connected classification head.

## Method

The model takes 3D input tensors of shape (T, D, C) built from normalized top-10 bid/ask price and volume levels. A 2D convolutional layer (16 filters, kernel size 4xD) with LeakyReLU (alpha=0.01) extracts local time-feature patterns, followed by two 1D convolutional stages (16 filters kernel size 4, then 32 filters kernel size 3), each with batch normalization and max pooling (size 2). A bidirectional LSTM with 64 units processes the resulting sequence, and its final-time-step output feeds two fully connected layers of 32 units each (LeakyReLU) before a 2-unit softmax output.

Training uses the Adam optimizer with a learning rate of 0.001, sparse categorical cross-entropy loss, a batch size of 32, and 10 epochs, on a 70%/30% train/test split with missing values forward-filled. Performance is judged with accuracy, F1-score and AUC-ROC, and the model's practical value is further checked with a simple virtual trading strategy evaluated by Sharpe ratio and profit factor.

## Results

- Overall accuracy was 61%, with an AUC-ROC of 0.6180 against a random-classifier benchmark of 0.5.
- For the upward class: precision 71%, recall 68%, F1-score 69%.
- For the downward class: precision 44%, recall 47%, F1-score 45%.
- The confusion matrix showed 63,596 correctly classified upward instances and 23,628 correctly classified downward instances, with 31,456 upward instances misclassified as downward (reported elsewhere in the paper as 27,004 downward instances misclassified as upward).
- A simple prediction-based trading strategy produced a Sharpe ratio of 0.2158 and a profit factor of 1.5347.
- The temporally-consistent balancing method improved accuracy over conventional random sampling by about 2-3 percentage points (the paper states both a 2% and a 3% improvement in different passages).

## Limitations

- Downward-class prediction was substantially weaker than upward-class prediction (F1-score 45% versus 69%), leaving a directional bias in the model.
- Evaluated on a single instrument and venue (XBT/USD on BitMEX) over an 11-month window, so generalization to other assets or exchanges is untested.
- The trading-strategy evaluation is preliminary, without volatility, volume, or liquidity indicators added to the feature set.
- Reader note: normalization statistics are taken from the previous trading day (same-day for the first day), which assumes stable short-term statistics and was not stress-tested across regime changes.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-data|high frequency data]]

## Citation

Taiki Yamamoto, Haruhi Enomoto, Junsuke Senoguchi (2025). Hybrid CNN-LSTM Model for Bitcoin Limit Order Book Prediction.

DOI: 10.21203/rs.3.rs-7176682/v1

Text ingested: `markdown_output/yamamoto-2025-hybrid-cnn-lstm-model-bitcoin-limit.md`, converted from `raw/ofi-event-clock/yamamoto-2025-hybrid-cnn-lstm-model-bitcoin-limit.pdf`.

Coverage of this summary: Read the entire converted markdown: abstract, introduction, data and methods, results, discussion, and conclusion, plus the author-contribution and data-availability statements at the end.

Known problems with the input: The paper's title heading was not present in the converted markdown (the visible text begins with affiliation footnotes and a preprint coversheet); the title field uses the title_hint supplied in the job file; Author-affiliation mapping is inferred from the order of the two affiliation footnotes versus the order of authors in the contribution statement (T.Y., H.E., J.S.); the markdown does not attach footnote numbers directly to author names; The venue/publisher is not explicitly named in the text (only a DOI with prefix 10.21203 and a 'Posted Date' are given), so venue is left blank; The paper reports two different figures for the accuracy improvement from the data-balancing method ('2%' in one passage and '3%' in another) and two different counts for downward-classified-as-upward misclassifications (31,456 and 27,004); both are carried through as printed.
<!-- AUTHORED REGION END -->