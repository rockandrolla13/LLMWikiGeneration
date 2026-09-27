---
authors:
- Ritwik Das
- Auntara Nandi
content_hash: sha256:932c43a8c2d764f68f2e17bdd40339d48fa6f989c14fd966ed15087410f69453
created: 2026-09-27 01:47:00+00:00
page_id: sources/das-2026-predicting-stock-price-movements-high-frequency
page_type: source
related:
- concepts/trade-clock
- concepts/limit-order-book
- concepts/high-frequency-trading
- concepts/order-flow-prediction
- concepts/feature-engineering
- concepts/backtesting
- concepts/bid-ask-spread
revision_id: 1
schema_version: 2
source_hash: sha256:2e2b94bcfc1a3c8ba07c6975eefecea5adcdd0b1b1bfa2e114e4d901f2d9e893
source_path: markdown_output/das-2026-predicting-stock-price-movements-high-frequency.md
source_type: paper
tags:
- limit-order-book
- machine-learning
- svm
- random-forest
- gradient-boosting
- mid-price-prediction
- spread-crossing
- backtesting
- clock-trade
- asset-equity
- harvest-relevant
title: Predicting Stock Price Movements in High-Frequency Trading
updated: '2026-09-27T01:47:00Z'
uuid: 721ef9dd-4ede-57ec-a3a2-5d2bdac53a1f
year: 2026
---

<!-- AUTHORED REGION START -->
# Predicting Stock Price Movements in High-Frequency Trading

## Summary

The paper asks whether machine learning models can predict short-horizon mid-price direction and bid-ask spread crossings from limit order book (LOB) data at the millisecond scale, using a single stock's trading day split into a 9:30-11:00 modeling window and an 11:00-12:00 strategy window.

Following Kercheval and Zhang's feature grouping, the author builds 126 features from up to 10 LOB levels per side (raw prices/volumes, bid-ask spreads and mid-prices, price differences, level means, cumulative bid/ask differences, and time derivatives), and labels each observation with the subsequent mid-price move (up/down/stationary) and spread-crossing outcome (up/down/stationary) a fixed number of trade events later. Support vector machines, random forests, and gradient boosting are each tuned by 10-fold cross-validated grid search and compared using precision, recall, and F1, alongside a logistic regression benchmark.

During the 9:30-11:00 modeling period the models classify mid-price movement and spread crossings with precision, recall, and F1 mostly in the 70%-80% range, weaker for the minority stationary class. Applying the trained random forest model to the separate 11:00-12:00 strategy period, however, produced poor spread-crossing predictions and a simulated trading strategy built on those predictions lost money overall.

The paper's contribution is mainly a worked demonstration, following Kercheval and Zhang's SVM-based LOB feature framework, of how well standard ML classifiers transfer from an in-sample modeling window to an adjacent out-of-sample trading window, and it argues that time-sensitive features, time-series modeling, and transaction-fee-aware relabeling of the spread-crossing target are needed to close that gap.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Observations are LOB snapshots taken at timestamped trade events; the prediction horizon is a fixed number of subsequent trade events rather than a fixed calendar time. Labels for mid-price and spread-crossing classification models use a horizon of 30 timestamped trade events (used for the v6 time-derivative features); for the 11:00-12:00 trading-strategy backtest the horizon is widened to 50 timestamped trade events because the classifiers produced almost no non-stationary predictions at 30.

## Data

