---
authors:
- Maorufa Zaman
- Haris Md Sahed
content_hash: sha256:c791fd0d09d7b9bc2724816022d3c12be6626ed5293bc7548d449e74907bcb43
created: 2026-09-27 01:47:00+00:00
page_id: sources/zaman-2026-volatility-aware-extreme-event-detection-high
page_type: source
related:
- concepts/high-frequency-trading
- concepts/limit-order-book
- concepts/order-flow-imbalance
- concepts/high-frequency-data
- concepts/feature-engineering
- concepts/backtesting
revision_id: 1
schema_version: 2
source_hash: sha256:df544be69bd0b955327124b551a58c807c6cc99428e01a97196b643257723cde
source_path: markdown_output/zaman-2026-volatility-aware-extreme-event-detection-high.md
source_type: paper
tags:
- bitcoin
- crypto
- extreme-event-detection
- xgboost
- class-imbalance
- volatility-clustering
- limit-order-book
- clock-calendar
- asset-crypto
- harvest-relevant
title: Volatility-Aware Extreme Event Detection in High-Frequency Financial Markets
updated: '2026-09-27T01:47:00Z'
uuid: b1a173a2-9072-5e79-8137-05befb60d877
year: 2026
---

<!-- AUTHORED REGION START -->
# Volatility-Aware Extreme Event Detection in High-Frequency Financial Markets

## Summary

The paper asks why models trained on high-frequency Bitcoin limit order book data struggle to flag rare, large price moves, and argues the usual culprits, non-stationarity, microstructure noise and severe class imbalance, are compounded by a fourth, underexamined problem: how the 'extreme event' label itself is defined. A standard quantile-based label, based only on the size of a future return, treats each extreme move as an isolated point and ignores that big moves tend to cluster in time alongside periods of elevated volatility.

The authors first characterize the dataset directly: they show the mid-price series is non-stationary, log returns are heavy-tailed and strongly volatility-clustered, and only a small share of observations qualify as extreme under the standard return-only definition. They then propose a volatility-aware label that marks an observation as extreme if either its forward cumulative return crosses a quantile threshold or it sits inside a period of unusually high rolling volatility, which mechanically raises the share of positive examples. An XGBoost classifier is trained on lagged return, volatility, momentum, order-flow-imbalance and spread features, evaluated with time-series cross-validation, with class weighting to offset imbalance and a per-fold decision threshold chosen from the precision-recall curve rather than a fixed 0.5 cutoff.

The return-only label yields performance barely above a random classifier, whereas the volatility-aware label produces a large jump in precision-recall AUC together with a markedly higher recall, without any change to the model itself. Threshold calibration further improves the fraction of true extreme events the model manages to flag while keeping precision at a workable level. A separate attempt to predict the direction, rather than just the occurrence, of these events performed close to random, suggesting direction is harder to learn than occurrence in this setting.

The paper's central claim is that, in this imbalanced, non-stationary setting, how the prediction target is built matters more than model sophistication: incorporating volatility-regime information into the label, rather than swapping in a more complex architecture, is what drives the reported improvement.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The underlying Bitcoin limit order book data is resampled to near-uniform 1-minute observations (average spacing 60.24 seconds). At each step the model uses a log return and a cumulative future return summed over a forward horizon of 3 minutes to decide whether that point counts as an extreme event, so both the sampling interval and the prediction horizon are defined in wall-clock time rather than by trade or message count.

## Data

- **Asset class:** Crypto
- **Instruments:** Bitcoin (BTC) limit order book data
- **Venue:** not stated
- **Period:** April 7, 2021 to April 19, 2021 (about 12 days)
- **Granularity:** 17,113 observations at near-1-minute frequency (average interval 60.24 seconds), with 156 features per observation covering midpoint price, bid-ask spread, buy/sell trading volumes and multiple order book depth levels

## Features and Measures

