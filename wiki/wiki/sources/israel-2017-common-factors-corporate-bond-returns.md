---
authors:
- Ronen Israel
- Diogo Palhares
- Scott Richardson
content_hash: sha256:2c50ef7b0945d490dd6e0f364473f1e555754ec8bb4f9c2487197528c33be48a
created: '2026-10-22T21:10:31Z'
doi: 10.2139/ssrn.2576784
page_id: sources/israel-2017-common-factors-corporate-bond-returns
page_type: source
publication_date: '2017'
publication_venue: Journal of Investment Management (forthcoming at the version read)
related:
- concepts/style-premia
- concepts/factor-investing
- concepts/factor-signals-in-credit
- concepts/corporate-bonds
- concepts/low-risk-anomaly
- concepts/bond-momentum
- concepts/equity-momentum-in-credit
- concepts/cross-sectional-momentum
- concepts/value-premium
- concepts/credit-relative-value
- concepts/duration-times-spread
- concepts/credit-risk-premium
- concepts/merton-model
- concepts/distance-to-default
- concepts/volatility-targeting
- concepts/limits-to-arbitrage
- concepts/risk-vs-mispricing
- concepts/fama-french-factors
- concepts/leverage-ratios
- concepts/constrained-optimization
- concepts/option-adjusted-spread
- concepts/fama-macbeth-regression
- concepts/gross-profitability
- sources/houweling-2017-factor-investing
- sources/jostova-2013-momentum
- sources/bendor-2021-systematic-investing-in-credit
- sources/bharath-2008-forecasting-default-merton-distance-to-default
- sources/haesen-2017-momentum-spillover
- sources/dickerson-2026-corporate-bond-factor-replication-crisis
- entities/ronen-israel
- entities/diogo-palhares
- entities/scott-richardson
- entities/aqr-capital-management
- entities/london-business-school
revision_id: 1
schema_version: 2
source_hash: sha256:e3f55e9b04bd13fc0dd515698622504852c0133f1aaac0ce30036ce7b23c5c09
source_path: markdown_output/israel-2017-common-factors-corporate-bond-returns.md
source_type: paper
sources: []
tags:
- corporate-bonds
- credit-factors
- carry
- value
- momentum
- defensive
- fama-macbeth
- long-only-optimisation
- mispricing
- style-premia
title: Common Factors in Corporate Bond Returns
updated: '2026-10-22T21:10:31Z'
updated_by: op_0cdb8cc1f169
uuid: 44ee182c-3d68-5963-b080-13b6ad5e5a18
version_read: 'SSRN working paper 2576784, dated June 5, 2017, marked ''Forthcoming
  in the Journal of Investment Management''. Earlier title: ''Investing with style
  in corporate bonds''.'
year: 2017
---

<!-- AUTHORED REGION START -->
# Common Factors in Corporate Bond Returns

**Authors:** [[entities/ronen-israel|Ronen Israel]], [[entities/diogo-palhares|Diogo Palhares]], [[entities/scott-richardson|Scott Richardson]] · **Year:** 2017 · **Venue:** Journal of Investment Management (forthcoming at the version read)
**Version read:** SSRN working paper 2576784, dated June 5, 2017, marked 'Forthcoming in the Journal of Investment Management'. Earlier title: 'Investing with style in corporate bonds'.

**Converted text:** `markdown_output/israel-2017-common-factors-corporate-bond-returns.md`

## Summary

Israel, Palhares and Richardson test whether four characteristics known from other markets predict the cross-section of US corporate bond excess returns. The four are carry, defensive (low risk or quality), momentum and value. The sample is a one-bond-per-issuer panel of BAML investment-grade and high-yield index constituents, monthly from January 1997 to April 2015.

Each characteristic is built from simple, transparent measures. Carry is the option-adjusted spread. Defensive combines low market leverage, high gross profitability and low duration. Momentum combines six-month bond excess return and six-month issuer equity return. Value is the residual of log spread on default-risk anchors. The authors demean non-carry, non-duration characteristics within five duration-times-spread (DTS) quintiles so that long-short portfolios sit closer to market neutral.

Value and momentum carry the strongest predictive power in Fama-MacBeth regressions. Defensive loses significance once value and momentum enter. Carry is weak alone and loads heavily on the credit market factor. An equal-risk combination of all four earns a long-short Sharpe ratio of 2.19 and an alpha that equity factors and market premia do not explain. A constrained long-only version beats a value-weighted benchmark by 2.20% a year net of estimated costs, an information ratio of 0.86.

