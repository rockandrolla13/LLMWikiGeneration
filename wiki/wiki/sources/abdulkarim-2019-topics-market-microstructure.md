---
authors: []
content_hash: sha256:1959c7ff58a8feadf61bafa6f8f1edefcddee5f2bf088a13057ab632d9f4d9f5
created: 2026-09-27 01:47:00+00:00
page_id: sources/abdulkarim-2019-topics-market-microstructure
page_type: source
publication_venue: University of Essex, Department of Economics (PhD thesis)
related:
- concepts/sampling-clocks
- concepts/limit-order-book
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/bid-ask-spread
- concepts/order-flow
- concepts/high-frequency-data
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:fe2bad7f75c094e2c7f58a517a5adfd54b153ffb1748e0e7c6559bf99e9f791b
source_path: markdown_output/abdulkarim-2019-topics-market-microstructure.md
source_type: paper
tags:
- limit-order-book
- high-frequency-trading
- directional-changes
- order-cancellations
- market-simulation
- transaction-tax
- nvwap
- london-stock-exchange
- clock-compares
- asset-equity
- harvest-relevant
title: Topics in Market Microstructure
updated: '2026-09-27T01:47:00Z'
uuid: 43bcf28e-7397-5870-add0-2d209f3682ee
year: 2019
---

<!-- AUTHORED REGION START -->
# Topics in Market Microstructure

## Summary

This PhD thesis in economics presents three distinct studies in market microstructure. The first asks whether a proposed EU financial transaction tax (FTT) of 0.1% would harm high-frequency traders and market quality, tested via an agent-based simulation rather than real data, since none existed yet for a tax that had not been implemented. The second and third studies both rebuild the London Stock Exchange's SETS electronic order book in real time for 5 stocks over July and August 2007 and sample the data at peaks and troughs of cumulative price return, in the style of the Directional Changes methodology.

The second study asks whether the shape of the bid and ask sides of the order book, captured via Notional Volume Weighted Average Price (NVWAP) curves, can identify the prevailing price trend without knowing the price itself, replicating and extending Malik and Markose (2012). The third study asks whether order cancellations, as distinct from new submissions, on each side of the book help explain the size of price drops and a proposed spread/volatility measure during downtrend (peak-to-trough) moves, motivated by concerns that cancellations contributed to flash crashes.

The simulation found the tax increased trading volume and narrowed the spread in the scenarios tested, while price-return volatility was little changed, supporting the tax rather than the hypothesis that it would harm HFTs. The NVWAP-shape indicator correctly identified price trends in the large majority of cases in-sample, though its out-of-sample accuracy fell markedly for less liquid stocks in the more volatile month. The cancellation study found buy-side cancellations and submissions were significant drivers of large price drops, and in some specifications of the proposed spread measure, with the significant side and direction depending on whether the market was calm or volatile and on whether the price move was of normal or extreme size.

The thesis's contributions are applying agent-based simulation to a policy question (the FTT) with no real-data precedent to test it against; showing that NVWAP curve shape and volume statistics are usable predictive proxies that do not require price history; and introducing a peak-trough (event-based) sampling scheme plus an NVWAP-slope-based spread measure to study order cancellations, in place of the fixed calendar-time sampling used elsewhere in that literature.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Chapter 2 simulates a continuous double-auction market in artificial clock time (300,000 simulated seconds, about 11 trading days), not sampled from real data. Chapters 3 and 4 use an intrinsic, price-move-based clock: order book snapshots are taken at peaks and troughs of cumulative price return identified by a Directional-Changes-style threshold of 25bp, defining uptrend/downtrend intervals of varying duration. Chapter 3 additionally compares this event-based sampling against fixed calendar intervals (5, 10 and 15 minutes) in an out-of-sample robustness check of the same trend-prediction indicator. Chapter 4 explains the change in cumulative return (and a proposed NVWAP-based spread measure) from peak to trough as a function of order submissions and cancellations recorded within each such peak-to-trough interval. (This single field is a compromise across three chapter-studies with different designs; see method for the per-chapter breakdown.)

## Data

