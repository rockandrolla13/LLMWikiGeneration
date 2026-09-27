---
authors:
- Anastasia Bugaenko
content_hash: sha256:2eadd67c02b314217137afe3a24edc4d605fb4e9d58e1e811a1030f3a21c71ac
created: 2026-09-27 01:47:00+00:00
page_id: sources/bugaenko-2020-empirical-study-market-impact-conditional-order
page_type: source
publication_venue: Adam Smith Business School, University of Glasgow (MSc Quantitative
  Finance dissertation)
related:
- concepts/trade-clock
- concepts/order-flow-imbalance
- concepts/price-impact
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/adverse-selection
- concepts/square-root-law
- concepts/metaorder
- concepts/high-frequency-data
- concepts/kyles-lambda
revision_id: 1
schema_version: 2
source_hash: sha256:3615f5271a41ab08135f44e04fd87e0e17fb9d187c96aacfc2af45e46fad9a3b
source_path: markdown_output/bugaenko-2020-empirical-study-market-impact-conditional-order.md
source_type: paper
tags:
- market-impact
- order-flow-imbalance
- machine-learning
- kyle-model
- nasdaq
- lobster-data
- decision-tree-regression
- price-impact
- clock-trade
- asset-equity
- harvest-relevant
title: Empirical Study of Market Impact Conditional on Order-Flow Imbalance
updated: '2026-09-27T01:47:00Z'
uuid: 62610f09-03b6-5d1f-b5c9-19c396bbd233
year: 2019
---

<!-- AUTHORED REGION START -->
# Empirical Study of Market Impact Conditional on Order-Flow Imbalance

## Summary

The dissertation asks whether large NASDAQ equity orders move prices in the way that Kyle's linear impact model or the empirical square-root model predicts, and whether a machine-learning regression can recover a better functional form for market impact than ordinary least squares.

Working from LOBSTER-reconstructed limit order book and trade data for four NASDAQ stocks (SIRI, EBAY, TSLA and PCLN) during 2015, the author first estimates an unconditional lag-1 price response function for single market orders, then conditions that response on normalised trade volume, and finally aggregates signed order flow over T consecutive market orders (T=5,10,20,50) to study aggregate impact against order-flow imbalance. Linear Regression and Decision Tree Regression models are fit to the imbalance-impact relationship and compared using mean squared error, R-squared and k-fold cross-validation.

The lag-1 response is positive for all four stocks and roughly tracks the average spread for the two small-tick names; response conditioned on normalised trade volume is close to flat, which the author attributes to a selective liquidity-taking bias. Order-flow imbalance and aggregate impact for TSLA are strongly correlated, and the relationship is close to linear for small imbalances but becomes concave for larger ones; Decision Tree Regression achieves a lower cross-validated MSE than Linear Regression, and a Kyle's-lambda estimated from the linear region suggests TSLA was comparatively liquid over the sample.

The contribution is mainly empirical and methodological: replicating and cross-checking earlier LOBSTER-based response-function estimates against a published benchmark, then applying supervised machine learning, rather than plain OLS, to the imbalance-impact regression, with cross-validation used explicitly to guard against overfitting.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Observations are indexed by market order (MO) arrivals rather than wall-clock time. The lag-1 response function is computed as the signed mid-price change between one market order and the next. Order-flow imbalance and its aggregate impact are then measured over windows of T=5, 10, 20 and 50 consecutive market orders, so the prediction horizon is defined in a count of trades rather than in elapsed time.

## Data

- **Asset class:** Equities
- **Instruments:** Four NASDAQ-listed stocks: SIRI, EBAY, TSLA and PCLN (two large-tick, two small-tick)
- **Venue:** NASDAQ (LOBSTER-reconstructed limit order book data derived from NASDAQ TotalView-ITCH message and orderbook files)
- **Period:** First six months of 2015 for the primary lag-1 response and volume-conditioning analysis, extended to the second half of 2015 for comparison, and the entire year of 2015 for the order-flow-imbalance and Kyle's-lambda analysis; trading window restricted to 10:30-15:00 each day.
- **Granularity:** Event-by-event with millisecond timestamps, aggregated to per-market-order and multi-market-order (T-order) windows

## Features and Measures

