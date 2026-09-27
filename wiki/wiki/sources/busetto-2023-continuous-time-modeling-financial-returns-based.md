---
authors:
- Riccardo Busetto
- Simone Formentin
content_hash: sha256:6372a240adc0ce2a5e99a84176d986f10e968d9ef787284dc4d2ccebe2a2876d
created: 2026-09-27 01:47:00+00:00
page_id: sources/busetto-2023-continuous-time-modeling-financial-returns-based
page_type: source
publication_venue: IFAC PapersOnLine 56-2 (2023) 9318-9323
related:
- concepts/intrinsic-time
- concepts/limit-order-book
- concepts/order-imbalance
- concepts/market-microstructure-noise
- concepts/high-frequency-data
- concepts/queue-imbalance
- entities/riccardo-busetto
- entities/simone-formentin
revision_id: 1
schema_version: 2
source_hash: sha256:0f8d61898838636475606235520a26082ddcafe1cce286c77ccbec12e4863de1
source_path: markdown_output/busetto-2023-continuous-time-modeling-financial-returns-based.md
source_type: paper
tags:
- limit-order-book
- order-imbalance
- continuous-time-identification
- event-based-sampling
- lobster-dataset
- return-prediction
- clock-intrinsic
- asset-equity
- harvest-core
title: Continuous-time modeling of financial returns based on Limit Order Book data
updated: '2026-09-27T01:47:00Z'
uuid: dc0a291a-e1d6-5bc2-be9c-ac4bf9d9c33e
year: 2023
---

<!-- AUTHORED REGION START -->
# Continuous-time modeling of financial returns based on Limit Order Book data

## Summary

The paper asks how to model the relationship between limit order book state and near-term returns without forcing the inherently event-driven, irregularly-timed order book onto an arbitrary fixed sampling grid. The authors frame this as a system identification problem from a control-systems perspective, which they say has not previously been applied to limit order book dynamics. They first introduce a new regressor, Base Imbalance, defined from how tightly or loosely consecutive price levels on the bid and ask sides are spaced across the top ten levels of the book, and compare it against an existing regressor, Depth Imbalance, which instead compares resting volume on each side.

Working with the LOBSTER benchmark dataset for one trading day (AMZN as the main stock, with AAPL and GOOG reported in an appendix), the authors keep only the observations where an event actually changes the mid price, discarding the majority of book updates that leave the mid unchanged, and drop the first 60 minutes of trading to avoid the open. On this cleaned, irregularly-sampled series they estimate a continuous-time output-error model relating Base Imbalance to the following return using the Simple Refined Instrumental Variable method extended to irregular sampling (SRIVC), splitting each day into a first-half training set and second-half test set.

Base Imbalance shows a materially stronger linear relationship with returns than Depth Imbalance, both sample-by-sample and especially when the data are grouped into deciles by regressor value. The fitted continuous-time model beats a moving-average benchmark on out-of-sample fit and on the fraction of times it predicts the correct direction of the next return, and this improves further when the sample is restricted to observations with a large absolute Base Imbalance.

What is new is the Base Imbalance regressor itself, and the use of continuous-time system identification (rather than a fixed-interval discrete model) as a way to model limit order book-driven returns while keeping the data's native event timing and some model interpretability.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Observations are kept only at book events that actually move the mid price, using the rule that a return is measured from one price-changing event to the next price-changing event; all intervening book updates that leave the mid price unchanged are discarded rather than sampled. The authors argue this avoids both the oversampling of a very fine fixed grid and the information loss of a coarse fixed grid (citing the Epps effect), and note this native event timing is what motivates a continuous-time rather than discrete-time model.

## Data

- **Asset class:** Equities
- **Instruments:** AMZN (main analysis), with AAPL and GOOG reported in an appendix
- **Venue:** not stated (LOBSTER limit order book reconstruction dataset)
- **Period:** single trading day, 2016-06-21, active trading hours only (first 60 minutes removed)
- **Granularity:** event-by-event order book reconstruction, top 10 price levels each side, filtered down to events that change the mid price