The premia do not look like macroeconomic risk compensation. The combined portfolio behaves as a hedge against falling growth and rising volatility. Mispricing evidence is strongest for momentum. Momentum pays more among small, thinly covered, less institutionally held bonds, and it predicts analyst sales revisions.

## Data

- Universe: all constituents of the BAML US Corporate Master (investment grade) and US High Yield Master indices, monthly, January 1997 to April 2015.
- One representative bond per issuer per month, following Haesen et al. (2013): senior only, the issuer's dominant rating bucket by amount outstanding, prefer 5-15 year maturity, prefer bonds at most two years old, then the largest amount outstanding.
- Sample size: 274,665 bond-months, 11,804 bonds, 4,296 firms. The average month holds 1,247 bonds and $573 billion notional, 59% IG and 41% HY by notional.
- BAML supplies OAS, option-adjusted (effective) duration, total returns and excess returns over a duration-matched Treasury. Ratings use S&P, coded AAA=1 to D=10.
- About 48% of the universe links to Compustat via CUSIP and ticker. Equity returns, leverage, profitability and default probability need this link.
- Average issue: OAS 386 bp, duration 5.1 years, $437 million outstanding, 7.8 years to maturity, age percent 28%. Median OAS is 302 bp.
- Mispricing proxies: I/B/E/S analyst coverage, Lipper eMAXX institutional ownership, bond issue size, and a Markit shorting fee score from 0 to 5.
- Macro and factor data: FRED (VIX, industrial production, CPI), Ken French library (SMB, HML, UMD), AQR (QMJ), Fed flow of funds for broker-dealer leverage. Analyst sales forecasts (FY1, FY2) for January 2001 to April 2015.

## Method

Return target. The dependent variable is the monthly bond excess return over a duration-matched Treasury, as reported by BAML. All characteristics are measured at month end $t$ and predict the return over month $t+1$. Portfolios rebalance monthly.

Carry. Carry is the bond's option-adjusted spread, $\text{CARRY}_{i,t} = \text{OAS}_{i,t}$. The authors prefer OAS to yield because they target returns over key-rate-duration-matched Treasuries. They note OAS equals carry only on a flat credit curve. It understates carry on an upward-sloping curve, which most issuers have. They reject issuer-curve fitting as model dependent and opaque.

Defensive. Defensive combines three measures. (1) Market leverage, $\text{LEV}_{i,t} = \frac{ND}{ND + ME}$ with $ND$ = book debt + minority interest + preferred stock - cash, and $ME$ = equity market capitalisation. Accounting data assume a six-month reporting lag. (2) Gross profitability, gross profits over assets (Novy-Marx, 2013). (3) Low effective duration from BAML. Low leverage, high profitability and low duration are the safe side. The paper states the low-duration direction explicitly; the leverage and profitability directions follow from its argument that leverage raises default risk and profitability signals safety. The authors exclude beta and volatility because DTS mixes duration (low is good) and spread (high is good), two effects that cancel.

Momentum. Credit momentum is the trailing six-month cumulative bond excess return. Equity momentum is the trailing six-month cumulative issuer equity return. No skip month is stated. Higher past return is the long side.

Value. Value compares spread to a default-risk anchor. A cheap bond has a high spread relative to default risk. Structural value is the residual $\varepsilon_i$ from a monthly cross-sectional regression $\log \text{OAS}_i = a + b \log PD_i + \varepsilon_i$ (our notation; the source states it in words). The text says $PD$ follows Bharath and Shumway (2008), while Table A.1 cites Shumway (2001). Empirical value is the residual from $\log \text{OAS}_i = a + b_1 \log \text{Dur}_i + b_2 \text{Rating}_i + b_3 \sigma^{12m}_i + \varepsilon_i$ (our notation; the source states it in words, and does not say whether rating and volatility enter in logs). $\sigma^{12m}$ is the volatility of bond excess returns over the last 12 months. The empirical anchor exists for bonds without listed equity. High residual is the long side.

Combining measures within a theme. Where a theme has several measures, the authors combine standardised measures with equal-risk weights. A missing standardised measure gets a score of zero, so the composite exists for any bond with at least one measure. The exact standardisation used for portfolio sorts is not stated.

Beta neutralisation. Ex-ante beta is DTS, $\text{Dur}_i \times \text{OAS}_i$. Each month the authors sort bonds into five DTS quintiles and demean each characteristic within its quintile. Carry and duration skip this step, because demeaning them on DTS would mechanically mix high carry with low duration. The step lowers but does not remove the negative correlation of other themes with carry.