- **cumulative future return.** Sum of log returns over a forward window of several minutes, used instead of a single-step return to smooth out microstructure noise when deciding whether a future move is large.
- **volatility-aware extreme event label.** A binary target that flags an observation as extreme if its forward cumulative return passes a quantile threshold or if it falls in a period where rolling volatility is itself unusually high, rather than judging return size alone.
- **rolling volatility regime indicator.** A flag for whether trailing rolling standard deviation of returns exceeds a quantile threshold, meant to capture the tendency of large moves to cluster in persistent high-variance periods.
- **order flow imbalance.** A measure of buy pressure relative to sell pressure built from buy and sell trading volumes, used as one of the model's predictive features alongside lagged returns, momentum and spread measures.

## Method

The task is framed as binary classification: is a given 1-minute observation an 'extreme event' under either the return-only or the volatility-aware label. Predictors include lagged and absolute returns, rolling return volatility over multiple windows, a high-volatility regime flag, rolling-sum momentum features, order flow imbalance and related order-pressure measures, and bid-ask spread changes and volatility, all built only from information available up to the current time step.

An XGBoost classifier is trained with the scale_pos_weight parameter set to the ratio of negative to positive examples in each training fold, to offset class imbalance without resampling. Model evaluation uses TimeSeriesSplit cross-validation so that each fold trains only on past data and tests on later data. Because a fixed 0.5 classification threshold performs poorly on such a rare-event problem, the decision threshold is instead chosen within each fold from the precision-recall curve, picking the threshold that maximizes recall subject to a minimum precision floor, with a lower bound imposed on the threshold itself to avoid degenerate near-zero cutoffs. Precision-recall AUC is treated as the main evaluation metric, alongside ROC-AUC, F1, precision and recall.

## Results

- Under the return-only baseline label (about 2% of observations positive), the classifier's PR-AUC is about 0.08, close to the random baseline of about 0.06, and recall is very low.
- Redefining the label to include high-volatility regimes raises the share of positive examples from about 2% to about 6% (6.10% precisely), without changing the model.
- With the volatility-aware label the classifier reaches an average PR-AUC of about 0.40, ROC-AUC of about 0.87, precision of about 0.28, recall of about 0.49 and F1 of about 0.31.
- The authors describe the jump from a PR-AUC of about 0.06 to about 0.40 as more than a sixfold improvement over the random baseline.
- Per-fold threshold calibration lets the model flag about 50% of extreme events while keeping precision at a workable level.
- Log returns in the sample show strong deviation from normality: standard deviation 0.00107, negative skewness of -3.03 and kurtosis of 133.7, consistent with frequent small moves punctuated by rare large ones.
- A separate attempt to classify the direction of extreme moves scored only marginally above the random baseline.

## Limitations

- The authors state the study does not model the direction of price movements, only whether an extreme move occurs.
- The authors state the dataset's temporal coverage is limited, which may restrict how well the findings generalize.
- The authors report that a preliminary attempt at directional classification performed only marginally above random, without further investigation of why.
- Reader note: the dataset covers a single asset (Bitcoin) over roughly 12 days on one unnamed venue, so the size of the reported PR-AUC gain has not been shown to hold on other assets, periods or exchanges.
- Reader note: the paper does not report sensitivity of results to the specific threshold-calibration hyperparameters (the minimum precision floor and the minimum threshold), which were fixed rather than tuned.

## Related

- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/backtesting|backtesting]]

## Citation

Maorufa Zaman, Haris Md Sahed (2026). Volatility-Aware Extreme Event Detection in High-Frequency Financial Markets.

DOI: 10.48550/arxiv.2607.17555

Text ingested: `markdown_output/zaman-2026-volatility-aware-extreme-event-detection-high.md`, converted from `raw/ofi-event-clock/zaman-2026-volatility-aware-extreme-event-detection-high.pdf`.

Coverage of this summary: Read the full markdown file: abstract, introduction, literature review, data description, methodology, results and discussion, and conclusion.

Known problems with the input: No publication year is printed; year is taken from the job file's year_hint of 2026; No venue, journal, or conference name is stated anywhere in the visible text, so the venue field is left empty; The markdown replaces the paper's mathematical definitions (log return, threshold formulas, rolling volatility, feature formulas) with picture placeholders, so their exact algebraic form could not be verified from text; The abstract states a baseline PR-AUC of about 0.06, while the results section states the baseline target itself reaches PR-AUC of about 0.08 versus a random baseline of about 0.06; both figures are reported here as the paper states them rather than reconciled.
<!-- AUTHORED REGION END -->