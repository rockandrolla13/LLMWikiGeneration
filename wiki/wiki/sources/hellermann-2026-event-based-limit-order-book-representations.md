---
authors:
- Justin Hellermann
- Stefan Lessmann
content_hash: sha256:8f6fe17d3764a298f6fa12afaa4185b2b5846c293564f45c6d3e4bd2b792144e
created: 2026-09-27 01:47:00+00:00
page_id: sources/hellermann-2026-event-based-limit-order-book-representations
page_type: source
publication_venue: SSRN working paper (preprint, not peer reviewed)
related:
- concepts/sampling-clocks
- concepts/limit-order-book
- concepts/order-flow
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/deep-learning-for-finance
- concepts/transformers
- concepts/feature-engineering
- concepts/volume-clock
- concepts/trade-clock
revision_id: 1
schema_version: 2
source_hash: sha256:46f901e8106fe04d8028f5522e0cbcdd209e30f0529d836b35334dfd5605798f
source_path: markdown_output/hellermann-2026-event-based-limit-order-book-representations.md
source_type: paper
tags:
- bar-construction
- event-based-sampling
- limit-order-book
- vwap
- electricity-markets
- probabilistic-forecasting
- calibration
- clock-compares
- asset-none
- harvest-core
title: Event-Based Limit Order Book Representations for Probabilistic VWAP Forecasting
  in Intraday Electricity Markets
updated: '2026-09-27T01:47:00Z'
uuid: aaaf7d2c-532a-502a-8ebb-be814e2afb25
year: 2026
---

<!-- AUTHORED REGION START -->
# Event-Based Limit Order Book Representations for Probabilistic VWAP Forecasting in Intraday Electricity Markets

## Summary

The paper asks whether how limit-order-book and transaction data are aggregated into bars, rather than the forecasting model itself, is a first-order driver of probabilistic forecast quality in continuous intraday electricity markets. It focuses on forecasting the volume-weighted average price (VWAP) of the next bar, a benchmark the authors argue is more economically meaningful than the last trade price or mid-quote because it reflects realised execution.

Using reconstructed order-book and transaction data from the EPEX M7 UK intraday market, the authors build four competing bar construction schemes: time bars (fixed calendar intervals), tick bars (fixed transaction counts), volume bars (fixed cumulative physical quantity), and traded-value bars (fixed cumulative absolute monetary value, using the absolute value because electricity prices can be negative). Thresholds are tuned so all four schemes produce roughly the same number of bars. Each bar's features (transaction- and order-book-based) feed a probabilistic forecasting model - a mixture density network (feed-forward or Transformer-encoder based) with a Gaussian mixture output, benchmarked against a Student-t regression model - trained with a combined negative-log-likelihood/CRPS loss and calibrated afterward with isotonic regression.

The central finding is that traded-value bars deliver the lowest average forecast error (CRPS) and, together with the other event-based schemes, better calibration than clock-time bars, especially as the aggregation threshold coarsens. The paper links this to an exposure-homogeneity argument: traded-value (and, on a different measure, volume) bars produce far more consistent monetary exposure per bar across and within time-to-delivery states than time bars do, and a within-run fixed-effects regression shows this homogeneity is systematically associated with lower CRPS. Two downstream applications - classifying price-regime states (scarcity/oversupply/very-low-price) and a portfolio-balancing execution backtest - both show event-based bars, and traded-value bars in particular, improving decision-relevant outcomes (regime detection and price quality), though not uniformly improving downside-risk measures.

What is new is the systematic, model-controlled comparison of event-based bar construction schemes (well established in financial market microstructure) applied for the first time, per the authors, to continuous intraday electricity markets, plus the direct within-run statistical test tying bar-induced exposure homogeneity to probabilistic forecast quality, and the translation of that improvement into two concrete operational use cases.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The paper reconstructs the limit order book and executed-transaction stream and re-samples it into four alternative bar types: fixed-calendar time bars, fixed-count tick bars, fixed-quantity volume bars, and fixed-monetary-value traded-value bars (using absolute traded value, since electricity prices can be negative). Thresholds (5,000, 10,000, and 20,000 for traded-value bars, with matching thresholds for the other schemes) are chosen so each scheme yields about the same number of observations (around 0.6 million each) over the sample. The forecasting target for every scheme is the VWAP of the next bar of that type; for time bars the resulting horizon is fixed in calendar time, while for the three event-based schemes the effective calendar-time horizon varies endogenously with trading intensity.

