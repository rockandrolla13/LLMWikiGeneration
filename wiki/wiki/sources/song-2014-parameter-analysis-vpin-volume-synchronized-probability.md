---
authors:
- Jung Heon Song
- Kesheng Wu
- Horst D. Simon
content_hash: sha256:5b28b9c423ef56a8ea80da38133b88898e345ccd41deed64761b90cb19e1d2c1
created: 2026-09-27 01:47:00+00:00
page_id: sources/song-2014-parameter-analysis-vpin-volume-synchronized-probability
page_type: source
publication_venue: Lawrence Berkeley National Laboratory
related:
- concepts/volume-clock
- concepts/informed-trading
- concepts/trade-classification
- concepts/order-flow
- concepts/adverse-selection
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/vpin
- entities/kesheng-wu
revision_id: 1
schema_version: 2
source_hash: sha256:eb1076ecd78b79eae1411b4265c95f669cecea8e8a8e12f4e57d5a6789283467
source_path: markdown_output/song-2014-parameter-analysis-vpin-volume-synchronized-probability.md
source_type: paper
tags:
- vpin
- informed-trading
- flash-crash
- futures
- parameter-optimization
- sensitivity-analysis
- clock-volume
- asset-futures
- harvest-core
title: Parameter Analysis of the VPIN (Volume synchronized Probability of Informed
  Trading) Metric
updated: '2026-09-27T01:47:00Z'
uuid: 31918c89-1c5e-5848-8070-c7f2bd0a9d68
year: 2014
---

<!-- AUTHORED REGION START -->
# Parameter Analysis of the VPIN (Volume synchronized Probability of Informed Trading) Metric

## Summary

VPIN (volume synchronized probability of informed trading) is a measure of order-flow toxicity proposed to explain the liquidity breakdown before the 2010 Flash Crash. Computing it requires choosing several free parameters, and an earlier brute-force search of about 16,000 parameter combinations across 97 futures contracts had reduced its average false positive rate (FPR) from 20% to 7%. This paper attempts a more systematic search for better parameter choices and a better understanding of which parameters actually matter.

The authors define VPIN through six free parameters: the nominal bar price, the bulk volume classification (BVC) scheme used to split volume into buy/sell, buckets per day, a probability threshold, a support window, and an event horizon. They search this parameter space with the NOMAD blackbox optimizer (the Mesh Adaptive Direct Search algorithm, with and without its Variable Neighborhood Search extension), run separately for each of five candidate nominal-price strategies because of their differing computational cost. Once near-optimal regions are found, global sensitivity analysis is performed with the UQTK toolkit, which fits a polynomial-chaos surrogate model and computes Sobol variance-based sensitivity indices over successively narrower parameter bounds.

NOMAD without the neighborhood-search extension found parameter sets with FPR as low as about 2.44%-2.58%; adding the neighborhood-search extension generally produced FPRs in the 3-5% range and did not fully resolve inconsistency across different optimization starting points, so a single global optimum was not confirmed. Sensitivity analysis shows that under wide parameter bounds the number of buckets per day and the support window dominate FPR variance, but once bounds are narrowed toward the best solutions found, the event horizon and support window become the dominant parameters, while pricing strategy and the probability threshold (once kept above about 0.98) contribute comparatively little.

The contribution is turning an earlier ad hoc, brute-force parameter search into a systematic optimization-plus-sensitivity-analysis pipeline, and giving concrete recommended parameter ranges intended for practical use of VPIN: mean price as the nominal price, buckets-per-day near 1836, a support window near 0.0478, an event horizon near 0.0089, and a threshold kept above 0.98 but not too close to 1.

## Clock and Sampling

**Volume clock: one observation per unit of volume traded.**

See [[concepts/volume-clock|Volume Clock]].

VPIN groups trades into equal-volume buckets, described as running on 'volume time'; each bucket contains a fixed number of smaller bars (30 bars per bucket throughout this study). A 'VPIN event' is triggered when the normalized VPIN value crosses a chosen threshold from below, and the prediction horizon is a fixed subsequent time duration (the event horizon) over which realized volatility (Maximum Intermediate Return) is compared against a baseline range to classify the event as a true or false positive.

## Data

