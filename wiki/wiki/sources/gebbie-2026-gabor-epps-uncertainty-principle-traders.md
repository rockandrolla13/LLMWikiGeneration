---
authors:
- Tim Gebbie
content_hash: sha256:c40d7731c71b16cd103bbd4bb6406ba7acaba904e9f3e9b9356d0def03ffa2e9
created: 2026-09-27 01:47:00+00:00
page_id: sources/gebbie-2026-gabor-epps-uncertainty-principle-traders
page_type: source
related:
- concepts/sampling-clocks
- concepts/order-flow-imbalance
- concepts/market-microstructure
- concepts/market-microstructure-noise
- concepts/order-imbalance
- concepts/high-frequency-trading
- concepts/epps-effect
- entities/tim-gebbie
revision_id: 1
schema_version: 2
source_hash: sha256:d9389469cfd995ecdc97e615aab6e53abbd086e02508e93bf8388725df7a9ee3
source_path: markdown_output/gebbie-2026-gabor-epps-uncertainty-principle-traders.md
source_type: paper
tags:
- market-clocks
- epps-effect
- order-flow
- cross-asset-correlation
- market-microstructure
- uncertainty-principle
- trading-heuristics
- clock-compares
- asset-none
- harvest-relevant
title: A Gabor–Epps uncertainty principle for traders
updated: '2026-09-27T01:47:00Z'
uuid: a3745e04-fcba-5307-8119-5148d360d844
year: 2026
---

<!-- AUTHORED REGION START -->
# A Gabor–Epps uncertainty principle for traders

## Summary

The paper asks how long a trader needs to observe cross-asset order flow before a correlation estimate can be treated as reliable, arguing that the answer depends on which market clock (calendar time, trade/event time, or volume time) is used to sample the data. It applies the classical Gabor time-frequency uncertainty bound, borrowed from signal processing rather than physics, to a windowed cross-asset order-flow or imbalance signal.

The approach combines this Gabor bound with a reaction-diffusion order-book model from companion work to derive a minimum resolvable window (a 'Gabor floor') in terms of shared-refresh, cross-asset-coupling, and imbalance-reversal rates, and then connects it to the Epps effect, the empirical fact that measured correlation rises with the observation window. An attenuation ('resolution') function is used to define more conservative correlation-maturity horizons, at 80% and 90% of the long-run correlation plateau, than the bare Gabor floor.

The main finding, illustrated with two stylised numerical examples (a 'liquid' and a 'less liquid' asset pair with assumed per-second rates), is that the Gabor floor is only a first resolvability scale, while the Epps-based maturity horizon needed before a correlation signal is operationally tradable is substantially longer. Six practical trading rules are proposed from this principle, covering correlation-maturity estimation, diversification claims, clock choice for execution versus accounting, monitoring refresh/coupling rates, clock-mismatch risk, and spectral order-flow diagnostics.

What is new is framing cross-asset correlation estimation explicitly as a time-frequency resolution problem tied to the choice of market clock, rather than treating short-window correlation estimates purely as a noise or estimator-variance issue.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The paper is theoretical rather than an empirical clock choice fitted to one dataset: it treats the observation window as a clock-dependent quantity, contrasting calendar time, event/trade-count time, and volume time as alternative bases on which the Gabor bound and the Epps correlation-emergence curve can be applied. The illustrative numerical examples are stylised calendar-time (per-second) calculations, not fitted to real trade data.

## Data

- **Asset class:** No data (theory or survey)
- **Instruments:** not stated (stylised numerical examples only, described only as a 'liquid pair' and a 'less liquid pair', not tied to named instruments)
- **Venue:** not stated
- **Period:** not stated
- **Granularity:** not stated (illustrative per-second rate examples only, no dataset used)

## Features and Measures

