---
title: Firm-specific versus systematic momentum
page_id: sources/graef-2025-firm-specific-systematic-momentum
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Frank Graef
- Daniel Hoechle
- Markus Schmid
year: 2025
venue: Finance Research Letters 76, 106963
tags:
- momentum
- factor-momentum
- idiosyncratic-returns
- return-decomposition
- replication
sources: []
related:
- concepts/residual-momentum
- concepts/cross-sectional-momentum
- concepts/fama-french-factors
- concepts/factor-timing
mind_map_priority: medium
schema_version: 2
uuid: de94bc89-6df9-56a5-9158-6b9db3cbd344
content_hash: sha256:49bc1b20397a2dcdcd9ee8b0865ce1d8f8110c3d9ec29fb13460d7c2bc97f7fd
---

<!-- AUTHORED REGION START -->
# Firm-Specific versus Systematic Momentum

**Authors:** Frank Graef, Daniel Hoechle, Markus Schmid

**Year:** 2025 · **Venue:** Finance Research Letters 76, 106963

**Institutions:** University of Applied Sciences Northwestern Switzerland; University of St. Gallen; Swiss Finance Institute; ECGI

## Summary

A direct test of the claim that stock momentum is caused by factor momentum. Decompose returns into a systematic part (factor loadings times factor returns) and a firm-specific residual, then race the two as sorting signals. The firm-specific part wins, and the systematic part predicts nothing over medium horizons. The transmission mechanism proposed by Ehsani and Linnainmaa (2022, "EL") does not survive the test.

## Sample

CRSP monthly US stock returns merged with Compustat, NYSE/AMEX/Nasdaq ordinary common stock, July 1963 to December 2019; strategy results run July 1966 to December 2019. Financials and negative-book-equity firms are excluded and accounting data lagged six months. Fama–French five-factor betas are estimated over months t−60 to t−1 with at least 36 observations. Newey–West standard errors, three lags.

## Findings

The baseline value-weighted momentum strategy earns 0.66% per month (t = 3.05) with a five-factor alpha of 0.755%; equal-weighted, 0.85% and 0.765%.

Sorting on **medium-term idiosyncratic** returns earns 0.571% per month (t = 3.24) with an alpha of 0.937% (t = 5.65) — close to conventional momentum. Sorting on **medium-term systematic** returns earns 0.200% (t = 1.00) with an alpha of 0.040% (t = 0.17). That is the opposite of what the factor-momentum channel predicts. At the short horizon the pattern flips: short-term idiosyncratic returns give a strong reversal (−0.783%) while short-term systematic returns are positive (0.383%, t = 2.19), so any factor-to-stock spillover is confined to about one month.

The results hold under the CAPM, Fama–French three-factor, Hou et al. (2021) augmented q, and Stambaugh–Yuan mispricing models, and under t−72 to t−13 or t−36 to t−1 beta windows.

The second test targets beta dispersion, which EL's mechanism requires. Momentum earns 0.585% in an "extreme-beta" subsample (a loading above the 80th or below the 20th percentile on at least one factor) and 0.544% in the "modest-beta" subsample — effectively the same, despite very different net factor loadings.

The authors replicate EL's Table 7 UMD-style residual strategies successfully (0.607 versus EL's 0.58 under the CAPM), but the systematic-return analogue, which EL do not test, fails.

## Why It Matters / Caveats

A short, targeted rebuttal, not a general theory. It does not dispute that factor momentum exists or correlates with stock momentum — only that the stated transmission channel produces it. Single market, single sample, and the decomposition inherits whatever the chosen factor model gets wrong.

## Open Questions

- If beta dispersion is irrelevant, what does explain the empirical link between factor momentum and stock momentum that EL document?
- Why is short-term systematic momentum positive when medium-term systematic momentum is zero?

## See Also

[[concepts/residual-momentum|Residual Momentum]] · [[concepts/cross-sectional-momentum|Cross-Sectional Momentum]] · [[concepts/fama-french-factors|Fama-French Factors]] · [[concepts/factor-timing|Factor Timing]]

[[sources/blitz-2011-residual-momentum|Blitz, Huij & Martens (2011)]] is the direct antecedent for the idiosyncratic-momentum signal. [[sources/li-2025-systematic-momentum|Li, Yuan & Zhou (2025)]] reach the opposite conclusion about the systematic component using an intraday, characteristic-regression construction. [[sources/daniel-2016-momentum-crashes|Daniel & Moskowitz (2016)]] is cited for momentum's time-varying risk exposures.

**Not yet written:** `concepts/factor-momentum`, `entities/juhani-linnainmaa`, `entities/markus-schmid`

<!-- AUTHORED REGION END -->
