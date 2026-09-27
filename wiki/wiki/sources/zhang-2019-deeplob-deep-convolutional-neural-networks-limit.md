---
authors:
- Zihao Zhang
- Stefan Zohren
- Stephen Roberts
content_hash: sha256:3b03ef68c73aede4fc4007022f31dcc20c051701fbba0c3be1d3d4af87b0c6b2
created: 2026-09-27 01:47:00+00:00
page_id: sources/zhang-2019-deeplob-deep-convolutional-neural-networks-limit
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/high-frequency-data
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/feature-engineering
- concepts/micro-price
- entities/stefan-zohren
revision_id: 1
schema_version: 2
source_hash: sha256:642511663231f9f541e054b1dbd16c469230a0102f5f3d511a9ab14c2ad81f3c
source_path: markdown_output/zhang-2019-deeplob-deep-convolutional-neural-networks-limit.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- cnn-lstm
- price-direction-prediction
- transfer-learning
- market-microstructure
- high-frequency-data
- clock-event
- asset-equity
- harvest-relevant
title: 'DeepLOB: Deep Convolutional Neural Networks for Limit Order Books'
updated: '2026-09-27T01:47:00Z'
uuid: 33887eea-5e88-5060-979f-a369ec392c09
year: 2019
---

<!-- AUTHORED REGION START -->
# DeepLOB: Deep Convolutional Neural Networks for Limit Order Books

## Summary

The paper asks whether a deep network can learn its own features directly from raw limit order book (LOB) data, rather than relying on handcrafted indicators, and whether such features generalise to stocks the network never trained on. Limit order books are treated as a high-dimensional, non-stationary environment where deeper price levels are noisy and hard to summarise with fixed parametric models such as VAR or ARIMA.

The authors' model, DeepLOB, stacks standard convolutional layers, an Inception Module (parallel convolutions of different sizes plus max-pooling, merged together), and an LSTM layer on top of raw price and volume data from the top ten levels of the book. It is trained end to end with categorical cross-entropy to classify each moment as up, down or stationary over a chosen horizon, using labels built by comparing smoothed averages of past and future mid-prices against a threshold. The model is evaluated first on the public FI-2010 benchmark (five Nasdaq Nordic stocks, ten days of data) for direct comparison with prior published methods, and then on a full year of London Stock Exchange (LSE) order book updates for five liquid stocks, with three months held out for testing.

DeepLOB outperforms all the compared baseline methods on FI-2010 by F1 score, and on the LSE data it delivers accuracy that stays fairly stable across the test period and across prediction horizons. Applied without retraining to five further LSE stocks that were never part of training (transfer learning), it achieves accuracy close to that on the training stocks, which the authors read as evidence that the convolutional layers learn features common to price formation across instruments rather than instrument-specific patterns. A simple mid-price trading simulation, ignoring transaction costs, produces statistically significant positive profits.

What is new relative to prior LOB machine-learning work is the combination of an Inception Module with an LSTM trained end to end on raw (not hand-engineered) order book data, the demonstration that the learned features transfer to unseen instruments, and a LIME-based sensitivity analysis used to open up the model and check that its predictions are driven by sensible order-book regions rather than by an opaque 'black box'.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Each input sample is the 100 most recent raw states of the order book (price and volume at the top 10 levels on both sides, 40 features per state), one state per order-book update event rather than per fixed calendar interval; on the LSE data these events arrive irregularly, averaging about 0.192 seconds apart. Labels are built from smoothed mid-price averages: the mean of the previous k mid-prices is compared against the mean of the next k mid-prices (or, for the FI-2010 labels, against the current mid-price), and the percentage change is thresholded to produce up/down/stationary labels for prediction horizons k of 10, 20, 50 or 100 events ahead.

## Data

- **Asset class:** Equities
- **Instruments:** FI-2010 benchmark: five stocks from the Nasdaq Nordic market. LSE dataset: Lloyds Bank, Barclays, Tesco, BT and Vodafone used for training/testing; HSBC, Glencore, Centrica, BP and ITV used only for transfer-learning tests.
- **Venue:** Nasdaq Nordic stock market (FI-2010 dataset); London Stock Exchange (LSE dataset)
- **Period:** FI-2010: 10 consecutive days. LSE: 3rd January 2017 to 24th December 2017, restricted to 08:30:00-16:00:00; first 6 months used for training, next 3 months for validation, last 3 months for testing.
- **Granularity:** Raw order-book updates (event-level), 10 price/volume levels per side (40 features per snapshot); about 150,000 events per day per stock on the LSE data, with an average inter-event time of 0.192 seconds; each model input uses the 100 most recent states.

## Features and Measures

