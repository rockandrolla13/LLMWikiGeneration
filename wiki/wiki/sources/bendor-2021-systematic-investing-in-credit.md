---
authors:
- Arik Ben Dor
- Albert Desclée
- Lev Dynkin
- Jay Hyman
- Simon Polbennikov
content_hash: sha256:f2aa370784fe87276494b5ef6b30e2d5db994d5c36fbbba5f2b3acd4b14ef375
created: '2026-10-22T15:27:29Z'
edition: 1st
is_early_release: false
isbn: 9781119751281 (hardback); 9781119751304 (PDF)
mind_map_priority: high
page_count_estimate: 744
page_id: sources/bendor-2021-systematic-investing-in-credit
page_type: source
publisher: John Wiley & Sons
related:
- concepts/merton-model
- concepts/variance-risk-premium
- concepts/volatility-risk-premia
- concepts/short-volatility-strategies
- concepts/credit-risk-premium
- concepts/credit-hedge-ratios-equity-options
- concepts/capital-structure-arbitrage
- concepts/bond-market-segmentation
- concepts/information-ratio
- concepts/structural-models
- concepts/low-risk-anomaly
- concepts/cds-bond-basis
- concepts/bond-liquidity
- concepts/liquidity-risk
- concepts/mean-reversion
- concepts/bond-index-inclusion-criteria
- concepts/index-reconstitution
- concepts/event-risk
- concepts/fallen-angel
- concepts/liquidity-scoring-mechanism
- concepts/credit-default-swaps
- concepts/factor-signals-in-credit
- concepts/systematic-credit-relative-value
- concepts/credit-relative-value
- concepts/duration-times-spread
- concepts/corporate-bond-liquidity-premium
- concepts/bid-ask-spread
- concepts/credit-spread-changes
- concepts/new-issue-concession
- concepts/default-rates
- concepts/speculative-grade-default-rate
- concepts/credit-spread-curve
- concepts/credit-spread-forecasting
- concepts/rating-based-stop-loss
- concepts/survival-probability
- concepts/hazard-rate-curve
- concepts/z-spread
- concepts/empirical-duration
- concepts/carry-rolldown
- concepts/value-premium
- concepts/leverage-ratios
- concepts/factor-investing
- concepts/fama-french-factors
- concepts/excess-spread-to-peers
- concepts/turnover-buffer
- concepts/spread-per-turn-of-leverage
- concepts/risk-vs-mispricing
- concepts/cross-sectional-momentum
- concepts/residual-momentum
- concepts/spillover-effect
- concepts/alpha-correlation-turnover
- concepts/equity-momentum-in-credit
- concepts/factor-timing
- concepts/cross-asset-rotation
- concepts/illiquidity-premium
- concepts/autocorrelation-time-series
- concepts/risk-premia
- concepts/issuer-size-premium
- concepts/liquidity-cost-score
- concepts/quantamental-investing
- concepts/post-earnings-announcement-drift
- concepts/equity-short-interest
- sources/bendor-2007-dts
- sources/haesen-2017-momentum-spillover
- sources/houweling-2017-factor-investing
- sources/jostova-2013-momentum
- sources/dickerson-2024-bond-pitfalls
- entities/arik-ben-dor
- entities/albert-desclee
- entities/lev-dynkin
- entities/jay-hyman
- entities/simon-polbennikov
revision_id: 1
schema_version: 2
source_hash: sha256:3da27977b1a55ad23821c375533cf247df4c4c48f5b837e031bbc7993871f59d
source_path: markdown_output/bendor-2021-systematic-investing-in-credit.md
source_type: book
sources: []
tags:
- corporate-bonds
- credit-factors
- systematic-credit
- fallen-angels
- equity-momentum
- relative-value
- index-inefficiencies
- dts
title: Systematic Investing in Credit
updated: '2026-10-22T15:27:29Z'
updated_by: op_955147eb8c65
uuid: c6fc5fe5-87f5-598f-8c87-c0b73e24a5c1
year: 2021
---

<!-- AUTHORED REGION START -->
# Systematic Investing in Credit

**Authors:** [[entities/arik-ben-dor|Arik Ben Dor]], [[entities/albert-desclee|Albert Desclée]], [[entities/lev-dynkin|Lev Dynkin]], [[entities/jay-hyman|Jay Hyman]], [[entities/simon-polbennikov|Simon Polbennikov]]

**Year:** 2021

**Publisher:** John Wiley & Sons

**ISBN:** 9781119751281 (hardback); 9781119751304 (PDF)

**Converted text:** `markdown_output/bendor-2021-systematic-investing-in-credit.md` (pdftotext; see the note in its first line).

## Summary

This book collects the research of a team of five quantitative credit researchers on how to invest in corporate bonds systematically. Each chapter is a self-contained empirical study. Each asks a practical question, builds a signal or portfolio rule from bond, equity or fundamental data, and tests it on long histories of US investment-grade and high-yield bonds, with some chapters covering euro and sterling markets.

The book has three main threads. The first is that credit is a distinct asset class: a mix of Treasuries and equities does not reproduce corporate bond returns. The second is that index rules create predictable, exploitable price pressure, as with fallen angels, new-issue concessions, the timing of index inclusion, and forced selling after downgrades. The third is that a small set of factors (value, equity momentum, and equity-based signals such as earnings surprises and short interest) predicts bond returns, provided the test matches risk carefully on spread, DTS and sector.

Throughout, the authors measure risk with duration times spread (DTS), match long and short portfolios on systematic exposures before claiming alpha, and account for transaction costs with bond-level liquidity estimates. The later chapters show how to combine signals at the bond level, control turnover with entry and exit thresholds, and feed quantitative scores to fundamental analysts.

## Key Contributions

- Shows that credit cannot be replaced by a combination of Treasuries and equities; the residual return is tied to volatility premia and the low-risk effect.
- Documents index-driven inefficiencies: fallen-angel price pressure and reversal, new-issue concessions, the value of delaying index inclusion, and the cost of rating-based stop-loss rules.
- Defines two value signals: excess spread to peers (ESP, relative value) and spread per unit of debt-to-earnings (SPiDER, long-horizon value).
- Shows that issuer equity momentum, post-earnings-announcement drift and equity short interest predict corporate bond returns.
- Finds a negative risk-matched issuer size premium in credit, except in crises.
- Gives a portfolio-construction method for combining signals at the bond level, with DTS matching and turnover buffers, plus the OneScore quant-plus-fundamental composite.

## How the Book Is Organised

- **Part One: Investing in Credit vs. a Combination of Treasuries and Equities** — chapters 1. Whether credit is a separate asset class.
- **Part Two: Capitalizing on Index Inefficiencies** — chapters 2–9. Fallen angels, issuance, index inclusion delay, new-issue concessions, try-and-hold mandates and stop-loss rules.
- **Part Three: Performance Implications of Portfolio Characteristics** — chapters 10–12. Coupon, maturity and ESG effects.
- **Part Four: Factor Investing in Credit** — chapters 13–19. Value, equity momentum, sector timing, issuer size, and combining factors.
- **Part Five: Using Equity-Related Data, Dynamics, and Instruments** — chapters 20–21. Earnings-announcement drift and equity short interest as bond signals.

## Chapter Guide

### Chapter 1. Can a Combination of Treasuries and Equities Replace Credit in a Portfolio?

**Question.** Can a mix of Treasuries and equities replace a credit allocation? If corporate bonds earn more than a risk-matched equity-Treasury mix, what explains the gap?

**Data.** Part 1 (asset allocation): S&P 500 total return, Bloomberg Barclays Treasury index, and the market-value-weighted combination of the Bloomberg Barclays US IG Corporate and HY indices, monthly, January 1993 to December 2019. Part 2 (issuer level): all issuers in the Bloomberg Barclays US Corporate and High Yield indices, January 1990 to December 2019, linked to Compustat equity with the Ben Dor and Xu (2015) bond-to-equity mapping. Filters drop bonds priced below $40, companies whose equity is an ADR, OTC or non-US listing, and stocks priced below $1 at the start of the month. IG and HY are analysed separately. A European sample serves as an out-of-sample test. Factor data: Fama-French five factors, momentum, BAB, and option-based VRP proxies built from SPX and 10y Treasury futures options.

**Method.** Two parts. (1) Reallocation control. Each month, regress trailing 36m credit-index returns on S&P 500 and Treasury-index returns. The coefficients become next month's weights in a replication portfolio, with any remainder in 3m T-bills. Adding x% of this replication portfolio to an E/T benchmark measures the reallocation effect. The gap between benchmark + x% credit and benchmark + x% replication measures the credit-specific effect. (2) Issuer-level replication, which also removes the mismatch effect (different issuers and sector weights in bond and equity indices). Step 1: each month, build a bond portfolio and an equity portfolio with identical issuers and identical issuer weights. Four weighting schemes are used: EW, Bond-VW, Equity-VW and Total-VW. Step 2: estimate each portfolio's betas to the S&P 500 and to the 10y on-the-run Treasury with monthly OLS on trailing 36m data, using exponential-decay weights. Solve two equations for two unknowns, the equity-portfolio weight $w_E$ and the 10y Treasury weight $w_T$: $w_E\,\beta^{E}_{SPX} = \beta^{B}_{SPX}$ and $w_E\,\beta^{E}_{UST} + w_T = \beta^{B}_{UST}$ (the 10y OTR has beta 1 to the rate factor and 0 to the S&P 500). The leftover weight goes to 3m T-bills. The test asset is the monthly bond-minus-replication return. Robustness checks use two other matching rules. One scales the equity portfolio to the bond portfolio's trailing 36m volatility. The other uses Merton (1974) analytical equity hedge ratios plus the ratio of issuer analytical duration to 10y OTR duration. Attribution regresses bond-over-replication returns on S&P 500 and Treasury excess returns, then adds FF5 + momentum, an equity VRP proxy, bond VRP proxies and BAB. The equity VRP proxy is a short 1m ATM SPX straddle held to expiry and delta-hedged daily with SPX futures. The bond VRP proxies are short 1m ATM puts and calls on 10y Treasury futures, held separately and delta-hedged daily. (The two matching equations are written from the prose description. The book's own equation is in a note not checked here.)

**Findings.**

- Adding credit raised the Sharpe ratio of every E/T benchmark tested, even after removing the reallocation effect. For a 60/40 equities/Treasuries portfolio over 1993-2019, the Sharpe ratio rose from 0.71 to 0.86. On average, the 36m-regression replication of the credit index held 16% equities, 81% Treasuries and 3% T-bills.
- With matched issuers, weights and risk, corporate bonds beat the equity-Treasury replication by more than 1.5%/yr in IG and about 3%/yr in HY. Information ratios ranged from 0.47 to 0.84 across the weighting schemes. Bond and replication returns correlated around 0.80 in IG and 0.70 in HY. In Europe the information ratios were about 0.4 for IG and 0.67 for HY.
- The IG replication held on average 9% equities and 60% Treasuries. The HY replication held 19% equities and 18% Treasuries. IG bond portfolios had significant Treasury betas in 97% of calibration windows, against 40% for HY.
- The result held under the other matching rules. Volatility matching in HY gave information ratios of 0.39 to 0.59. Merton hedge ratios gave 0.41 in IG and 0.37 in HY with EW. Volatility matching fits IG poorly because it ignores IG's Treasury exposure.
- The baseline alpha was 1.806%/yr in IG and 3.495%/yr in HY, both significant. The equity VRP factor cut it by 47bp in IG and 75bp in HY. Bond VRP puts cut it by a further 55bp in IG (OCR shows 'SSbp') and 85bp in HY. Bond VRP calls were not significant. BAB cut it by a further 32bp in IG and 45bp in HY. The final alphas of 80bp in IG and 211bp in HY were not significant. So the gap is mostly short-volatility premia (equity VRP and the short rate puts embedded in callable bonds) plus a low-risk anomaly that runs across the capital structure.
- Replicating the bond indices' volatility exposure with options is not practical at scale. With 5% of daily option volume, one day covers only 0.48% of index market value through SPX options. Covering it fully through Treasury options would take 5,273 trading days (21 years).

**Use for bond signals.** The bond-minus-replication return is a clean credit-specific excess return. It is a good dependent variable or risk-adjustment benchmark for testing bond alphas, because it strips out equity and rate beta. Corporate-bond portfolios carry implicit short equity-vol, short rate-put and low-beta (BAB) exposures. Check whether a new credit signal is simply loading on these exposures. The authors also suggest predicting which issuers' bonds beat their own risk-matched stock as a future capital-structure signal.

Concepts: [[concepts/merton-model|Merton Structural Model]] · [[concepts/variance-risk-premium|Variance Risk Premium]] · [[concepts/volatility-risk-premia|Volatility Risk Premia (VIRP)]] · [[concepts/short-volatility-strategies|Short Volatility Strategies]] · [[concepts/credit-risk-premium|Credit Risk Premium]] · [[concepts/credit-hedge-ratios-equity-options|Credit Hedge Ratios with Equity Options]] · [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]] · [[concepts/bond-market-segmentation|Bond Market Segmentation]] · [[concepts/information-ratio|Information Ratio]] · [[concepts/structural-models|Structural Models]] · [[concepts/low-risk-anomaly|Low-Risk Anomaly]]

### Chapter 2. Fallen Angels: Characteristics, Performance, and Implications for Investors

**Question.** Do bonds downgraded from IG to HY suffer temporary price pressure from forced selling, and not just from news? Can a rule-based portfolio exploit the reversal that follows?

**Data.** All bonds in the Bloomberg Barclays US Corporate Index with a rating event between January 1990 and December 2009. That gives 761 issuers and 2,251 bonds: 1,485 downgraded to HY and 766 upgraded to IG, which serve as a control group. Each bond is tracked monthly from 12 months before to 24 months after the event. Defaulted bonds exit at the month-end after default. Peer groups: 27 buckets by industry (financials, industrials, utilities) x rating (A and above, Baa, Ba, B, Caa and below) x maturity (up to or over 10y). They are populated monthly from Corporate or HY index bonds without a rating event in the prior 24 months, and a peer group needs at least 20 bonds. TRACE volumes and LCS (liquidity cost score) are from 2007 onward. The Markit cash-CDS basis is from 2004 onward. The portfolio backtest runs from January 1991 to June 2010.

