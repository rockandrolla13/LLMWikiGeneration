---
authors:
- Enrique Martínez Miranda
- Steve Phelps
- Matthew J. Howard
content_hash: sha256:aa3066a6ab4e92b51c636cf8a5531f753df08da36d580ea9f80263a6521d78aa
created: 2026-09-27 01:47:00+00:00
page_id: sources/miranda-2019-order-flow-dynamics-prediction-order-cancelation
page_type: source
publication_venue: High Frequency
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/order-flow
- concepts/order-flow-prediction
- concepts/market-microstructure
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/feature-engineering
- concepts/adverse-selection
revision_id: 1
schema_version: 2
source_hash: sha256:db269cdb16f554a8f46b52789ded43d19f648aea60fbed4193f9fe92af2f493d
source_path: markdown_output/miranda-2019-order-flow-dynamics-prediction-order-cancelation.md
source_type: paper
tags:
- spoofing
- market-manipulation
- limit-order-book
- svm
- event-time
- order-cancelation
- london-stock-exchange
- classification
- clock-event
- asset-equity
- harvest-core
title: Order flow dynamics for prediction of order cancelation and applications to
  detect market manipulation
updated: '2026-09-27T01:47:00Z'
uuid: 8fdd587f-5776-5141-8512-7910d0e7c9b2
year: 2019
---

<!-- AUTHORED REGION START -->
# Order flow dynamics for prediction of order cancelation and applications to detect market manipulation

## Summary

Can the state of the limit order book (LOB) reveal that a large order in progress is likely to be canceled rather than filled, and can it be used to predict ahead of time when a still-active large order will be canceled? The authors are motivated by spoofing and related manipulation strategies, where a trader submits a large non-bona-fide order to move the price and then cancels it before it can be executed.

Using reconstructed LOBs (up to 200 price levels) built from London Stock Exchange trade-and-quote data for Barclays and British Petroleum (BP), the authors define an event-time window around each large order and represent the LOB state over that window as a matrix of aggregated volumes at each price level, vectorized into a feature vector. A support vector machine with an RBF kernel is trained as a binary classifier separating canceled large orders from filled ones, for two tasks: a detection task, where the cancelation event falls inside the modeled window, and a prediction task, where the cancelation is still to occur outside the window. Additional engineered features describing recent volume imbalance, price trend, and submission depth are also tested. Window sizes are chosen from the empirical distribution of cancelation durations rather than picked arbitrarily.

Microstructure-level LOB features, together with the added engineered features, produced the most accurate and self-consistent classification for both detecting and predicting cancelations, outperforming two macro-level feature baselines drawn from earlier manipulation-detection studies. Detection (which includes the cancelation event in the window) marginally outperformed prediction (which excludes it). The best window size differed by stock, and accuracy degraded as the window size grew. Under stressed 2008 market conditions, SVM accuracy fell and AdaBoost performed better than the SVM.

