---
authors:
- Adesola Adegboye
- Michael Kampouridis
- Fernando Otero
content_hash: sha256:bb87d83472c4ab960fa3ed14cd01dd101b4acc9667524f961f829b8e3f5c4bf7
created: 2026-09-27 01:47:00+00:00
page_id: sources/adegboye-2021-improving-trend-reversal-estimation-forex-markets
page_type: source
publication_venue: International Journal of Intelligent Systems
related:
- concepts/intrinsic-time
- concepts/backtesting
- concepts/feature-engineering
- concepts/directional-change
- entities/adesola-adegboye
- entities/michael-kampouridis
revision_id: 1
schema_version: 2
source_hash: sha256:f27b17a8d4a666ddcbd39242e42c052bba99391626919afce2c6fbcf137f7f61
source_path: markdown_output/adegboye-2021-improving-trend-reversal-estimation-forex-markets.md
source_type: paper
tags:
- forex
- directional-changes
- trend-reversal
- classification
- genetic-programming
- event-based-sampling
- algorithmic-trading
- backtesting
- clock-intrinsic
- asset-fx
- harvest-relevant
title: Improving Trend Reversal Estimation in Forex Markets Under a Directional Changes
  Paradigm with Classification Algorithms
updated: '2026-09-27T01:47:00Z'
uuid: af8f8299-5956-5a71-9c30-e0f0f33448ac
year: 2021
---

<!-- AUTHORED REGION START -->
# Improving Trend Reversal Estimation in Forex Markets Under a Directional Changes Paradigm with Classification Algorithms

## Summary

The paper asks whether explicitly predicting if a directional-change (DC) event will be followed by an overshoot (OS) event, rather than assuming it always will as prior DC scaling laws do, improves trend-reversal prediction and trading performance in forex markets. It introduces a classification step (via Auto-Weka) that runs ahead of three existing OS-length estimation techniques (Factor-2, Factor-M, and a genetic-programming symbolic regression, Reg-GP) and embeds the resulting reversal-point predictions into a DC-based trading strategy.

Using 10-minute interval data for 20 FX currency pairs (16 pairs from March 2016 to February 2017, 4 pairs from June 2013 to May 2014, with a 70:30 train/test split) across 1,000 datasets built from 5 DC thresholds x 20 pairs x 10 months, the classification-augmented variants (denoted C+) are compared to their non-classification counterparts and to other DC-related and non-DC benchmarks: a training-set-probability benchmark (p-trading), a trade-at-DCC-point benchmark, three technical indicators (RSI, EMA, MACD), and buy-and-hold.

Adding the classification step reduced OS-length prediction error (RMSE) and increased trading returns and risk-adjusted returns for all three DC algorithms tested; the best-performing combination, C+Reg-GP, ranked first on return, Sharpe ratio and (mostly) maximum drawdown among 15 strategies compared, and outperformed buy-and-hold on both average return and variance.

The main contribution is separating the "will an OS event occur" decision from the "how long will it be" estimation, training the length-estimation models only on DC events known (with perfect foresight on the training set) to have a corresponding OS event so that classification errors do not contaminate that step. The paper also shows the DC-OS length relationship is non-linear and dataset-specific rather than a single universal scaling law.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Observations are triggered by Directional Change (DC) events: price is tracked against a threshold and each DC event (upturn or downturn) is confirmed only in hindsight once price has retraced by that threshold, at which point a DC Confirmation (DCC) point is set. A DC event is typically followed by an Overshoot (OS) event that ends when the opposite-direction DC is confirmed, together forming a full DC trend. At each DCC the model first predicts whether an OS event will follow and, if so, estimates its length (via Factor-2, Factor-M, or Reg-GP) to set the trend-reversal (DCE) point used for trading; if no OS event is predicted, the DCC point itself is used as the reversal point.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** 20 FX currency pairs: AUD/JPY, AUD/NZD, AUD/USD, CAD/JPY, EUR/AUD, EUR/CAD, EUR/CSK, EUR/GBP, EUR/JPY, EUR/NOK, EUR/USD, GBP/AUD, GBP/CHF, GBP/USD, NZD/USD, USD/CAD, USD/JPY, USD/NOK, USD/SGD, USD/ZAR
- **Venue:** not stated
- **Period:** 16 pairs: March 2016 to February 2017; 4 pairs: June 2013 to May 2014
- **Granularity:** 10-minute interval (high-frequency) data, 70:30 train/test split per dataset

## Features and Measures

- **Directional Change (DC) event.** An upturn or downturn confirmed once price has retraced by a fixed threshold from the last extreme, dividing the market into alternating trends.
- **Overshoot (OS) event.** The portion of a DC trend continuing beyond the DC confirmation point until the opposite-direction DC is confirmed.
- **DC/OS classification attributes (A1-A6).** Six attributes used to predict whether a DC event will have a corresponding OS event: price and time differences from the DC confirmation point, price-change speed, price at the previous confirmation point, whether the previous DC had an OS event, and whether the DC event's start and end times are equal.
- **Factor-2.** OS length estimated as twice the DC event length, based on an empirical scaling law from prior FX literature.
- **Factor-M.** OS length estimated as a dataset-specific multiple M of DC length, with M fitted per dataset and separately for upward and downward trends.
- **Reg-GP.** OS length estimated via a genetic-programming symbolic regression that evolves both the functional form and coefficients of the DC-to-OS length relationship, minimizing RMSE.