- **Asset class:** Equities
- **Instruments:** 5 LSE-listed stocks used in Chapters 3-4: HSBC Holdings (HSBA), British Petroleum (BP), Tesco (TSCO), AstraZeneca (AZN), Vodafone Group (VOD). Chapter 2 instead simulates a single artificial stock in an agent-based limit order market with a fixed population of 2050 traders (2052 including two informed traders in the news-flow scenario).
- **Venue:** London Stock Exchange Electronic Trading System (SETS) order book (Chapters 3-4); Chapter 2 is a Matlab-based agent simulation built on the platform of Daniel and Cappellini (2006), not a real exchange.
- **Period:** Chapters 3-4: July and August 2007, 44 trading days, order book rebuilt in real time. Chapter 2: a simulated run of 300,000 seconds (assuming a 27000-second trading day), run four times crossing a 0.1% transaction tax (on/off) with an exogenous news-flow process (on/off).
- **Granularity:** Chapters 3-4: ultra-high-frequency order-book event data reconstructed tick by tick, sampled at peak/trough turning points (minimum 25bp cumulative-return move) and also at fixed 5-, 10- and 15-minute intervals for robustness checks; intraday window 8:01 AM to 4:29 PM to exclude auctions. Chapter 2: simulated continuous double auction with book depth of 1024 orders and tick size of 0.01.

## Features and Measures

- **Notional Volume Weighted Average Price (NVWAP).** The average expected transaction price for a trade of a given cumulative size, computed by walking down one side of the order book; used to model the shape of the bid and ask sides.
- **NVWAP curve slope (steepening/flattening indicator).** The regression slope of market impact (NVWAP minus mid-price) against cumulative normalized volume on each side of the book; the change in its log is used to detect steepening versus flattening of that side.
- **Bid/ask volume contraction-expansion indicator.** The change in log total volume available on the bid or ask side of the book between the start and end of a trend interval, used jointly with the slope indicator to signal the prevailing price trend.
- **Peak-Trough (Directional-Changes-style) sampling.** Turning points in cumulative price return are located whenever the return moves by at least a threshold (25bp) from the last extreme, splitting the series into uptrend and downtrend intervals used as the unit of analysis instead of fixed calendar bars.
- **Order cancellation/new-order volume by side.** Total and average buy- and sell-side new order and cancellation volumes (raw, normalized by average daily volume, or logged) within each peak-to-trough interval, used as regressors for the size of the price move and for a spread measure.
- **NVWAP-slope-based bid-ask spread measure.** A proposed volatility/spread measure defined as the change in the log of the NVWAP curve slopes (bid and ask) from peak to trough, used as an alternative to the conventional best bid-ask spread.

## Method

Chapter 2: an agent-based simulation, built on the Daniel and Cappellini (2006) platform, of a pure continuous double-auction limit order market with a fixed population of heterogeneous zero-intelligence agents (random liquidity providers, an informed trader, and a data-driven top-percentile 'HFT' group following Kirilenko et al. 2011). It is run four times, crossing a 0.1% financial transaction tax (on/off) with an exogenous news-flow process (on/off), and compares trading volume, bid-ask spread and a mean-adjusted return-variance estimator across the four runs.

Chapter 3: the LSE SETS limit order book for 5 stocks is reconstructed in real time for July-August 2007. Cumulative mid-price returns are used to locate peaks and troughs (at least 25bp), and at each such point the bid- and ask-side NVWAP curves are estimated by regressing market impact on cumulative normalized volume; the resulting slope and volume statistics at the start and end of each uptrend/downtrend interval are compared against a hypothesized sign pattern, then tested out-of-sample at fixed 5-, 10- and 15-minute prediction horizons.

Chapter 4: using the same reconstructed order book, buy- and sell-side new-order and cancellation volumes within each peak-to-trough interval are regressed (by OLS and by robust regression) against the size and per-minute rate of the cumulative-return move, and against a proposed NVWAP-slope-based spread measure, under several specifications (volumes normalized by average daily volume; logged total volumes; logged average volumes; with and without a duration control), separately for normal (up to 100bp) and extreme (over 100bp) return changes.

## Results

