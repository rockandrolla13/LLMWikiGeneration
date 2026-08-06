---
title: Residual momentum
page_id: sources/blitz-2011-residual-momentum
page_type: source
source_path: markdown_output/1-s2.0-S0927539811000041-main.md
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- David Blitz
- Joop Huij
- Martin Martens
year: 2011
venue: Journal of Empirical Finance 18, 506-521
tags:
- momentum
- residual-returns
- time-varying-risk
- fama-french
- risk-adjusted-returns
sources: []
related:
- concepts/residual-momentum
- concepts/cross-sectional-momentum
- concepts/fama-french-factors
- concepts/risk-vs-mispricing
mind_map_priority: high
schema_version: 2
uuid: 5e4b50a4-adda-5b5f-8d7f-d4d4b57096fe
content_hash: sha256:91c73fbb730d076c96d7cd06bec84c1ee44739d785ed03ad1b085239a58135c4
---

<!-- AUTHORED REGION START -->
# Residual Momentum

**Authors:** David Blitz, Joop Huij, Martin Martens

**Year:** 2011 · **Venue:** Journal of Empirical Finance 18, 506–521

**Institutions:** Robeco Quantitative Strategies; Rotterdam School of Management; Erasmus University Rotterdam

## Summary

Conventional momentum implicitly bets on persistence in common-factor returns, which loads it with large time-varying Fama–French exposures. Ranking stocks on **residual** returns instead of total returns removes most of that exposure. The result is roughly the same return at half the volatility, so risk-adjusted profits about double.

## Sample

CRSP US domestic primary stocks (NYSE, AMEX, Nasdaq), January 1926 to December 2009; strategy returns run January 1930 to December 2009. Stocks priced below $1 are dropped. Residuals come from a Fama–French three-factor regression estimated over 36-month rolling windows, and stocks are ranked on the t−12 to t−2 residual return standardised by its own standard deviation. Equal-weighted deciles, overlapping holding periods.

## Findings

With one-month holding periods, total return momentum earns 10.26% per year with 22.70% volatility (Sharpe 0.45) and a conditional alpha of 7.98% (t = 4.27). Residual momentum earns 11.20% with 12.49% volatility (Sharpe 0.90) and an alpha of 10.85% (t = 8.35).

Conditional betas to the market, size and value factors are three to five times smaller for residual momentum. After negative formation-period market returns the market beta is −0.34 for total return momentum against −0.12 for residual momentum. Regression R² falls from 34–48% to 13–17%. Roughly 50% of conventional momentum's risk, but only 25% of its profit, comes from these dynamic exposures.

The factor-persistence check that motivates all this: formation-period and holding-period factor return signs agree 54–61% of the time, against a 50% null.

Three known "risk" facts about momentum dissolve. Over 2000–2009 total return momentum lost 8.5% per year while residual momentum made 4.7%. Over 1930–2009 total return momentum earned 14.7% in expansions and lost 8.7% in recessions; residual momentum earned a positive 5.6% during recessions. Residual momentum is also near size-neutral, so it is not a small-cap bet, and the December/January tax-loss pattern is much weaker.

## Why It Matters / Caveats

If the profitable part of momentum is the firm-specific part, then priced-risk and microstructure explanations look weaker, and the anomaly is a bigger problem for weak-form efficiency, not a smaller one. Caveats: deciles are equal-weighted and no transaction costs are applied, and the residual signal needs 36 clean monthly returns per stock, which excludes recent listings.

## Open Questions

- How much of the doubled Sharpe ratio survives the turnover of a standardised residual signal?
- Does the residual construction help or hurt in the crash states identified by Daniel and Moskowitz?

## See Also

[[concepts/residual-momentum|Residual Momentum]] · [[concepts/cross-sectional-momentum|Cross-Sectional Momentum]] · [[concepts/fama-french-factors|Fama-French Factors]] · [[concepts/risk-vs-mispricing|Risk vs Mispricing]]

[[sources/daniel-2016-momentum-crashes|Daniel & Moskowitz (2016)]] tackle the same dynamic-beta problem by scaling rather than by residualising. [[sources/graef-2025-firm-specific-systematic-momentum|Graef, Hoechle & Schmid (2025)]] extend the firm-specific-returns argument to test the factor momentum channel.

**Not yet written:** `entities/david-blitz`, `entities/joop-huij`, `entities/martin-martens`

<!-- AUTHORED REGION END -->
