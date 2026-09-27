---
authors:
- Ymir Mäkinen
- Juho Kanniainen
- Moncef Gabbouj
- Alexandros Iosifidis
content_hash: sha256:cfb1824bc40f873321a36b5591486a830b2bfebab07bfd6ccfdf3dd647be07f3
created: 2026-09-27 01:47:00+00:00
page_id: sources/makinen-2018-forecasting-jump-arrivals-stock-prices-new
page_type: source
publication_venue: arXiv preprint
related:
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/feature-engineering
- concepts/high-frequency-data
- concepts/market-microstructure
- entities/juho-kanniainen
- entities/moncef-gabbouj
- entities/alexandros-iosifidis
revision_id: 1
schema_version: 2
source_hash: sha256:13fdad2134c759dd975e35971820dfcce5f633609e58e9b11bdfa603d8b6582a
source_path: markdown_output/makinen-2018-forecasting-jump-arrivals-stock-prices-new.md
source_type: paper
tags:
- limit-order-book
- jump-prediction
- neural-networks
- attention-mechanism
- lstm
- cnn
- equity-markets
- high-frequency-data
- clock-calendar
- asset-equity
- harvest-relevant
title: 'Forecasting of Jump Arrivals in Stock Prices: New Attention-based Network
  Architecture using Limit Order Book Data'
updated: '2026-09-27T01:47:00Z'
uuid: 0421eb0c-5f51-5dac-8ab8-140e18fc33f0
year: 2021
---

<!-- AUTHORED REGION START -->
# Forecasting of Jump Arrivals in Stock Prices: New Attention-based Network Architecture using Limit Order Book Data

## Summary

The paper asks whether the arrival of price jumps in equity returns can be predicted from high-frequency limit order book (LOB) data using neural networks, motivated by the idea that market makers with information about incoming news may withdraw liquidity from one side of the book shortly before a jump, making the resulting order-book asymmetry a predictive signal. Jumps are defined as price moves too large to be explained by continuous (Brownian) price dynamics, and are labeled using the nonparametric jump test of Lee and Mykland (2008) applied to mid-price data.

The authors use NASDAQ TotalView-ITCH order book data (ten levels per side) for five liquid stocks (GOOG, MSFT, AAPL, INTC, FB) over 360 trading days spanning about a year and a half. Order book state and event intensities are recomputed every second; from these, 144 indicators following Kercheval and Zhang (2015) are derived, and samples are drawn every minute using a 120-minute lookback window. The task is binary classification: whether a jump occurs in the following one-minute period. Four network types are compared: a multi-layer perceptron (MLP), a convolutional network (CNN), a Long Short-Term Memory network (LSTM), and a new CNN-LSTM-Attention architecture that applies an attention mechanism along the feature dimension (rather than the time dimension) to weight which LOB-derived inputs matter most for a given sample.

The CNN-LSTM-Attention model achieved the highest average F1 score across stocks and time periods, ahead of the plain LSTM, the CNN, and the MLP, all of which outperformed a random classifier. The improvement from including LOB data (versus a variant using only the time-of-day feature) was stock-specific, ranging from clear to marginal. Predicting the direction of a jump (up versus down), by contrast, was much harder and close to random.

What is new is the feature-wise attention mechanism itself: rather than weighting which time steps matter (the usual use of attention in sequence models), it weights which order-book-derived features matter, and the authors use this to inspect which feature groups (largely order-book quantities/volumes, more than prices) the model relies on for jump prediction.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The underlying order book state and order-flow intensities are recomputed every second during market hours (23,400 observations per trading day), but the model itself is sampled at fixed one-minute intervals: each input sample is a 120-step lookback window of one-minute observations (the past 120 minutes), and the label is a fixed one-minute-ahead binary indicator of whether a Lee-Mykland-detected jump occurs in the following one-minute period.

## Data

- **Asset class:** Equities
- **Instruments:** GOOG (Google), MSFT (Microsoft), AAPL (Apple), INTC (Intel), and FB (Facebook) — five liquid NASDAQ-listed stocks
- **Venue:** NASDAQ (TotalView-ITCH limit order book data)
- **Period:** 360 trading days spanning about one and a half years, 2014-2015
- **Granularity:** Order book state and event intensities computed every second during market hours; model samples drawn at one-minute intervals using a 120-step (120-minute) lookback window

## Features and Measures

