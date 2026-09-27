---
authors:
- Silvia Onofri
- Andrey Shternshis
- Stefano Marmi
content_hash: sha256:83cd3304f820188acaa967876f54cdb0b10641ddb61e9afba33641ebba6b80b7
created: 2026-09-27 01:47:00+00:00
page_id: sources/onofri-2025-emergence-randomness-temporally-aggregated-financial-tick
page_type: source
related:
- concepts/trade-clock
- concepts/high-frequency-data
- concepts/stylized-facts
- concepts/autocorrelation-time-series
- concepts/limit-order-book
- concepts/high-frequency-trading
revision_id: 1
schema_version: 2
source_hash: sha256:0fc9f1efecbfeb5c8d0c05c350d7b9144bb85d01ad08f72a871830adf7a3b478
source_path: markdown_output/onofri-2025-emergence-randomness-temporally-aggregated-financial-tick.md
source_type: paper
tags:
- randomness-tests
- tick-data
- high-frequency-data
- market-efficiency
- entropy
- nist-sts
- clock-trade
- asset-equity
- harvest-relevant
title: Emergence of Randomness in Temporally Aggregated Financial Tick Sequences
updated: '2026-09-27T01:47:00Z'
uuid: 7e4d8eae-592b-55a2-bd58-f77b9a7b793e
year: 2025
---

<!-- AUTHORED REGION START -->
# Emergence of Randomness in Temporally Aggregated Financial Tick Sequences

## Summary

The paper asks how far tick-by-tick stock returns resemble the output of a random number generator, and how that resemblance changes as the data are aggregated over more transactions. It extends the authors' earlier entropy-only analysis by applying comprehensive randomness-test batteries -- frequency, pattern, entropy/complexity, spectral, and random-walk tests -- rather than relying only on serial correlation or entropy measures.

Each day's sequence of executed trade prices is converted into a binary string by comparing consecutive prices (0 if the ratio falls, 1 if it rises, no bit if unchanged). Binary strings are then built at aggregation levels from 1 to 100 transactions, with multiple overlapping samples generated per level so the full dataset is used, and monthly strings are tested with the NIST Statistical Test Suite and the Alphabit and Rabbit sub-batteries of TestU01, alongside two custom entropy-based tests (ShannonEntropy and KL) from prior work. Before use on financial data, each test is validated with a 'sanity check' against three independent random-number generators (a quantum RNG, the Linux /dev/urandom generator, and a Mobius-function-based generator), and any test that too often rejects randomness on these known-random strings is excluded.

Randomness generally increases with the aggregation level, confirming the earlier entropy-based finding across many more tests. However, some tests reveal exceptions: for two of the most actively traded stocks, predictability persists even at the highest aggregation level tested, and one spectral test shows a non-monotonic pattern in which predictability first rises with aggregation before falling. One stock's data show anomalous behavior traced to an imbalance between the frequency of price increases and decreases rather than genuine serial dependence, which is largely, but not fully, corrected by rebalancing the binary encoding around each day's median price.

The main new contributions are the systematic use of multiple randomness-test families rather than entropy alone, the discovery of the non-monotonic predictability-aggregation pattern, and a proposal to use the aggregated, whitened binary strings as a model-free source of pseudo-random numbers derived from financial data.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Observations are individual executed trade (tick) prices; consecutive-trade price ratios are converted into a binary digit. These digits are then aggregated over transaction-count 'aggregation levels' from 1 to 100 trades, with multiple overlapping starting offsets sampled at each level to use the full dataset. There is no explicit forecast target; instead the paper studies how randomness properties of the resulting binary strings change as the transaction-count aggregation level increases.

## Data

- **Asset class:** Equities
- **Instruments:** AAPL, MSFT, TSLA, INTC, LLY, SNAP, F, CCL, and the SPY ETF (nine tickers)
- **Venue:** not stated (order data reconstructed from LOBSTER limit order book message files)
- **Period:** 80 trading days between 01-08-2022 and 21-11-2022
- **Granularity:** Nanosecond-timestamped executed order prices (visible and hidden limit-order executions), each trading day spanning 9:30 to 16:00 (390 minutes).

