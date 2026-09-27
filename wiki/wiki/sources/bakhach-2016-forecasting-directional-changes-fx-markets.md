---
authors:
- Amer Bakhach
- Edward P. K. Tsang
- Hamid Jalalian
content_hash: sha256:5a9406f72403fd7e030ca92fe04666d19241a1bbb3eb36049222b8c988041fb6
created: 2026-09-27 01:47:00+00:00
page_id: sources/bakhach-2016-forecasting-directional-changes-fx-markets
page_type: source
related:
- concepts/intrinsic-time
- concepts/alpha-signal
- concepts/high-frequency-data
- concepts/backtesting
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:88251b791d29dc1fc2b622f4c7f12835d4c54819e940054f1631fa5f249c108c
source_path: markdown_output/bakhach-2016-forecasting-directional-changes-fx-markets.md
source_type: paper
tags:
- directional-change
- fx-forecasting
- decision-tree
- trend-continuation
- currency-pairs
- threshold-forecasting
- clock-intrinsic
- asset-fx
- harvest-relevant
title: Forecasting Directional Changes in the FX Markets
updated: '2026-09-27T01:47:00Z'
uuid: db3ea7e9-6006-5174-9bf0-53932d4d324f
year: 2016
---

<!-- AUTHORED REGION START -->
# Forecasting Directional Changes in the FX Markets

## Summary

The paper works within the Directional Change (DC) framework, which summarizes a market as alternating uptrends and downtrends defined by a price-move threshold rather than by fixed time intervals. Most prior forecasting work asks whether tomorrow's price will extend today's trend at all; here the authors instead ask a magnitude question: once a trend has just been confirmed at a small threshold, will it continue far enough to also trigger a directional-change confirmation at a larger threshold before it reverses?

To answer this, they define a single explanatory variable, the Overshoot Value (OSV), computed at the moment a small-threshold trend is confirmed, relative to the last confirmed directional-change event of the larger threshold. This variable is fed into a J48 (C4.5) decision tree, trained separately on uptrends and downtrends for each of three currency pairs, to forecast a binary target variable indicating whether the small-threshold trend will also become an extreme point of the larger threshold. They test the approach on EUR/CHF, GBP/CHF, and USD/JPY minute-by-minute mid-prices from January 2013 to July 2015, using different, separately chosen small and large thresholds for each pair, and compare its out-of-sample accuracy to an ARIMA benchmark.

Across all three currency pairs and both trend directions, out-of-sample forecasting accuracy exceeded 80%, consistently beating the ARIMA benchmark in every tested case. A second experiment varies the larger threshold over ten values while holding the smaller threshold fixed, showing that accuracy falls as the gap between the two thresholds widens, in step with a growing class imbalance in the target variable; a linear regression confirms this relationship is statistically significant for all three pairs.

What is new is the single-variable forecasting approach itself, and the identification of a threshold-driven limit to its usefulness: once the larger threshold is set far enough above the smaller one, the resulting class imbalance becomes severe enough that the model's accuracy drops below what a naive always-predict-no rule would achieve, which the authors flag as a boundary condition on when their approach is worth using.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Observations are the sequence of Directional Change (DC) events defined by a price threshold rather than fixed time steps: the market is treated as alternating uptrends and downtrends, each ending when price moves by the chosen threshold in the opposite direction. The forecasting target, a Boolean variable, is evaluated at the moment a DC event of the smaller threshold is confirmed and asks whether that same extreme point will also turn out to be an extreme point of a larger threshold before the trend reverses, so the prediction horizon is defined in terms of a second, larger price-move threshold rather than a fixed time span.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** EUR/CHF, GBP/CHF, and USD/JPY currency pairs
- **Venue:** not stated
- **Period:** EUR/CHF: trained 1/1/2013-30/6/2015, tested 1/7/2015-31/7/2015; GBP/CHF: trained 1/1/2013-30/4/2015, tested 1/5/2015-31/7/2015; USD/JPY: trained 1/1/2013-31/12/2014, tested 1/1/2015-31/7/2015
- **Granularity:** minute-by-minute mid-prices

## Features and Measures

