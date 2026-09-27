---
authors:
- Faisal Qureshi
content_hash: sha256:c6900ac58bd7c6a045c5705cb400989b8f835bdf10098d7251c627461adbc76e
created: 2026-09-27 01:47:00+00:00
page_id: sources/qureshi-2018-investigating-limit-order-book-characteristics-short
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/order-imbalance
- concepts/high-frequency-trading
- concepts/feature-engineering
- concepts/market-microstructure
- concepts/overfitting-backtesting
revision_id: 1
schema_version: 2
source_hash: sha256:9cac2fabec02a804fbd49bcd93acd7f32d9a97195e69870ee68538511cb2b220
source_path: markdown_output/qureshi-2018-investigating-limit-order-book-characteristics-short.md
source_type: paper
tags:
- limit-order-book
- order-imbalance
- price-prediction
- random-forest
- class-imbalance
- feature-engineering
- nasdaq-equities
- clock-event
- asset-equity
- harvest-relevant
title: 'Investigating Limit Order Book Characteristics for Short Term Price Prediction:
  a Machine Learning Approach'
updated: '2026-09-27T01:47:00Z'
uuid: 45bbfd12-b1b0-5c5e-82e0-8d610ace25eb
year: 2018
---

<!-- AUTHORED REGION START -->
# Investigating Limit Order Book Characteristics for Short Term Price Prediction: a Machine Learning Approach

## Summary

The paper asks which Limit Order Book (LOB) and order-message features carry information about the immediate direction of short-term price movement, using a machine learning approach rather than a hand-built microstructure model. It restricts the question to direction only, explicitly leaving the magnitude of price change and any trading strategy out of scope.

A baseline predictor that classifies purely by label frequency is compared against six classifiers (Gaussian Naive Bayes, Stochastic Gradient Descent, a multilayer perceptron, Support Vector Machine, Gaussian Process Classifier, and Random Forest) on LOBSTER order-book data for four NASDAQ large-cap stocks. Because raw next-event price labels are heavily skewed toward 'no change', the paper tests binarizing the label, SMOTE over/under-sampling, and a smoothing scheme that compares the mean of the previous and next several mid-quote observations against a minimum-change threshold, before re-running all classifiers.

Random Forest, run on the smoothed label, is selected as the best classifier and tuned, then used to test separate feature-set families: raw order-message fields, LOB price/volume fields at different depths, level-by-level order-book imbalance, and an engineered order-arrival-rate feature. The tuned Random Forest substantially beats the baseline, LOB features are strongly predictive and improve with more levels, while order-book imbalance features behave in the opposite direction, improving as fewer levels are used, and a single level-1 imbalance feature outperforms the full 10-level LOB feature set.

What is new is the systematic feature-set-by-feature-set comparison (order fields, LOB depth, imbalance, and an engineered order-arrival-rate feature) built around a smoothed labeling scheme designed to counter the class imbalance that raw tick-by-tick price-direction labels otherwise produce.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are indexed by individual LOBSTER order events (creations, cancellations, executions) rather than fixed time intervals. The initial label predicts whether the mid-quote price at the next order event is above, below, or equal to the current mid-quote price. To reduce label noise from single-event price flicker, a smoothed label instead compares the mean of the previous S mid-quote observations to the mean of the following S, classified as up, down, or stationary against a minimum-price-change threshold parameter alpha, with S=20 and alpha=1 used as the working parameters for most of the study.

## Data

- **Asset class:** Equities
- **Instruments:** NASDAQ large-cap stocks AAPL, AMZN, GOOG, and INTC for the main study, using 10-level LOBSTER sample data (MSFT sample data was also available but not used as the main analysis stock)
- **Venue:** NASDAQ, via LobsterData sample data
- **Period:** a single day of trading, 21 June 2012
- **Granularity:** individual order-message (LOBSTER message-file) events reconstructed into a 10-level limit order book (orderbook file); experiments generally run on subsamples of 5,000 to 50,000 data points out of per-stock files of 156,000 to 250,000 lines

## Features and Measures

- **LOB imbalance.** the buy/sell volume imbalance at a given order-book level, computed level-by-level from the reconstructed book and grouped into feature sets by number of levels retained (from 1 level up to 10 levels).
- **Order Arrival Rate.** an engineered feature counting the volume of buy and sell orders created, cancelled, and executed within a short historic window, computed separately for orders at the best book level versus all other levels.
- **Order Feature Sets.** groupings of raw order-message fields (event time, order type, order ID, size, price, direction) used to test how much predictive information order attributes carry on their own, without book-level information.
- **LOB Feature Sets.** groupings of book price/volume fields by depth (levels 1 through 10) used to test how prediction accuracy changes as fewer book levels are retained.

