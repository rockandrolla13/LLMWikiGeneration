---
authors:
- Francesco Corradi
- Andrea Zaccaria
- Luciano Pietronero
content_hash: sha256:b157cd4e6a4675d711614bd2cfe254f3c2f8011d64b71adab4ca7a89cf61d6dd
created: 2026-09-27 01:47:00+00:00
page_id: sources/corradi-2015-liquidity-crises-different-time-scales
page_type: source
related:
- concepts/limit-order-book
- concepts/order-flow
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/liquidity-risk
- concepts/market-microstructure
- concepts/price-impact
- concepts/stylized-facts
- concepts/queue-imbalance
revision_id: 1
schema_version: 2
source_hash: sha256:142478de80b9cbd77dcc96cce47c198e4a77130735df433b6ede386fca9c3fb2
source_path: markdown_output/corradi-2015-liquidity-crises-different-time-scales.md
source_type: paper
tags:
- limit-order-book
- liquidity-imbalance
- order-flow-imbalance
- price-jumps
- market-microstructure
- resilience
- high-frequency-data
- equities
- clock-calendar
- asset-equity
- harvest-relevant
title: Liquidity crises on different time scales
updated: '2026-09-27T01:47:00Z'
uuid: 6009fbf3-0ec7-5de8-93dd-d0a4aa76c821
year: 2018
---

<!-- AUTHORED REGION START -->
# Liquidity crises on different time scales

## Summary

The paper asks what state or behavior of the limit order book precedes large price fluctuations, and whether the answer depends on the time scale considered. Using a year of tick-by-tick limit order book data for stocks on the London Stock Exchange (results shown for AZN), the authors first define large price events with a combined absolute-and-relative return filter over fixed time windows, then study the flow of market orders, limit orders and cancellations around those events at a 15-minute scale, and the static shape of the order book just before events at a 30-second scale. At the 15-minute scale, they find that large price moves coincide with a breakdown of the normal compensation mechanism in which incoming market orders are usually matched by an offsetting flow of new limit orders: during large events, the side of the book under pressure gets an excess of market orders that is not met by enough new limit orders, so the market loses resilience. At the 30-second scale, instead, the key factor is the static depth of the book: the side about to break down already shows thinner posted volume near the best price before the event, even when the incoming market-order flow is not unusually large. The authors introduce an exponential-liquidity measure of book depth on each side and a liquidity-imbalance measure comparing the two sides, and show both are correlated with the sign and magnitude of the next price move. What is new is the explicit separation of two liquidity mechanisms, resilience versus depth/breadth, by time scale, and the introduction of the liquidity-imbalance measure as a simple, book-based predictor of the direction of the next return.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Large events and their surrounding order flow are studied in fixed wall-clock windows of two different sizes: 15 minutes for the order-flow/resilience analysis and 30 seconds for the static order-book-depletion analysis. Within the 15-minute windows the paper tracks the relative volumes of market orders, limit orders and cancellations in 30-second sub-bins; for the 30-second analysis the state of the book is measured at the last order-book operation before the start of the window, and the following 30-second return is the prediction target.

## Data

- **Asset class:** Equities
- **Instruments:** AZN (AstraZeneca); the same analysis was also run on BP, RBS and VOD with similar results, but only AZN's results are shown
- **Venue:** London Stock Exchange
- **Period:** whole year 2002
- **Granularity:** Tick-by-tick limit order book operations (limit orders, market orders, cancellations), aggregated into fixed windows of 15 minutes or 30 seconds; the first 30 minutes of each trading day are discarded.

## Features and Measures

- **exponential liquidity.** A measure of order-book depth on one side, computed as an exponentially weighted average of the volume posted at each price tick within a maximum distance from the best quote, with a decay parameter that sets how quickly weight falls off away from the best price.
- **liquidity imbalance (L_imb).** The normalized difference between the ask-side and bid-side exponential liquidity, measured at the start of a time window, intended to indicate whether the book's state favors an upward or downward next return.
- **relative order flow (MO, LO, cancellation shares).** The volume of market orders, limit orders and cancellations on one side of the book expressed as a share of their sum in a given sub-interval, tracked before and during large events to see whether the usual balance between order types holds up.

