---
authors:
- Zoltán Eisler
- János Kertész
- Fabrizio Lillo
content_hash: sha256:e720aab9b01187f140fe9c9b95fa6afa97438890ea44ce3feb83cf7c42c97407
created: 2026-09-27 01:47:00+00:00
page_id: sources/eisler-2007-limit-order-book-different-time-scales
page_type: source
related:
- concepts/sampling-clocks
- concepts/limit-order-book
- concepts/bid-ask-spread
- concepts/order-imbalance
- concepts/price-impact
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/stylized-facts
- entities/zoltan-eisler
- entities/fabrizio-lillo
revision_id: 1
schema_version: 2
source_hash: sha256:92d7769f58a9a74eb5872c543d729c16a11e369c890df6b765098b81b49ff2e1
source_path: markdown_output/eisler-2007-limit-order-book-different-time-scales.md
source_type: paper
tags:
- limit-order-book
- market-microstructure
- time-scales
- bid-ask-spread
- order-imbalance
- high-frequency-data
- stylized-facts
- clock-compares
- asset-equity
- added-by-hand
title: The limit order book on different time scales
updated: '2026-09-27T01:47:00Z'
uuid: c4597798-71cc-5ce2-8991-9c8fbc63786b
year: 2007
---

<!-- AUTHORED REGION START -->
# The limit order book on different time scales

## Summary

The paper is a mostly visual, phenomenological comparison of how the limit order book of a single liquid London Stock Exchange stock, GlaxoSmithKline (GSK), looks and behaves as the observation time scale shrinks from months down to individual order book events, using order book snapshots taken through the trading year 2002.

On monthly or longer horizons, prices resemble an ordinary diffusion process with drift, and the bid-ask spread and the asymmetry between the buy and sell sides of the book are negligible relative to typical price moves. On the daily scale, returns become fat-tailed and volatility-clustered, and the shape of the order book fluctuates strongly from day to day around a persistent pattern of a dense region near the spread, a regularly striped pattern of orders every few ticks, and larger orders resting at round price levels. At the level of individual trades, limit order placements and cancellations, price changes are governed by the mechanics of market order execution, order placement inside the spread, and (more rarely) cancellation of the best price, and a liquidity shock that widens the spread relaxes gradually rather than instantly.

No formal statistical model is estimated; the contribution is a catalogue of typical time and price scales (for example intertrade time, the half-life of spread relaxation after a liquidity shock, and the ratio of spread to typical return) at each of the three regimes, together with an argument that no single existing model then available captured behavior across all of them, particularly at the finest, event-driven scale most relevant to high-frequency trading strategies.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Observations are order-book snapshots taken at three physical-time granularities of the same LSE order book for GSK in 2002: one snapshot per trading day (at the 15000th second) across all trading days for the yearly view, several snapshots per day every 1000 to 5000 seconds for the daily view, and a continuous event-by-event reconstruction of trades, limit order placements and cancellations within a short intraday window of about 4000 seconds for the finest view. There is no explicit forecast horizon: the paper is descriptive, comparing how return and order-book statistics change as the sampling interval shrinks rather than predicting future prices.

## Data

- **Asset class:** Equities
- **Instruments:** GlaxoSmithKline (GSK) shares; several other liquid LSE stocks were examined but not shown in detail
- **Venue:** London Stock Exchange, SETS electronic market, continuous auction session
- **Period:** Year 2002 (January 2 to December 31, 2002)
- **Granularity:** Order book snapshots at frequencies ranging from once per day down to individual order-book events (trades, limit order placements, cancellations)

## Features and Measures

- **Bid-ask spread.** The difference between the best ask price and the best bid price at a given time, measured in ticks.
- **Buy/sell order book imbalance.** A measure comparing the total volume of resting buy limit orders to the total volume of resting sell limit orders in the book at a given time.
- **Price impact of an event.** The shift in the best bid or ask price caused by a single market order, limit order placement, or cancellation event.

## Method

The study is observational rather than model-fitting: the authors reconstruct the LSE limit order book for GSK during 2002 at three time granularities (across-day snapshots, daily intraday snapshots every 1000 to 5000 seconds, and event-by-event snapshots within a short intraday window), and compare the resulting price, spread and buy/sell imbalance statistics qualitatively against diffusion, fat-tailed return and long-memory order-flow pictures already discussed in the literature. No formal estimation, hypothesis test or backtest is performed; conclusions rest on visual inspection of order-book heatmaps and simple averages such as mean spread, mean absolute return over different horizons, and mean intertrade time.

## Results

- Averaged over all 252 trading days of 2002, 50% of the total limit order volume in the book sits within a 68 tick range of the best quotes.
- The mean daily absolute return is 23 ticks, compared with a mean bid-ask spread of 1.9 ticks.
- The mean 1-minute and 10-minute absolute returns are 0.9 and 3 ticks respectively, both close to or below the mean spread of 1.9 ticks.
- The average time between consecutive trades for GSK is about 10 seconds.
- The order book shows a persistent striped pattern of orders every few ticks and larger orders resting near round price levels, features that vanish when the book is averaged over a day or a year.
- The imbalance between resting buy and sell limit order volume varies substantially over time but is not directly reflected in subsequent daily returns.
- After a liquidity shock that widens the bid-ask spread, the spread does not revert instantly; relaxation of the spread and associated liquidity fluctuations is gradual.

## Limitations

- Detailed results are shown for a single stock (GSK); the authors state other liquid stocks give qualitatively similar results only where the tick-to-price ratio is small.
- The analysis is qualitative and visual rather than based on a fitted statistical model, so no formal test distinguishes between competing explanations.
- Reader note: the sample is limited to one exchange (London Stock Exchange) and one calendar year (2002).
- Reader note: figures and picture-based evidence (order book heatmaps) could not be inspected directly from the converted text, so some claims rely on the authors' captions rather than the images themselves.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/price-impact|price impact]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/stylized-facts|stylized facts]]
- [[entities/zoltan-eisler|Zoltán Eisler]]
- [[entities/fabrizio-lillo|Fabrizio Lillo]]

## Citation

Zoltán Eisler, János Kertész, Fabrizio Lillo (2007). The limit order book on different time scales.

Text ingested: `markdown_output/eisler-2007-limit-order-book-different-time-scales.md`, converted from `raw/ofi-event-clock/eisler-2007-limit-order-book-different-time-scales.pdf`.

Coverage of this summary: Read the entire converted markdown file, including abstract, introduction, all four time-scale sections, and the conclusion.

Known problems with the input: The document does not print an explicit publication year for this specific paper (only the 2002 data year and a 2007-dated self-citation); year taken from job file metadata (year_hint); Venue (e.g. conference or journal name) is not stated anywhere in the converted text; Several equations and all figures were replaced by placeholder text ('picture... intentionally omitted') during conversion, so the order-imbalance formula and order-book snapshots could not be verified directly, only described from surrounding prose.
<!-- AUTHORED REGION END -->