- **Asset class:** Futures
- **Instruments:** 97 of the most actively traded futures contracts; detailed sensitivity analysis focuses on the 5 largest by volume (S&P 500 E-mini, Euro FX, Nasdaq 100, Light Crude NYMEX, and Dow Jones E-mini)
- **Venue:** not stated
- **Period:** A 67-month period covering 2007 to 2012
- **Granularity:** Trade-level data aggregated into volume bars and then into equal-volume buckets (30 bars per bucket).

## Features and Measures

- **VPIN (volume synchronized probability of informed trading).** A measure of order-flow imbalance computed by classifying volume within volume buckets as buy- or sell-initiated and averaging the buy-sell imbalance over a support window of buckets.
- **Bulk Volume Classification (BVC).** A method assigning a fraction of each bar's volume to buys and the rest to sells based on the normalized sequential price change, using a normal or Student-t distribution function, instead of classifying whole trades as in the tick rule.
- **VPIN event and false positive rate (FPR).** A VPIN event is declared when the normalized VPIN value crosses a chosen threshold from below and persists for a fixed event-horizon duration; it is a false positive if realized volatility during that horizon falls within a normal range, and FPR is the ratio of false positive events to total events, pooled across contracts.

## Method

The paper treats minimizing average FPR over the 97 futures contracts as a blackbox optimization problem, solved with NOMAD's Mesh Adaptive Direct Search (MADS) algorithm, run separately for each of five candidate nominal-price strategies because of their differing computational cost. A Variable Neighborhood Search (VNS) extension is also tested as a way to escape local minima. Once near-optimal parameter regions are found, global sensitivity analysis is performed with UQTK, which builds a polynomial-chaos-expansion surrogate model over the free parameters and computes Sobol variance-based sensitivity indices, repeated over successively narrower parameter bounds centered on the best NOMAD solutions.

## Results

- An earlier brute-force search of about 16,000 parameter combinations across 97 futures contracts had reduced the average FPR from 20% to 7%.
- NOMAD optimization without the neighborhood-search extension found parameter combinations with FPR of 2.44% and 2.58%.
- Enabling the Variable Neighborhood Search (VNS) strategy generally produced FPRs in the 3-5% range and did not remove inconsistency in solutions found from different starting points.
- Reading raw futures data and constructing volume bars were the most time-consuming computational steps; using weighted-median as the nominal price made bar construction take as much as 7 times longer than using closing, mean, or weighted-mean prices.
- Sensitivity analysis shows buckets-per-day and the support window dominate FPR variance under wide parameter bounds, but as bounds are narrowed toward the best NOMAD solutions the event horizon and support window become the dominant parameters.
- Within the narrowed bounds near the best solutions, the choice of pricing strategy and the probability threshold (once above about 0.98) contribute minimally to FPR variance.
- The authors recommend mean price as the nominal price, buckets-per-day near 1836, a support window near 0.0478, an event horizon near 0.0089, and a threshold kept above 0.98 but not too close to 1.

## Limitations

- The authors state they were not able to find a single global minimizer of FPR; different NOMAD starting points converge to different, only loosely consistent parameter combinations.
- Reader note: sensitivity conclusions depend on the researcher-chosen parameter bounds -- parameters such as buckets-per-day and the threshold shift from dominant to negligible depending on how tightly the search bounds are set around known good solutions.
- Computation for some parameter searches hit a 72-hour job-time limit on the computing cluster used and had to be restarted, which the authors note is less efficient than an uninterrupted run.

## Related

- [[concepts/volume-clock|Volume Clock]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/order-flow|order flow]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/vpin|VPIN]]
- [[entities/kesheng-wu|Kesheng Wu]]

## Citation

Jung Heon Song, Kesheng Wu, Horst D. Simon (2014). Parameter Analysis of the VPIN (Volume synchronized Probability of Informed Trading) Metric. Lawrence Berkeley National Laboratory.

DOI: 10.2139/ssrn.2427086

Text ingested: `markdown_output/song-2014-parameter-analysis-vpin-volume-synchronized-probability.md`, converted from `raw/ofi-event-clock/song-2014-parameter-analysis-vpin-volume-synchronized-probability.pdf`.

Coverage of this summary: Read the full markdown file: introduction and Flash Crash background, VPIN definition and free parameters, computational cost analysis, NOMAD/MADS and VNS optimization sections, UQTK sensitivity analysis, results tables, conclusion, and reference list.
<!-- AUTHORED REGION END -->