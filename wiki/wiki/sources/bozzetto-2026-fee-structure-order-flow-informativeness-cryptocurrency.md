---
authors:
- Christian Bozzetto
- Imtiaz Sifat
- Narmin Nahidi
content_hash: sha256:5fc56b8209060a3ebbb0549ca25dc085a92356628dc6ea3b6dc20754ce8ff6f0
created: 2026-09-27 01:47:00+00:00
page_id: sources/bozzetto-2026-fee-structure-order-flow-informativeness-cryptocurrency
page_type: source
publication_venue: Book chapter in AI, FinTech, and the Future of Robo-Advisory (Contributions
  to Finance and Accounting, Springer), edited by N. Nahidi and A. Zarifis.
related:
- concepts/order-flow-imbalance
- concepts/order-flow
- concepts/price-impact
- concepts/market-microstructure
- concepts/informed-trading
- concepts/adverse-selection
revision_id: 1
schema_version: 2
source_hash: sha256:6d37c8b3fd48399d0183bd429ff09cb4e2003ff1886fc74c37d3ac3bd386f997
source_path: markdown_output/bozzetto-2026-fee-structure-order-flow-informativeness-cryptocurrency.md
source_type: book
tags:
- cryptocurrency
- order-flow
- trading-fees
- market-microstructure
- price-discovery
- binance
- xgboost
- clock-calendar
- asset-crypto
- harvest-relevant
title: Fee Structure and Order Flow Informativeness in the Cryptocurrency Market
updated: '2026-09-27T01:47:00Z'
uuid: 28717785-7e09-5e12-8e6d-d2758d9aad27
year: 2026
---

<!-- AUTHORED REGION START -->
# Fee Structure and Order Flow Informativeness in the Cryptocurrency Market

## Summary

The paper asks whether cryptocurrency exchange fee structures change how informative order flow is about prices, using Binance's abrupt switch from zero-fee to commission-based BTC/USDT trading around March 2023 as a natural experiment.

Using nanosecond-level Binance order book data from July 31, 2022 to July 31, 2023, plus executed-trade data from March 15 to July 31, 2023, the authors build order flow imbalance (OFI, from order book events, following Cont, Kukanov and Stoikov 2014) and trade flow imbalance (TFI, from executed trades), and regress contemporaneous mid-price changes on each at frequencies from 1 second to 1 hour, separately before and after the fee change, with a Chow test for a structural break and an XGBoost model as a non-linear robustness check.

The main finding is that OFI's explanatory power for mid-price changes rose substantially after fees were introduced, and that TFI consistently explains more of the price change than OFI in both regimes, with the combined OFI-and-TFI model performing best overall. The Chow test confirms a structural break at the fee-change date, and the XGBoost feature-importance analysis ranks TFI and OFI as the two most important predictors, ahead of intraday time-of-day features.

What is new is the interpretation: rather than fees being a pure friction that degrades market quality, the authors argue fees act as a screening mechanism that filters out uninformative order flow, so a completely zero-fee market can be less informationally efficient than one with modest trading costs.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Order flow imbalance (from order book events) and trade flow imbalance (from executed trades) are computed as cumulative signed contributions and then resampled into fixed calendar-time bins of 1 second, 10 seconds, 1 minute, 10 minutes, and 1 hour; mid-price change over each bin is regressed contemporaneously on the imbalance measured over that same bin (an explanatory/contemporaneous regression, not a forecast of a future bin), separately for the periods before and after the March 2023 fee change. The XGBoost model is instead a genuine held-out prediction exercise, using a 70/30 train-test split.

## Data

- **Asset class:** Crypto
- **Instruments:** BTC/USDT trading pair
- **Venue:** Binance
- **Period:** Order book data from July 31, 2022 to July 31, 2023, spanning Binance's March 2023 shift from zero-fee to commission-based trading (the empirics split the sample on March 15, 2023); trade data from March 15, 2023 to July 31, 2023.
- **Granularity:** Nanosecond-level order book states (best bid/ask price and size up to 20 levels deep), resampled to frequencies from 1 second to 1 hour for the regression analysis.

