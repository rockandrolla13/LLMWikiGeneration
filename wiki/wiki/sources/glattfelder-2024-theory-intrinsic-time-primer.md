---
authors:
- James B. Glattfelder
- Richard B. Olsen
content_hash: sha256:9bf94a679beb5d287e6bc23a127490424cd0aba3c6de311974e2e1ed56f91698
created: 2026-09-27 01:47:00+00:00
page_id: sources/glattfelder-2024-theory-intrinsic-time-primer
page_type: source
related:
- concepts/intrinsic-time
- concepts/stylized-facts
- concepts/high-frequency-data
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:e53b7c19f906f596e1f87498257c16295be0a24297ccdba995f6195682552b6f
source_path: markdown_output/glattfelder-2024-theory-intrinsic-time-primer.md
source_type: paper
tags:
- intrinsic-time
- directional-change
- scaling-laws
- event-based-time
- complex-systems
- market-microstructure
- clock-intrinsic
- asset-fx
- harvest-relevant
title: 'The Theory of Intrinsic Time: A Primer'
updated: '2026-09-27T01:47:00Z'
uuid: 993577d2-9d01-55db-8b9f-b8223fc0eee1
year: 2024
---

<!-- AUTHORED REGION START -->
# The Theory of Intrinsic Time: A Primer

## Summary

The paper explains why classical, calendar-time analysis of markets may obscure regularities, and surveys the 'intrinsic time' paradigm, an event-based, algorithmically defined notion of time built from directional changes in price, asking what this reframing reveals about financial markets and complex systems generally.

It reviews the history of event-based time in finance, from Mandelbrot and Taylor's early subordination idea through Olsen & Associates' directional-change algorithm, defines the directional-change and overshoot algorithm using a percentage price threshold, and surveys the resulting scaling laws, such as the number of directional changes scaling with the threshold and the average overshoot length approximating the threshold itself, together with a more recent liquidity/volatility decomposition of returns built from these events.

The paper argues that when a time series is analyzed through directional-change and overshoot events rather than fixed intervals, several scaling-law regularities become visible that are otherwise obscured, and that overshoots act as a proxy for liquidity while the count of directional changes acts as a proxy for volatility, letting a return series be decomposed into these two components.

As a primer rather than a new empirical study, its contribution is conceptual synthesis: it frames intrinsic time as evidence that a single universal time does not exist for financial markets, that time is instead observer-dependent and defined by a market's own intrinsic activity, and it connects this idea to broader complexity-science phenomena such as scale-free networks, allometric scaling and Pareto-type distributions as instances of the same organizing principle.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Time ticks are defined algorithmically from the price series itself using a directional-change threshold: starting in an up or down mode, an extremum price is tracked, and a directional-change event is registered once the price retraces by more than the threshold from that extremum, at which point the mode flips and a new extremum is set. After a directional change, each further price move of one threshold-length in the same direction registers an overshoot tick. Multiple thresholds can be applied at once to give a multi-scale, event-based time representation instead of fixed calendar sampling.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** Foreign exchange rates, illustrated in the primer by a cited study covering 13 currency exchange rates; the primer itself presents no new dataset of its own
- **Venue:** not stated
- **Period:** not stated
- **Granularity:** not stated (the paper describes an event-based intrinsic-time construction rather than analyzing a specific fixed-granularity dataset)

## Features and Measures

- **Directional change (DC).** An intrinsic-time event registered when price retraces by more than a chosen percentage threshold from the last extreme price, flipping the tracking mode between up and down.
- **Overshoot (OS).** An intrinsic-time event registered when, after a directional change, price continues moving in the new direction by a further threshold-length; multiple overshoots can occur before the next directional change.
- **Directional-change scaling law.** An empirical power-law-type relationship between the number of directional changes observed in a sample and the directional-change threshold used to define them.
- **Liquidity/volatility decomposition.** A decomposition of a return series, viewed through intrinsic time, into a component driven by overshoot variability, treated as a proxy for liquidity, and a component driven by the count of directional changes, treated as a proxy for volatility.

## Method

The paper is a conceptual and historical review rather than a new empirical study: it does not fit a model to new data but synthesizes prior published results and derivations, including the directional-change/overshoot algorithm, previously published scaling-law estimates, and a return-decomposition identity from earlier work, to argue for intrinsic time as a research paradigm. It judges the validity of the surveyed scaling-law claims by the same criterion used across the complexity-science literature it draws on, namely linearity on a log-log plot, while cautioning that formal statistical tests are needed to avoid misidentifying a scaling law.

## Results

- The number of directional changes in a sample follows a power-law-type relationship with the directional-change threshold, first reported in 1997 and re-derived here from the intrinsic-time algorithm.
- The average overshoot length after a directional change is approximately equal to the threshold itself, motivating the convention of setting the overshoot increment equal to the directional-change threshold.
- A cited 2011 study reported 12 independent scaling laws in foreign exchange data, holding across close to three orders of magnitude and across 13 currency exchange rates.
- A cited 1990 study found a scaling law relating the mean absolute change of log mid-prices, sampled at different time intervals, to the size of that interval.
- A cited biological scaling law states that the total number of heartbeats over a mammal's lifetime is roughly constant across species, at approximately 1.5 times ten to the ninth.
- The paper argues that intrinsic-time analysis reveals structures and regularities in financial time series that are otherwise hidden when using fixed, equidistant time sampling.

## Limitations

- As a primer/review, the paper presents no new empirical test of its own; all quantitative scaling-law and decomposition results are drawn from previously published studies.
- Reader note: no specific dataset, sample period, or venue is analyzed directly in this document, limiting how directly its claims can be checked against underlying data from this paper alone.
- The paper itself cautions that scaling-law claims require rigorous statistical testing to avoid misidentification, a caveat that applies to the broad set of scaling laws it surveys.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/directional-change|Directional Change]]

## Citation

James B. Glattfelder, Richard B. Olsen (2024). The Theory of Intrinsic Time: A Primer.

DOI: 10.48550/arxiv.2406.07354

Text ingested: `markdown_output/glattfelder-2024-theory-intrinsic-time-primer.md`, converted from `raw/ofi-event-clock/glattfelder-2024-theory-intrinsic-time-primer.pdf`.

Coverage of this summary: Read the whole document, including the abstract, introduction, sections on the rise of intrinsic time, scaling laws, and the decoding-complexity discussion, and the reference list.

Known problems with the input: This document is a conceptual/historical primer, not an empirical study; results attributed to prior papers (e.g., the 12 scaling laws, the heartbeat invariant) are as reported in the primer's own text, not independently verified here against the original source papers.
<!-- AUTHORED REGION END -->