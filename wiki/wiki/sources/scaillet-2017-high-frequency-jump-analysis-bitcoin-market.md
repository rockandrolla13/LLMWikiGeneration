---
authors:
- Olivier Scaillet
- Adrien Treccani
- Christopher Trevisan
content_hash: sha256:9108f971137048bbf9cdda99298fe82fade77087a9524ab5ea68704a05d0cc54
created: 2026-09-27 01:47:00+00:00
page_id: sources/scaillet-2017-high-frequency-jump-analysis-bitcoin-market
page_type: source
related:
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/bid-ask-spread
- concepts/market-microstructure-noise
- concepts/jump-clustering
- concepts/high-frequency-data
- concepts/informed-trading
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:4761d33371fed4a5c092832091f7e8f7a218b0e9fa4c5e2c42e8e53311f1736c
source_path: markdown_output/scaillet-2017-high-frequency-jump-analysis-bitcoin-market.md
source_type: paper
tags:
- bitcoin
- cryptocurrency
- jump-detection
- order-flow
- liquidity
- high-frequency-data
- market-microstructure
- event-study
- clock-calendar
- asset-crypto
- harvest-relevant
title: High-Frequency Jump Analysis of the Bitcoin Market
updated: '2026-09-27T01:47:00Z'
uuid: 35d8b5cb-fcb6-5506-8672-09f7acd43b1c
year: 2017
---

<!-- AUTHORED REGION START -->
# High-Frequency Jump Analysis of the Bitcoin Market

## Summary

The paper asks whether jumps, the sudden discontinuous price moves that low-frequency studies often over-detect, are genuinely present and economically important in an emerging, unregulated, retail-driven market, and what market conditions precede and follow them. It uses a leaked internal database from the Mt. Gox bitcoin exchange covering June 2011 to November 2013, which uniquely records trader identifiers and whether each trade was buyer- or seller-initiated at the transaction level.

The authors apply the Lee and Mykland (2012) jump test to tick-by-tick bitcoin prices, using a noise-robust volatility estimator and controlling for the multiple-testing problem across days with a false discovery rate (FDR) procedure. They then build a regular, calendar-time panel (mainly 5-minute bars, with robustness checks at 10 and 20 minutes) of order flow imbalance, a bid-ask spread proxy, a novel measure of trader concentration they call the whale index, realized variance, and microstructure noise variance, and fit a probit model to see whether these variables predict the next-period jump probability. A follow-up event study compares market conditions before and after each detected jump using t-tests on log-ratios relative to a pre-jump reference period.

The main findings are that jumps are far more common in bitcoin than in large-cap equities or FX studied in prior work, that jump days cluster rather than arriving as an independent Poisson process, and that a widening bid-ask spread, larger absolute order flow imbalance, and a higher whale index (fewer traders responsible for most liquidity-taking) all significantly raise the probability of a jump in the next period. After a jump, trading activity, the number of traders, the spread, and both variance measures all spike but revert within about 45 minutes, whereas the level of the price itself shows a persistent shift.

What is new is the use of individually identified traders and trade-direction data, rarely available for other markets, to construct the whale index and directly link liquidity concentration to jump risk, together with a systematic before/after event study of jump impact that is only feasible because bitcoin generates a large enough number of detected jumps for statistical inference.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Jump detection itself operates on tick-by-tick transaction prices within each trading day, using the Lee-Mykland statistic computed over local blocks to average out microstructure noise. For the predictability and impact analysis the tick data is aggregated into fixed calendar bars, mainly 5-minute intervals (also checked at 10- and 20-minute), and a probit model predicts whether a jump occurs in the next 5-minute period from lagged spread, order-flow and trader-concentration variables; post-jump impact is measured over four consecutive 15-minute calendar windows following the jump, compared to a reference level one hour before the jump.

## Data

- **Asset class:** Crypto
- **Instruments:** bitcoin (BTC/USD)
- **Venue:** Mt. Gox exchange
- **Period:** June 26, 2011 to November 29, 2013
- **Granularity:** tick-level (transaction) data with trader IDs and trade direction, aggregated into 5-minute (and, for robustness, 10- and 20-minute) calendar bars

