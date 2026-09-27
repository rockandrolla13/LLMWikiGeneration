---
authors:
- Michael Hanke
- Michael Weigerding
content_hash: sha256:b1ff2ee3156ef1c79c35b36502a0a6420ca04cdfa0558d2948e3b1fd614f15e7
created: 2026-09-27 01:47:00+00:00
page_id: sources/hanke-2015-order-flow-imbalance-effects-german-stock
page_type: source
publication_venue: Business Research
related:
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/adverse-selection
- concepts/bid-ask-spread
- concepts/market-microstructure
- concepts/informed-trading
revision_id: 1
schema_version: 2
source_hash: sha256:fd6b281615d5a8a0d01a2ea5f85ae88cd97b0e1e6f156dc0bb69f0b2bfa2a42e
source_path: markdown_output/hanke-2015-order-flow-imbalance-effects-german-stock.md
source_type: paper
tags:
- order-imbalance
- panel-regression
- german-equities
- xetra
- return-predictability
- fixed-effects
- financial-crisis
- clock-calendar
- asset-equity
- harvest-relevant
title: Order flow imbalance effects on the German stock market
updated: '2026-09-27T01:47:00Z'
uuid: c700ea22-8b1a-580c-9ecb-d8cb3213a346
year: 2015
---

<!-- AUTHORED REGION START -->
# Order flow imbalance effects on the German stock market

## Summary

The paper asks whether order flow imbalance (the daily difference between buyer- and seller-initiated orders) is related to same-day German stock returns and, separately, whether past imbalance can predict next-day returns, and whether that relation depends on firm size, liquidity, or the 2007-2009 financial crisis.

Using German Xetra trading system data from February 2002 through September 2009, in which every trade is already labeled as buyer- or seller-initiated (avoiding the need for a trade-classification algorithm used in most prior studies), the authors filter out illiquid stocks, corporate-action days, and data errors to arrive at a panel of daily observations. Rather than the time-series regressions used in most earlier work, they use a fixed-effects panel regression that removes both stock-specific and day-specific effects, separately modeling the concurrent-and-lagged (conditional) relation and the past-only (unconditional, predictive) relation, and adding interaction terms for market capitalization and bid-ask spread to capture size and liquidity effects, plus a dedicated crisis-period subsample.

Concurrent order imbalance is strongly and positively related to same-day returns, and conditional lags are negative, consistent with the existing literature; but the unconditional, return-predicting first lag, while still positive and significant, is much smaller than the concurrent effect and largely disappears by the second lag, weaker than in earlier studies based on 1990s US data. Smaller and less liquid stocks show a stronger imbalance-return relation and a weaker next-day reversal, following a U-shaped pattern across firm size. The relation is not driven by extreme imbalances, and the concurrent relation strengthens during the financial crisis while the predictive relation stays roughly unchanged.

What is new here is the first order-imbalance study on German equities, the first use of a fixed-effects panel design (rather than per-stock time series) for this question, the first look at how the relation behaves during a financial crisis, and evidence that the predictive lagged effect has weakened compared to 1990s-era markets, which the authors read as a sign of increased market efficiency, tempered by the absence of data on canceled limit orders and off-exchange large orders.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Order imbalance and returns are both aggregated to one full trading day per stock. Order imbalance counts buyer-minus-seller-initiated market and marketable-limit orders during the day; returns are daily log changes in the last mid-quote before the closing auction. The unconditional (forecasting) model therefore has a one-trading-day-ahead horizon, with a second daily lag also tested, and the conditional model relates same-day and lagged daily imbalances to the same-day return.

## Data

- **Asset class:** Equities
- **Instruments:** German stocks traded on the Xetra system; 212 stocks in the final sample out of 1225 in the initial dataset
- **Venue:** Deutsche Börse Xetra
- **Period:** February 1, 2002 to September 30, 2009, split into eight subperiods (2002 partial year, 2003-2008 full years, 2009 partial year)
- **Granularity:** Daily observations of order imbalance, mid-quote returns, market capitalization, and bid-ask spread