- **Asset class:** Equities
- **Instruments:** A single stock's limit order book; the stock's ticker/name is not stated in the text provided.
- **Venue:** not stated
- **Period:** One trading day, split into a 9:30-11:00 window (used for model training/validation/testing) and an 11:00-12:00 window (used for the trading strategy); the calendar date is not stated.
- **Granularity:** Limit order book depth of up to 10 price/volume levels per side (per the paper's feature-vector table), sampled at each timestamped trade event; the combined feature-and-label dataset has 332,673 rows and 128 columns (126 features, 2 labeled responses).

## Features and Measures

- **Core LOB set (v1).** Ten levels of bid and ask price and volume, best level first.
- **Time-insensitive sets (v2, v3, v4, v5).** Derived, single-snapshot quantities computed from v1: bid-ask spreads and mid-prices per level (v2), price differences across levels (v3), mean prices/volumes across levels (v4), and cumulative bid/ask price and volume differences (v5).
- **Time-sensitive set (v6).** Time derivatives of the per-level ask/bid prices and volumes, computed over a fixed number of timestamped trade events.
- **Top-five volume ratio.** The total volume of the top five ask-side price levels divided by the total volume of the top five bid-side levels, used as a summary-statistic predictor for the logistic regression.

## Method

Three classifiers are fit and compared: a support vector machine with an RBF kernel (tuned to C=10, gamma=0.1), a random forest (500 trees, max_features tuned to 11, i.e. the square root of 126 features, unrestricted depth), and gradient boosting (500 estimators, learning rate tuned to 0.56, max depth 3); all three are tuned with 10-fold cross-validated grid search on a 152,511-row training/validation set drawn from the 9:30-11:00 window, and evaluated on a held-out 50838-row test set from the same window using confusion matrices, precision, recall, and F1. A logistic regression on the same 126 features, and separately on 10 principal components of those features, is fit as a simpler benchmark. For the trading strategy, the best-performing classifiers (mainly random forest, briefly SVM) are applied out of sample to the 11:00-12:00 window to predict spread-crossing direction, and a simple long/short rule based on the predicted crossing is used to compute realized profit versus the maximum profit achievable under perfect prediction.

## Results

- During 9:30-11:00, precision, recall, and F1 for mid-price movement were mostly around 70%-80% for the SVM, random forest, and gradient boosting models, with recall notably weaker for the minority stationary class.
- For bid-ask spread crossing in the same period, all three models predicted the majority stationary class well, but SVM was markedly better than random forest or gradient boosting at also catching the minority upward/downward crossings.
- Applying the random-forest model trained on 9:30-11:00 data to the 11:00-12:00 strategy period, precision for predicted downward and upward spread crossings fell to about 0.1 and 0.002 respectively, even though overall precision stayed high because the stationary class dominates.
- If every spread-crossing label in the 11:00-12:00 window had been predicted correctly, the trading strategy's maximum profit would have been 45.91 (20.8 from longing, 25.11 from shorting); trading on the model's actual predictions instead produced a total profit of -96.26 (-36.07 from longing, -60.19 from shorting).
- A logistic regression on the 126 features or on 10 PCA components performed worse than the machine learning classifiers; the only odds ratio far from 1 was about 2, for the best ask/bid price difference predicting stationary spread crossings.
- A boxplot of the top-five-level ask/bid volume ratio showed values above 60 only for the upward and downward mid-price movement classes, consistent with order-book size imbalance driving price moves.

## Limitations

- The paper does not state the stock, exchange, or calendar date of the sample, so it cannot be independently identified.
- The modeling window (9:30-11:00) and the strategy/backtest window (11:00-12:00) are adjacent hours on the same trading day rather than an independent out-of-sample period.
- The author explicitly attributes the strategy period's poor performance to the absence of time-sensitive features and time-series modeling, and to not yet accounting for transaction fees in the spread-crossing labels.
- Reader note: the strategy backtest ignores transaction costs and uses only one afternoon of trading, so the reported -96.26 loss is a single, small-sample result rather than a robust performance estimate.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/backtesting|backtesting]]
- [[concepts/bid-ask-spread|bid ask spread]]

## Citation

Ritwik Das, Auntara Nandi (2026). Predicting Stock Price Movements in High-Frequency Trading.

DOI: 10.5281/zenodo.18205695

Text ingested: `markdown_output/das-2026-predicting-stock-price-movements-high-frequency.md`, converted from `raw/ofi-event-clock/das-2026-predicting-stock-price-movements-high-frequency.pdf`.

Coverage of this summary: Read the entire markdown file, front to back (abstract, data preprocessing, model fitting, model assessment, interpretations, trading strategies, conclusion, references).

Known problems with the input: year from file metadata; No stock ticker, exchange, or calendar date is given for the LOB dataset used; year_hint 2026 was used since no year is printed anywhere in the text.
<!-- AUTHORED REGION END -->