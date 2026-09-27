---
authors:
- James B. Glattfelder
- Anton Golub
content_hash: sha256:e6323b12ec36b74508666920ef29834108582045fd496ba0ac926506b318b506
created: 2026-09-27 01:47:00+00:00
page_id: sources/glattfelder-2022-bridging-gap-decoding-intrinsic-nature-time
page_type: source
publication_venue: Working paper
related:
- concepts/sampling-clocks
- concepts/stylized-facts
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/intrinsic-time
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:235163ce6a2de9c29c060eb2d0dfd40b993d3b8fab1ea112e196e115cd228ca3
source_path: markdown_output/glattfelder-2022-bridging-gap-decoding-intrinsic-nature-time.md
source_type: paper
tags:
- intrinsic-time
- directional-change
- scaling-laws
- fx-microstructure
- tick-data
- volatility-decomposition
- liquidity
- clock-compares
- asset-multi
- harvest-relevant
title: 'Bridging the Gap: Decoding the Intrinsic Nature of Time in Market Data'
updated: '2026-09-27T01:47:00Z'
uuid: dc71b2b4-e110-5cc9-add8-45914b6b3ed5
year: 2022
---

<!-- AUTHORED REGION START -->
# Bridging the Gap: Decoding the Intrinsic Nature of Time in Market Data

## Summary

The paper asks how intrinsic time -- an event-based clock for price series built from directional changes and overshoots -- relates mathematically to ordinary physical (calendar) time statistics, noting that prior intrinsic-time literature lacked this explicit link.

