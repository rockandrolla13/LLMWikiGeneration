---
authors:
- Yukun Shi
- Ding-Rong Chen
- Biao Guo
- Yaofei Xu
- Cheng Yan
content_hash: sha256:eab9299b1afc3947066334ea3ec0f8151db4abd18f2afd1ea614cbcd8b5bf2c6
created: '2026-10-05T15:52:32Z'
page_id: sources/shi-2022-cds-implied-volatility-trading-strategies
page_type: source
publication_date: '2022'
publication_venue: International Review of Financial Analysis 83, 102295
related:
- concepts/credit-default-swaps
- concepts/credit-default-swap-spread
- concepts/capital-structure-arbitrage
- concepts/option-implied-credit-information
- concepts/reduced-form-credit-models
- concepts/merton-model
- concepts/volatility-smirk
- concepts/implied-volatility-skew
- concepts/cointegration
- concepts/statistical-arbitrage
- concepts/mean-reversion
- concepts/unit-recovery-claim
- concepts/cds-implied-volatility
- sources/shi-2022-cds-options-comovement
- sources/cao-2023-implied-vol-bond-returns
- sources/dafonseca-2020-cds-equity-volatility-comovement
- sources/hong-2025-implied-vol-cds-korea
- sources/kapadia-2012-limited-arbitrage-equity-credit
- sources/avino-2024-hedging-credit-equity-options
- sources/carr-2011-american-puts-credit-protection
- analyses/capital-structure-arbitrage-literature-review
- entities/yukun-shi
- entities/ding-rong-chen
- entities/biao-guo
- entities/yaofei-xu
- entities/cheng-yan
revision_id: 1
schema_version: 2
source_hash: sha256:afef89ef73f231c35db2137b4c512183b570702a4857bc74103bceb85860ed48
source_path: markdown_output/shi-2022-cds-implied-volatility-trading-strategies.md
source_type: paper
sources: []
tags:
- credit-default-swaps
- implied-volatility
- unit-recovery-claim
- deep-otm-puts
- cds-equity-arbitrage
- cointegration
- capital-structure-arbitrage
- trading-strategy
title: The Information Content of CDS Implied Volatility and Associated Trading Strategies
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: 6d24bcbd-14b3-5b65-9097-f3a8e2f84a8b
version_read: Accepted manuscript (University of Glasgow Enlighten eprint 274873,
  deposited 12 July 2022; preprint dated July 5, 2022)
year: 2022
---

<!-- AUTHORED REGION START -->
# The Information Content of CDS Implied Volatility and Associated Trading Strategies

**Authors:** Yukun Shi, Ding-Rong Chen, Biao Guo, Yaofei Xu, Cheng Yan · **Year:** 2022 · **Venue:** International Review of Financial Analysis 83, 102295
**Version read:** Accepted manuscript (University of Glasgow Enlighten eprint 274873, deposited 12 July 2022; preprint dated July 5, 2022)

## Summary

The paper builds a CDS-implied volatility (CIV): the equity volatility that the CDS market implies for a firm. It uses the unit recovery claim (URC) of Carr and Wu (2011), a claim that pays one dollar if the firm defaults before maturity. A URC can be priced from a CDS spread or from deep out-of-the-money American puts on the same firm's stock. Setting the two equal gives a put price from the CDS. A 200-step binomial tree then inverts that put price into a volatility.

The authors compare their CIV with two earlier CIV measures (Guo 2016; Kelly et al. 2019), which rely on Merton-type structural models. Their measure co-moves far more with option-implied volatility (OIV), with an average correlation of about 0.8. It also explains much more of OIV in regressions. The link is strongest for 1-year CDS, where the maturity mismatch with options is smallest.

CIV and OIV are cointegrated for most firms. The authors sort CDS each week on a z-score of the CIV-OIV gap. They buy protection-side returns in the lowest quintile and short the highest. Before costs, this earns 58.29% a year with a Sharpe ratio of 2.97 for 5-year CDS. Option-side versions work for deep OTM puts and delta-hedged deep OTM puts, but not for ATM straddles or ATM delta-hedged calls. Skewness, jump and volatility risk factors explain little of the CDS strategy return.

## Data

