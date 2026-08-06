---
title: 'Understanding Systematic Risk: A High-Frequency Approach'
page_id: sources/pelger-2015-understanding-systematic-risk
page_type: source
source_type: working-paper
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Markus Pelger
year: 2015
venue: UC Berkeley Center for Risk Management Research Working Paper 2015-09
tags:
- systematic-risk
- high-frequency-data
- latent-factors
- leverage-effect
- jumps
sources: []
related:
- concepts/approximate-factor-models
- concepts/principal-components-analysis
- concepts/high-frequency-data
- concepts/implied-volatility-surface
- concepts/stylized-facts
- concepts/factor-models
mind_map_priority: high
schema_version: 2
uuid: 1961b984-b2db-520d-9ab0-ef0910b14825
content_hash: sha256:69583f59fe00240abeed8a891602a4a7e820b54c3144c90844517db8998f1dad
---

<!-- AUTHORED REGION START -->
# Understanding Systematic Risk: A High-Frequency Approach

**Author:** Markus Pelger

**Year:** 2015 (dated 21 August 2015) · **Venue:** UC Berkeley Center for Risk Management Research Working Paper #2015-09

**Institution:** Stanford University (paper is part of the author's UC Berkeley PhD thesis)

## Summary

The empirical companion to the estimation theory in [[sources/pelger-2019-large-dimensional-hf-factor-model|Pelger (2019)]]. It applies latent-factor estimation to intraday S&P 500 data and asks four questions: how many factors, how persistent, do jump factors differ from continuous ones, and does the leverage effect live in systematic or idiosyncratic risk.

## What It Does

Under a large-dimensional [[concepts/approximate-factor-models|approximate factor model]], continuous and jump components are separated by truncation, giving a "continuous risk covariance" and a "jump covariance" matrix. [[concepts/principal-components-analysis|PCA]] on each yields the respective latent factors. The number of factors comes from a perturbed eigenvalue ratio. Statistical factors are compared with observable economic ones through generalized correlations — the highest correlations achievable by linear orthogonal combinations of the two sets.

The methodological point: no factor set is pre-specified, and because short horizons are usable, no restriction is placed on how factors vary over time.

## Findings

5-minute prices for S&P 500 firms, 2003–2012.

**Continuous factors.** Four persistent factors for 2007–2012, three for 2003–2006. The four are well approximated by a market portfolio plus oil, finance and electricity industry portfolios, with generalized correlations of 1.00, 0.98, 0.95 and 0.80. The Fama–French–Carhart factors do markedly worse: 0.95, 0.74, 0.60 and 0.00. Value, size and momentum play no significant role. The finance factor is the one that disappears before 2007.

**Jump factors.** One persistent jump factor, a market jump factor. Generalized correlations of the four industry jump factors with the first four statistical jump factors are 0.99, 0.75, 0.29 and 0.05 — clearly different from the continuous case.

**Volatility factors.** Using daily short-maturity at-the-money implied volatilities for the same firms, one persistent market volatility factor, plus a temporary banking volatility factor during the crisis.

**Leverage effect.** Decomposing the return-volatility correlation, the negative [[concepts/stylized-facts|stylized]] leverage effect is driven predominantly by the systematic component and can be absent for idiosyncratic risk. The author reads this as an argument against the financial-leverage explanation, which does not distinguish sources of risk, and as consistent with a risk-premium account — while stopping short of claiming proof.

## Caveats

High-frequency volatility estimates understate the leverage effect relative to implied-volatility estimates; only the latter are in line with the literature. Robustness to microstructure noise is argued indirectly, from stability across 5-min, 15-min and daily horizons.

## Open Questions

- Why do oil, finance and electricity emerge as the industry factors, rather than a broader sector set?
- Does the systematic-only leverage effect hold outside the 2003–2012 window?

## See Also

[[concepts/approximate-factor-models|Approximate Factor Models]] · [[concepts/principal-components-analysis|Principal Components Analysis]] · [[concepts/high-frequency-data|High-Frequency Data]] · [[concepts/implied-volatility-surface|Implied Volatility Surface]] · [[sources/pelger-2019-large-dimensional-hf-factor-model|Pelger (2019)]] · [[sources/aitsahalia-2017-pca-hf-factor-model|Aït-Sahalia & Xiu (2017)]]

**Not yet written:** `leverage-effect`, `generalized-correlation`, `jump-factors`, `volatility-factors`, `eigenvalue-ratio-estimator`.

<!-- AUTHORED REGION END -->

