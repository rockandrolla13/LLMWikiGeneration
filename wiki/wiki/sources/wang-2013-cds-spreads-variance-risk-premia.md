---
authors:
- Hao Wang
- Hao Zhou
- Yi Zhou
content_hash: sha256:3f961913e47eacc64bb13b3de3bcc759fe44a0cc089e822f45f847425e7f6e4d
created: '2026-10-05T15:52:32Z'
page_id: sources/wang-2013-cds-spreads-variance-risk-premia
page_type: source
publication_date: '2013'
publication_venue: Journal of Banking and Finance 37
related:
- concepts/volatility-risk-premia
- concepts/realized-variance
- concepts/credit-default-swap-spread
- concepts/credit-spread-puzzle
- concepts/structural-models
- concepts/merton-model
- concepts/option-implied-credit-information
- concepts/leverage-ratios
- concepts/variance-risk-premium
- concepts/model-free-implied-variance
- sources/collin-dufresne-2001-determinants-credit-spread-changes
- sources/cao-2023-implied-vol-bond-returns
- sources/hong-2025-implied-vol-cds-korea
- sources/dafonseca-2020-cds-equity-volatility-comovement
- analyses/capital-structure-arbitrage-literature-review
- entities/hao-wang
- entities/hao-zhou
- entities/yi-zhou
revision_id: 1
schema_version: 2
source_hash: sha256:04f29e8d991d5152d9cd854adbf29f5983d813565a038e21fbba857809e219e5
source_path: markdown_output/wang-2013-cds-spreads-variance-risk-premia.md
source_type: paper
sources: []
tags:
- variance-risk-premium
- credit-default-swaps
- implied-variance
- realized-variance
- systematic-risk
- structural-models
- equity-credit-linkage
- credit-spread-puzzle
title: Credit Default Swap Spreads and Variance Risk Premia
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: 16b48e33-ac6a-5898-8b00-aeaf88f805b8
version_read: 'Federal Reserve FEDS working paper 2011-02 (title page: first draft
  August 2009, this version October 2010). The published JBF 2013 version may differ;
  all figures here come from the FEDS draft.'
year: 2013
---

<!-- AUTHORED REGION START -->
# Credit Default Swap Spreads and Variance Risk Premia

**Authors:** Hao Wang, Hao Zhou, Yi Zhou · **Year:** 2013 · **Venue:** Journal of Banking and Finance 37
**Version read:** Federal Reserve FEDS working paper 2011-02 (title page: first draft August 2009, this version October 2010). The published JBF 2013 version may differ; all figures here come from the FEDS draft.

## Summary

The paper asks whether a firm's own variance risk premium explains its CDS spread. The variance risk premium (VRP) is the gap between the option-implied variance of the firm's stock and a forecast of its realised variance. The idea is that this gap reflects the firm's exposure to systematic variance risk, since idiosyncratic variance should cancel out between the two.

Firm VRP is a strong explanatory variable for 5-year CDS spread levels. On its own it explains about a third of the variation across 382 firms from 2001 to 2008. It stays significant next to leverage, the market VRP, rates, bond-market spreads and firm accounting controls. Once firm VRP is in, the market VRP turns negative. Leverage and firm VRP are the two strongest variables.

The link is stronger for weaker credits and for longer CDS maturities. It is also stronger when the implied variance is model-free, using all strikes, rather than from a single moneyness. VRP gains power at monthly and quarterly frequency, while raw implied variance does better at weekly frequency.

Several checks support a systematic-risk reading. VRP has a larger first principal component than implied or expected variance. Aggregate VRP Granger-causes implied and expected variance, but not the reverse. Firm VRP betas on market VRP price the cross-section of average VRP. A simulated structural model with stochastic asset variance reproduces the pattern, while a Merton model does not.

## Data

- Markit single-name CDS, January 2001 to September 2008; USD contracts on US non-financial, non-utility, non-government entities; subordinated contracts dropped. Benchmark is 5-year Modified Restructuring; 1-10 year maturities used for robustness.
- After matching: more than 22,000 firm-month observations on 382 entities; ratings span AAA to CCC, mostly A, BBB and BB.
- Equity options from Ivy DB OptionMetrics (arbitrage-violating quotes removed); dividends from CRSP.
- Realised variance from TAQ 15-minute returns, aggregated from daily to monthly.
- Firm balance sheets from Compustat (quarterly); swap rates, CMT yields and Moody's Aaa/Baa yields from the Federal Reserve; S&P 500 returns from CRSP; market VRP from Zhou (2009).
- Monthly end-of-month matching for the main tests; weekly and quarterly for frequency checks.

## Method

Model-free implied variance from call prices across strikes (CRR lattice used only to map American prices to a smooth implied-volatility curve and back):
$$IV_{i,t}\equiv E^Q_t[\mathrm{Var}_i(t,t+T)]=2\int_0^\infty\frac{C_i(t+T,K)/B(t,t+T)-\max[0,S_{i,t}/B(t,t+T)-K]}{K^2}\,dK.$$
Realised variance from intraday log prices:
$$RV_{i,t}=\sum_{j=1}^{n}\big[s_{i,t-1+j/n}-s_{i,t-1+(j-1)/n}\big]^2.$$
Expected (physical) variance is the fitted value of a one-lag forecast regression $RV_{i,t+1}=\alpha+\beta IV_{i,t}+\gamma RV_{i,t}+\epsilon_{i,t+1}$:
$$EV_{i,t}\equiv E^P_t[\mathrm{Var}_i(t,t+T)]=\hat\alpha+\hat\beta IV_{i,t}+\hat\gamma RV_{i,t},\qquad VRP_{i,t}=IV_{i,t}-EV_{i,t}.$$
Benchmark panel regression with Petersen (2009) firm-and-time clustered errors:
$$CDS_{i,t}=\alpha+\beta_1VRP_{i,t}+\beta_2MVRP_t+\beta_3LEV_{i,t}+\beta_4S\&P_t+\beta_5r_t+\beta_6DPS_t+\beta_7STS_t+\beta_8ATO_{i,t}+\beta_9PE_{i,t}+\beta_{10}MB_{i,t}+\beta_{11}ROA_{i,t}+\beta_{12}SALE_{i,t}+\varepsilon_{i,t},$$
where LEV is book debt over book debt plus market equity, r the one-year swap rate, DPS the Baa-Aaa spread, STS the 5-year swap-Treasury spread, and the rest are accounting controls.

