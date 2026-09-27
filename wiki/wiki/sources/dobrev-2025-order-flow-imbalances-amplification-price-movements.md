---
authors:
- Dobrislav Dobrev
- Edith Liu
- Joon Kim
- Marius Rodriguez
content_hash: sha256:93d87533d75ba5284b0cfa89f31ec919183d57c63a26b13552581bc54b18cad6
created: 2026-09-27 01:47:00+00:00
page_id: sources/dobrev-2025-order-flow-imbalances-amplification-price-movements
page_type: source
publication_venue: FEDS Notes, Board of Governors of the Federal Reserve System
related:
- concepts/order-flow-imbalance
- concepts/order-flow
- concepts/price-impact
- concepts/liquidity-risk
- concepts/bond-liquidity
- concepts/high-frequency-data
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:f9dbe47f28fb354494ea769a090dc1f9054dde0ff38dca1fe876e86c253e359c
source_path: markdown_output/dobrev-2025-order-flow-imbalances-amplification-price-movements.md
source_type: article
tags:
- treasury-market
- order-flow-imbalance
- market-liquidity
- price-impact
- high-frequency
- tariff-shock-2025
- market-depth
- clock-calendar
- asset-bonds-rates
- harvest-relevant
title: 'Order Flow Imbalances and Amplification of Price Movements: Evidence from
  U.S. Treasury Markets'
updated: '2026-09-27T01:47:00Z'
uuid: 7cd3525c-3a00-564e-8f74-190fe6bb036a
year: 2025
---

<!-- AUTHORED REGION START -->
# Order Flow Imbalances and Amplification of Price Movements: Evidence from U.S. Treasury Markets

## Summary

The note argues that monitoring large directional order flow, not just volatility or trading volume alone, is important for understanding notable Treasury price moves when liquidity is severely strained. It describes a liquidity mismatch mechanism in which market turbulence causes liquidity demand to surge while supply evaporates, because rising volatility prompts market makers to cut risk exposure at the same time other investors are trying to rebalance portfolios.

The authors ground this argument in the Treasury market turbulence of early April 2025 around the announced reciprocal tariffs, comparing two intraday event windows: April 7, when a rumored tariff pause and its swift denial triggered a sharp swing, and April 9, when an actual 90-day tariff pause was announced alongside a 10-year Treasury auction. Both days saw comparable declines in liquidity supply (market depth) but differed sharply in the direction and persistence of buy-versus-sell demand.

Despite similarly sized intraday volume spikes on both days, comparable in scale to the spike seen during the 2014 Treasury flash rally, April 7 produced a large, sustained, one-directional cumulative order-flow imbalance in favor of selling that coincided with a much bigger price move. April 9's imbalance, by contrast, was smaller, swung in both directions, and was short-lived, with a correspondingly smaller price reaction. Realized volatility on both days was unusually high even after accounting for the historically low market depth.

The note's contribution is descriptive and illustrative rather than a formal statistical model: it shows that looking only at daily volumes and price changes can mask important intraday differences in liquidity demand and supply, and that tracking intraday order-flow imbalance alongside market depth gives a fuller, more timely picture of when strained liquidity is amplifying price moves. The authors position this as useful both for day-to-day market surveillance and for broader monitoring of macro-financial vulnerabilities tied to liquidity and volatility.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Trading volumes for the 10-year Treasury note and futures are aggregated into 5-minute wall-clock bars, while yields are sampled at 5-second intervals during main US trading hours. Cumulative trading imbalance (buyer-initiated minus seller-initiated volume) is tracked continuously through two specific intraday event windows on April 7 and April 9, 2025. There is no formal predictive horizon; the note is a descriptive, event-study comparison of liquidity, volume and price behavior across two days rather than a forecasting exercise.

## Data

