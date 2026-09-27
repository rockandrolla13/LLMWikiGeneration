---
authors:
- Dat Thanh Tran
- Juho Kanniainen
- Moncef Gabbouj
- Alexandros Iosifidis
content_hash: sha256:11fe295f730fab7cfe10901d51a53ae947fd00acd6982afbda041d084e30f40b
created: 2026-09-27 01:47:00+00:00
page_id: sources/tran-2021-data-normalization-bilinear-structures-high-frequency
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/feature-engineering
- concepts/high-frequency-data
- entities/dat-thanh-tran
- entities/juho-kanniainen
- entities/moncef-gabbouj
- entities/alexandros-iosifidis
revision_id: 1
schema_version: 2
source_hash: sha256:3e5aea6995adb44f8aee7658f8d6bec8a886d35ea70d009196e39272fb967714
source_path: markdown_output/tran-2021-data-normalization-bilinear-structures-high-frequency.md
source_type: paper
tags:
- limit-order-book
- normalization
- deep-learning
- bilinear-network
- mid-price-prediction
- high-frequency-data
- clock-event
- asset-equity
- harvest-relevant
title: Data Normalization for Bilinear Structures in High-Frequency Financial Time-series
updated: '2026-09-27T01:47:00Z'
uuid: 8995c22e-9ec3-593c-bf17-008ee501e14a
year: 2021
---

<!-- AUTHORED REGION START -->
# Data Normalization for Bilinear Structures in High-Frequency Financial Time-series

## Summary

The paper asks how to normalize noisy, non-stationary, multi-modal financial time series so that TABL networks - which model temporal and feature dependencies with two separate bilinear projections rather than a single flattened input - can learn effectively, arguing that existing schemes such as batch normalization and Deep Adaptive Input Normalization (DAIN) only normalize along the temporal axis and ignore the feature-axis non-stationarity that bilinear projections are also sensitive to.

The proposed Bilinear Normalization (BiN) layer computes the mean and standard deviation of each input sample along both the temporal dimension and the feature dimension, standardises the sample along each axis separately using learnable scale and shift parameters, and then combines the two standardised views using two learnable non-negative weights that let the network decide how much weight to give each axis.

BiN is tested by inserting it as an input layer into two existing TABL architectures, B(TABL) (one hidden layer) and C(TABL) (two hidden layers), on the FI-2010 limit order book benchmark - Level-II data from 5 Finnish stocks over 10 trading days, split into the first 7 days for training and the last 3 for evaluation - predicting the direction of the mid-price after H = 10, 20, or 50 future events. BiN-C(TABL) beat the unnormalized C(TABL) at every horizon tested, with the largest gain at H = 50, where average F1 rose from 78.44% to 88.06%.

Compared with the state-of-the-art DeepLOB (an 11-hidden-layer CNN-LSTM), BiN lets a much smaller 2-hidden-layer TABL network close most of the gap at short horizons and overtake DeepLOB outright at the longest horizon tested, while adding very few extra parameters - the smaller B(TABL) network gains only 102 extra parameters from BiN yet matches the larger BiN-C(TABL) network's performance at every horizon.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Each input sample is a matrix built from the 10 most recent limit order book snapshots (price and volume at the 10 best bid and 10 best ask levels, 40 features per snapshot), where a new snapshot is recorded after order-book events such as placements, executions, and cancellations rather than at fixed time intervals. The prediction target is the direction of the mid-price after a fixed number of future events - the prediction horizon H, set to 10, 20, or 50 - with a separate model trained for each horizon value.

## Data

- **Asset class:** Equities
- **Instruments:** 5 stocks traded on the Helsinki Exchange (the FI-2010 benchmark dataset)
- **Venue:** Helsinki Exchange (operated by NASDAQ Nordic)
- **Period:** 10 business days total; first 7 days used for training and the last 3 for evaluation
- **Granularity:** Level-II order book snapshots recorded per event; top 10 price levels per side, giving a 40-dimensional feature vector per snapshot; each input sample uses the 10 most recent snapshots (a 40x10 matrix); more than 4 million order events in total

