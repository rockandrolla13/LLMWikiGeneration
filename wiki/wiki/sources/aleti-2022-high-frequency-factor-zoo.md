---
title: The High-Frequency Factor Zoo
page_id: sources/aleti-2022-high-frequency-factor-zoo
page_type: source
source_type: working-paper
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Saketh Aleti
year: 2022
venue: Working paper, Duke University (SSRN 4236964, 3 October 2022)
tags:
- factor-zoo
- jump-risk
- high-frequency-data
- risk-premia
- multiple-testing
sources: []
related:
- concepts/high-frequency-data
- concepts/factor-models
- concepts/risk-premia
- concepts/realized-variance
mind_map_priority: medium
schema_version: 2
uuid: 4f1d38ff-50ac-50f0-b68f-7585d9eed755
content_hash: sha256:3447e881f3fcb90c1c288d2f294302ee72d2ce060eb5be80013d094a14921f56
---

<!-- AUTHORED REGION START -->
# The High-Frequency Factor Zoo

**Author:** Saketh Aleti

**Year:** 2022 · **Venue:** Working paper, Duke University (SSRN 4236964, dated 3 October 2022)

## Summary

Rebuilds the factor zoo at intraday frequency so that each factor's returns can be split into a continuous (diffusive) part and jump parts, then prices both separately. Two results: jump and semijump risk are often priced and command larger premia than continuous risk, and most of the cross-sectional variation in expected returns traces to jump risk exposure, not continuous risk.

## Sample

All common stocks on NYSE, NASDAQ and NYSEMKT, January 1996 to December 2020. TAQ prices cleaned by standard procedures, sampled at 5 minutes and aggregated to 15 minutes for estimation, combined with CRSP open/close prices and adjusted returns: 14,610 stocks and about 2.38 billion high-frequency return observations.

Note a discrepancy inside the paper: the abstract says 224 high-frequency factor portfolios, while Section 2 describes 272 — 218 characteristic-sorted factors from Chen–Zimmermann and Jensen–Kelly–Pedersen, 6 Fama–French factors plus momentum, and 48 industry portfolios. Verify against the published version before citing a count.

## Findings

Continuous and jump betas are estimated separately using infill asymptotics, then priced by the continuous-time Fama–MacBeth regression of Aït-Sahalia, Jacod and Xiu (2021).

Among the Fama–French six workhorse factors, only two components carry significant premia: the jump component of the market and the continuous component of RMW. Nearly all of the market's excess return, 6.3%, comes from jump risk premia, about 3.4% from negative jump risk premia. RMW's continuous component draws 4%.

Across the full zoo, 42 of 654 estimates survive multiple-testing adjustment. Signs go the expected way — negative jumps (factor crashes) command a premium, positive jumps a negative one, continuous premia are generally positive — and all three magnitudes are comparable to the portfolio returns themselves.

Because zoo factors are heavily cross-correlated, the paper also prices 13 cluster portfolios built as first principal components of the Jensen–Kelly–Pedersen clusters. Four are robustly significant: negative jumps in Accruals (1.64% p.a.), positive jumps in Skewness (−2.22%) and Investment (−1.78%), and continuous returns in Profitability (3.01%). These clusters span 5, 6, 23 and 15 underlying factors, against an average portfolio return of 1.12%.

A final variance decomposition splits cross-sectional return variation between continuous and jump risk premia. Jump risk dominates for both large/mid-cap stocks and portfolios across several spanning models; continuous risk explains little and its premium is insignificant for most assets.

## Why It Matters / Caveats

It reframes the factor-zoo problem: not only which factors are priced, but which *component* of each factor. Hedging demand against discontinuous moves, not smooth covariation, does most of the pricing work. Caveats: working paper, one market, and portfolio-level microstructure noise is assumed to diversify away rather than modelled. Multiple-testing correction across strongly correlated factors is acknowledged as hard, which is why the cluster analysis exists.

## Open Questions

- Are the four significant clusters stable out of sample, or are they the survivors of the same search process that produced the zoo?
- Does the jump/continuous split change which factors survive the trading-cost screens applied in the low-frequency replication literature?

## See Also

[[concepts/high-frequency-data|High-Frequency Data]] · [[concepts/factor-models|Factor Models]] · [[concepts/risk-premia|Risk Premia]] · [[concepts/realized-variance|Realized Variance]] · [[concepts/fama-french-factors|Fama-French Factors]] · [[concepts/look-ahead-bias-data-mining|Look-Ahead Bias and Data Mining]]

[[sources/li-2025-systematic-momentum|Li, Yuan & Zhou (2025)]] use the same TAQ-based intraday factor machinery to hunt for return predictability rather than risk premia.

**Not yet written:** `concepts/factor-zoo`, `concepts/jump-risk`, `concepts/multiple-hypothesis-testing`, `entities/saketh-aleti`

<!-- AUTHORED REGION END -->
