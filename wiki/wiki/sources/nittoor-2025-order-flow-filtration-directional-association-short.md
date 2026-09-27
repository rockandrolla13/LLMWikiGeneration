---
authors:
- Aditya Nittur Anantha
- Shashi Jain
- Prithwish Maiti
content_hash: sha256:2576270a5536ce015415c9ea9a63590e6b548c92a1c003e64f46e118dabf891b
created: 2026-09-27 01:47:00+00:00
page_id: sources/nittoor-2025-order-flow-filtration-directional-association-short
page_type: source
related:
- concepts/order-flow-imbalance
- concepts/limit-order-book
- concepts/hawkes-processes
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/order-flow
- concepts/trade-classification
- entities/aditya-nittur-anantha
- entities/shashi-jain
revision_id: 1
schema_version: 2
source_hash: sha256:9ffb020fcc4799618c2d2094deef673b31f31e6a5cd052970c3455d20bbfa58f
source_path: markdown_output/nittoor-2025-order-flow-filtration-directional-association-short.md
source_type: paper
tags:
- order-flow-filtration
- order-book-imbalance
- hawkes-processes
- market-microstructure
- nse-india
- fleeting-orders
- high-frequency-trading
- order-to-trade-ratio
- clock-calendar
- asset-futures
- harvest-core
title: Order-Flow Filtration and Directional Association with Short-Horizon Returns
updated: '2026-09-27T01:47:00Z'
uuid: 077d1a25-c10d-55ad-84c4-87e764d76dea
year: 2025
---

<!-- AUTHORED REGION START -->
# Order-Flow Filtration and Directional Association with Short-Horizon Returns

## Summary

The paper asks whether removing ephemeral, fleeting order activity from the order flow strengthens the association between order book imbalance (OBI) and returns a few seconds to a couple of minutes ahead, in a market where the exchange already penalises noisy order flow. It uses tick-by-tick data for BANKNIFTY index futures on the National Stock Exchange of India and proposes a three-step diagnostic ladder rather than a forecasting model: contemporaneous Pearson correlation between OBI and realised returns, a regime-based correlation and regression score after discretising OBI into nine bins and returns into three bins, and a multivariate Hawkes process whose fitted excitation kernels measure how strongly imbalance-regime events causally excite future return-regime events. Three structural filters are defined at the order level: an order-lifetime filter, a modification-count filter, and a modification-timing filter, each applied either directly to the reconstructed limit order book or to the parent orders behind executed trades.

The main finding is asymmetric. When the filters are applied to the standing limit order book, all three diagnostics move only slightly and inconsistently relative to the unfiltered benchmark, across three sample trading days spanning the early, middle and late part of a monthly futures expiry cycle. When the same filters are instead applied to the parent orders of executed trades, and imbalance is rebuilt from the resulting signed trade flow, the Hawkes-based cross-excitation from imbalance regimes to return regimes rises substantially and consistently on every sample day.