**Method.** Event study: issuer-level monthly returns relative to peers, value- and equal-weighted, by quarter relative to the event month. For flow statistics, a bond's peer group is reset monthly. For spread and cost measures, the peer group is fixed at the post-event bucket. Cross-sectional sort: issuers are ranked on average relative return over a 4-month formation period (event month to end of month 3) into 20 buckets, then followed over three 6-month periods. Regressions: relative returns in the underperformance period are regressed on information proxies, the change in cash-CDS basis, and the product of the change in relative LCS and relative turnover. Predictive regression: average relative return over the next 12 months is regressed on the basis level and on (relative LCS x turnover) at the end of month 3. The cash-CDS basis is issuer Libor-OAS minus a mix of 5y and 10y CDS with RPV01 equal to the issuer's spread duration. Portfolios start fully in cash in January 1991 and rebalance monthly, with no leverage. They hold only the largest bond per issuer, with a 10% maximum position. Held bonds are equal-weighted and uninvested cash earns 1m Libor. 'Buy All': buy every fallen angel at the end of its event month and hold for 24 months. 'Three-Month Reversal': buy at the end of month 3 if relative spread is at least 40bp; sell when relative spread turns negative or after 24 months. 'Flexible Reversal': buy in months 1-6 if relative spread is above 40bp and tighter than last month and the price is above $40. Every portfolio sells on default, call or maturity. A rough net return is monthly return minus $\tfrac{1}{2}\,\mathrm{LCS}\times\mathrm{Turnover}$.

**Findings.**

- Value-weighted fallen-angel issuers lagged peers by a cumulative 15.09% over the three quarters before the downgrade plus the downgrade month. They then beat peers by 6.63% by month 24, with about two-thirds of the gain in quarters 4-5. The upgraded control group showed no reversal. Its pre-event gain was only about a third as large (5.66% vs. -15.09%).
- The evidence points to forced selling, not overreaction. The effect was larger for big issuers: cumulative value-weighted underperformance was 9.67% against 2.82% equal-weighted. Baa3-to-Ba1 one-notch downgrades behaved like the full sample. For 46.1% of issuers, the minimum relative return fell in the event month or the next three months, which makes month 3 the natural buy point.
- The bottom 5% of performers over the 4-month formation period beat peers by 5.75%, 1.04% and 0.86% in the next three 6-month periods. The reversal is strongest just after the selling ends.
- Price-pressure proxies explain the cross-section. Turnover rose from 5.1% to just over 18% in the downgrade month while LCS spiked. The cash-CDS basis widened to about 225bp (OCR '22Sbp') three months after the downgrade. A 1% widening of the basis meant 1.63% per month more underperformance (t-statistic of -5.80). Together with the LCS x turnover term (t-stat. -6.08), the basis explains 30% of the cross-section in the regression. The introduction says 'about 40%'. A wider basis at month 3 predicted about 15bp per month (OCR '1Sbp') of outperformance per 1% of basis over the next 12 months.
- Buy All beat peers by about 3.6% a year with an information ratio of 0.64. Three-Month Reversal raised the information ratio to 1.03 against broad peers and 0.93 against modified peers. Flexible Reversal did worse than Three-Month Reversal because waiting for each bond's inflection gave up some tightening. Holding periods were 21.7 months for Buy All and 9.7 and 9.8 months for the reversal portfolios. The headline is that fallen-angel portfolios beat peers by about 8.5% per year.
- Returns depend on supply. In the second half of the sample, Three-Month Reversal's average monthly relative return was three times higher (1.19% vs. 0.40%) and its information ratio rose from 0.8 to 1.25. After an estimated LCS cost, the net relative return was 72.7bp/month and the total return about 12.39% a year, with an annualized information ratio of 0.94.

**Use for bond signals.** Use event time since an IG-to-HY downgrade as a conditioning variable. Avoid or underweight fallen angels in months 0-3, and buy from about month 3 when the spread to rating/industry/maturity peers is at least 40bp. Exit when the relative spread reaches zero or at 24 months. Three price-pressure measures add cross-sectional ranking power within fallen angels: the change in the cash-CDS basis, the basis level at month 3, and the product of relative LCS and relative turnover.

Concepts: [[concepts/bond-market-segmentation|Bond Market Segmentation]] · [[concepts/cds-bond-basis|CDS-Bond Basis]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[concepts/liquidity-risk|Liquidity Risk]] · [[concepts/mean-reversion|Mean Reversion]] · [[concepts/information-ratio|Information Ratio]] · [[concepts/bond-index-inclusion-criteria|Bond Index Inclusion Criteria]] · [[concepts/index-reconstitution|Index Reconstitution]] · [[concepts/event-risk|Event Risk]] · [[concepts/fallen-angel|Fallen Angel]]

### Chapter 3. Fallen Angels: Capacity, Transaction Costs, and the Bond-CDS Basis

**Question.** Is the fallen-angel reversal stable over time, present in Europe, and specific to fallen angels? Does it survive capacity limits and trading costs? Can a bond-CDS basis trade capture it without outright credit risk?

**Data.** US fallen-angel sample from Chapter 2, extended to December 2011 for the capacity and cost tests. European fallen angels downgraded 2000-2011. LCS (Konstantinovsky, Ng and Phelps 2016) is available from 2007. The basis study uses 101 matched bond-CDS pairs for issuers downgraded 2004-2010 with actively traded CDS. Issuers downgraded because of an M&A event are excluded. CDS data come from Markit, with Barclays trader quotes as backup. Spreads are capped at the 95th percentile (20%). The Bloomberg Barclays HY Index default history covers 22 years from 1990.

**Method.** (a) Stability check: 1y and 2y post-downgrade relative returns over four sub-periods. (b) Europe: the Chapter 2 event study is repeated and split into 'High Supply' years, where fallen angels exceed 30% of the HY market (2002, 2005, 2009), and low-supply years. (c) A 'Mean Reversion' control applies the Three-Month Reversal rules to non-fallen-angel HY bonds: buy if relative spread is at least 40bp, and sell if it turns negative or after 21 months. (d) Capacity: issuer weight is $w_i=\min\left(\tfrac{1}{N},\,10\%,\,\tfrac{\text{Cap}\times MV_i}{\text{Port.size}}\right)$ with Cap = 5% of issuer market value and portfolio size from $125mn to $2bn. The formula is reconstructed from a garbled PDF equation and its worked example. (e) Costs: each purchase is marked at the ask using its LCS. (f) Basis trade: go long a market-value-weighted bundle of the issuer's unsecured bonds and buy protection on 5y CDS for 24 months. The market-adjusted basis is $(\text{5y CDS} - \text{MV-weighted OAS of issuer bonds}) - (\text{OTR 5y CDX.NA.HY} - \text{HY Index OAS})$. Four variants are tested. 'Buy All' enters at the end of the downgrade month. 'Sell Tight' exits when the market-adjusted basis reaches 0. 'Sell Tight-Buy Wide' enters only if the market-adjusted basis is at least 120bp negative. 'Sell Tight-Buy Wide in Month 3' adds entry 3 months after the downgrade. A 5% stop-loss variant is also tested.

**Findings.**

- The reversal was stable over time: fallen angels beat peers by about 5.5 to 9.5% over two years in every sub-period. In Europe, issuers lost 18.54% before the downgrade and then gained 6.93%, close to the 6.63% in the US. In high-supply years the drop was deeper (22.61% vs. -14.44%) and the recovery larger (10.24% vs. 2.48%).
- The effect is specific to fallen angels and is not general HY mean reversion. The EW Mean Reversion portfolio's Sharpe ratio (0.72) barely beat the HY Index (0.66). With matching cash, Three-Month Reversal beat it in both halves of the sample (0.92% vs. 0.44% and 1.86% vs. 1.11% per month). Fallen-angel equities showed no matching reversal.
- Fallen angels defaulted less often than other HY issuers: 15% against 24% by issuer count, and 12% against 16% by amount outstanding.
- Capacity is adequate. From $125mn to $2bn, Three-Month Reversal's monthly return fell by 74bp and its Sharpe ratio fell to 0.95 (from 1.14), still above the HY Index at 0.65. Buy All's return fell only about 27bp. Trading costs cut returns by 59bp/month for Three-Month Reversal and 37bp/month for Buy All. Net Sharpe ratios were around 0.65 against 0.43 for the HY Index.
- Basis trades across 101 pairs: Buy All had a Sharpe ratio of 1.05 but a net Sharpe ratio of only 0.26, with 85% of pairs positive. Sell Tight earned 0.8% vs. 0.5% a month with a net Sharpe ratio of 0.97. Sell Tight-Buy Wide (33 issuers) earned 1.8% a month with a Sharpe ratio of 2.38 and a net Sharpe ratio of 1.3. The month-3 variant had the best Sharpe ratio (3.30) and a net Sharpe ratio of 1.74. With a 5% stop-loss, Buy All's net Sharpe ratio fell from 0.26 to 0.05. The wide-basis variants held up at 1.23 and 1.53.

**Use for bond signals.** The fallen-angel reversal is a distinct bond-level signal. It is not HY short-term reversal and does not appear in equities. It scales to about $2bn and survives LCS costs. The market-adjusted cash-CDS basis at downgrade (entry threshold at least 120bp negative, exit at 0) works as a credit-hedged version of the signal and as a filter for which fallen angels to trade.

Concepts: [[concepts/cds-bond-basis|CDS-Bond Basis]] · [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[concepts/liquidity-scoring-mechanism|Liquidity Scoring Mechanism]] · [[concepts/mean-reversion|Mean Reversion]] · [[concepts/bond-market-segmentation|Bond Market Segmentation]] · [[concepts/credit-default-swaps|Credit Default Swaps]] · [[concepts/information-ratio|Information Ratio]]

### Chapter 4. Introducing the Fallen Angel Reversal Scorecard

**Question.** Can a monthly bond-level score that tracks each fallen angel's stage in its reversal cycle rank fallen angels better than the fixed Three-Month Reversal rule or relative OAS alone?

**Data.** Fallen angels with a positive spread relative to peers right after the downgrade. Each bond is tracked while its relative spread stays positive and within 24 months of the downgrade. Peers are index bonds with the same rating and level-3 industry, market-value-weighted. Turnover comes from TRACE (2007 onward). Stage statistics use spread data from 1991 to 2019. Live FAR scores start June 2010, and the test period runs July 2010 to December 2019 with sub-periods 2010-2014 and 2015-2019. The benchmark is the Bloomberg Barclays US High Yield Index.

**Method.** Step I, stage. The real-time indicator Pre-Reversal$_t=1$ if relative OAS in month $t$ is the highest since the downgrade month. Ex post, the inflection month is the month of peak relative OAS within the 24 months. Among Pre-Reversal=1 months, inflection probability depends on the monthly change in relative turnover. Relative turnover is bond turnover (monthly volume / amount outstanding) over the value-weighted peer turnover. The change is split at a 5% cut-off, and $P_{\text{infl}}$ is the empirical share of inflection months in each group over a trailing 5-year window. Step II, sensitivity. The baseline is $\text{Rel.OAS/m}=\dfrac{\text{Rel.OAS}_t}{24-\text{months since downgrade}+1}$. Regress next month's change in relative OAS on Rel.OAS/m interacted with three state dummies (tightening = Pre-Reversal 0; inflection; non-inflection widening), on a trailing 5-year window. Step III, score. If Pre-Reversal=0: $\text{raw}=-\beta_{\text{tight}}\,\text{Rel.OAS/m}$. If Pre-Reversal=1: $\text{raw}=-[P_{\text{infl}}\,\beta_{\text{infl}}+(1-P_{\text{infl}})\,\beta_{\text{wide}}]\,\text{Rel.OAS/m}$. The FAR score is the monthly cross-sectional percentile rank, from 0 to 100. Tests: (1) monthly top-half minus bottom-half sort, equal-weighted with a 10% cap and the excess in 1m Libor if fewer than 10 bonds, with returns measured relative to peers. It is compared with sorts on relative OAS and on Rel.OAS/m. (2) FA-tilted HY portfolio: per issuer, take the bond with the highest FAR score. The top issuer gets a 3% overweight and the others get 3% x FAR/max FAR. The rest goes to the HY Index. Controls are a peer-tilted portfolio and an FA-EW-tilted portfolio with the same total overweight.

**Findings.**

- The reversal cycle has three stages. The month after the inflection point has the largest median tightening (122bp), about seven times a typical tightening month (17bp). After an ordinary widening month, spreads widen a further 13bp. When Pre-Reversal = 0, the month really is in the tightening stage 70% of the time.
- A rise in relative turnover flags the inflection point. Among Pre-Reversal=1 months, the inflection probability was 32% when the turnover change was at least 5%, against 24% when it was smaller. Across all fallen angels the figures were 12% and 5%.
- Full-sample sensitivities to Rel.OAS/m were -0.82 in tightening months, -4.26 in inflection months and +1.86 in non-inflection widening months. The adjusted R-squared was 23.42%.
- Top-minus-bottom sorts from July 2010 to December 2019 earned 3.88% per year (IR 0.40) on relative OAS and 4.69% per year (IR 0.51) on Rel.OAS/m. FAR scores did best at 5.67% per year (IR 0.65). FAR's maximum drawdown was -9.42% against -26.12% and -23.90% for the other two sorts. Even the bottom FAR half beat peers.
- The FA-tilted HY portfolio overweighted fallen angels by 23% on average. It beat the HY Index by 1.07% per year (2010-2014) and 5.32% per year (2015-2019), with IRs of 1.31 and 0.98. The peer-tilted control did about as well as the index. FAR weighting beat equal-weighting all fallen angels with IRs of 0.67 and 0.94.

**Use for bond signals.** FAR is a ready-made bond-level alpha template. Divide the peer-relative spread by the months left in the event window. Condition on a real-time stage flag (is the spread at its running maximum?) and a flow flag (change in relative turnover of at least 5%). Use stage-specific betas fitted on a rolling 5-year window, then rank cross-sectionally each month. The same design (spread / time-to-normalisation x regime-dependent sensitivity) could carry over to other forced-flow events such as index exits.

Concepts: [[concepts/mean-reversion|Mean Reversion]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[concepts/information-ratio|Information Ratio]] · [[concepts/factor-signals-in-credit|Factor Signals in Credit]] · [[concepts/systematic-credit-relative-value|Systematic Credit Relative Value]] · [[concepts/credit-relative-value|Credit Relative Value]] · [[concepts/bond-index-inclusion-criteria|Bond Index Inclusion Criteria]] · [[concepts/fallen-angel|Fallen Angel]]