Quintile portfolios. Each month bonds are sorted into quintiles on the (demeaned) characteristic. Returns within quintiles are value weighted; equal weighting gives the same inferences. The long-short portfolio is Q5 minus Q1. A constant-volatility version scales the Q5-Q1 return to a 5% annual target using its 24-month realised volatility: $r^{CV}_t = r_t \cdot \frac{5\%}{\hat\sigma_{24m,t}}$ (our notation; the source states it in words). From January 1997 to December 1998 the scalar is fixed at its January 1999 value, a look-ahead the authors disclose.

Combined score. For each characteristic the authors build a portfolio with weights linear in cross-sectional ranks (Asness et al., 2014). They scale each by $5\%/\hat\sigma_{24m}$. The combined weight is the equal-weighted average of the four scaled weight vectors, $w^{COMBO}_i = \frac{1}{4}\sum_k \frac{5\%}{\hat\sigma_{k,24m}} w^{rank}_{k,i}$ (our notation; the source states it in words). They justify equal weights as a 1/N rule applied to similarly risky characteristic portfolios.

Fama-MacBeth tests. Each month they run $R_{i,t+1} = \alpha + \beta_1 \text{CARRY}_{i,t} + \beta_2 \text{DEF}_{i,t} + \beta_3 \text{MOM}_{i,t} + \beta_4 \text{VALUE}_{i,t} + \gamma Z + \varepsilon_{i,t+1}$. Each characteristic is rank-normalised: rank, subtract the mean rank, divide by the rank standard deviation, fill missing with zero. Coefficients read as the one-month return difference per one standard deviation of rank. Controls $Z$ are a 12-month rolling credit-market beta, rating, duration and age percent (days since issue over original maturity in days).

Spanning tests. Constant-volatility long-short returns are regressed on EQUITY, TSY, CREDIT, SMB, HML, UMD and QMJ. Macro tests add monthly changes in log VIX, log industrial production and log CPI. A quarterly test adds the change in log broker-dealer leverage (Adrian et al., 2014).

Long-only portfolio. Each month a linear programme maximises exposure to the combined score, $\max_w \sum_i w_i \, COMBO_i$ (our notation; the objective is an omitted image in the source, and the text says it maximises exposure to the combined score). Constraints: $w_i \ge 0$; $|w_i - b_i| \le 0.25\%$; full investment; monthly turnover at most 10%; each trade at least $100,000; portfolio OAS within 50 bp of the benchmark; portfolio duration within 0.50 years of the benchmark. The benchmark $b$ is value weighted over the one-bond-per-issuer universe, IG and HY together. Net returns subtract costs by rating and maturity from Table 1 of Chen, Lesmond and Wei (2007). Active return is the portfolio less a 24-month rolling beta times the benchmark.

## Signal Definitions

**Carry (OAS)** (carry). Bond option-adjusted spread as reported by BAML. Higher OAS is the long side. Not demeaned within DTS quintiles.
- Inputs: OAS (BAML)
- Frequency: monthly
- Notes: Standalone Fama-MacBeth coefficient 0.00 (t = 1.0); 0.14 (t = 2.3) jointly. Long-short alpha insignificant after the CREDIT factor. Exact proxy for carry only on a flat credit curve.

**Defensive: market leverage** (defensive / low risk). Net debt / (net debt + equity market cap), with net debt = book debt + minority interest + preferred stock - cash. Low leverage is the safe (long) side; direction implied by the paper's default-risk argument.
- Inputs: Compustat balance sheet (six-month reporting lag), equity market cap
- Frequency: monthly
- Notes: Demeaned within five DTS quintiles. Combined with the other defensive measures at equal-risk weights; missing measures scored zero.

**Defensive: gross profitability** (defensive / quality). Gross profits over assets (Novy-Marx, 2013). High profitability is the safe (long) side; direction implied by the paper's safety argument.
- Inputs: Compustat gross profit and total assets
- Frequency: monthly
- Notes: Demeaned within five DTS quintiles. Reporting lag for this measure is not stated separately (the six-month lag is stated for leverage).

**Defensive: low duration** (defensive / low risk). Effective (option-adjusted) duration from BAML. Low duration is the long side.
- Inputs: Effective duration (BAML)
- Frequency: monthly
- Notes: Excluded from DTS demeaning because that would mechanically pair high carry with low duration.

**Momentum: credit** (momentum). Most recent six-month cumulative bond excess return over duration-matched Treasuries. High past return is the long side.
- Inputs: Monthly bond excess returns (BAML)
- Frequency: monthly
- Notes: No skip month stated. Demeaned within DTS quintiles. Combined with equity momentum at equal-risk weights.

