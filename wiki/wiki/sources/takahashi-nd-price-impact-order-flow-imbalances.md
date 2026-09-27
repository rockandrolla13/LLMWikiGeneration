---
authors:
- Makoto Takahashi
content_hash: sha256:7ce5e5637184d5010af9e1b4c33da589ff19d4db59e2fab91fc94702425158ef
created: 2026-09-27 01:47:00+00:00
page_id: sources/takahashi-nd-price-impact-order-flow-imbalances
page_type: source
publication_venue: The Hosei Journal of Business (Keieishirin), Hosei University,
  Volume 56, Number 3, pp. 63-77
related:
- concepts/price-impact
- concepts/order-flow-imbalance
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/informed-trading
revision_id: 1
schema_version: 2
source_hash: sha256:5d664ceeac5e2e5dde4b2b2463000fc4f3a261239a35b7040f1543d0f95d6533
source_path: markdown_output/takahashi-nd-price-impact-order-flow-imbalances.md
source_type: paper
tags:
- price-impact
- order-flow-imbalance
- limit-order-book
- market-microstructure
- intraday-seasonality
- high-frequency-data
- clock-calendar
- asset-equity
- harvest-relevant
title: Price Impact of Order Flow Imbalances
updated: '2026-09-27T01:47:00Z'
uuid: 5a232cef-dfd2-5a32-8a72-a1e6a25ded19
year: 2019
---

<!-- AUTHORED REGION START -->
# Price Impact of Order Flow Imbalances

## Summary

The paper asks whether the linear price-impact-of-order-flow-imbalance relationship proposed by Cont, Kukanov and Stoikov (2014, referred to as CKS) for a stylized limit order book model holds up empirically, and whether the intraday pattern CKS reported for the price impact coefficient repeats on a different stock.

Using order book data for Amazon.com reconstructed with LOBSTER, the author builds mid-quote returns and an order flow imbalance measure (the net of limit order arrivals, cancellations/deletions, and marketable order executions at the best bid and ask) over ten-second intervals for one trading day, and regresses returns on the imbalance separately for each of thirteen 30-minute windows spanning the day, first with a linear specification and then with an added quadratic (signed squared) term.

The linear price-impact coefficients are all significantly positive and are highest just after the open and lowest near the close, matching the intraday pattern CKS reported for other stocks. But adding the quadratic term shows a significantly negative quadratic coefficient in most windows, meaning the true relation between order flow imbalance and price changes is concave rather than linear as CKS's baseline specification assumed; the quadratic effect follows the opposite intraday pattern to the linear one, being strongest just after the open.

What is new is the demonstration that, on this stock and day, the originally linear CKS price impact model understates a curvature concentrated in the morning session, connecting the finding to concave price-impact functions reported elsewhere in the literature.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Order-book events (new limit orders, cancellations/deletions, and marketable executions at the best bid and ask) are netted into a single order-flow-imbalance series and aggregated into fixed 10-second calendar intervals to form mid-quote returns and the order-flow-imbalance regressor. The price-impact regression is estimated separately for each of thirteen fixed 30-minute calendar windows across the trading day, so each observation's horizon is the following 10 seconds, and impact coefficients are compared across the day rather than forecast forward in time.

## Data

- **Asset class:** Equities
- **Instruments:** Amazon.com, Inc. (single stock)
- **Venue:** not stated (order book reconstructed via LOBSTER; the specific exchange is not named in the paper)
- **Period:** One trading day, June 21, 2012, 9:30-16:00
- **Granularity:** Order-book events aggregated into 10-second mid-quote return and order-flow-imbalance observations, with separate regressions estimated over thirteen 30-minute intervals

## Features and Measures

- **Order flow imbalance (OFI).** The net of limit order arrivals, cancellations/deletions, and marketable order executions at the best bid and best ask over a fixed interval, following Cont, Kukanov and Stoikov (2014); a positive value indicates net buying pressure at the top of the book.
- **Price impact coefficient.** The ordinary-least-squares slope of mid-quote returns regressed on order flow imbalance within a 30-minute window, measuring how much the price moves per unit of net order flow.
- **Quadratic (augmented) price impact model.** An extension of the linear price impact regression that adds a term for order flow imbalance multiplied by its own absolute value, testing for a nonlinear or concave relation between imbalance and price change.

## Method

Following the stylized limit order book model of Cont, Kukanov and Stoikov (2014), in which price changes are a deterministic linear function of net order flow imbalance under a uniform-depth assumption, the author fits a noisy empirical version by ordinary least squares: mid-quote returns over ten-second windows are regressed on order flow imbalance, separately for each of thirteen 30-minute intervals spanning one trading day, first with a constant and a linear imbalance term, then with an added quadratic (signed-squared) imbalance term to test for nonlinearity, using robust standard errors throughout.

## Results

- The order-flow-imbalance regression sample from June 21, 2012 has 2,260 ten-second observations, extracted from 55,070 best-bid/best-offer order book events.
- All 13 linear price impact coefficients are significantly positive, with R-squared ranging between 37.6% and 63.6%, consistent with Cont, Kukanov and Stoikov (2014).
- The linear price impact coefficient is highest just after the market opens and lowest just before the close, matching the intraday pattern reported for other stocks.
- Adding a quadratic imbalance term makes most of the quadratic coefficients significantly negative, indicating a concave rather than linear relation between order flow imbalance and price changes.
- The quadratic impact coefficient follows the opposite intraday pattern to the linear coefficient, being small just after the open and large near the close.
- Over the sampled day the Amazon.com stock price fell by 3.18 dollars (1.42%) between 9:30 and 15:30.

## Limitations

- The author notes that extending the model to treat marketable orders, limit orders and cancellations separately, and to a multivariate setting across assets, is left to future work.
- Reader note: the empirical analysis covers a single stock (Amazon.com) on a single trading day (June 21, 2012), so the intraday patterns are not tested for robustness across other days or assets.
- Reader note: the 'concave' relation is tested with only a single added squared-imbalance term; other nonlinear functional forms are not compared.
- Reader note: no out-of-sample or predictive validation is performed; the model is fit and interpreted in-sample for each 30-minute window separately.

## Related

- [[concepts/price-impact|price impact]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/informed-trading|informed trading]]

## Citation

Makoto Takahashi (2019). Price Impact of Order Flow Imbalances. The Hosei Journal of Business (Keieishirin), Hosei University, Volume 56, Number 3, pp. 63-77.

DOI: 10.15002/00025621

Text ingested: `markdown_output/takahashi-nd-price-impact-order-flow-imbalances.md`, converted from `raw/ofi-event-clock/takahashi-nd-price-impact-order-flow-imbalances.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, the price impact model in Section 2, the data description in Section 3, estimation results in Section 4, and the conclusion; this is a short research note and was read in full, including all tables.

Known problems with the input: Line 1 of the converted markdown ('PDF issue: 2026-09-27') is a file-conversion artifact, not part of the original paper, and was ignored; The exchange on which Amazon.com traded is not stated in the paper beyond noting the data source is LOBSTER; the venue field is marked not stated.
<!-- AUTHORED REGION END -->