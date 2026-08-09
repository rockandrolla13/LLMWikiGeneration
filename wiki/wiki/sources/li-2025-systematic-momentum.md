---
title: 'Systematic Momentum: A New Class of Price Patterns'
page_id: sources/li-2025-systematic-momentum
page_type: source
source_path: markdown_output/li-yuan-zhou-systematic-momentum.md
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Sophia Zhengzi Li
- Peixuan Yuan
- Guofu Zhou
year: 2025
venue: Management Science (Articles in Advance, published online 25 November 2025)
tags:
- momentum
- intraday
- systematic-component
- limits-to-arbitrage
- anomalies
sources: []
related:
- concepts/cross-sectional-momentum
- concepts/high-frequency-data
- concepts/limits-to-arbitrage
- concepts/risk-vs-mispricing
mind_map_priority: high
schema_version: 2
uuid: d96b0f0e-4a2c-54e7-b69f-c07f38a03d37
content_hash: sha256:b4d972ccdfb73fa241fbdaf0351cd7145b6c295b9723efd18ab0af1608b8a8df
---

<!-- AUTHORED REGION START -->
# Systematic Momentum

**Authors:** Sophia Zhengzi Li, Peixuan Yuan, Guofu Zhou

**Year:** 2025 · **Venue:** Management Science, Articles in Advance (online 25 November 2025)

**Institutions:** Rutgers Business School; Hong Kong Baptist University; Olin Business School, Washington University in St. Louis

## Summary

The systematic component of a stock's return — the part explained by anomaly characteristics — is itself persistent. Sorting stocks on that component produces a return momentum that works **intraday, daily, weekly and monthly**, unlike Jegadeesh–Titman momentum, which works only monthly and reverses intraday. The authors argue it is distinct from factor momentum and does not crash.

## Sample

Russell 1000 constituents (or largest 1,000 US stocks). Intraday prices and quotes from TAQ, January 1993 to December 2020; daily CRSP returns and the monthly strategy comparisons, January 1970 to December 2020. Returns come from quote midpoints over twelve half-hour intervals from 10:00 to 16:00 plus one overnight interval.

## Findings

Each period, stock returns are regressed cross-sectionally on standardised anomaly variables; the systematic component (SYS) is the sum of fitted coefficients times characteristics. Three anomaly sets are used: 15 representative anomalies, the 15 of Ehsani and Linnainmaa (2022), and a 60-anomaly set. Annualised long–short returns range from 3.82% to 12.06% across intraday intervals for the first two sets and 5.92% to 14.68% for the 60-anomaly set, strongest in the morning. The signal persists about 65 intraday periods, roughly five days.

At monthly frequency, assuming a 20 bp round-trip cost: the conditional strategy C-SMOM earns 19.52% per year (t = 6.64), gross Sharpe 0.94 and net 0.78 at 133% turnover; unconditional SMOM earns 16.58% (t = 6.44), Sharpe 0.82 and 0.67; JT momentum earns 13.41% (t = 4.15), Sharpe 0.55 and 0.45. In spanning tests industry momentum is fully subsumed by SMOM and C-SMOM, while C-SMOM survives controls for all the others.

By the Lo–MacKinlay decomposition the driver is positive autocovariance in individual-stock SYS, from both same-factor autocorrelation and cross-serial lead-lag among different factors. The lead-lag part contributes nothing to time-series factor momentum and negatively to cross-sectional factor momentum — the paper's argument that the two effects differ.

The proposed explanation is limits to arbitrage: the effect strengthens after frequent news arrivals, in high aggregate idiosyncratic-volatility periods, and among stocks whose returns are more concentrated in systematic risk.

## Why It Matters / Caveats

The claim is strong — "the strongest momentum pattern in asset pricing" — and rests on a signal built from 15 to 60 characteristics estimated period by period, a far heavier construction than a sorted past return. Turnover is 126–133% monthly and the cost assumption is favourable. The universe is the largest 1,000 stocks only.

## Open Questions

- Does the intraday result survive execution at traded prices rather than quote midpoints?
- How much of the monthly outperformance over JT is the signal and how much is the shorter formation window?
- The paper's JT benchmark uses a two- to six-month formation period rather than the conventional 12−2. How does the comparison look against the standard definition?

## See Also

[[concepts/cross-sectional-momentum|Cross-Sectional Momentum]] · [[concepts/high-frequency-data|High-Frequency Data]] · [[concepts/limits-to-arbitrage|Limits to Arbitrage]] · [[concepts/risk-vs-mispricing|Risk vs Mispricing]]

[[sources/graef-2025-firm-specific-systematic-momentum|Graef, Hoechle & Schmid (2025)]] find the systematic component uninformative at medium horizons, the reverse of this result, using a rolling-beta rather than cross-sectional-regression decomposition. [[sources/daniel-2016-momentum-crashes|Daniel & Moskowitz (2016)]] is the crash-risk benchmark this paper claims to escape. [[sources/aleti-2022-high-frequency-factor-zoo|Aleti (2022)]] works the same intraday factor data from a risk-premia angle.

**Not yet written:** `concepts/factor-momentum`, `concepts/intraday-return-patterns`, `entities/guofu-zhou`

<!-- AUTHORED REGION END -->