**Momentum: equity** (momentum). Most recent six-month cumulative return of the issuer's equity. High past return is the long side.
- Inputs: Issuer stock returns (requires equity link)
- Frequency: monthly
- Notes: No skip month stated. Demeaned within DTS quintiles. Momentum alpha is stronger in small, low-coverage, low-institutional-ownership bonds.

**Value: structural** (value). Residual from a monthly cross-sectional regression of log OAS on log default probability from a structural model. High residual (spread wide versus default risk) is the long side.
- Inputs: OAS; default probability (text: Bharath and Shumway 2008; Table A.1: Shumway 2001)
- Frequency: monthly
- Notes: Needs listed equity. Demeaned within DTS quintiles. Combined with empirical value at equal-risk weights.

**Value: empirical** (value). Residual from a monthly cross-sectional regression of log OAS on log duration, rating and 12-month bond excess-return volatility. High residual is the long side.
- Inputs: OAS, duration, S&P rating (1-10 code), trailing 12-month excess-return volatility
- Frequency: monthly
- Notes: Covers issuers without listed equity. The source does not say whether rating and volatility enter in logs. Value is the strongest single theme (Sharpe 1.75 for Q5-Q1).

**Combined style score (COMBO)** (multi-factor composite). Equal-weighted average of four single-theme portfolios. Each has weights linear in cross-sectional ranks, scaled by 5% over its 24-month realised volatility.
- Inputs: The four theme scores above; 24-month realised volatility of each theme portfolio
- Frequency: monthly
- Notes: Q5-Q1 Sharpe 2.19. Alpha 123 bp/month (t = 9.6) after market and equity factors. Used as the objective score in the long-only optimiser.

## Key Findings

1. In the joint Fama-MacBeth regression, value and momentum dominate. Value has a coefficient of 0.30 (t = 10.7) and momentum 0.22 (t = 7.1). Carry is 0.14 (t = 2.3), and defensive falls to 0.03 (t = 0.9). Alone, defensive is 0.15 (t = 5.0) and carry 0.00. The average cross-sectional R-squared is 15%, against 7.6% for 15 equity characteristics in Lewellen (2015).
2. Value-weighted Q5-Q1 portfolios earn annualised Sharpe ratios of 1.75 for value, 1.11 for defensive, 0.85 for momentum and 0.35 for carry. The equal-risk combination reaches 2.19. Returns rise roughly monotonically from Q1 to Q5 for every theme.
3. Carry correlates negatively with the other three themes even after DTS demeaning (-0.18 with defensive, -0.30 with momentum). Carry correlates 0.80 with the credit market factor. The other themes have correlations below 0.30 with market premia, often negative.
4. After controlling for credit, equity and Treasury premia and for SMB, HML, UMD and QMJ, the combined constant-volatility portfolio keeps an alpha of 123 bp a month (t = 9.6, information ratio 2.25). Carry's alpha disappears (0.05%, t = 0.7) because it loads 0.58 on CREDIT. Defensive, momentum and value keep significant alphas. Credit value loads negatively on SMB and QMJ and only mildly on HML.
5. The constrained long-only portfolio earns 5.72% gross and 5.26% net excess return a year, a net Sharpe ratio of 1.03. The benchmark earns 3.84% net with a Sharpe ratio of 0.69. The beta-adjusted active return is 2.20% net, with a 2.56% tracking error and an information ratio of 0.86.
6. The authors warn that long-short Sharpe ratios overstate bond economics. The combined dollar-neutral bond portfolio has 2.5% annual volatility, while HML has 11.6%. With similar dollar costs and turnover, bond costs per unit of risk are more than four times those of equities.
7. Macro exposures point to hedging, not risk. The combined portfolio loads -0.68 (t = -4.2) on industrial production growth and 1.12 (t = 2.9) on CPI changes, so it does well when growth falls and inflation rises. Only carry has risk-consistent signs, significant only for VIX. Value loads -0.18 (t = 2.2 in the text) on broker-dealer leverage shocks, but the combined loading is insignificant.
8. Momentum pays more where mispricing is likely. Its monthly long-short return is 0.40% among low-coverage issuers versus 0.16% among high-coverage ones. The high-minus-low gap is significant across coverage, institutional ownership and issue size terciles. Carry, defensive and value show mixed, mostly insignificant patterns. Extreme quintiles do not show the expected limits to arbitrage. The short sides are larger, better covered and cheaper to borrow.
9. Analyst sales revisions support a mispricing story for momentum. Over 12 months, long-quintile issuers get sales revisions 5.7% higher than short-quintile issuers (t = 7.28). Defensive shows 1.2% (t = 1.86). Carry goes the wrong way significantly (t = 6.17). A Merton-model translation maps the 5.7% to about 112 bp of bond return, about a third of the 290 bp momentum premium.

