---
authors:
- Kyle Bechler
- Mike Ludkovski
content_hash: sha256:26c4c01bcc531949c190ec8c14677d7cd068ee72d6d864fc10df588b449f7393
created: 2026-09-27 01:47:00+00:00
page_id: sources/bechler-2017-order-flows-limit-order-book-resiliency
page_type: source
related:
- concepts/volume-clock
- concepts/limit-order-book
- concepts/order-flow
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/price-impact
- concepts/market-microstructure
- concepts/stylized-facts
- concepts/high-frequency-data
- entities/mike-ludkovski
revision_id: 1
schema_version: 2
source_hash: sha256:7eff1fdb2d234da8974918e2d4dcf806cfa9a8922d4d893e9a9545f1cacc2fbe
source_path: markdown_output/bechler-2017-order-flows-limit-order-book-resiliency.md
source_type: paper
tags:
- meso-scale
- limit-order-book
- order-flow
- price-impact
- volume-bucketing
- scarce-liquidity
- nasdaq
- clock-volume
- asset-equity
- harvest-core
title: Order Flows and Limit Order Book Resiliency on the Meso-Scale
updated: '2026-09-27T01:47:00Z'
uuid: 46d80fae-8404-5c21-989b-3ee6c80cfeb4
year: 2017
---

<!-- AUTHORED REGION START -->
# Order Flows and Limit Order Book Resiliency on the Meso-Scale

## Summary

The paper asks how the limit order book behaves on the meso-scale, roughly minutes and encompassing dozens of trades, which is the timescale relevant to algorithmic order-execution scheduling, and specifically which combination of order-flow and book-shape variables best explains price changes and periods of scarce liquidity at that scale.

Using Nasdaq ITCH order-book message data for six liquid, large-tick common stocks (three from 2011 and three from 2013), the authors divide each trading day into buckets containing a fixed amount of executed market volume, and compute, per bucket, the trade imbalance, one-sided market and limit order flow at the touch, and a set of static book-depth and price-impact measures. They fit nonparametric (GAM) and linear models relating a bucket's price change to trade imbalance and order flows, then use stepwise linear regression, LASSO, MARS, and random forests to rank the importance of a wider covariate set, and a logistic regression to model a binary scarce-liquidity indicator built from the residuals of the trade-imbalance fit.

Trade imbalance alone has a nonlinear, S-shaped relationship with price change, but this becomes close to linear once it is combined with limit order flow into a single Net Liquidity measure, and adding this flow substantially improves the fit. Limit order flows at the touch, and the associated proportion of cancellations, are consistently among the strongest predictors of both price change and scarce liquidity, while deeper book-shape measures matter more than raw top-of-book depth or book imbalance; top-of-book depth alone is not a useful predictor at this timescale.

The authors present this as the first study of intraday limit order book data aggregated by executed volume rather than calendar time, and use that lens, together with a data-driven definition of scarce liquidity, to separate price trend (driven by trade imbalance) from liquidity and resilience (driven by limit order flow and deeper book shape) as distinct, complementary drivers of meso-scale price formation, a decomposition presented as new relative to prior work that assumed a purely linear, trade-imbalance-driven price impact.

## Clock and Sampling

**Volume clock: one observation per unit of volume traded.**

See [[concepts/volume-clock|Volume Clock]].

Each trading day is divided into buckets containing a fixed amount of executed market volume (V set to about 0.25%, 1%, or 2% of average daily volume, i.e. roughly 400, 100, or 50 buckets per day); a bucket ends at the timestamp of the trade that fills it, with market orders occasionally split across a bucket boundary. Within each bucket the authors compute the trade imbalance and net limit order flow at the touch, then regress the next bucket's mid-price change (or a scarce-liquidity indicator) on the current and lagged bucket-level variables.

## Data

- **Asset class:** Equities
- **Instruments:** Six large-cap, large-tick Nasdaq common stocks: MSFT, TEVA, and BBBY (first 100 trading days of 2011); INTC, ORCL, and NTAP (last 100 trading days of 2013)
- **Venue:** Nasdaq (ITCH TotalView Level-2 order book feed)
- **Period:** First 100 trading days of 2011 (MSFT, TEVA, BBBY) and last 100 trading days of 2013 (INTC, ORCL, NTAP)
- **Granularity:** Event-by-event limit order book messages (market executions and limit order additions, modifications, and cancellations) up to 30 price levels deep, restricted to 10:00am-3:45pm trading and then aggregated into executed-volume buckets.

## Features and Measures

