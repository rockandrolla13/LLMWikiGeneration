---
authors:
- Ioane Muni Toke
- Nakahiro Yoshida
content_hash: sha256:b85ac0e76235186ecf1e891852148ef9ed1a57afc166322b8b14ea50ec70f4a8
created: 2026-09-27 01:47:00+00:00
page_id: sources/toke-2022-marked-point-processes-intensity-ratios-limit
page_type: source
related:
- concepts/trade-clock
- concepts/hawkes-processes
- concepts/limit-order-book
- concepts/order-imbalance
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/order-flow-prediction
- concepts/trade-classification
revision_id: 1
schema_version: 2
source_hash: sha256:45b874769839f86d2407943042f5e5c332a911f0a8dad6cb5d30b5026b053b8d
source_path: markdown_output/toke-2022-marked-point-processes-intensity-ratios-limit.md
source_type: paper
tags:
- hawkes-processes
- limit-order-book
- intensity-ratio-model
- marked-point-processes
- quasi-likelihood
- trade-sign-prediction
- market-microstructure
- high-frequency-trading
- clock-trade
- asset-equity
- harvest-relevant
title: Marked point processes and intensity ratios for limit order book modeling
updated: '2026-09-27T01:47:00Z'
uuid: 3770e100-4ba2-5acb-b453-0ae171961a5e
year: 2020
---

<!-- AUTHORED REGION START -->
# Marked point processes and intensity ratios for limit order book modeling

## Summary

This paper extends an earlier ratio-based intensity framework (Muni Toke & Yoshida, 2020) to marked point processes, adding a third multiplicative term to the intensity that captures the conditional distribution of a mark attached to each event, on top of a shared baseline intensity and a state-dependent, process-specific component. The authors prove that quasi-maximum-likelihood and quasi-Bayesian estimators of the resulting two-step ratio model converge to a mixed Gaussian limit (Theorem 3.1), and check this convergence numerically by simulating a two-process, two-mark example over a range of sample horizons.

The method is then applied to limit order book data: the two processes are bid- and ask-side market orders, and the mark distinguishes an "aggressive" order that moves the price from a "non-aggressive" one that does not. Covariates tested include order-book imbalance, the sign of the last market order, a signed-spread indicator, and separate univariate Hawkes-process log-intensities computed for aggressive, non-aggressive, and pooled bid/ask order flows. Estimation proceeds in two successive ratio steps (first predicting side, then aggressiveness), and covariate sets are compared across stocks and days using a QAIC-type in-sample selection criterion, with a held-out, next-day prediction exercise used to judge out-of-sample performance against a multivariate Hawkes benchmark and the earlier non-marked ratio model.

Across 36 Euronext Paris stocks over 2015, imbalance and order-side-specific Hawkes covariates are the most frequently selected inputs, and the signed-spread covariate becomes more important as a stock's typical spread widens beyond about a tick. Out-of-sample, the best marked ratio model clearly outperforms the Hawkes benchmark and the earlier non-marked ratio model at jointly predicting the side and aggressiveness of the next market order.

What is new is the two-step marked-ratio construction itself: it lets clustering (via Hawkes-style covariates) and state-dependency (via imbalance and spread) be modeled jointly without ever having to specify the shared baseline intensity, and, because the ratio construction does not require precise event timestamps except where Hawkes covariates are used, it is more forgiving of the limitations of the reconstructed order-book timestamps than pure Hawkes approaches.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Observations are individual market order arrivals (bid or ask side) on the reconstructed limit order book; each arrival also carries a binary mark for whether it is price-moving (aggressive) or not. The model is fitted on one trading day and its fitted intensities/ratios are then used, unchanged, to predict the side and aggressiveness of every incoming market order on the following trading day, so the prediction horizon is simply "the next market order."

## Data

- **Asset class:** Equities
- **Instruments:** 36 stocks traded on Euronext Paris
- **Venue:** Euronext Paris
- **Period:** the whole year 2015 (roughly 200 trading days per stock, with some days missing for some stocks)
- **Granularity:** tick-by-tick TRTH (Thomson-Reuters Tick History) transaction and order-book-update files, millisecond timestamps; unique-timestamp aggregation is used only when Hawkes covariates are involved

## Features and Measures

