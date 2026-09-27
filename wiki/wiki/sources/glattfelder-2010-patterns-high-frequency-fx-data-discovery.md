---
authors:
- J.B. Glattfelder
- A. Dupuis
- R.B. Olsen
content_hash: sha256:fc75d008cebc8aa15dc2cbeaed2e43b511036e46b59069c74c3f26ee609f59d2
created: 2026-09-27 01:47:00+00:00
page_id: sources/glattfelder-2010-patterns-high-frequency-fx-data-discovery
page_type: source
related:
- concepts/intrinsic-time
- concepts/stylized-facts
- concepts/high-frequency-data
- concepts/bid-ask-spread
- concepts/market-microstructure
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:d3c3a29c24c3159bc5af476896647ac03565d731dff37bb4f25d06245a5934b3
source_path: markdown_output/glattfelder-2010-patterns-high-frequency-fx-data-discovery.md
source_type: paper
tags:
- scaling-laws
- fx-microstructure
- directional-change
- intrinsic-time
- tick-data
- stylized-facts
- clock-intrinsic
- asset-fx
- harvest-relevant
title: 'Patterns in high-frequency FX data: Discovery of 12 empirical scaling laws'
updated: '2026-09-27T01:47:00Z'
uuid: e7c59e1d-4c76-5e13-810f-f6f8584c45f6
year: 2010
---

<!-- AUTHORED REGION START -->
# Patterns in high-frequency FX data: Discovery of 12 empirical scaling laws

## Summary

The paper looks for new stylised, scale-invariant patterns in foreign-exchange price data beyond the one long-known scaling law relating average absolute price change to the size of the sampling time interval. Its central methodological move is to replace fixed calendar-time sampling with an event-based, 'intrinsic time' approach built around directional-change events, where a fixed percentage price move away from the last high or low triggers a reversal event and splits the price path into directional-change and overshoot segments.

Using five years of tick-by-tick bid/ask data for 13 currency pairs, the authors detect directional-change and price-move events across a grid of percentage thresholds and time intervals, then fit linear (log-log) relationships between the size of these thresholds/intervals and quantities such as tick counts, waiting times, and cumulative price moves. They cross-check the fitted laws against each other for internal consistency and compare all of them against a simple Gaussian random walk benchmark.

The main finding is 12 independent new scaling laws (plus 6 further ones derivable from these together with the two previously known laws) that hold across nearly three orders of magnitude of thresholds and across all 13 currency pairs. The laws let the authors estimate the length of the price 'coastline' (the sum of price moves at a given resolution), which turns out to be far longer than intuition suggests, and they show that a plain Gaussian random walk reproduces some but not all of these patterns.

What is new is both the number of independent scaling laws found and the event-based, directional-change lens used to find them, which the authors argue substantially extends the existing catalogue of FX stylised facts and narrows the space of theoretical models that could explain how the market behaves.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

The paper's core method is event-based: it detects 'directional changes' whenever price reverses from its last high or low extreme by a fixed percentage threshold, and defines 'intrinsic time' as ticking only at these directional-change events instead of at fixed calendar intervals. Most of the paper's new scaling laws (tick counts, price-move counts, and the total-move/directional-change/overshoot decomposition) are expressed as functions of this directional-change threshold. The paper also revisits an earlier scaling law defined over fixed physical-time intervals for comparison, but treats the threshold-triggered intrinsic clock as central to its new results.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** 13 currency pairs: AUD-JPY, AUD-USD, CHF-JPY, GBP-CHF, GBP-JPY, GBP-USD, EUR-AUD, EUR-GBP, EUR-CHF, EUR-JPY, EUR-USD, USD-CHF, USD-JPY. Some pairs (e.g. GBP-JPY) are synthetic cross-rates derived from two other quoted pairs.
- **Venue:** not stated
- **Period:** December 1, 2002 to December 1, 2007 (five years of tick data); results are also compared against a simulated Gaussian random walk benchmark
- **Granularity:** Tick-by-tick indicative bid/ask quote data, filtered to drop repeated ticks with the same price as the previous tick

## Features and Measures

- **Directional change (DC).** An event triggered when price moves by a fixed percentage threshold away from the last high or low extreme in the current up/down mode; DC events define the paper's 'intrinsic time' clock and split the price path into directional-change and overshoot segments.
- **Overshoot (OS).** The continuation of a price move beyond the point where the prior directional change was confirmed, measured from that confirmation point to the next extreme before the mode reverses again.
- **Tick (price-move unit).** A price move whose absolute size exceeds a small fixed threshold (0.02% in this study), used to count how many such moves occur during a larger price move of a given size.
- **Coastline.** The cumulative sum of directional-change or total-move price changes over a period, used to measure the total distance travelled by price at a given threshold resolution.

