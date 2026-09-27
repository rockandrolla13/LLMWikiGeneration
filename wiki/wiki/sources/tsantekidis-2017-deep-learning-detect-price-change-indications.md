---
authors:
- Avraam Tsantekidis
- Nikolaos Passalis
- Anastasios Tefas
- Juho Kanniainen
- Moncef Gabbouj
- Alexandros Iosifidis
content_hash: sha256:b8ae3039fe074124ff8c8fba98ff1c17abe81096f70f4df18f62f2c6033f837f
created: 2026-09-27 01:47:00+00:00
page_id: sources/tsantekidis-2017-deep-learning-detect-price-change-indications
page_type: source
publication_venue: 2017 25th European Signal Processing Conference (EUSIPCO)
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/high-frequency-data
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/deep-learning-for-finance
- concepts/order-flow-prediction
- concepts/mid-price-prediction
- entities/avraam-tsantekidis
- entities/nikolaos-passalis
- entities/anastasios-tefas
- entities/juho-kanniainen
- entities/moncef-gabbouj
- entities/alexandros-iosifidis
revision_id: 1
schema_version: 2
source_hash: sha256:87fa5175a02b07b34892ad92100b02906a8e33c50a89c653e1c25c2728a22b2c
source_path: markdown_output/tsantekidis-2017-deep-learning-detect-price-change-indications.md
source_type: paper
tags:
- limit-order-book
- lstm
- high-frequency-trading
- mid-price-prediction
- deep-learning
- market-microstructure
- clock-event
- asset-equity
- harvest-relevant
title: Using Deep Learning to Detect Price Change Indications in Financial Markets
updated: '2026-09-27T01:47:00Z'
uuid: b53090cd-3aa9-5b04-99ac-808ec26a505c
year: 2017
---

<!-- AUTHORED REGION START -->
# Using Deep Learning to Detect Price Change Indications in Financial Markets

## Summary

The paper asks whether a recurrent deep learning model can predict the near-term direction of the mid-price in a limit order book more accurately than the handcrafted-feature pipelines typically used in quantitative finance, when trained directly on raw high-frequency order book depth rather than resampled OHLC bars. The approach feeds an LSTM the 10 best price/volume levels on each side of the book (40 values per timestep), standardised separately for prices and volumes using the previous trading day's statistics to cope with scale differences across stocks and days. Labels are a smoothed three-class direction indicator (up, down, stationary) formed by comparing the mean of the preceding and following k mid-prices against a threshold, for three horizons. Training withholds the loss gradient for an initial run of steps so the network can build up a representation of the book before being scored.

The main finding is that the LSTM produces substantially higher Cohen's kappa and F1 scores than a linear SVM and a single-hidden-layer MLP fed the same information as a flattened window of past depth samples, with the advantage largest at the shortest prediction horizon and narrowing, but persisting, as the horizon lengthens. What is new relative to prior handcrafted-feature or small-sample approaches cited by the authors is the combination of a large-scale (multi-million-event) limit order book dataset, a recurrent architecture that consumes the book sequentially rather than as a fixed feature vector, and the day-adaptive normalisation scheme.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Each input timestep is one limit order book depth snapshot (an update event), represented by 10 price/volume levels on the bid side and 10 on the ask side (40 values). The prediction target compares the mean of the previous k mid-prices to the mean of the next k mid-prices around each event, with a threshold parameter that must be exceeded for the move to be labelled upward or downward rather than stationary; three horizons (k = 10, 20, 50) are tested.

## Data

- **Asset class:** Equities
- **Instruments:** Five Finnish stocks: Kesko Oyj, Outokumpu Oyj, Sampo, Rautaruukki and Wartsila Oyj
- **Venue:** Nasdaq Nordic (data feed)
- **Period:** 1st to 14th June 2010 (business days only)
- **Granularity:** Order book depth snapshots with 10 price/volume levels per side (40 values per event); about 4.5 million messages in total across 10 trading days for 5 stocks; the first 7 days are used for training and the remaining 3 for testing.

## Features and Measures

