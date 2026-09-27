---
authors:
- Ilia Zaznov
- Julian Martin Kunkel
- Atta Badii
- Alfonso Dufour
content_hash: sha256:3fe7eef0d5f372df8e0d45a86b6d7506c88e5a5c7da47fc552d8be98ae3ebc17
created: 2026-09-27 01:47:00+00:00
page_id: sources/zaznov-2024-intraday-dynamics-predictor-trioflow-fusion-convolutional
page_type: source
publication_venue: Applied Sciences (MDPI), volume 14, article 2984
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/order-flow
- concepts/order-flow-prediction
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/recurrent-neural-networks
- concepts/deep-learning-for-finance
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:e76c135e63657f843fa2404a169b2d7e4faeeacf9cc0799678865704a27c3ef5
source_path: markdown_output/zaznov-2024-intraday-dynamics-predictor-trioflow-fusion-convolutional.md
source_type: paper
tags:
- limit-order-book
- order-flow
- deep-learning
- cnn-gru
- price-direction-prediction
- high-frequency-trading
- trading-simulation
- clock-event
- asset-equity
- harvest-relevant
title: 'The Intraday Dynamics Predictor: A TrioFlow Fusion of Convolutional Layers
  and Gated Recurrent Units for High-Frequency Price Movement Forecasting'
updated: '2026-09-27T01:47:00Z'
uuid: ca27a519-e28f-5e6d-96c5-d312c5f9d338
year: 2024
---

<!-- AUTHORED REGION START -->
# The Intraday Dynamics Predictor: A TrioFlow Fusion of Convolutional Layers and Gated Recurrent Units for High-Frequency Price Movement Forecasting

## Summary

The paper asks whether tick-by-tick limit order book (LOB) and order flow (OF) data, once turned into a suitable feature representation, contain enough signal to forecast the direction of intraday stock price moves, and whether a new convolutional-recurrent architecture can improve on existing deep learning benchmarks for this task. The proposed model, TFF-CL-GRU, feeds LOB and OF features spanning the 100 most recent timestamps through nine convolutional layers, then three parallel convolutional sub-blocks, and finally a GRU layer before a three-way softmax output for up/flat/down classification.

Feature engineering combines LOB price and volume at the 10 best bid and ask levels (40 features) with the price, volume and buy/sell direction of the 10 most recent trades since the last LOB update (30 features), giving 70 features per timestamp for a new dataset built for three Moscow Exchange stocks, and a slightly different 44-feature representation for LOBSTER data on three NASDAQ stocks. Data are z-score normalised, and a separate model is trained per stock for 200 epochs on a 60%/20%/20% train/validation/test split.

Benchmarked against the state-of-the-art DeepLOB model on six stocks, TFF-CL-GRU produced a higher F1 score for every stock, with F1 scores of 65% (VTB), 45% (Sberbank), 51% (Gazprom), 49% (Apple), 60% (Amazon) and 55% (Google), versus DeepLOB's 60%, 41%, 46%, 31%, 36% and 38% respectively - an improvement of at least 4 percentage points in every case.

Beyond forecasting accuracy, the paper introduces a new combined LOB-and-order-flow dataset (previously unavailable together in a public benchmark) and tests practical viability with simulated trading: buying or selling whenever the model's predicted probability reaches at least a 90% confidence threshold, with the bid-ask spread as the only trading cost, short sales disallowed, and each simulation's starting balance set to 1000 times the share price. The model-based strategy produced higher median annual returns than a buy-and-hold benchmark for VTB and Gazprom, but not for Sberbank, whose stock was in a sustained decline over the sample and could not be shorted.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are per limit-order-book timestamp (tick-by-tick, sub-second, event-driven rather than fixed-interval), each combined with the order flow since the previous timestamp. The model looks back over the 100 most recent timestamps as input, and its prediction target is the direction of the next price move, classified into three categories: upward, flat, or downward.

## Data

- **Asset class:** Equities
- **Instruments:** Sberbank, VTB, and Gazprom (Moscow Exchange); Apple, Amazon, and Google (NASDAQ, via the LOBSTER dataset)
- **Venue:** Moscow Exchange, collected through the QUIK workstation; NASDAQ, via the existing LOBSTER dataset
- **Period:** Sberbank: 22 to 26 November 2021; VTB: 3 to 17 August 2021; Gazprom: 12 to 20 October 2021; the three NASDAQ stocks: given only as the garbled string '21 June 12' in the text
- **Granularity:** Tick-by-tick order book and order flow data; more than 750,000 timestamps for Sberbank, more than 550,000 for VTB, around 410,000 for Gazprom, around 400,000 for Apple, around 270,000 for Amazon, and around 150,000 for Google; the abstract states the combined dataset has more than 1.5 million records, while a figure caption elsewhere states more than 2 million records

