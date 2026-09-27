---
authors:
- Ban Zheng
- Eric Moulines
- Frédéric Abergel
content_hash: sha256:7197e9b03de2cef1f549c73a9f4644acfb2f7c0fff9f51a4e6898ec643c69e93
created: 2026-09-27 01:47:00+00:00
page_id: sources/zheng-2013-price-jump-prediction-limit-order-book
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/order-flow
- concepts/trade-classification
- concepts/order-imbalance
revision_id: 1
schema_version: 2
source_hash: sha256:62a161a8a3fd673ac19d7d7918a3fd045019f144d171a3125d97fddfcb61beb7
source_path: markdown_output/zheng-2013-price-jump-prediction-limit-order-book.md
source_type: paper
tags:
- limit-order-book
- price-jump
- logistic-regression
- lasso
- cac40
- trade-through
- clock-event
- asset-equity
- harvest-core
title: Price jump prediction in Limit Order Book
updated: '2026-09-27T01:47:00Z'
uuid: a7603136-b2d2-5119-a37e-2d1f00134b09
year: 2012
---

<!-- AUTHORED REGION START -->
# Price jump prediction in Limit Order Book

## Summary

The paper asks whether the shape of the limit order book, rather than just the past price path, is informative about the direction of the next market order and about a specific discrete event the authors call an 'inter-trade price jump': a market order that executes at a price beyond the best quote observed just after the previous market order arrival. It also asks whether 'trade-through' events, where a market order is larger than the volume resting at the best opposing quote, add further predictive information.

Using millisecond-level limit order book and trade data for the 40 constituent stocks of the CAC40 index over April 2011, the authors first show empirically that the ratio of bid to ask volume at the top depth levels predicts the sign of the next market order. They then build a feature vector from limit order volumes and price gaps at five depth levels on each side, market order size, and lagged event-type dummies (bid/ask limit order, market order, and trade-through), and fit a logistic regression to predict inter-trade price jumps, run separately on a morning sub-sample and an afternoon sub-sample to remove intraday seasonality, with LASSO regularization used for automatic variable selection.

Out-of-sample prediction quality, measured by the area under the ROC curve (AUC), is consistently around 0.80 across essentially all 40 CAC40 stocks and both session halves. LASSO consistently selects the best bid/ask volume, the current market order size, and the current market-order-side indicator as the most important variables, while trade-through indicators are selected far less often than the authors expected.

What is new is defining the inter-trade price jump directly as a limit-order-book event, rather than as a statistical jump in a continuous-time price process, building an explicit order-book feature set for it, and using LASSO logistic regression to rank which feature types matter most for this event across many stocks and two intraday sub-periods.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Time is indexed by the sequence of limit order book events (limit order arrivals, cancellations, and market orders); the prediction target is evaluated specifically at market-order events, where it is a binary indicator of whether that market order executed at a price beyond the best quote observed just after the immediately preceding market order (an 'inter-trade price jump'). The effective horizon is therefore the very next market order in event time rather than a fixed calendar interval, and the data are additionally split into a morning and an afternoon sub-sample to remove intraday seasonality rather than modeling it directly.

## Data

- **Asset class:** Equities
- **Instruments:** The 40 constituent stocks of the CAC40 index
- **Venue:** Euronext (NSC electronic trading system)
- **Period:** April 2011, restricted to the continuous-trading part of each day and split into a morning sub-sample and an afternoon sub-sample
- **Granularity:** Millisecond-timestamped limit order book updates with 5 visible depth levels per side, matched with trade (market order) data

## Features and Measures

