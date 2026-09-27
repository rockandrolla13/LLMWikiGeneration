---
authors:
- Petko Stefanov Kalev
- Alex Lee
content_hash: sha256:e8f3d694ad3ba4c7ae73d53796b929f353433da190136ffdd39de4e9767ed96f
created: 2026-09-27 01:47:00+00:00
page_id: sources/kalev-2025-lietf-trading-behavior-during-u-s
page_type: source
publication_venue: Economics - Innovative and Economics Research Journal
related:
- concepts/etf-flows
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/informed-trading
- concepts/trade-classification
revision_id: 1
schema_version: 2
source_hash: sha256:b24602e8bb618fe944425ca1fe24a2535dda41285dc90ebeeb8a4558f011913e
source_path: markdown_output/kalev-2025-lietf-trading-behavior-during-u-s.md
source_type: paper
tags:
- etf
- leveraged-etf
- order-imbalance
- trade-war
- event-study
- momentum
- informed-trading
- clock-calendar
- asset-equity
- harvest-relevant
title: Lietf Trading Behavior During U.S. – China Trade War
updated: '2026-09-27T01:47:00Z'
uuid: 583b92f0-68e2-5ce5-aa91-cb8266a0bf52
year: 2025
---

<!-- AUTHORED REGION START -->
# Lietf Trading Behavior During U.S. – China Trade War

## Summary

The paper studies how investors in Leveraged and Inverse Exchange-Traded Funds (LIETFs) tracking the S&P 500 and Nasdaq-100 behaved during the early phase of the 2018 U.S.-China tariff trade war, asking whether their trading reflects informed forecasting of index moves or merely short-term momentum chasing.

Using Reuters trade and quote data for the 12 most liquid U.S. LIETFs from January to November 2018 and a hand-collected list of 17 trade-war news events, the authors build two measures of abnormal trading activity -- an abnormal buy-sell ratio and an abnormal order imbalance -- and estimate panel regressions at 5-, 15-, 30- and 60-minute intervals to test three hypotheses: that trading activity shifts around news, that abnormal activity predicts subsequent index returns, and that investors chase short-term momentum.

Trading volumes and order imbalances change significantly around trade-war news, generally declining from the pre-news to the post-news period, which supports the first hypothesis. However, neither the abnormal buy-sell ratio nor the abnormal order imbalance reliably predicts future index returns, so the authors find little evidence that LIETF investors possess forecasting skill. Instead, order imbalance is positively related to past returns at intervals under 30 minutes (trend-chasing) but negatively related at the 60-minute interval (reversal-seeking).

The paper's contribution is proposing the abnormal buy-sell ratio and abnormal order imbalance as new measures of LIETF trading activity and applying them to a geopolitical news setting, concluding that LIETF investors behave as speculative, momentum-driven traders rather than informed ones around trade-war announcements.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Trade and quote data are aggregated into fixed calendar intervals of 5, 15, 30 and 60 minutes during the continuous trading session (9:30 a.m. to 4:00 p.m.) on the NYSE and NASDAQ. Within each interval, trades are signed buyer- or seller-initiated using the Lee-Ready algorithm and used to build cumulative buy/sell values and order imbalance; the prediction target is the underlying index's return over the same forward interval, so the horizon is simply the length of the calendar interval used, from 5 minutes up to 60 minutes.

## Data

- **Asset class:** Equities
- **Instruments:** 12 U.S.-listed leveraged and inverse ETFs (LIETFs) tracking the S&P 500 or Nasdaq-100 indices, with leverage factors of 1.25, 2, 3, -2 and -3.
- **Venue:** NYSE and NASDAQ, continuous trading session (9:30 a.m. to 4:00 p.m.)
- **Period:** Trade and quote data from January 1, 2018 to November 1, 2018; 17 trade-war news events collected from China Briefing.
- **Granularity:** Trade- and quote-level data aggregated into 5-, 15-, 30- and 60-minute intervals for each LIETF.

## Features and Measures

- **Abnormal buy-sell ratio.** The difference between the percentage change in cumulative dollar buy value and the percentage change in cumulative dollar sell value for a LIETF between consecutive intervals, used as a predictor of future index returns.
- **Abnormal order imbalance.** The difference between abnormal buy-values and abnormal sell-values, where each abnormal value is the percentage gap between the current interval's buy (or sell) dollar value and the running 75th percentile of buy (or sell) values over the previous 120 intervals.
- **Order imbalance.** Dollar buy-value minus dollar sell-value for a LIETF within an interval, with each trade signed as buyer- or seller-initiated using the Lee and Ready algorithm.
- **Cumulative order imbalance.** The running sum of an LIETF's 5-minute order imbalances from two days before a news event to two days after, used to visualize how imbalances build up around news releases.