The main contribution is the use of fully reconstructed, high-resolution LOB microstructure data, rather than the daily or macro summary statistics used in earlier manipulation-detection work, to both detect and predict ahead of time the cancelation of a large order, framed as an event-time-windowed binary classification problem with a data-driven procedure for selecting the window size.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are sampled in event time: each order-flow event (submission, cancelation, amendment, or execution) recorded in the reconstructed LOB advances the clock by one step, rather than a fixed calendar interval. The window size tT is chosen from the empirical distribution of event-time durations of large-order cancelations. Detection uses the window [t0', tT], which includes the cancelation event; prediction uses the window (tT, tTmax], which excludes the cancelation and must forecast whether it will occur in that later interval.

## Data

- **Asset class:** Equities
- **Instruments:** Barclays PLC and British Petroleum (BP) PLC, both listed on the London Stock Exchange
- **Venue:** London Stock Exchange (LSE)
- **Period:** September to December 2007 for Barclays and BP; January to May 2008 additionally for BP
- **Granularity:** Full order-by-order TAQ (trade and quote) event data used to reconstruct the LOB up to 200 price levels; the minimum time resolution in the data is 1 second

## Features and Measures

- **Dominant imbalance (full/partial LOB).** An indicator feature showing whether the volume imbalance over the last n events was dominated by the same side as the newly submitted large order.
- **Price trend.** An indicator (up, none, or down) of the recent mid-price trend over the n events preceding submission of the large order.
- **Submission depth.** A real-valued feature recording how many price levels away from the best quote the large order was submitted.
- **LOB state matrix.** A matrix of aggregated volumes at each price level around the mid-price over the chosen event-time window, vectorized to form the input to the SVM.

## Method

The problem is formulated as binary classification: canceled large orders are labeled 1 and filled large orders labeled 0. An SVM with a Gaussian RBF kernel is trained (C = 1.947994, sigma = 2.925576), using five-fold cross-validation and data rebalanced to an equal split between the two classes. The SVM is compared against two macro-feature baselines reconstructed from prior published manipulation-detection studies, and, in an appendix, against Decision Trees, k-Nearest Neighbours, Naive Bayes, AdaBoost, and Random Forests. Performance is judged by the area under the ROC curve (AUC) and the F2 score, averaged over k = 10 repeated random subsamples per window-size bin so that each bin contributes the same number of data points.

## Results

- Using microstructure-level LOB data plus the additional engineered features gave the most accurate and self-consistent classification for both detecting and predicting cancelations, beating two macro-feature baselines for both stocks.
- For Barclays, the best detection window was [7, 30] event-time units, with F2 above about 0.85 and AUC above about 0.95; accuracy declined as the window size grew toward 122 events.
- For BP, the best detection window was [24, 44] events; even the widest tested window, [104, 124], still performed comparably to the best Barclays window.
- The best window size for the prediction task matched the best detection window for each stock: tT = 30 for Barclays and tT = 44 for BP.
- Detection (which includes the cancelation event in the window) marginally outperformed prediction (which excludes it) for both stocks.
- In the sample, Barclays had 10,043 canceled and 9,649 filled large buy orders, and BP had 25,257 canceled and 9,269 filled large buy orders.
- Under 2008 crisis-period data for BP, SVM accuracy fell relative to 2007, AdaBoost outperformed the SVM, and AdaBoost's accuracy rose (rather than fell) as the window size grew.

## Limitations

- The authors describe the TAQ data (2007-2008, 1-second minimum resolution) as "old" relative to present-day markets with millisecond- or faster-scale activity.
- The data lack individual trader account identifiers, so a canceled order cannot be definitively tied to manipulative intent versus an ordinary change of mind.
- The analysis is restricted to buy-side large orders in two stocks (Barclays and BP); the sell side and a broader universe of stocks are not tested.
- Reader note: the optimal window size is stock-specific rather than universal, and the study demonstrates a classification methodology rather than a validated real-world manipulation detector.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/adverse-selection|adverse selection]]

## Citation

Enrique Martínez Miranda, Steve Phelps, Matthew J. Howard (2019). Order flow dynamics for prediction of order cancelation and applications to detect market manipulation. High Frequency.

DOI: 10.1002/hf2.10026

Text ingested: `markdown_output/miranda-2019-order-flow-dynamics-prediction-order-cancelation.md`, converted from `raw/ofi-event-clock/miranda-2019-order-flow-dynamics-prediction-order-cancelation.pdf`.

Coverage of this summary: Read the full markdown text of the paper start to finish, including abstract, introduction, related literature, problem formulation, all experiment sections (7.1-7.8), discussion, and conclusion.

Known problems with the input: Running headers/footers and stray characters from PDF-to-markdown conversion (e.g., garbled journal banner text) were present but did not affect the core text; One numeric detail appears corrupted by the conversion ('84.33.56' time-events, given as the BP duration standard deviation) and was excluded as unreliable.
<!-- AUTHORED REGION END -->