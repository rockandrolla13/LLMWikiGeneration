---
authors:
- Haiming Luo
content_hash: sha256:f239ad68f0edb3458ad1a274078a168e24d4c92e5dbcc62dadfa47e272d70e75
created: 2026-09-27 01:47:00+00:00
page_id: sources/luo-2011-profitable-opportunities-around-macroeconomic-announcements-u
page_type: source
publication_venue: Brock University
related:
- concepts/informed-trading
- concepts/order-imbalance
- concepts/order-flow
- concepts/adverse-selection
- concepts/limit-order-book
- concepts/bid-ask-spread
- concepts/market-microstructure
- concepts/bond-liquidity
revision_id: 1
schema_version: 2
source_hash: sha256:a6684967535f44a97eb19d442ee30d6b6446497f7c5cc46d25b385b6fad3cbf2
source_path: markdown_output/luo-2011-profitable-opportunities-around-macroeconomic-announcements-u.md
source_type: paper
tags:
- treasury-bonds
- trade-imbalance
- order-book-slope
- macro-announcements
- informed-trading
- dispersion-of-beliefs
- market-microstructure
- trading-strategy
- clock-calendar
- asset-bonds-rates
- harvest-relevant
title: Profitable Opportunities around Macroeconomic Announcements in the U.S. Treasury
  Market
updated: '2026-09-27T01:47:00Z'
uuid: d55b955d-56a8-5190-bf8d-8f192b404333
year: 2010
---

<!-- AUTHORED REGION START -->
# Profitable Opportunities around Macroeconomic Announcements in the U.S. Treasury Market

## Summary

The thesis asks how macroeconomic announcements, informed trading and dispersion of beliefs among investors jointly affect the ability of daily trade imbalance to predict next-day returns in the U.S. Treasury market, using six-tier eSpeed order book and trade data for 2-year, 5-year and 10-year Treasury notes and the 30-year Treasury bond from June 2005 to May 2008. Unlike prior studies that estimate trade imbalance from all trades, it first separates likely informed trades from liquidity trades by ranking orders on aggressiveness (how far a trader executes across order-book tiers) and size, treating the largest and medium-sized most-aggressive trades as a proxy for informed trading.

To capture how hard a given announcement is to interpret, the thesis constructs a daily order book slope: the elasticity of cumulative order-book volume to price across the first five tiers on each side, averaged across bid and ask sides and across several intraday snapshots. A gentler slope is read as greater disagreement among investors about fair value. Daily regressions of next-day returns on lagged and contemporaneous trade imbalance, order-book imbalance, and announcement/dispersion dummies are used to test whether informed-trade imbalance is especially informative on announcement days when beliefs are most dispersed.

The main finding is that, on macro-announcement days with a high dispersion of beliefs (the order book slope in the bottom quarter to bottom sixth of its distribution), the trade imbalance estimated from aggressive trades significantly and positively predicts the following day's return for the 2-year, 5-year and 10-year notes, even after controlling for the current day's imbalance. A trading strategy built on this signal, conditioned on low order-book slope and announcement timing, produces positive average returns for all three note maturities but is only statistically significant for the 2-year note.

What the thesis adds relative to earlier trade-imbalance literature is the separation of informed from liquidity-driven trade imbalance using order aggressiveness, and the use of a market-based order book slope, rather than the dispersion of professional forecasts, as the proxy for dispersion of beliefs; the author describes this as the first study of the Treasury market's reaction to announcements conditioned on dispersion measured this way.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The order book slope is built from eight fixed hourly snapshots between 8:30am and 15:30pm (later summary tables instead use 20 half-hourly snapshots across the 7:30am to 5:30pm U.S. session). Trade imbalance and order book imbalance are aggregated to the daily level using the day's first and last mid-quotes, and the main regressions predict the following trading day's log return from the current and one-day-lagged imbalance variables. A separate price-impact regression instead divides the trading day into 108 five-minute intervals and regresses five-minute price changes on trade imbalance within each interval; intraday bid-ask spreads around announcements are examined in one-minute intervals.

## Data

- **Asset class:** Bonds and rates
- **Instruments:** On-the-run 2-year, 5-year and 10-year U.S. Treasury notes and the 30-year U.S. Treasury bond
- **Venue:** eSpeed electronic trading platform (Cantor Fitzgerald)
- **Period:** 1 June 2005 to 30 May 2008 for the Treasury and trade-imbalance analysis; macroeconomic announcement/consensus data for sixteen indicators over the same window
- **Granularity:** Six-tier order book and trade records timestamped to the millisecond, aggregated into hourly or half-hourly snapshots, 5-minute intervals (price impact regression), 1-minute intervals (intraday spread analysis) and daily totals (main return-predictability regressions and trading strategy)

## Features and Measures

- **order book slope.** a measure of the elasticity of cumulative order-book volume to price across the first five tiers on each side, averaged across bid and ask sides and across several intraday snapshots, used as a daily proxy for the dispersion of beliefs among investors; a gentler slope indicates more disagreement about fair value.
- **order aggressiveness classification (A1/A2, large/medium/small).** trades are split into two aggressiveness tiers -- A1 (the trader executes across multiple order-book tiers to fill the desired quantity) and A2 (the trader only trades at the first tier) -- and three size tiers; the largest and medium-sized A1 trades are used as a proxy for informed trades.
- **trade imbalance from informed trades (TIBA1).** buyer-initiated minus seller-initiated large and medium most-aggressive (A1) trades on a given day, used as a daily estimate of the net position taken by informed traders, distinct from trade imbalance computed over all trades.
- **order book imbalance (OIB).** at each intraday snapshot, the sum of bid-side volumes across the first five tiers minus the sum of ask-side volumes across the first five tiers; the daily order book imbalance sums the snapshot-level values across the trading day.
- **macroeconomic surprise.** the standardized difference between an actual macroeconomic release and its consensus forecast value, divided by the sample standard deviation of that difference for the given indicator, used to flag announcement days with unusually large surprises.