## Method

A binary classification step (Auto-Weka searching 39 classification algorithms and their hyperparameters, run 10 times per dataset with 10-fold cross-validation, tuned to a 60-minute execution budget) predicts, at each DC confirmation point, whether the DC event will have a corresponding OS event, using six DC/OS attributes (A1-A6).

When an OS event is predicted, one of three OS-length estimation techniques (Factor-2, Factor-M, or the genetic-programming symbolic regression Reg-GP, tuned via the I/F-Race package) is fitted only on DC events known, with perfect foresight on the training set, to have a corresponding OS event, giving the predicted trend-reversal point; when no OS event is predicted, the DC confirmation point itself is used. Five DC thresholds are evaluated per dataset and the threshold with the lowest RMSE is selected.

The predicted reversal points drive a directional-change trading strategy (opening/closing positions at upward/downward DC extremes, net of a 0.025% transaction cost) evaluated across 1,000 datasets via return, maximum drawdown and Sharpe ratio, benchmarked against DC variants without classification, a training-set-probability benchmark, a trade-at-DCC-point benchmark, technical indicators (RSI, EMA, MACD), and buy-and-hold, with significance assessed via the Friedman test and Hommel post-hoc procedure.

## Results

- C+Reg-GP had the lowest average RMSE (18.8175) among six OS-length estimators, with classification accuracy for the classifier-based variants typically 70% to 85%.
- Even where classification accuracy was low (55-58% for EUR/CSK), the classification step still reduced RMSE because it filtered out cases with no OS event.
- A Friedman test on RMSE ranked C+Reg-GP first (average rank 1.90), statistically outperforming the non-classification Factor-2 and Factor-M variants.
- In trading, C+Reg-GP had the highest average return (0.2247) of the 15 strategies tested; every classification variant (C+Factor-M 0.0684, C+Factor-2 0.1186) had a higher average return than its non-classification counterpart, most of which had negative average returns.
- C+Reg-GP outranked Reg-GP, p+Reg-GP and DCC+Reg-GP in 14 of the 17 traded currency pairs.
- C+Reg-GP had the lowest (best) average maximum drawdown (0.1259), ranking best in 13 of 17 currency pairs among its Reg-GP variants, though for Factor-M/Factor-2 the non-classification versions had lower drawdown.
- Of 34 risk-adjusted return series tested, C+Reg-GP had a positive Sharpe ratio in 28, more than any other strategy, and ranked first in the Friedman test.
- Against buy-and-hold, C+Reg-GP had a mean return of 0.225% versus -0.128% for buy-and-hold, with lower variance (0.153 vs 0.515), outperforming in 12 currency pairs (confirmed by a Kolmogorov-Smirnov test, p-value 7.2529e-04).

## Limitations

- The DC-OS length relationship is dataset-dependent; the authors state there is no generalised formula for predicting trend reversal across all datasets, so equations must be tailored per dataset.
- The classification step is computationally expensive (around 60 minutes of Auto-Weka search per dataset, versus 3 seconds for trading itself), though the authors note it could be parallelised.
- Reader note: evaluation is limited to 20 FX pairs sampled at 10-minute intervals over a two-month tuning window and ten-month test window; generalization to other markets or sampling frequencies is not tested.
- Reader note: some currency pairs (AUD/JPY, CAD/JPY, USD/JPY) never triggered a trade under C+Reg-GP across all 50 GP runs, limiting the comparable sample for those pairs.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/backtesting|backtesting]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/directional-change|Directional Change]]
- [[entities/adesola-adegboye|Adesola Adegboye]]
- [[entities/michael-kampouridis|Michael Kampouridis]]

## Citation

Adesola Adegboye, Michael Kampouridis, Fernando Otero (2021). Improving Trend Reversal Estimation in Forex Markets Under a Directional Changes Paradigm with Classification Algorithms. International Journal of Intelligent Systems.

DOI: 10.1002/int.22601

Text ingested: `markdown_output/adegboye-2021-improving-trend-reversal-estimation-forex-markets.md`, converted from `raw/ofi-event-clock/adegboye-2021-improving-trend-reversal-estimation-forex-markets.pdf`.

Coverage of this summary: Read the full paper markdown end to end, from title/abstract through methodology, experimental setup, all results tables, the summary/conclusion, and the reference list.

Known problems with the input: The markdown conversion contains OCR/PDF-extraction artifacts: stray page-footer line numbers embedded mid-sentence throughout, and several sentences with words missing or garbled (e.g. in sections 3.3 and 3.3.1). These did not prevent extracting the substantive content, but exact reproduction of a few sentences in the source is imperfect.
<!-- AUTHORED REGION END -->