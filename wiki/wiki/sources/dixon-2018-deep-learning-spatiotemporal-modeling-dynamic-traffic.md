---
authors:
- Matthew F. Dixon
- Nicholas G. Polson
- Vadim O. Sokolov
content_hash: sha256:74a21a10178313efd99c187d9014a52890a00e78113131ca252f7ecc05726d05
created: 2026-09-27 01:47:00+00:00
page_id: sources/dixon-2018-deep-learning-spatiotemporal-modeling-dynamic-traffic
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/deep-learning-for-finance
- concepts/recurrent-neural-networks
- concepts/lstm-networks
- concepts/order-flow-prediction
- concepts/feature-engineering
revision_id: 1
schema_version: 2
source_hash: sha256:1045931c87e91d147576ad4187371761a249642e72e65b70bd749094edb1038e
source_path: markdown_output/dixon-2018-deep-learning-spatiotemporal-modeling-dynamic-traffic.md
source_type: paper
tags:
- high-frequency-trading
- deep-learning
- limit-order-book
- futures
- spatio-temporal-modeling
- recurrent-neural-networks
- clock-event
- asset-futures
- harvest-relevant
title: 'Deep Learning for Spatio-Temporal Modeling: Dynamic Traffic Flows and High
  Frequency Trading'
updated: '2026-09-27T01:47:00Z'
uuid: 3879d3df-b307-5e13-a1b9-093bf30c5153
year: 2018
---

<!-- AUTHORED REGION START -->
# Deep Learning for Spatio-Temporal Modeling: Dynamic Traffic Flows and High Frequency Trading

## Summary

The paper's question is whether deep, layered nonlinear predictors can capture the sharp regime changes (traffic breakdown-to-recovery, sudden price moves) that arise in spatio-temporal data but are hard for traditional physical or linear time-series models to reproduce. It motivates deep learning as a nonparametric, algorithmic alternative built from layers of univariate 'semi-affine' functions, trained by stochastic gradient descent with dropout for regularisation and implicit variable selection.

The same underlying spatio-temporal predictor is cast two ways: a feed-forward network that embeds lagged inputs directly into the input vector, and a recurrent/LSTM network that instead carries a hidden state across time steps. Both are applied to two very different problems: five-minute average speed data from 21 loop detectors along a 13-mile stretch of Chicago's Interstate I-55, comparing deep learning against a sparse vector-autoregression under several pre-filtering choices; and nanosecond-timestamped CME E-mini S&P 500 futures order-book updates, where the relative depth ('book pressure') across quoted price levels feeds a classifier for the direction of the next tick's mid-price move.

For the traffic application, deep learning combined with median-filtered inputs gives the best out-of-sample fit among the model/pre-processing combinations tried, though unfiltered deep learning underperforms even a naive forecast. For the futures application, the deep classifier substantially outperforms an elastic-net-only benchmark on both accuracy and per-class F1 score, and its bias-variance trade-off (via learning curves) improves as the training set grows.

What is new is treating the recurrent/LSTM cell as an automatic, non-parametric analogue of a nonlinear vector autoregression, applied consistently to a physical (traffic) and a financial (limit order book) domain, together with practical discussion of the trade-off between 'clocking' (fixed-interval undersampling of event data) and using every raw event, and of the severe class imbalance in tick-level price-direction labels.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

The futures application samples the limit order book at every book-update message (nanosecond timestamps) rather than on a fixed calendar grid; the response is the discrete mid-price change from the current update to h updates ahead, with h set to 1 (the very next book event) in the main experiment. The paper separately discusses an alternative 'clocking' approach that undersamples events at regular intervals, but reports that clocking the data reduced predictive power because of the severe class imbalance, so the reported results use the unclocked, per-event data with over/under-sampling to rebalance classes instead.

## Data

- **Asset class:** Futures
- **Instruments:** CME E-mini S&P 500 (ES) futures, specifically the ESU6 contract; a separate non-financial application uses average-speed data from 21 loop detectors along a 13-mile stretch of Interstate I-55 near Chicago.
- **Venue:** Chicago Mercantile Exchange (CME) FIX message feed for the futures data; Illinois Department of Transportation / Argonne National Laboratory sensor archive for the traffic data.
- **Period:** CME ES data: August 1, 2016 to August 31, 2016, between 12:00pm and 22:00 UTC each day. Traffic data: five-minute records archived since 2008, with training and test sets drawn from two separate contiguous 90-day windows in 2013.
- **Granularity:** Nanosecond-timestamped limit-order-book update messages recording price and depth for up to 10 quoted levels on each side of the market for the futures data, aggregated into a balanced training set of 298,062 observations of 440 lagged relative-depth-imbalance variables; five-minute average speed/flow/occupancy readings for the traffic data.

## Features and Measures

