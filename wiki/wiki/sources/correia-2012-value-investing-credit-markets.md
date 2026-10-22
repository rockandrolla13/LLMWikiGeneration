---
authors:
- Maria Correia
- Scott Richardson
- İrem Tuna
content_hash: sha256:024438d782f488890ebb8846f8257061689fbf9b4ba3a511c51ecef1f3008da4
created: '2026-10-22T21:10:31Z'
doi: 10.1007/s11142-012-9191-x
page_id: sources/correia-2012-value-investing-credit-markets
page_type: source
publication_date: '2012'
publication_venue: Review of Accounting Studies
related:
- concepts/credit-relative-value
- concepts/distance-to-default
- concepts/merton-model
- concepts/structural-models
- concepts/credit-spread-puzzle
- concepts/credit-spread-forecasting
- concepts/credit-spread-changes
- concepts/mean-reversion
- concepts/equity-momentum-in-credit
- concepts/value-premium
- concepts/risk-vs-mispricing
- concepts/duration-times-spread
- concepts/factor-signals-in-credit
- concepts/credit-default-swap-spread
- concepts/systematic-credit-relative-value
- concepts/corporate-credit-fundamentals
- concepts/default-model-implied-spread-value-signal
- concepts/bankruptcy-hazard-model
- sources/bharath-2008-forecasting-default-merton-distance-to-default
- sources/collin-dufresne-2001-determinants-credit-spread-changes
- sources/bendor-2007-dts
- sources/bendor-2021-systematic-investing-in-credit
- sources/houweling-2017-factor-investing
- sources/huang-2025-global-credit-spread-puzzle
- entities/maria-correia
- entities/scott-richardson
- entities/irem-tuna
- entities/london-business-school
- entities/moodys
revision_id: 1
schema_version: 2
source_hash: sha256:ee83a35f227f4e7509e01346ac97410d64b4b85ff87d3826b26970992fa344c1
source_path: markdown_output/correia-2012-value-investing-credit-markets.md
source_type: paper
sources: []
tags:
- credit-value
- default-prediction
- distance-to-default
- corporate-bonds
- cds
- credit-relative-value
- fama-macbeth
- structural-credit-model
- accounting-signals
title: Value Investing in Credit Markets
updated: '2026-10-22T21:10:31Z'
updated_by: op_0cdb8cc1f169
uuid: c0b8d271-79fe-5f79-823a-fed181b6f2a8
version_read: Pre-publication manuscript (SSRN abstract 1800212). The PDF metadata
  title is 'CONFERENCE_RAST_EM2413_Final (2)', created 16 Oct 2012. The acknowledgements
  thank Jim Ohlson (editor), a discussant and a referee. There are no journal page
  numbers.
year: 2012
---

<!-- AUTHORED REGION START -->
# Value Investing in Credit Markets

**Authors:** [[entities/maria-correia|Maria Correia]], [[entities/scott-richardson|Scott Richardson]], [[entities/irem-tuna|İrem Tuna]] · **Year:** 2012 · **Venue:** Review of Accounting Studies
**Version read:** Pre-publication manuscript (SSRN abstract 1800212). The PDF metadata title is 'CONFERENCE_RAST_EM2413_Final (2)', created 16 Oct 2012. The acknowledgements thank Jim Ohlson (editor), a discussant and a referee. There are no journal page numbers.

**Converted text:** `markdown_output/correia-2012-value-investing-credit-markets.md`

## Summary

The paper asks whether credit markets fully price the default information in accounting and equity data. It builds four monthly forecasts of one-year physical default probability. Two are its own (a crude distance to default and a hazard model), one is Bharath and Shumway (2008), and one is the Moody's/KMV EDF.

Each default probability is turned into a theoretical five-year credit spread through a Kealhofer-style risk-neutral mapping. Recovery, the market Sharpe ratio and asset correlation are held at fixed constants. Better default forecasters also explain more of the cross-section of bond and CDS spread levels. EDF does best on both counts.

The value signal is credit relative value (CRV): the log of the actual spread over the theoretical spread. CRV mean-reverts strongly at the bond level. High-CRV bonds (spread wide of the model) earn higher credit returns over the next one to three months. The effect survives equity characteristics, eight risk factors, industry demeaning and a spread-level residualisation.

Quintile long/short portfolios earn monthly hedge returns of about 41 to 77 bp in the first month. The authors estimate institutional round-trip costs of 52 to 70 bp. They conclude that the returns cover costs for an institution but not for a retail investor.

