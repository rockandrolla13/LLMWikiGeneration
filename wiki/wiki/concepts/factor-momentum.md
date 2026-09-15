---
title: Factor Momentum
page_id: concepts/factor-momentum
page_type: concept
concept_type: technique
abstraction_level: intermediate
revision_id: 1
created: 2026-09-15 00:00:00+00:00
updated: '2026-09-15T00:00:00Z'
tags:
- momentum
- factor-momentum
- factor-timing
- autocorrelation
sources:
- sources/ehsani-2022-factor-momentum
- sources/graef-2025-firm-specific-systematic-momentum
- sources/li-2025-systematic-momentum
related:
- concepts/cross-sectional-momentum
- concepts/residual-momentum
- concepts/factor-timing
- concepts/momentum-trend-following
- concepts/autocorrelation-time-series
- concepts/principal-components-analysis
- contradictions/factor-momentum-transmission
mind_map_priority: high
schema_version: 2
uuid: a0fb1bc6-37e8-52b7-9a39-bfbf6ab59bb0
content_hash: sha256:265e13bc9cd80e70dd0de01ded03c7aab3085b5f131906d0cc86b0030800ec54
---

<!-- AUTHORED REGION START -->
# Factor Momentum

## Definition

Factor momentum is a strategy that bets on the positive autocorrelation of long–short factor returns. It holds a factor, such as size or profitability, after a year in which that factor made money, and holds its reverse after a year in which it lost. It is momentum applied to factors rather than to individual securities.

## Construction

Following [[sources/ehsani-2022-factor-momentum|Ehsani & Linnainmaa (2022)]]:

- **Time-series version.** Long each factor whose average return over months t−12 to t−1 is positive, and short it otherwise. This is a pure bet on each factor's own autocorrelation.
- **Cross-sectional version.** Long factors with above-median past returns and short those below. It is weaker, because it also bets that one factor's high return predicts low returns on the others. In the data the opposite usually holds.
- **Scaling.** Factors are levered to a common variance before signing, so no single volatile factor dominates. Volatility enters the sizing, not the signal.
- **PC version.** Extract principal components from many characteristic factors in real time, demean them, equalise their variance and sign them on past returns. Most of the momentum sits in the highest-eigenvalue components.

A useful property is that the investor never needs to know which leg of a factor earns the premium on average. The signal picks the direction each year.

## Relation to Stock Momentum

If stock returns have a factor structure, factor autocorrelation shows up as cross-sectional stock momentum. Past winners load on factors that did well, so buying them buys those factors. Ehsani & Linnainmaa find that factor momentum spans standard, industry, intermediate, Sharpe-ratio and residual stock momentum, and that the reverse does not hold. They read momentum as "timing other factors" rather than a distinct factor.

That transmission story is contested. [[sources/graef-2025-firm-specific-systematic-momentum|Graef, Hoechle & Schmid (2025)]] find that sorting stocks on the systematic part of their past returns earns nothing over medium horizons, while the firm-specific part earns close to full momentum. See [[contradictions/factor-momentum-transmission|Factor momentum transmission]].

[[sources/li-2025-systematic-momentum|Li, Yuan & Zhou (2025)]] document a related but distinct effect. Their systematic component comes from period-by-period characteristic regressions, and they use a Lo–MacKinlay decomposition to separate it from factor momentum.

## Why It Matters for Signal Design

- A momentum signal built on factors, or on a security's factor exposures, can carry most of what stock-level momentum carries at lower volatility.
- Residualising returns before ranking is not neutral. What the residual captures depends on which autocorrelated factors the model leaves out.
- In a bond context the same logic would apply to credit, rates and liquidity factors. This wiki has no source that tests factor momentum in corporate bonds directly; [[concepts/bond-momentum|Bond Momentum]] and [[sources/haesen-2017-momentum-spillover|Haesen et al. (2017)]] cover the security-level evidence.

## Sources

- [[sources/ehsani-2022-factor-momentum|Ehsani & Linnainmaa (2022)]] — central; defines the strategy and the transmission argument
- [[sources/graef-2025-firm-specific-systematic-momentum|Graef, Hoechle & Schmid (2025)]] — rebuttal of the transmission channel
- [[sources/li-2025-systematic-momentum|Li, Yuan & Zhou (2025)]] — systematic momentum, distinguished from factor momentum

## Related Concepts

- [[concepts/cross-sectional-momentum|Cross-Sectional Momentum]]
- [[concepts/residual-momentum|Residual Momentum]]
- [[concepts/factor-timing|Factor Timing]]
- [[concepts/momentum-trend-following|Momentum and Trend Following]]
- [[concepts/autocorrelation-time-series|Autocorrelation in Time Series]]
- [[concepts/principal-components-analysis|Principal Components Analysis]]
<!-- AUTHORED REGION END -->