### Chapter 5. Issuance Dynamics and Performance of Corporate Bonds

**Question.** Does heavy debt issuance predict weak subsequent corporate bond returns at the market, sector and issuer level? If so, how much does it cost a market-weighted index, and which alternative weightings avoid the cost?

**Data.** USD corporate bonds from investment grade to high yield. The authors combine the Bloomberg Barclays US Corporate, US 144A and US High Yield indices into a composite US Corporate All Ratings index, split into eight custom sectors. Sample runs August 1994 to July 2014, with monthly observations. The issuer-level tests keep only issuers mapped to Compustat GVKEYs, about 80% of index bonds. Barclays Liquidity Cost Scores (LCS) are used from 2007.

**Method.** Macro and sector level: the issuance rate is six-month net issuance divided by the amount outstanding at the end of the period. Net issuance = new gross issuance - redemptions - maturing bonds. Monthly rolling observations are sorted into issuance-rate quartiles. The test compares the next six months' excess return over duration-matched Treasuries for Q1 (low issuance) against Q4 (high issuance). A size test sorts issuers into quartiles of index debt outstanding and correlates issuance rate with the next six months' excess return within each quartile. Index drag: build a benchmark with constant sector weights equal to each sector's time-average weight. The drag from moving sector weights is then the market-weighted excess return minus the constant-weight excess return. Each sector's contribution is $\overline{w_s r_s} - \bar w_s \bar r_s$, the time-average of weight times return minus the product of the averages. Issuer level: the issuance rate is 12-month net index issuance divided by end-of-period index debt. An issuer is 'aggressive' if its rate exceeds the index's rate, else 'moderate'. The two groups form market-weighted portfolios. An alternative split uses Compustat data: the 12-month net increase in liabilities divided by end-of-period total assets, compared with the index average. A spread-risk control runs a monthly cross-sectional regression of issuer excess return on DTS, interacted with aggressive/moderate and sector dummies. The authors drop the top and bottom 1% of returns: $\text{ExcRet}_i = \beta_{g,s}\,\text{DTS}_i\,\mathbb{1}\{\text{issuance}=g\}\,\mathbb{1}\{\text{sector}=s\} + \varepsilon_i$. Alternative indices: (a) equal sector weights, or equal notional per sector. (b) A 'contrarian' issuer weighting that starts at market weights and is adjusted monthly. The new weight is $w_{t+1} = w_t\,(1+g_{\text{index}})/(1+g_{\text{issuer}})$, where $g$ is the debt growth rate. Monthly changes are capped at +/-10% of the issuer's weight, and new issuers enter at full market weight.

**Findings.**

- Dynamic sector weights cost the market-weighted US Corporate All Ratings index 14bp a year versus constant time-average weights (Feb 1994 to Jul 2014). The drag rose from 10bp a year before the financial crisis to 23bp a year during and after it. It was persistent, with an information ratio of -0.60.
- The negative link between issuance and later returns is driven by large borrowers. The issuance-return correlation reaches almost -25% in the top size quartile, which holds 80% of index market value. By sector it is -49% for banks and brokerage, where 93% of the sector is in the top size quartile. It is only -7.6% for basic goods.
- Moderate issuers earned almost double the excess return of aggressive issuers, with similar volatility. The gap held in all three broad sectors and in every rating bucket except Baa. It was strongest in Ba-B, where the moderate-minus-aggressive information ratio was 0.69. Fallen angels cannot fully explain the gap, because they mostly move from Baa to Ba-B.
- Controlling for spread exposure via DTS, moderate issuers still beat aggressive ones by 0.38bp/month (industrials) and 0.42bp/month (utilities) per unit of DTS. That is about 3.8 and 4.2bp/month at a portfolio DTS of 10. The financials result is weak.
- Equal-sector and equal-notional indices beat the market-weighted index by 1.4 to 1.5bp/month, about 17bp/year, with information ratios close to 0.4. The equal-sector index gained 3.5% cumulatively over January 1994 to July 2014, mostly in crises and recoveries. The contrarian issuer index almost doubled the average excess return and information ratio. However, it had systematically higher LCS, meaning lower liquidity, especially in 2008.

**Use for bond signals.** Issuer net-issuance rate relative to the index is a ready-made negative signal: underweight issuers growing index debt (or balance-sheet liabilities over assets) faster than the market over the past 12 months. Aggregate and sector issuance rates are slower timing signals for credit beta and sector tilts. The liabilities-over-assets version gave stronger results than the index-debt version.

Concepts: [[concepts/factor-signals-in-credit|Factor Signals in Credit]] · [[concepts/duration-times-spread|Duration Times Spread (DTS)]] · [[concepts/bond-index-inclusion-criteria|Bond Index Inclusion Criteria]] · [[concepts/systematic-credit-relative-value|Systematic Credit Relative Value]] · [[concepts/bond-liquidity|Bond Liquidity]]

### Chapter 6. The Value of Waiting to Buy: Inclusion-Delay Investment-Grade Corporate Indices

**Question.** Can a benchmark that waits X months before adding eligible new issues beat the standard IG Corporate index while keeping its credit beta? If it does, how much of the gain comes from avoiding new-issue liquidity premia ('seasoning') and how much from avoiding bonds that soon get downgraded or default?

**Data.** The Bloomberg Barclays USD IG Corporate and IG Long Corporate indices, at monthly frequency. The direct LCS-based analysis covers February 2007 to August 2016, with 7,431 new issues. The decomposition is extended back to January 1990 using average first-month bid-to-bid pricing impacts: +42.5bp for intermediate new issues and +79.3bp for long ones.

**Method.** An X-month inclusion-delay index adds a bond X months after it would have entered the IG Corporate Returns Universe, provided it is still index-eligible then. Delays tested: 0, 1, 3, 6, 12, 18 and 24 months. Pricing fix: the standard index prices a new issue offer-to-bid in its first month. Delay indices use bid-to-bid pricing throughout, so they are compared with a bid-adjusted IG index, the '0-month delay index'. The bid price is estimated from the offer price and LCS. With $\text{LCS}_0 = (OP_0 - BP_0)/BP_0$, we get $BP_0 = OP_0/(1+\text{LCS}_0)$. The adjusted first-month price return is approximately the reported return plus $BP_0\,\text{LCS}_0/(OP_0 + AI_0)$. Weighting: 'natural' weights come from the delay index's own holdings, with no rebalancing. 'Adjusted' weights are rescaled monthly to match the IG index's market-value weights in 12 sector x quality buckets: FIN/IND/UTL crossed with AAA/AA/A/BAA. Decomposition with adjusted weights uses a look-ahead 'Clean' 0-month index. It drops 'problem bonds', meaning bonds downgraded to HY or defaulting within 24 months of eligibility. Clean minus 0-month measures the value of avoiding problem bonds. 24-month delay minus Clean measures the value of seasoning. 0-month minus IG index measures the effect of the pricing convention. A 'Young & Clean' index, holding non-problem bonds under 24 months old, is a side construct.

**Findings.**

- The pricing convention matters. Over February 2007 to August 2016, new issues' average first-month excess return was about -11bp offer-to-bid but +42bp bid-to-bid. This lifts IG index returns by about 0.9bp/m, or 11bp a year. The lift is 1.4bp/m for the IG Long index.
- Short delays do not help. The 1-month delay index underperformed the 0-month index by 0.7bp/m in excess return, so new issues seem to get even richer in their first index month. From 12 months the delay indices outperform. The 24-month delay beat the 0-month index by 3.2bp/m, about 372bp cumulatively over 115 months. Its return correlation with the IG index was 1.00.
- Over 1990 to 2016, avoiding problem bonds was worth about 1.2bp/m, measured as Clean 0-month minus 0-month delay. Seasoning was worth -0.3bp/m: the Clean 0-month index beat the 24-month delay. The seasoning component flipped from -1.0bp/m before 2007 to +0.8bp/m after July 2009. The authors link the flip to a post-crisis liquidity premium in new issues.
- Cumulatively since 1990, the 24-month delay index beat the IG index by 716bp. Of this, 296bp came from the bid-versus-offer pricing convention, which is probably not harvestable. Another 432bp came from avoiding problem bonds, which rises in credit stress. Seasoning contributed -12bp.
- The Clean-minus-24-month excess return difference had a correlation of -0.53 with monthly changes in IG OAS. When spreads spike, recently issued non-problem bonds lag, which is why long samples are needed. Bond LCS rises with age (correlation 0.27), so replicating a long delay costs a little more. The authors judge this cost modest relative to the outperformance.

**Use for bond signals.** Bond age since index entry is a usable feature: a filter that excludes bonds under 12 to 24 months old acts as a crude screen against issuers who issue just before trouble. That ties to the Chapter 5 issuance signal. The seasoning (new-issue richness) effect changes sign across regimes, so do not treat it as a stable factor.

Concepts: [[concepts/bond-index-inclusion-criteria|Bond Index Inclusion Criteria]] · [[concepts/index-reconstitution|Index Reconstitution]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[concepts/corporate-bond-liquidity-premium|Corporate Bond Liquidity Premium]] · [[concepts/bid-ask-spread|Bid-Ask Spread]] · [[concepts/liquidity-scoring-mechanism|Liquidity Scoring Mechanism]]

### Chapter 7. Concessions in Corporate Bond Issuance: Magnitude, Determinants, and Post-Issuance Dynamics

**Question.** How large are new-issue concessions in US IG corporate bonds, and what supply and demand factors drive them? How quickly do they disappear after pricing, and how much alpha do they offer compared with standard active credit strategies?

**Data.** There are two datasets. (1) The Barclays US IG Syndicate desk dataset, January 2008 to February 2014: 1,218 bonds from 876 issuance events. Each record has a maturity-adjusted concession, defined as new-issue ask spread on the offer day minus the benchmark bond's prior-day bid spread. (2) A 'B/P' dataset from 2000: 3,334 bonds from 2,643 events. It pairs Bloomberg new-issue ask spreads with POINT bid spreads for a rules-based benchmark bond, and is not maturity-adjusted. Other inputs: Lipper IG fund flows, LCS, and Bloomberg Barclays Corporate Index spreads.

**Method.** Concession = new-issue spread minus the spread of a benchmark bond from the same issuer. In B/P, the benchmark bond has the same issuer, the same notch rating and callability, and the closest maturity. The bond-level OLS regression of concession on three groups of factors uses the syndicate data. Supply factors: log issue size, issue size as a percentage of issuer debt, trailing 12-month issuance, and a 'frequent issuer' dummy for 4 or more deals in 12 months. Market demand factors: Corporate Index spread level (uncertainty), its one-month change (sentiment), peer-issuer spread change, aggregate LCS, IG fund flows, and prior-month maturities and calls. Issue and issuer factors: use of proceeds, rating, industry, maturity, and the issuer spread lagged 15 business days to avoid endogeneity. Post-issuance dynamics: track the B/P concession over 20 trading days. Concession alpha: a hypothetical index-tracking portfolio swaps secondary bonds for new issues each month. The alpha of new issue $i$ is $\alpha_i = \text{Concession}_i \times \text{SpreadDur}_i \times MV_i / MV_{\text{index}}$, summed over issues, assuming pro-rata allocation.

**Findings.**

- Concessions are predictable. The factors explain over 60% of cross-issue variation. Issue size matters most among supply factors: coefficients are 5.21 (log size) and 3.19 (relative size), with t-statistics of 9.05 and 3.90. Doubling issuance from $1bn to $2bn for an issuer with $1bn of debt adds about 7bp. Frequent issuers pay about 2.4bp more.
- Market uncertainty (index spread level) and sentiment (its recent change) are the strongest demand factors, with t-statistics of 10.68 and 5.87. The median concession tracks index spreads with a correlation of 0.72. It was 5 to 10bp before 2008, rose above 20bp in the crisis, then fell. Fund inflows barely matter: a very large 10% inflow cuts the concession by only 0.6bp.
- Concessions vanish fast. In B/P bid-minus-bid terms, the median fell from 9bp at pricing to 3bp at the end of day one and 2bp after a week. Using Bloomberg ask spreads it fell to as low as 0.5bp after a week. The new issue's cheapness is almost gone on the first trading day.
- The issuer's existing bonds also move. Spreads mean-reverted after pricing only for the largest 10 issues (over $9bn). For all other issues, secondary spreads kept widening after pricing, which suggests the market underreacts before the deal. Verizon's $45bn deal in 2013 widened its bonds by about 80bp in eight days, and relative spreads then tightened by 40bp.
- For an index-tracking manager, concession capture was worth about 14bp a year on average since 2008, and over 20bp in 2008 and 2009. That is comparable to typical market-timing or sector-rotation alpha. The authors put it at about half the alpha a typical credit investor can hope to generate from active strategies. It needs primary-market access, not skill.

**Use for bond signals.** The regression gives an ex-ante concession estimate from observable deal and market features, such as relative and absolute size, frequent-issuer status, index spread and its one-month change. That estimate can rank deals for primary participation. The finding that secondary bonds keep widening after pricing for most deals suggests a short-horizon negative signal on an issuer's outstanding bonds around large new issues.

Concepts: [[concepts/bond-index-inclusion-criteria|Bond Index Inclusion Criteria]] · [[concepts/duration-times-spread|Duration Times Spread (DTS)]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[concepts/bid-ask-spread|Bid-Ask Spread]] · [[concepts/credit-spread-changes|Credit Spread Changes]] · [[concepts/new-issue-concession|New-Issue Concession]]

### Chapter 8. 'Try-and-Hold' Credit Investing

**Question.** How should long-horizon investors measure risk and expected return when they buy to hold but must sell bonds downgraded below a rating threshold? How should those estimates depend on the current spread environment?

**Data.** Moody's one-year letter-rating transition matrix for 1970-2012, adjusted for withdrawn ratings. Moody's cohort default rates for 1991-2012. Long-term average spreads by rating, from Bloomberg Barclays US Corporate and High Yield indices, extended back to 1970 and excluding September 2008 to April 2009. For the empirical studies, issuer-level annual cohorts from the Bloomberg Barclays Corporate and HY indices for 1991-2013 (2009 is excluded as an outlier in some tests).

