---
authors:
- Adesola Adegboye
- Michael Kampouridis
content_hash: sha256:142c04ae6abe37106350ecd3aef925569dc14fa8f63cdb98dbbbe3e50581842b
created: 2026-09-27 01:47:00+00:00
page_id: sources/adegboye-2021-machine-learning-classification-regression-models-predicting
page_type: source
publication_venue: Expert Systems with Applications (preprint)
related:
- concepts/intrinsic-time
- concepts/backtesting
- concepts/feature-engineering
- concepts/directional-change
- entities/adesola-adegboye
- entities/michael-kampouridis
revision_id: 1
schema_version: 2
source_hash: sha256:409f3341b3781a290682f58b0f11bed44e16f68b478c09a5dca808abc397259f
source_path: markdown_output/adegboye-2021-machine-learning-classification-regression-models-predicting.md
source_type: paper
tags:
- fx
- directional-changes
- genetic-programming
- trend-reversal
- classification
- algorithmic-trading
- symbolic-regression
- clock-intrinsic
- asset-fx
- harvest-relevant
title: Machine Learning Classification and Regression Models for Predicting Directional
  Changes Trend Reversal in FX Markets
updated: '2026-09-27T01:47:00Z'
uuid: 1e931147-0519-55e3-98ca-839d6869d75b
year: 2020
---

<!-- AUTHORED REGION START -->
# Machine Learning Classification and Regression Models for Predicting Directional Changes Trend Reversal in FX Markets

## Summary

Traders using directional changes (DC) sample price data by threshold-defined price moves instead of fixed time intervals, splitting the series into a directional-change (DC) event followed by an overshoot (OS) event. Prior work assumed every DC event is followed by an OS event and then fit a formula linking DC length to OS length; this paper asks whether adding a first classification step, predicting whether an OS event will occur at all, improves prediction of when a trend actually reverses.

Building on the authors' earlier genetic-programming (GP) symbolic-regression work, the paper adds a classification stage: Auto-Weka selects and tunes a classifier per dataset to label each DC event as followed by an OS event or not, using six DC/OS-derived attributes. GP-based symbolic regression, trained only on DC events that genuinely have an OS event, then predicts OS length for events the classifier flags as having one; for events flagged as not having one, the trend is taken to end at the DC event itself. This combined classification-plus-regression trend-reversal estimate is embedded in a new DC-based trading strategy and tested on 10-minute FX data for 20 currency pairs over 10 months (1,000 datasets in total, each built with one of 5 dynamically chosen DC thresholds), against ten benchmarks: three other DC-based reversal estimators, seven technical-analysis indicators, and buy-and-hold.

The classification step reaches 0.817 average accuracy, 0.842 precision and 0.822 recall in predicting whether an OS event follows a DC event. Combining classification with GP regression (C+GP) gives the lowest average RMSE (18.617) of the four OS-length estimators compared and ranks first by the Friedman/Hommel test, significantly ahead of two earlier hand-specified formulas. The resulting trading strategy (C+GP+TS) has the highest average return among all eleven trading strategies tested, including DC-based rivals and seven technical-analysis indicators, and it also beats buy-and-hold on both average return and variance.

What is new is the extra classification step that separates DC events with a genuine subsequent overshoot from those without one, before regression is fit only on the former; the authors report this reduces regression error and improves trading performance relative to their own GP-only predecessor and to two earlier linear DC-OS formulas, and they conclude no single formula generalises across all 20 currency pairs, so trend-reversal prediction needs to be tailored per dataset.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Prices are resampled into directional-change (DC) events using a percentage price-move threshold: once price reverses by at least the threshold from the last extreme, a DC event is confirmed and an overshoot (OS) event begins, ending at the next opposite-direction DC event. Five DC thresholds are dynamically selected per dataset. The prediction target (trend-reversal point) is the DC event's end if a classifier predicts no following OS event, or the DC event's end plus the GP-regression-estimated OS length if it predicts one will occur; the underlying raw data feeding this process is 10-minute FX bars.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** AUD/JPY, AUD/NZD, AUD/USD, CAD/JPY, EUR/AUD, EUR/CAD, EUR/CSK, EUR/NOK, GBP/AUD, NZD/USD, USD/CAD, USD/NOK, USD/JPY, USD/SGD, USD/ZAR, EUR/GBP, EUR/USD, EUR/JPY, GBP/CHF, GBP/USD (20 currency pairs)
- **Venue:** Data purchased from OLSENDATA.com; underlying trading venue/exchange not stated
- **Period:** March 2016 to February 2017 for most pairs; June 2013 to May 2014 for EUR/USD, EUR/JPY, GBP/CHF and GBP/USD
- **Granularity:** 10-minute interval FX price data

## Features and Measures

