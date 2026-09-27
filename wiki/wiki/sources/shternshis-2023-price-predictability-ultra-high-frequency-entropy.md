---
authors:
- Andrey Shternshis
- Stefano Marmi
content_hash: sha256:c6eb1628288e1ebd0ba46243431291b8ba3a7bbf7beea72b5b6d2e23244e3f70
created: 2026-09-27 01:47:00+00:00
page_id: sources/shternshis-2023-price-predictability-ultra-high-frequency-entropy
page_type: source
related:
- concepts/trade-clock
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/order-flow
- concepts/autocorrelation-time-series
- concepts/stylized-facts
- concepts/long-memory
- concepts/limit-order-book
- concepts/high-frequency-trading
revision_id: 1
schema_version: 2
source_hash: sha256:7725f529ae9e9809682a9b47cb1c38e3b59159996cb3da838642b2ae35337f8a
source_path: markdown_output/shternshis-2023-price-predictability-ultra-high-frequency-entropy.md
source_type: paper
tags:
- ultra-high-frequency
- entropy
- predictability-test
- limit-order-book
- transaction-time
- order-flow
- market-microstructure
- stylized-facts
- clock-trade
- asset-equity
- harvest-relevant
title: 'Price predictability at ultra-high frequency: Entropy-based randomness test'
updated: '2026-09-27T01:47:00Z'
uuid: 2b48cd55-272b-547b-98d7-2b1c1cc362c7
year: 2023
---

<!-- AUTHORED REGION START -->
# Price predictability at ultra-high frequency: Entropy-based randomness test

## Summary

The paper asks whether ultra-high-frequency, tick-by-tick sequences of price-direction signs are statistically predictable from their own history, and how that predictability changes as the data are aggregated by number of transactions, i.e. moving to a coarser step size in transaction time.

Its approach is to build a hypothesis test on empirical block frequencies: it estimates Shannon entropy over overlapping blocks of symbols and derives a Neyman-Pearson-type statistic, a scaled Kullback-Leibler divergence, whose asymptotic distribution is chi-squared, so independence of a new symbol from the sequence's history can be tested even when the two symbols (price up or down) are not equally likely. The test is first checked on simulated order-flow models capturing order splitting, herd or chartist behaviour, and mean reversion, then applied to LOBSTER limit-order-book data for nine US-listed assets (eight stocks plus the SPY ETF) over 80 trading days from August to November 2022, after discretizing each non-zero return into a binary up/down symbol in transaction time.

The main finding is that predictability is common at the finest, per-transaction resolution and declines, though not always monotonically, as the sequence is aggregated to coarser transaction counts per step. Predictable days tend to show higher trading volume, more price changes, and higher autocorrelation of returns and of their magnitudes than unpredictable days. For most assets, predictability comes from persistence (an elevated chance of repeating the same up/down direction), but for a smaller group it instead comes from an elevated chance of the direction flipping. Splitting each day into shorter, non-overlapping sub-intervals usually locates a single predictable interval per predictable day, with SNAP as an exception where several predictable intervals can occur back to back.

What is new is a computationally cheap test, needing only frequency counts rather than Monte Carlo simulation, that remains valid when the two symbols are not equiprobable and uses overlapping blocks, together with a systematic link between the degree of predictability, the aggregation level, and standard microstructure stylized facts such as long memory of order signs, volatility clustering and fat tails.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Each recorded transaction (timestamped to one nanosecond) updates the price, and non-zero price returns are coded into a binary up/down symbol to build the raw, per-transaction sequence. The paper then re-samples this sequence at coarser 'aggregation levels' by keeping only every a-th transaction (for example every 10th, 15th or 30th) and recomputing the return sign at that sampling rate, so predictability is always tested one step ahead on whatever transaction-count grid is chosen, not on a fixed calendar-time or volume-based clock.

## Data

- **Asset class:** Equities
- **Instruments:** AAPL, MSFT, TSLA, INTC, LLY, SNAP, F and CCL (individual US-listed stocks) plus the SPY ETF, which tracks the S&P 500 Index
- **Venue:** Not stated beyond the data provider: LOBSTER (www.lobsterdata.com) limit order book reconstructions
- **Period:** 01.08.2022 to 21.11.2022, spanning 80 trading days
- **Granularity:** Full record of executed visible and hidden limit order transactions timestamped to one nanosecond, with a robustness check that aggregates simultaneous same-nanosecond transactions into one event

## Features and Measures