- **mid-price.** The average of the best bid and best ask price at a given time, used as the reference price series whose future direction the model predicts.
- **smoothed direction label.** A three-class label (up, down, stationary) built by comparing the mean of the previous k mid-prices to the mean of the next k mid-prices, with a threshold that the change must exceed to count as directional, used to strip tick-level noise out of the prediction target.
- **per-day adaptive z-score normalisation.** Prices and volumes are each standardised separately, using the mean and standard deviation computed from the previous trading day's data, so that price-scale differences between stocks and day-to-day distribution shifts do not distort the network's input.
- **burn-in period.** The first steps of each recurrent sequence are excluded from the training loss so that the LSTM's hidden state can build up a representation of the order book before its predictions are scored.

## Method

The predictive model is a single LSTM layer feeding a feed-forward layer with leaky ReLU activations, trained by minimising categorical cross-entropy with the Adam optimiser; gradients are not backpropagated for the first 100 steps of each sequence (the burn-in period). A grid check found that 32 to 64 hidden units avoided over- and under-fitting the data, and the reported model uses an LSTM with 40 hidden neurons.

The LSTM is compared against a linear SVM trained with stochastic gradient descent (its regularisation parameter chosen by cross-validation on a training-set split) and an MLP with one hidden layer of 128 leaky-ReLU units; because both baselines are non-recurrent, they instead receive the concatenation of the previous 100 depth samples as a single input vector, with the label of the most recent sample as the prediction target. All three models are evaluated with Cohen's kappa plus the mean recall, precision and F1 score across the three direction classes, using the first 7 days of data for training and the remaining 3 days as a held-out test set, repeated separately for each of the three prediction horizons.

## Results

- The LSTM reached a Cohen's kappa of 0.500 at the shortest horizon (k = 10), well above the SVM's 0.068 and the MLP's 0.226.
- At k = 10, the LSTM's mean F1 score was 66.33%, versus 48.27% for the MLP and 35.88% for the SVM.
- The LSTM's advantage persisted but narrowed at the longest horizon tested: at k = 50 its kappa was 0.411, against 0.324 for the MLP and 0.243 for the SVM.
- The LSTM outperformed both baselines across all three tested prediction horizons (k = 10, 20, 50), with the gap largest for the shortest horizon.
- The dataset totalled about 4.5 million order book messages spanning 10 trading days for five stocks, with 7 days used for training and 3 for testing.

## Limitations

- Only 10 trading days (7 train / 3 test) from a single two-week period are used, so results may not generalise to other market regimes.
- Only five stocks from a single exchange (Nasdaq Nordic) are tested.
- Reader note: no transaction costs, slippage, or execution feasibility are modelled; the paper itself notes the mid-price is a 'virtual value' at which no order can actually trade.
- Reader note: performance is reported on a single chronological train/test split rather than multiple rolling folds, so reported metrics may not reflect stability across different periods.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]
- [[entities/avraam-tsantekidis|Avraam Tsantekidis]]
- [[entities/nikolaos-passalis|Nikolaos Passalis]]
- [[entities/anastasios-tefas|Anastasios Tefas]]
- [[entities/juho-kanniainen|Juho Kanniainen]]
- [[entities/moncef-gabbouj|Moncef Gabbouj]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]

## Citation

Avraam Tsantekidis, Nikolaos Passalis, Anastasios Tefas, Juho Kanniainen, Moncef Gabbouj, Alexandros Iosifidis (2017). Using Deep Learning to Detect Price Change Indications in Financial Markets. 2017 25th European Signal Processing Conference (EUSIPCO).

DOI: 10.23919/eusipco.2017.8081663

Text ingested: `markdown_output/tsantekidis-2017-deep-learning-detect-price-change-indications.md`, converted from `raw/ofi-event-clock/tsantekidis-2017-deep-learning-detect-price-change-indications.pdf`.

Coverage of this summary: Read the full paper (about 5 pages): abstract, introduction, related work, the high-frequency limit order data description, the LSTM methodology and normalisation scheme, the experimental setup and results table, and the conclusion.

Known problems with the input: Several equations in the converted markdown are rendered as omitted images (e.g. mid-price definition, LSTM gate equations, the cross-entropy loss); their content is described here from the surrounding prose rather than the equations themselves.
<!-- AUTHORED REGION END -->