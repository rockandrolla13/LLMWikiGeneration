---
content_hash: sha256:127861f6d2987d97ffd08aa87a60f1549dc6a2ca4089b6813be8631323e762dd
created: 2026-09-27 01:47:00+00:00
mind_map_priority: low
page_id: concepts/epps-effect
page_type: concept
related:
- concepts/sampling-clocks
- concepts/realized-covariance
- concepts/trade-clock
- concepts/volume-clock
- concepts/market-microstructure-noise
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
sources:
- sources/chang-2021-epps-effect-under-alternative-sampling-schemes
- sources/gebbie-2026-gabor-epps-uncertainty-principle-traders
tags:
- epps-effect
- correlation
- asynchronous-trading
- sampling
- high-frequency-data
title: Epps Effect
updated: '2026-09-27T01:47:00Z'
uuid: 0616f5ae-a5f9-5936-b94a-8a434442d941
---

<!-- AUTHORED REGION START -->
# Epps Effect

The Epps effect is the fall in measured correlation between two assets as the sampling interval gets shorter. Two assets that move together over an hour can appear almost unrelated over a second.

## Why it happens

Two assets do not trade at the same instants. Over a short interval one may have traded and the other not, so their returns over that interval are mismatched. Delays in how information passes from one asset to the other add to the effect.

## Why it matters here

Any feature that uses more than one asset relies on returns being lined up. Cross-asset imbalance measures and [[concepts/realized-covariance|realized covariance]] are examples. The choice of [[concepts/sampling-clocks|sampling clock]] changes how returns are lined up, so it changes the correlation that is measured.

## Caveats

The effect is partly a measurement artefact and partly a real feature of how markets absorb information. The sources in this wiki differ on how much of it a change of clock can remove.

## Sources in This Wiki

- [[sources/chang-2021-epps-effect-under-alternative-sampling-schemes|The Epps effect under alternative sampling schemes]] (Patrick Chang, Etienne Pienaar, Tim Gebbie, 2021). Compares the Epps correlation-decay effect under calendar, event (trade) and volume time using a Hawkes-process simulation and JSE equity data, finding it emerges linearly under volume time.
- [[sources/gebbie-2026-gabor-epps-uncertainty-principle-traders|A Gabor–Epps uncertainty principle for traders]] (Tim Gebbie, 2026). Uses the Gabor time-frequency uncertainty bound and the clock-dependent Epps effect to derive six rules of thumb for how long a trader must observe cross-asset order flow before treating correlation as tradable.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/realized-covariance|realized covariance]]
- [[concepts/trade-clock|Trade Clock]]
- [[concepts/volume-clock|Volume Clock]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/high-frequency-data|high frequency data]]
<!-- AUTHORED REGION END -->