## Features and Measures

- **Order flow imbalance (OFI).** Following Cont, Kukanov and Stoikov (2014), the sum over a time window of signed contributions from order book events that change bid or ask size at the best level, capturing net changes in demand versus supply.
- **Trade flow imbalance (TFI).** An analogous signed-imbalance measure built from executed trade data rather than order book (quote) events, intended to capture information in market orders specifically.

## Method

Contemporaneous OLS regressions of mid-price change on OFI, separately on TFI, and on both together are estimated at five resampling frequencies (1 second to 1 hour), separately for the periods before and after the March 2023 fee change, and compared via R-squared. A Chow test is used to formally test for a structural break in the OFI-mid-price relationship around the fee change. As a robustness check, an XGBoost gradient-boosting model is fit to predict mid-price changes from OFI, TFI, and time-of-day features (minute, hour, day of week), using a 70/30 train-test split with Bayesian-optimization hyperparameter tuning, and compared against OLS by mean absolute error and by feature importance.

## Results

- The hourly R-squared of mid-price change on OFI alone rose from 5.03% before the March 2023 fee change to 11.15% after.
- At the 10-minute frequency, OFI's R-squared rose from 4.04% before the fee change to 21.55% after.
- In the post-fee period, TFI's hourly R-squared of 51.78% exceeded OFI's hourly R-squared of 11.15%, and the combined OFI-and-TFI model reached its highest R-squared, 56.30%, at the 10-minute frequency.
- A Chow test comparing the pre- and post-fee-change OFI regressions produced an F-statistic of 1977.61 (p<0.01), rejecting the null hypothesis of no structural break.
- In the XGBoost feature-importance analysis for predicting mid-price changes, TFI (44.61%) and OFI (35.01%) were the two most important predictors, ahead of the minute-of-hour (12.73%) and hour-of-day (7.54%) features; day-of-week importance was negligible.
- XGBoost reduced out-of-sample mean absolute error to 532.34 versus 595.69 for OLS; an initial overfitting gap (362.15 training MAE versus 574.29 testing MAE) was narrowed by Bayesian hyperparameter tuning to 511.35 training versus 532.34 testing.

## Limitations

- The OFI/TFI-versus-mid-price regressions are contemporaneous (same time-bin), not one-step-ahead forecasts; the authors themselves note that post-fee OFI's predictive power for one-step-ahead price changes is negligible.
- The analysis covers a single trading pair (BTC/USDT) on a single exchange (Binance) over one year, so the fee-screening result may not generalize to other assets, venues, or fee schedules.
- Reader note: the before period (through mid-March 2023) contains the November 2022 FTX collapse, a major market disruption that the authors themselves flag as affecting the bid-ask spread series, which could confound a clean before/after fee comparison.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-flow|order flow]]
- [[concepts/price-impact|price impact]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/adverse-selection|adverse selection]]

## Citation

Christian Bozzetto, Imtiaz Sifat, Narmin Nahidi (2026). Fee Structure and Order Flow Informativeness in the Cryptocurrency Market. Book chapter in AI, FinTech, and the Future of Robo-Advisory (Contributions to Finance and Accounting, Springer), edited by N. Nahidi and A. Zarifis..

DOI: 10.1007/978-3-032-18109-1_13

Text ingested: `markdown_output/bozzetto-2026-fee-structure-order-flow-informativeness-cryptocurrency.md`, converted from `raw/ofi-event-clock/bozzetto-2026-fee-structure-order-flow-informativeness-cryptocurrency.pdf`.

Coverage of this summary: Read the entire chapter front to back: abstract, introduction, literature review and hypotheses, data and methodology, results (fee-structure impact, structural break analysis, machine learning robustness check), and implications/conclusion.
<!-- AUTHORED REGION END -->