---
authors:
- Myles Sjogren
- Timothy DeLise
content_hash: sha256:da87e99f30ba3d0e294d6afb307565eb4a6b5538ed1956bac41bbae8e3f1d42d
created: 2026-09-27 01:47:00+00:00
page_id: sources/sjogren-2021-general-compound-hawkes-processes-mid-price
page_type: source
related:
- concepts/intrinsic-time
- concepts/hawkes-processes
- concepts/limit-order-book
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/stylized-facts
- concepts/jump-clustering
revision_id: 1
schema_version: 2
source_hash: sha256:77106e5439bf7631a0d22346f235d304cef3a190a61e401498fc252e472aff2a
source_path: markdown_output/sjogren-2021-general-compound-hawkes-processes-mid-price.md
source_type: paper
tags:
- hawkes-process
- limit-order-book
- mid-price-prediction
- point-process
- futures
- equities
- volatility-forecasting
- walk-forward-validation
- clock-intrinsic
- asset-multi
- harvest-relevant
title: General Compound Hawkes Processes for Mid-Price Prediction
updated: '2026-09-27T01:47:00Z'
uuid: f2728349-3dc6-5cd6-a1ae-42edd1f5237f
year: 2021
---

<!-- AUTHORED REGION START -->
# General Compound Hawkes Processes for Mid-Price Prediction

## Summary

The paper asks how well the General Compound Hawkes Process (GCHP) family, originally built to model insurance risk and then adapted to limit order books, transfers to new markets and to the practical task of predicting the mid-price. A GCHP pairs a Hawkes process, which governs the timing of mid-price-change events and lets one event raise the likelihood of the next, with a Markov chain that governs the size and direction of each change; the paper studies four variants that differ only in how many Markov states are used to describe possible move sizes, from a simple fixed up/down model up to an n-state model built from quantiles of historical moves.

The authors first confirm, on proprietary sugar futures order-book data and on public stock order-book data (including AMZN, FB, MSFT and other names), several empirical patterns that justify a Hawkes-based approach: mid-price change events arrive in clusters, their inter-arrival times are not exponentially distributed (Weibull or Gamma fits tend to win instead), and the number of price changes in a window remains correlated with the number in earlier windows for a noticeable period. They then fit each of the four GCHP variants day by day, judging fit quality by comparing the model's theoretical diffusive-limit volatility to the empirical volatility of the data, and use the best-fitting model per window for prediction.

Two prediction methods are tested: a closed-form approach that plugs the fitted Hawkes and Markov-chain parameters into a diffusive-limit formula to produce a single numeric mid-price forecast, and a simulation-based approach that generates many simulated Hawkes/Markov-chain price paths and averages their endpoints. Directional (three-class up/stationary/down) prediction accuracy was generally only modestly above chance and highly sensitive to the choice of threshold, training/testing window length, and number of simulated paths, whereas a coarser two-class volatility label (large move versus small move) was predicted noticeably more reliably across both futures and stock data.

What is new is a systematic side-by-side test of the different GCHP state-count variants on two very different asset classes with an explicit walk-forward, same-day fitting and prediction protocol, plus a worked appendix showing that under this modeling setup the sign of the model's directional forecast depends only on the steady-state probabilities of the fitted Markov chain and not directly on the Hawkes process parameters.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

The raw feed is a full limit order book event log (every update to the top ten price/volume levels on each side produces a new row), but the compound Hawkes model is fit to a derived sub-series of discrete mid-price-change events, each an up or down move of a fixed tick size or one of several quantile-based move sizes for the higher-state variants. Forecasts use same-day walk-forward train/test windows (for example a 3 hour training window followed by a 2 hour test window for sugar futures, or roughly one hour and half-hour windows for individual stocks) that are stepped forward through the trading day, with the prediction target being the mid-price, or its direction/volatility class, a fixed time past the end of each training window.

## Data

- **Asset class:** Several asset classes
- **Instruments:** Sugar (SB) futures; stocks including AMZN, FB, MSFT and others, with per-stock fitting results reported for AMZN, EBAY and FB
- **Venue:** not stated (proprietary futures order-book feed; public stock order-book data drawn from a cited external source, no exchange named)
- **Period:** Sugar futures: several months of data starting January 2021 (proprietary). Stock data: a one-month window in November 2014, 18 to 20 days per stock.
- **Granularity:** Futures: every individual update to the top ten price/volume levels on each side of the book. Stocks: order book updated after every market order, also using ten price/volume levels per side.

## Features and Measures