- **Gabor resolution floor.** a minimum observation-window length below which the rate of a market process, such as cross-asset coupling, cannot be reliably resolved from a windowed signal, derived from the classical Gabor time-frequency uncertainty bound applied to a chosen market clock.
- **Weighted imbalance energy.** a liquidity-weighted spectral-power measure of a signed order-flow or imbalance signal in a chosen clock, describing how much of the imbalance signal's power sits at frequencies that are more price-relevant or costly to trade against.
- **Epps attenuation (resolution) function.** a function describing how realised cross-asset correlation rises from near zero toward its long-window plateau value as the observation window widens, used to define a more conservative maturity horizon than the Gabor floor.
- **Correlation maturity horizon.** the window length at which realised correlation reaches a chosen fraction, such as 80% or 90%, of its long-run plateau value, proposed as a threshold below which a cross-asset correlation signal should not be treated as tradable.

## Method

The paper is analytical: it restates the classical Gabor time-frequency uncertainty bound and applies it to a windowed cross-asset order-flow or imbalance signal observed on a chosen market clock (calendar, trade, or volume time). It combines this with a reaction-diffusion order-book model from companion work to derive a Gabor resolution floor in terms of shared-refresh, cross-asset-coupling, and imbalance-reversal rates. It then links this floor to the Epps effect, using an attenuation function motivated by asynchronous-refresh and finite-coupling-response arguments to define more conservative correlation-maturity horizons.

Two stylised numerical examples, a 'liquid' and a 'less liquid' asset pair with assumed per-second refresh, coupling, and imbalance-reversal rates, are worked through to illustrate the resulting Gabor floors and Epps maturity horizons. No empirical order-book data is fitted, estimated, or backtested anywhere in the paper.

## Results

- The Gabor uncertainty bound implies a minimum resolvable window delta_C is at least 1/(2*beta), where beta is the slowest of the relevant shared-refresh, cross-asset-coupling, and imbalance-reversal rates.
- In the stylised liquid-pair example the slowest relevant rate is 2 per second, giving a Gabor floor of 0.25 seconds; in the less-liquid-pair example the slowest rate is 0.15 per second, giving a Gabor floor of about 3.3 seconds.
- Because the Epps attenuation function reaches only about 0.80 and 0.90 of its long-run plateau after roughly 5 and 10 multiples of the relevant rate, the paper's proposed maturity horizons exceed the Gabor floor: about 2.5 and 5.0 seconds in the liquid example versus about 33.3 and 66.7 seconds in the less liquid example.
- The paper proposes six practical trading rules, including estimating a per-pair correlation maturity horizon, not treating low short-horizon correlation as true diversification, executing in market-activity time while accounting for risk in calendar time, monitoring refresh and coupling rates for deterioration, pricing in clock-mismatch risk, and using spectral order-flow diagnostics.
- The argument concludes that realised cross-asset correlation depends on the chosen measurement clock and the order-flow mechanism generating the dependence, not on the assets alone.

## Limitations

- The author states explicitly that the numerical examples are stylised dimensional illustrations, not calibrated or empirically estimated trading parameters.
- No empirical order-book or trade data is analyzed in this paper; the framework is illustrated only with assumed per-second rates for hypothetical liquid and less-liquid pairs.
- The paper explicitly disclaims that its 'uncertainty principle' is a theorem or an empirical law, describing it instead as a signal-processing analogy.
- Reader note: because no real dataset or backtest is used, the six proposed trading rules are not validated against realized trading performance in this paper.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/epps-effect|Epps Effect]]
- [[entities/tim-gebbie|Tim Gebbie]]

## Citation

Tim Gebbie (2026). A Gabor–Epps uncertainty principle for traders.

DOI: 10.48550/arxiv.2607.04130

Text ingested: `markdown_output/gebbie-2026-gabor-epps-uncertainty-principle-traders.md`, converted from `raw/ofi-event-clock/gebbie-2026-gabor-epps-uncertainty-principle-traders.pdf`.

Coverage of this summary: Read the whole markdown file, from abstract through conclusion, references, and both stylised example tables.

Known problems with the input: year from file metadata.
<!-- AUTHORED REGION END -->