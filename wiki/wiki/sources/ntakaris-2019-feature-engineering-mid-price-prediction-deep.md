---
authors:
- Adamantios Ntakaris
- Giorgio Mirone
- Juho Kanniainen
- Moncef Gabbouj
- Alexandros Iosifidis
content_hash: sha256:b9194b109feb9c35d4deb1b23331deb21b6cbbf478169408ebd362a69094b866
created: 2026-09-27 01:47:00+00:00
page_id: sources/ntakaris-2019-feature-engineering-mid-price-prediction-deep
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/feature-engineering
- concepts/high-frequency-trading
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/market-microstructure-noise
- concepts/order-imbalance
- entities/adamantios-ntakaris
- entities/juho-kanniainen
- entities/moncef-gabbouj
- entities/alexandros-iosifidis
revision_id: 1
schema_version: 2
source_hash: sha256:630b2f47646781ceb8a7d002a7df50a7c0f61ad3c592077f2f3694d779ee569f
source_path: markdown_output/ntakaris-2019-feature-engineering-mid-price-prediction-deep.md
source_type: paper
tags:
- mid-price-prediction
- limit-order-book
- deep-learning
- feature-engineering
- econometrics
- high-frequency-trading
- lstm
- multi-objective-learning
- clock-event
- asset-equity
- harvest-core
title: Feature Engineering for Mid-Price Prediction with Deep Learning
updated: '2026-09-27T01:47:00Z'
uuid: cbb9c522-e46e-5e80-bed0-f488a7903c11
year: 2019
---

<!-- AUTHORED REGION START -->
# Feature Engineering for Mid-Price Prediction with Deep Learning

## Summary

The paper asks whether handcrafted features drawn from financial econometrics can improve deep-learning based prediction of limit order book mid-price movements, compared with two existing handcrafted feature sets from the literature and with features extracted automatically by an LSTM autoencoder. It builds an extensive econometric feature list split into statistical, volatility, noise/uncertainty and price-discovery categories, computed from message-book and limit-order-book data, and feeds each feature set into nine deep learning architectures (five MLPs, two CNNs, two LSTMs, one of the LSTMs with an attention layer).

Two experimental protocols are used. Protocol I, introduced for the first time in this paper, extracts a feature representation for every next order book event using a rolling 10-event window with overlap, and treats mid-price forecasting as a joint problem: classifying the direction of the next mid-price change and predicting the number of events until it occurs, with zero lag. Protocol II, adapted from earlier work, instead builds independent 10-event blocks and casts mid-price movement as a three-class (up, down, stationary) classification problem with a 10-event lag.

Experiments use two TotalView-ITCH datasets: Amazon and Google for the US market and five Nordic stocks (Kesko Oyj, Outokumpu Oyj, Sampo Oyj, Rautaruukki, Wartsila Oyj), each spanning ten business days, with roughly 13,000,000 events in the US dataset and 4,000,000 in the Nordic dataset. Across both protocols, and both balanced and unbalanced label sets, the three handcrafted feature sets (the new econometric set, a technical/quantitative set, and a time-sensitive/insensitive LOB set) consistently beat the features taken from the fully automated LSTM autoencoder.

The authors present their econometric feature list as the first of its kind built specifically for LOB mid-price prediction, and present Protocol I as a reusable, event-driven labeling scheme that keeps every trading event rather than discarding information at a fixed lag, at the cost of requiring per-event online prediction.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Protocol I extracts a new feature representation at every single order book event, using a rolling 10-event window with an overlap of nine events between consecutive representations, and predicts both the direction of the next mid-price change and the number of events until it occurs, with zero lag. Protocol II instead partitions the event stream into independent, non-overlapping 10-event blocks and predicts a three-class (up, down, stationary) mid-price movement label with a 10-event lag between blocks. Both protocols are event-driven rather than calendar-time sampled, so there are no missing values.

## Data

- **Asset class:** Equities
- **Instruments:** Amazon, Google (US); Kesko Oyj, Outokumpu Oyj, Sampo Oyj, Rautaruukki, Wartsila Oyj (Nordic)
- **Venue:** not stated
- **Period:** US: 22.09.15 to 05.10.15; Nordic: 01.06.10 to 14.06.10 (ten business days each)
- **Granularity:** Millisecond timestamps from TotalView-ITCH message books converted into limit order books of depth 10 on both sides; feature representations sampled every event (Protocol I) or in independent 10-event blocks (Protocol II).

## Features and Measures