## Features and Measures

- **Order (flow) imbalance, number measure.** For each stock and day, the difference between the number of buyer-initiated and seller-initiated market and marketable-limit orders, scaled by their total so the measure runs from -1 to 1.
- **Abnormal market capitalization.** A stock's market capitalization for the day expressed relative to its sample average, used as an interaction term to capture a U-shaped relation between firm size and the imbalance-return effect.
- **Fixed-effects within transformation.** A panel-regression device that demeans returns and imbalances separately by stock and by day, removing unobserved stock-specific and market-wide effects before estimating the imbalance-return relation.

## Method

The authors estimate fixed-effects panel regressions of daily mid-quote returns on current and lagged daily order imbalance, using the within transformation to remove stock- and day-specific effects; a Hausman test supports fixed effects over a random-effects specification. Two families of models are estimated: a conditional model including the concurrent imbalance plus four lags, and an unconditional model using only past imbalance (for forecasting), each tested with and without interaction terms for market capitalization, abnormal market capitalization, and bid-ask spread to capture size and liquidity effects. All coefficients are tested with two-tailed t-tests using robust standard errors that account for the heteroskedasticity and autocorrelation found in preliminary analysis. The same conditional and unconditional models, with and without size/liquidity interactions, are re-estimated on a subsample covering the financial crisis to see whether the imbalance-return relation changed during that period.

## Results

- The concurrent order imbalance coefficient (2588, scaled by 10 to the power of 5) is positive and significant, while the four conditional lags are all negative and significant, strongest at the second lag (307, same scaling).
- In the unconditional model the first lag coefficient (289, same scaling) is positive and significant but far smaller than the concurrent coefficient, and the effect is essentially gone by the second lag.
- Smaller and less liquid stocks show a stronger concurrent imbalance-return relation and a weaker next-day reversal; the size interaction terms describing this U-shaped pattern are significant at the 1 percent level.
- Splitting the sample by imbalance magnitude shows the concurrent effect is strongest for small imbalances and weakens for larger ones, the opposite of what some earlier studies on other markets found.
- During the financial crisis subsample the concurrent imbalance coefficients and the regressions' adjusted R-squared increase, while the unconditional (predictive) coefficients remain largely unchanged from the full-sample estimates.
- Order imbalance is close to evenly split across the sample (50.08 percent of daily observations positive) with a standard deviation of about 21.05 percent, and its magnitude is significantly related to the bid-ask spread but not to market capitalization.

## Limitations

- The dataset lacks information on canceled limit orders, which the authors say would likely have made the documented imbalance effects even stronger if it had been available.
- The Xetra dataset may not capture very large orders filled outside the exchange's regular trading, which the authors suggest could explain the weaker-than-expected effect for extreme imbalances.
- Reader note: the study covers a single exchange and country (Xetra, Germany) over 2002-2009, so the panel evidence may not generalize to other European venues or later, more automated market conditions.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/informed-trading|informed trading]]

## Citation

Michael Hanke, Michael Weigerding (2015). Order flow imbalance effects on the German stock market. Business Research.

DOI: 10.1007/s40685-015-0025-0

Text ingested: `markdown_output/hanke-2015-order-flow-imbalance-effects-german-stock.md`, converted from `raw/ofi-event-clock/hanke-2015-order-flow-imbalance-effects-german-stock.pdf`.

Coverage of this summary: Read the full markdown from abstract through the literature review, methodology, data and sample-selection sections, all results sections (conditional relation, unconditional relation, imbalance-magnitude subsamples, financial crisis subsample), and the summary/conclusion.

Known problems with the input: The markdown rendering corrupts minus signs and some symbols in the regression tables (shown as characters like a tilde or a replacement glyph), so exact coefficient signs are taken from the surrounding descriptive text rather than from the corrupted table symbols themselves.
<!-- AUTHORED REGION END -->