## Features and Measures

- **binary tick-return encoding.** Encodes the ratio of consecutive transaction prices as a single bit (0 if the ratio is below 1, 1 if above 1, no bit if unchanged), producing a binary string that standard randomness-test batteries can be applied to.
- **aggregation level.** A transaction-count aggregation parameter, from 1 to 100, at which price ratios are sampled with multiple overlapping starting offsets, used to study how randomness properties change as more transactions are pooled per observation.
- **ShannonEntropy and KL randomness tests.** Two entropy-based statistical tests, carried over from the authors' prior work, that check whether fixed-length blocks of the binary string are equiprobable (ShannonEntropy) and whether successive symbols are statistically independent even if not equiprobable (KL).

## Method

Each stock-month binary string is treated as a candidate output of a random number generator and evaluated with five families of statistical tests -- frequency, pattern, entropy/complexity, spectral, and random-walk tests -- drawn from the NIST Statistical Test Suite and the Alphabit and Rabbit sub-batteries of TestU01, plus the two custom entropy-based tests. Before applying tests to financial strings, a sanity check runs every test against strings from three independent reference random-number generators at several string lengths; any test that rejects randomness too often on these known-random strings is excluded from use at that string length. Test outcomes are p-values compared against a fixed significance level, and results are summarized across aggregation levels using boxplots of the negative log of the p-value.

## Results

- Randomness generally increases with the transaction-count aggregation level, confirming the authors' earlier entropy-based finding across a much broader set of tests.
- For some tests and stocks, notably AAPL and TSLA (the two highest-turnover names in the sample), predictability persists even at the maximum aggregation level of 100 transactions.
- The Fourier3 spectral test, and several other tests, show a non-monotonic pattern for some stocks: predictability first rises with aggregation level before falling, a pattern not detected by prior entropy-only analyses.
- INTC data show an anomalous case where HammingCorrelation tests indicate increasing, rather than decreasing, predictability with aggregation in August 2022, traced to a strong imbalance between the frequency of price increases and decreases.
- Rebalancing the binary encoding around the daily median price removes most, but not all, of this anomalous INTC pattern; randomness emerges near aggregation level 70 under the balanced encoding, versus non-decreasing predictability without it.
- At an aggregation level of 100, the authors estimate their method can generate on the order of 500 verified entropy bits per trading day for stocks not affected by the persistent-predictability or frequency-imbalance exceptions.

## Limitations

- Several randomness-battery tests could not be run at all because the available string lengths (tens of thousands to about a million bits per month) were too short for tests that require much longer strings.
- The sanity-check exclusion procedure depends on a fixed 2% failure threshold and on the three particular reference random-number generators chosen.
- Reader note: results are reported per individual stock-month rather than through a single pooled statistical test across the whole sample, so the overall significance level across many repeated tests is not formally controlled.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-trading|high frequency trading]]

## Citation

Silvia Onofri, Andrey Shternshis, Stefano Marmi (2025). Emergence of Randomness in Temporally Aggregated Financial Tick Sequences.

DOI: 10.48550/arxiv.2511.17479

Text ingested: `markdown_output/onofri-2025-emergence-randomness-temporally-aggregated-financial-tick.md`, converted from `raw/ofi-event-clock/onofri-2025-emergence-randomness-temporally-aggregated-financial-tick.pdf`.

Coverage of this summary: Read the full markdown file: abstract, introduction, methodology for encoding prices and randomness tests, dataset description, sanity-check procedure, all reported test results and cases, conclusion, and reference list.

Known problems with the input: year from file metadata (no publication year printed for this paper itself; year_hint 2025 from the job file was used).
<!-- AUTHORED REGION END -->