- **Trade imbalance (TI).** A bucket's net signed executed volume divided by its total executed volume, ranging from -1 (all sells) to +1 (all buys).
- **Net Liquidity.** A weighted average of market order flow and touch limit order flow within a bucket, with the weighting chosen so that price change is close to linear in the combined measure.
- **Price impact (PI).** The volume-weighted average execution cost, in ticks, of immediately trading a given number of shares against the resting book, computed from cumulative depth at each price level.
- **LOB slope (S).** A linear-regression summary of book depth across price levels, interpreted as a linearized price impact per share on one side of the book.
- **Book imbalance (BI).** The relative difference between resting volume at the best bid and the best ask, i.e. top-of-book depth imbalance.
- **Scarce liquidity indicator (SL).** A binary, bucket-level and side-specific indicator flagging when the realized price change deviates from its fitted relationship with trade imbalance by more than a chosen multiple of the residual standard deviation.

## Method

The authors fit a nonparametric generalized additive model (a penalized regression spline, estimated with the R package mgcv) relating bucket price change to trade imbalance, then extend it to a linear model that combines market and limit order flow into a single Net Liquidity measure. They then assess the predictive importance of a wider covariate set, including LOB depth and shape measures, price impact, slope, book imbalance, and lagged flows and price changes, using four model classes: stepwise-selected linear regression, LASSO fit by cross-validation, multivariate adaptive regression splines (MARS), and random forests, comparing goodness-of-fit and random-forest variable importance across the six tickers and three bucket sizes.

A logistic regression version of the same covariate set is used to model the binary scarce-liquidity indicator on each side of the book, with performance judged out-of-sample by the area under the ROC curve (AUC) on a held-out test set. Time-series properties of order flows and of the scarce-liquidity indicator, including autocorrelation and cross-correlation across buckets, are examined using the sample autocorrelation function (ACF).

## Results

- Regressing price change on trade imbalance alone gives a goodness-of-fit of about R-squared 0.4; adding contemporaneous limit order flow at the touch raises it to about 0.7, and adding deeper LOB shape metrics raises it further to about 0.8.
- The relative price impact of a touch limit order compared to a market order is stable across tickers and bucket sizes, at roughly 50%-70% of a market order's impact.
- Scarce liquidity, unusually large price moves relative to the executed volume, occurs on each side of the book in about 6% of volume buckets, using a 1.5 standard-deviation threshold on the residual from the trade-imbalance fit.
- Logistic regression models for scarce liquidity are correct roughly 70-80% of the time when they flag a bucket as high risk, but because scarce liquidity is rare, more occurrences are missed than caught.
- A per-trading-day version of the trade-imbalance fit for MSFT (1% ADV buckets) only raises R-squared from 46.9% to 53.3%, indicating the unexplained variation is mostly intraday rather than day-to-day.
- Top-of-book depth alone is not a statistically useful predictor of price change; deeper book measures such as two-level depth, price impact, and LOB slope carry more information.
- Order-flow autocorrelation is modest but persists across many lags, consistent with long-memory-like behavior in liquidity provision over the trading day.

## Limitations

- The authors state the analysis is limited to six liquid, large-tick Nasdaq stocks and does not cover small-tick or illiquid assets.
- The authors state that time-series modelling of the full multivariate order-flow system was judged too complex for this paper and left for future work; only marginal stylized facts (ACF) are reported.
- Reader note: the two ticker samples are drawn from different calendar years (2011 and 2013), so cross-period comparisons are confounded with differences in the market regime.

## Related

- [[concepts/volume-clock|Volume Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/price-impact|price impact]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/high-frequency-data|high frequency data]]
- [[entities/mike-ludkovski|Mike Ludkovski]]

## Citation

Kyle Bechler, Mike Ludkovski (2017). Order Flows and Limit Order Book Resiliency on the Meso-Scale.

DOI: 10.1142/s2382626618500065

Text ingested: `markdown_output/bechler-2017-order-flows-limit-order-book-resiliency.md`, converted from `raw/ofi-event-clock/bechler-2017-order-flows-limit-order-book-resiliency.pdf`.

Coverage of this summary: Read the full text end to end: abstract, introduction, LOB and price-impact background, the volume-bucketing method, the price-trend/liquidity regression analysis, the liquidity-predictor and scarce-liquidity models, the time-series section, the conclusion, references, and the appendix tables and figures.

Known problems with the input: Several equations and figures are rendered as omitted images in the markdown conversion, so some formal definitions (e.g. price impact PI, LOB slope S, Net Liquidity) are described qualitatively rather than reproduced as exact formulas; Summary-statistics and predictor-importance tables (Tables 1-2 and 6-7) are OCR-garbled or collapsed in the markdown conversion; numbers from those tables were used only where independently confirmed in the surrounding prose.
<!-- AUTHORED REGION END -->