## Features and Measures

- **LOB price/volume features.** Price and volume at the 10 best bid levels and 10 best ask levels of the order book at each timestamp, giving 40 numeric features per snapshot.
- **Order flow features.** Price, volume, and buy/sell direction for the most recent transactions since the previous LOB timestamp: 10 transactions (30 features) in the authors' own dataset, or a single transaction plus an event-type code (4 features) in the LOBSTER dataset.
- **z-score normalisation.** Each feature is rescaled by subtracting its mean and dividing by its standard deviation, chosen because it is less sensitive to the outliers present in the data than min-max or decimal-precision scaling.

## Method

The TFF-CL-GRU network takes a [100, 70] input tensor (or [100, 44] for the LOBSTER data) through nine convolutional layers with 32 filters each and a max-pooling layer, then splits into three parallel convolutional sub-blocks (64 filters each) that are concatenated, reshaped, and passed to a GRU layer with 64 units, ending in a dense softmax layer with three outputs (up, flat, down); PReLU activations are used throughout the convolutional layers. A separate model is trained per stock for 200 epochs on a 60%/20%/20% train/validation/test split, using categorical cross-entropy loss. Performance is judged against the DeepLOB benchmark using accuracy, precision, recall and F1 score, with F1 emphasised because the three price-direction classes are imbalanced. A simple trading simulation then converts model predictions into buy/sell market orders whenever the predicted class probability is at least 90%, banning short sales, charging only the bid-ask spread as a cost, starting each simulation with a balance equal to 1000 times the share price, and comparing the resulting annualised returns (assuming 260 trading days per year) against a buy-and-hold benchmark over one thousand randomly ordered one-day simulations per stock.

## Results

- TFF-CL-GRU outperformed DeepLOB's F1 score for every one of the six stocks tested, by at least 4 percentage points.
- F1 scores for TFF-CL-GRU were 65% (VTB), 45% (Sberbank), 51% (Gazprom), 49% (Apple), 60% (Amazon), and 55% (Google), versus DeepLOB's 60%, 41%, 46%, 31%, 36%, and 38%.
- By training epoch 200, the validation F1 score for DeepLOB on VTB stock barely reached 60%, while TFF-CL-GRU's exceeded it by at least 5 percentage points.
- Trading simulations using TFF-CL-GRU's predictions produced higher median annual returns than buy-and-hold for VTB and Gazprom, but negative returns for Sberbank because that stock was in a declining trend and short sales were prohibited.
- VTB experienced days with price increases exceeding 2%, contributing to unusually high annual returns in its trading simulations.
- Buy-and-hold strategy returns were more volatile across simulations than the model-based strategy's returns.

## Limitations

- Authors state the model's complexity and computational demands need to be addressed before practical real-time trading deployment.
- The trading simulation excludes commissions, forbids short sales, and was not run for Apple, Amazon, or Google because those stocks were in a downward trend for the sample period.
- Reader note: the exchange data covers only a handful of trading days to about two weeks per stock, which may limit how well the reported F1 scores and returns generalise to other periods.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Ilia Zaznov, Julian Martin Kunkel, Atta Badii, Alfonso Dufour (2024). The Intraday Dynamics Predictor: A TrioFlow Fusion of Convolutional Layers and Gated Recurrent Units for High-Frequency Price Movement Forecasting. Applied Sciences (MDPI), volume 14, article 2984.

DOI: 10.3390/app14072984

Text ingested: `markdown_output/zaznov-2024-intraday-dynamics-predictor-trioflow-fusion-convolutional.md`, converted from `raw/ofi-event-clock/zaznov-2024-intraday-dynamics-predictor-trioflow-fusion-convolutional.pdf`.

Coverage of this summary: Read the full paper markdown end to end, including abstract, introduction, preliminaries, prior work, data preparation and model architecture sections, experimental design, results, and conclusion.

Known problems with the input: The paper gives the date for the three NASDAQ (LOBSTER) stocks only as the garbled string '21 June 12' in the text; it is reported as printed rather than guessed at as a specific date; The abstract states the combined dataset has 'over 1.5 million' records, while a figure caption elsewhere states 'over 2 million records'; both figures are reported as printed, not reconciled.
<!-- AUTHORED REGION END -->