Modelling the price process as Brownian motion with volatility sigma, the authors use an identity for the variance of a randomly stopped sum (Wald's equation, generalised as the Blackwell-Girshick equation) to derive an equation linking the physical-time squared return over an interval to two intrinsic-time quantities: the expected number of directional changes for a chosen threshold, and the variance of the overshoot beyond that threshold. They also propose a new empirical scaling law for the variance of the overshoot as a function of the threshold, alongside three scaling laws already established in the intrinsic-time literature, and show that combining all of these scaling laws yields an invariant quantity that no longer depends on the physical-time interval or the directional-change threshold.

The derived relationship and the invariant are evaluated on one simulated Brownian-motion path and on two tick-by-tick currency series, a crypto pair (ETH/USDT) and a fiat pair (USD/JPY). For Brownian motion and the crypto pair the invariant is approximately constant across a grid of thresholds, supporting the derived identity, but for the fiat pair the identity appears to break down unless an extra scaling constant is introduced.

The main contribution is the explicit analytic bridge between physical-time and intrinsic-time statistics and the resulting decomposition of physical-time squared returns into a volatility component, measured by the directional-change count, and a liquidity component, measured by overshoot variability, together with the new overshoot-variance scaling law.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The paper contrasts physical time, where prices are sampled at fixed calendar intervals, with intrinsic (directional-change) time, where the clock advances only when the price reverses by a fixed threshold from the last local extreme, with any further move in the same direction beyond that threshold recorded as an overshoot. It derives an identity linking the physical-time squared return over a calendar interval to the intrinsic-time count of directional changes and the variance of overshoots for a matched threshold, rather than defining any explicit forecast horizon.

## Data

- **Asset class:** Several asset classes
- **Instruments:** A simulated Brownian motion path; the ETH/USDT cryptocurrency exchange rate; and the USD/JPY fiat currency exchange rate.
- **Venue:** not stated (the tick-by-tick market data source is not named)
- **Period:** Brownian motion: one simulated realisation spanning close to 181 days. ETH/USDT: 2021-03-01 00:00:00 to 2021-04-15 23:59:59. USD/JPY: 2013-01-01 00:00:00 to 2013-05-31 23:59:59.
- **Granularity:** Tick-by-tick; the simulated Brownian motion is spaced at one-second intervals, while the two currency series are recorded at the observation (trade/quote) level.

## Features and Measures

- **Directional change (DC).** A reversal in price of at least a fixed threshold measured from the last local price extreme, used as the basic event that advances intrinsic time.
- **Overshoot.** The additional price move, beyond the directional-change threshold, that continues in the same direction after a directional change has been registered, before the next reversal.
- **Number of directional changes.** The count of directional-change events for a chosen threshold over a physical-time window, used in this paper as a proxy for the price process's volatility.
- **Overshoot variability.** The variance of the overshoot length around its mean for a given threshold, used in this paper as a proxy for market illiquidity.
- **Bridge invariant.** A quantity combining the squared-return scaling law (physical time) with the directional-change-count and overshoot-variance scaling laws (intrinsic time), which the authors show should stay constant across different choices of the calendar interval and the directional-change threshold if the bridging identity holds.

## Method

Assuming the price process follows Brownian motion, the authors express the physical-time squared return as a compound sum of intrinsic-time increments and apply an identity for the variance of a randomly stopped sum (Wald's equation / the Blackwell-Girshick equation) to derive a relationship between the squared return and the number of directional changes and the variance of overshoots. For each of the three time series they then estimate, by fitting a power law of the form f(x) = alpha times x to the power E across a grid of thresholds, four scaling relations: squared return versus the calendar interval, overshoot variance versus the directional-change threshold, number of directional changes versus the threshold, and average overshoot versus the threshold. They evaluate whether the resulting combination of these fitted scaling laws is invariant across the grid of calendar intervals and thresholds. No hypothesis tests, backtests, or out-of-sample forecast evaluation are performed; validation is a descriptive comparison of the fitted invariant against a constant, supplemented by charts.

## Results

- For Brownian motion, the squared-return-versus-interval scaling exponent is estimated at 1.0031, close to the theoretical value of 1, and the other three scaling-law exponents are similarly close to their theoretical values.
- The Brownian-motion bridge invariant averages 2.5585 times 10 to the power -9 across all threshold combinations, with a standard deviation of 4.100 times 10 to the power -11, approximately constant as the bridging identity predicts.
- For ETH/USDT the invariant is also approximately constant, at about 2.2094 times 10 to the power -8 with standard deviation 1.0552 times 10 to the power -9, though with more scatter than the Brownian-motion case.
- For USD/JPY the bridging identity appears to break down; the authors show that inserting an extra scaling factor of about 0.7235 restores an approximate match between the two sides of the invariant.
- A new empirical scaling law is proposed for the overshoot variance as a function of the directional-change threshold, with an estimated exponent of 1.9088 for Brownian motion, 1.7249 for ETH/USDT, and 1.9516 for USD/JPY.
- The paper concludes that physical-time squared returns can be decomposed into an intrinsic-time volatility component (the directional-change count) and an intrinsic-time liquidity component (the overshoot variability).

## Limitations

- Only one simulated Brownian-motion path and two currency pairs are analysed; no equities, rates, or bond instruments are tested.
- The USD/JPY result requires an extra, empirically fitted scaling factor whose theoretical justification the authors leave to future work.
- The authors state that further work is needed to establish the accuracy of the empirical relationships and to justify introducing the extra scaling factor.
- Reader note: the paper is explicitly described as a working paper and reports no formal statistical significance tests around the fitted exponents or the invariant estimates.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/directional-change|Directional Change]]

## Citation

James B. Glattfelder, Anton Golub (2022). Bridging the Gap: Decoding the Intrinsic Nature of Time in Market Data. Working paper.

DOI: 10.2139/ssrn.4308220

Text ingested: `markdown_output/glattfelder-2022-bridging-gap-decoding-intrinsic-nature-time.md`, converted from `raw/ofi-event-clock/glattfelder-2022-bridging-gap-decoding-intrinsic-nature-time.pdf`.

Coverage of this summary: Read the full markdown file end to end, including the introduction, the review of directional-change and overshoot scaling laws, the derivation of the physical-time/intrinsic-time bridge identity, the scaling-and-invariance section, the empirical analysis on Brownian motion and the two currency series, and the conclusion.

Known problems with the input: The paper is self-described in its own text only as 'this working paper', with no journal, conference, or working-paper-series name printed; 'Working paper' is used as the venue on that basis; Most inline equations are shown in the markdown only as 'picture intentionally omitted', so the derivations are described qualitatively rather than reproduced in symbol form.
<!-- AUTHORED REGION END -->