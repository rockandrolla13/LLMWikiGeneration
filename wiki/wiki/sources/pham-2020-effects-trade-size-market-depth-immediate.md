---
authors:
- Manh Cuong Pham
- Heather Margot Anderson
- Huu Nhan Duong
- Paul Lajbcygier
content_hash: sha256:5a2e842c46f11d8b434b7f5dc1f9662b2d8dc8514bf831fe263eb0708bd9ec8a
created: 2026-09-27 01:47:00+00:00
page_id: sources/pham-2020-effects-trade-size-market-depth-immediate
page_type: source
related:
- concepts/trade-clock
- concepts/price-impact
- concepts/limit-order-book
- concepts/order-imbalance
- concepts/metaorder
- concepts/market-microstructure
- concepts/informed-trading
revision_id: 1
schema_version: 2
source_hash: sha256:ecc9c7c5f72b2d54fea8c6fa82713ed80c6bb0e5676be629d86f8dff5da28c39
source_path: markdown_output/pham-2020-effects-trade-size-market-depth-immediate.md
source_type: paper
tags:
- price-impact
- market-depth
- order-splitting
- limit-order-book
- market-microstructure
- out-of-sample-forecasting
- australian-equities
- clock-trade
- asset-equity
- harvest-core
title: The effects of trade size and market depth on immediate price impact in a limit
  order book market
updated: '2026-09-27T01:47:00Z'
uuid: 70fce246-d438-50ca-825e-4fc41c362f57
year: 2020
---

<!-- AUTHORED REGION START -->
# The effects of trade size and market depth on immediate price impact in a limit order book market

## Summary

The paper asks whether information on quoted market depth can improve out-of-sample forecasts of the immediate price impact of individual trades in a limit-order-book market, and whether such a model can be used to quantify the benefit of splitting large orders into smaller ones. The authors build a threshold-type model for Australian Securities Exchange stocks in which a market depth indicator equals one when a trade's volume is at least as large as the quoted depth at the best opposite-side price just before the trade, and zero otherwise; the indicator multiplies a linear function of trade attributes (scaled volume, market capitalization, volatility) and time-series variables (price-impact lags and day/time dummies), so the model predicts zero impact whenever the indicator is zero.

Using tick-by-tick data on 92 S&P/ASX200 stocks from 2007 to 2013, split into five market-capitalization groups, the authors estimate separate buy and sell models by least squares over rolling nine-month windows and forecast one month ahead, repeating this 75 times to cover October 2007 to December 2013. They compare their depth-augmented models against non-depth versions, the nonlinear models of Zhou (2012) and Lillo et al. (2003), and a naive always-zero-impact model, judging accuracy by out-of-sample mean squared error and mean absolute error together with Giacomini-White conditional predictive-accuracy tests and Hansen et al. Model Confidence Set tests.

The depth indicator is the largest single contributor to forecast accuracy, cutting out-of-sample MSE and MAE by about 60% relative to non-depth models, with price-impact dynamics contributing a further 5-6% and intraday/day-of-week effects a smaller additional gain. The depth-augmented model is the single best model in more than 93% (86%) of the 75 out-of-sample windows judged by MSE (MAE), and stays in the confidence set of best models more than 97% (90%) of the time. Splitting a large trade into a series of same-sign smaller trades is found to reduce its aggregate price impact by between 60% and 82% on average, with a split into 10 trades close to the largest saving.

New in the paper is the use of the depth indicator as a multiplicative on/off switch rather than a standard regressor, an adaptation of heterogeneous-autoregressive (HAR) lag structure from the volatility literature to price-impact dynamics, and a demonstration that the same depth indicator also predicts future order imbalance and the gap between immediate and permanent price impact, linking the paper's immediate-impact model to the wider order-flow literature.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Observations are individual trades in tick-by-tick data; each trade's immediate price impact is the log change between the mid-quote right after and right before that trade, and all regressors are measured strictly before the trade. Price-impact dynamics are captured by moving averages of past same-signed price impacts over the previous 1, 5, 20 and 50 same-direction trades. A separate order-splitting analysis aggregates consecutive same-sign, same-day trades into an artificial single trade to compare its predicted price impact with the trades' combined observed impact. A secondary analysis measures order imbalance and the price impact gap over fixed 5- and 30-minute calendar intervals following a trade.

## Data

- **Asset class:** Equities
- **Instruments:** 92 S&P/ASX200 stocks, divided into five market-capitalization groups (12 stocks in the largest group, 20 stocks in each of the other four)
- **Venue:** Australian Securities Exchange (ASX)
- **Period:** In-sample estimation from January 2007; out-of-sample forecasts run October 2007 to December 2013 over 75 rolling one-month windows
- **Granularity:** Tick-by-tick individual trade records (buyer/seller-initiated) merged with best bid/ask quote data, plus daily shares-outstanding data for market capitalization

## Features and Measures