- **Binary price-direction symbol.** Each non-zero price return is coded 0 for a decrease and 1 for an increase, turning the tick-by-tick price series into a binary symbolic sequence in transaction time.
- **Entropy bias (statistic B).** An empirical-frequency estimate of Shannon entropy over overlapping blocks of symbols; its distance from the maximum entropy achievable under full randomness is compared to a chi-squared distribution to detect dependence on sequence history.
- **Neyman-Pearson predictability statistic (statistic D).** A scaled Kullback-Leibler divergence between the empirical transition frequencies of blocks of symbols and the frequencies expected under the no-dependence null, with a known chi-squared asymptotic distribution that remains valid when symbols are not equiprobable.
- **Aggregation level (transaction-time sampling step).** The number of raw transactions treated as one time step before recomputing the price-direction symbol, used to trace how quickly predictability decays as the sampling grid coarsens.

## Method

The core method is a hypothesis test for independence of symbols in a stationary sequence drawn from a finite alphabet. Non-overlapping blocks of a length k, chosen from the sequence length and alphabet size, are used to estimate empirical frequencies and hence Shannon entropy; under the null of independent, equiprobable symbols the entropy bias follows a chi-squared distribution, and the paper extends this to unequal symbol probabilities via a Neyman-Pearson statistic D built from overlapping blocks, a scaled Kullback-Leibler divergence whose own chi-squared asymptotic distribution is derived and checked with QQ-plots in an appendix. A day is labelled predictable when the null is rejected at significance level 0.01. The test is validated on three simulated order-flow models (an order-splitting model, an order-driven model, and a trade-superposition model) before being applied per trading day to the LOBSTER data for the nine assets, varying the transaction-count aggregation level to see how the fraction of predictable days changes. Predictable and unpredictable days are then compared on trading volume, autocorrelation of returns and of their magnitudes, the tail thickness of a fitted Student's t distribution of returns, and the frequency of detected price jumps, using two-sample mean-difference tests at 0.05 and 0.01 significance. A final step applies a Sidak-corrected multiple-testing procedure across non-overlapping intra-day sub-intervals to localize which part of a predictable day carries the detected predictability.

## Results

- For AAPL, all 80 days were classified as predictable using the NP-statistic, and 79 of 80 using the entropy-bias statistic, before any aggregation.
- Aggregating AAPL transactions to a level of a = 30 left only 4 predictable days (02.08, 20.09, 05.10) plus one more identified via entropy bias.
- For TSLA, 35 predictable days were found at aggregation a = 25, falling to 4 predictable days at a = 65.
- For INTC, 44 predictable days were found at aggregation a = 2, falling to 8 predictable days at a = 7 and to a single predictable day, October 13, at a = 10.
- SNAP had 53 predictable days with no aggregation, and unlike most other assets its predictability came from an unusually low, not high, probability of repeating the same up/down symbol.
- On predictable days, several assets (AAPL, MSFT, INTC, LLY, F, CCL and SPY) showed significantly higher trading volume and more non-zero price changes than on not-predictable days.
- For 8 out of 9 assets, non-zero returns on predictable days had significantly higher autocorrelation than on not-predictable days.
- For SNAP, 7 predictable sub-day intervals were found occurring consecutively on both October 21 and October 24.

## Limitations

- The authors note the test alone does not establish that ultra-high-frequency predictability translates into a profitable trading strategy once transaction costs are taken into account.
- The paper points out that long memory in price-return signs can produce detectable predictability without violating the efficient market hypothesis, so a rejected null need not mean an exploitable inefficiency.
- The classification of a day as predictable depends on a user-chosen block length k and a fixed significance level of 0.01, both of which affect how many days are flagged.
- Reader note: the dataset covers only 80 trading days across four months (August-November 2022) for nine US-listed names, so conclusions about seasonal or cross-asset patterns rest on a short, non-random sample window.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-flow|order flow]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/long-memory|long memory]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]

## Citation

Andrey Shternshis, Stefano Marmi (2023). Price predictability at ultra-high frequency: Entropy-based randomness test.

DOI: 10.48550/arxiv.2312.16637

Text ingested: `markdown_output/shternshis-2023-price-predictability-ultra-high-frequency-entropy.md`, converted from `raw/ofi-event-clock/shternshis-2023-price-predictability-ultra-high-frequency-entropy.pdf`.

Coverage of this summary: Read the full main text: abstract, introduction, the statistical-test derivation (Section 2), the dataset description (Section 3), the simulated-model validation and real-data analysis (Section 4, subsections 4.1-4.5), and the discussion and conclusion (Section 5). Appendix A's proof sketch was read for its stated result but not derived line by line, and only the first part of Appendix B's per-stock tables was read; the remainder of Table 8 and the bibliography were not read in detail.

Known problems with the input: No publication year or venue/journal name is printed anywhere in the visible converted text; year is taken from the job file's year_hint (2023); year from file metadata; The markdown replaces mathematical equations and some figure content with '==> picture... omitted <==' placeholders, and OCR mangles some exponents/subscripts; no numbers were taken from those garbled spans; The final portion of the file (later rows of Appendix Table 8 and the bibliography) was not read in detail, since it only lists further per-day partition results and reference citations.
<!-- AUTHORED REGION END -->