## Data

- **Asset class:** No data (theory or survey)
- **Instruments:** 30-minute delivery products traded in the continuous intraday electricity market (electricity is not one of the listed asset classes)
- **Venue:** EPEX M7 continuous intraday electricity market, UK bidding zone
- **Period:** 2023 (order-book events 2022-12-31 to 2023-12-31; executed transactions 2022-12-31 to 2023-12-31)
- **Granularity:** Individual order-book events (creation, modification, cancellation, matching) and individual executed transactions, aggregated into bars of about 0.6 million observations per scheme

## Features and Measures

- **Time bars.** Bars formed by aggregating transactions over fixed calendar-time intervals, giving every calendar interval equal weight regardless of trading activity.
- **Tick bars.** Bars formed after a fixed number of transactions, so each bar contains the same trade count but not necessarily the same traded quantity or value.
- **Volume bars.** Bars formed once cumulative traded physical volume (MWh) since the last bar reaches a fixed threshold.
- **Traded-value bars.** Bars formed once cumulative absolute traded monetary value (price times volume, with an absolute value applied because of negative electricity prices) reaches a fixed threshold; the paper's main focus, analogous to dollar bars in equity markets.
- **VWAP forecasting target.** The volume-weighted average price of the next bar, defined as the sum of price times volume divided by the sum of volume over the transactions in that bar.
- **Exposure-homogeneity measures.** Two summary statistics per bar type and threshold: the dispersion (standard deviation) of mean traded value across time-to-delivery bins, and the average coefficient of variation of traded value within each time-to-delivery bin, used to quantify how comparable bar-level economic exposure is across the trading horizon.
- **Mixture density network (feed-forward and Transformer).** A neural network that maps bar-level features (contemporaneous, or a lagged sequence via a Transformer encoder) to the weights, means, and variances of a Gaussian mixture, giving a full predictive density for next-bar VWAP.

## Method

For each bar type and threshold, features are built from the reconstructed limit order book and recent transactions (volume-weighted buy/sell prices, mid-price indicators, bid-ask spreads, depth imbalance, quantile-based price/volume measures at multiple book levels, order-book slope, and rolling volatility statistics), plus time-to-delivery information. Two probabilistic model families are trained on these features to forecast next-bar VWAP: a mixture-density-network head (Bishop-style) fed either by a feed-forward network on the contemporaneous feature vector or by a Transformer encoder over a lagged sequence of 5 or 10 bars, with 2, 4, or 8 mixture components; and a Student-t regression model as a more parsimonious probabilistic benchmark. Models are trained by minimising a weighted combination of negative log-likelihood and the Continuous Ranked Probability Score (CRPS), and predictive distributions are subsequently recalibrated with isotonic regression fit on a validation set. Data are split by trading day into 60% training, 20% validation, and 20% test sets. The full design (bar type, threshold, lag length, mixture count, model architecture) totals 1,260 simulation runs, letting the authors attribute forecast-quality differences to data representation rather than model choice.

Forecast quality is assessed with CRPS, negative log-likelihood, normalised RMSE/MAE, probability integral transform (PIT) diagnostics, empirical coverage curves, and integrated squared calibration error (ISE) for both PIT and coverage. A separate within-run fixed-effects regression relates CRPS to the two exposure-homogeneity measures (with bar construction, threshold, lag, and hyperparameters absorbed as run fixed effects) at both the product level and the day level. Two applications extend the analysis: a regime-diagnostic classifier that scores the probability of high-price, very-low-price, and low-price VWAP outcomes using Brier skill, separation, and recall; and a portfolio-balancing execution backtest that compares a Last Bar benchmark, a Hypothetical Mean strategy, an unattainable Oracle Benchmark, and three probabilistic execution rules, evaluated on price quality, PnL per MW, early- versus late-execution share, 5% delivery PnL, and maximum drawdown, with Kruskal-Wallis and Mann-Whitney U tests used to check statistical significance across bar types.