- **Directional Change (DC) framework.** An approach that summarizes price movement as alternating uptrends and downtrends, each confirmed once price moves by at least a chosen threshold from the last extreme point, instead of sampling at fixed time steps.
- **Small threshold / large threshold (STheta / BTheta).** Two different Directional Change thresholds applied to the same price series at once; every extreme point confirmed under the larger threshold is guaranteed to also be an extreme point under the smaller threshold, but not vice versa.
- **Overshoot Value (OSV).** A single explanatory variable computed at a small-threshold extreme point, measuring how far the current price already lies past the last confirmed directional-change confirmation point of the larger threshold, normalized by that larger threshold.
- **Boolean target variable BBTheta.** A forecasting target that is true when a small-threshold trend's extreme point will also become an extreme point of a chosen larger threshold before the trend reverses, i.e. whether the trend will extend that far.

## Method

For each of the three currency pairs, the authors split uptrends and downtrends into separate labeled data sets over pair-specific training and out-of-sample testing windows. For each Directional-Change-confirmed extreme point at the smaller threshold, they compute the single OSV variable relative to the most recently confirmed extreme point of the larger threshold, then train a J48 (C4.5) decision tree on the training window to predict the Boolean target BBTheta. Out-of-sample accuracy is measured as the fraction of correctly forecast true and false instances, and compared against an ARIMA benchmark (R's auto.arima() function) fit to predict the same target. A second experiment repeats this procedure for ten different values of the larger threshold, with the smaller threshold fixed at 0.1%, to see how forecasting accuracy changes as the class balance of the target variable shifts, checking the relationship with a linear regression of accuracy on the larger threshold.

## Results

- Out-of-sample accuracy exceeded 80% for all three currency pairs and both trend directions, for example 0.814 and 0.820 for EUR/CHF uptrends and downtrends, 0.803 and 0.818 for GBP/CHF, and 0.831 and 0.846 for USD/JPY.
- The OSV-based approach beat the ARIMA benchmark in every tested case, for example 0.814 versus 0.589 for EUR/CHF uptrends and 0.831 versus 0.713 for USD/JPY uptrends.
- Accuracy fell as the larger threshold moved further from the fixed smaller threshold of 0.1%: for EUR/CHF uptrends accuracy dropped from 0.815 at a larger threshold of 0.13% to 0.619 at 0.22%.
- A linear regression of accuracy on the larger threshold gave a p-value below 0.01 for all three currency pairs, indicating the size of the larger threshold significantly affects forecasting accuracy.
- At wide threshold gaps the class imbalance became severe enough to hurt the model: for EUR/CHF uptrends, once the larger threshold exceeded 0.19% (imbalance fraction below 0.30), forecast accuracy fell below 0.65, worse than the 0.70 expected from always predicting the majority class.

## Limitations

- The authors state that the small and large threshold values used for each currency pair were chosen arbitrarily rather than optimized or economically motivated.
- Only three currency pairs and roughly two and a half years of minute-level data are tested, with training and testing window lengths that differ across pairs.
- Reader note: forecasting accuracy is reported separately by trend direction and by currency pair, and the paper shows it can fall below a naive always-false baseline once the class imbalance is severe enough, which the authors acknowledge only for wide threshold gaps.
- The forecast is not embedded in an actual trading strategy or backtested for profitability in this paper; the authors describe that as a next step.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/alpha-signal|alpha signal]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/backtesting|backtesting]]
- [[concepts/directional-change|Directional Change]]

## Citation

Amer Bakhach, Edward P. K. Tsang, Hamid Jalalian (2016). Forecasting Directional Changes in the FX Markets.

DOI: 10.1109/ssci.2016.7850020

Text ingested: `markdown_output/bakhach-2016-forecasting-directional-changes-fx-markets.md`, converted from `raw/ofi-event-clock/bakhach-2016-forecasting-directional-changes-fx-markets.pdf`.

Coverage of this summary: Read the entire markdown text of the paper, including the abstract, all seven numbered sections, both experiment tables (Table III and Table IV), the figure captions, and the reference list.

Known problems with the input: No publication venue or year is printed anywhere in the converted markdown; only author affiliations appear at the top, so venue is left blank and year is taken from the job file's year_hint; year from file metadata; Several equation/figure graphics (the DC-event condition, the OSV formula, and the DC-summary charts) are rendered as omitted pictures with partially OCR'd captions, and were used here only for qualitative description, not for any numbers.
<!-- AUTHORED REGION END -->