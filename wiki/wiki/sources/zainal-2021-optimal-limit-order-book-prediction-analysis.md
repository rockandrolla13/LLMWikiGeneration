---
authors:
- Mohammad Zainal
- Ibrahim Gad
- Hameed AlQaheri
content_hash: sha256:e256a92f2d1e086cd3fc8cb60af8a5db32dae034bbe5b4b622c4fcf6dbba2020
created: 2026-09-27 01:47:00+00:00
page_id: sources/zainal-2021-optimal-limit-order-book-prediction-analysis
page_type: source
publication_venue: Journal of System and Management Sciences, Vol. 11 (2021) No. 3,
  pp. 75-100
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/market-microstructure
- concepts/feature-engineering
- concepts/high-frequency-trading
revision_id: 1
schema_version: 2
source_hash: sha256:83c26b7db2004631d686d14d3df2ee159f3999e959029427cf31de2d09025add
source_path: markdown_output/zainal-2021-optimal-limit-order-book-prediction-analysis.md
source_type: paper
tags:
- limit-order-book
- pigeon-inspired-optimization
- deep-learning
- feature-selection
- nasdaq
- lobster-dataset
- event-classification
- clock-event
- asset-equity
- harvest-relevant
title: An Optimal Limit Order Book Prediction Analysis Based on Deep Learning and
  Pigeon-Inspired Optimizer
updated: '2026-09-27T01:47:00Z'
uuid: 3ceb362c-6bb7-5133-82b3-ef2d263fb74e
year: 2021
---

<!-- AUTHORED REGION START -->
# An Optimal Limit Order Book Prediction Analysis Based on Deep Learning and Pigeon-Inspired Optimizer

## Summary

The paper targets prediction from limit order book (LOB) data for five NASDAQ-listed stocks (Amazon, Apple, Google, Intel, Microsoft), motivated by the growing availability of order-book data and interest in system-driven, pre-trade-transparent markets. It frames the task as classifying each new LOB state into one of five event types (new-order submission, partial cancellation, full deletion, visible execution, hidden execution) rather than as a price-direction forecast.

The approach has three stages. First, order-book and message fields (price, size, order ID, timestamp, event type) are min-max scaled. Second, a Pigeon-Inspired Optimizer (PIO) - a swarm-intelligence search modeled on homing-pigeon navigation rules (a map-and-compass step guided by the current best solution, and a landmark step guided by the centroid of better solutions) - searches for a reduced subset of LOB features, scoring candidate subsets with a fitness function built from true-positive rate, false-positive rate, and the number of selected features, using a decision-tree classifier to evaluate each candidate subset. Third, the selected features are fed into a deep network combining convolutional layers, an Inception module, and a dense layer to classify each incoming LOB state.

On the combined five-ticker LOBSTER dataset the deep classifier reached an overall accuracy of 0.77, with the best per-ticker results on Google and Apple; on Apple data the PIO's best feature subset repeatedly settled on the same three features but with a high false-positive rate. The authors report their per-ticker accuracy figures as higher than several previously published LOB models, though those comparison figures come from different datasets (FI-2010, London Stock Exchange) rather than the same sample. A one-way ANOVA on the order-book fields across the five event-type groups is used to support the classifier's targeting of these fields as distinguishing information.

What is new here, relative to the deep-learning LOB literature the paper reviews, is the specific combination of a pigeon-inspired swarm optimizer for LOB feature selection with an Inception-based deep classifier for multi-class event-type prediction, plus the accompanying ANOVA check on which order-book fields differ significantly by event type.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Data comes from the LOBSTER order-book and message feed for each ticker, which logs every book-changing event (submission, cancellation, deletion, visible execution, hidden execution) with a timestamp in seconds after midnight. The prediction target is the event type associated with each new LOB state; the deep model consumes a sliding window of the previous 10 consecutive LOB snapshots (order-book depth of five price levels per side) to classify the event type of the resulting state, rather than sampling on a fixed calendar or volume clock.

## Data

- **Asset class:** Equities
- **Instruments:** Five NASDAQ-listed stocks: Amazon (AMZN), Apple (AAPL), Google (GOOG), Intel (INTC), and Microsoft (MSFT).
- **Venue:** NASDAQ (via the LOBSTER order-book data feed)
- **Period:** Stated only for Intel (INTC): training data from 04-02-2019 to 31-05-2019 (82 files) and test data from 03-06-2019 to 28-06-2019 (20 files); it is not stated whether the same window applies to the other four tickers.
- **Granularity:** Order-book snapshots at a depth of five price levels per side (each row a vector of length 20 across the top five bid/ask levels), timestamped in seconds after midnight with at least millisecond precision. LOBSTER's broader database (not necessarily the sample used here) is described as covering trading days from 27 June 2007 onward, between 09:30 am and 04:00 pm, excluding weekends and public holidays.

## Features and Measures

- **Pigeon-Inspired Optimizer (PIO) feature selection.** A swarm-intelligence search over LOB feature subsets, modeled on homing-pigeon map-and-compass and landmark navigation rules, scored by a fitness function combining true-positive rate, false-positive rate and the count of selected features, evaluated via a decision-tree classifier.
- **LOB and message fields.** Raw per-event order-book and message fields, including price, size, order ID, timestamp, and bid/ask price and size up to the fifth best level, used as inputs to feature selection and classification.
- **Inception-based deep classifier.** A neural network combining convolutional layers, an Inception module, and a dense layer that classifies each new LOB state into one of five event types.