## Results

- Traded-value bars achieve the lowest average CRPS (7.080), followed by tick bars (8.200) and volume bars (8.305), while time bars perform worst (9.358).
- A one-standard-deviation increase in the dispersion of mean traded value across time-to-delivery bins raises CRPS by 1.291 at the product level and 1.718 at the day level; a one-standard-deviation increase in within-bin traded-value heterogeneity raises CRPS by 0.441 and 0.712 respectively, both statistically significant.
- Traded-value bars have the lowest coverage-calibration error at the lower thresholds (ISE of 0.0008 at 5,000 and 0.0011 at 10,000) and the lowest PIT-calibration error at the higher thresholds (0.0005 at 10,000 and 0.0078 at 20,000).
- Volume bars produce the most homogeneous exposure across time-to-delivery bins (e.g. an SD of TTD means of 69.26 at the 5,000 threshold), while traded-value bars become marginally more homogeneous within a bin at the highest threshold examined (within-bin CV of 0.175 at 20,000).
- In regime-diagnostic tests the mixture density network clearly outperforms the Student-t regressor across all event categories, for example a Brier skill of 0.7339 versus 0.1634 for the high-price regime.
- Among probabilistic execution strategies, traded-value bars deliver the highest PnL per MW (22.22) versus tick bars (11.95) and volume bars (11.86), though traded-value bars do not achieve the best downside-risk metrics.
- Kruskal-Wallis tests confirm that execution-quality metrics differ systematically across bar construction schemes, for example a statistic of 698.0361 for price quality.
- The underlying dataset contains over 517 million order-book events and more than 24 million transactions in 2023, with about 2.44% of transactions occurring at negative prices.

## Limitations

- The empirical analysis covers a single market (the UK EPEX M7 continuous intraday market), one delivery-product granularity (30-minute products), and one year of data (2023).
- External fundamentals such as weather, renewable-generation forecasts, cross-border capacity, and outage information are deliberately excluded, so results reflect only endogenous market data.
- The execution backtest omits queue priority, latency, transaction costs, and market impact, so it is described by the authors as a comparative rather than fully realistic simulation of trading.
- The paper is an unreviewed preprint (stated on every page as 'This preprint research paper has not been peer reviewed').
- Reader note: the manuscript text does not print an explicit publication year on its title page; the year used here is taken from the source file's metadata, not the paper itself.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow|order flow]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/transformers|transformers]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/volume-clock|Volume Clock]]
- [[concepts/trade-clock|Trade Clock]]

## Citation

Justin Hellermann, Stefan Lessmann (2026). Event-Based Limit Order Book Representations for Probabilistic VWAP Forecasting in Intraday Electricity Markets. SSRN working paper (preprint, not peer reviewed).

DOI: 10.2139/ssrn.7115109

Text ingested: `markdown_output/hellermann-2026-event-based-limit-order-book-representations.md`, converted from `raw/ofi-event-clock/hellermann-2026-event-based-limit-order-book-representations.pdf`.

Coverage of this summary: Read the full paper end to end: abstract, introduction, related work, methodology (bar construction and market-state representation, VWAP forecasting framework), data section, experimental setup, all results subsections (market-state representation, exposure homogeneity vs. CRPS, forecasting performance, calibration and reliability, summary of findings), the practical-applications section (regime diagnostics, portfolio balancing), future work, conclusion, and the appendix tables and references.

Known problems with the input: The PDF-to-markdown conversion renders most tables as run-together HTML/markdown blocks with column headers and values interleaved into the surrounding prose, and significance-star markers are garbled (e.g. rendered as stray arrow characters); numbers were cross-checked carefully against these tables before use; No explicit publication year appears in the visible text of the paper itself (only the SSRN abstract number and citation years for other works); the year field was taken from the job file's year_hint rather than the source document.
<!-- AUTHORED REGION END -->