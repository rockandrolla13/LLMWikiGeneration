---
authors:
- Xianglin Kong
content_hash: sha256:881fbdde74565a3990e5afbf8a77250e55f8c3943db9b4cd44b3c12175aa80bb
created: 2026-09-27 01:47:00+00:00
page_id: sources/kong-2025-volatility-estimation-agricultural-futures-markets-microstructure
page_type: source
publication_venue: University of Manitoba (Master of Science thesis, Agribusiness
  and Agricultural Economics)
related:
- concepts/limit-order-book
- concepts/realized-variance
- concepts/market-microstructure-noise
- concepts/bid-ask-spread
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/trade-clock
- concepts/micro-price
revision_id: 1
schema_version: 2
source_hash: sha256:9dd70d90d8d215553350439a2aa7002326c2eee54d1e9ed480ae8a50f898ee4f
source_path: markdown_output/kong-2025-volatility-estimation-agricultural-futures-markets-microstructure.md
source_type: paper
tags:
- agricultural-futures
- garch
- limit-order-book
- realized-volatility
- market-microstructure-noise
- volatility-forecasting
- intraday-data
- clock-calendar
- asset-futures
- harvest-relevant
title: 'Volatility Estimation in Agricultural Futures Markets: A Microstructure Approach'
updated: '2026-09-27T01:47:00Z'
uuid: b2f91703-b253-5902-8c0b-636b51f04648
year: 2025
---

<!-- AUTHORED REGION START -->
# Volatility Estimation in Agricultural Futures Markets: A Microstructure Approach

## Summary

The thesis asks whether information contained in the limit order book of agricultural futures markets can improve intraday volatility forecasts relative to a standard time-series model that ignores it, focusing on lean hog and corn futures traded on CME Group's electronic platform.

The author reconstructs the full limit order book for both markets over about thirteen months, sampling observations at a data-driven frequency based on each commodity's own average trading frequency rather than a common fixed interval, in order to limit market microstructure noise while retaining information. Returns are computed from a volume-weighted mid-price that uses best bid/ask quantities as weights rather than a simple midpoint average, on the reasoning that this better approximates the true price under discrete tick pricing. Two forecasting models are estimated per commodity: a standard GARCH(1,1), and a GARCH-X model that adds exogenous limit-order-book variables, namely best and second-level bid/ask quantities and the bid-ask spread, to the variance equation. One-day-ahead forecasts from both models are compared against realized volatility computed from the intraday data, using the Diebold-Mariano test and mean-squared, root-mean-squared, and mean-absolute error measures.

ARCH effects were statistically significant on the large majority of trading days for both commodities, supporting the use of GARCH-type models. The order-book-based exogenous variables in GARCH-X were frequently statistically significant, particularly the bid-ask spread and the best-level bid and ask quantities. Despite this, GARCH-X forecasts did not outperform plain GARCH(1,1) forecasts when both were compared against realized volatility: GARCH had a smaller error than GARCH-X on the large majority of days for both hogs and corn, and the Diebold-Mariano test showed GARCH and GARCH-X forecasts were statistically indistinguishable from each other on most days.

The contribution is using intraday, order-book-derived variables, rather than daily prices, to model volatility in agricultural futures specifically, an asset class the author notes has received far less microstructure-based volatility research than equity or foreign-exchange markets, together with a trading-frequency-based sampling scheme and a quantity-weighted mid-price return definition tailored to discrete tick prices.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Volatility is estimated using intraday snapshots taken at a fixed time interval chosen separately for each commodity from its own average time between price-changing trades, rather than a common 5-minute interval, in order to keep more observations while limiting microstructure noise. GARCH and GARCH-X produce one-day-ahead forecasts: data from day i is used to estimate the model, and on day i+1 volatility is predicted at each snapshot t using the observation at t-1.

## Data

- **Asset class:** Futures
- **Instruments:** Lean hog futures (contract unit 40,000 pounds) and corn futures (contract unit 5,000 bushels), using the highest-volume contract each day
- **Venue:** CME Group (Chicago Mercantile Exchange / Chicago Board of Trade electronic limit order book)
- **Period:** November 23, 2018 to December 27, 2019
- **Granularity:** Full reconstructed limit order book, sampled at commodity-specific fixed intervals derived from average trading frequency (6 seconds for lean hogs, 9 seconds for corn); lean hogs session 8:30am-1:05pm CT, corn morning session 8:30am-1:20pm CT, first and last five minutes of each session excluded