- **Mid-Price.** The average of the best bid and best ask price at the top of the limit order book; its movement is the quantity the paper tries to forecast.
- **Financial Duration.** The time elapsed between consecutive order book events, used as a statistical feature capturing trading-activity intensity.
- **Realized Volatility.** A volatility-measure feature built from squared log-returns that serves as a natural estimator of the price process's quadratic variation.
- **Realized Bipower Variation.** A volatility-measure feature that isolates the continuous (diffusive) part of price variation from the jump component.
- **Realized Quarticity.** A noise/uncertainty-measure feature (with tripower and quadpower variants) estimating the integrated quarticity, i.e. the degree of estimation error in realized variance, over a fixed window of events.
- **Weighted Mid-Price by Order Imbalance.** A price-discovery feature that adjusts the mid-price using the imbalance between bid- and ask-side order book volumes.
- **Volume Imbalance.** A price-discovery feature measuring the relative difference between bid-side and ask-side volumes posted in the order book.
- **Normalized Bid-Ask Spread.** The bid-ask spread expressed as a number of ticks between the best bid and best ask price.

## Method

Nine deep learning models are trained independently for each protocol: five multilayer perceptrons (MLP) with up to three hidden layers and varying node counts and dropout, two convolutional neural networks (one adapted from prior work, one from a grid search over filter counts, kernel sizes and dropout), and two LSTM networks (one adapted from prior work, one augmented with an attention layer). All models are trained with the Nadam optimizer (Nesterov-accelerated Adam) via reverse-mode automatic differentiation (backpropagation), for 250 epochs with a 0.2 validation split, using dropout for regularization. For Protocol I the loss combines binary cross-entropy for the direction classification with mean squared error for the event-count regression; Protocol II uses categorical cross-entropy for its three-class output. A separate LSTM autoencoder, chosen via a grid search over encoder/decoder depth and latent-representation size, is trained to produce a fully automated feature set for comparison against the three handcrafted sets. Performance is judged by f1 score for classification and RMSE for regression, computed separately on unbalanced data and on data balanced by random undersampling of the majority class, and reported per stock as well as for a pooled ('Joint') case per market.

## Results

- Handcrafted econometric features combined with a shallow MLP under Protocol I let the model react to mid-price direction changes within a single millisecond for Amazon and the pooled US case; the paper notes about 30% of US trades and 36% of Nordic trades share the same millisecond timestamp.
- For the pooled ('Joint') US case under Protocol I, the attention-based LSTM2 model reached an f1 score of 59% with an RMSE of 89.69.
- For the pooled Nordic case under Protocol I, MLP3 gave the best f1 scores of 53% (unbalanced) and 56% (balanced) under the Econ and Tech-Quant feature sets respectively, though its regression RMSE stayed above 165.29.
- Under Protocol II, the best pooled-case classification score was 65% f1 for the US dataset (MLP4, Tech-Quant feature set, balanced) versus 51% f1 for the Nordic dataset (MLP4, Tech-Quant, unbalanced).
- Across both protocols, the three handcrafted feature sets (Econ, Tech-Quant, LOB) outperformed features taken from the fully automated LSTM autoencoder.
- Before undersampling, Protocol I mid-price direction labels split 47%/53% down/up for the US dataset and 45%/55% for the Nordic dataset; undersampling then reduced the data by 90% and 85% respectively.

## Limitations

- The authors note LOB data is exposed to a bid-ask bounce effect that may inject bias, and leave this for future research.
- The evaluation is limited to two US and five Nordic stocks over ten business days each; the authors explicitly leave extension to wider LOB datasets for future work.
- The LSTM autoencoder grid search was limited to at most four hidden layers for the encoder and decoder, which the authors say leaves further analysis of the fully automated approach open.
- Reader note: each market is covered by a single ten-business-day window, so results may not generalize across different volatility or liquidity regimes.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/order-imbalance|order imbalance]]
- [[entities/adamantios-ntakaris|Adamantios Ntakaris]]
- [[entities/juho-kanniainen|Juho Kanniainen]]
- [[entities/moncef-gabbouj|Moncef Gabbouj]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]

## Citation

Adamantios Ntakaris, Giorgio Mirone, Juho Kanniainen, Moncef Gabbouj, Alexandros Iosifidis (2019). Feature Engineering for Mid-Price Prediction with Deep Learning.

DOI: 10.1109/access.2019.2924353

Text ingested: `markdown_output/ntakaris-2019-feature-engineering-mid-price-prediction-deep.md`, converted from `raw/ofi-event-clock/ntakaris-2019-feature-engineering-mid-price-prediction-deep.pdf`.

Coverage of this summary: Read the full markdown file: abstract, introduction, literature review, problem statement, the handcrafted feature pool section, all deep learning method subsections (MLP, CNN, LSTM, LSTM autoencoder), the data description and both experimental protocols, the results and discussion section, the conclusion, and the feature-definition appendix (A.1-A.4); the remaining pages are repetitive per-stock/per-model score tables (Appendix B, Protocol II) whose headline figures are already covered by the Results and Discussion text.

Known problems with the input: year from file metadata.
<!-- AUTHORED REGION END -->