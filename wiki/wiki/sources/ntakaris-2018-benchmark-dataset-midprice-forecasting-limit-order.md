---
authors:
- Adamantios Ntakaris
- Martin Magris
- Juho Kanniainen
- Moncef Gabbouj
- Alexandros Iosifidis
content_hash: sha256:ebb929fffcae84c45543ece517fea65e2b61847961700e913315fbb175dbfb9a
created: 2026-09-27 01:47:00+00:00
page_id: sources/ntakaris-2018-benchmark-dataset-midprice-forecasting-limit-order
page_type: source
publication_venue: Journal of Forecasting (preprint)
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/feature-engineering
- concepts/order-flow-prediction
- concepts/mid-price-prediction
- entities/adamantios-ntakaris
- entities/martin-magris
- entities/juho-kanniainen
- entities/moncef-gabbouj
- entities/alexandros-iosifidis
revision_id: 1
schema_version: 2
source_hash: sha256:6776d298848e0088a2245929c9835ad90e1adac81212d3970d3d55c85bbb4094
source_path: markdown_output/ntakaris-2018-benchmark-dataset-midprice-forecasting-limit-order.md
source_type: paper
tags:
- limit-order-book
- benchmark-dataset
- mid-price-prediction
- ridge-regression
- extreme-learning-machine
- nasdaq-nordic
- high-frequency-trading
- clock-event
- asset-equity
- harvest-relevant
title: Benchmark Dataset for Mid-Price Forecasting of Limit Order Book Data with Machine
  Learning Methods
updated: '2026-09-27T01:47:00Z'
uuid: b75607ca-680f-54cd-845b-deac67c840c5
year: 2018
---

<!-- AUTHORED REGION START -->
# Benchmark Dataset for Mid-Price Forecasting of Limit Order Book Data with Machine Learning Methods

## Summary

The paper addresses the lack of public benchmark datasets for machine-learning research on high-frequency limit order book (LOB) data. It releases a large event-based dataset built from the NASDAQ OMX Nordic ITCH feed of the Helsinki Exchange, covering five stocks over ten consecutive trading days, and defines an anchored, day-based cross-validation protocol together with baseline models so future work can be compared on a common footing.

Each observation is an event-based 144-dimensional feature vector, built from ten consecutive order-book events and combining raw ten-level bid/ask price and volume data, features summarizing the recent state of the book, and time-derivative features. Labels describe the direction of the mid-price (up, down, stationary) over five different event-based horizons, using a fixed percentage-change threshold of 0.002. Three normalization schemes (z-score, min-max, decimal precision) are compared, together with two baseline classifiers: a linear ridge regression and a non-linear single-hidden-layer feedforward network (SLFN) whose hidden weights are set by k-means clustering.

Normalization matters much more for the nonlinear model: the SLFN's F1 score rises substantially once features are normalized, while the linear ridge regression benefits far less. Predictive performance also improves as the forecast horizon lengthens, with the longest tested horizon achieving materially higher F1 than the shortest one. Averaged across the two baseline models the authors report an out-of-sample F1 of about 46%.

The contribution is primarily the dataset and evaluation protocol rather than a new model: it is presented as the first publicly released, order-flow-complete LOB dataset built specifically for supervised mid-price-movement prediction, intended as a shared testbed against which the community can compare new methods.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are indexed by order-book events (order submissions, executions, cancellations) rather than wall-clock time; each feature vector aggregates information from ten consecutive events. Prediction targets are defined over the next k events for k in {1, 2, 3, 5, 10}, measuring the percentage change of the mid-price between the current event and the k-th future event, with three-way labels (up/down/stationary) assigned by a fixed percentage-change threshold.

## Data

- **Asset class:** Equities
- **Instruments:** Five NASDAQ OMX Nordic (Helsinki Exchange) stocks: KESBV (Kesko), OUT1V (Outokumpu), SAMPO, RTRKS (Rautaruukki), WRT1V (Wartsila)
- **Venue:** NASDAQ OMX Nordic, Helsinki Stock Exchange
- **Period:** 1 June 2010 to 14 June 2010 (ten consecutive trading days)
- **Granularity:** Millisecond-timestamped order-book events from the ITCH feed; feature vectors built from blocks of ten consecutive events, restricted to the 10:30-18:00 trading window.