**Method.** Single-bond model over a five-year horizon. Carry is the spread. The analysis steps year by year through repeated one-year transition matrices. When a bond is downgraded to or below the sell threshold, it is sold at a loss of $\Delta S \times \text{SpreadDur}$. Here $\Delta S$ is the gap between the average spread of the new rating and the book spread. A 78bp fallen-angel penalty is added when an IG bond is sold right after a downgrade to HY. Spread duration shrinks over time, and losses are capped at 60% (40% recovery). Proceeds are reinvested in a bond of the original rating with the same remaining maturity. The loss distribution comes from simulation, giving expected return, standard deviation, and 98% VaR/CVaR. Three sell disciplines are compared: hold-to-default, sell-at-B, and sell-at-Ba. Conditioning on spreads: in year 1, multiply downgrade probabilities by the ratio of current to long-term average spread for each rating, multiply upgrade probabilities by its reciprocal, and rescale the diagonal so rows sum to 100%. In later years, spreads and multipliers mean-revert exponentially in log spreads, with a one-year half-life. A term-structure variant uses rating spreads by maturity bucket.

**Findings.**

- In a naive buy-and-hold view, expected default losses use up a large part of lower-rated spreads. Ba's 309bp a year spread includes 122bp a year of expected default loss, leaving 187bp. Baa's 162bp a year carries 23bp a year of expected loss.
- Stricter sell rules cut default losses but add more forced-sale losses, so expected return falls. For Baa bonds, the five-year forced-sale probability is 23.7% under sell-at-Ba and 7.2% under sell-at-B. Moving from sell-at-Ba to sell-at-B cuts the expected forced-sale loss from 165bp to 72bp. For A bonds, expected five-year return is 509bp (hold), 505bp (sell-at-B) and 483bp (sell-at-Ba).
- Sell rules shrink the Baa-over-A advantage. The Baa spread is 47% above the A spread. Baa's expected-return advantage is 36% under hold-to-default, 31% under sell-at-B and just 18% under sell-at-Ba. Sell-at-B gives the best return per unit of risk for both ratings. With a sell-at-Ba rule, long-maturity Baa bonds should be avoided.
- Spreads predict credit events only about two years ahead. The correlation of start-of-year spreads with one-year defaults is 0.84 (HY) and 0.63 (IG), falling to 0.12 and 0.18 in year two. With one-year downgrade rates it is 56% for A and 36% for Baa issuers, excluding 2009. Downgrade and spread correlations fade by year three. In 'high' downgrade years, downgrades run at roughly double the long-term rate and spreads about double.
- Conditioned on a high-spread date (November 2011), sell-at-Ba makes Baa clearly worse than A in expected return. A-rated debt then offers about 1200bp of five-year expected return at risk of about 600 to 700bp. In the low-spread case (January 2007), Baa bonds have a similar risk level but only 300-400bp of expected return.

**Use for bond signals.** Rating proximity to a common sell threshold (Baa vs a Ba cut-off), times the current spread-to-long-run-spread ratio, is a measurable forced-selling risk score. It worsens with maturity. The spread-scaled transition matrix gives a simple conditional downgrade probability that can serve as a feature, with a horizon of no more than two years.

Concepts: [[concepts/default-rates|Default Rates]] · [[concepts/speculative-grade-default-rate|Speculative-Grade Default Rate]] · [[concepts/credit-risk-premium|Credit Risk Premium]] · [[concepts/mean-reversion|Mean Reversion]] · [[concepts/credit-spread-curve|Credit Spread Curve]] · [[concepts/credit-spread-forecasting|Credit Spread Forecasting]] · [[concepts/fallen-angel|Fallen Angel]]

### Chapter 9. Effect of Rating-Based Stop-Loss Rules on Performance

**Question.** How do rating-based liquidation (stop-loss) rules, which sell bonds downgraded to or below a threshold, change the return and risk of diversified corporate bond portfolios?

**Data.** Custom subindices built from the combined Bloomberg Barclays US Corporate and US High Yield universes, monthly, December 1992 inception, through January 2015 (some tables say 1993-2015). Subperiods are 1993-2004 and 2005-2015. There are also euro and sterling corporate indices from 1999. Moody's one-year transition probabilities are used for intuition.

**Method.** Market-cap-weighted portfolios are rebalanced each month-end. Each portfolio buys bonds in a given rating range, either a single rating or a cumulative range such as Aaa-Baa. It sells bonds downgraded to or below a sell rating (A, Baa, Ba, B, or Caa1 and below). The benchmark is the buy-and-hold (BH) portfolio with the same buy rule and no liquidation. Results are excess returns over duration-matched Treasuries, volatility and maximum drawdown, reported as increments over BH. Aaa-Baa selling at Ba matches the IG index. Splits are by financials vs non-financials and by subperiod. 'Quality-matched' peers replace downgraded bonds with rating subindices so the rating mix stays the same. 'DG' portfolios hold only downgraded bonds. Decomposition of the drag: $E[\text{Loss}] = E[\text{DGFreq}]\,E[\text{DGLoss}] + \text{Cov}(\text{DGFreq},\text{DGLoss})$, where DGLoss = spread gap x duration (5.5 years). Appendix model for one Aa bond with spread $S_{Aa}$ and duration $D$, A spread $S_A$, and downgrade probability $p$: $R_{BH}=S_{Aa}$ and $R_{SG}=S_{Aa}-pD(S_A-S_{Aa})$. So $(R_{SG}-R_{BH})/R_{BH} = -pD(S_A/S_{Aa}-1)$, which is proportional to duration. The DTS-based volatility ratio does not depend on $D$. Equation (2) is OCR-garbled in the source, so it is not reproduced here.

**Findings.**

- Stop-loss rules reduced returns at every threshold, and more so when the threshold is close to the buy rating. A-rated BH earned 66bp a year. Selling at Caa, B, Ba and Baa cost 4, 7, 13 and 22bp a year. The IG-index-like portfolio (Aaa-Baa selling at Ba) lagged its BH version by 20bp a year.
- Risk falls much less than return. Aaa-Aa selling at A lost 41bp a year of return. It cut the drawdown by only 126bp (from 1,825bp), and cut volatility by a similarly small share of the 366bp BH level. That is a 56% return cut against single-digit percentage risk cuts. The IG-like portfolio's volatility fell from 450 to 425bp a year, while its return fell 27%. The appendix explains why: the percentage return drop scales with duration, but the volatility drop does not.
- The Aaa-Aa sell-at-A drag decomposes into 26bp a year from average downgrade frequency times average loss, plus 13bp a year from their 66% correlation. That gives 39bp, close to the 41bp observed. In the crisis peak, the loss given downgrade reached about 12.5% (227bp x 5.5 years).
- Downgraded bonds outperform their new rating peers. Bonds downgraded from Aaa-Aa to A earned 103bp a year against 66bp for A-rated BH. Quality-matched peers that swap downgraded bonds for rating subindices lag, by 24bp a year for Aaa-Aa BH. The drag was much larger after 2005 for high grades: Aaa-Aa selling at A lost 82bp a year in 2005-2015. Financials were hit hardest, with Aaa-Aa selling at A costing 46bp against 16bp for non-financials.
- Euro and sterling markets show the same pattern. In euro, Baa selling at Ba lost 57bp a year (37%), and the IG-like portfolio lost 24bp. In sterling, where duration is longer (7.6 vs 6 years), A selling at Baa lost 91bp a year. Holding instead of selling fallen angels would lift the sterling IG-like portfolio by 70%, from 49 to 84bp a year.

**Use for bond signals.** Recently downgraded bonds, especially those that cross a common sell threshold, outperform their new rating peers. A 'recent downgrade into rating r' flag is therefore a positive relative-value feature against same-rating peers. Benchmark stop-loss rules embed a measurable drag that a buy-and-hold or wider-threshold portfolio can harvest, largest for long-duration portfolios.

Concepts: [[concepts/duration-times-spread|Duration Times Spread (DTS)]] · [[concepts/bond-index-inclusion-criteria|Bond Index Inclusion Criteria]] · [[concepts/index-reconstitution|Index Reconstitution]] · [[concepts/credit-risk-premium|Credit Risk Premium]] · [[concepts/factor-signals-in-credit|Factor Signals in Credit]] · [[concepts/rating-based-stop-loss|Rating-Based Stop-Loss]]

### Chapter 10. Coupon Effects in Corporate Bonds: Pricing, Empirical Duration, and Spread Convexity

**Question.** Does a bond's coupon (how far it trades above or below par) change its spread, its sensitivity to Treasury yields, and its long-run performance relative to other bonds of the same issuer?

**Data.** Bloomberg Barclays US Corporate / US IG Corporate Index, monthly, January 1992 to April 2014 (268 months). Spread-on-coupon tests use 'frequent issuers' with seven or more bonds outstanding (on average 11.7% of issuers but 40.5% of eligible bonds; about 105 issuers per month). Empirical-duration regression uses all noncallable index bonds (737,506 observations). Illustration uses four Verizon bonds on April 28, 2014 priced with the Pedersen (2006) bond-implied CDS (BCDS) model, 40% recovery.

**Method.** Motivation: in survival-based pricing, recovery is a fixed share of par, so a premium bond loses more value on default than a discount bond of the same issuer. Repricing four Verizon bonds at a common BCDS of 163bp gives ZV spreads that rise linearly with coupon.

(1) Spread vs coupon. Each month, a pooled cross-sectional regression over frequent issuers: $OAS_{i,j} - \overline{OAS}_j = \alpha_j (SprdDur_{i,j} - \overline{SprdDur}_j) + \beta (Coupon_{i,j} - \overline{Coupon}_j)$, where $\alpha_j$ is an issuer-specific spread-curve slope and $\beta$ is a market-wide coupon effect. Equivalent to measuring each bond's rich/cheap vs its own issuer curve and regressing that on coupon.

(2) Empirical duration. Pooled regression of carry-adjusted monthly return (total return minus one-twelfth of beginning yield) on $-D_i \Delta y$. Model 1: empirical hedge ratio $\beta_{treas} + \beta_{spread} S_i$. Model 2 adds $\gamma \cdot PriceDistPar_i$ (absolute distance of price from par), with four separate $\gamma$s for premiums (price >= 110) and discounts (price <= 90) in rising-yield and falling-yield months. Treasury yield change uses the fitted 5y, 10y or 30y yield by maturity bucket (<7y, 7-15y, >=15y).

(3) Discount-minus-premium portfolio (bottom-up, issuer-matched). Monthly, for each frequent issuer: split bonds into two equal halves by coupon minus yield (odd middle bond goes to premium). Split each half by duration and reweight long/short-duration cells so both halves hit a common target duration (issuer average where feasible). Drop the issuer if durations cannot be matched. Aggregate issuers by issuer market weight into a discount portfolio and a premium portfolio, matched by issuer, sector and quality in market value and spread-duration contribution. Active portfolio = discount minus premium. Results are then partitioned by quartiles of 10y Treasury yield change, deciles of market excess return, quartiles of a duration-matched Baa-Aaa yield spread, and quartiles of discount-portfolio average price.

**Findings.**

- Since 2008 the coupon coefficient has been about 0.1 and strongly significant: two otherwise identical bonds from one issuer with coupons 1% apart differ by about 10bp of spread, the higher coupon trading wider.
- Empirical duration falls as spread rises. For a 100bp bond, Model 1 gives a hedge ratio of 0.83 for both a 110-price premium and a 90-price discount. Model 2 shows discounts are more sensitive to falling yields and less to rising yields, which acts like positive convexity. Premiums behave the other way.
- The issuer-matched long-discount/short-premium portfolio earned 3.5bp/mo with an information ratio of 1.01 over 1992-2014, despite the premium portfolio's spread carry advantage. Active volatility was 12bp/month against about 150bp/month for each leg. Both legs had a duration of 5.25. About 33% of the 28,198 issuer/month observations were dropped because durations could not be matched.
- The strategy is not directional in rates: it is positive in all four yield-change quartiles and strongest when yields rally, with information ratios of 1.84 and 1.65 in quartiles 1 and 2. By market excess return it earns 6 to 10bp/month in the two top and two bottom deciles and near zero in the middle six.
- The effect is concentrated in high credit-risk regimes. By duration-matched Baa-Aaa spread quartile, active volatility is 3.2bp/month in Q1 and 6.1bp/month in Q2 with near-zero return. Discounts beat premiums by 12.2bp/month in Q4. The information ratio is 0.59 in Q3 and 2.28 in Q4.

**Use for bond signals.** Within-issuer price/coupon position is a usable cheapness and convexity feature. Premium bonds trade about 10bp wider per 1% of coupon, yet discounts outperform, mainly when Baa-Aaa spreads are wide. Price-from-par should also enter any empirical-duration or rate-hedge model. The authors doubt the effect pays as a standalone strategy after costs. They suggest it as a tie-breaker tilt toward low-coupon bonds.

Concepts: [[concepts/duration-times-spread|Duration Times Spread (DTS)]] · [[concepts/survival-probability|Survival Probability]] · [[concepts/hazard-rate-curve|Hazard Rate Curve]] · [[concepts/credit-default-swaps|Credit Default Swaps]] · [[concepts/z-spread|Z-Spread]] · [[concepts/credit-spread-curve|Credit Spread Curve]] · [[concepts/empirical-duration|Empirical Duration]]

### Chapter 11. Maturity Dependence of Corporate Bond Excess Returns

**Question.** Why have long-maturity IG corporate bonds delivered lower excess returns and lower information ratios than short-maturity bonds, even though spread curves slope upward?

**Data.** Bloomberg Barclays US IG Corporate Index, end of January 1994 to January 2019 (25 years), monthly index excess returns over duration-matched Treasuries. Bonds bucketed by average life into 1-3, 3-5, 5-7, 7-9, 9-11, 11-20 and 20-35 years. Bonds with significant optionality, average life below 1 or above 35, or extremely high OAS are excluded. Liquidity Cost Scores (LCS) are used from January 2007. Rating subsets are A and Baa.

**Method.** Compute average excess return and information ratio (mean over standard deviation of monthly excess returns) per maturity bucket, for the full period and five nonoverlapping five-year windows. Attribute each bucket's return to four parts. (a) Spread carry: beginning-of-month spread accretion. (b) Roll-down: price return from repricing at a one-month-shorter maturity on an unchanged issuer spread curve. Issuer curves are fitted monthly for issuers with bonds in at least three of seven buckets, and aggregated curves are used for other issuers. (c) Spread trend: the sample-specific cumulative spread change between start and end of the period. (d) Downgrade cost: the residual, interpreted as realized and unrealized rating-migration losses. LCS per unit of DTS is compared across 7-9, 9-11 and 11-20 year buckets. The monthly net change in average rating (fine notches) is tracked against index OAS.

