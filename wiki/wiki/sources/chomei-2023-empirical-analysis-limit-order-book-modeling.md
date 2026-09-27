---
authors:
- Shunya Chomei
content_hash: sha256:01bbbe5433c6a0aa6b68da9fed0e04bc471aaf3903a43b786775816103bf4c43
created: 2026-09-27 01:47:00+00:00
page_id: sources/chomei-2023-empirical-analysis-limit-order-book-modeling
page_type: source
related:
- concepts/event-clock
- concepts/order-flow-imbalance
- concepts/order-flow
- concepts/order-flow-prediction
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
source_hash: sha256:0e10a464732100b8c809f483a84c581fe8940ccfae14ddef6667afadd56496b0
source_path: markdown_output/chomei-2023-empirical-analysis-limit-order-book-modeling.md
source_type: paper
tags:
- limit-order-book
- order-flow-imbalance
- point-processes
- trade-sign-prediction
- tokyo-stock-exchange
- model-selection
- clock-event
- asset-equity
- harvest-relevant
title: Empirical analysis in limit order book modeling for Nikkei 225 Stocks with
  Cox-type intensities
updated: '2026-09-27T01:47:00Z'
uuid: c3450d76-e46e-5cb1-9e6b-8daff7a67074
year: 2023
---

<!-- AUTHORED REGION START -->
# Empirical analysis in limit order book modeling for Nikkei 225 Stocks with Cox-type intensities

## Summary

The paper asks whether a Cox-type point-process model of order flow, originally validated on Paris Stock Exchange data, also works for predicting the direction of the next market order on the Tokyo Stock Exchange, and whether adding further order-book imbalance covariates and using more historical days of data can improve that prediction.

Building directly on Muni Toke and Yoshida's ratio-of-Cox-intensities framework, the paper models bid and ask market-order arrivals as point processes whose intensities share a common unobserved baseline and differ only through observable covariates: quote imbalances at several depth levels, cumulative-depth imbalances, the sign of the last trade, the product of that sign with a spread indicator, and lagged versions of the imbalance covariates. Parameters are estimated by quasi-maximum likelihood on tick data for 222 Tokyo Stock Exchange stocks between March 2019 and February 2020, testing various subsets of these covariates and, separately, how many days of historical data should be used to calibrate the model before predicting the next day's, or next several days', order signs. Model choice among covariate combinations is also checked using three information-criterion variants: quasi-AIC, quasi-consistent AIC and quasi-BIC.

The base model using just the best-quote imbalance already predicts the sign of the next market order correctly most of the time, and accuracy improves further when imbalances a few ticks away from the best quote, the previous imbalance one order back, the last trade's sign, and the sign-times-spread indicator are added. Predicting whether the sign will flip, rather than just its level, is harder and gets worse, not better, once the last trade's sign is added as a covariate. Recalibrating the model every one to two weeks rather than daily raises accuracy slightly, while much longer calibration windows lower it, which the author reads as evidence that the true covariate coefficients drift over time. Models with fewer parameters but similar accuracy tend to be preferred by the information criteria, and the criteria's preferred models track the accuracy-based rankings from the prediction study.

The contribution over the original Paris Stock Exchange study is showing that the same ratio-of-intensities approach transfers to the Tokyo market and to a much larger cross-section of stocks, introducing higher-depth and lagged imbalance covariates that were not in the original covariate set, and directly comparing how the look-back window used for calibration affects prediction accuracy.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

The model treats bid and ask market-order arrivals as point processes; the estimated ratio of intensities predicts the side (bid or ask) of the very next market order after the current time t. Predictions are made and scored order-by-order, on whether the next market order's sign matches the predicted side, not on any fixed time grid, and parameters are recalibrated using a rolling window of l trading days of order-book history to predict the following l days.

## Data

- **Asset class:** Equities
- **Instruments:** 222 stocks traded on the Tokyo Stock Exchange (the list is given in an appendix)
- **Venue:** Tokyo Stock Exchange
- **Period:** March 2019 to February 2020
- **Granularity:** Individual market-order, limit-order and cancellation events (tick data); more than 100 million market orders and more than 1 billion limit orders and cancellations across the 222 stocks are used for estimation

## Features and Measures