## Method

Price is defined as the arithmetic mean of bid and ask, and directional-change events are detected with an algorithm that tracks a running high or low extreme and flips 'mode' whenever price reverses from that extreme by more than a fixed percentage threshold. Repeating this detection across a grid of 250 logarithmically spaced price-move thresholds (from 0.01% to 5.05%) and, for time-interval-based laws, 245 logarithmically spaced intervals (from 20 seconds to about 46 days) produces the raw observations behind each scaling law.

For each law the authors fit a linear relationship between the logarithm of the measured quantity and the logarithm of the threshold or time interval using a standard linear-model fit, and also test a quadratic specification to check for systematic curvature; the fitted slope and intercept give the scaling-law's exponent and multiplicative constant, reported per currency pair with an adjusted R-squared. A simulated Gaussian random walk with fixed one-second time steps is used throughout as a benchmark for which patterns are, or are not, reproduced by a simple stochastic model.

The paper also cross-checks the discovered laws algebraically against each other (for example relating the price-move-count law to the average-time-between-moves law) to test internal consistency, and uses the total-move decomposition law to estimate the length of the annualised price coastline at several threshold resolutions.

## Results

- The study reports 12 independent new scaling laws, plus 6 further ones derivable from these and from two previously known laws, holding across all 13 currency pairs and over close to three orders of magnitude of thresholds.
- Considering directional-change thresholds of 1% and 5%, the average annualised coastline length was 186% and 34.8% respectively; decreasing the resolution threshold 500-fold increased the coastline length by a factor of 650, versus only 220 for the Gaussian random walk benchmark.
- Accounting for transaction costs, the coastline measured at a 0.05% threshold (a move that occurs on average every 15 minutes) implied an average daily price move of 6.4%.
- For the scaling law relating quadratic mean price move to time interval, the measured average exponent across currency pairs was 0.457, below the value of 0.500 measured for the Gaussian random walk benchmark of the same law.
- On average, a directional change is followed by an overshoot of similar magnitude, making the resulting total move roughly twice the directional-change threshold, while also containing about twice as many ticks and taking about twice as long to unfold as the directional-change segment alone.
- The Gaussian random walk benchmark's average maximal price move within a fixed time interval was found to be roughly eight times larger than in the empirical FX data, and the benchmark's coastline expanded less under finer thresholds than the real data did.
- Cross-checking the fitted laws algebraically against each other for EUR-USD showed agreement to within about 0.5%, supporting the internal consistency of the parameter estimates.

## Limitations

- The paper does not fit or claim any particular probability distribution for the underlying quantities; it reports scaling-law relations only for their average and cumulative values.
- Most laws deviate noticeably for EUR-CHF relative to the other 12 currency pairs, without a full explanation given for this discrepancy.
- The Gaussian random walk benchmark uses an arbitrarily chosen fixed one-second time step, so some of its differences from the empirical data on time-sensitive laws could reflect this modelling choice rather than a genuine market feature.
- The authors explicitly state the study is not related to the analysis of lead-lag relationships between currency pairs.
- Reader note: several of the 13 pairs are synthetically constructed cross-rates derived from two other quoted series, which could introduce shared statistical structure across those particular pairs.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/directional-change|Directional Change]]

## Citation

J.B. Glattfelder, A. Dupuis, R.B. Olsen (2010). Patterns in high-frequency FX data: Discovery of 12 empirical scaling laws.

DOI: 10.1080/14697688.2010.481632

Text ingested: `markdown_output/glattfelder-2010-patterns-high-frequency-fx-data-discovery.md`, converted from `raw/ofi-event-clock/glattfelder-2010-patterns-high-frequency-fx-data-discovery.pdf`.

Coverage of this summary: Read the full paper text: abstract, introduction, the enumeration and cross-checking of scaling laws (sections 2.1-2.3), the methods and data section (3), and the conclusion. The appendix tables of per-currency parameter estimates were skimmed rather than read line by line, since they repeat values already summarized in Table 1 and the main text.

Known problems with the input: No publication year is printed anywhere in the visible text; year taken from the job file's year_hint (2010).
<!-- AUTHORED REGION END -->