## Features and Measures

- **144-dimensional LOB feature vector.** A per-event feature representation combining raw 10-level bid/ask price and volume data, features summarizing the recent state of the order book, and time-derivative features.
- **event-based mid-price label.** A three-class label (up, down, stationary) describing the percentage change of the mid-price between the current event and a future event k steps ahead, assigned using a fixed percentage-change threshold.
- **day-based anchored cross-validation protocol.** An expanding-window evaluation scheme in which the training set grows by one trading day each fold while a single subsequent day is held out for testing, used to benchmark methods on the dataset.

## Method

Two baseline models are fit on the 144-dimensional event representations: a linear ridge regression that maps feature vectors to class-indicator target vectors via a closed-form penalized least-squares solution, and a non-linear single-hidden-layer feedforward network (SLFN) whose hidden-layer weights are obtained by k-means clustering of the training data and whose hidden units use a radial basis function, with output weights fit by least squares. Both models are evaluated on unnormalized data and on three normalization schemes (z-score, min-max, decimal precision), under the anchored day-based cross-validation protocol. Performance is judged mainly by the F1 score, chosen over accuracy because the three mid-price classes are imbalanced, alongside accuracy, precision and recall averaged over folds with their standard deviations.

## Results

- The dataset contains about 4,000,000 order-book events across five NASDAQ Nordic stocks over ten trading days, reduced to 394,337 event-based feature representations.
- For the linear ridge regression on the longest tested horizon, F1 rises from about 40% on raw data to about 43% under z-score normalization, 42% under min-max, and 40% under decimal precision normalization.
- For the nonlinear SLFN on the same horizon, F1 rises from about 33% on raw data to about 46% under z-score normalization and 43% under both min-max and decimal precision normalization.
- Normalization improves the SLFN's F1 score by almost 10 percentage points, a much larger gain than for the linear ridge regression.
- F1 is consistently higher for the longer, five-event-ahead horizon than for the one-event-ahead horizon, for example about 27% versus about 43% under the unfiltered and min-max/decimal-precision setups.
- Ridge regression outperforms the SLFN on raw data and under z-score normalization, but the SLFN matches or exceeds ridge regression under min-max and decimal precision normalization.
- Averaged across both baseline methods, the authors report an out-of-sample F1 of approximately 46%.

## Limitations

- The 144-dimensional feature set does not include information about the sequence of order-flow messages, only aggregated book-state and time-derivative features.
- Reader note: the dataset covers only ten trading days and five stocks from a single exchange (Helsinki), so generalization to other markets, asset classes, or longer periods is untested.
- No trading strategy or economic profitability analysis is provided; the paper restricts itself to machine-learning prediction metrics (accuracy, precision, recall, F1).

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]
- [[entities/adamantios-ntakaris|Adamantios Ntakaris]]
- [[entities/martin-magris|Martin Magris]]
- [[entities/juho-kanniainen|Juho Kanniainen]]
- [[entities/moncef-gabbouj|Moncef Gabbouj]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]

## Citation

Adamantios Ntakaris, Martin Magris, Juho Kanniainen, Moncef Gabbouj, Alexandros Iosifidis (2018). Benchmark Dataset for Mid-Price Forecasting of Limit Order Book Data with Machine Learning Methods. Journal of Forecasting (preprint).

DOI: 10.1002/for.2543

Text ingested: `markdown_output/ntakaris-2018-benchmark-dataset-midprice-forecasting-limit-order.md`, converted from `raw/ofi-event-clock/ntakaris-2018-benchmark-dataset-midprice-forecasting-limit-order.pdf`.

Coverage of this summary: Read the full markdown file: abstract, literature review, dataset description, experimental protocol, baseline models, results tables, conclusion, and reference list.

Known problems with the input: year from file metadata (no publication year printed on this version of the paper; year_hint 2018 from the job file was used).
<!-- AUTHORED REGION END -->