Extensions: splits by rating group (AAA-A, BBB, BB-CCC) and CDS maturity; VRPs built from OTM/ATM/ITM puts and calls; horse races of VRP, IV and EV; weekly/monthly/quarterly frequency comparison; Granger causality on market-level VRP, IV and EV with 3 lags; principal components of firm VRP, IV and EV; a two-pass Fama-MacBeth-style test of firm VRP on market VRP versus a CAPM test on equity returns; and 60-month simulations of a BBB firm under a Merton model and under a stochastic-variance (square-root) asset model.

## Key Findings

1. In a univariate regression, firm VRP has a t-statistic of 10.03 and an adjusted R-squared of 34%; a one-standard-deviation rise in VRP (21.57) raises the 5-year CDS spread by 60 bp.
2. With all controls the VRP coefficient falls only from 2.78 to 2.29 (t = 9.21). Adjusted R-squared goes from 0.35 with market VRP to 0.47 with leverage and 0.49 with all controls.
3. Firm VRP subsumes market VRP: adding firm VRP drives the market VRP coefficient negative.
4. VRP coefficients for BB-CCC names are almost five to seven times those for AAA-A names and at least twice those for BBB; coefficients and R-squared rise with CDS maturity from 1 to 10 years.
5. The t-statistic on VRP rises from 6.44 to 10.41 as data frequency moves from weekly to quarterly, consistent with a slow-moving systematic component.
6. The first principal component explains 78% of firm VRP variation versus 54% for implied variance and 57% for expected variance; aggregate VRP Granger-causes implied and expected variance but not the reverse.
7. In the cross-section, firm VRP betas on market VRP price average firm VRP with a slope of 1.17 against an average market VRP of 1.20 (adjusted R-squared 14.05%); the matching CAPM test gives 0.03% against a 0.46% market return.

## Limitations

- Read from the FEDS 2011-02 draft; the published JBF 2013 version may differ.
- Regressions explain contemporaneous spread levels; despite the paper's use of 'predict', there is no out-of-sample forecast of spread changes or returns.
- Sample ends in September 2008, so it misses the worst of the crisis and the post-Big-Bang CDS market.
- Expected variance depends on a single linear forecast model; VRP inherits its errors.
- Granger tests at firm level were noisy and insignificant; the causality result is for the aggregate only.
- Monthly matching of quarterly balance-sheet data makes leverage stale relative to VRP.
- The structural-model support is a single simulated BBB firm, not a fitted model.

## Questions Raised

- Do changes in firm VRP forecast next-month CDS or bond spread changes, beyond explaining levels?
- How much of firm VRP is a jump or skew premium rather than a diffusive variance premium?
- Does firm VRP keep its edge over implied variance alone after 2008, when option and CDS liquidity changed?
- Can a firm's beta to market VRP be used directly as a systematic credit-risk exposure in bond portfolios?

## Relevance to Bond Signals

Firm-level VRP (model-free implied variance minus forecast realised variance) is a candidate issuer feature that captures systematic variance exposure not in leverage or rating, with larger loadings for high-yield and longer tenors. For bond signals it can serve as a fair-value input for spread levels and, at monthly or quarterly horizons, a slower-moving complement to raw implied volatility.

See [[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage: Literature Review for Bond Signals]].

## Concepts

- [[concepts/volatility-risk-premia|Volatility Risk Premia (VIRP)]]
- [[concepts/realized-variance|Realized Variance]]
- [[concepts/credit-default-swap-spread|Credit Default Swap Spread]]
- [[concepts/credit-spread-puzzle|Credit Spread Puzzle]]
- [[concepts/structural-models|Structural Models]]
- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/option-implied-credit-information|Option-Implied Information in Credit Markets]]
- [[concepts/leverage-ratios|Leverage Ratios]]
- [[concepts/variance-risk-premium|Variance Risk Premium]]
- [[concepts/model-free-implied-variance|Model-Free Implied Variance]]

## Entities

- [[entities/hao-wang|Hao Wang]]
- [[entities/hao-zhou|Hao Zhou]]
- [[entities/yi-zhou|Yi Zhou]]

## Related Sources

- [[sources/collin-dufresne-2001-determinants-credit-spread-changes|The Determinants of Credit Spread Changes]]
- [[sources/cao-2023-implied-vol-bond-returns|Implied Volatility Changes and Corporate Bond Returns]]
- [[sources/hong-2025-implied-vol-cds-korea|Do Changes in the Implied Volatility of Stock Options Predict Future Changes in CDS Spreads?]]
- [[sources/dafonseca-2020-cds-equity-volatility-comovement|The Co-Movement of Credit Default Swap Spreads, Equity Returns and Volatility: Evidence from Asia-Pacific Markets]]
<!-- AUTHORED REGION END -->