**Findings.**

- Information ratios fall almost monotonically with maturity over 1994-2019, and even raw average excess returns are lower for long than short buckets. Longer maturity paid off in returns only during the post-2008 rally, and information ratios still declined with maturity then.
- The 3-5 year bucket earned 91bp/y of excess return while the 9-11 year bucket earned only 27bp/y, despite a higher average OAS. The 9-11 bucket is hurt by negative roll-down from a flat or inverted issuer curve near 10 years.
- The 10-year sector is the new-issue hub: 40% of index bonds at end-January 2019 were issued with a 9-11 year maturity. 86% of 9-11 year bonds were issued in the prior two years, versus 44% for 7-9 years and 35% for 3-5 years. These bonds have lower LCS per unit of DTS. Their liquidity-driven tight spreads normalize as they age, which flattens or inverts the curve just below 10 years.
- A sample-specific bear steepening hurt long bonds most. Without the spread trend the 20-35 year bucket would have earned 103bp/y, 60bp/y more than realized. The trend effect is only 3bp/y for 1-3 years. Even after adding the trend back, extending maturity beyond seven years earned no extra return.
- Downgrade cost rises with maturity and is smallest at the short end. It is on average twice as large in Baa as in A, because Baa-to-HY downgrades widen spreads much more. Ratings drift lower more when index OAS is high.

**Use for bond signals.** Maturity is a priced feature in the cross-section. Short and intermediate (up to about 7y) IG bonds have the best risk-adjusted excess returns, and the 9-11y new-issue sector is a persistent laggard on roll-down. Roll-down from fitted issuer curves and expected downgrade cost by maturity and rating are useful building blocks for an expected-excess-return signal. Control for maturity when testing other signals.

Concepts: [[concepts/carry-rolldown|Carry and Rolldown]] · [[concepts/credit-spread-curve|Credit Spread Curve]] · [[concepts/duration-times-spread|Duration Times Spread (DTS)]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[concepts/bond-index-inclusion-criteria|Bond Index Inclusion Criteria]] · [[concepts/credit-risk-premium|Credit Risk Premium]] · [[concepts/low-risk-anomaly|Low-Risk Anomaly]]

### Chapter 12. ESG Investing in Credit

**Question.** Does a best-in-class ESG tilt within sectors help or hurt corporate bond performance once other risk exposures are matched, and do high-ESG bonds trade at a spread premium?

**Data.** Bloomberg Barclays US IG, Euro IG and US HY corporate indices, mapped through equity identifiers to issuer ESG scores from MSCI ESG Research and Sustainalytics. Only bonds rated by both providers are used. IG runs August 2009 to April 2018, HY October 2012 to 2018, monthly. IG coverage always exceeded 80% of index market value and 63% of issuers. HY coverage at the end was just over a third of issuers and close to 60% of market value.

**Method.** Score properties: monthly rank correlations between providers; 12-month transition frequencies across ESG terciles; rank correlation with median index credit rating; averages by country of domicile.

Performance: each month-end, an optimizer builds two index-tracking portfolios from ESG-covered bonds, one maximizing and one minimizing weighted-average ESG score (or a single E, S or G pillar). Both must match the index's average spread, duration and DTS, the allocation across three rating buckets, and market weight, spread duration and DTS contribution in each cell of 8 sectors x 2 maturity buckets (US IG). Euro IG uses 5 sectors x 2 maturities plus issuer geography, benchmarked to the ESG-covered subset. Issue and issuer concentration limits apply, giving about 180 bonds per portfolio in US IG. High-minus-low return is the ESG effect, measured in excess of duration-matched Treasuries. The same is repeated within sectors and in US HY (about 160 bonds, matching duration, spread, rating and sector).

Valuation: monthly cross-sectional regression of bond OAS on industry, rating, OASD and normalized issuer ESG score (plus geography in Euro). The ESG coefficient is the spread premium in bp per one standard deviation of ESG. Pillars are tested singly and pooled over months.

Downgrades: split bonds at the median ESG or pillar score and compare annual downgrade notch rates.

Appendix: monthly cross-sectional regressions of bond excess returns on OAS, OASD, sector DTS and normalized ESG score.

**Findings.**

- A naive ESG tilt is a quality tilt. The top ESG tercile trades 15 to 36bp tighter than the bottom tercile, and the environmental score has the strongest link to rating and spread. ESG scores are stable: a top-tier issuer stays top tier after a year 79% (MSCI) or 88% (Sustainalytics) of the time.
- Risk-matched high-ESG portfolios beat low-ESG portfolios in US IG and Euro IG with both providers. In Euro IG, overall ESG gave over 3bp/month with an information ratio close to 1. Governance was the best single pillar in the US over the full period. Environment was best in Euro IG and in US IG over the last two years. Social mattered least.
- There is no evidence of a systematic richening of high-ESG bonds, so the outperformance is not a one-off repricing. US IG shows no significant ESG spread premium in most months (for example -0.6bp per standard deviation, t-stat -0.5, in a March 2018 regression with R-squared of 72%). Euro IG shows a stable premium of about -5bp per standard deviation in the later period. That is much smaller than the 42-51bp/yr outperformance and of opposite sign.
- Bonds with low governance scores had consistently higher subsequent downgrade rates than high-governance bonds, except in the final year. This points to the ESG return coming from fewer negative issuer events.
- In US HY, results are weaker. Coverage is thin, the spread premium is not significant, and long-short results are mostly positive. Only the MSCI governance tilt is statistically significant. The return regressions show high-ESG names beating low-ESG ones by about 0.5 to 1bp/month per standard deviation in IG. These coefficients correlate about 0.5 with the portfolio-simulation returns.

**Use for bond signals.** ESG, and especially governance, is a weak but persistent within-sector return signal. It only shows up after neutralizing the quality, spread and geography biases of the raw scores. Use the scores as a sector-neutral, rating-neutral tilt or as a downgrade-risk predictor, and expect provider disagreement. Rank correlations between providers are low, lowest for governance.

Concepts: [[concepts/factor-signals-in-credit|Factor Signals in Credit]] · [[concepts/duration-times-spread|Duration Times Spread (DTS)]]

### Chapter 13. Relative Value Investing in Credit Using Excess Spread to Peers

**Question.** Can a bond's spread in excess of rating-industry-duration peers, after adjusting for issuer leverage, identify undervalued bonds that outperform without the market directionality of simply buying high spread?

**Data.** Bloomberg Barclays US Corporate (IG) Index, January 1993 to January 2016, monthly. The universe keeps senior noncallable bonds mapped to Compustat and drops the top 0.5% of spreads. This gives more than 2000 bonds per month on average and over 4000 recently. Financial leverage comes from Compustat with a three-month lag. Trade Efficiency Scores (TES) and trading volumes are used from 2007. All returns are in excess of duration-matched Treasuries.

**Method.** Premise: on average the market is priced correctly, and the peer group stands in for the bond's fundamental 'theoretical' spread.

Peer group: bonds in the same credit rating x industry x duration (maturity) cell. The book's illustration uses consumer noncyclical, Baa-rated, 3-7 year bonds. The full set of rating, industry and maturity breakpoints used for the cells is not specified in the text.

ESP score: excess spread over the peer average, controlling for excess financial leverage over the peer average. Leverage = book debt / (market equity + book debt), lagged three months. Figure 13.3 plots excess spread against excess leverage within a cell, with a fitted line. Bonds above the line (high spread for their leverage) are high ESP, and bonds below it are low ESP. Read literally this is the residual of $s_i - \bar s_{peer}$ on $L_i - \bar L_{peer}$. The book calls the figure a crude illustration and gives no explicit formula, so the exact functional form is not stated. A no-leverage variant (pure excess spread to peers) is also reported.

Ranking and portfolios: ESP is recomputed monthly. (a) Decile portfolios of ESP, market-weighted. (b) Long-short: long above-median ESP, short below-median ESP, IG universe, rebalanced monthly. (c) Turnover buffer: enter the long leg when ESP is in the top 40% and exit only when it drops below the median. Mirror this for the short leg ('10% buffer'). The '15% buffer' holds longs until the bottom 45% and shorts until the top 45%. The ESP formula is unchanged. (d) Index-tracking portfolios that maximize average ESP while matching DTS, duration and market-value contributions in eight sectors and overall DTS and duration, with 4%, 2% or 1% issue caps and ticker caps at double that. These hold 34 to over 100 bonds.

Factor test: monthly Fama-MacBeth cross-sectional regressions of bond excess returns on percentile-rank loadings (scaled -1 to 1) for spread, duration and ESP, plus bond DTS times sector dummies. Example: a 60th-percentile ESP bond has an ESP loading of 0.2.

**Findings.**

- Returns and information ratios rise nearly monotonically across ESP deciles in both subperiods. Adding the leverage control moderately improves decile separation.
- Long above-median ESP outperformed short below-median ESP by 1.78% per year and beat the index by 1.18% per year, 1993-2016. Information ratios were above 1.2 in all periods with low correlation to the index. The high-ESP portfolio's spread was only 17bp above the index, so carry cannot explain the 118bp per year gain. Mean reversion in relative spreads drives it.
- In Fama-MacBeth regressions the ESP factor earns 15.2bp/month (about 1.8%/yr) with a t-stat of 8.6 alone and 8.0 alongside spread and duration. The spread factor (5.2bp per month, t-stat 2.7, alone) becomes insignificant once ESP is included. The ESP factor is weakly correlated with credit and Fama-French equity factors.
- ESP ranks are sticky at the extremes. More than 75% of top-decile bonds stay in the top two deciles after a year, and more than 65% of bottom-decile bonds stay in the bottom two. The plain median-split strategy turns over 11% a month. The 10% and 15% buffers cut turnover to 5.7% and 4.3% per month, with higher returns and slightly lower information ratios.
- Returns are higher when the ESP dispersion between high and low portfolios is wide. Returns were negative over 12 months in 2002 and 2015, during spread momentum episodes. Information ratios are highest in the least liquid TES buckets. ESP-tilted index trackers with 34 to 109 bonds beat the index by more than 1.2% per year with information ratios above 1. About 50 random positions are enough for a long-short overlay to reach an information ratio near one.

**Use for bond signals.** ESP is a ready-made cross-sectional value signal. Compute a residual spread within rating x industry x duration cells, adjust for excess leverage, rank monthly, and trade with a top-40%/median buffer. It is distinct from carry and DTS. Its main risks are spread momentum episodes and an illiquidity tilt in the top decile. It pairs naturally with equity momentum, which the book later combines in OneScore.

Concepts: [[concepts/systematic-credit-relative-value|Systematic Credit Relative Value]] · [[concepts/credit-relative-value|Credit Relative Value]] · [[concepts/value-premium|Value Premium]] · [[concepts/factor-signals-in-credit|Factor Signals in Credit]] · [[concepts/duration-times-spread|Duration Times Spread (DTS)]] · [[concepts/leverage-ratios|Leverage Ratios]] · [[concepts/mean-reversion|Mean Reversion]] · [[concepts/factor-investing|Factor Investing in Corporate Bonds]] · [[concepts/fama-french-factors|Fama-French Factors]] · [[concepts/excess-spread-to-peers|Excess Spread to Peers (ESP)]] · [[concepts/turnover-buffer|Turnover Buffer]]

### Chapter 14. Long-Horizon Value Investing in Credit Using Spread per Unit of Debt-to-Earnings Ratio

**Question.** Can a simple, model-free ratio of issuer spread to debt over long-run earnings (SPiDER) identify mispriced issuers whose bonds outperform over a one- to two-year horizon, net of risk, carry and costs?

**Data.** Bloomberg Barclays US Corporate and US High Yield index bonds, January 1993 to February 2020, matched to domestic Compustat statements. Exclusions: financials; HY bonds rated below B or priced below $50; issuers with less than six years of statements in the past 10 years; fiscal year or quarter not ending in October to December. Mapped market value rises from 85% to 98% in IG and from 68% to 83% in HY. Strategy returns run from March 1993 to February 2020 and are monthly excess returns over duration-matched Treasuries. Benchmarks are the IG and HY indices excluding financials, with HY also excluding bonds below B.

**Method.** Signal, computed annually at end-February for each issuer: $SPiDER_{i,t} = \dfrac{OAS_{i,t}}{Debt_{i,t} / \text{Sustainable EBITDA}_{i,t}}$. $OAS$ is the market-value-weighted OAS of the issuer's bonds at end-February. $Debt$ is long-term plus short-term debt. Sustainable EBITDA is the average of the last 10 annual EBITDAs, with at least six. Fundamentals come from the fiscal year or quarter ending October to December of year t-1, giving at least a two-month lag. The annual statement is used if available, otherwise the sum of the last four quarters with debt from the latest quarter.

Validation: within rating buckets, D/E quintiles predict downgrades over 1-3 years. A yearly regression $OAS_{i,t} = \sum_j a_{j,t} I(industry=j) + b_t (D/E)_{i,t} + \epsilon$ (industry = level-3 sectors) gives positive slopes.

Ranking: issuers are sorted into SPiDER quintiles within industry each February. Issuers are equal-weighted and held 12 months regardless of rating changes. The strategy is long Q5 (high SPiDER, cheap) and short Q1. A long-only Q5 portfolio is also tested.

Risk and carry checks: DTS-implied volatility $\sigma_{Q_i} = \sigma_{Q1} \cdot DTS_{Q_i}/DTS_{Q1}$ is compared with realized volatility. DTS-matched returns use $R^{adj}_{Q_i,t} = (DTS_{Q1,t}/DTS_{Q_i,t}) R_{Q_i,t}$. A pure OAS-quintile carry strategy is the comparison. An OAS-neutral version sorts into four OAS buckets within industry, then splits each bucket into top and bottom SPiDER halves. Rating x industry half-splits and per-industry Q5-Q1 are also tested.

Alternatives: different earnings windows, trend-extrapolated EBITDA, I/B/E/S forward EBITDA (from 2003), inverse interest coverage, and debt-to-cash.

Implementation: sell on index exit; value weights or value weights capped at 4%; quarterly rebalancing (new OAS only, or new OAS and new statements); 24-month overlapping Jegadeesh-Titman holding (two equal annual sub-portfolios, half renewed each February); net-of-cost returns using annual turnover times average Q5 LCS. Index trackers are built annually from a liquid universe (maturity over 3y, notional above the 25th percentile, one bond per issuer preferring bonds under 2 years old and duration nearest the industry average). They maximize weighted SPiDER subject to a 1% (or 2%) bond cap and matching sector weights and index DTS, with optional OAS matching, giving about 100 bonds.