## Limitations

- The sample is short, about 18 years (January 1997 to April 2015), and the authors caveat time-series tests on that basis.
- The volatility scalar for 1997-1998 uses its January 1999 value, a disclosed look-ahead in the constant-volatility series.
- Only about 48% of bonds link to Compustat, so leverage, profitability, equity momentum and structural value miss many issuers. Missing measures are scored zero.
- OAS is an imperfect carry measure on sloped credit curves, and no curve-adjusted carry is tested.
- The long-only objective function is an omitted image in the converted text. Transaction costs come from a rating-maturity table, not from trade-level data.
- One bond per issuer removes liquidity and issue-size effects by design, so results may not carry over to the full bond universe.
- The structural default-probability source is cited inconsistently: Bharath and Shumway (2008) in the text, Shumway (2001) in Table A.1.

## Questions Raised

- How much of the value premium survives once value is built on a curve-adjusted spread rather than OAS?
- Does the DTS-quintile demeaning step change the ranking of themes when applied to carry and duration as well?
- Is momentum alpha concentrated in high yield, given that it is stronger in small, thinly covered bonds?
- How sensitive is the long-only information ratio to realistic trade-level costs from TRACE instead of a rating-maturity table?
- Does the defensive theme add anything once value and momentum are in the model, given its insignificant joint coefficient?

## Relevance to Bond Signals

The paper gives a full recipe for four credit style signals and their combination, built from BAML fields plus Compustat and equity returns. Its DTS-quintile demeaning is a direct, reusable neutralisation step for any bond characteristic correlated with spread. Value (spread residual on default-risk anchors) and momentum (six-month bond and equity returns) are the strongest standalone inputs. Carry adds little alpha after the credit factor, and defensive is largely spanned by value and momentum. The long-only constraint set (0.25% active weight, 50 bp OAS band, 0.5-year duration band, 10% turnover) offers a test harness for net-of-cost signal evaluation.

## Concepts

- [[concepts/style-premia|Style Premia (Value, Momentum, Carry, Defensive)]]
- [[concepts/factor-investing|Factor Investing in Corporate Bonds]]
- [[concepts/factor-signals-in-credit|Factor Signals in Credit]]
- [[concepts/corporate-bonds|Corporate Bonds]]
- [[concepts/low-risk-anomaly|Low-Risk Anomaly]]
- [[concepts/bond-momentum|Bond Momentum]]
- [[concepts/equity-momentum-in-credit|Equity Momentum in Credit]]
- [[concepts/cross-sectional-momentum|Cross-Sectional Momentum]]
- [[concepts/value-premium|Value Premium]]
- [[concepts/credit-relative-value|Credit Relative Value]]
- [[concepts/duration-times-spread|Duration Times Spread (DTS)]]
- [[concepts/credit-risk-premium|Credit Risk Premium]]
- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/distance-to-default|Distance to Default]]
- [[concepts/volatility-targeting|Volatility Targeting]]
- [[concepts/limits-to-arbitrage|Limits to Arbitrage]]
- [[concepts/risk-vs-mispricing|Risk-vs-Mispricing Debate]]
- [[concepts/fama-french-factors|Fama-French Factors]]
- [[concepts/leverage-ratios|Leverage Ratios]]
- [[concepts/constrained-optimization|Constrained Optimization in Economics]]
- [[concepts/option-adjusted-spread|Option-Adjusted Spread (OAS)]]
- [[concepts/fama-macbeth-regression|Fama-MacBeth Regression]]
- [[concepts/gross-profitability|Gross Profitability]]

## Entities

- [[entities/ronen-israel|Ronen Israel]]
- [[entities/diogo-palhares|Diogo Palhares]]
- [[entities/scott-richardson|Scott Richardson]]
- [[entities/aqr-capital-management|AQR Capital Management]]
- [[entities/london-business-school|London Business School]]

## Related Sources

- [[sources/houweling-2017-factor-investing|Factor Investing in the Corporate Bond Market]]
- [[sources/jostova-2013-momentum|Momentum in Corporate Bond Returns]]
- [[sources/bendor-2021-systematic-investing-in-credit|Systematic Investing in Credit]]
- [[sources/bharath-2008-forecasting-default-merton-distance-to-default|Forecasting Default with the Merton Distance to Default Model]]
- [[sources/haesen-2017-momentum-spillover|Momentum Spillover from Stocks to Corporate Bonds]]
- [[sources/dickerson-2026-corporate-bond-factor-replication-crisis|The Corporate Bond Factor Replication Crisis]]
<!-- AUTHORED REGION END -->