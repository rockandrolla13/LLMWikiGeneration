---
authors:
- Ka Kei Chan
- Olga Kolokolova
- Ming-Tsung Lin
- Ser-Huang Poon
content_hash: sha256:1a1855bf058a243135dfdd6d3dd48c31301d681df3a740e4f55875bdf87b2227
created: '2026-10-05T15:52:32Z'
page_id: sources/chan-2023-price-convergence-cds-put-option
page_type: source
publication_date: '2023'
publication_venue: Journal of Empirical Finance 72, pp. 188-213
related:
- concepts/capital-structure-arbitrage
- concepts/credit-default-swaps
- concepts/credit-default-swap-spread
- concepts/option-implied-credit-information
- concepts/hazard-rate-curve
- concepts/nelson-siegel-model
- concepts/market-implied-ratings
- concepts/limits-to-arbitrage
- concepts/bond-market-segmentation
- concepts/credit-relative-value
- concepts/fama-french-factors
- concepts/mean-reversion
- concepts/unit-recovery-claim
- sources/kapadia-2012-limited-arbitrage-equity-credit
- sources/shi-2022-cds-options-comovement
- sources/avino-2024-hedging-credit-equity-options
- sources/amadori-2014-relative-informational-efficiency
- sources/hong-2025-implied-vol-cds-korea
- sources/carr-2011-american-puts-credit-protection
- analyses/capital-structure-arbitrage-literature-review
- entities/ka-kei-chan
- entities/olga-kolokolova
- entities/ming-tsung-lin
- entities/ser-huang-poon
- entities/gfi-group
revision_id: 1
schema_version: 2
source_hash: sha256:8896fca453f23e3926258eb6a6c99e85b07a8893b9dc6a92c7e9b12f091b2c3d
source_path: markdown_output/chan-2023-price-convergence-cds-put-option.md
source_type: paper
sources: []
tags:
- capital-structure-arbitrage
- cds
- deep-out-of-the-money-puts
- hazard-rate-curve
- nelson-siegel
- market-segmentation
- convergence-trading
- hedge-funds
title: 'Price Convergence Between Credit Default Swap and Put Option: New Evidence'
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: cf517af4-b7f1-55b9-a67d-d559cb34b516
version_read: 'Published open-access version of record (manifest version: ''published,
  open access''), CC BY licence.'
year: 2023
---

<!-- AUTHORED REGION START -->
# Price Convergence Between Credit Default Swap and Put Option: New Evidence

**Authors:** Ka Kei Chan, Olga Kolokolova, Ming-Tsung Lin, Ser-Huang Poon · **Year:** 2023 · **Venue:** Journal of Empirical Finance 72, pp. 188-213
**Version read:** Published open-access version of record (manifest version: 'published, open access'), CC BY licence.

## Summary

The paper revisits Carr and Wu (2011), who argued that CDS and deep out-of-the-money puts (DOOMPs) should price the same default claim. The authors argue the two markets are only partly integrated. CDS trade over the counter, mostly at five years, and are held by banks and insurers. DOOMPs are exchange traded, mostly under six months, and attract hedge funds. So the law of one price can fail for a long time.

They turn each CDS and each put into an implied hazard rate. Each day they fit a Nelson-Siegel hazard curve per rating class, separately for CDS and for puts. The gap between a put-implied and a CDS-implied hazard rate is then split into three parts: the gap between the two rating curves at the CDS maturity (market segmentation), the gap between each contract's residual from its own curve (contract-level noise), and a slope term for the maturity mismatch.

Both residuals shrink back toward their own curves, and the two curves drift toward each other. But the two forces often point in different directions. Put-implied curves sit above CDS-implied curves on average, especially for investment-grade names. Overall hazard rates converge only when both the curve gap and the residual gap point the same way.

A trade that uses the raw put-minus-CDS hazard gap (the Carr-Wu style 'Benchmark') makes money before costs but loses after them. Trading only when the curve gap and residual gap agree (the 'Decomposition' signal) stays profitable after costs. At the market level, residual noise in the put market goes with better hedge fund returns, while cross-market segmentation predicts worse hedge fund returns a month later.

