---
authors:
- Jie Lu
content_hash: sha256:fe99a0e4a02993b362faa1389275e309174a0e3d48865358af051eb3b4da96be
created: 2026-09-27 01:47:00+00:00
page_id: sources/lu-2009-essays-behavioral-finance-market-microstructure
page_type: source
publication_venue: Rutgers, The State University of New Jersey (PhD dissertation,
  Graduate Program in Economics; dissertation director Bruce Mizrach)
related:
- concepts/trade-clock
- concepts/limit-order-book
- concepts/price-impact
- concepts/order-imbalance
- concepts/bid-ask-spread
- concepts/market-microstructure
- concepts/informed-trading
- concepts/liquidity-risk
- concepts/trade-classification
revision_id: 1
schema_version: 2
source_hash: sha256:7cec801c336c438c72da27f022136c901cbe20bb663ea0723d0a64a467b517f0
source_path: markdown_output/lu-2009-essays-behavioral-finance-market-microstructure.md
source_type: paper
tags:
- market-microstructure
- limit-order-book
- cds-market
- order-imbalance
- bid-ask-spread
- otc-derivatives
- china-equities
- behavioral-finance
- clock-trade
- asset-multi
- harvest-relevant
title: Essays on Behavioral Finance and Market Microstructure
updated: '2026-09-27T01:47:00Z'
uuid: 93454ed4-308a-525d-8909-8e944a8cdae7
year: 2009
---

<!-- AUTHORED REGION START -->
# Essays on Behavioral Finance and Market Microstructure

## Summary

This 2009 Rutgers economics dissertation is comprised of three separate essays under one advisor. The first models individual day traders' interactions in an internet stock-trading chat room as a dynamic signaling game with informed traders, momentum traders, noise traders, and arbitrageurs, then tests the model's predictions against a data set of chat-room posts and trades from more than 1,000 traders. The second studies the market impact of the full limit order book (not just the best quote) on the Shanghai and Shenzhen stock exchanges, using and extending Hasbrouck's (1991) structural vector-autoregressive model. The third is an empirical microstructure study of the credit default swap (CDS) over-the-counter market, covering CDS spread, trade-to-quote ratio, bid-ask spread, the frequency trades fall inside the quoted range, and the link between order imbalance and spread changes.

In the chat-room essay, all three of the model's equilibrium predictions were confirmed: more profitable traders posted more fundamental analysis and less profitable traders posted more non-fundamental analysis; less profitable traders followed others more often; and more profitable traders were followed more often. In the Chinese limit-order-book essay, estimated market impact was positively related to turnover and market capitalization and negatively related to tick frequency for A shares, and small trades (below the paper's own size cutoff) had a much smaller price impact than larger trades, with the daily order imbalance of small trades negatively related to same-day and next-day stock returns. In the CDS essay, liquidity proxies (trade-to-quote ratio, bid-ask spread, percentage bid-ask spread) varied widely across CDS index, sovereign/municipal, financial, and other corporate reference entities and by currency/region, with U.S. dollar financial-sector CDS relatively liquid before their liquidity deteriorated through the 2007-2008 financial crisis; daily order imbalance was also linked to the direction of CDS spread changes.

The dissertation frames each essay as a first of its kind: the first study of real-time interaction among individual traders using a live chat room rather than delayed bulletin-board posts; the first application of a Hasbrouck-style vector-autoregressive limit-order-book model to intraday quotes in the Chinese A/B/H share market; and an empirical microstructure study of the CDS OTC market spanning index, sovereign, and corporate reference entities from April 2006 to March 2008, a period that runs through the early stage of the financial crisis and while CDS still traded almost entirely through voice and electronic interdealer brokers rather than a central exchange.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Chapter 3 estimates a Hasbrouck-style vector-autoregression on the limit order book with time indexed in trades/ticks rather than the wall clock, reporting the cumulative market-impact response several tick-periods (M, averaging about 3 minutes) after a marginal buy order. Chapter 4 records CDS quotes and trades whenever they update, with no fixed sampling interval, then aggregates order imbalance and spread changes to a daily frequency to test contemporaneous and next-day relationships. Chapter 2 time-stamps chat-room posts and trades to the minute over a single sample month and studies posting and following behavior in aggregate across the whole sample rather than at one fixed prediction horizon. This single note covers all three essays in the dissertation; the paper does not itself compare clocks against each other.