## Method

The thesis first estimates a price-impact regression of five-minute price changes on trade imbalance to benchmark eSpeed market liquidity against prior GovPX-based estimates. It then runs daily regressions of next-day log returns on current and one-day-lagged trade imbalance (both aggregate and informed-trades-only), current order book imbalance, and dummy variables marking announcement days and low (bottom quarter, fifth or sixth) order book slope, separately for each of the four securities. Descriptive statistics on trading volume, frequency, trade size, quote size, bid-ask spreads and order book slope are compared across announcement and non-announcement days, and across days with high macroeconomic surprise versus high dispersion of beliefs, using t-tests and Wilcoxon signed-rank tests.

Building on the regression results, the thesis constructs and backtests a daily trading strategy: buy (sell) at the day's opening ask (bid) quote and reverse at the day's closing bid (ask) quote when the prior day's trade imbalance was positive (negative), applied only on days meeting a chosen combination of low order book slope and, in a further variant, prior-day announcement timing. Average returns and t-statistics are compared across trade-imbalance definitions (aggregate versus informed-trades-only) and slope thresholds, and against a reproduction of Chordia and Subrahmanyam's (2004) unconditional trade-imbalance strategy.

## Results

- The average order book slope over the full sample is 25.14 for 2-year notes, falling to 17.64 for 5-year notes, 9.06 for 10-year notes and 3.89 for the 30-year bond, so the slope flattens (implying more dispersion of beliefs) as maturity lengthens.
- The price-impact coefficient of trade imbalance on 5-minute price changes for 2-year notes is 0.000973 with an adjusted R-squared of 0.1159, compared with a coefficient of 0.0465 and adjusted R-squared of 0.322 reported for 2-year notes using older GovPX data.
- On macro-announcement days with the bottom-1/4 order-book slope, lagged trade imbalance from informed trades significantly and positively predicts next-day returns for the 2-year, 5-year and 10-year notes even after controlling for the current day's imbalance; the effect is larger and more significant using the bottom-1/6 grouping than the bottom-1/4 grouping for the 2-year and 5-year notes.
- In the dispersion-conditioned trading strategy (not restricted to announcement days), the 10-year note earns a significant average daily return of 0.144% when the order book slope is 20% below its trailing 365-day average.
- In the strategy further conditioned on announcement days, the 2-year note earns a significant average daily return of 0.083% when the prior day was an announcement day with order book slope 30% below its trailing 365-day average; after a $2.5-per-$1 million trading cost (versus about $39 per $1 million estimated for the older GovPX market), the net profit is $827.5 per $1 million traded.
- Average daily U.S.-hours trading volume for 2-year notes is $26485 million (median $24929 million), versus only $412 million in Tokyo hours and $1701 million in London hours.
- On announcement days with high dispersion of beliefs, average U.S.-hours trading volume for 2-year notes rises by 46% relative to non-announcement days, and the one-minute average bid-ask spread just before the 8:30am release widens by 114%.
- Reproducing Chordia and Subrahmanyam's (2004) unconditional trade-imbalance strategy (no dispersion or announcement conditioning) produces significantly negative average daily returns for the 2-year notes in this Treasury sample.

## Limitations

- The sample covers a single roughly three-year window (June 2005-May 2008) and only four on-the-run Treasury securities.
- The 30-year bond is thinly traded in this data, so the trading strategy is only developed for the 2-, 5- and 10-year notes.
- Of the three note maturities in the announcement-conditioned trading strategy, only the 2-year note's average return is statistically significant; the 5-year and 10-year results are described as positive but not significant.
- Reader note: this is a Master's thesis, and most supporting tables and figures (e.g. the numbered Tables 1-29) render in this markdown conversion as images or broken layout rather than text, so their exact reported values beyond what is restated in the prose could not be independently checked.

## Related

- [[concepts/informed-trading|informed trading]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/order-flow|order flow]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/bond-liquidity|bond liquidity]]

## Citation

Haiming Luo (2010). Profitable Opportunities around Macroeconomic Announcements in the U.S. Treasury Market. Brock University.

Text ingested: `markdown_output/luo-2011-profitable-opportunities-around-macroeconomic-announcements-u.md`, converted from `raw/ofi-event-clock/luo-2011-profitable-opportunities-around-macroeconomic-announcements-u.pdf`.

Coverage of this summary: Read the abstract, introduction, full literature review, full data description, full methodology section (order book slope, order aggressiveness, price impact, daily return regressions, return predictability), the full descriptive-statistics and regression results section, the full trading strategy section and the conclusion; the numbered tables/appendices themselves were not separately extracted beyond the values restated in the prose.

Known problems with the input: The job's slug and title_hint suggest 2011, but the thesis itself is copyright-dated 2010 ('©2010'); year was set to 2010 from that printed date rather than the hint; Several equations and figures render as garbled OCR fragments (e.g. broken subscripts and stray characters) in the markdown; those fragments were not used as a source of numbers or wording.
<!-- AUTHORED REGION END -->