- **DC event price (X1).** The price difference between the upturn/downturn extreme point and the directional-change confirmation point.
- **DC event time (X2).** The time difference between the upturn/downturn extreme point and the directional-change confirmation point.
- **Sigma' (X3).** The speed at which price changes from the start of a trend to the directional-change confirmation point.
- **Previous DC event price (X4).** The market price recorded at the previous DC confirmation point.
- **Previous DC has OS (X5).** A yes/no flag for whether the immediately preceding DC trend had a corresponding overshoot event.
- **Flash event (X6).** A yes/no flag for whether a DC event's start time and end time are equal.
- **DC-OS length ratio formulas (Equations 1, 2, and 3).** Prior formulas mapping DC event length to expected overshoot length: a fixed ratio, a dataset-tailored linear constant, and a GP-evolved symbolic function; used here as benchmarks against the paper's own classification-plus-regression estimate.

## Method

The classification stage applies Auto-Weka (an automated algorithm-and-hyperparameter search over 39 Weka classifiers) separately to each dataset, trained with 10-fold cross-validation on the training split and run 10 independent times per dataset, keeping the model with the best F-measure; the search runtime was tuned to 60 minutes. The regression stage evolves symbolic-regression trees with genetic programming (population 500, 37 generations, tournament size 3, crossover probability 0.98, mutation probability 0.02, elitism probability 0.10, maximum tree depth 3, tuned via I/F-Race), trained only on DC events with a genuine OS event, using addition, subtraction, division, multiplication, power, sine, cosine, log and exponential functions with protected division/log/exponential/power, and RMSE as the fitness measure; negative, NaN or infinite OS-length predictions are wrapped to zero.

Performance is judged three ways. Classification is scored by accuracy, precision and recall against held-out data. Regression is scored by RMSE of predicted versus actual OS length, compared against three earlier DC-OS formulas using the Friedman test with Hommel post-hoc correction. The combined trend-reversal estimate then drives a trading strategy (open on an upward DC trend if no position is open and projected return after transaction costs is positive; close on a downward DC trend under the mirrored rule; hold otherwise, using all available capital and a 0.025% transaction cost per trade), judged on return, maximum drawdown and Sharpe ratio against ten benchmarks (three DC-based reversal estimators, seven technical-analysis indicators, and separately buy-and-hold), again with Friedman/Hommel tests for statistical ranking.

## Results

- The classification step averaged 0.817 accuracy, 0.842 precision and 0.822 recall across 20 currency pairs in predicting whether a DC event has a corresponding OS event.
- The combined classification-plus-regression estimator (C+GP) had the lowest average RMSE (18.617) of the four OS-length estimators compared, versus 25.795, 34.477 and 20.265 for the three prior formulas.
- C+GP ranked first by the Friedman test (average rank 1.450) and was statistically better than two of the three prior formulas at the 5% level; the predecessor GP-only formula ranked second.
- The resulting trading strategy (C+GP+TS) had the highest average return (0.225%) among 11 strategies tested and ranked first in 12 of 17 actively traded currency pairs.
- C+GP+TS ranked first by the Friedman test for both trading return and Sharpe ratio, statistically outperforming all other strategies at the 5% level.
- Against buy-and-hold, C+GP+TS had a higher average return (0.225% vs -0.121%) and lower variance (0.153 vs 0.515), a difference a Kolmogorov-Smirnov test found significant (p=7.2529e-04).
- On maximum drawdown, the Aroon technical indicator, not C+GP+TS, had the best (lowest) average result among all strategies compared.

## Limitations

- The classification step performed much worse on one currency pair (EUR/CSK: 0.557 accuracy, 0.620 precision, 0.419 recall) than on the other 19 pairs, where accuracy stayed above 0.780.
- The paper's own conclusion states there is no single generalised formula for predicting trend reversal across datasets; each dataset needs its own tailored model.
- Technical-analysis benchmarks had lower average drawdown and fewer losses than the DC-based strategies including C+GP+TS, implying they take less risk even though they earn less average return.
- Auto-Weka's classification search was run in single-threaded mode with a fixed 60-minute budget due to limited hardware, which the authors note could be shortened with more parallel resources.
- Reader note: all data came from a single vendor (OLSENDATA.com) and two overlapping historical windows (2013-2014 and 2016-2017), so results have not been tested against more recent FX regimes or other data sources.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/backtesting|backtesting]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/directional-change|Directional Change]]
- [[entities/adesola-adegboye|Adesola Adegboye]]
- [[entities/michael-kampouridis|Michael Kampouridis]]

## Citation

Adesola Adegboye, Michael Kampouridis (2020). Machine Learning Classification and Regression Models for Predicting Directional Changes Trend Reversal in FX Markets. Expert Systems with Applications (preprint).

DOI: 10.1016/j.eswa.2021.114645

Text ingested: `markdown_output/adegboye-2021-machine-learning-classification-regression-models-predicting.md`, converted from `raw/ofi-event-clock/adegboye-2021-machine-learning-classification-regression-models-predicting.pdf`.

Coverage of this summary: Read the full paper front to back: abstract, introduction, DC background and related literature, the full methodology (classification, GP symbolic regression, trading strategy), the experimental setup (data, tuning), all results subsections (classification, regression, trading, buy-and-hold comparison, sample GP equations, computational times, summary), and the conclusion.
<!-- AUTHORED REGION END -->