- **GCHPnSDO quantile state mapping.** A way of building the Markov chain states for the n-state compound Hawkes model by splitting historical mid-price moves into positive and negative sets, cutting each set into quantile bands, and setting each state's value to the mean move size within its band.
- **Three-class directional label.** A classification of each forward mid-price move into upward, stationary, or downward by comparing the move to a fixed threshold and its negative.
- **Two-class volatility label.** A classification of each forward mid-price move into large or small by comparing its absolute size to a fixed threshold, used to test whether the model flags bigger swings regardless of direction.
- **Price-change autocorrelation.** A lag-based correlation of the count of mid-price changes in fixed time windows against the count in earlier, shifted windows, used to check how long the influence of one book event persists.

## Method

Each of four GCHP variants (GCHPDO, GCHP2SDO, GCHP4DO and the general n-state GCHPnSDO) pairs a Hawkes process for event timing with a Markov chain for event direction/size, fit day by day to the mid-price-change series. Hawkes parameters are fit by maximizing the process likelihood, and Markov-chain transition probabilities are estimated from empirical move frequencies in the training window; a diffusive-limit theorem then expresses the model's theoretical volatility in terms of the fitted parameters, and a least-squares comparison of this theoretical volatility to the empirical volatility over increasing time windows gives an error rate used to pick the best-fitting variant for each day or window.

Two separate prediction procedures are built on top of the fitted model. The first plugs the fitted parameters directly into a diffusive-limit corollary to produce one numeric mid-price forecast for a fixed horizon past the end of the training window. The second simulates many Hawkes-process arrival sequences together with simulated Markov-chain transitions to generate many candidate mid-price paths, then averages the simulated path endpoints into a final forecast. Both procedures are evaluated with same-day walk-forward validation (moving the train/test window forward through the day), and performance is judged on three-class directional accuracy, two-class volatility-label accuracy, and the distribution of the error between predicted and realized mid-price.

## Results

- The largest, n-state model (GCHPnSDO) was the best-fitting sugar futures variant on 64 of the tested windows (50.39% of them), more often than any other variant, but it also had the highest mean fitting error rate (7.69) among the four variants.
- Among the sugar futures variants, GCHP4DO had the lowest mean fitting error rate (2.77), despite being the best fit on only 26 of the tested windows.
- Sugar futures data showed on average close to 2000 mid-price changes per day, versus roughly 4000 per day for the AMZN stock data examined, reflecting different liquidity levels across instruments.
- Using the diffusive-limit prediction method on sugar futures data with thresholds of 0.025 (three-class) and 0.04 (two-class), three-class directional accuracy was only slightly above chance while the two-class volatility label was predicted clearly better than chance.
- On AMZN stock data (thresholds 0.15 and 0.3), the two-class volatility-label prediction accuracy peaked above sixty percent.
- The repeated-simulation prediction method used 250 simulated Hawkes/Markov-chain paths per test window to form each final mid-price forecast on sugar futures data.
- Across the reported experiments, three-class directional prediction accuracy topped out at around forty percent, while the two-class volatility label was consistently predicted more accurately than direction.
- An algebraic appendix shows that, under this model, the sign of the predicted future price direction depends only on the fitted Markov chain's steady-state probabilities and not directly on the Hawkes process's own parameters.

## Limitations

- Best-fitting model choice, and predictive accuracy, varied heavily day to day and stock to stock, and the authors state that extensive hyper-parameter tuning (thresholds, window lengths, number of simulated paths) was needed to get workable results.
- The stock dataset covers only 18 to 20 days per name, which the authors themselves say limits how well the stock results can generalize compared to the several months of futures data.
- The authors note that fitting and running the model across substantial amounts of limit order book data is computationally costly.
- Reader note: results are reported per instrument/window rather than pooled with formal significance testing, so the size of the directional accuracy edge over chance is hard to judge precisely from the paper alone.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/jump-clustering|jump clustering]]

## Citation

Myles Sjogren, Timothy DeLise (2021). General Compound Hawkes Processes for Mid-Price Prediction.

DOI: 10.48550/arxiv.2110.07075

Text ingested: `markdown_output/sjogren-2021-general-compound-hawkes-processes-mid-price.md`, converted from `raw/ofi-event-clock/sjogren-2021-general-compound-hawkes-processes-mid-price.pdf`.

Coverage of this summary: Read the full paper markdown from abstract through the appendices and references.

Known problems with the input: Nearly all mathematical definitions and theorems are rendered as omitted images in the markdown, so exact equation forms (Hawkes intensity, likelihood, diffusive-limit expressions) could not be verified from the text and are described only qualitatively here; Several summary-statistics tables (Figures 10, 13, 14, 15) are collapsed into single newline-separated cells by the markdown conversion; column alignment was inferred from the surrounding prose and may not be perfectly reliable.
<!-- AUTHORED REGION END -->