## Features and Measures

- **Bilinear Normalization (BiN).** A learnable normalization layer that computes and applies separate mean/standard-deviation standardisation along a sample's temporal axis and its feature axis, then blends the two standardised versions using two learnable non-negative weights, tailored for networks that use bilinear (time-and-feature) projections.
- **TABL bilinear projection.** A network layer that models a multivariate time series with two separate learned linear projections, one along the temporal axis and one along the feature axis, instead of flattening the input into a single vector before a dense layer.

## Method

BiN is inserted as the input layer of two existing TABL architectures: B(TABL), a one-hidden-layer network with 5843 parameters, and C(TABL), a two-hidden-layer network with 11343 parameters. Models are trained for 80 epochs with the Adam optimizer, a learning rate schedule starting at 1e-3 and dropping to 1e-4 at epoch 11 and 1e-5 at epoch 71, weight decay of 1e-3 or a max-norm constraint of 10.0, and dropout of 0.1 after each hidden layer. Because the FI-2010 mid-price movement classes are imbalanced, a weighted cross-entropy loss is used, and each experiment is repeated 5 times with the median accuracy, precision, recall and F1 reported. BiN is compared against the unnormalized TABL baseline and against Batch Normalization (BN), DAIN-MLP, and DAIN-RNN as alternative input normalization schemes, and, separately, against the deeper DeepLOB benchmark, across prediction horizons H = 10, 20 and 50.

## Results

- BiN-C(TABL) beat the unnormalized C(TABL) at every prediction horizon tested (H = 10, 20, 50).
- At H = 50, BiN raised C(TABL)'s average F1 from 78.44% to 88.06%, roughly a 10-percentage-point gain.
- At H = 10, BiN-C(TABL) reached F1 81.04% versus DeepLOB's 83.40%; at H = 20, 71.22% versus DeepLOB's 72.82%; at H = 50, BiN-C(TABL) exceeded DeepLOB, 88.06% versus 80.35%.
- Adding standard Batch Normalization to C(TABL) instead hurt performance - for H = 10, average F1 dropped from 77.63% (unnormalized C(TABL)) to 66.87% (BN-C(TABL)).
- A smaller, one-hidden-layer BiN-B(TABL) network matched BiN-C(TABL)'s performance at every horizon despite adding only 102 parameters versus C(TABL)'s 11343.
- Applying BiN to every hidden layer instead of only the input layer made almost no further difference - for example at H = 10, BiN-C(TABL) scored 81.04% F1 versus 81.03% when BiN was also applied to hidden layers.

## Limitations

- Reader note: evaluated only on the FI-2010 benchmark (5 Finnish equities, 10 trading days), so generalisation to other markets or asset classes is untested in the paper.
- Reader note: BiN is only tested inside TABL-family architectures (B(TABL) and C(TABL)); the paper does not test it with other network types such as CNNs or plain RNNs.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/high-frequency-data|high frequency data]]
- [[entities/dat-thanh-tran|Dat Thanh Tran]]
- [[entities/juho-kanniainen|Juho Kanniainen]]
- [[entities/moncef-gabbouj|Moncef Gabbouj]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]

## Citation

Dat Thanh Tran, Juho Kanniainen, Moncef Gabbouj, Alexandros Iosifidis (2021). Data Normalization for Bilinear Structures in High-Frequency Financial Time-series.

DOI: 10.1109/icpr48806.2021.9412547

Text ingested: `markdown_output/tran-2021-data-normalization-bilinear-structures-high-frequency.md`, converted from `raw/ofi-event-clock/tran-2021-data-normalization-bilinear-structures-high-frequency.pdf`.

Coverage of this summary: Read the full paper markdown end to end: introduction, related work on normalization schemes, the BiN formulation, and the FI-2010 experimental setup and results (all three tables).

Known problems with the input: No publication year or venue is printed anywhere in the paper text; the job file's year_hint (2021) was used for year, and venue is left blank.
<!-- AUTHORED REGION END -->