- Markit single-name USD corporate CDS, weekly (Wednesdays), January 2002 to December 2014; at least 52 weeks of data; modified-restructuring clause with unchanged recovery.
- OptionMetrics (via WRDS) American equity puts: positive bid, maturity over 360 days, delta above -0.15, highest open interest (delta closest to 0 if tied).
- Risk-free rates: 1-, 3-, 5-, 7- and 10-year constant-maturity Treasury yields from the Federal Reserve Board.
- 120,588 CIV-OIV pairs; after dropping extreme equity/debt values, 335 firms over 666 weeks; put maturities 360 to 969 days (mean 546).
- CDS maturities 1, 3, 5, 7 and 10 years; option-strategy sample of 108,449 weekly deep OTM put contracts and 136,928 ATM call-put pairs.

## Method

URC value with constant rate r and default intensity lambda: $URC(t,T)=E^Q_t[e^{-r\tau}1(\tau<T)]=\lambda\frac{1-e^{-(r+\lambda)(T-t)}}{r+\lambda}$; risk-neutral default probability $D(t,T)=1-e^{-\lambda(T-t)}$, with $URC(t,T)\le D(t,T)\le e^{r(T-t)}URC(t,T)$.

From puts with strikes inside the default corridor [A,B]: $URC^{American\text{-}put}=\frac{P_1-P_2}{K_1-K_2}$, simplified (with $K_2=0$ on default) to $URC^{American\text{-}put}=P_1/K_1$. From the CDS spread S with recovery R: $URC^{CDS}=\frac{S}{1-R}\cdot\frac{1-e^{-(r+\frac{S}{1-R})T}}{r+\frac{S}{1-R}}$.

CIV: set $P_1^{*}=K_1\,URC^{CDS}=P(S_t,K_1,T,r,\sigma_{CIV})$ and invert with a 200-step binomial tree for American options. Assumes flat CDS term structure (constant r and lambda), a default corridor, and $K_1$ inside it (the authors flag this last one as the weakest; Appendix A derives a link for puts outside the corridor).

Tests: firm-level regressions $OIV_{i,t}=\alpha_i+\beta_iCIV_{i,t}+\beta^{CV}_i Controls_{i,t}+\varepsilon_{i,t}$ and the reverse, with option delta, open interest and maturity as controls, split by investment-grade and junk; ADF stationarity tests on spreads. Trading: $CIV_{i,t}=\beta_iOIV_{i,t}+\varepsilon_{i,t}$, z-score $(\varepsilon_{i,t}-u_i(\varepsilon_{i,t}))/\sigma_i(\varepsilon_{i,t})$ from past data (starting at the 10th observation; after Balvers et al. 2000). Sort into quintiles; long quintile 1 (lowest z) and short quintile 5 (L1-S5), plus long positive vs short negative z portfolios. CDS returns are log changes in spread, no transaction costs, 2% risk-free rate. Option strategies: deep OTM puts, delta-hedged deep OTM puts, ATM straddles, delta-hedged ATM calls. Risk checks: regressions on nonparametric risk-neutral skewness $Skew=\sigma_{i,call}(0.25)-\sigma_{i,put}(-0.25)$, a Yan (2011) jump proxy and Cremers et al. (2015) jump and volatility factors.

## Key Findings

1. The URC-based CIV tracks option-implied volatility closely: the average firm-level correlation is 79.98%, versus 31.14% for the Kelly et al. (2019) measure and 11.63% for Guo (2016). The correlation with the CDS spread is 77.87%.
2. In a univariate regression, CIV explains 66.38% of OIV variation (adjusted R^2), against 14.46% and 24.10% for the two structural-model CIVs.
3. The CIV-OIV link is strongest at short CDS maturity: mean correlation 0.899 for 1-year CIV, falling to 0.806 for 10-year CIV. CIV and OIV are closest (0.584 vs 0.600) for 1-year CDS with low moneyness.
4. The 5-year CIV-OIV spread is stationary (cointegrated) for 85% of firms (285 of 335), while CIV, OIV and realized volatility in levels mostly have unit roots.
5. The z-score L1-S5 CDS strategy on 5-year CIV earns an annualized 58.29% before costs, with a Sharpe ratio of 2.97 and a cumulative log return of 7.308. The long-positive/short-negative version has a Sharpe ratio of 2.745.
6. Using 1-year CIV the L1-S5 strategy is stronger: annualized 1.898, Sharpe ratio 3.996, cumulative 23.7966.
7. On the option side, the 5-minus-1 strategy works for deep OTM puts (Sharpe 3.435) and delta-hedged deep OTM puts (Sharpe 3.801), but not for ATM straddles or delta-hedged ATM calls. Risk-factor regressions explain little of the CDS strategy (adjusted R^2 at most 0.035), though the volatility factor is significant.

