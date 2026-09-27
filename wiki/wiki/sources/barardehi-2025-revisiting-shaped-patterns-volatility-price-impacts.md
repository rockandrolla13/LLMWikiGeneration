---
authors:
- Yashar H. Barardehi
- Dan Bernhardt
content_hash: sha256:4bad922cb04cf874368127918dee9cbc76ddc5a354e84cc0d0ce08bb82aac606
created: 2026-09-27 01:47:00+00:00
page_id: sources/barardehi-2025-revisiting-shaped-patterns-volatility-price-impacts
page_type: source
publication_venue: Journal of Financial Markets
related:
- concepts/sampling-clocks
- concepts/market-microstructure
- concepts/price-impact
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/informed-trading
- concepts/trade-classification
- concepts/stylized-facts
- concepts/autocorrelation-time-series
- concepts/trade-clock
- concepts/kyles-lambda
revision_id: 1
schema_version: 2
source_hash: sha256:8006de13dcfe8796a7f6c93693d99a57fdf4e5aa95646a32df189c09f72bfc47
source_path: markdown_output/barardehi-2025-revisiting-shaped-patterns-volatility-price-impacts.md
source_type: paper
tags:
- trade-time
- calendar-time
- market-microstructure
- kyles-lambda
- intraday-patterns
- over-aggregation
- liquidity-provision
- price-impact
- clock-compares
- asset-equity
- harvest-core
title: 'Revisiting the ∪-shaped patterns in volatility and price impacts: Novel results
  using trade-time estimates'
updated: '2026-09-27T01:47:00Z'
uuid: 3e0645f3-804d-57bb-bde8-75c4a8e5049d
year: 2025
---

<!-- AUTHORED REGION START -->
# Revisiting the ∪-shaped patterns in volatility and price impacts: Novel results using trade-time estimates

## Summary

The paper asks whether the well-known intraday U-shaped patterns in volatility and Kyle's lambda (the sensitivity of prices to trade imbalances) are real features of trading, or artifacts of the standard practice of measuring them over fixed calendar-time intervals such as 15 minutes. It follows a companion paper (Barardehi, Bernhardt and Davies, 2019, referred to as BBD) in constructing trade-time intervals, or trade sequences: runs of consecutive transactions that accumulate to a target dollar volume set per stock and month, priced at the prior day's close so that current price moves cannot affect how a sequence is defined.

Using NYSE common-stock trades and NBBO quotes from 2009 to 2017, the authors estimate time-of-day regressions of return volatility and Kyle's lambda separately in calendar time and trade time, controlling for stock and date fixed effects. In calendar time they reproduce the familiar U-shaped patterns, but in trade time both volatility and Kyle's lambda fall over most of the trading day. They attribute the difference to over-aggregation: fixed time windows lump together more individual trade-time intervals when trading is heaviest, near the open and especially the close, which mechanically inflates calendar-time price-impact and volatility estimates in those windows.

The paper also decomposes trade imbalances into expected and unexpected components and studies how each is priced across trading-activity levels. In active markets, returns persist and expected imbalances are priced positively, while in quiet markets returns revert and expected imbalances are priced negatively; unexpected imbalances are priced more strongly when they share the sign of the expected component. The authors interpret this as evidence of imperfectly competitive, inventory-constrained liquidity provision rather than the perfectly competitive, martingale-pricing foundation of classical microstructure models, and support the over-aggregation explanation with both a simulated data-generating-process model and a set of robustness checks such as excluding trades near the close, a fixed-number-of-transactions design, and 5-minute calendar windows.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Trade-time intervals, called trade sequences, are runs of consecutive transactions that accumulate a stock- and month-specific target dollar volume, V = 0.025% of prior month-end market cap plus $80,000, priced at the prior day's closing price; this gives a median trade time of about 12 minutes overall and about 16 minutes for the smallest-cap tercile. Calendar-time intervals use fixed 15-minute (and, as a robustness check, 5-minute) wall-clock windows. Both schemes assign intervals to 30-minute time-of-day windows and estimate volatility and Kyle's lambda from the return and net order flow realized within that same interval, so the horizon is the interval itself rather than a forward-looking forecast. A separate robustness design instead fixes the number of transactions per interval at 60 to strip out the effect of interval length.

## Data

- **Asset class:** Equities
- **Instruments:** NYSE-listed common stocks with a prior year-end closing price of at least $1
- **Venue:** NYSE (consolidated trades and quotes via Daily TAQ)
- **Period:** January 1, 2009 to December 31, 2017 (a few robustness figures restrict the sample to 2009-2012)
- **Granularity:** Tick-by-tick trade prints and millisecond-frequency NBBO quotes, aggregated into 15-minute calendar windows or trade-time sequences