- **Market depth indicator.** A dummy variable equal to one when a trade's volume is at least as large as the quoted depth at the best opposite-side price immediately before the trade, and zero otherwise; it multiplicatively gates the rest of the price-impact model so predicted impact is zero when depth exceeds trade size.
- **Scaled trade volume.** A trade's share volume divided by the running average same-day, same-direction volume of all trades up to and including that trade.
- **Market capitalization variable.** The mid-quote price times the number of shares outstanding for the stock just prior to the trade.
- **Pre-trade volatility.** The standard deviation of mid-quote returns from the first trade of the day up to just before the current trade.
- **HAR-style price-impact lags.** Moving averages of the previous 1, 5, 20 and 50 same-direction trades' price impacts, adapting Corsi's heterogeneous-autoregressive structure from realized volatility to transaction-time price-impact dynamics.
- **Order imbalance and price impact gap.** Order imbalance is buy minus sell volume over total volume in a fixed interval after a trade; the price impact gap is the signed difference between permanent price impact over that interval and the trade's immediate price impact.

## Method

The immediate price impact model multiplies the depth indicator by a linear function of trade attributes (scaled volume, market capitalization, volatility) and time-series variables (HAR-style lags of past price impact at 1, 5, 20 and 50 same-direction trades, plus day-of-week and time-of-day dummies), so predicted impact is forced to zero whenever the indicator is zero. Separate models are estimated for buys and sells within each of five market-capitalization groups (12 stocks in the largest group, 20 in each of the other four), using pooled least squares over nine-month rolling in-sample windows and one-month-ahead forecasts, rolled forward 75 times to cover October 2007 to December 2013; all continuous variables are winsorized at the 1st and 99th percentiles within each stock, direction and window.

Out-of-sample forecast accuracy is compared using mean squared error and mean absolute error, pairwise Giacomini-White conditional predictive-accuracy tests, and Hansen et al. Model Confidence Set tests run with a stationary bootstrap of 1500 replications at a 5% significance level. An order-splitting exercise re-uses the best-performing model to estimate the unobserved price impact of an artificial trade that aggregates a run of consecutive same-sign, same-day small trades, and compares this to the trades' observed combined impact. A further regression links the depth indicator to subsequent order imbalance and the price impact gap over fixed post-trade intervals.

## Results

- Adding the market depth indicator to the HARX and LX models cuts their out-of-sample MSE and MAE by about 60% on average.
- The depth-augmented model strictly outperforms all other models in more than 93% (86%) of the 75 one-month out-of-sample windows, judged by MSE (MAE).
- The depth-augmented model remains in the Hansen et al. Model Confidence Set of best models in more than 97% (90%) of out-of-sample windows by MSE (MAE).
- Adding HAR-style lags of past price impact reduces out-of-sample MSE and MAE by about 5-6%.
- Splitting a large trade into a series of consecutive same-sign smaller trades reduces the aggregate immediate price impact by between 60% and 82% on average, with a split into 10 trades close to the largest reduction.
- About 30% of trades in the sample carry non-zero immediate price impact, so a naive always-zero-impact model outperforms non-depth models on mean absolute error.
- The market depth indicator negatively predicts future order imbalance and the gap between permanent and immediate price impact, and this relationship is stronger for smaller-capitalization stocks.
- More accurate depth-augmented forecasts imply a reduction of roughly $ AUD 97.1 million per year in the forecast uncertainty of price impact costs versus non-depth models.

## Limitations

- The sample only covers lit ASX trades from 2007 to 2013 and excludes block trades and dark-pool trades.
- The stock sample keeps only tickers that survived unchanged in the S&P/ASX200 index across the whole 2007-2013 period, which the authors note may introduce survival bias.
- The depth indicator becomes less accurate for trades from 2012 onward, when multiple trades recorded at the same millisecond ('anomalous trades') make zero- and non-zero-impact trades harder to distinguish.
- Reader note: all evidence is from a single, relatively unfragmented equity market (Australia); applicability to fixed-income or more fragmented equity markets is not tested in this paper.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/price-impact|price impact]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/metaorder|metaorder]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/informed-trading|informed trading]]

## Citation

Manh Cuong Pham, Heather Margot Anderson, Huu Nhan Duong, Paul Lajbcygier (2020). The effects of trade size and market depth on immediate price impact in a limit order book market.

DOI: 10.1016/j.jedc.2020.103992

Text ingested: `markdown_output/pham-2020-effects-trade-size-market-depth-immediate.md`, converted from `raw/ofi-event-clock/pham-2020-effects-trade-size-market-depth-immediate.pdf`.

Coverage of this summary: Read the abstract, full introduction, the model specification (Section 2), the data and methodology sections (Section 3), all of the results and discussion (Section 4), the economic implications section (Section 5), the market-depth/order-flow-gap section (Section 6), and the conclusion (Section 7); did not read the appendices' derivations or the reference list.

Known problems with the input: Markdown conversion omits Tables 1-6 and Figures 1-3; only the surrounding text's discussion of their content, not the underlying table numbers, was available to extract from.
<!-- AUTHORED REGION END -->