The authors read this as evidence that not all trades contribute equally to price formation: trades tied to very short-lived or heavily revised parent orders carry comparatively little directional information, while trades that survive simple structural filters carry a clearer causal imprint on subsequent returns. The paper is explicitly diagnostic rather than predictive or execution-oriented, and it is framed as a tool for evaluating order-based surveillance regulation (such as India's 'Persistent Noise Creator' rules) rather than as a trading signal in its own right.

What is new is the combination of a lifecycle-based filtration scheme (lifetime, modification count, modification timing) with a layered diagnostic ladder that moves from linear correlation, to discretised regime association, to Hawkes excitation norms, and the finding that filtration effects are largely invisible in correlation and regime diagnostics but become clearly visible only once Hawkes kernel norms are computed on trade-linked, parent-order-filtered imbalance.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Order book imbalance is computed from event counts inside a fixed backward-looking evaluation window of length h = 10 seconds ending at anchor time tau; anchor times are spaced every 15 seconds through the continuous trading session from 09:20 to 15:25. The realised return is computed over a subsequent forecast window of length 1 second, using the first and last signed trade prices in that window. A separate, event-time layer promotes discretised OBI and return regimes to point-process events and fits a multivariate Hawkes process to them, so causal excitation is additionally analysed in event time rather than calendar time.

## Data

- **Asset class:** Futures
- **Instruments:** BANKNIFTY index futures (January 2023 expiry); selected NSE equities are also mentioned as a data source but the reported results are for BANKNIFTY futures
- **Venue:** National Stock Exchange of India (NSE)
- **Period:** Three trading days: 2 January, 13 January and 23 January 2023, chosen to span the early, middle and late part of the January 2023 futures expiry cycle
- **Granularity:** Event-driven tick data recording new order submission, modification, cancellation and trade events, each tagged with an order ID, timestamp, side, price and quantity; only ticks that change the top-5 levels of the book are recorded

## Features and Measures

- **Order Book Imbalance (OBI).** A normalised measure of net directional pressure built from counts of buy- and sell-side order events inside a backward-looking evaluation window, using the total number of orders in the window as the denominator.
- **Order Book Imbalance by Trades (OBI(T)).** An imbalance measure computed only from signed executed trades within a window, using a tick-based trade-sign classification, so it is unaffected by cancelled or unexecuted orders.
- **Order Lifetime Filter.** Removes events tied to orders whose total resting time in the book is below a fixed threshold, set to 100 milliseconds in the experiments.
- **Modification Count Filter.** Removes events tied to orders whose number of modifications exceeds a fixed threshold, set to 3 in the experiments.
- **Modification Time Filter.** Removes events tied to orders whose last two modifications occur closer together in time than a fixed threshold, set to 50 milliseconds in the experiments.
- **Hawkes Excitation Norm Score.** A scalar built from the integrated kernel matrix of a fitted multivariate Hawkes process, summarising how strongly OBI-regime events excite future return-regime events of matching sign.

## Method

The authors reconstruct the limit order book from raw tick data under an unfiltered baseline and under each of three structural filters, applied either to all standing orders or only to the parent orders of executed trades, and recompute OBI and OBI(T) on each variant. They evaluate association with short-horizon returns using a three-layer diagnostic ladder: first, rolling Pearson correlation between OBI and realised returns at multiple horizons; second, discretisation of OBI into nine regimes and returns into three regimes, with a directional, sign-weighted correlation score and an OLS regression-based R-squared score, both recomputed after removing autocorrelation via univariate ARMA residuals and across a grid of positive lags; third, a multivariate Hawkes process with a sum-of-exponentials kernel fitted to the regime-labelled counting processes, from which an integrated excitation matrix and a directionally-weighted Hawkes excitation norm are extracted.

All scoring functionals are computed identically across filtration schemes, using the same evaluation windows and normalisation, so that differences in scores can be attributed to the filtration itself rather than to reparameterisation. For the trade-based imbalance OBI(T), the authors focus on the Hawkes-based diagnostic only, since contemporaneous correlation between executed-trade imbalance and same-window returns is mechanically strong and considered uninformative for the comparison.

## Results

- On the most active sample day (23 January 2023), the unfiltered book reconstruction contained 83,547,534 ticks; the lifetime filter removed 5,928,152 order identifiers leaving 51,023,701 ticks, the modification-count filter removed 5,416,670 order identifiers leaving 72,228,161 ticks, and the modification-time filter removed only 168,058 order identifiers yet still left just 47,531,611 ticks.
- For imbalance computed from the standing book, the average Pearson correlation score with subsequent returns was 0.01018 unfiltered, rising only to 0.01133 under the modification-time filter and falling to 0.00826 under the modification-count filter, with the lifetime filter leaving it essentially unchanged.
- Book-based OBI showed no consistent improvement in directional association with returns under any of the three structural filters, across the correlation, regime-based and Hawkes-based diagnostics, and the ranking among filters varied across days.
- For trade-based imbalance, filtering the parent orders behind executed trades produced large, systematic gains in Hawkes excitation from imbalance regimes to return regimes on all three sample days.
- On 2 January 2023, the lifetime filter raised the Hawkes excitation score for trade-based imbalance from 10.9933 unfiltered to 15.2172.
- On 13 January 2023, the lifetime filter nearly doubled the trade-based excitation score, from 8.3639 unfiltered to 15.8630.
- On 23 January 2023, the day with the highest market activity in the sample, the modification-time filter raised the trade-based excitation score from 11.5868 unfiltered to 24.7352.
- The authors conclude that not all trades contribute equally to price formation: trades linked to short-lived or heavily revised parent orders carry a weaker directional imprint than trades that survive structural filtering, even though the same filters do little for book-based OBI.

## Limitations

- The empirical analysis covers only three trading days for a single instrument (BANKNIFTY futures), which the authors describe as a restricted sample.
- The study is explicitly diagnostic and does not specify or backtest a forecasting or execution strategy built on the filtered signals.
- The setting is an emerging-market futures contract already subject to order-based surveillance rules, which may limit how the findings generalise to other markets or regulatory regimes.
- Reader note: with only three sample days, the reported filter rankings and excitation scores could be sensitive to day-specific volatility and activity levels, as the paper itself notes that filter rankings vary across days for book-based OBI.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-flow|order flow]]
- [[concepts/trade-classification|trade classification]]
- [[entities/aditya-nittur-anantha|Aditya Nittur Anantha]]
- [[entities/shashi-jain|Shashi Jain]]

## Citation

Aditya Nittur Anantha, Shashi Jain, Prithwish Maiti (2025). Order-Flow Filtration and Directional Association with Short-Horizon Returns.

DOI: 10.2139/ssrn.5934441

Text ingested: `markdown_output/nittoor-2025-order-flow-filtration-directional-association-short.md`, converted from `raw/ofi-event-clock/nittoor-2025-order-flow-filtration-directional-association-short.pdf`.

Coverage of this summary: Read the full markdown file, including abstract, all main sections, tables and the appendix with detailed per-day, per-filter, per-horizon scores.

Known problems with the input: Most mathematical definitions and formulas are rendered as omitted images in the markdown conversion ('picture... intentionally omitted'), so exact functional forms of some quantities could not be verified from the text alone, though the surrounding prose, tables and reported numbers remain legible and were used directly.
<!-- AUTHORED REGION END -->