- **lag-1 response function R(1).** The signed average change in mid-price between the mid-price just before a market order and the mid-price just before the following market order, used to measure single-trade price impact.
- **normalised trade volume.** A market order's volume divided by the average volume at the opposite side's best quote, recalculated each day, used to compare impact across stocks with different typical trade sizes.
- **order-flow imbalance (ΔV).** The sum of signed market-order volumes over a window of T consecutive market orders, capturing the net buying or selling pressure over that window.
- **aggregate impact R(ΔV,T).** The change in mid-price from immediately before an original market order to after a sequence of T subsequent market orders, studied as a function of the order-flow imbalance over that same window.
- **Kyle's lambda.** The slope of the linear region of the aggregate-impact-versus-order-flow-imbalance relationship, taken as an estimate of Kyle's model impact coefficient and interpreted as a measure of market illiquidity.

## Method

The empirical work uses LOBSTER-reconstructed NASDAQ TotalView-ITCH message and order-book files for SIRI, EBAY, TSLA and PCLN, restricted to market-order executions between 10:30 and 15:00 on each trading day, with multiple simultaneous limit-order fills at one timestamp regrouped into a single market order.

Two response measures are built directly from the mid-price series: an unconditional lag-1 response R(1), the signed average mid-price change from just before one market order to just before the next, and a volume-conditioned version using normalised trade volume. A separate aggregated measure, order-flow imbalance over T consecutive market orders, is regressed against the corresponding aggregate impact.

The imbalance-impact relationship is modelled with Ordinary Least Squares Linear Regression and with Decision Tree Regression, each fit on a train/test split and then assessed with 10-fold cross-validation, using mean squared error and R-squared as the performance measures; the slope of the linear region of this relationship is reported as an estimate of Kyle's lambda.

## Results

- Lag-1 unconditional response R(1) is positive for all four stocks; for the small-tick stocks (TSLA, PCLN) R(1) scales roughly with the average spread.
- The correlation coefficient between order-flow imbalance and aggregate impact for TSLA over 2015 (T=10, 47,473 observations) was 0.8538, a strong positive relationship.
- Linear Regression fit to the full imbalance-impact relationship for TSLA had an MSE of 3.86 dollar cents; Decision Tree Regression achieved a lower MSE of 2.5 dollar cents.
- On the subset where the imbalance-impact relationship is linear, Decision Tree Regression's average MSE was lower than Linear Regression's by almost 0.50 dollar cents.
- The estimated Kyle's lambda for TSLA was 0.011, interpreted by the author as indicating a comparatively liquid market.
- Aggregate impact appeared close to linear for small absolute order-flow imbalance but became concave for larger imbalances, which the author attributes to a selective liquidity-taking bias.
- Response conditioned on normalised trade volume was close to flat for small-tick PCLN and showed only a weak, quickly-diluting dependency for large-tick EBAY.
- Average spread and price dispersion were higher in the second half of 2015 than the first half, coinciding with the 2015-16 stock market sell-off; averaging both halves brought the author's response-function estimates close to a previously published benchmark using the same LOBSTER data source.

## Limitations

- Restricted to single independent market orders; meta-orders and their child-order sequences could not be identified because LOBSTER data carries no trader or account identifiers.
- Only four NASDAQ equities were studied (SIRI, EBAY, TSLA, PCLN); the author states that robust conclusions about Kyle's lambda would require comparison across many more stocks and venues.
- Reader note: the sample is a single calendar year (2015) on one venue (NASDAQ), so findings may partly reflect a period-specific volatility event (the 2015-16 sell-off) rather than a stable relationship.
- Reader note: the thesis states it does not include the underlying source code, which limits independent reproducibility of the reported figures.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/price-impact|price impact]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/square-root-law|square root law]]
- [[concepts/metaorder|metaorder]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/kyles-lambda|Kyle's Lambda]]

## Citation

Anastasia Bugaenko (2019). Empirical Study of Market Impact Conditional on Order-Flow Imbalance. Adam Smith Business School, University of Glasgow (MSc Quantitative Finance dissertation).

DOI: 10.2139/ssrn.3589220

Text ingested: `markdown_output/bugaenko-2020-empirical-study-market-impact-conditional-order.md`, converted from `raw/ofi-event-clock/bugaenko-2020-empirical-study-market-impact-conditional-order.pdf`.

Coverage of this summary: Read the entire thesis end-to-end: abstract, chapters 1-5 (introduction, literature review, data and methodology, empirical study, conclusion), the reference list, and all appendices A-E, including the descriptive-statistics and cross-validation tables in Appendix C.9.

Known problems with the input: Markdown conversion garbles nearly all equations and several figures into 'picture omitted' placeholders and introduces OCR artifacts in tables and the reference list; only prose that remained legible was used; The paper's own title page prints the date as August 2019; that stated year was used for `year` rather than the job file's year_hint of 2020.
<!-- AUTHORED REGION END -->