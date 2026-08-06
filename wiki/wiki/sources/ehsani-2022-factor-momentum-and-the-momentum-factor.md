---
title: "Factor Momentum and the Momentum Factor"
page_id: sources/ehsani-2022-factor-momentum-and-the-momentum-factor
page_type: source
source_type: journal-article
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
authors: [Sina Ehsani, Juhani T. Linnainmaa]
year: 2022
venue: The Journal of Finance
doi: 10.1111/jofi.13131
tags: [factor-momentum, momentum, asset-pricing, principal-components, anomalies, quant-equity, empirical-finance]
related: [concepts/factor-momentum, concepts/cross-sectional-momentum, concepts/residual-momentum, concepts/momentum-neutral-factors, concepts/omitted-factor-momentum, concepts/high-eigenvalue-factor-momentum, concepts/sentiment-persistence-factor-autocorrelation, entities/sina-ehsani, entities/juhani-linnainmaa, entities/serhiy-kozak, entities/stefan-nagel, entities/shrihari-santosh, entities/narasimhan-jegadeesh, entities/sheridan-titman, entities/mark-carhart]
mind_map_priority: high
---

# Factor Momentum and the Momentum Factor

**Authors:** [[entities/sina-ehsani|Sina Ehsani]], [[entities/juhani-linnainmaa|Juhani T. Linnainmaa]]

**Venue:** The Journal of Finance, 2022

## Summary

This paper argues that individual stock momentum is largely a manifestation of [[concepts/factor-momentum|factor momentum]]: most equity factors are positively autocorrelated, earning 51 bps per month following a positive year versus 6 bps following a down year. A time-series factor-momentum strategy that trades factors — or the [[concepts/high-eigenvalue-factor-momentum|high-eigenvalue principal-component factors]] extracted from them — subsumes standard, industry, industry-adjusted, intermediate, Sharpe-ratio, and [[concepts/residual-momentum|residual momentum]]. The authors show that [[concepts/cross-sectional-momentum|cross-sectional stock momentum]] is transmitted through dispersion in factor loadings, that [[concepts/momentum-neutral-factors|momentum-neutral factors]] display even more momentum than standard factors, and that residual momentum is an [[concepts/omitted-factor-momentum|omitted-factor-momentum]] artifact. The evidence implies momentum is not a distinct risk factor but a dynamic strategy that times other factors, consistent with the [[concepts/sentiment-persistence-factor-autocorrelation|sentiment-persistence mechanism]] of Kozak, Nagel, and Santosh.

## Key Claims

1. Most factors are positively autocorrelated: the average (nonmomentum) factor earns 6 bps/month after a losing year and 51 bps after a winning year (slope t = 4.22), so a factor's own prior return predicts its future return.
2. [[concepts/factor-momentum|Factor momentum]] concentrates in [[concepts/high-eigenvalue-factor-momentum|high-eigenvalue PC factors]] that explain more of the cross-section; a strategy trading the first 10 PC factors has a five-factor alpha with t = 6.51, consistent with the absence of near-arbitrage opportunities.
3. Factor momentum (from 20 individual factors or 10 high-eigenvalue PCs) prices momentum-sorted decile portfolios as well as or better than the Carhart UMD factor, and momentum in high-eigenvalue PCs fully explains UMD's returns (alpha = -6 bps, R-squared = 43%).
4. [[concepts/momentum-neutral-factors|Momentum-neutral factors]] (weights twisted to be orthogonal to stocks' past returns) exhibit MORE momentum than standard factors and subsume standard factor momentum, so factor momentum is not merely incidental to individual-stock momentum.
5. [[concepts/residual-momentum|Residual momentum]] is an [[concepts/omitted-factor-momentum|omitted-factor-momentum]] artifact: simulations and actual data show estimated residuals display momentum whenever the asset-pricing model omits autocorrelated factors, even if firm-specific returns are IID.

## Concepts

- [[concepts/factor-momentum|Factor momentum]] — the central construct; the paper trades factors on their own prior-year returns and shows it subsumes stock momentum.
- [[concepts/cross-sectional-momentum|Cross-sectional momentum]] — decomposed into four sources, with factor autocorrelation via beta dispersion the dominant channel.
- [[concepts/residual-momentum|Residual momentum]] — shown to add nothing once factor momentum is controlled for.
- [[concepts/momentum-neutral-factors|Momentum-neutral factors]] — construction that removes incidental stock-momentum bets yet retains (more) factor momentum.
- [[concepts/omitted-factor-momentum|Omitted-factor momentum]] — explains why residuals display momentum when models omit autocorrelated factors.
- [[concepts/high-eigenvalue-factor-momentum|High-eigenvalue factor momentum]] — factor momentum concentrates in PCs explaining most of the cross-section.
- [[concepts/sentiment-persistence-factor-autocorrelation|Sentiment-persistence factor autocorrelation]] — the KNS mechanism the paper invokes to rationalize positive factor autocorrelation.

## Related Sources

(Leave empty for now — links added by future ingestions)