- **Asset class:** Bonds and rates
- **Instruments:** 10-year (benchmark, on-the-run) Treasury note and 10-year Treasury futures contract, with references to broader segments of the US Treasury cash and futures markets
- **Venue:** Largest and most liquid electronic trading platforms for benchmark Treasury securities and Treasury futures contracts; data sourced from Bloomberg, the Repo Inter Dealer Broker community, LSEG, and Datascope Tick History
- **Period:** Long-run historical context uses business days from January 4, 2010 to September 29, 2025, including a Pandemic Crisis period (February 27 to April 1, 2020) and a Bank Stresses period (March 8 to April 1, 2023). The core event analysis covers March 31 to April 16, 2025, focused on April 7 and April 9, 2025.
- **Granularity:** Intraday: yields sampled at 5-second intervals, volumes aggregated into 5-minute bars over 7am-5pm ET trading hours, and cumulative order-flow imbalance tracked continuously within each event window

## Features and Measures

- **market depth.** the average volume of best-price quotes on the buy and sell sides of the market, used as the note's standard measure of liquidity supply
- **realized volatility.** the sum of squared five-minute intraday returns during main US trading hours for the benchmark 10-year Treasury note, used to gauge price volatility and compare it against market depth
- **cumulative trading imbalance.** the running difference between buyer-initiated and seller-initiated trading volume, plotted through an intraday event window to show the direction and persistence of liquidity demand

## Method

The note is a descriptive event study rather than a formal econometric model. It compares realized volatility (sum of squared five-minute returns) against market depth over a long historical window to place the April 2025 episode in context, then zooms into two specific intraday windows on April 7 and April 9, 2025 that had comparable declines in market depth. Within each window it plots intraday price against 5-minute trading volume and against cumulative buyer-minus-seller trading imbalance, and compares the two days visually and in magnitude rather than through regression or hypothesis testing.

## Results

- Cumulative trading imbalance on April 7, 2025 surged to over $2 billion in one-sided sell pressure shortly after 10:10 am, before gradually dissipating over the next 10 minutes as a rumored tariff pause was denied.
- On April 9, 2025, trading imbalance around 1:20 pm fluctuated in both directions, with short-lived spikes not exceeding $1 billion.
- Intraday 10-year Treasury futures volume spikes around 10:10-10:20 am on April 7 and 1:20-1:30 pm on April 9 were each comparable in scale to the volume spike observed during the 2014 Treasury flash rally.
- Despite comparable volume spikes on both days, price movements around the April 9 spike were markedly smaller than those around the April 7 spike.
- Realized volatility on both April 7 and April 9, 2025 was unusually high even after controlling for the historically low market depth observed on those days.
- A similar volume surge on March 31, 2025 tied to month-end rebalancing did not trigger a large price move, reflecting normal market depth on that day.

## Limitations

- The analysis covers only two specific intraday event windows within a single week in April 2025.
- The note is descriptive and comparative rather than a formal regression or statistical model.
- Risk-adjusted volume comparisons across instruments and price-impact measures for the two days are mentioned but not shown in the note.
- Reader note: conclusions rest on visual comparison of two days rather than a broader sample of stress episodes.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-flow|order flow]]
- [[concepts/price-impact|price impact]]
- [[concepts/liquidity-risk|liquidity risk]]
- [[concepts/bond-liquidity|bond liquidity]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Dobrislav Dobrev, Edith Liu, Joon Kim, Marius Rodriguez (2025). Order Flow Imbalances and Amplification of Price Movements: Evidence from U.S. Treasury Markets. FEDS Notes, Board of Governors of the Federal Reserve System.

DOI: 10.17016/2380-7172.3954

Text ingested: `markdown_output/dobrev-2025-order-flow-imbalances-amplification-price-movements.md`, converted from `raw/ofi-event-clock/dobrev-2025-order-flow-imbalances-amplification-price-movements.pdf`.

Coverage of this summary: Read the entire FEDS note in full, including the background section, all figures' captions and notes, footnotes, and the reference list.

Known problems with the input: Markdown includes repeated webpage header/footer boilerplate (page title, navigation links, and a browser print timestamp of 9/27/26) left over from converting the Fed's website page; this was treated as non-content and ignored.
<!-- AUTHORED REGION END -->