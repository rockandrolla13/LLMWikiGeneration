---
authors:
- Chiara Coluzzi
- Sergio Ginebri
content_hash: sha256:c878571b7651df991f46a1c5bc9f849699ad85f1ace402db91159671410b5621
created: 2026-09-27 01:47:00+00:00
page_id: sources/ginebri-2008-order-dynamics-italian-treasury-security-wholesale
page_type: source
publication_venue: Universita degli Studi del Molise, Economics & Statistics Discussion
  Paper No. 50/08
related:
- concepts/limit-order-book
- concepts/order-flow
- concepts/bid-ask-spread
- concepts/bond-liquidity
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:ee4088755a41cdd508d72ed352d4a7ca12882aedf85e26647cebf3fd547b14d1
source_path: markdown_output/ginebri-2008-order-dynamics-italian-treasury-security-wholesale.md
source_type: paper
tags:
- government-bonds
- order-flow
- limit-order-book
- bid-ask-spread
- market-microstructure
- italy
- clock-calendar
- asset-bonds-rates
- harvest-relevant
title: Order Dynamics in the Italian Treasury Security Wholesale Secondary Market
updated: '2026-09-27T01:47:00Z'
uuid: 5316f430-bf9b-5fa0-ace1-a23980fef63e
year: 2008
---

<!-- AUTHORED REGION START -->
# Order Dynamics in the Italian Treasury Security Wholesale Secondary Market

## Summary

The paper asks how the order book and order flow interact on MTS, a quote-driven electronic limit order book market for Italian Government securities, and tests several hypotheses drawn from theoretical limit-order-book models (Parlour; Goettler, Parlour and Rajan; Foucault) on real Government bond data, which the authors describe as one of the first such tests outside equity or FX markets.

Using snapshots of the order book and trade records for the 10-year BTP traded on MTS from January 1, 2004 to November 13, 2006, the authors define order-flow variables (new best limit bid/ask orders, buy/sell market orders, cancellations, and no-activity) from changes in the best-price size between consecutive 5-minute snapshots, plus an extended set of variables that split limit orders by aggressiveness (inside-, at-, and behind-the-quote). Both the seven- and eleven-variable systems are estimated with seemingly unrelated regressions using the first lag of the order-flow and order-book-state variables as explanatory variables, after removing intraday seasonality from the mean and variance of each series.

The main finding is a 'diagonal effect': market and limit orders, and periods of no activity, are all positively autocorrelated, similar to earlier evidence from equity limit order markets. Best-price and second-price depth raise new limit orders on the same side of the book, but depth beyond the second price has no consistent effect, even though most of the book's volume sits there. A wider best bid-ask spread discourages market orders and, in the extended aggressiveness system, encourages limit orders placed inside the quote, consistent with theory. An increase in the number of quoting primary dealers unexpectedly reduces both limit and market order flow, and price-change volatility shows no measurable effect on order placement in this sample.

What is new is the direct empirical test of these order-book hypotheses on Government bond data rather than equities or FX, and the finding that book depth beyond the second-best price behaves as essentially irrelevant to order placement, unlike depth at the two best prices.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Order book proposals are recorded as snapshots every 5 minutes from 8:30am to 5:30pm; new limit orders, cancellations, and market order volumes are each computed as the change between consecutive 5-minute snapshots, even though the underlying transactions are timestamped to the second. The regression system uses the first lag (the previous 5-minute snapshot) of each order-flow and order-book-state variable to explain the current snapshot's order flows, so the effective prediction horizon is one 5-minute step ahead.

## Data

- **Asset class:** Bonds and rates
- **Instruments:** 10-year BTP (Italian Treasury bond), on-the-run and off-the-run series
- **Venue:** MTS (Mercato Telematico dei titoli di Stato), the Italian wholesale interdealer market
- **Period:** January 1, 2004 to November 13, 2006
- **Granularity:** order book snapshots every 5 minutes (8:30am-5:30pm); transactions timestamped to the second; around 148,000 observations

## Features and Measures