- **Bid-Ask volume ratio.** At a given depth level, the ratio between the resting bid and ask quote volumes computed just before a market order arrives, used to condition the probability that the next market order buys or sells.
- **Log limit order volumes and price gaps.** Log-transformed resting order sizes and log price gaps between consecutive depth levels on the bid and ask sides, at five levels of depth, used as explanatory variables for the jump-prediction regression.
- **Lagged market order size and side dummies.** The log size of the current and several preceding market orders, plus indicator variables marking whether recent events were bid- or ask-side limit orders, market orders, or trade-throughs.
- **Trade-through indicator.** A dummy variable marking a market order whose size exceeds the volume resting at the best opposing quote, so that it mechanically forces an immediate change in the best price.
- **Inter-trade price jump (prediction target).** A binary label equal to one when a market order executes at a price beyond the best bid or ask quote observed just after the previous market order arrival.

## Method

The authors fit a logistic regression in which the log-odds of a bid-side or ask-side inter-trade price jump is a linear function of a feature vector built from the current market order's log size, five levels of log bid/ask volumes and price gaps, and several lags of market-order-side and trade-through dummies, with coefficients estimated by maximum likelihood. Because the resulting feature vector is high-dimensional ($p = 1 + m(2L-1) + 6n = 76$ with $L = 5$ depth levels and $m = n = 5$ lags), they additionally fit an L1-penalized (LASSO) logistic regression, with the penalty strength chosen by cross-validation, both to regularize the fit and to perform automatic variable selection and rank which features are picked first, second, and so on. Performance is judged out-of-sample by the area under the ROC curve (AUC), computed separately for the bid-side and ask-side jump targets, for the morning and afternoon sub-samples, and pooled across all 40 CAC40 stocks (746 backtests in total for the variable-selection-frequency analysis).

## Results

- Out-of-sample AUC for predicting inter-trade price jumps is around 0.80 and is consistently high across all 40 CAC40 stocks and both morning and afternoon sub-samples.
- The conditional probability that the next market order is a buy is highly correlated with the bid-ask volume ratio at the best (depth-1) quote; the relationship is noisier at deeper levels.
- Averaged across stocks, the conditional probability of the implied next trade sign reaches about 0.80 when best-quote liquidity is strongly unbalanced.
- The most frequently LASSO-selected variables for the bid-side jump are the current log bid-depth-1 volume, the current bid-side market-order dummy, and the current market order size; the mirrored set of ask-side variables is most selected for the ask-side jump.
- Trade-through indicators are selected by LASSO far less often than expected, i.e. trade-through aggressiveness contributes less to jump prediction than the authors anticipated.
- With $L = 5$ depth levels and $m = n = 5$ lags, the resulting feature vector has dimension $p = 76$.

## Limitations

- The paper's definition of a price jump (inter-trade price jump) is specific to its own bid/ask best-quote and market-order-arrival construction, so results may not transfer to other jump definitions such as statistical, continuous-time bi-power-variation jumps.
- The sample covers a single calendar month (April 2011) on a single market (Euronext CAC40 stocks); the authors themselves describe the paper as 'merely a first attempt.'
- Reader note: no comparison against a non-order-book baseline model is reported for the jump-prediction task itself.
- Reader note: because the prediction target and the explanatory features are both constructed from the same bid/ask/market-order variables, part of the reported AUC may reflect a close mechanical relationship between quote depletion and the jump definition, rather than genuinely new predictive information.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow|order flow]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/order-imbalance|order imbalance]]

## Citation

Ban Zheng, Eric Moulines, Frédéric Abergel (2012). Price jump prediction in Limit Order Book.

DOI: 10.4236/jmf.2013.32024

Text ingested: `markdown_output/zheng-2013-price-jump-prediction-limit-order-book.md`, converted from `raw/ofi-event-clock/zheng-2013-price-jump-prediction-limit-order-book.pdf`.

Coverage of this summary: Read the whole paper: abstract, introduction, limit order book notation and data description, the bid-ask liquidity balance / trade-sign empirical section, the logistic regression and LASSO methodology, the AUC and variable-selection results, and the conclusion.

Known problems with the input: Table 2 (per-stock event counts) and the captions for Figures 3-7 render with jumbled column/row structure in this markdown conversion; only the prose-stated summary numbers were used here, not the raw per-stock table values.
<!-- AUTHORED REGION END -->