## Data

- CDS: GFI inter-dealer traded quotes (CreditMatch and brokerage desks), US single-name senior CDS, July 2012 to April 2016; 46,495 intraday observations, about 81% at the 5-year tenor; points-upfront quotes converted to par spreads. Markit composites added for other tenors when fitting CDS curves.
- Options: OptionMetrics puts with |delta| < 0.15, bid > 0 and volume > 0 (no $5 strike cap, unlike Carr-Wu); 82,623 put observations, mean maturity 0.38 years.
- Pairs: each day each firm's 5-year CDS is matched to the put with the longest maturity (highest open interest on ties): 4,268 pairs; 2,134 trades unwind within 7-30 days for the regressions.
- Ratings: Markit implied ratings (actual ratings unavailable for the period).
- Recovery: 40% for all CDS.
- Other: Fama-French five factors, VIX, Pastor-Stambaugh liquidity, Hu-Pan-Wang Treasury noise, Eurekahedge and Barclayhedge hedge fund returns, Fung-Hsieh seven factors; monthly aggregate measures over 45 months.

## Method

Implied hazard rates follow Carr and Wu (2011): the CDS-implied rate is H^C = k/(1-RR) with RR = 0.4; the put-implied rate is backed out of the unit recovery claim value P/K under a flat hazard.