- **Inception Module.** a block that runs several convolution filter sizes (1x1, 3x1, 5x1) and a max-pooling branch in parallel over the same input and concatenates their outputs, so the network can capture patterns over several different numbers of past time steps at once instead of committing to one fixed filter length.
- **strided price/volume convolution (micro-price feature).** a first convolutional layer with filter size and stride (1x2) that combines each order-book level's own price and volume into one feature without mixing information across levels; a second such layer then combines information across levels, and the authors state that the resulting feature maps reproduce the micro-price definition weighted by the bid/ask imbalance.
- **smoothed mid-price direction labels.** up/down/stationary labels built by comparing the mean of the previous k mid-prices against the mean of the next k mid-prices (or against the current mid-price), with the percentage change thresholded by a parameter alpha, used to reduce label noise relative to comparing raw price ticks directly.
- **LIME sensitivity analysis.** a model-agnostic method that locally perturbs a given input and observes how the model's output changes, used here to highlight which price and volume regions of the order book most influenced a given DeepLOB prediction.

## Method

DeepLOB is trained end to end by minimising categorical cross-entropy with the Adam optimiser (learning rate 0.01, epsilon 1), mini-batches of size 32, and early stopping once validation accuracy fails to improve for 20 epochs (about 100 epochs on FI-2010, about 40 on the LSE data); models were built in Keras on a TensorFlow backend and trained on a single NVIDIA Tesla P100 GPU. On FI-2010 the model is compared against prior published methods (including ridge regression, single-layer feedforward networks, LDA/MDA variants, bag-of-features models, and attention-augmented bilinear networks) under two established evaluation setups: an anchored forward day-by-day split, and a fixed 7-day-train/3-day-test split; performance is judged by mean accuracy, precision, recall and F1 score across folds, with F1 treated as the primary metric because the FI-2010 classes are imbalanced.

On the LSE data the same architecture is trained on five stocks and evaluated on a held-out three-month test period, both on those same stocks and, separately, on five stocks never included in training, to test whether learned features transfer across instruments. A simple trading simulation converts the model's up/down/stationary signal into buy/sell/wait actions at the mid-price, closing all positions by the end of each day, and profitability is assessed with boxplots of daily profit and t-statistics on those profits. Finally, LIME is applied to individual predictions to compare which order-book regions DeepLOB versus a baseline CNN treat as influential.

## Results

- On FI-2010 Setup 1 at prediction horizon k=10, DeepLOB reaches an F1 score of 77.66%, versus 72.84% for the next-best compared method (a two-hidden-layer attention-augmented bilinear network).
- On FI-2010 Setup 2 at k=10, DeepLOB reaches an F1 score of 83.40%, versus 77.63% for the same next-best method.
- DeepLOB uses about 60,000 parameters (60k in the paper's parameter-count table), far fewer than the 768k parameters used by the compared CNN-I baseline, though its forward pass takes 0.253 milliseconds versus 0.025 milliseconds for CNN-I.
- On the LSE test stocks used in training, mean prediction accuracy is 70.17% at k=20, 63.93% at k=50 and 61.52% at k=100.
- On five LSE stocks excluded from training (transfer learning), accuracy is 68.62% at k=20, 63.44% at k=50 and 61.46% at k=100, close to the accuracy on the training stocks.
- The LSE dataset contains more than 134 million samples over 12 months, with about 150,000 events per day per stock and an average inter-event time of 0.192 seconds.
- A simple mid-price trading simulation without transaction costs produces consistently positive cumulative profits and significant t-statistics across stocks and prediction horizons over the three-month test period.
- LIME analysis shows most components of the order-book input are inactive (uninformative) for the CNN-I baseline, which the authors attribute to its use of large first-layer filters and max-pooling.

## Limitations

- The FI-2010 benchmark used for head-to-head comparison with prior methods covers only 10 consecutive days from a less liquid market, which the authors themselves say is not enough to fully verify robustness.
- The trading simulation assumes execution at the mid-price with one share per trade and no transaction costs, which the authors describe as not a realistic standalone strategy, only a relative comparison metric.
- Testing is confined to cash equities (Nasdaq Nordic and London Stock Exchange stocks); no other asset class is evaluated.
- Reader note: the paper's own header shows placeholder journal/volume information rather than a stated publication venue, so venue could not be extracted from the text.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/micro-price|Micro-Price]]
- [[entities/stefan-zohren|Stefan Zohren]]

## Citation

Zihao Zhang, Stefan Zohren, Stephen Roberts (2019). DeepLOB: Deep Convolutional Neural Networks for Limit Order Books.

DOI: 10.1109/tsp.2019.2907260

Text ingested: `markdown_output/zhang-2019-deeplob-deep-convolutional-neural-networks-limit.md`, converted from `raw/ofi-event-clock/zhang-2019-deeplob-deep-convolutional-neural-networks-limit.pdf`.

Coverage of this summary: Read the abstract, introduction, related work, the full data/normalisation/labelling section, the full model architecture section, the full experimental results section (FI-2010 setups, LSE results, trading simulation, sensitivity analysis) and the conclusion; the reference list was skimmed only for citation context.

Known problems with the input: The paper's visible header text ('JOURNAL OF LATEX CLASS FILES, VOL. XX, NO. XX, XXX') is placeholder formatting, not an actual venue/volume; venue was left empty rather than guessed; No explicit publication year is printed in the body text read; year was set to 2019 from the job's year_hint.
<!-- AUTHORED REGION END -->