## Method

Order-book and message data are min-max scaled, then a Pigeon-Inspired Optimizer searches the feature space: each candidate solution is a subset of feature indices, scored by a fitness function combining true-positive rate, false-positive rate, and the number of selected features when a scikit-learn decision-tree classifier is trained and tested on that subset; the optimizer alternates a map-and-compass update guided by the current global-best solution with a landmark update guided by the centroid of the better-performing half of the population. The selected feature subset then feeds a deep classifier built from convolutional layers, an Inception module, and a dense layer, trained to output one of five event-type labels (submission, partial cancellation, full deletion, visible execution, hidden execution).

The PIO run used a compass factor R = 0.09, population size Np = 64, and 10 iterations. The deep model was trained in batches of 1024 samples, each sample built from 10 consecutive LOB states, using the Adam optimizer (learning rate 0.01), categorical cross-entropy loss, and 100 training epochs. Performance is judged by sensitivity/recall (TPR), accuracy, false-positive rate (FPR) and F-score, and the proposed model's accuracy is compared against three previously published LOB models (a single-layer feedforward network, and one- and two-hidden-layer attention-augmented bilinear networks, plus DeepLOB) reported in other work on different datasets. A one-way ANOVA is run on each order-book field across the five event-type groups to check whether their means differ significantly by event type.

## Results

- On the combined (all five tickers merged) LOBSTER dataset the deep-learning model reached accuracy 0.77, precision 0.43, recall 0.436 and F1 0.436.
- On Apple (AAPL) data alone the model reached accuracy 0.749, recall 1, and F1 0.645; on Google (GOOG) data alone it reached accuracy 0.802, recall 0.50 and F1 0.50, the highest per-ticker accuracy reported.
- The authors report their AAPL and GOOG accuracy figures (74.9 and 80.2) as exceeding those of several previously published LOB models evaluated on other datasets, including C(TABL) (74.07 on FI-2010) and DeepLOB (63.93 on London Stock Exchange data).
- On AAPL data, the PIO's global-best solution repeatedly selected the same three features (indices 9, 12, 18) across most of its 10 iterations, with TPR of 0.625 but a high FPR of 0.991 throughout.
- On the merged five-ticker dataset, the PIO global-best solution's TPR rose over iterations from about 0.620 to 0.876, while FPR also rose, reaching 1.000 by the later iterations.
- A one-way ANOVA found statistically significant differences among the five event-type groups' means for most order-book fields at the 0.05 significance level, with a smaller subset of fields (including the price-direction field) not reaching significance; at the looser 0.1 level, even fewer fields were non-significant.
- The combined LOBSTER dataset totaled 852671 samples for the majority event-type class (label 1), split into 681485 training and 171186 test rows, versus 15834 samples for the minority class (label 2), split into 12693 training and 3141 test rows.

## Limitations

- Single data source (NASDAQ via LOBSTER) and, per the authors' own text, a training/testing date range given explicitly only for Intel (INTC), even though five tickers are analyzed overall.
- The authors state the proposed model's performance is similar to a classical deep-learning model, that its running time is a little longer, and that it requires tuning of the deep-learning layer hyperparameters.
- The authors themselves note that because the comparison baselines (Table 10) are evaluated on different datasets (FI-2010, London Stock Exchange) rather than the same LOBSTER sample, results may differ from those in similar studies.
- Reader note: the false-positive rate reported for the PIO feature-selection stage is very high in places (above 0.99, reaching 1.000), which the paper describes as increased model stability without discussing what this implies for classification reliability.
- The authors state that future work should investigate more comprehensive deep-learning models and reinforcement-learning-based trading strategies building on the PIO-selected features.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/high-frequency-trading|high frequency trading]]

## Citation

Mohammad Zainal, Ibrahim Gad, Hameed AlQaheri (2021). An Optimal Limit Order Book Prediction Analysis Based on Deep Learning and Pigeon-Inspired Optimizer. Journal of System and Management Sciences, Vol. 11 (2021) No. 3, pp. 75-100.

DOI: 10.33168/jsms.2021.0305

Text ingested: `markdown_output/zainal-2021-optimal-limit-order-book-prediction-analysis.md`, converted from `raw/ofi-event-clock/zainal-2021-optimal-limit-order-book-prediction-analysis.pdf`.

Coverage of this summary: Read the full paper end to end: abstract, introduction and related work, limit order book and pigeon-inspired-optimizer preliminaries, the LOBSTER dataset description, the full method section (data preprocessing, PIO feature selection, deep-learning classification, performance metrics), all results tables (PIO iteration results, deep-learning results, state-of-the-art comparison, ANOVA table), the concluding remarks, and the reference list.

Known problems with the input: The narrative text describes the merged-dataset figures as accuracy/recall/F-score = 0.77/0.43/0.436, while Table 9 labels the same figures as accuracy/precision/recall/F1 = 0.77/0.43/0.436/0.436; Table 9's labeling was used here as the more detailed source; The stated training/testing date range is given only for Intel (INTC) even though five tickers are analyzed; unclear if the same window applies to the other four; Several inline equations and figures (e.g. the PIO position/velocity update rules) were rendered as garbled or omitted picture placeholders in the markdown conversion and were not used for any factual claim; One ANOVA table column header appears to be a conversion artifact ('Bize_2', likely a Bid_Size field); not relied upon for any specific claim.
<!-- AUTHORED REGION END -->