## Features and Measures

- **Depth Imbalance (DI).** An existing order-book imbalance measure, normalized between -1 and 1, that compares the resting volume on the bid side against the ask side near the top of book.
- **Base Imbalance (BI).** A new regressor proposed in this paper, built from how closely spaced the resting price levels are on the bid side versus the ask side across the top ten levels, on the reasoning that tightly spaced orders on one side reflect more competitive, urgent traders on that side.

## Method

After cleaning the LOBSTER data to keep only mid-price-changing events and dropping the market-open period, the authors first check whether Depth Imbalance or Base Imbalance is more informative, using the Pearson correlation coefficient both on raw observations and on decile-averaged observations. They then fit a continuous-time output-error dynamical model linking Base Imbalance to the following return, using the Simple Refined Instrumental Variable method adapted to continuous time and to irregularly sampled data (SRIVC), with model order chosen by a sensitivity analysis over RMSE normalized by the return's standard deviation. The model is trained on the first half of the trading day and tested on the second half, and is compared against a Moving Average benchmark model. Evaluation metrics are RMSE, R-squared, RMSE normalized by the standard deviation of returns, and a directional hit rate (the fraction of predictions with the same sign as the realized return).

## Results

- For AMZN, the raw sample-to-sample correlation with returns was 0.0668 for Depth Imbalance versus -0.1763 for Base Imbalance, so Base Imbalance is the more informative of the two even though both are described as weak by the paper's own correlation-strength bands (weak: 0.2 to 0.45; moderate: 0.45 to 0.75; strong: at least 0.75).
- When observations are grouped into deciles by regressor value, the correlation with returns rises sharply for Base Imbalance, reaching an absolute value above 0.97 in each of the three stocks studied, versus a weaker and less stock-consistent decile correlation for Depth Imbalance.
- The fitted continuous-time model, using all events, achieved an R-squared of 0.0406 on the test half of the day and a directional hit rate of 0.5318, versus an R-squared of 0.0041 and hit rate of 0.5305 for the Moving Average benchmark.
- Restricting to observations where the absolute Base Imbalance is at least 0.25 raised the continuous-time model's test R-squared to 0.1857 and its directional hit rate to 0.5915, both above the corresponding Moving Average benchmark figures.
- The frequency response of the fitted model shows the estimated effect of Base Imbalance on returns is larger at higher frequencies, i.e. fast changes in Base Imbalance matter more for near-term returns than slow ones.

## Limitations

- The authors describe this as a preliminary work and note it assumes a constant probability distribution for the data across the trading day.
- The main results are estimated on a single trading day (2016-06-21) for one stock (AMZN), with only two additional stocks (AAPL, GOOG) shown in an appendix.
- The explained variance (R-squared) of the fitted model remains low in absolute terms even in the best-filtered case.
- Reader note: only large-cap US technology stocks are examined; no bonds or other asset classes are covered.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/queue-imbalance|Queue Imbalance]]
- [[entities/riccardo-busetto|Riccardo Busetto]]
- [[entities/simone-formentin|Simone Formentin]]

## Citation

Riccardo Busetto, Simone Formentin (2023). Continuous-time modeling of financial returns based on Limit Order Book data. IFAC PapersOnLine 56-2 (2023) 9318-9323.

DOI: 10.1016/j.ifacol.2023.10.218

Text ingested: `markdown_output/busetto-2023-continuous-time-modeling-financial-returns-based.md`, converted from `raw/ofi-event-clock/busetto-2023-continuous-time-modeling-financial-returns-based.pdf`.

Coverage of this summary: Read the entire paper markdown, including abstract, introduction, problem statement, exploratory data analysis, continuous-time system identification section, conclusions, and the appendix table for AAPL and GOOG.

Known problems with the input: Several equations (Base Imbalance and Depth Imbalance definitions, the continuous-time model form, the optimization objective) are rendered as omitted pictures in the converted markdown, so their exact mathematical form could not be verified beyond the plain-language description already given in the text.
<!-- AUTHORED REGION END -->