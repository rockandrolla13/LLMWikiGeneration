---
authors:
- Antoine Bambade
content_hash: sha256:59a7193c82d9d053d244c6ce766f16188339bdc03695cce74c4dfd68f4337c46
created: 2026-09-27 01:47:00+00:00
page_id: sources/bambade-2019-new-way-compute-probability-informed-trading
page_type: source
publication_venue: Journal of Mathematical Finance, 2019, 9, 637-666
related:
- concepts/sampling-clocks
- concepts/informed-trading
- concepts/adverse-selection
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/volume-clock
- concepts/vpin
revision_id: 1
schema_version: 2
source_hash: sha256:22c20044c0d19b99f58f17cfa32a6fb099dc8d35fec643df9de08cd1e86ed053
source_path: markdown_output/bambade-2019-new-way-compute-probability-informed-trading.md
source_type: paper
tags:
- probability-of-informed-trading
- vpin
- volume-clock
- time-clock
- flow-toxicity
- flash-crash
- clock-compares
- asset-simulated
- harvest-relevant
title: A New Way to Compute the Probability of Informed Trading
updated: '2026-09-27T01:47:00Z'
uuid: cc71901a-7cdc-52b4-a445-f4128019d68e
year: 2019
---

<!-- AUTHORED REGION START -->
# A New Way to Compute the Probability of Informed Trading

## Summary

The paper revisits the theoretical foundations of the Probability of Informed Trading (PIN) and its widely used approximation, Volume-Synchronized PIN (VPIN). Prior critics had already found VPIN empirically sensitive to its starting point, to the trade-classification rule used, and to how average daily volume is defined; this paper instead attacks the theory, arguing that VPIN cannot approximate PIN because PIN was built in a fixed-time, random-volume (time-clock) framework while VPIN was built in a fixed-volume, random-time (volume-clock) framework, and that the two sets of assumptions cannot both hold at once.

The author first re-derives the PIN model of Easley, Kiefer, O'Hara and Paperman from its underlying tree of informed/uninformed Poisson order arrivals, recovering the bid-ask spread and PIN formula from first principles. It then examines the first-order approximation, credited to a result by Katti on the moments of the absolute difference of two Poisson variables, that the original VPIN derivation relies on to approximate the expected buy-sell imbalance; the paper shows this reference result requires the two Poisson intensities to be linked by a specific ratio condition that does not hold in the PIN model's general setting, and instead computes the exact expected imbalance for the time-clock model using modified Bessel functions, showing where and when the first-order approximation is accurate versus inaccurate as a function of the relative sizes of the informed and uninformed arrival rates. Simulation experiments across three parameter regimes illustrate both the closeness and the failure modes of the approximation.

The author then derives a new, exact way to compute the PIN in the time-clock framework directly from the first three moments (mean, variance, skewness) of observed buy or sell trade volume over an arbitrary observation window, avoiding the volume-clock heuristic on which VPIN depends. In further simulations this new estimator (labelled NPIN) tracks the true PIN more closely than VPIN's first-order approximation across all three tested parameter regimes.

What is new is treating VPIN's volume-clock assumptions and PIN's time-clock assumptions as genuinely incompatible framings rather than as approximation error to be tuned away, and supplying an exact, moment-based PIN estimator that stays inside PIN's original time-clock framework instead of substituting a volume clock.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

PIN is modelled in continuous time over a fixed trading period, with informed and uninformed buy and sell orders arriving as independent Poisson processes, so that the trading period is fixed and the resulting trade volume is random (a time-clock framework). VPIN instead aggregates trades into fixed-volume buckets and treats each bucket as an information period, so that volume is fixed and the time to fill a bucket is random (a volume-clock framework). The paper's central methodological point is that these two clocks embody different, mutually incompatible assumptions, and it derives its new PIN estimator by staying entirely within the original time-clock framework, using the moments of trade volume observed over an arbitrary fixed time window rather than over a fixed-volume bucket.

## Data

- **Asset class:** Simulated data
- **Instruments:** not stated (no real market dataset is used; all results are derived analytically or from simulated Poisson order-arrival processes)
- **Venue:** not stated
- **Period:** not stated
- **Granularity:** simulated Poisson buy/sell order-arrival processes under three parameter regimes

## Features and Measures