Per rating class and day, fit a Nelson-Siegel curve to hazard rates by maturity:
$$F(\tau|\beta_0,\beta_1,\beta_2,m)=\beta_0+\beta_1\frac{1-e^{-\tau/m}}{\tau/m}+\beta_2\Big(\frac{1-e^{-\tau/m}}{\tau/m}-e^{-\tau/m}\Big)$$
(eq. 13, checked against the PDF; \beta_0 long-term level, \beta_1 short-term, \beta_2 medium-term hump, m sets the hump's shape and position), then split H = F + R (fitted + residual).

Decomposition of the cross-market gap (eq. 1):
$$H^P_{\tau_P}-H^C_{\tau_C}=(F^P_{\tau_C}-F^C_{\tau_C})+(R^P_{\tau_P}-R^C_{\tau_C})+(F^P_{\tau_P}-F^P_{\tau_C}),$$
i.e. curve difference + residual difference + put-curve slope adjustment.

Tests: (H1) pooled panel regressions of each component on credit level, |delta|, implied vol, open interest, CDS and put bid-ask spreads, CDS trade count and log put maturity, with date and rating fixed effects; (H2) \Delta H = \beta_0 + \beta_1 \Delta F + \beta_2 R + e for each market (negative \beta_2 = convergence to the curve); (H3) \Delta D^H = \beta_0 + \beta_1 d^F + \beta_2 d^R + \beta_3 d^S + e using the residualised components.

Trading: short the relatively expensive leg and buy the cheap leg (one put against Price^P/(N k) units of 5-year CDS, N = 5), unwind at the first chance after 7 days; returns include the net CDS spread stream to maturity or default, and costs of half the bid-ask spread on each side. Benchmark trades on sign(H^P - H^C); Decomposition trades only when curve and residual gaps share a sign. Aggregate monthly Noise^C, Noise^P (RMS residual scaled by fitted value) and Segment^CP (RMS 5-year curve gap scaled by mean fitted value) are related to hedge fund alphas.

## Key Findings

1. CDS- and put-implied hazard rates correlate 58% overall; the correlation depends heavily on maturity mismatch, ranging from 47% to 85% across mismatch terciles.
2. Individual hazard rates revert to their own rating curves: the loading on the past residual is -0.063 for CDS and -0.340 for puts, both significant at 1%; there is no such reversion toward simple rating-class means or medians.
3. Cross-market convergence is driven by both the curve gap and the residual gap (coefficients -0.069 and -0.208), while the maturity-slope term is not significant.
4. Before costs, the Benchmark (raw-gap) trade earns 18.3% per trade over 2,930 trades and the Decomposition trade 30% over 1,037 trades; after costs the Benchmark loses 8% while the Decomposition still earns 3.8%.
5. Trades with agreeing signs close faster: average holding 28.53 days versus 36.93 days when the curve and residual gaps disagree.
6. The monthly segmentation measure rises with Treasury-market noise (0.43) and VIX (0.30) and falls with the market excess return (-0.49); a one-standard-deviation rise predicts about 22 bp lower hedge fund abnormal return the next month.

## Limitations

CDS trades come from a single inter-dealer broker (GFI), though the authors report no significant difference from Markit composites. Ratings are Markit CDS-implied, which makes the CDS curve partly circular in CDS levels. Puts are much shorter than CDS (longest put used 2.5 years), so the put curve's long end is extrapolated. Fewer than 1% of puts have strikes under $5, so the corridor logic of Carr-Wu is applied to much higher strikes; robustness at the 10th and 25th strike percentiles is only in the online appendix. Flat-hazard and fixed 40% recovery assumptions carry over. Trade returns include a CDS spread stream to maturity, so they are per-trade total returns over long horizons, not short-period returns. The sample is short (45 months) and the hedge fund tests use 45 monthly observations.

## Questions Raised

- Would the curve-plus-residual decomposition work for bond-implied versus CDS-implied hazard rates (the CDS-bond basis)?
- Does the put-market noise measure predict credit spread or bond returns, not only hedge fund performance?
- How much of the persistent put-over-CDS curve gap for investment-grade names is a jump-risk premium in puts versus segmentation?
- Is the rating-curve residual a better relative-value signal than raw firm-level gaps in other credit instruments?

## Relevance to Bond Signals

The key design idea transfers directly: split a firm's mispricing into a rating-curve component and a residual from its own market's curve, and trade only when both point the same way. For bonds, the residual of a bond spread from a rating-by-maturity Nelson-Siegel curve is a reverting signal, and agreement with an equity-option-implied hazard gap could act as a filter.

See [[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage: Literature Review for Bond Signals]].

## Concepts

- [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]]
- [[concepts/credit-default-swaps|Credit Default Swaps]]
- [[concepts/credit-default-swap-spread|Credit Default Swap Spread]]
- [[concepts/option-implied-credit-information|Option-Implied Information in Credit Markets]]
- [[concepts/hazard-rate-curve|Hazard Rate Curve]]
- [[concepts/nelson-siegel-model|Nelson-Siegel Model]]
- [[concepts/market-implied-ratings|Market-Implied Ratings]]
- [[concepts/limits-to-arbitrage|Limits to Arbitrage]]
- [[concepts/bond-market-segmentation|Bond Market Segmentation]]
- [[concepts/credit-relative-value|Credit Relative Value]]
- [[concepts/fama-french-factors|Fama-French Factors]]
- [[concepts/mean-reversion|Mean Reversion]]
- [[concepts/unit-recovery-claim|Unit Recovery Claim]]

## Entities

- [[entities/ka-kei-chan|Ka Kei Chan]]
- [[entities/olga-kolokolova|Olga Kolokolova]]
- [[entities/ming-tsung-lin|Ming-Tsung Lin]]
- [[entities/ser-huang-poon|Ser-Huang Poon]]
- [[entities/gfi-group|GFI]]

## Related Sources

- [[sources/kapadia-2012-limited-arbitrage-equity-credit|Limited arbitrage between equity and credit markets]]
- [[sources/shi-2022-cds-options-comovement|Market Co-movement Between Credit Default Swap Curves and Option Volatility Surfaces]]
- [[sources/avino-2024-hedging-credit-equity-options|Contingent Claims and Hedging of Credit Risk with Equity Options]]
- [[sources/amadori-2014-relative-informational-efficiency|The Relative Informational Efficiency of Stocks, Options and Credit Default Swaps During the Financial Crisis]]
- [[sources/hong-2025-implied-vol-cds-korea|Do Changes in the Implied Volatility of Stock Options Predict Future Changes in CDS Spreads?]]
- [[sources/carr-2011-american-puts-credit-protection|A Simple Robust Link Between American Puts and Credit Protection]]
<!-- AUTHORED REGION END -->