**Findings.**

- D/E is a valid fundamental risk anchor. A one-standard-deviation rise in D/E adds 10.7bp of OAS in IG and 28.3bp in HY. With industry dummies, D/E explains over 85% of the cross-sectional spread variation. Changes in aggregate OAS and D/E correlate 0.30 in IG and 0.39 in HY. High-D/E issuers are downgraded more within each rating bucket.
- The Q5-minus-Q1 SPiDER strategy had an information ratio of 1.17 in IG and 0.73 in HY over March 1993 to February 2020. Equity value factors had 0.32 to 0.60 over a similar period. Long-only Q5 earned 1.83% a year (information ratio 0.47) in IG versus 0.63% (0.16) for the benchmark, and 3.64% versus 2.21% in HY. Returns and information ratios rise monotonically from Q1 to Q5, while volatility is flat across quintiles.
- Risk and carry do not explain the result. The pure OAS-quintile carry strategy has about three times SPiDER's carry (1.53% IG, 4.52% HY) but an information ratio three to four times lower. The OAS-neutral SPiDER has near-zero carry and still outperforms. After DTS-matching, Q5 still beats Q1 by a wide margin. Per industry, Q5-Q1 earns at least 128 bps/yr in IG and 134 bps/yr in HY.
- The signal lives about two years. Quarterly long-short returns stay positive and fade to near zero by quarter eight, with a bump in quarter five when the next annual report usually confirms the position. More than half of Q1 and Q5 issuers keep their quintile a year later. Annual turnover is about 43% in IG with 12-month rebalancing and 28% with 24-month rebalancing. In HY the figures are 55% and 35%.
- After costs, IG long-only Q5 still beats the benchmark with an information ratio of 0.33 (12-month rebalancing) and 0.37 (24-month). In HY only the 24-month version survives costs. Value-weighting cuts long-short information ratios to 0.58 in IG and 0.57 in HY. Debt-to-cash is the least correlated alternative definition (rank correlation 0.44 in IG and 0.30 in HY), so it is a candidate for combination. SPiDER-tilted trackers of about 100 bonds beat both benchmarks.

**Use for bond signals.** SPiDER is an issuer-level absolute value signal: OAS divided by debt over 10-year average EBITDA, ranked within industry each February with a two-month accounting lag. It is model-free and comparable across sectors and over time, so it can be aggregated for sector timing. Its slow decay suits low-turnover 12- to 24-month holding, and it complements the faster cross-sectional ESP signal.

Concepts: [[concepts/spread-per-turn-of-leverage|Spread Per Turn of Leverage]] · [[concepts/value-premium|Value Premium]] · [[concepts/systematic-credit-relative-value|Systematic Credit Relative Value]] · [[concepts/duration-times-spread|Duration Times Spread (DTS)]] · [[concepts/leverage-ratios|Leverage Ratios]] · [[concepts/risk-vs-mispricing|Risk-vs-Mispricing Debate]] · [[concepts/carry-rolldown|Carry and Rolldown]] · [[concepts/factor-signals-in-credit|Factor Signals in Credit]] · [[concepts/factor-investing|Factor Investing in Corporate Bonds]]

### Chapter 15. Equity Momentum in Credit

**Question.** Do an issuer's recent stock returns predict the next-month excess returns of its corporate bonds? If so, is the effect robust across quality, liquidity and market regimes, and does it survive turnover and transaction costs?

**Data.** All bonds in the Bloomberg Barclays US Corporate IG and US HY indices, December 1992 to May 2017, monthly. Bond returns are excess returns over duration-matched Treasuries, plus OAS and duration analytics. Bonds are mapped to issuer stocks with a historical bond-equity mapping (Ben Dor and Xu 2015). Issuers without equity data, such as private companies, are dropped. Trade Efficiency Scores (TES) are available from January 2007, so the liquidity tests and the cost study cover February 2007 to May 2017.

**Method.** Signal. Equity momentum is the issuer's stock price return over a formation window ending at month-end. The base illustration uses a 3-month window. The main signal combines 1-, 3- and 6-month price returns with equal weights, after each return is divided by the square root of its window length so that windows are on an equal footing: $EMC_i = \tfrac{1}{3}\left(\frac{R_{i,1m}}{\sqrt{1}} + \frac{R_{i,3m}}{\sqrt{3}} + \frac{R_{i,6m}}{\sqrt{6}}\right)$ (this formula is my rendering of the note's words; the book gives no equation). There is no skip month; the book contrasts this with the equity MOM factor, which uses 12-month returns excluding the last month. Month-end stock prices are used, and a robustness test lags them by 1, 2 or 3 business days. The signal is not normalised within sectors (Chapter 16 says so explicitly).

Issuer-to-bond mapping. Every bond of an issuer gets the issuer's equity signal. The signal is therefore an issuer-level sort applied to all of that issuer's bonds.

Portfolios. At the start of each month bonds are sorted on the signal into deciles or quintiles across the whole universe. IG and HY are sorted separately. The rating breakdown sorts within Aaa-A, Baa and HY buckets. The liquidity tests sort first into TES buckets (1-3, 4-7, 8-10) or into terciles of trailing 12-month return autocorrelation (bottom 30%, mid 40%, top 30%) and then into momentum quintiles within each bucket. The EMC strategy is long the top quintile (Q5) and short the bottom quintile (Q1). The text calls the quintiles 'diversified' but does not state the weighting scheme inside them. Holding period is one month with monthly rebalancing. Returns are before transaction costs. There is no DTS or duration scaling, so the long-short has time-varying net OAS and DTS.

Variants. (a) Residual momentum: stock price returns are regressed on S&P 500 returns over a 12-month rolling window, and residual returns over 1, 3 and 6 months are rescaled and equally weighted as above. (b) Combination with relative value: bonds are double-sorted into four buckets on ESP score (High 6-10, Low 1-5, from Chapter 13) and EMC (above or below the median), giving HH, HL, LH and LL. (c) Long-only with turnover control (Appendix 15.2): monthly rebalancing with a buy rule and a sell rule. EMC1 buys top-decile bonds and sells otherwise. EMC2 buys top-decile bonds and sells only when a bond falls to the bottom decile, leaving a wide hold buffer. EMC3 is EMC2 but buys only liquid bonds (TES 1-3). Transaction costs are estimated from Barclays Liquidity Cost Scores.

**Findings.**

- Bond excess returns rise almost monotonically across equity-momentum deciles. On the 3-month signal, the bottom decile earned about -4.7%/yr and the top decile +4.01%/yr, against 0.67%/yr for the IG index. The bottom decile is about twice as volatile as the others.
- The IG Q5-Q1 strategy on the combined 1/3/6-month signal earned 6.34%/yr with an information ratio of 1.56 over 1993-2017, before costs, and it worked in both subperiods. The effect is stronger in lower quality: 3.9%/yr (IR 0.83) for A3 and above, 8.8%/yr for Baa and 19.9%/yr for HY. The conclusion quotes 15.9%/yr for HY, so the two figures disagree.
- The signal decays fast but keeps paying for months. A top-decile issuer has only a 17% chance of staying top-decile after three months. A fixed high-vs-low cohort gained 35bp, 22bp and 19bp in months 1-3 and 95bp after six months. About 80% of that came in the first three months, so quarterly rebalancing is a fair trade-off.
- EMC is defensive. It is negatively correlated with IG excess returns and the equity market, positively correlated with QMJ, and only weakly linked to equity MOM. It earned 11.53%/yr in credit drawdowns and 4.30%/yr in recoveries, while the index earned -8.07%/yr and 4.12%/yr. Its net spread turns negative in equity and credit down-cycles.
- Illiquidity does not explain EMC. Within TES buckets, Q5-Q1 returns are similar across liquidity groups and the information ratio rises only from 1.48 to 1.99 as liquidity worsens. Results are also similar across return-autocorrelation buckets and with a 1-3 day price lag. Residual (market-beta-stripped) momentum did slightly worse than raw price momentum.
- Costs and combination decide practical value. A long-only top-decile portfolio turns over 73% a month and loses money after costs. With a buy-top-10% / sell-bottom-10% buffer, turnover falls to 8.9% a month and the portfolio beats the index by 0.78%/yr after costs (IR 0.59), or 0.91%/yr (IR 0.70) when buys are limited to liquid bonds. Combining with ESP relative value gives 2.49%/yr over the index (IR 2.14). That beats High ESP (0.85%/yr) and High EMC (1.43%/yr) added together.

**Use for bond signals.** Issuer equity momentum is a cheap, issuer-level bond signal that is strongest in Baa and HY and works in liquid bonds. Use a 1/3/6-month blend with square-root scaling and no skip month, and rebalance through a wide hold buffer or a turnover budget. It works best as one input next to a relative-value signal. Its net spread is countercyclical, so hedge or neutralise DTS if you want pure selection alpha.

Concepts: [[concepts/cross-sectional-momentum|Cross-Sectional Momentum]] · [[concepts/residual-momentum|Residual Momentum]] · [[concepts/spillover-effect|Momentum Spillover Effect]] · [[concepts/factor-signals-in-credit|Factor Signals in Credit]] · [[concepts/duration-times-spread|Duration Times Spread (DTS)]] · [[concepts/systematic-credit-relative-value|Systematic Credit Relative Value]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[concepts/alpha-correlation-turnover|Alpha Correlation and Turnover]] · [[concepts/equity-momentum-in-credit|Equity Momentum in Credit]] · [[concepts/turnover-buffer|Turnover Buffer]]

### Chapter 16. Corporate Sector Timing Using Equity Momentum

**Question.** How much of the EMC strategy's return comes from implicit sector bets rather than issuer selection? Can sector-level equity momentum time corporate bond sector allocation?

**Data.** Bloomberg Barclays US Corporate IG, Euro Corporate IG and US HY indices, November 2007 to October 2017, monthly. Returns are excess over duration-matched Treasuries. Issuers are ranked 1-10 by the EMC scorecard from Chapter 15. Sectors are eight custom groups built from index Level 3 classes (for attribution) and 15 Class 3 sectors (for timing).

**Method.** EMC scores. Issuers are scored 1 to 10 on the Chapter 15 equity momentum signal: issuer stock price returns over 1, 3 and 6 months, normalised for window length and averaged. Scores are not normalised within sectors.

Attribution (issuer selection vs sector rotation). A sector-neutral EMC sorts issuers on equity momentum within each of eight sectors. It goes long the top 20% (Q5) and short the bottom 20% (Q1) in each sector. The sector legs are aggregated with the benchmark index's sector weights, so long and short legs have identical sector weights. Their sector DTS contributions can still differ. Sector-rotation contribution = unconstrained EMC return minus sector-neutral EMC return. Volatility and information ratio are also computed on this difference.

Sector timing. Each month the 15 Class 3 sectors are ranked on sector equity momentum, defined as the average of issuer stock price returns over 1, 3 and 6 months normalised by window length. The book does not say how issuers are weighted inside a sector. The strategy holds a market-value-weighted portfolio of the top 5 sectors (and a bottom-5 portfolio for comparison), rebalanced monthly and held one month. It is measured against the index and against bottom-5. Returns are before transaction costs. A scatter of sector-month equity momentum against next-month sector excess return estimates the slope.

**Findings.**

- Across EMC scores, US IG excess returns are almost monotonic in 2007-2017. Score 1 earned -7.2%/yr and score 10 earned 8.10%/yr, against 1.43%/yr for the index.
- Sector-neutral EMC still works in every sector and universe, so issuer selection is the main driver. Returns are lower in less cyclical sectors such as consumer noncyclical and utilities.
- Sector rotation added 0.97%/yr (US IG), 0.70%/yr (Euro IG) and 3.38%/yr (US HY) to top-quintile EMC outperformance. That is 24 to 35% of the total, or about 30% in the conclusion.
- Each extra 1%/month of sector equity momentum adds about 5 to 8bp/month of next-month sector excess return. The link is strongest in US HY and weakest in Euro IG.
- Holding the top 5 of 15 sectors by equity momentum beat the index by 2.38%/yr (US IG), 1.77%/yr (Euro IG) and 4.04%/yr (US HY), with information ratios above 1 before costs. Much of the gain came in 2008-2009, 2011 and 2015-2016, when sector returns diverged.

**Use for bond signals.** Split equity momentum into a within-sector issuer score and a sector-level tilt, and treat them as two signals with separate risk budgets. The sector tilt pays mainly in turbulent markets and its costs are not tested. A sector-neutral version is cleaner if you want pure selection alpha.

Concepts: [[concepts/cross-sectional-momentum|Cross-Sectional Momentum]] · [[concepts/factor-timing|Factor Timing]] · [[concepts/cross-asset-rotation|Cross-Asset Rotation Strategy]] · [[concepts/factor-signals-in-credit|Factor Signals in Credit]] · [[concepts/duration-times-spread|Duration Times Spread (DTS)]]

### Chapter 17. Issuer Size Premium in Credit Markets

**Question.** Do bonds of small issuers earn a spread or return premium over those of large issuers once you control for rating, sector, duration, spread and liquidity? Could issuer size be a systematic credit factor?

**Data.** US-domiciled issuers in the Bloomberg Barclays US Corporate IG and US HY indices, with Yankees excluded. Returns cover January 1994 to May 2018, monthly, as excess returns over Treasuries. LCS liquidity data start in 2007, so the spread decomposition covers 2008-2018. A May 2018 snapshot has 629 IG and 784 HY issuers.

**Method.** Size measure. Issuer size is the issuer's amount of debt outstanding in the IG and HY indices. The chapter rejects equity market cap, because it mixes in valuation, and balance-sheet total debt, because it is quarterly with staggered reporting. Size is relative: each month issuers are ranked against peers, because average issuer size grew a lot over the sample.

Sorted portfolios. Each month issuers are split into small (bottom 30%), medium (middle 40%) and large (top 30%). Bond analytics and returns are aggregated to issuer level with market-value weights, excluding subordinated issues. Issuers are then market-value weighted in each portfolio, rebalanced monthly. Volatility is also measured per unit of beginning-of-month DTS, and over monthly, quarterly and semiannual horizons (overlapping, annualised by sqrt(12), sqrt(4), sqrt(2)) to expose stale pricing.