- **PIN (Probability of Informed Trading).** The proportion of trading activity attributable to informed traders, derived from a tree model in which Nature first decides whether an information event occurs and, if so, whether it is good or bad news, and informed and uninformed traders then submit Poisson-arrival buy and sell orders.
- **VPIN (Volume-Synchronized Probability of Informed Trading).** An approximation of PIN computed from the order imbalance observed within fixed-volume trade buckets, intended to be an easier-to-compute, real-time proxy for PIN.
- **New exact PIN estimator (NPIN).** An estimator of PIN computed from the mean, variance and skewness of buy (or sell) trade volume observed over an arbitrary fixed time window, derived to be exact within the original time-clock PIN framework rather than relying on VPIN's volume-clock approximation.

## Method

The paper is primarily analytical: it re-derives the PIN model's bid/ask/spread expressions from the underlying tree of Poisson arrival processes, computes the exact expectation of the buy-sell imbalance using modified Bessel functions (invoking results by Katti and by Ramasubban), and derives an asymptotic first-order expansion of that exact expectation to show when the original VPIN heuristic is and is not accurate. It then derives the new NPIN estimator from the first three moments of observed trade volume.

All results are checked against simulation: Poisson buy/sell processes are generated directly from chosen informed and uninformed arrival-rate parameters, and the empirical order imbalance, the exact PIN, the first-order approximation, and (in the second set of experiments) the new NPIN estimator are compared graphically across three parameter regimes chosen to span cases where informed-order and uninformed-order rates differ by orders of magnitude or are of similar size.

## Results

- The paper re-derives the exact PIN formula in continuous (time-clock) form and shows its numerator equals the product of the informed-event probability and the informed order-arrival rate, contrasting this with the first-order approximation used to derive VPIN, which the paper shows is not always accurate.
- It shows that the reference result the original VPIN derivation relies on (Katti's result on the moments of the absolute difference of two Poisson variables) requires the two Poisson intensities to be linked by a specific ratio, a condition that does not hold in the PIN model's general setting.
- It argues that VPIN's volume-clock bucketing implicitly treats the time to fill a bucket as random, while the original PIN model treats the trading period as fixed and volume as random, so the two framings cannot both be assumed to hold for the same quantity at once.
- A new exact PIN estimator (NPIN) is derived from the first three moments (mean, standard deviation, skewness) of buy or sell trade volume over an arbitrary observation window, rather than from the volume-clock heuristic.
- In simulation with the uninformed-order rate fixed at 100 and the informed-order rate set to 10000, 20000 or 30000, the new NPIN formula tracks the true PIN closely, more closely than VPIN's first-order approximation.
- In a regime where the informed-order rate is fixed at 10000 and the uninformed-order rate takes values 10000, 2000 or 30000, VPIN is shown to slightly over-estimate the true PIN.
- Each simulated point in the first experiment set averaged 10,000 Poisson draws; the second experiment set generated 1,000,000 draws split into 100 consecutive blocks of 10,000 to estimate the mean, standard deviation and skewness used by the new formula.

## Limitations

- The paper is entirely analytical and simulation-based; the author explicitly proposes testing the new formula against real trading data as future work rather than doing so here.
- Reader note: with no empirical market dataset used, it is not shown whether the new estimator's theoretical advantage over VPIN survives real trade classification noise, non-Poisson clustering, or intraday seasonality.
- The author notes that one of the three simulated parameter regimes (informed and uninformed rates of similar magnitude) is described as trickier and in need of further study.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/volume-clock|Volume Clock]]
- [[concepts/vpin|VPIN]]

## Citation

Antoine Bambade (2019). A New Way to Compute the Probability of Informed Trading. Journal of Mathematical Finance, 2019, 9, 637-666.

DOI: 10.4236/jmf.2019.94032

Text ingested: `markdown_output/bambade-2019-new-way-compute-probability-informed-trading.md`, converted from `raw/ofi-event-clock/bambade-2019-new-way-compute-probability-informed-trading.pdf`.

Coverage of this summary: Read the whole markdown file end to end, including the introduction, the PIN time-clock derivation, the analysis of the first-order approximation and the volume-clock paradigm, the new PIN formula derivation, both simulation sections, and the conclusion.

Known problems with the input: A large share of the mathematical derivations were rendered by the PDF-to-markdown converter as omitted picture placeholders, and several Greek-letter parameter symbols (the informed and uninformed Poisson arrival-rate symbols in particular) did not survive the conversion and appear as blank or garbled characters in the surviving text, so this summary refers to those parameters in words rather than by symbol.
<!-- AUTHORED REGION END -->