- **Relative depth imbalance (book pressure).** The normalized quoted depth at each price level on the bid and ask sides of the order book, treated as a feature vector; the paper argues that the cross-section of these imbalances, not just the best bid and ask, drives short-term mid-price moves.
- **Feed-forward deep predictor with embedded lags.** A multi-layer feed-forward network in which past observations are stacked directly into the input vector, so the input-layer weight matrix grows with the number of lags used.
- **Recurrent/LSTM spatio-temporal predictor.** A recurrent architecture that represents the lag structure implicitly through a hidden state carried across time steps, framed by the authors as a non-parametric analogue of a nonlinear vector autoregression.
- **Clocking (fixed-interval undersampling).** Resampling event-driven order-book or sensor data onto a regular time grid to reduce class imbalance or dimensionality, at the cost of losing some of the finest-grained events.

## Method

The predictor is built as a stack of univariate 'semi-affine' layers (weight matrices, offsets and an activation function) composed into either a feed-forward network or, when the time dimension is instead represented by a carried hidden state, a recurrent/LSTM network. Both are trained by stochastic gradient descent (with momentum, AdaGrad/RMSprop or Adam-style variants discussed) on a penalized loss, with dropout used for regularisation and implicit variable selection; network depth, layer width and activation choice are tuned by random or grid search using out-of-sample error on a held-out validation set.

For the traffic application, a sparse vector-autoregression / lasso or elastic-net stage first screens which sensors and lags matter, and the surviving predictors feed a four-layer feed-forward network trained on the H2O platform; performance is judged by in-sample and out-of-sample mean squared error and R-squared against the sparse linear model, with and without median or trend pre-filtering of the raw speed series.

For the futures application, relative depth imbalances across price levels and lags are first screened by an elastic-net model, and the surviving variables feed a five-layer feed-forward network with a softmax output, trained via TensorFlow's SGD to classify the next book update's mid-price move as up, flat or down; because the great majority of raw observations are flat, the training set is rebalanced by over- and under-sampling, and performance is judged out-of-sample by classification accuracy, per-class F1 score, ROC curves and learning curves, against an elastic-net-only benchmark.

## Results

- Comparing seven traffic-flow model/pre-processing combinations, deep learning combined with median-filter pre-processing had the best out-of-sample fit, with out-of-sample R-squared ranging from 0.74 up to 0.85 across the combinations tested.
- Deep learning applied to unfiltered traffic data, combined with a sparse linear estimator, performed worse than a naive forecast, showing that pre-filtering mattered more than model choice alone.
- For the E-mini S&P 500 futures classification task, the elastic-net benchmark reached 49.6% out-of-sample accuracy for the next book-update's mid-price direction, versus 81.7% for the deep learner built on the same elastic-net-selected features.
- The deep learner's F1 scores for down-tick, flat and up-tick classes were 0.201, 0.897 and 0.186 respectively, each higher than the elastic-net model's 0.116, 0.649 and 0.108.
- The balanced training set for the futures classifier held 298,062 observations of 440 relative-depth-imbalance variables, built to counter a raw class imbalance in which about 99.9% of observations had a zero mid-price response.
- Learning curves showed the gap between in-sample and out-of-sample F1 scores shrinking as the training-set size grew, which the authors read as evidence the deep classifier was not overfitting.
- Grid-search over the traffic-flow network's structure and hyper-parameters took a total wall-clock time of 138 days.

## Limitations

- The futures classification results rest on a single instrument (ES futures) and a single one-month sample; Reader note: this limits how far the accuracy and F1 figures can be expected to generalize across instruments or regimes.
- The authors describe deep learning models as hard to interpret ('black boxes'), time-consuming to build with ad-hoc steps, and not always amenable to standard statistical inference because of the nesting of layers.
- The traffic-flow comparison is drawn from a single 13-mile highway corridor and specific non-recurrent events (a football game, a snow day); Reader note: a short, location-specific sample of this kind may not generalize to other roads or conditions.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/feature-engineering|feature engineering]]

## Citation

Matthew F. Dixon, Nicholas G. Polson, Vadim O. Sokolov (2018). Deep Learning for Spatio-Temporal Modeling: Dynamic Traffic Flows and High Frequency Trading.

DOI: 10.1002/asmb.2399

Text ingested: `markdown_output/dixon-2018-deep-learning-spatiotemporal-modeling-dynamic-traffic.md`, converted from `raw/ofi-event-clock/dixon-2018-deep-learning-spatiotemporal-modeling-dynamic-traffic.pdf`.

Coverage of this summary: Read the entire converted markdown file front to back, including both applications (traffic-flow and futures), the deep-learning background section, results tables, the discussion, and the training/SGD appendix.

Known problems with the input: Several equations and figures (the layer-composition formula, SGD/momentum/Adam update rules, network diagrams) are rendered as omitted images in this conversion, so exact functional forms could only be checked against the surrounding prose; No explicit publication venue (journal or conference) is printed in the document; only a working-paper-style date (May 7, 2018) is given.
<!-- AUTHORED REGION END -->