## Features and Measures

- **weighted mid-point price.** The best bid and ask price averaged using the opposite side's quoted quantity as weights (best ask quantity weighting the bid price and vice versa), used as a proxy for the true price that accounts for discrete tick pricing.
- **GARCH-X exogenous LOB variables.** Best and second-level bid and ask order quantities plus the bid-ask spread, added to the variance equation of a GARCH model to test whether order-book depth and spread help explain volatility.
- **realized volatility.** The sum of squared intraday returns over a chosen sampling interval, used as a model-free benchmark measure of true volatility against which GARCH and GARCH-X forecasts are compared.

## Method

Volatility is modelled three ways: realized volatility computed directly from intraday weighted mid-point returns, a standard GARCH(1,1) model, and a GARCH-X model that adds the LOB-derived exogenous variables (best and second-level bid and ask quantities and the spread) to the GARCH variance equation. Both GARCH models produce one-day-ahead volatility forecasts using the prior day's data, re-estimated for each forecast day. An LM test for ARCH effects is used first to justify the GARCH-type specification. Forecast quality is judged by comparing GARCH and GARCH-X forecasts against realized volatility using mean squared error, root mean squared error, and mean absolute error, and by the Diebold-Mariano test, which is also used to test whether GARCH and GARCH-X forecasts differ significantly from each other.

## Results

- For lean hogs, 198 of 222 days showed statistically significant ARCH effects at lag one, and more than 200 of 222 days at lags two through ten, supporting the use of GARCH-type models.
- For corn, 236 of 252 days showed significant ARCH effects at lag one, and 238 of 252 days at lag ten.
- In the GARCH-X model for lean hogs, the spread was significant at the 5% level on 190 of 218 days, the most consistently significant of the exogenous variables.
- In the GARCH-X model for corn, the best bid quantity was significant on 220 of 223 days, the most consistently significant variable for that commodity.
- The GARCH-X model had a smaller forecast error than GARCH on only 11.41% of days for lean hogs and only 6.32% of days for corn.
- The Diebold-Mariano test found GARCH and GARCH-X forecasts statistically indistinguishable from each other on most days for both commodities.
- GARCH and GARCH-X forecasts tracked each other more closely than either tracked realized volatility, with GARCH-X showing higher fluctuation.

## Limitations

- The author notes that realized volatility itself does not incorporate LOB information beyond the return-weighting step, making it an imperfect benchmark for judging whether GARCH-X's LOB variables help.
- The study uses only best- and second-level bid/ask quantities and the spread as exogenous variables; deeper book levels are not included.
- The sampling interval (6 seconds for hogs, 9 seconds for corn) is derived from one criterion, average trading frequency, and the author notes results could change with a different sampling scheme.
- Reader note: the analysis covers only two commodities over about one year, so findings may not generalize to other agricultural futures or periods.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/trade-clock|Trade Clock]]
- [[concepts/micro-price|Micro-Price]]

## Citation

Xianglin Kong (2025). Volatility Estimation in Agricultural Futures Markets: A Microstructure Approach. University of Manitoba (Master of Science thesis, Agribusiness and Agricultural Economics).

Text ingested: `markdown_output/kong-2025-volatility-estimation-agricultural-futures-markets-microstructure.md`, converted from `raw/ofi-event-clock/kong-2025-volatility-estimation-agricultural-futures-markets-microstructure.pdf`.

Coverage of this summary: Read the full thesis: abstract, introduction, literature review, data section, methods (GARCH, GARCH-X, realized volatility, Diebold-Mariano test, error metrics), all of the results section including both the DM-test and MSE/RMSE/MAE tables, and the conclusion; did not read the reference list in detail.

Known problems with the input: The markdown conversion garbles some bullet numbering in the literature review's numbered sub-lists, but the surrounding prose is intact and was used as written.
<!-- AUTHORED REGION END -->