Spread premium. Each month a cross-sectional regression in the Fama-MacBeth style is run of issuer spread on small and large dummies plus controls. Model 1 adds duration and sector. Model 2 adds rating dummies. Model 3 adds LCS divided by duration. SML spread = coefficient on the small dummy minus coefficient on the large dummy. The total small-minus-large spread gap is decomposed into size, liquidity and rating parts.

Exposure-matched SML factor. Each month two portfolios are built by optimisation. One minimises issuer size and the other maximises it. Both must match the index's OAS, OAD and DTS. They must also match index weights and OAD and DTS contributions in 16 sector-maturity buckets, plus weights and duration contributions by rating bucket. Tight issuer concentration limits apply relative to index weight and DTS contribution. SML return = small minus large. A relaxed variant lets OAS and DTS deviate by up to 10% from the index so the small portfolio can collect spread.

**Findings.**

- Size is very persistent, so a size signal would have low turnover. An IG issuer in the smallest decile has a 72% chance of staying there after 12 months, and one in the largest decile has a 90% chance.
- Small-issuer portfolios show higher information ratios in simple sorts, but this comes from stale pricing. Their volatility per unit of DTS is about 30% lower in IG and 20% lower in HY. Their LCS is over 50% higher and their returns are strongly autocorrelated. Measured over quarterly or semiannual horizons, small IG portfolios become more volatile than large ones.
- The raw small-minus-large spread gap is mostly rating and liquidity. At May 2018, SML spread was 17.2bp (IG) and 69.1bp (HY) with sector and duration controls. It fell to 5.7bp and 6.9bp with ratings, and to 3.0bp and 5.3bp with liquidity. The pure size spread premium swung between -22bp and 24bp in IG.
- With exposures matched, small issuers underperform large ones by 67bp/yr in IG and 32bp/yr in HY over 1994-2018. The gap is worst in 2007-2018. SML is positive only in crises, for example +20.2% (IG) and +43.3% (HY) in communication and technology during 2001-2002.
- Even matched portfolios show lower volatility for small issuers: 3.37% vs 4.50%/yr in IG and 8.06% vs 10.27%/yr in HY. Letting spread and DTS deviate by 10% to collect carry still leaves SML at -16bp/yr in IG and about zero in HY.

**Use for bond signals.** Do not use issuer size (index debt outstanding) as a long-small alpha factor in credit, because it has a negative risk-matched premium. Use it as a control or a crisis-regime tilt instead. Check any signal that loads on small issuers for stale-pricing volatility bias, and measure risk on multi-month returns or in DTS-matched, exposure-matched portfolios.

Concepts: [[concepts/factor-signals-in-credit|Factor Signals in Credit]] · [[concepts/factor-investing|Factor Investing in Corporate Bonds]] · [[concepts/duration-times-spread|Duration Times Spread (DTS)]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[concepts/illiquidity-premium|Illiquidity Premium]] · [[concepts/corporate-bond-liquidity-premium|Corporate Bond Liquidity Premium]] · [[concepts/fama-french-factors|Fama-French Factors]] · [[concepts/autocorrelation-time-series|Autocorrelation in Time Series]] · [[concepts/risk-premia|Risk Premia (Expected Return Sources)]] · [[concepts/issuer-size-premium|Issuer Size Premium]]

### Chapter 18. Integrating Systematic Strategies into Credit Portfolio Construction

**Question.** Can the ESP relative value signal and the EMC equity momentum signal be combined and run as a real US IG corporate bond portfolio, after turnover limits, liquidity filters and transaction costs?

**Data.** Bloomberg Barclays US Corporate IG index constituents, March 2007 to July 2019, monthly. Signals are Barclays ESP (bond-level) and EMC (issuer-level) scores, each 1 to 10, produced at the start of each month. Transaction costs come from bond-level Barclays Liquidity Cost Scores (LCS, available for US IG and HY since January 2007). Liquidity filter uses Trade Efficiency Scores (TES, 1 to 10). Returns are excess returns over duration-matched Treasuries. Down-cycle table goes back to 1997.

**Method.** Signals. ESP: bonds are grouped into peer groups by rating, sector and maturity. Each bond's excess spread over its peer average is regressed on issuer fundamentals (debt/assets, net debt/EBITDA, EBIT/interest coverage; financials use only long-term debt / long-term assets). The unexplained residual spread is ranked across the index into a 1-10 score; high = cheap. EMC: issuer stock returns over 1, 3 and 6 months, each adjusted for horizon length, are equally weighted; the composite is ranked into a 1-10 issuer score; high = strong momentum. Both are refreshed monthly.

Tests of the signals. (a) Market-cap-weighted portfolios sorted on score pairs (1-2, 3-4, ..., 9-10), monthly 2007-2019. (b) 'Top' portfolios = score 9 or 10, which is the top 20% of bonds (ESP) or issuers (EMC). (c) Two combinations: 'Combined Portfolios 50/50' = equal-weight blend of top-ESP and top-EMC portfolios; 'Combined Signals 50/50' = per-bond score $S = 0.5\,\mathrm{ESP} + 0.5\,\mathrm{EMC}$, buy the top quintile of $S$. Signal overlap is measured by monthly Kendall tau rank correlation across constituents.

Implementation A, turnover buffer. Universe = index bonds with TES <= 3. Buy a bond when its combined ESP-EMC signal is in the top 20%. Hold it until the combined signal falls to or below the bottom 45%, then sell. Bonds in between are neither bought nor sold. Monthly rebalance; no explicit index-matching constraints. An alternative rule (not back-tested in the text) buys on high ESP unless EMC is very low, using EMC only as a value-trap screen.

Implementation B, turnover budget. Monthly linear optimisation: maximise portfolio average combined signal $0.5\,\mathrm{ESP}+0.5\,\mathrm{EMC}$ subject to: TES <= 3 to buy; no new purchases of bonds with under 3 years to maturity (existing ones may be kept); portfolio OAS, OAD and DTS broadly equal to the index; sector weights and sector OAD/DTS contributions near the index; issuer concentration limits; at most x% of market value traded per month. Budgets are swept; 11% per month is chosen (with hindsight) for the case study. Costs are charged at each bond's LCS (bid-offer times spread duration for spread-quoted bonds; (offer - bid)/bid for price-quoted bonds).

**Findings.**

- Both signals sort returns monotonically. ESP 1-2 bonds earned -0.74%/yr and ESP 9-10 bonds 3.39%/yr in excess return; EMC 1-2 earned -4.25%/yr and EMC 9-10 +4.55%/yr. The index earned 1.08%/yr.
- ESP and EMC rank correlations oscillate around zero. In credit down-cycles top-ESP portfolios underperformed the index (pro-cyclical, from higher DTS) while top-EMC portfolios outperformed (contra-cyclical), so they diversify each other.
- Before costs, top ESP and top EMC beat the index by 2.31%/yr and 3.48%/yr, with information ratios of 1.45 and 1.68. Blending the two portfolios cut tracking error to 1.51%/yr and lifted the IR to 1.92. Combining the signals per bond gave a similar IR of 2.06 but a much larger 6.00%/yr outperformance, at 2.91%/yr tracking error, because it holds about half as many bonds.
- The turnover-buffer portfolio (buy top 20%, sell at bottom 45%) averaged 10.4% monthly turnover and held bonds 14 months on average. It beat the index by 2.66%/yr before costs and 1.78%/yr after LCS costs, with tracking error 1.41%/yr. Cost drag was 1.15%/yr in 2007-2012 but only 0.64%/yr in 2013-2019.
- With an 11% monthly turnover budget and index-matched OAS, OAD, DTS and sectors, the portfolio returned 3.49%/yr versus 1.08%/yr for the index before costs, and 2.52%/yr after costs, with IR 1.05. Average holding time was 9.8 months. Net returns peak at moderate budgets: low budgets cannot implement the signal and high budgets lose more to costs.
- After costs, the budget portfolio beat the index by 1.45%/yr and the buffer portfolio by 1.78%/yr, both with IR above one. The budget portfolio lagged by 0.67%/yr in 2007-2012, which the authors link to fixed turnover in volatile markets and to sector constraints that block EMC's sector-timing value.

**Use for bond signals.** Combine value and momentum at the bond level (average the scores) rather than blending two portfolios: the IR is similar but the return per unit of turnover is higher. Use asymmetric entry/exit thresholds (enter top 20%, exit bottom 45%) and a liquidity pre-filter, and report results net of bond-level bid-offer costs; DTS-match to the index or the value leg carries hidden beta.

Concepts: [[concepts/systematic-credit-relative-value|Systematic Credit Relative Value]] · [[concepts/factor-signals-in-credit|Factor Signals in Credit]] · [[concepts/duration-times-spread|Duration Times Spread (DTS)]] · [[concepts/cross-sectional-momentum|Cross-Sectional Momentum]] · [[concepts/value-premium|Value Premium]] · [[concepts/factor-investing|Factor Investing in Corporate Bonds]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[concepts/information-ratio|Information Ratio]] · [[concepts/alpha-correlation-turnover|Alpha Correlation and Turnover]] · [[concepts/turnover-buffer|Turnover Buffer]] · [[concepts/liquidity-cost-score|Liquidity Cost Score (LCS)]]

### Chapter 19. OneScore: Combining Quantitative and Fundamental Views in Credit

**Question.** How should ESP value and EMC momentum be combined at the issuer level, within sectors, so the output can sit next to fundamental analysts' issuer recommendations, and does the composite work?

**Data.** Bloomberg Barclays US Corporate IG index issuers. Main back-test covers the five years to February 2020; drawdown and correlation tables run to March 2020 (start date unreadable in the scan) with monthly excess returns over duration-matched Treasuries. No turnover limits and no transaction costs. (PDF pages 635-640 are the Part 4 introduction, not this chapter.)

**Method.** OneScore construction: (1) For each issuer, average the bond-level ESP and EMC scores over its bonds with maturity above three years, using market-value weights. (2) Rank (normalise) the issuer-level ESP and EMC separately within each industry sector. (3) Average the two normalised ranks with equal weights. (4) Re-rank that average within the sector. (5) Map ranks to deciles 1-10. High OneScore = attractive versus sector peers.

Back-test: at each month start, pick up to 10 top and 10 bottom issuers per sector (fewer in concentrated sectors such as transportation), pool them across sectors into equally weighted top and bottom portfolios; bonds within an issuer are market-weighted; bonds of three years or less are excluded. ESP-only and EMC-only long-short strategies are built the same way from sector-normalised scores.

DTS neutralisation: each leg's monthly excess return is divided by its beginning-of-month DTS and multiplied by 12 (about the 1993-2020 time-average DTS of the index), so long and short legs both carry DTS 12: $r^{adj}_{leg} = r_{leg}\times 12/\mathrm{DTS}_{leg,t-1}$.

**Findings.**

- Top-OneScore IG issuers persistently outperformed bottom-OneScore issuers over the five years to February 2020, and sector-level top-minus-bottom portfolios had high risk-adjusted returns in all sectors, strongest in basic, cyclical and technology.
- Example of the quantamental use: Kinross Gold was a top OneScore pick on 28 February 2020 with sector-normalised ESP 8.1 and EMC 9.4, and analysts rated it Overweight.
- Without risk matching, ESP long-short returns are pro-cyclical and EMC returns contra-cyclical. DTS-matching the legs cuts ESP's correlation with index excess returns from 34% to -6% in drawdowns and from 44% to -22% in benign periods; EMC moves from -64% to -50% in crises.
- DTS-neutral OneScore becomes more defensive in drawdowns (index correlation from -37% to -48%) and less directional otherwise (from +35% to -28%), and both components added value in volatile and benign regimes after the adjustment.

**Use for bond signals.** Build composite credit signals at the issuer level and neutralise them within sectors, then risk-match the long and short legs on DTS before judging cyclicality. Much of the apparent pro-cyclicality of value and contra-cyclicality of momentum is a DTS bias, not alpha behaviour.

Concepts: [[concepts/systematic-credit-relative-value|Systematic Credit Relative Value]] · [[concepts/factor-signals-in-credit|Factor Signals in Credit]] · [[concepts/duration-times-spread|Duration Times Spread (DTS)]] · [[concepts/cross-sectional-momentum|Cross-Sectional Momentum]] · [[concepts/value-premium|Value Premium]] · [[concepts/factor-investing|Factor Investing in Corporate Bonds]] · [[concepts/quantamental-investing|Quantamental Investing]]

### Chapter 20. Does the Post-Earnings-Announcement-Drift Extend to Credit Markets?

**Question.** Do corporate bond prices underreact to earnings surprises as stocks do, and can credit investors profit from it after controlling for risk and liquidity?

**Data.** All bonds in the Bloomberg Barclays US Corporate and High Yield indices, January 2001 to December 2017 (tests start April 2001 because prior-quarter breakpoints are needed). Daily bond returns; bonds mapped to equity with a proprietary bond-to-equity map. Earnings dates and EPS from Compustat and I/B/E/S. Filters: drop ADR and OTC equities, drop announcements where Compustat and I/B/E/S dates differ by more than two calendar days, drop firms without I/B/E/S coverage or without full 3-day stock returns. Final sample: 1,929 firms, about 847 per quarter, about 30 announcements each; 84% of IG and 70% of HY index market value at the end. Excess returns for IG, total returns for HY.

**Method.** Surprise measures for issuer i, quarter q, announcement day $q_t$:
- SUE (described, not used): $SUE_{i,q}=\frac{EPS_{i,q}-E(EPS_{i,q})}{\sigma_{i,q}}$ with $E(EPS_{i,q})=EPS_{i,q-4}+\frac{\sum_{n=1}^{8}(EPS_{i,q-n}-EPS_{i,q-n-4})}{8}$, $\sigma$ = std of surprises over the last eight quarters.
- CFE: $CFE_{i,q}=\frac{EPS_{i,q}-\text{Consensus}_{i,q}}{p_{i,q}}$, consensus = mean of each active analyst's latest forecast before the announcement (excluding stopped coverage and non-majority accounting bases); $p$ = stock price at the prior month-end.
- EAR: $EAR_{i,q}=\prod_{j=q_t-1}^{q_t+1}(1+R_{i,j})-\prod_{j=q_t-1}^{q_t+1}(1+FF_j)$, where FF is the return of the stock's 5x5 size / book-to-market Fama-French portfolio. Window is days -1 to +1.
- BAR: $BAR_{i,q}=\sum_{j=q_t-1}^{q_t+1}\sum_{k}w^{MV}_{k,j-1}(R_{k,j}-R_{peers,j})$; peers = value-weighted return of the bond's rating x industry bucket (4 ratings: A+/A, Baa, Ba, B/B-; 8 industries).
DTS-adjusted abnormal return: $R^{DTS-adj.abn}_{k,t}=R_{k,t}-\frac{DTS_{k,t}}{DTS_{peers,t}}R_{peers,t}$, aggregated to issuer by market value.

