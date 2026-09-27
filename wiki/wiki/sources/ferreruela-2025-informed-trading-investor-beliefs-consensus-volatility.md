---
authors:
- Sandra Ferreruela
- Daniel Martín
content_hash: sha256:c9d5d2e9dc928f59d29bb8fe0ad5db04322decda677a59c5be0849f2f48f1ef3
created: 2026-09-27 01:47:00+00:00
page_id: sources/ferreruela-2025-informed-trading-investor-beliefs-consensus-volatility
page_type: source
publication_venue: Journal of Multinational Financial Management
related:
- concepts/volume-clock
- concepts/informed-trading
- concepts/limit-order-book
- concepts/order-flow-imbalance
- concepts/market-microstructure
- concepts/bid-ask-spread
- concepts/high-frequency-data
- concepts/adverse-selection
- concepts/liquidity-risk
- concepts/vpin
revision_id: 1
schema_version: 2
source_hash: sha256:558bb3017eecba5630dd7cc61fd72a1a021a76254785812148099132fabac22a
source_path: markdown_output/ferreruela-2025-informed-trading-investor-beliefs-consensus-volatility.md
source_type: paper
tags:
- informed-trading
- limit-order-book
- vpin
- lob-slope
- volatility
- covid-19
- ibex-35
- granger-causality
- clock-volume
- asset-equity
- harvest-core
title: 'Informed trading, investor beliefs consensus and volatility: Evidence from
  the Limit Order Book dynamics during COVID-19 and short-selling ban'
updated: '2026-09-27T01:47:00Z'
uuid: 3bb84c34-eeff-5fb6-9adb-d1af5ad16b36
year: 2025
---

<!-- AUTHORED REGION START -->
# Informed trading, investor beliefs consensus and volatility: Evidence from the Limit Order Book dynamics during COVID-19 and short-selling ban

## Summary

This study asks whether the shape of the limit order book, summarized by its slope, is a better predictor of short-horizon volatility than VPIN, the standard measure of order-flow toxicity from informed trading. It examines 32 IBEX-35 constituent stocks, split into large-, mid- and small-cap portfolios, using tick-by-tick trade and full order-book data from Bolsas y Mercados Españoles for the period 2 January 2019 to 31 December 2020, which spans the COVID-19 pandemic crash and a subsequent short-selling ban.

Data are sampled on a volume clock: each stock's trading day is divided into volume buckets, and the last observed value in each bucket is used to compute VPIN, the LOB slope, the relative spread and depth. The authors combine stock-by-stock OLS regressions pooled by random-effects meta-analysis, Driscoll-Kraay fixed-effects panels, conditional probability tables built from empirical-CDF-normalized VPIN and slope, and stock-level VAR models with Granger-causality tests and meta-analytic impulse-response functions, controlling throughout for the COVID crash, the short-selling ban, a de-escalation window, trade size, and EGARCH(1,1) conditional volatility.

VPIN plays a dual role: it raises belief consensus in the book while eroding internal liquidity, an effect strongest in small caps. But for predicting next-period volatility, book consensus dominates: once SLOPE's cross-stock percentile exceeds about 0.4, the probability of the lowest-volatility state exceeds 97% for large caps, while VPIN's conditional probability distributions stay flat regardless of its own level. Granger-causality tests confirm the asymmetry: the SLOPE-to-volatility and volatility-to-SLOPE links are significant in all 32 stocks, whereas VPIN's causal links with SLOPE and volatility appear in only 12 to 17 of the 32 stocks depending on the pair.

The paper's contribution is to shift short-horizon volatility analysis away from executed trade imbalance and toward the latent, unexecuted structure of the order book, showing this consensus channel is both more universal across stocks and more size-dependent in how it interacts with VPIN than prior microstructure work assumed.

## Clock and Sampling

**Volume clock: one observation per unit of volume traded.**

See [[concepts/volume-clock|Volume Clock]].

Each stock's tick-by-tick trades and order-book snapshots are aggregated into volume buckets sized at one-fiftieth of its average 2019 daily volume (the construction underlying the 50-length rolling VPIN window); the last observed value within a bucket is used for VPIN, SLOPE, spread and depth. Prediction is one bucket ahead: values measured at bucket τ-1 (VPIN, SLOPE, and controls) are used to explain SLOPE, spread, depth, or EGARCH volatility at bucket τ.

## Data

- **Asset class:** Equities
- **Instruments:** 32 IBEX-35 constituent stocks, split into three portfolios of 11 large-cap, 11 mid-cap and 10 small-cap stocks
- **Venue:** SIBE (Sistema de Interconexión Bursátil Español), operated by Bolsas y Mercados Españoles (BME)
- **Period:** 2 January 2019 to 31 December 2020, including the COVID-19 crash (21 January 2020 to 17 March 2020), the short-selling ban (18 March 2020 to 18 May 2020), and a de-escalation window (19 May 2020 to 13 July 2020)
- **Granularity:** tick-by-tick, millisecond-level trades and the full limit order book, aggregated into volume buckets; continuous trading only, with call auctions excluded

## Features and Measures

