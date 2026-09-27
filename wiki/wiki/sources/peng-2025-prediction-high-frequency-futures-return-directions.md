---
authors:
- Ying Peng
- Yifan Zhang
- Xin Wang
content_hash: sha256:e113ab63b35d60f8d0edb8ff1a744c595d09495ae8d7088817f2355dad601e56
created: 2026-09-27 01:47:00+00:00
page_id: sources/peng-2025-prediction-high-frequency-futures-return-directions
page_type: source
related:
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/order-flow
- concepts/order-imbalance
- concepts/trade-classification
- concepts/feature-engineering
revision_id: 1
schema_version: 2
source_hash: sha256:81fa1c23314bdb5594c9b48c4107db76e9131b5837ced2898134c5e8da93cb4b
source_path: markdown_output/peng-2025-prediction-high-frequency-futures-return-directions.md
source_type: paper
tags:
- futures
- china-markets
- imbalanced-classification
- mean-uncertainty
- sublinear-expectation
- high-frequency-trading
- svm
- logistic-regression
- clock-calendar
- asset-futures
- harvest-relevant
title: 'Prediction of high-frequency futures return directions based on the mean uncertainty
  classification methods: An application in China''s future market'
updated: '2026-09-27T01:47:00Z'
uuid: 46f57b9a-56d7-5ab3-9740-2396395697c6
year: 2025
---

<!-- AUTHORED REGION START -->
# Prediction of high-frequency futures return directions based on the mean uncertainty classification methods: An application in China's future market

## Summary

The paper predicts the direction of very short-horizon average returns in China's high-frequency futures market, where only sufficiently large price moves count as genuine up or down signals and everything smaller is treated as noise, which makes the resulting classification labels heavily imbalanced. Building on an existing mean-uncertainty logistic regression method developed under sublinear-expectation (nonlinear-expectation) theory, which lets the model's disturbance term come from a family of distributions rather than a single one to better reflect real distributional uncertainty, the authors derive and prove an analogous mean-uncertainty support vector machine.

Both mean-uncertainty classifiers are tested against conventional imbalance-handling variants of logistic regression and SVM (plain, SMOTE-based, and random-undersampling-based) on the 15 most liquid contracts on China's futures market by September 2024 turnover, covering metals, agricultural products and livestock, using trading and limit-order-book data sampled every half second over October 2024. Two binary labeling tasks are built, upward versus non-upward and downward versus non-downward moves of a short-term average return, with the minority class defined by the 95th or 5th percentile of that return; eight order-flow, volume and spread predictor types, each computed over four lookback windows (32 features total), feed the classifiers, which are trained and tested with a rolling multi-day scheme and, within each day, a rolling short window separating feature and label calculation.

Both mean-uncertainty methods clearly outperformed their respective conventional counterparts on balanced accuracy, F-measure and especially recall for the contracts shown in detail, with plain LR and plain SVM in particular almost never flagging the minority (significant-move) class at all. In terms of the resulting long/short trading-strategy returns per trade across all 15 contracts, the mean-uncertainty methods beat the conventional alternatives on most, but not all, contracts.

What is new is a mean-uncertainty SVM classifier, built as a sublinear-expectation counterpart to conventional SVM with a stated theoretical property, evaluated together with the prior mean-uncertainty LR method specifically on the practical task of predicting short-horizon return direction and trading on those predictions in China's futures market, rather than on the more abstract classification benchmarks used in the original mean-uncertainty LR paper.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The paper explicitly defines a wall-clock 'calendar time' interval and builds both the forward-looking label window and four backward-looking lookback windows (0-2.5, 2.5-6.5, 6.5-12.5 and 12.5-25 seconds) on it. Within each trading day, a 30-second rolling window is used: the first 25 seconds are used to compute the eight predictor types (over the four lookback spans, 32 features total) and the following 5 seconds are used to compute the short-term average return that defines the label; this 30-second window rolls forward every 5 seconds through the day. The short-term average return is the average of transaction/mid-prices over the short forward span rather than a single point-to-point return, and an observation is labeled a significant upward or downward move only if that average return exceeds the 95th percentile or falls below the 5th percentile of the return distribution.

## Data

- **Asset class:** Futures
- **Instruments:** Top 15 most liquid contracts by September 2024 turnover on China's futures market: Gold (AU), Copper (CU), Tin (SN), Nickel (NI), Corn (C), Zinc (ZN), Bottle Chips (PR), Rebar (RB), Silver (AG), Aluminum (AL), Hogs (LH), Cotton (CF), Lead (PB), Corn Starch (CS) and Soybean Meal (M)
- **Venue:** China's futures market, via CTP-API-connected exchanges (specific exchange not further named)
- **Period:** 1 October 2024 to 31 October 2024, 18 trading days after excluding pre-open/pre-close periods; liquidity ranking based on September 2024 turnover
- **Granularity:** Trading and limit order book data sampled every 0.5 seconds via the CTP-API; the five-minute pre-opening and pre-closing windows of each day are excluded

## Features and Measures