## Data

- **Asset class:** Several asset classes
- **Instruments:** Chapter 2: a US stock day-trading chat room's posts and trades (equities, unnamed tickers such as CSCO/INTC/YHOO appear in log excerpts). Chapter 3: Shanghai and Shenzhen A shares, B shares (USD-denominated) and H shares (HKD-denominated, Shenzhen only). Chapter 4: CDS on 2695 reference entities across CDS indexes, sovereign/municipal governmental bonds, and financial and other corporate bonds, denominated in USD, EUR, JPY, GBP and AUD.
- **Venue:** Active Trader Financial Chatroom (Ch.2); Shanghai Stock Exchange and Shenzhen Stock Exchange (Ch.3); OTC CDS market, records from interdealer broker GFI Group Inc.'s brokerage desks and its CreditMatch electronic platform (Ch.4).
- **Period:** October 2000, 14 trading days (Ch.2); June 2007 (Ch.3); April 2006 to March 2008 (Ch.4).
- **Granularity:** Chat posts and trades time-stamped to the minute (Ch.2); limit order book with 5 bid/ask tiers, updated no faster than every second, trade-driven (Ch.3); intraday CDS quote (1 bid, 1 ask) and trade records updated whenever quoted, later aggregated to daily order imbalance and spread changes (Ch.4).

## Features and Measures

- **Hasbrouck market-impact VAR.** A vector-autoregression relating the percentage change in the bid-ask midpoint to lagged quote revisions and signed trade indicators, used to estimate how much a marginal buy order permanently moves the quote midpoint after several tick-periods.
- **Extended limit-order-book VAR.** An extension of the Hasbrouck VAR that adds price and depth information from several tiers of the bid and ask book, not just the best quote, to the same market-impact estimation.
- **Trade-to-quote ratio.** The ratio of completed trades to quote updates for a given reference entity or stock, used as a proxy for how quickly a counterparty can be found and hence for market liquidity.
- **Bid-ask spread and percentage bid-ask spread.** The gap between the best bid and ask price (BAS), and that gap expressed as a percentage of the mid-price (%BAS), used as liquidity measures for CDS contracts.
- **Daily order imbalance.** The net of buyer-initiated minus seller-initiated trading, volume-weighted for equities and as an unweighted trade count for CDS, aggregated to a daily frequency and related to same-day and next-day price or spread changes.

## Method

Chapter 2 builds a two-period dynamic game among informed traders, momentum traders, noise traders, and arbitrageurs who submit orders to a market maker, then solves for symmetric Bayesian Nash equilibria with and without a public communication (posting) channel, deriving three testable predictions about who posts fundamental versus non-fundamental content and who gets followed. These are tested with regressions of posting frequency and a 'being-followed' rate on estimated per-trade profits, computed under two alternative transaction-cost and position-size assumptions.

Chapter 3 estimates Hasbrouck's (1991) structural VAR linking trade signs and quote revisions on Chinese A/B/H shares, then extends it to include several tiers of book depth and price on each side, following Mizrach (2008). Market impact is judged from the cumulative response of the quote midpoint several tick-periods after a one-unit buy order; cross-sectional regressions then relate estimated impact to turnover, market capitalization, and tick frequency, and impacts are compared separately for trades below and above a working small-trade size cutoff.

Chapter 4 is largely descriptive: it tabulates CDS spread, trade-to-quote ratio, bid-ask spread and percentage bid-ask spread, and the frequency that trades occur inside versus outside the quoted range, broken out by reference-entity category (index, sovereign/municipal, financial corporate, other corporate) and by currency/region. It then regresses daily and next-day CDS spread changes on the daily, unweighted order imbalance to judge whether buyer- versus seller-initiated flow predicts spread moves.

## Results