Event study: each announcement is put in a quintile within its sector, using the previous quarter's sector quintile cut-offs (implementable). Drift = sum of issuer daily abnormal returns from trading day t+2 (skipping day t+1 to avoid overlap with the EAR/BAR window) over 30, 60, 90 or 120 trading days. Q5-Q1 reported.
Regressions: subsequent abnormal returns over [2d,21d], [22d,41d], [42d,61d] on CFE, EAR, BAR, plus stock momentum (250 trading days before the announcement, skipping the most recent 20), stock reversal (20 trading days before, skipping the most recent day), past bond abnormal return (same short window), lagged EAR, sector and rating dummies; variables trimmed at 0.5/99.5 percentiles and standardised within each year-quarter.
Tradable test: monthly index-tracking portfolio. Universe: maturity above 3 years, notional above the index 25th percentile, one bond per issuer (prefer bonds under 2 years old, then duration closest to industry average). Maximise portfolio-weighted EAR, using each issuer's most recent EAR from the past three months, subject to 1% max bond weight (about 100 bonds) and exact match to index sector weights, OAS and DTS. Variants: no OAS match, 2% cap, Min-EAR portfolio, and an ESP >= 5 filter (2% cap; HY index restricted to Ba/B).

**Findings.**

- Issuers with positive (negative) surprises earn higher (lower) abnormal bond returns for the next 60 to 70 trading days, after which the drift stops with no reversal. Q5-Q1 spreads grow until about 90 trading days.
- EAR (the 3-day stock reaction) is the strongest surprise measure, CFE second, and the bond's own reaction BAR weakest. In multivariate regressions EAR stays significant with stock momentum, reversal, past bond returns and lagged EAR included, so PEAD in credit is distinct from equity momentum in credit.
- The effect is larger in HY than IG and grows as rating falls. Q5-Q1 is positive in every year, every industry and every rating bucket, and results are unchanged after DTS-adjusting both returns and BAR.
- Liquidity does not explain it. The effect appears in all TES buckets (1-3, 4-7, 8-10); beyond 30 days it is not monotonic in TES, and by return autocorrelation it is larger among liquid issuers.
- A risk-matched, roughly 100-bond Max-EAR index-tracking portfolio outperformed both the IG and HY indices under all specifications. Max-EAR over Min-EAR returns and information ratios are two to four times those of Max-EAR over index, so avoiding negative-surprise issuers matters, especially in IG. Adding an ESP >= 5 cheapness filter raised returns and information ratios further.

**Use for bond signals.** Use EAR (3-day Fama-French-adjusted stock return around the announcement) as an issuer-level credit signal whose drift lasts about 60-70 trading days; start from day t+2, neutralise by sector with lagged cut-offs, and DTS-match. Combine with a value filter (ESP) to decide whether a stale surprise is still unpriced.

Concepts: [[concepts/factor-signals-in-credit|Factor Signals in Credit]] · [[concepts/duration-times-spread|Duration Times Spread (DTS)]] · [[concepts/systematic-credit-relative-value|Systematic Credit Relative Value]] · [[concepts/cross-sectional-momentum|Cross-Sectional Momentum]] · [[concepts/fama-french-factors|Fama-French Factors]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[concepts/information-ratio|Information Ratio]] · [[concepts/post-earnings-announcement-drift|Post-Earnings-Announcement Drift]]

### Chapter 21. Equity Short Interest as a Signal for Credit Investing

**Question.** Does the share of a company's stock that is on loan to short sellers predict downgrades and returns of its corporate bonds, and is it subsumed by bond short interest, relative value or equity momentum?

**Data.** Bloomberg Barclays US Corporate and US High Yield indices, January 2007 to December 2019, monthly. Daily securities lending positions from FIS Astec Analytics (a lower bound on true lending, since not all lenders report). Shares outstanding from Compustat; bonds mapped to US-listed parent common stock (ADRs excluded). Mapped coverage rose from 76% to 84% of IG and 57% to 75% of HY market value. IG uses excess returns over duration-matched Treasuries, HY total returns (Sharpe ratios use 1-month Libor). (PDF pages after the chapter end are the book index.)

**Method.** Signal: $ESI_{i,t}=\frac{\text{shares in outstanding stock loans}_{i,t}}{\text{total shares outstanding}_{i,t}}$, using all contract types, all loans open at business close, any collateral. Example: 2,000,000 shares on loan out of 100,000,000 gives ESI 2%. Bond short interest (BSI) for an issuer = average across its bonds (with at least one open loan) of notional on loan / notional outstanding.

Tests: (1) Downgrades: each month, quintile-sort issuers on prior month-end ESI within each rating bucket; track rating changes over 3, 6, 9, 12 months. (2) Quintiles: on the last trading day of each month sort issuers within sectors (8 sectors) into ESI quintiles, value-weight, hold one month; Q1-Q5 = long least shorted, short most shorted. (3) Index-replicating portfolios (main test): replication universe = senior bonds, maturity above 3 years, notional above the index 25th percentile, one bond per issuer (keep bonds issued under 2 years ago if any, then duration closest to industry average). Each month choose weights that maximise (or minimise) portfolio ESI subject to issuer weight at most 2% (at least 50 issuers, about 55 in practice), sector weights equal to the index, portfolio OAS and DTS equal to the index. 'ESI strategy' = Min-ESI minus Max-ESI.
Combinations: $CSI_{i,t}=z(ESI_{i,t})+z(BSI_{i,t})$ and $ESIvalue_{i,t}=z(ESI_{i,t})-z(ESP_{i,t})$, with z = monthly cross-sectional standardisation to mean 0, std 1; the tilted portfolios maximise/minimise the composite. Conditional tests split the universe into ESP 1-5 vs 6-10, and EMC 1-5 vs 6-10, and rerun Min/Max-ESI.

**Findings.**

- ESI is higher in HY: the value-weighted average was 1.28% for IG issuers versus 3.27% for HY. Within each rating bucket, the highest-ESI quintile suffered more or larger downgrades over 3 to 12 months, in every rating bucket.
- Naive sector-neutral quintile sorts fail: Q1-Q5 had an information ratio of -0.08 in IG and 0.16 in HY, because high-ESI issuers have wider spreads, higher DTS, lower quality and, in IG, worse liquidity, so the long-short is short risk.
- Once OAS, DTS and sectors are matched, ESI works on the short side. In IG the index beat the Max-ESI portfolio in 104 of 155 months by 1.61%/yr, and Min-ESI minus Max-ESI earned 2.06% with IR 1.28. In HY the index beat Max-ESI by 1.97%/yr (100 of 155 months), but Min-ESI lagged the index by 0.37%, so ESI is a one-sided signal.
- Bond short interest adds nothing beyond ESI. In IG it does not predict downgrades or returns, likely because IG bond borrowing is mostly market-making; in HY it works but the ESI+BSI combination (CSI) does not beat ESI alone, and the Max-ESI and Max-CSI portfolios overlap 57%.
- ESI is complementary to value and momentum. Its company-level Spearman correlation with ESP is 0.08 (IG) and -0.04 (HY), and with EMC -0.01 (IG) and -0.09 (HY). Min-ESI beats Max-ESI within both cheap and expensive ESP halves and both EMC halves. In IG the ESIvalue composite reached an IR of 2.42 versus 1.40 for ESP and 1.27 for ESI; in HY the composite was slightly worse than the best single signal.

**Use for bond signals.** Use ESI (shares on loan / shares outstanding) as a monthly issuer-level bearish screen, mainly for underweights. Always test it inside a DTS-, OAS- and sector-matched portfolio, because raw sorts load on spread risk. In IG it pairs well with an ESP value score (ESI minus ESP), whereas bond short interest adds no information beyond it.

Concepts: [[concepts/factor-signals-in-credit|Factor Signals in Credit]] · [[concepts/duration-times-spread|Duration Times Spread (DTS)]] · [[concepts/systematic-credit-relative-value|Systematic Credit Relative Value]] · [[concepts/credit-relative-value|Credit Relative Value]] · [[concepts/cross-sectional-momentum|Cross-Sectional Momentum]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[concepts/information-ratio|Information Ratio]] · [[concepts/equity-short-interest|Equity Short Interest]]

## Questions Raised

- Do these signals survive on corrected bond-return data, with the signal and return prices kept apart?
- How correlated are equity momentum, earnings drift and short interest once each is DTS- and sector-matched, and what does a combined signal add?
- How much of the index-inefficiency alpha (fallen angels, concessions) remains as more investors adopt the same rules?
- Do the value and momentum results transfer to markets with thinner equity coverage, such as private issuers?

## Intended Audience

Credit portfolio managers, quantitative researchers and investment committees who want evidence-based rules for corporate bond selection, with enough method detail to replicate the studies.

## Key Concepts in This Source

- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/variance-risk-premium|Variance Risk Premium]]
- [[concepts/volatility-risk-premia|Volatility Risk Premia (VIRP)]]
- [[concepts/short-volatility-strategies|Short Volatility Strategies]]
- [[concepts/credit-risk-premium|Credit Risk Premium]]
- [[concepts/credit-hedge-ratios-equity-options|Credit Hedge Ratios with Equity Options]]
- [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]]
- [[concepts/bond-market-segmentation|Bond Market Segmentation]]
- [[concepts/information-ratio|Information Ratio]]
- [[concepts/structural-models|Structural Models]]
- [[concepts/low-risk-anomaly|Low-Risk Anomaly]]
- [[concepts/cds-bond-basis|CDS-Bond Basis]]
- [[concepts/bond-liquidity|Bond Liquidity]]
- [[concepts/liquidity-risk|Liquidity Risk]]
- [[concepts/mean-reversion|Mean Reversion]]
- [[concepts/bond-index-inclusion-criteria|Bond Index Inclusion Criteria]]
- [[concepts/index-reconstitution|Index Reconstitution]]
- [[concepts/event-risk|Event Risk]]
- [[concepts/fallen-angel|Fallen Angel]]
- [[concepts/liquidity-scoring-mechanism|Liquidity Scoring Mechanism]]
- [[concepts/credit-default-swaps|Credit Default Swaps]]
- [[concepts/factor-signals-in-credit|Factor Signals in Credit]]
- [[concepts/systematic-credit-relative-value|Systematic Credit Relative Value]]
- [[concepts/credit-relative-value|Credit Relative Value]]
- [[concepts/duration-times-spread|Duration Times Spread (DTS)]]
- [[concepts/corporate-bond-liquidity-premium|Corporate Bond Liquidity Premium]]
- [[concepts/bid-ask-spread|Bid-Ask Spread]]
- [[concepts/credit-spread-changes|Credit Spread Changes]]
- [[concepts/new-issue-concession|New-Issue Concession]]
- [[concepts/default-rates|Default Rates]]
- [[concepts/speculative-grade-default-rate|Speculative-Grade Default Rate]]
- [[concepts/credit-spread-curve|Credit Spread Curve]]
- [[concepts/credit-spread-forecasting|Credit Spread Forecasting]]
- [[concepts/rating-based-stop-loss|Rating-Based Stop-Loss]]
- [[concepts/survival-probability|Survival Probability]]
- [[concepts/hazard-rate-curve|Hazard Rate Curve]]
- [[concepts/z-spread|Z-Spread]]
- [[concepts/empirical-duration|Empirical Duration]]
- [[concepts/carry-rolldown|Carry and Rolldown]]
- [[concepts/value-premium|Value Premium]]
- [[concepts/leverage-ratios|Leverage Ratios]]
- [[concepts/factor-investing|Factor Investing in Corporate Bonds]]
- [[concepts/fama-french-factors|Fama-French Factors]]
- [[concepts/excess-spread-to-peers|Excess Spread to Peers (ESP)]]
- [[concepts/turnover-buffer|Turnover Buffer]]
- [[concepts/spread-per-turn-of-leverage|Spread Per Turn of Leverage]]
- [[concepts/risk-vs-mispricing|Risk-vs-Mispricing Debate]]
- [[concepts/cross-sectional-momentum|Cross-Sectional Momentum]]
- [[concepts/residual-momentum|Residual Momentum]]
- [[concepts/spillover-effect|Momentum Spillover Effect]]
- [[concepts/alpha-correlation-turnover|Alpha Correlation and Turnover]]
- [[concepts/equity-momentum-in-credit|Equity Momentum in Credit]]
- [[concepts/factor-timing|Factor Timing]]
- [[concepts/cross-asset-rotation|Cross-Asset Rotation Strategy]]
- [[concepts/illiquidity-premium|Illiquidity Premium]]
- [[concepts/autocorrelation-time-series|Autocorrelation in Time Series]]
- [[concepts/risk-premia|Risk Premia (Expected Return Sources)]]
- [[concepts/issuer-size-premium|Issuer Size Premium]]
- [[concepts/liquidity-cost-score|Liquidity Cost Score (LCS)]]
- [[concepts/quantamental-investing|Quantamental Investing]]
- [[concepts/post-earnings-announcement-drift|Post-Earnings-Announcement Drift]]
- [[concepts/equity-short-interest|Equity Short Interest]]

## Entities

- [[entities/arik-ben-dor|Arik Ben Dor]]
- [[entities/albert-desclee|Albert Desclée]]
- [[entities/lev-dynkin|Lev Dynkin]]
- [[entities/jay-hyman|Jay Hyman]]
- [[entities/simon-polbennikov|Simon Polbennikov]]

## Related Sources

- [[sources/bendor-2007-dts|DTS (Duration Times Spread) - A New Measure of Spread Exposure in Credit Portfolios]]
- [[sources/haesen-2017-momentum-spillover|Momentum Spillover from Stocks to Corporate Bonds]]
- [[sources/houweling-2017-factor-investing|Factor Investing in the Corporate Bond Market]]
- [[sources/jostova-2013-momentum|Momentum in Corporate Bond Returns]]
- [[sources/dickerson-2024-bond-pitfalls|Common Pitfalls in the Evaluation of Corporate Bond Strategies]]
<!-- AUTHORED REGION END -->