## Method

A baseline predictor ('BasePred') draws labels randomly according to each class's empirical frequency, providing a floor against which classifiers are compared; it is checked against a synthetic dataset with randomized feature values to confirm it is not exploiting real structure. Six classifiers (Gaussian Naive Bayes, Stochastic Gradient Descent, a multilayer perceptron, Support Vector Machine, Gaussian Process Classifier, and Random Forest), using standard scikit-learn implementations, are evaluated on the raw three-class (up/down/stationary) label; SVM and Gaussian Process Classifier are dropped early for failing to converge in reasonable time. Because the raw label is heavily skewed toward the stationary class, the paper tests binarizing the label (dropping stationary points), SMOTE over/under-sampling, and a smoothing scheme comparing the mean of the previous and next S mid-quote prices against a minimum-change threshold alpha, re-running all six classifiers on each variant.

Random Forest is selected as the best-performing classifier and tuned via k-fold grid search over number of estimators, maximum features, and minimum samples per leaf, alongside a grid search over the smoothing parameters alpha and S; the tuned Random Forest with the smoothed label is then used as a benchmark for the rest of the study. Order, LOB (by depth), imbalance (by level), and order-arrival-rate feature sets are each evaluated separately by re-running Random Forest and comparing accuracy, precision, recall, F1-weighted, F1-micro, and per-class accuracy, and the best feature sets from each family are then combined into a single 'Combined' dataset.

## Results

- The tuned Random Forest classifier with the smoothed label (S=20, alpha=1) reached 89.47% overall accuracy versus 33.81% for the class-frequency baseline predictor on the same 100K-point sample.
- Raw (unsmoothed) three-class labeling produced heavy class imbalance, with approximately 90% of data points in the stationary class.
- LOB-based feature sets were strongly predictive and accuracy fell as fewer book levels were retained, with the largest single drop occurring between the 2-level and 1-level feature sets (LOB-2 accuracy 76.59% vs LOB-1 accuracy 68.15%).
- In contrast to raw LOB depth features, LOB imbalance feature sets improved as fewer levels were used, and the smallest imbalance set (level-1 only) reached 91.21% accuracy, outperforming the full 10-level LOB feature set at 87.92%.
- Order-message features alone were weak predictors except for a single 'time since midnight' feature, which alone reached 90.83% accuracy, a result the author flags as possibly reflecting overfitting to a single day of data.
- Combining the best order, LOB, imbalance, and arrival-rate feature sets into one 'Combined' dataset (89.54% accuracy) gave no meaningful improvement over the benchmark Random Forest run on the full base feature set (89.47% accuracy).
- Order Arrival Rate features computed on the level-1 order book performed best at a 10.0-second historic window (80.14% accuracy) versus a 0.1-second window (69.45%), while the corresponding rates for non-level-1 orders performed best at a 1.0-second window (62.85%).

## Limitations

- The study uses a single day of trading (21 June 2012) and focuses its detailed feature analysis mainly on one stock (AMZN), limiting generalizability across time periods and tickers.
- SVM and Gaussian Process Classifier were dropped early for failing to converge, and SGD and the neural network classifier behaved erratically, sometimes predicting a single class for all inputs, for reasons the author states were not investigated further.
- Reader note: many sub-experiments run on subsamples of 5,000 to 50,000 points due to compute limits (a 1.83 GHz Celeron notebook), rather than on the full 156,000-250,000-line per-stock dataset.
- The smoothing and classifier hyperparameters (alpha, S, Random Forest settings) were tuned non-rigorously, as the author states directly.
- Only next-event direction of the mid-quote is predicted; the magnitude of price change and trading-strategy construction are explicitly out of scope.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]

## Citation

Faisal Qureshi (2018). Investigating Limit Order Book Characteristics for Short Term Price Prediction: a Machine Learning Approach.

DOI: 10.48550/arxiv.1901.10534

Text ingested: `markdown_output/qureshi-2018-investigating-limit-order-book-characteristics-short.md`, converted from `raw/ofi-event-clock/qureshi-2018-investigating-limit-order-book-characteristics-short.pdf`.

Coverage of this summary: Read the whole markdown file, abstract through conclusion, including all results tables.

Known problems with the input: year from file metadata.
<!-- AUTHORED REGION END -->