## Method

Large price events are identified with a combined filter that requires both an absolute return above a threshold and a return above a multiple of the local average volatility, applied over fixed time windows (15 minutes with a 0.5% threshold and 3-sigma multiple, or 30 seconds with a 0.3% threshold and 6-sigma multiple), discarding events preceded by another large event too soon before. For the 15-minute analysis, the paper computes relative shares of market orders, limit orders and cancellations on each side of the book before and during events, and fits a linear relationship between the incoming market-order volume and the responding limit-order volume to gauge the book's resilience. For the 30-second analysis, the paper computes the exponential-liquidity measure on each side of the book at the start of the window, fits a power-law relationship between subsequent return magnitude and ask-side liquidity, and separately studies the liquidity-imbalance measure by plotting the average subsequent return, and the frequency of positive, negative and zero returns, against it.

## Results

- The combined absolute-and-relative event filter selects 332 positive and 362 negative large events for AZN over the one-year sample.
- During large 15-minute events, the side of the book under pressure sees its limit-order and cancellation flow rise to roughly three times, and its market-order flow rise up to about five times, their respective annual averages.
- At the 15-minute scale, the slope linking incoming market-order volume to responding limit-order volume on the pressured side is markedly lower than the average slope during large positive events, and higher than average on the pressing side, showing a breakdown of the usual order-flow compensation.
- At the 30-second scale, the side of the book about to break down already shows visibly lower posted volume near the best price before the event, even though the incoming market-order flow is not much larger than average just before the event.
- Fitting the relationship between subsequent return magnitude and ask-side exponential liquidity with a power law gives K = 0.2944 +/- 0.0028 and alpha = 0.2800 +/- 0.0041 for positive events, with compatible parameter values found for negative events.
- The goodness-of-fit of this power-law relationship, measured by R-squared, is highest for an exponential-liquidity decay parameter around 5-6 ticks from the best price.
- Higher values of the liquidity-imbalance measure are associated with more frequent positive returns; at a liquidity imbalance of about 0.8, positive returns occur more than twice as often as negative returns.

## Limitations

- Detailed results are shown only for one stock, AZN; results for BP, RBS and VOD are stated to be similar but are not shown.
- The authors state they cannot yet establish a lagged, causal relationship between order-flow imbalance and price jumps at the 15-minute scale, since order flow and the return are measured over the same window.
- The predictive power of the liquidity-imbalance measure for future returns is not tested on a separate training/test split; the authors state this is left for future work.
- Reader note: the sample covers a single calendar year (2002) for a small set of large-cap London Stock Exchange stocks, which limits how far the findings generalize to other markets or periods.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/liquidity-risk|liquidity risk]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/price-impact|price impact]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/queue-imbalance|Queue Imbalance]]

## Citation

Francesco Corradi, Andrea Zaccaria, Luciano Pietronero (2018). Liquidity crises on different time scales.

DOI: 10.1103/physreve.92.062802

Text ingested: `markdown_output/corradi-2015-liquidity-crises-different-time-scales.md`, converted from `raw/ofi-event-clock/corradi-2015-liquidity-crises-different-time-scales.pdf`.

Coverage of this summary: Read the entire markdown file, including the abstract, introduction and order-book description, the order-flow/resilience analysis at the 15-minute scale, the static-depletion and exponential-liquidity analysis at the 30-second scale, the liquidity-imbalance section, and the conclusions.

Known problems with the input: The document itself is dated "September 27, 2018" on its title page; this appears to be a later revision timestamp rather than the original publication year implied by the job's year_hint of 2015, so the year field uses the date printed on this version (2018) per the extraction instructions; Most figures are rendered as omitted pictures with only captions and axis text recovered, so exact plotted values beyond what is stated in the prose could not be checked.
<!-- AUTHORED REGION END -->