## Limitations

All returns are before transaction costs, which are large in single-name CDS and deep OTM options. CDS 'returns' are log spread changes, not P&L of a CDS position, and a fixed 2% risk-free rate is assumed. The method assumes a flat CDS term structure, a default corridor, and that the put strike lies inside it; the authors call the last assumption problematic and the corridor a possibly strong assumption. There are internal number inconsistencies: the introduction gives a full-sample CIV coefficient of 1.0362, while Section 4.1 gives 1.231; the text gives a 0.099 maximum drawdown where Table 5 shows 0.100. Sample ends in 2014. Firm-level regression and ADF details rely on tables that convert poorly. No author affiliations appear in the accepted manuscript.

## Questions Raised

- Does the CIV-OIV z-score signal survive realistic CDS bid-ask costs and P&L-based CDS returns?
- Does a CIV-OIV dislocation also predict corporate bond spread changes or excess returns for the same issuer?
- How does the signal behave after 2014, with post-crisis CDS liquidity and standardized coupons?

## Relevance to Bond Signals

CIV gives a credit-to-equity volatility translation that can be compared with option-implied volatility; a large z-scored gap is a candidate relative-value signal between credit and equity derivatives. For bonds, the same gap could be tested as a predictor of issuer spread changes, using 1-year tenors where the link is tightest.

See [[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage: Literature Review for Bond Signals]].

## Concepts

- [[concepts/credit-default-swaps|Credit Default Swaps]]
- [[concepts/credit-default-swap-spread|Credit Default Swap Spread]]
- [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]]
- [[concepts/option-implied-credit-information|Option-Implied Information in Credit Markets]]
- [[concepts/reduced-form-credit-models|Reduced-Form Credit Models]]
- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/volatility-smirk|Volatility Smirk as Informed-Trading Signal]]
- [[concepts/implied-volatility-skew|Implied Volatility Skew]]
- [[concepts/cointegration|Cointegration]]
- [[concepts/statistical-arbitrage|Statistical Arbitrage]]
- [[concepts/mean-reversion|Mean Reversion]]
- [[concepts/unit-recovery-claim|Unit Recovery Claim]]
- [[concepts/cds-implied-volatility|CDS-Implied Volatility]]

## Entities

- [[entities/yukun-shi|Yukun Shi]]
- [[entities/ding-rong-chen|Ding-Rong Chen]]
- [[entities/biao-guo|Biao Guo]]
- [[entities/yaofei-xu|Yaofei Xu]]
- [[entities/cheng-yan|Cheng Yan]]

## Related Sources

- [[sources/shi-2022-cds-options-comovement|Market Co-movement Between Credit Default Swap Curves and Option Volatility Surfaces]]
- [[sources/cao-2023-implied-vol-bond-returns|Implied Volatility Changes and Corporate Bond Returns]]
- [[sources/dafonseca-2020-cds-equity-volatility-comovement|The Co-Movement of Credit Default Swap Spreads, Equity Returns and Volatility: Evidence from Asia-Pacific Markets]]
- [[sources/hong-2025-implied-vol-cds-korea|Do Changes in the Implied Volatility of Stock Options Predict Future Changes in CDS Spreads?]]
- [[sources/kapadia-2012-limited-arbitrage-equity-credit|Limited arbitrage between equity and credit markets]]
- [[sources/avino-2024-hedging-credit-equity-options|Contingent Claims and Hedging of Credit Risk with Equity Options]]
- [[sources/carr-2011-american-puts-credit-protection|A Simple Robust Link Between American Puts and Credit Protection]]
<!-- AUTHORED REGION END -->