## Features and Measures

- **absolute order flow imbalance (OF).** The absolute value of the difference between aggressive buy volume and aggressive sell volume within an interval, used as a proxy for directional trading pressure.
- **whale index (WR).** The ratio of the number of unique passive traders to the total number of unique traders in an interval; a high value means few traders are responsible for most liquidity-taking.
- **median bid-ask spread (MS).** The median of the ratio of the bid-ask difference to the mid-price within an interval, used as the paper's illiquidity proxy.
- **realized variance (RV).** A noise-robust estimator (Podolskij and Vetter, 2009) of the latent price's variance over an interval.
- **microstructure noise variance (NV).** The estimated variance of the market microstructure noise contaminating observed prices, computed as in Lee and Mykland (2012).

## Method

The core statistical tool is the Lee and Mykland (2012) high-frequency jump test, applied to blocks of tick prices with a noise-robust volatility estimator and a noise-variance estimator, combined with false discovery rate (FDR) control at a 10% target level to correct for repeated daily testing; a runs test (Mood, 1940) is then applied to the sequence of jump/no-jump days to check whether jump arrivals are independent, as a simple Poisson-arrival model would imply. Jump predictability is assessed with a binary probit regression of a jump indicator on lagged spread, order flow, trader-concentration, price-level, realized-variance and noise-variance covariates, with and without sub-period fixed effects, reporting coefficient estimates, marginal probabilities, and adjusted pseudo-R2. Jump impact is assessed with Student t-tests on the log-ratio of post-jump statistics (computed over four consecutive 15-minute windows) to a one-hour-earlier reference level, separately for all jumps, positive jumps, and negative jumps.

## Results

- The Lee-Mykland test with 10% FDR control identifies 124 jump days out of 888 sample days, roughly one jump day per week, far more frequent than reported in prior high-frequency studies of large-cap equities or FX.
- 70 of the 124 detected jumps are positive and 54 are negative, with average sizes of 4.65% and -4.14% respectively, and a maximum single move of 32% within a 5-minute interval.
- A runs test strongly rejects independent jump arrival on the full sample (<0.01), though the clustering is concentrated in the earliest sub-period and is not detected in the final third of the sample.
- A probit model shows that the median spread, absolute order flow imbalance, and the whale index all significantly and positively predict the probability of a jump in the next 5-minute period, with an adjusted pseudo-R2 of 0.07.
- Following a jump, trading volume, the number of active traders, order flow imbalance, the spread, realized variance and noise variance all rise, but these effects revert to prior levels within about 45 minutes.
- The price-level effect of a jump is persistent rather than transient: positive jumps leave a lasting lower price and negative jumps a lasting higher price, in contrast to the other measures that revert.

## Limitations

- The analysis covers a single exchange (Mt. Gox) and a single asset (bitcoin) over 2011-2013, a period before modern market structure, regulation, or the entry of institutional liquidity providers.
- The data set records only executed trades with an inferred buyer/seller direction, not the full limit order book, so spread and depth measures are proxies rather than direct order-book observations.
- Reader note: the jump test only flags whether at least one jump occurred on a given day, not how many, which the authors note prevents a direct test of exponential inter-jump durations.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/jump-clustering|jump clustering]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Olivier Scaillet, Adrien Treccani, Christopher Trevisan (2017). High-Frequency Jump Analysis of the Bitcoin Market.

DOI: 10.2139/ssrn.2982298

Text ingested: `markdown_output/scaillet-2017-high-frequency-jump-analysis-bitcoin-market.md`, converted from `raw/ofi-event-clock/scaillet-2017-high-frequency-jump-analysis-bitcoin-market.pdf`.

Coverage of this summary: Read the entire converted markdown: abstract, introduction, data and cleaning section, jump-test methodology, all three empirical results subsections (jump distribution, predictability, impact), and the conclusion.

Known problems with the input: Mathematical expressions (the log-price model, block-averaging formula, test statistic, and asymptotic variance) are rendered as omitted-picture placeholders in the converted markdown, so the exact functional forms could not be independently verified beyond what is described in prose.
<!-- AUTHORED REGION END -->