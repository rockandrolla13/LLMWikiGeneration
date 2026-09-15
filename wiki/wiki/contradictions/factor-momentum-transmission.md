---
title: Does Factor Momentum Cause Stock Momentum?
page_id: contradictions/factor-momentum-transmission
page_type: contradiction
revision_id: 1
created: 2026-09-15 00:00:00+00:00
updated: '2026-09-15T00:00:00Z'
status: unresolved
tags:
- momentum
- factor-momentum
- residual-momentum
sources:
- sources/ehsani-2022-factor-momentum
- sources/graef-2025-firm-specific-systematic-momentum
related:
- concepts/factor-momentum
- concepts/residual-momentum
- concepts/cross-sectional-momentum
schema_version: 2
uuid: 4af1e0b6-8065-5351-9e73-5679780d2f52
content_hash: sha256:376ba3e3044b41261275042430092acea03fb6027caf2fdcf09332672dc5cb31
---

<!-- AUTHORED REGION START -->
# Does Factor Momentum Cause Stock Momentum?

**Status:** unresolved

## Claim A: stock momentum is mostly factor momentum

[[sources/ehsani-2022-factor-momentum|Ehsani & Linnainmaa (2022)]] argue that factor autocorrelation transmits into the cross-section of stocks through dispersion in factor loadings. Their evidence is spanning tests. Factor momentum explains standard, industry, intermediate, Sharpe-ratio and residual stock momentum, and none of these explains factor momentum. On their reading, residual momentum is profitable because residuals from an incomplete model inherit the momentum of omitted factors, not because firm-specific returns persist.

## Claim B: the firm-specific part carries momentum and the systematic part does not

[[sources/graef-2025-firm-specific-systematic-momentum|Graef, Hoechle & Schmid (2025)]] split each stock's past return into a systematic part (five-factor loadings times factor returns) and a firm-specific residual. They sort on each part separately. Over medium horizons the firm-specific sort earns 0.571% a month (t = 3.24), close to full momentum. The systematic sort earns 0.200% (t = 1.00) with an alpha of 0.040%. Momentum also earns about the same in extreme-beta (0.585%) and modest-beta (0.544%) subsamples, which cuts against a channel that runs through beta dispersion.

## Where exactly they conflict

Both papers agree on the empirical correlation between factor momentum and stock momentum. Graef et al. also replicate Ehsani & Linnainmaa's residual-momentum table. The disagreement is over the **mechanism**. Does the systematic component of a stock's return drive its continuation? Claim A says yes; Claim B's direct test says no.

## Points that bear on a resolution

These are editorial observations from reading both papers. Neither paper states them as a resolution.

- Ehsani & Linnainmaa say themselves that firm-specific momentum cannot be ruled out. Unknown factors, unobserved factor returns and noisy betas make the split unidentifiable without a natural experiment. Graef et al.'s systematic return is built from estimated five-factor betas, so the same omitted-factor problem applies to their decomposition. A null on the systematic sort is what one would see if the relevant autocorrelated factors sit outside the five-factor model.
- Ehsani & Linnainmaa report in a footnote that weighting factors by the cross-sectional variance of their betas hardly changes the strategy (0.31% versus 0.34% a month, correlation 0.95). Their own evidence therefore gives beta dispersion only a weak role, which is consistent with Graef et al.'s beta-subsample result.
- The two tests use different right-hand-side objects. Ehsani & Linnainmaa trade factor returns directly, including high-eigenvalue PCs of 47 factors. Graef et al. sort stocks on fitted systematic returns from a five-factor model. A factor-level spanning result and a stock-level sorting result can both hold.

## What would settle it

A setting where firm-specific returns are observed, or a decomposition that is robust to the omitted-factor problem. For example, one could repeat Graef et al.'s systematic sort using the high-eigenvalue PC factors that carry Ehsani & Linnainmaa's momentum instead of the five Fama–French factors. The wiki has no source that does this.
<!-- AUTHORED REGION END -->