## Features and Measures

- **trade sequence / trade time (dur).** A run of consecutive transactions whose cumulative dollar volume, priced at the prior day's close, first reaches a stock-month-specific target; its duration in minutes is the trade time, with a shorter duration indicating higher trading activity.
- **net order flow (NOF).** A volume-neutral signed measure built from the proportion of buyer-initiated volume BP, defined as sign(BP-0.5) times the square root of |BP-0.5|, used as the independent variable in Kyle's-lambda regressions.
- **Kyle's lambda (time-of-day).** The OLS-estimated sensitivity of trade- or calendar-time midpoint returns to net order flow, estimated separately by 30-minute time-of-day window and stock-size tercile with stock and date fixed effects and double-clustered standard errors.
- **expected vs. unexpected trade-imbalance decomposition.** Trade imbalance is regressed on its own lag (an AR(1)) by time-of-day and activity level; the fitted values are the expected component and the residuals the unexpected component, each then used to re-estimate Kyle's lambda separately.

## Method

The authors estimate time-of-day fixed-effects regressions of volatility and Kyle's lambda in both trade time and calendar time, using OLS with stock and date fixed effects and standard errors double-clustered at both levels, run separately by market-cap tercile. Robustness checks re-run the analysis after excluding trades near the close, using a fixed number of 60 consecutive transactions per interval instead of a fixed time or dollar-volume window, halving or rescaling the target dollar volume, and shortening calendar windows to 5 minutes. To connect the empirical over-aggregation story to a data-generating process, an appendix develops and simulates a stylized Markov-switching liquidity model in which a price-impact parameter switches between low- and high-liquidity states and order sizes respond to the prevailing liquidity state, then compares calendar-time and trade-time estimates computed from the same simulated data.

## Results

- Trade-time estimates of both return volatility and Kyle's lambda fall by over 50% from the market open to the close, rather than following the U-shaped pattern found in calendar time.
- Calendar-time volatility and Kyle's-lambda estimates exceed their trade-time counterparts by up to 30% near the open and by up to 50% near the close.
- The base trade-time target dollar volume is V = 0.025% of prior month-end market cap plus $80,000, giving a median trade time of about 12 minutes overall and about 16 minutes for the smallest market-cap tercile.
- Findings are qualitatively unchanged when trades in the first or last 5, 10 or 15 minutes of the day are excluded, when the target dollar volume is rescaled, when a 5-minute rather than 15-minute calendar window is used, and across market-cap terciles.
- The autocorrelation of trade imbalances in trade time rises from 0.15 in the lowest trading-activity quartile to 0.34 in the highest quartile.
- Using a fixed 60 transactions per interval, instead of a fixed time or dollar-volume window, to control for over-aggregation makes both calendar-time and trade-time patterns resemble the baseline trade-time pattern.
- In the paper's simulated data-generating process, the average trade-time-estimated Kyle's lambda declines from 0.034 to 0.027 between the lowest and highest trading-activity terciles, matching the model's built-in liquidity-activity relationship, whereas calendar-time estimates move in the opposite direction.

## Limitations

- Sample is restricted to NYSE-listed common stocks from 2009-2017; equities only, no other asset classes.
- Authors state they do not have permission to share the underlying data.
- Reader note: trading direction is inferred via NBBO-based Lee-Ready classification rather than observed directly, so results depend on that classification's accuracy.
- Reader note: Kyle's lambda is a linear-regression estimate, not a structurally identified parameter, so the interpretation of magnitudes is conditional on that functional form.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/price-impact|price impact]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/trade-clock|Trade Clock]]
- [[concepts/kyles-lambda|Kyle's Lambda]]

## Citation

Yashar H. Barardehi, Dan Bernhardt (2025). Revisiting the ∪-shaped patterns in volatility and price impacts: Novel results using trade-time estimates. Journal of Financial Markets.

DOI: 10.1016/j.finmar.2025.100971

Text ingested: `markdown_output/barardehi-2025-revisiting-shaped-patterns-volatility-price-impacts.md`, converted from `raw/ofi-event-clock/barardehi-2025-revisiting-shaped-patterns-volatility-price-impacts.pdf`.

Coverage of this summary: Read the complete paper: introduction, Section 2 data and methodology, Sections 3-5 results and discussion, Section 6 conclusion, the CRediT statement, Appendix A stylized simulation, Appendix B five-minute robustness check, and the reference list.

Known problems with the input: The markdown conversion replaces most equations and figures with picture-omitted placeholders, so exact equation forms could not be verified from text alone; only the prose description of variables and the numbers stated outside the equations were used.
<!-- AUTHORED REGION END -->