- **n-th imbalance i_n(t).** A measure built from the number of shares available at the n-th best quote on the bid versus the ask side at time t, close to +1 when there is very little volume on the ask side (signaling likely price rises) and close to -1 when there is very little volume on the bid side.
- **Cumulative-depth imbalance.** The same imbalance idea but computed from the cumulative quoted volume up to the n-th quote level on each side, rather than the volume at a single level.
- **Sign of the last trade.** An indicator that is -1 if the most recent market order was an ask-side (sell) trade and +1 if it was a bid-side (buy) trade.
- **Sign-spread product.** The last trade's sign multiplied by an indicator that is +1 when the current bid-ask spread is above its mean and -1 when it is below.
- **Lagged imbalance covariates.** The same imbalance measures evaluated at the time of an earlier market order, m orders back from the present, giving the model a short memory of recent imbalance history.

## Method

Bid and ask market-order counts are modeled as point processes whose intensities are written as a common, unobserved baseline intensity multiplied by a covariate-dependent factor; taking the ratio of the bid and ask intensities cancels the baseline, so only the covariates' relative effect on the trade-sign decision needs to be estimated. Parameters are fit by a quasi-maximum-likelihood procedure over a chosen window of trading days, under regularity conditions bounding the moments of the baseline intensity and covariates and requiring a non-degenerate information tensor; the paper reports that the resulting estimator is asymptotically normal, citing the proof from the earlier Muni Toke and Yoshida paper this work extends.

The fitted models are judged in two ways. First, using the previous day's (or previous l days') estimated parameters, the next market order's side is predicted as bid if the model's bid-side probability exceeds 0.5 and ask otherwise, and the paper reports how often that prediction is correct, separately reporting accuracy on the subset of orders where the sign actually changes from the previous order. Second, nested covariate sets are compared using three quasi-likelihood information criteria (quasi-AIC, quasi-consistent AIC, quasi-BIC), counting across the 222 stocks how often each covariate combination is selected as best under each criterion.

## Results

- Using only the best-quote imbalance as a covariate, the model predicts the next market order's side with about 73% accuracy across the 222 stocks.
- Adding the imbalance measured one to two ticks away from the best quote raises accuracy only slightly above the best-quote-only model.
- Adding the previous imbalance from one order back raises accuracy to about 73.5%; adding the last trade's sign and the sign-spread indicator on top of the base imbalance raises it further, to about 75.5% and then about 77%.
- Including imbalances measured more than 3 ticks away from the best quote, or from more than 2 orders in the past, does not improve accuracy and sometimes slightly reduces it.
- Predicting whether the trade sign will flip from the previous order is harder: accuracy is about 68% with imbalance covariates alone and above 70% with past imbalances added, but drops to 50%-55% once the last trade's sign and spread indicator are included, which the author attributes to consecutive same-side orders dragging predictions toward the previous sign.
- Recalibrating parameters every one to two weeks instead of daily raises accuracy on the richest covariate model from about 77% to about 78%, while lengthening the estimation window too far reduces accuracy again, consistent with the true parameters drifting over time.
- The information criteria tend to favor models with fewer parameters and accuracy similar to larger models; quasi-consistent AIC and quasi-BIC in particular favor the smaller imbalance-plus-one-lag model, while quasi-AIC more often favors larger models.

## Limitations

- The prediction test only checks the direction (bid vs ask) of the very next market order, not the size or timing of the resulting price move.
- Recalibration windows longer than a few weeks reduce accuracy, which the paper attributes to the true covariates drifting over time, but it does not otherwise model or correct for this drift.
- The paper only tests the model on two markets (Paris, from the earlier study, and Tokyo, here), both analyzed with the same Cox-type modeling family.
- Reader note: the sample period (March 2019 to February 2020) predates the COVID-19 volatility shock, so results may not describe how the model performs under market stress.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]

## Citation

Shunya Chomei (2023). Empirical analysis in limit order book modeling for Nikkei 225 Stocks with Cox-type intensities.

DOI: 10.48550/arxiv.2302.01668

Text ingested: `markdown_output/chomei-2023-empirical-analysis-limit-order-book-modeling.md`, converted from `raw/ofi-event-clock/chomei-2023-empirical-analysis-limit-order-book-modeling.pdf`.

Coverage of this summary: Read the full converted markdown text: abstract, introduction, the model and estimation-procedure section, both empirical-study subsections (prediction and model selection), the conclusion, and skimmed the reference list and the stock-list appendix.

Known problems with the input: Most equations and the theorem statement are rendered as omitted images ('picture... intentionally omitted'), so the exact functional forms of the intensity, covariates and estimator could not be verified beyond what is described in prose; The appendix's 222-stock list is heavily OCR-garbled (codes, names and industries run together across table cells) and was not used beyond confirming the stock count; No journal or venue name is stated in the extracted text; treated here as an unstated/working-paper venue.
<!-- AUTHORED REGION END -->