- **VPIN.** Volume-Synchronized Probability of Informed Trading: the cumulative absolute imbalance between buy and sell volume within each volume bucket, with trade direction assigned probabilistically from the standardized price change using the bulk volume classification method.
- **SLOPE.** The slope of the limit order book's demand and supply sides, computed from the relationship between cumulative log volume and price level, used as a proxy for the concentration (or dispersion) of trader beliefs and for internal liquidity.
- **Relative spread (RS).** The normalized difference between best bid and best ask prices, used as a proxy for external liquidity and market-impact cost.
- **DEPTH.** The average accumulated shares at non-zero price positions on the best bid and best ask sides, used as a proxy for internal liquidity.
- **CDF-normalized VPIN and SLOPE.** Stock-by-stock empirical cumulative distribution function transforms of VPIN and SLOPE onto a common 0-1 percentile scale, enabling cross-stock and cross-market comparison.
- **EGARCH(1,1) conditional volatility.** An exponential GARCH model of the log conditional variance of bucket returns, used as the paper's primary volatility measure because it captures persistence, clustering and asymmetric (leverage) responses to shocks.

## Method

For H1a and H1b, the authors regress SLOPE, the relative spread (RS) and DEPTH on lagged VPIN and a common set of controls (CRASH, SSB, de-escalation dummies, average trade size, EGARCH volatility) separately for each stock within each cap group, pool the stock-level OLS coefficients via inverse-variance-weighted random-effects meta-analysis, and cross-check the results with fixed-effects Driscoll-Kraay panel regressions robust to serial correlation, heteroskedasticity and cross-sectional dependence.

For H2, conditional probability tables map deciles of empirical-CDF-normalized SLOPE and VPIN at bucket τ-1 to bins of EGARCH volatility at bucket τ; statistical significance is assessed with bootstrapped confidence intervals (5000 resamples) and Monte Carlo simulation (10,000 tables) against the null of independence, and the exercise is repeated with an alternative volatility proxy based on absolute return residuals.

For H3, EGARCH volatility, SLOPE and cumulative VPIN are residualized against the CRASH, SSB and de-escalation shocks via the Frisch-Waugh-Lovell approach, standardized, and fit with a stock-by-stock VAR; causal direction is tested with stock-level Granger tests aggregated into panel-level Dumitrescu-Hurlin and Wald statistics, and dynamic responses are summarized with meta-analytic cumulative impulse-response functions reported separately by market-cap segment.

## Results

- In large-cap meta-analysis, lagged VPIN significantly raises SLOPE (belief consensus): coefficient 1.4871, p=0.0213.
- VPIN's effect on SLOPE is strongest and most reliable in small caps (coefficient 0.6208, p<0.001), the highest statistical confidence of any group.
- VPIN robustly reduces internal liquidity (DEPTH) in every cap group; the effect is largest in small caps (coefficient -1.1891, p<0.001), significant in 80.0% of small-cap stocks.
- VPIN's effect on external liquidity (RS) is statistically insignificant in large caps (coefficient -0.2878, p=0.1927).
- Conditional probability tables show that once SLOPE (CDF) exceeds 0.4, the probability of the lowest-volatility state exceeds 93% for large caps and approaches 97% at the highest consensus levels; VPIN (CDF) shows no comparable monotonic relationship with volatility.
- For small caps, the probability of low volatility surpasses 71% at the highest consensus deciles of SLOPE (CDF).
- Panel Granger-causality tests find SLOPE Granger-causes EGARCH volatility, and EGARCH Granger-causes SLOPE, in all 32 stocks; VPIN's causal links are asset-dependent, significant in only 12 to 17 of the 32 stocks depending on the pair.
- Driscoll-Kraay fixed-effects panels confirm VPIN raises SLOPE in large caps (1.8758, p<0.01) and small caps (0.7093, p<0.05), but the mid-cap effect loses significance (-1.1668).

## Limitations

- Sample is limited to 32 stocks on a single exchange (SIBE, Spain) over 2019-2020, a period dominated by the COVID-19 crash and short-selling ban.
- Auctions are excluded from the sample, restricting analysis to continuous trading hours only.
- Full VAR/IRF coefficient estimates and some robustness tables are not shown in the main text; the authors state they are available upon request or in supplementary materials.
- Reader note: the extreme-volatility study period (COVID crash, short-selling ban) may limit how well the consensus-dominance finding generalizes to calmer markets.

## Related

- [[concepts/volume-clock|Volume Clock]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/liquidity-risk|liquidity risk]]
- [[concepts/vpin|VPIN]]

## Citation

Sandra Ferreruela, Daniel Martín (2025). Informed trading, investor beliefs consensus and volatility: Evidence from the Limit Order Book dynamics during COVID-19 and short-selling ban. Journal of Multinational Financial Management.

DOI: 10.1016/j.mulfin.2025.100944

Text ingested: `markdown_output/ferreruela-2025-informed-trading-investor-beliefs-consensus-volatility.md`, converted from `raw/ofi-event-clock/ferreruela-2025-informed-trading-investor-beliefs-consensus-volatility.pdf`.

Coverage of this summary: Read the full text: abstract, introduction, literature review, data and measures section, all of section 4 (non-contemporaneous regressions, conditional probability tables, VAR/Granger causality), the conclusion, and the appendix confounder-sensitivity figures; the large numeric tables (2-10) were scanned for key meta-analytic and panel coefficients rather than transcribed cell-by-cell.

Known problems with the input: Markdown conversion omits all displayed equations (replaced with 'picture omitted' placeholders) and garbles some inline citation fragments, so exact equation forms are not verifiable from this file; Large data tables (2-10) contain OCR artifacts (misaligned columns, stray characters) that made some individual-stock coefficients unreliable to extract; only clearly legible meta-analytic and panel-level coefficients were used.
<!-- AUTHORED REGION END -->