- **Diagonal effect.** The tendency for order flow of a given type (e.g. a market buy or a limit sell) to be positively autocorrelated, i.e. more likely to be followed by another order of the same type than an unconditional draw would predict.
- **Order book depth by level (best, second, worst size).** The quantity of limit orders available at the best price, at the second-best price, and beyond the second-best price on each side of the book, entered separately as explanatory variables for order flow.
- **Steepness and slope.** Steepness is the distance between the best and worst quoted price scaled by the midpoint, averaged across bid and ask; slope is the same price distance scaled by the volume available beyond the best price, so it captures both the breadth and the depth of the book.
- **Market quality index.** Average quoted quantity in the book scaled by the average percentage bid-ask spread, combining depth and tightness into a single liquidity indicator.

## Method

The authors define seven order-flow variables (new best limit bid/ask orders, buy/sell market orders, cancellations of best bid/ask orders, and no-activity) from 5-minute order book snapshots, attributing changes in best-price size to new limit orders or cancellations. An extended eleven-variable system further splits limit orders by aggressiveness into inside-, at-, and behind-the-quote categories on each side. Both systems are estimated with seemingly unrelated regressions (SUR), which allow contemporaneous cross-equation error correlation; because every equation shares the same explanatory variables, the SUR coefficients equal the OLS coefficients. Explanatory variables are the first lag of the order-flow variables themselves plus lagged order-book-state variables (best spread, depth at the best/second/worst price, number of book updates, number of operators, price change, steepness, slope, and the market quality index). All series are seasonally adjusted to remove intraday patterns in mean and variance before estimation.

## Results

- Market and limit orders show positive autocorrelation (clustering), consistent with the 'diagonal effect' found on the Paris Bourse by Biais et al. (1995); no-activity is clustered as well.
- Testing the alternative negative-autocorrelation hypothesis on first-differenced order variables found no support in this data.
- Best-price depth has a positive effect only on new limit orders on the same side of the book; it does not reduce same-side limit orders or raise opposite-side limit orders as theory predicts, and it does not affect market orders.
- Depth at the second-best price behaves like best-price depth, but depth beyond the second-best price (worst size) has no consistent positive effect on new limit orders, even though most of the book's volume sits beyond the second price.
- A wider best bid-ask spread has a negative effect on both market and limit orders in the seven-equation system, but in the eleven-equation system it raises inside-the-quote limit orders and lowers at- and behind-the-quote limit orders, consistent with theory.
- An increase in the number of market operators (primary dealers quoting) has a negative effect on both limit and market orders, contrary to the expectation that more competition would raise order flow.
- Absolute or signed price change, used as a volatility proxy, shows no significant effect on order placement in this sample.
- In the eleven-equation system, higher same-side depth raises inside-the-quote limit orders and lowers behind-the-quote orders, partially supporting a 'jump the queue' aggressiveness hypothesis, though it also raises at-the-quote orders, which the authors attribute to the diagonal effect dominating.

## Limitations

- The authors state that a thorough interpretation of the regularities found in the cancellation equations is currently missing.
- The paper studies a single instrument (the 10-year BTP) on a single market (MTS) over 2004-2006, so results may not generalize to other maturities or venues.
- Reader note: no goodness-of-fit statistics (e.g. R-squared) for the SUR equations are reported in the text, making it hard to judge how much of order flow variation is explained.
- Reader note: the paper reports only in-sample regression coefficients; it does not test out-of-sample predictive accuracy.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow|order flow]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/bond-liquidity|bond liquidity]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Chiara Coluzzi, Sergio Ginebri (2008). Order Dynamics in the Italian Treasury Security Wholesale Secondary Market. Universita degli Studi del Molise, Economics & Statistics Discussion Paper No. 50/08.

Text ingested: `markdown_output/ginebri-2008-order-dynamics-italian-treasury-security-wholesale.md`, converted from `raw/ofi-event-clock/ginebri-2008-order-dynamics-italian-treasury-security-wholesale.pdf`.

Coverage of this summary: Read the entire paper: introduction, literature review and tested hypotheses, market and dataset description, variable definitions and empirical strategy, results for both the seven- and eleven-equation systems, conclusion, and all tables.

Known problems with the input: Markdown conversion garbles some table structure (merged header cells, footnote digits appended to values), but the prose and readable parts of the tables were sufficient to cross-check the numbers used here.
<!-- AUTHORED REGION END -->