- **Total volume (Volume_all).** The total number of positions (contracts) transacted within a given lookback interval.
- **Maximum volume (Volume_max).** The largest single-transaction volume observed within a given lookback interval.
- **Price change (Lambda).** The change in mid-price over a lookback interval scaled by the total volume transacted in that interval.
- **Quote imbalance (LobImbalance).** The average imbalance between best-bid and best-ask quoted sizes over a lookback interval.
- **Turnover imbalance (TxnImbalance).** A measure of buy/sell volume asymmetry over a lookback interval, with each trade's side inferred using the Lee-Ready algorithm.
- **Historical return (PastReturn).** The realized return over a lookback interval, computed from the average transaction price relative to the interval's maximum mid-price.
- **Turnover (speed).** A measure of how quickly positions turn over within a lookback interval, relating transaction speed to total position size.
- **Quoted spread (QuotedSpread).** The average proportional bid-ask spread over a lookback interval.

## Method

Mean-uncertainty LR (from prior work) models the classification disturbance term as coming from an interval of possible means rather than a single value, which bounds the model's predicted class probability between an upper and lower value instead of one point estimate; the width of this interval is estimated from a moment condition solved over a sliding window whose length is a tuned hyper-parameter. The authors extend this idea to build mean-uncertainty SVM, proving an analogous uncertainty-interval result for the SVM decision function (using a Gaussian kernel in the empirical application) and classifying a sample into the minority class when its estimated upper probability exceeds 0.5.

Both mean-uncertainty classifiers, plus baseline LR, SVM, and SMOTE- and random-undersampling-based variants of each, are trained on 32 calendar-time features (eight predictor types across four lookback windows) to predict the upward/non-upward and downward/non-downward significant-move labels. Models are evaluated with recall, balanced accuracy and a beta-weighted F-measure suited to imbalanced classification, using a rolling out-of-sample scheme: each 3-trading-day window trains on the first two days and tests on the third, then rolls forward by one day; within each day a 30-second window (25 seconds of features, 5 seconds for the label) rolls forward every 5 seconds.

Investment strategies are built directly on the classifiers' predictions: an upward-flagged observation triggers a long ('long/not long') position and a downward-flagged observation triggers a short ('short/not short') position, with the cumulative and average return per trade over the 18-day test period computed from the realized short-term average returns of the flagged (minority-class) observations.

## Results

- For gold futures (AU), mean-uncertainty LR reached 0.697 recall on the test set versus 0.009 for plain LR, while also achieving the top balanced accuracy (0.577) and F-measure (0.348) among the LR-related methods.
- Plain LR's recall on the minority (significant-move) class was 0.000 for tin (SN) and zinc (ZN), and only 0.009 for gold (AU) and rebar (RB), showing it essentially failed to flag significant moves in these tests.
- Mean-uncertainty SVM reached 0.817 recall on gold (AU) and 0.866 recall on tin (SN), against 0.000 recall for plain SVM on every one of the four detailed contracts (AU, SN, ZN, RB).
- Across all 15 futures contracts, both mean-uncertainty LR and mean-uncertainty SVM produced a higher average return per trade than the conventional alternatives on 80% of contracts for the upward/non-upward (long) strategy.
- For the downward/non-downward (short) strategy, mean-uncertainty LR beat the other LR-related methods on 80% of contracts, while mean-uncertainty SVM beat the other SVM-related methods on 67% of contracts.
- Labels were built from the 95th percentile (upward) and 5th percentile (downward) of short-term average returns, with 32 features (eight predictor types across four lookback windows spanning up to 25 seconds) computed from data sampled every 0.5 seconds over 18 trading days in October 2024.
- Models were trained and tested with a rolling window of 3 trading days (2 days train, 1 day test), and within each day a 30-second window (25 seconds of features, 5 seconds for the label) rolled forward every 5 seconds.

## Limitations

- Detailed classification-metric tables are shown for only 4 of the 15 contracts (AU, SN, ZN, RB); performance on the other 11 contracts is summarized only through aggregate percentage-of-contracts-improved figures.
- The rolling walk-forward scheme uses only 2 training days per 1 test day over 18 trading days total, a comparatively short evaluation window for judging strategy robustness.
- Reported average returns per trade come from a simple long/short rule triggered directly by classifier output, without transaction costs, slippage, or capacity/market-impact considerations mentioned in the text.
- Reader note: results cover a single month (October 2024) of China's futures market; no test of stability across different market regimes or longer periods is presented.

## Related

- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/feature-engineering|feature engineering]]

## Citation

Ying Peng, Yifan Zhang, Xin Wang (2025). Prediction of high-frequency futures return directions based on the mean uncertainty classification methods: An application in China's future market.

DOI: 10.48550/arxiv.2508.06914

Text ingested: `markdown_output/peng-2025-prediction-high-frequency-futures-return-directions.md`, converted from `raw/ofi-event-clock/peng-2025-prediction-high-frequency-futures-return-directions.pdf`.

Coverage of this summary: Read the full paper markdown from abstract through the appendix and references.

Known problems with the input: No journal or conference name is printed anywhere in the document; it appears to be a preprint or working paper, so venue is left blank; Nearly all model equations (LR/SVM formulas, moment conditions, SLE definitions and theorems) are rendered as omitted images in the markdown, so their exact mathematical form could not be verified from the text and is only described qualitatively here; Results tables (2-5) show heavy column/row misalignment from the markdown conversion (e.g. an extra empty column before the Mean-uncertainty LR/SVM values); numbers were matched to their labels using the bolded best-value markers and surrounding prose.
<!-- AUTHORED REGION END -->