## Method

Trades are signed as buyer- or seller-initiated with the Lee and Ready (1991) rule, and dollar buy and sell values are cumulated within 5-, 15-, 30- and 60-minute intervals for each of the 12 LIETFs. From these the authors build the abnormal buy-sell ratio and the abnormal order imbalance, the latter benchmarked against a rolling 75th percentile of past buy/sell values, as their two main predictor variables.

The predictive-ability hypothesis is tested with panel regressions of the interval index return on the lagged abnormal buy-sell ratio or abnormal order imbalance, controlling for Parkinson high-low range volatility and quoted spread, with weekday and LIETF fixed effects. The trend-chasing hypothesis is tested with a panel regression of the current order imbalance on lagged index returns, again with the same controls and fixed effects. A separate descriptive comparison of trading activity in pre-news, news-day and post-news sub-periods, using t-tests, is used to test whether trading activity itself shifts around news.

All three panel regressions are estimated separately for non-inverse and inverse LIETFs and across the four interval lengths, so that predictive power and trend-chasing behavior can be compared across return-forecasting horizons.

## Results

- Average trading activity fell from the pre-news period through the news-day period to the post-news period for both SPX- and NDX-tracking LIETFs, with the differences across sub-periods statistically significant.
- Correlations between the 5-minute cumulative order imbalances of opposite-leverage LIETFs were strongly negative, e.g. 0.92 for SPX +3X vs -3X and 0.91 for NDX +3X vs -3X, indicating investors held consistent views across leveraged and inverse products.
- Panel regressions of index returns on the lagged abnormal buy-sell ratio produced only a few coefficients significant with the theoretically expected sign, giving weak support for informed trading.
- Panel regressions using the abnormal order imbalance found no statistically significant predictive relationship with future returns at the 5-, 15- or 30-minute intervals for either non-inverse or inverse LIETFs; the one significant coefficient, at the 60-minute interval for inverse LIETFs, had the wrong sign for informed trading.
- Order imbalance was positively related to the first two lags of index returns for non-inverse LIETFs and negatively related for inverse LIETFs at the 5-, 15- and 30-minute intervals, all significant at the 1% level, consistent with short-term trend-chasing.
- At the 60-minute interval the sign of this relationship flipped for both non-inverse and inverse LIETFs, consistent with investors seeking reversals rather than continuing trends over longer intraday windows.
- The 12 sampled LIETFs held total assets of $13.67 billion, equal to 49.01% of the entire U.S. LIETF market.

## Limitations

- The sample covers only the initial phase of the 2018 tariff trade war (January-November 2018) and does not extend through later U.S.-China trade tensions, as the authors note.
- The analysis is limited to U.S.-listed LIETFs and does not examine whether similar patterns hold in markets with different regulatory frameworks, which the authors flag as a direction for future research.
- The study cannot separate speculative trading from possible hedging motives because investor-level holdings data are not available.
- Reader note: the news-event sample (17 hand-selected dates) is small, so statistical power for the event-study comparisons around any single news event may be limited.

## Related

- [[concepts/etf-flows|etf flows]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/trade-classification|trade classification]]

## Citation

Petko Stefanov Kalev, Alex Lee (2025). Lietf Trading Behavior During U.S. – China Trade War. Economics - Innovative and Economics Research Journal.

DOI: 10.2478/eoik-2025-0100

Text ingested: `markdown_output/kalev-2025-lietf-trading-behavior-during-u-s.md`, converted from `raw/ofi-event-clock/kalev-2025-lietf-trading-behavior-during-u-s.pdf`.

Coverage of this summary: Read the full markdown file, including introduction, literature review and hypotheses, research methodology and data sources, all results sections (descriptive statistics, forecast ability, trend-chasing), discussion, policy recommendations, limitations, conclusion and the appendix defining abnormal order imbalance.

Known problems with the input: The markdown contains a garbled, reordered sentence describing hypotheses H1-H3 (clauses from different sentences appear interleaved), which was not usable verbatim and was reconstructed only from the surrounding, clearly stated hypothesis definitions; One table caption and one sentence give trade-war news dates through 'Nov. 1, 2028' and 'February 2028' respectively, which appear to be a typo or OCR artifact for 2018 given that the rest of the paper consistently states the sample period as January-November 2018; this discrepancy is noted rather than silently corrected.
<!-- AUTHORED REGION END -->