- **order-book imbalance (Z1).** difference between the quantity available at the best bid and at the best ask, divided by their sum.
- **last order sign (Z2).** the side (bid/ask) of the most recent market order, coded as +/-1.
- **signed spread indicator (Z3).** the last order's sign multiplied by an indicator of whether the current spread is above or below the stock's median spread.
- **Hawkes log-intensity covariates (Z4-Z9).** log-intensities from separately fitted univariate Hawkes processes for aggressive bid orders, non-aggressive bid orders, aggressive ask orders, non-aggressive ask orders, all bid orders, and all ask orders, used as covariates in the ratio model.
- **two-step marked intensity ratio model.** the paper's core construction: the ratio of a state-dependent to an unspecified baseline intensity is used first to predict order side, then, conditional on side, a second ratio predicts the order's mark (aggressiveness).

## Method

Estimation uses quasi-maximum-likelihood and quasi-Bayesian estimators applied separately to two successive ratio models: a first-step ratio for the side (bid/ask) of the process, and a second-step ratio for the mark (aggressiveness) conditional on side. Theorem 3.1 establishes that both estimator types converge, at the standard root-time rate, to a mixed Gaussian law under stationarity and mixing conditions on the covariate processes, and a simulation of a two-process, two-mark example is used to check that the estimators' empirical standard deviations match the theoretical asymptotic variance across a range of sample horizons.

On the Euronext Paris data, for each stock and trading day the authors fit three ratio models (side, bid aggressiveness, ask aggressiveness) for many candidate covariate sets, computing Hawkes-based covariates first where needed, and select the best-fitting covariate set per day using a QAIC-type criterion; selection frequencies are then aggregated across stocks and days.

Out-of-sample performance is judged with a next-day prediction exercise: a model is fit on one trading day and its fitted parameters are used to compute intensities or ratios at every instant of the following trading day (assuming instantaneous computation), predicting each incoming market order's type as the type of highest intensity/ratio; accuracy is reported separately for side, for aggressiveness, and jointly (global), against a plain multivariate Hawkes benchmark and the earlier non-marked ratio benchmark.

## Results

- Across 36 Euronext Paris stocks in 2015, in-sample QAIC selection favours covariate sets combining order-book imbalance with Hawkes-based intensity covariates for aggressive and non-aggressive orders on both sides.
- The three covariate sets most often chosen for predicting order side are selected on about 80% of trading days on average across stocks.
- The frequency with which the signed-spread covariate is selected rises as a stock's mean observed spread widens from 1 to about 2 ticks, with a possible break point between 1.5 and 2 ticks, and stays high for wider-spread stocks.
- Out-of-sample, a plain multivariate Hawkes benchmark predicts the side and aggressiveness of the next market order with accuracy in a 40% to 60% range across stocks, averaging 50%.
- The non-marked ratio benchmark model modestly improves on the Hawkes benchmark, mainly through better side prediction: side accuracy of 0.808 versus 0.781 for the Hawkes model.
- The best-performing marked ratio model, which uses imbalance and Hawkes covariates for both the side and aggressiveness steps, reaches side accuracy 0.877 and aggressiveness accuracy 0.774.
- That best model's global accuracy (correct side and correct aggressiveness jointly) ranges from 60% to 80% across stocks, averaging 67%, i.e. roughly two out of three incoming market orders are correctly classified on both dimensions.

## Limitations

- The out-of-sample prediction exercise is explicitly described by the authors as theoretical, since it assumes intensities or ratios are available instantaneously at every point in time, ignoring any computation latency.
- Reader note: the empirical study covers a single exchange (Euronext Paris), a single year (2015), and equities only; no bonds or other asset classes or venues are tested.
- Reader note: the asymptotic theory (Theorem 3.1) relies on stationarity and strong-mixing assumptions on the covariate processes that are convenient for proofs but are not directly verified on the real intraday data used in the application.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/trade-classification|trade classification]]

## Citation

Ioane Muni Toke, Nakahiro Yoshida (2020). Marked point processes and intensity ratios for limit order book modeling.

DOI: 10.1007/s42081-021-00137-9

Text ingested: `markdown_output/toke-2022-marked-point-processes-intensity-ratios-limit.md`, converted from `raw/ofi-event-clock/toke-2022-marked-point-processes-intensity-ratios-limit.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, the marked-ratio-model construction and quasi-likelihood estimation sections, the numerical simulation illustration, the limit-order-book application (data, estimation procedure, QAIC model selection, out-of-sample prediction), the conclusion, the reference list, and skimmed the mathematical proof in Appendix A.

Known problems with the input: The converted markdown replaces all equations, figures and several tables with '[picture omitted]' placeholders, so exact formulas and some figure values could not be verified beyond what is stated in prose or in the surviving tables.
<!-- AUTHORED REGION END -->