- In the chat-room sample, more than 50% of the roughly 1,000 traders were profitable under the paper's conservative transaction-cost assumption, and all three of the model's predictions about posting and following behavior were confirmed empirically.
- About 70% of chat-room trade posts could not be matched into completed round trips over the 14 trading days studied, so profits were estimated assuming all open positions closed at day end.
- In the Shanghai/Shenzhen limit order book study, A-share market impact was positively related to turnover and market capitalization and negatively related to tick frequency; pooling in B and H shares dropped market capitalization from significance while turnover and tick frequency remained related to impact.
- Small trades (below the paper's 650-share cutoff) had a much smaller price impact than average-size trades under both the baseline Hasbrouck model and the extended limit-order-book model, and the daily order imbalance of small trades was negatively related to same-day and next-day stock returns.
- The CDS data set covered 2695 reference entities and contained 1554732 quotes and 135544 trades (1192839 bids, 1073450 asks) from GFI Group's interdealer-broker desks and CreditMatch platform between April 2006 and March 2008.
- Only 53% of CDS trades had both a bid and an ask recorded at the time of trade; of 261596 trades examined for placement relative to the quotes, less than half fell inside the quoted bid-ask range, consistent with an illiquid, broker-intermediated OTC market.
- CDS index trades occurred roughly once every 30 quotes overall; U.S. dollar-denominated financial-sector CDS had the highest trade-to-quote ratio of the categories studied, indicating relatively higher liquidity there before the financial crisis.
- Daily CDS order imbalance was linked to the direction of spread changes: CDS index and financial CDS categories showed positive median order imbalance while sovereign and non-financial industrial CDS showed negative median order imbalance, and spreads moved in the direction of buyer- versus seller-initiated order flow.

## Limitations

- The chat-room sample covers a single month (October 2000) with only 14 trading days, and about 70% of posted trades could not be matched into completed round trips, limiting the precision of individual profit estimates.
- The Chinese limit-order-book study uses one month of data (June 2007) and restricts the market-impact analysis to stocks above a minimum monthly trading-volume threshold, so results may not generalize to less liquid names or other periods.
- The CDS analysis draws on records from a single interdealer broker (GFI Group), so order flow intermediated by other dealers or brokers during the same period is not observed.
- Reader note: none of the three essays analyzes cash government or corporate bonds directly; the closest link to bond markets is the CDS reference entities (including sovereign, municipal and corporate bonds) and the general OTC/interdealer-broker microstructure discussion in Chapter 4.
- Reader note: many of the paper's own decimal results (e.g., median market-impact and trade-to-quote-ratio figures) are rendered with a colon in place of a decimal point in this converted markdown (for example '0:1367%'), which this note treats as unverifiable and excludes rather than risk copying a wrong digit.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/price-impact|price impact]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/liquidity-risk|liquidity risk]]
- [[concepts/trade-classification|trade classification]]

## Citation

Jie Lu (2009). Essays on Behavioral Finance and Market Microstructure. Rutgers, The State University of New Jersey (PhD dissertation, Graduate Program in Economics; dissertation director Bruce Mizrach).

DOI: 10.7282/t36973qc

Text ingested: `markdown_output/lu-2009-essays-behavioral-finance-market-microstructure.md`, converted from `raw/ofi-event-clock/lu-2009-essays-behavioral-finance-market-microstructure.pdf`.

Coverage of this summary: Read the abstract, acknowledgements, and full table of contents; read Chapter 1's introduction; read Chapter 2 in full apart from the two mathematical proof appendices (Sections 2.7-2.8); read Chapter 3 in full (data, Hasbrouck model, extended limit-order-book model, cross-sectional estimation, small trades, conclusion); read Chapter 4 in full (data, spread, trade-to-quote ratio, bid-ask spread, trades within quotes, order imbalance, conclusion); read Chapter 5's conclusion. Did not read the data tables and figures themselves (Sections 2.9, 3.8, 4.9-4.10) or the bibliography/curriculum vita.

Known problems with the input: The PDF-to-markdown conversion drops nearly all mathematical notation, replacing equations, propositions and payoff expressions with '[picture... intentionally omitted]' placeholders, so the formal game-theoretic and VAR specifications in Chapters 2 and 3 could not be verified beyond the surrounding prose; Many decimal figures in this converted markdown are rendered with a colon instead of a decimal point (e.g. '0:1367%', '38:6 trillion') and some large integers use semicolons as thousand separators (e.g. '1; 555; 000'); these were excluded from numbers_used and from the results/limitations text as unverifiable rather than risk transcribing a wrong digit; Ligature corruption throughout the OCR'd text (e.g. 'pro…t' for 'profit', '…rst' for 'first', 'de…ned' for 'defined') was silently normalized when paraphrasing but is noted here in case it affects downstream automated checks.
<!-- AUTHORED REGION END -->