## Data

- Bankruptcy sample: Chapter 7 and Chapter 11 filings, 1980 to end-2010, from four sources (Beaver, Correia and McNichols 2012; bankruptcy.com; Mergent FISD; LoPucki's database).
- Intro reports 1,767 bankrupt and 194,981 nonbankrupt firm-year observations. The conclusion says 1,797 bankruptcies. The document does not reconcile the two.
- Financial firms with SIC 6021, 6022, 6029 and 6036 are excluded (following Shumway 2001). Independent variables are winsorised at 1% and 99%.
- Inputs: quarterly Compustat accounting data, assumed available two months after fiscal quarter-end. Monthly CRSP market data. Default probabilities are re-estimated monthly over 367 months (January 1980 to July 2010).
- Moody's/KMV supplied point-in-time EDF history. EDF data start in January 1997.
- Bonds: monthly Merrill Lynch North American IG and HY index constituents, January 1997 onward. One bond per issuer: duration closest to five years, hard band 3 to 8 years, largest market value if several qualify. Option-adjusted spreads are used. About 2,000 bonds.
- CDS: 5-year senior USD contracts with modified restructuring from DataStream, January 2005 to April 2010. The data section gives 484 issuers and 25,050 firm-months. The conclusion says 453 CDS contracts.
- Return regressions and portfolio tests use 149 months, January 1997 to May 2009.

## Method

Default barrier and asset value. The barrier is $X_{i,t}$ = short-term debt (DLCQ) + 0.5 x long-term debt (DLTTQ) at the latest fiscal quarter, following Bharath and Shumway (2008). Asset value $V_{A_{i,t}}$ is CRSP market equity plus the book value of debt. Asset volatility $\sigma_{A_{i,t}}$ is the standard deviation of monthly stock returns over the prior twelve months, de-levered with market leverage. Drift is ignored.

Structural frame (eqs. 1-3). Default is $\ln V_{A_{i,t}} < \ln X_{i,t}$. With geometric Brownian asset dynamics this gives $PD_{i,t}=\Pr\big[(\ln(V_{A_{i,0}}/X_{i,t})+(\mu_i-\sigma^2_{A_{i,t}}/2)t)/(\sigma_{A_{i,t}}\sqrt{t}) < -\varepsilon_{i,t}\big]$ (inequality direction is our reading; the converted markdown drops the equation and the PDF text layer loses the operator).

Four default models, each a discrete-time hazard (Shumway 2001) estimated with an expanding window and a logistic link, $Prob=e^{score}/(1+e^{score})$. The dependent variable is 1 if the firm files for bankruptcy within one year of month-end. (1) D2D: $E[PD^{D2D}_{i,t}]=f\big(\ln(V_{A_{i,0}}/X_{i,t})/(\sigma_{A_{i,t}}\sqrt{t})\big)$ (eq. 10). (2) BCM-BOTH (Beaver, Correia and McNichols 2012), eq. 11: $f(NROAI, ROA, TL/TA, EBIT/TL, RETURNS, \sigma_E, LRSIZE)$ plus interactions of NROAI with ROA, TL/TA and EBIT/TL. NROAI flags negative ROA. ROA is trailing twelve-month NIQ + XINTQ(1-tax rate) over average total assets. TL/TA is LTQ/ATQ. EBIT/TL is trailing OIBDPQ over average total liabilities. RETURNS is the prior twelve-month equity return. $\sigma_E$ is the twelve-month standard deviation of CAPM excess returns. LRSIZE is log of firm market cap over total market cap. (3) BS (Bharath and Shumway 2008), eq. 12: $f(NI/TA, RETURNS, 1/\sigma_E, X, SIZE, \pi_{D2D})$, where $\pi_{D2D}=N(-D2D)$. (4) EDF from Moody's/KMV, used directly as the probability. Five other models (Altman, Ohlson, BCM accounting-only, BMR market-only, ratings) were tested and dropped as inferior.

Out-of-sample accuracy uses monthly ROC/AUC on a constant sample. AUC differences are tested over 367 months with Newey-West correction for eleven overlapping months.

Theoretical spread (eqs. 4-7). Five-year cumulative physical PD: $CPD_{i,t}=1-(1-PD_{i,t})^5$. Risk-neutral: $CQDF_{i,t}=N\big[N^{-1}(CPD_{i,t})+\lambda\sqrt{r^2_{i,t}}\sqrt{T}\big]$ (eq. 7, read from the PDF). Spread: $CS^*_{i,t}=-\frac{1}{T}\ln[1-(1-R_{i,t})\,CQDF_{i,t}]$ (eq. 6), derived by equating $e^{-rT}[(1-CQDF)+R\cdot CQDF]$ with $e^{-(r+CS)T}$. Base parameters: $R=40\%$, market Sharpe ratio $\lambda=0.5$, asset correlation 40%, $T=5$.

Value signal. $CRV_{i,t}=\ln(CS_{i,t}/CS^*_{i,t})$, computed once per default model. Positive CRV means the market spread is wide of the model spread (the bond is cheap).

Mean reversion (eq. 8), per bond with at least 12 months: $CRV_{i,t+K}-CRV_{i,t+K-1}=\alpha_i+\delta_i CRV_{i,t}+\varepsilon_{i,t}$ for K = 1..6. A cumulative six-month version regresses $CRV_{i,t+6}-CRV_{i,t}$ on $CRV_{i,t}$, with Newey-West errors over five lags.

Credit return (eq. 13, Lok and Richardson 2011): $RET_{i,t\to t+1}\approx \tfrac{1}{12}CS_{i,t}-Duration_{i,t}\,\Delta CS_{i,t\to t+1}$, from the protection seller's view. It correlates above 0.95 with Merrill Lynch total returns.

Predictive regression (eq. 14), monthly Fama-MacBeth, run separately for each horizon month k = 1..6 (not cumulated): $RET_{i,t+k}=\gamma_t+\gamma_{CRV}CRV_{i,t}+\gamma_{MOMS}MOMS+\gamma_{MOML}MOML+\gamma_{BTM}BTM+\gamma_{SIZE}SIZE+\gamma_{E/P}E/P+\gamma_{BETA}BETA+\varepsilon$. Estimation is WLS with weights $-\ln(CS_{i,t})$, which down-weights wide-spread bonds. MOMS is last month's equity return. MOML is a three-month half-life exponentially weighted return over the prior eleven months. BETA uses 60 months (minimum 36).

Portfolios. Each month, bonds are sorted into CRV quintiles. Returns are $-\ln(CS)$ risk-weighted and reported separately for each of months 1 to 6 ahead. Hedge = top quintile minus bottom quintile, with monthly rebalancing and no costs. Sharpe ratio = FM t-stat x $\sqrt{12}/\sqrt{149}$ (Lewellen 2010). The hedge series is regressed on dRP (BAA minus 10y change), dTS (10y minus 2y change), dVIX, dIP, MKT, SMB, HML and MOM (eq. 15).

Robustness: CDS spreads, Merrill Lynch total and excess returns, industry demeaning, Moody's broad default events, time-varying correlation (60-month window, floor 0.1, cap 0.7), $\lambda$ from 0.3 to 0.6, residualising CRV on spread level each month, and IG versus HY splits on S&P-rated issuers.

## Key Findings

1. All four default models classify bankruptcy well out of sample, and EDF ranks first. The AUC gaps between models are small and not statistically significant.
2. Theoretical spreads sit below actual bond spreads in most firm-months. This matches the credit spread puzzle. CDS shows the same pattern, at about 80% of cases.
3. Model spreads explain a large share of cross-sectional spread levels. EDF-based spreads correlate best with actual spreads. Models that forecast default better also explain spreads better.
4. CRV mean-reverts at the bond level. About two thirds of the gap between actual and theoretical spread closes within six months. Over 70% of bonds show significant cumulative reversion.
5. In Fama-MacBeth regressions with equity controls, CRV positively predicts next-month credit returns for all four models. The effect fades by month three. Short-horizon equity momentum (MOMS) is the strongest control.
6. Quintile hedge portfolios earn 41 to 77 bp in the first month after formation. BS gives the highest Sharpe ratio, and EDF the lowest. Sharpe ratios fall to 0.25-1.20 by month three.
7. Eight risk factors do not explain the hedge returns, and the monthly alphas stay large. The hedge loads positively on changes in the BAA-Treasury spread and negatively on market returns and industrial production. The authors trace this to a flight-to-quality tilt toward low-spread issuers.
8. Removing the spread-level tilt does not weaken the signal. Residualising CRV on spread level gives slightly stronger predictability, so the authors reject a carry explanation. The effect holds in both IG and HY and is sometimes stronger in HY.
9. Estimated institutional costs for the long/short portfolio are 52 to 70 bp. Cumulative bond hedge returns are 113 bp over three months and 169 bp over six. CDS gives 87 and 139 bp. Costs are covered for institutions but not for retail trades.

## Limitations

- Recovery (40%), market Sharpe ratio (0.5) and asset correlation (40%) are cross-sectional constants. Seniority and industry differences in recovery are not modelled.
- The default barrier (short-term debt plus half of long-term debt) ignores off-balance-sheet debt, credit lines, refinancing and convertibility. Asset value uses book debt, and drift is ignored.
- Asset volatility is backward-looking (twelve months of equity returns). The authors do not use option-implied volatility.
- Default is calibrated on bankruptcies only. The broader Moody's default set is used only as a robustness check.
- Returns come from a spread-and-duration approximation and ignore transaction costs. Cost estimates come from prior literature, so net profitability is uncertain.
- Sample counts are not consistent across the paper. Bankruptcies are given as 1,767 or 1,797, and CDS coverage as 484 issuers or 453 contracts.
- Many robustness results (CDS, industry demeaning, IG/HY split, carry residualisation, boom/bust) are reported in the text and not tabulated.

## Questions Raised

- Does CRV still work in post-2010 TRACE-era data, with realistic bid-ask costs by IG/HY bucket?
- How much of the CRV return comes from the equity-momentum content of the default model (as in BS) rather than from the fundamental anchor?
- Would issuer-specific recovery, option-implied asset volatility or market debt values make the theoretical spread a sharper anchor?
- How does CRV interact with DTS-scaled carry, and with spread-to-peers relative-value signals?
- Is the signal stronger after 2002, when Moody's acquired KMV? The paper notes higher EDF predictive power then but reports no numbers.

## Relevance to Bond Signals

This is a ready-to-build fundamental value signal for corporate bonds and CDS. It is the log ratio of the market spread to a structural or hazard-model spread, with fixed recovery, Sharpe ratio and correlation inputs. Use one bond per issuer near five-year duration, sort into quintiles monthly, risk-weight by $-\ln(CS)$, and expect most of the payoff in months one to three. Residualise CRV on spread level so the signal does not double as a quality tilt. Control for lagged equity returns, because short equity momentum is a strong separate predictor of credit returns.

## Concepts

- [[concepts/credit-relative-value|Credit Relative Value]]
- [[concepts/distance-to-default|Distance to Default]]
- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/structural-models|Structural Models]]
- [[concepts/credit-spread-puzzle|Credit Spread Puzzle]]
- [[concepts/credit-spread-forecasting|Credit Spread Forecasting]]
- [[concepts/credit-spread-changes|Credit Spread Changes]]
- [[concepts/mean-reversion|Mean Reversion]]
- [[concepts/equity-momentum-in-credit|Equity Momentum in Credit]]
- [[concepts/value-premium|Value Premium]]
- [[concepts/risk-vs-mispricing|Risk-vs-Mispricing Debate]]
- [[concepts/duration-times-spread|Duration Times Spread (DTS)]]
- [[concepts/factor-signals-in-credit|Factor Signals in Credit]]
- [[concepts/credit-default-swap-spread|Credit Default Swap Spread]]
- [[concepts/systematic-credit-relative-value|Systematic Credit Relative Value]]
- [[concepts/corporate-credit-fundamentals|Corporate Credit Fundamentals]]
- [[concepts/default-model-implied-spread-value-signal|Default-Model-Implied Spread Value Signal]]
- [[concepts/bankruptcy-hazard-model|Bankruptcy Hazard Model]]

## Entities

- [[entities/maria-correia|Maria Correia]]
- [[entities/scott-richardson|Scott Richardson]]
- [[entities/irem-tuna|İrem Tuna]]
- [[entities/london-business-school|London Business School]]
- [[entities/moodys|Moody's (Moody's/KMV)]]

## Related Sources

- [[sources/bharath-2008-forecasting-default-merton-distance-to-default|Forecasting Default with the Merton Distance to Default Model]]
- [[sources/collin-dufresne-2001-determinants-credit-spread-changes|The Determinants of Credit Spread Changes]]
- [[sources/bendor-2007-dts|DTS (Duration Times Spread) - A New Measure of Spread Exposure in Credit Portfolios]]
- [[sources/bendor-2021-systematic-investing-in-credit|Systematic Investing in Credit]]
- [[sources/houweling-2017-factor-investing|Factor Investing in the Corporate Bond Market]]
- [[sources/huang-2025-global-credit-spread-puzzle|The Global Credit Spread Puzzle]]
<!-- AUTHORED REGION END -->