- Chapter 2 (simulated market): after introducing the 0.1% transaction tax, volume transacted by the top 20% of traders rose (from 3,882,322 to 4,304,650 in the closed-market run without news, an increase of about 11%), the bid-ask spread narrowed in the open-market run with news flow (from 0.54 to 0.21), and estimated price-return volatility changed little (15.98% to 18.46% in the closed-market run; 6.73% to 7.23% with news flow).
- Chapter 3 (NVWAP trend indicator, in-sample): steepening/flattening and contraction/expansion behaviour of the NVWAP curves correctly identified the prevailing price trend in 86.61% of all uptrend/downtrend intervals across the 5 stocks, ranging from 86.34% (AZN) to 95.39% (HSBA) on the steepening/flattening measure.
- Chapter 3 (out-of-sample, fixed intervals): at a 5-minute prediction horizon the indicator correctly identified the price trend in 61.42% of observations across all five stocks in the more volatile month of August 2007, versus 69.61% in the calmer month of July 2007; for the least liquid stock (AZN) accuracy was only 25.99% in August versus 70.94% in July.
- Chapter 4 (descriptive): on average around 77% of new orders submitted across the 5 stocks were subsequently cancelled before execution (75.35% buy-side and 75.91% sell-side in July; 77.39% and 78.22% in August).
- Chapter 4 (extreme cumulative-return changes): buy-side cancellations and buy-side new-order submissions were highly significant determinants of the size of the cumulative-return drop from peak to trough under extreme price conditions in both July and August, while neither sell-side cancellations nor sell-side submissions were significant in either month.
- Chapter 4 (normal cumulative-return changes): sell-side cancellations and new orders were significant determinants of the cumulative-return change in August across all three model specifications, but only weakly so in July; the best-fitting size-of-drop model in August reached an R-squared of 55%.
- Chapter 4 (spread analysis): the NVWAP-slope-based spread measure was significantly related to sell-side cancellations and new orders in July under extreme cumulative-return changes, and to buy-side cancellations under normal conditions, but none of the three model specifications found significant effects in August under extreme conditions.
- Robust regressions largely confirmed these patterns; under extreme cumulative-return conditions in the volatile month (August), buy-side cancellations also became a significant determinant of the spread.

## Limitations

- The FTT simulation (Chapter 2) is not calibrated to or validated against real market data; the author describes it as a first, simplified test of the tax's effect and calls for follow-up work using real data.
- Chapters 3-4 cover only 5 LSE stocks over two months (July-August 2007), one calm and one crisis month, with the peak-trough threshold fixed at 25bp throughout.
- The order-book data used in Chapter 4 carries no trader identities, so specific manipulative strategies (e.g. spoofing, layering) cannot be traced to individual traders, only inferred from aggregate cancellation patterns.
- Reader note: because this record combines three distinct chapter-studies (an agent-based tax simulation and two empirical LSE order-book studies) into one paper entry, the single clock/data/asset_class fields above are a compromise across chapters; see clock.detail and method for the per-chapter breakdown.
- Reader note: the thesis itself states its cancellation-effect models are 'rather simple and general' and that quantifying the economic (as opposed to statistical) significance of cancellation effects remains open for future work.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/order-flow|order flow]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/directional-change|Directional Change]]

## Citation

Author not stated (2019). Topics in Market Microstructure. University of Essex, Department of Economics (PhD thesis).

Text ingested: `markdown_output/abdulkarim-2019-topics-market-microstructure.md`, converted from `raw/ofi-event-clock/abdulkarim-2019-topics-market-microstructure.pdf`.

Coverage of this summary: Read Chapter One's introduction; Chapter Two (transaction tax simulation) in full except the literature-review and case-study subsections; Chapter Three (NVWAP price-trend indicator) in full except most of the literature review; Chapter Four (order cancellations) in full for the introduction/motivation, data, results and conclusion, with the detailed model-specification derivations in section 3.2 read via headers and the results-table restatements rather than line by line; and Chapter Five's overall thesis conclusion. Literature-review subsections and the reference list were not read in detail.

Known problems with the input: The author's name is not printed anywhere in the converted markdown; the title page gives only the title, degree, department, university and submission date (January 2019). The job file's slug implies a surname, but that is a filename, not source content, so authors/author_affiliations are left empty rather than inferred; This record combines three distinct chapter-studies (an agent-based FTT simulation and two empirical LSE order-book studies) into one paper entry, per the required schema; the clock/data/asset_class fields are necessarily a compromise across chapters; The markdown has OCR/PDF-conversion artifacts: many stray page-footer numbers embedded mid-sentence, several truncated or garbled sentences (e.g. missing subjects in some Chapter 3/4 methodology sentences), and at least one internal numeric inconsistency in the source itself (Chapter 2's prose gives a second 'total volume traded' figure for the after-tax, with-news scenario, 4,406,196, that does not match the 4,406,250 shown in its own Table 6); Detailed model-specification derivations in Chapter 4 (the numbered MODEL SPEC blocks in section 3.2) and most literature-review subsections across all chapters were not read in full; only their headers, stated motivation, and the specifications as restated in the results tables were used.
<!-- AUTHORED REGION END -->