- **Basic LOB features.** Raw ask and bid prices and volumes for the ten best levels on each side of the order book.
- **Time-insensitive features.** Derived static features such as the bid-ask spread, mid-price, price differences between adjacent levels, and price/volume means and accumulated differences.
- **Time-sensitive features.** Features capturing change over time, including price and volume derivatives, average and relative order-arrival intensities by order type and side, and their accelerations.
- **Clock-time feature.** The time of day, rounded to the nearest hour, included so the model can learn intraday patterns independent of other inputs.
- **CNN-LSTM-Attention architecture.** A network combining a feature-dimension attention layer, a 1D convolution, max pooling, and an LSTM layer, used to produce the binary jump/no-jump prediction.

## Method

Jumps are labeled with the Lee and Mykland (2008) nonparametric test applied to mid-price data, using a 600-minute window for estimating bipower variation. Inputs are the 144 LOB-derived indicators of Kercheval and Zhang (2015). Four network architectures (MLP, CNN, LSTM, and the new CNN-LSTM-Attention model) are trained and compared, alongside a random classifier and a CNN-LSTM variant using only the time-of-day feature as baselines. Models are implemented in Keras with a TensorFlow backend, trained with the Adam optimizer and a cross-entropy loss. Training follows a rolling scheme across seven overlapping splits (50 up to 350 days of training data, each followed by a 10-day test period), with positive jump samples oversampled by shifting the sampling window by a few seconds because jumps are rare relative to non-jumps. Performance is judged primarily by F1 score, given the class imbalance, alongside precision, recall, and Cohen's Kappa.

## Results

- The CNN-LSTM-Attention model achieved the highest average F1 across all stocks and sets, about 0.72, versus 0.69 for LSTM, 0.66 for CNN, 0.53 for MLP, and 0.32 for a random classifier.
- A CNN-LSTM variant using only the time-of-day feature reached an average F1 of 0.66, comparable to the LSTM and CNN models trained on the full feature set.
- Averaged over all seven training/test splits, the CNN-LSTM-Attention model's F1 was 0.71.
- For the CNN-LSTM-Attention model, Intel had the best per-stock F1 at 0.78, while Microsoft had the worst score, roughly ten percentage points lower.
- Predicting the direction of a jump (up versus down) was much harder: the CNN-LSTM-Attention model's average F1 on that task was about 0.53, barely above the 0.49 random baseline.
- The dataset contained 5537 detected jumps across the observation period, concentrated heavily in the first half hour of the trading day.
- Inspecting attention weights on a small set of example samples showed order-book quantity/volume features were consistently weighted as important, more so than price-level features, alongside the time-of-day feature.

## Limitations

- Predicting the direction of a jump was much harder than predicting its arrival, with results close to a random classifier.
- The attention-mechanism interpretation was based on only four hand-picked example samples (one true positive, true negative, false positive, and false negative), not a systematic analysis of the full test set.
- The authors note the method is not applicable to markets without a public limit order book, such as foreign exchange.
- Reader note: jump labels depend on a chosen statistical test and its window/threshold settings, so a detected 'jump' is a modeling choice rather than a directly observed event.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[entities/juho-kanniainen|Juho Kanniainen]]
- [[entities/moncef-gabbouj|Moncef Gabbouj]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]

## Citation

Ymir Mäkinen, Juho Kanniainen, Moncef Gabbouj, Alexandros Iosifidis (2021). Forecasting of Jump Arrivals in Stock Prices: New Attention-based Network Architecture using Limit Order Book Data. arXiv preprint.

DOI: 10.48550/arxiv.1810.10845

Text ingested: `markdown_output/makinen-2018-forecasting-jump-arrivals-stock-prices-new.md`, converted from `raw/ofi-event-clock/makinen-2018-forecasting-jump-arrivals-stock-prices-new.pdf`.

Coverage of this summary: Read the full markdown text of the paper start to finish, including abstract, introduction, data section (2.1-2.3), model descriptions (3.1-3.6), results (4.1-4.4), conclusion, and the appendix tables.

Known problems with the input: The printed submission date is garbled by the PDF-to-markdown conversion ('Preprint submitted to arXiv September 17, September 17, 2021'); the job's year_hint is 2018, but 2021 is the year actually printed on this converted version, so year is reported as 2021 with this note; Several result tables (e.g., the per-stock/per-model tables) are rendered with merged or misaligned cells by the conversion, making exact digit-to-model mapping unreliable in places; only figures that could be cross-checked against unambiguous prose statements were used.
<!-- AUTHORED REGION END -->