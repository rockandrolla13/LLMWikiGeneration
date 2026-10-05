---
authors:
- Christopher C. Finger (ed.)
- Vladimir Finkelstein
- Jean-Pierre Lardy
- George Pan
- Thomas Ta
- John Tierney
content_hash: sha256:0ffc70317e8759470917dfa81966965a6e30a5ea493348c16b0463db07fa442b
created: '2026-10-05T15:52:32Z'
page_id: sources/finger-2002-creditgrades-technical-document
page_type: source
publication_date: '2002'
publication_venue: RiskMetrics Group
related:
- concepts/structural-models
- concepts/merton-model
- concepts/credit-default-swaps
- concepts/credit-default-swap-spread
- concepts/capital-structure-arbitrage
- concepts/survival-probability
- concepts/implied-volatility-skew
- concepts/reduced-form-credit-models
- concepts/credit-hedge-ratios-equity-options
- concepts/creditgrades-model
- sources/kapadia-2012-limited-arbitrage-equity-credit
- sources/avino-2024-hedging-credit-equity-options
- sources/cao-2023-implied-vol-bond-returns
- sources/dafonseca-2020-cds-equity-volatility-comovement
- analyses/capital-structure-arbitrage-literature-review
- entities/christopher-finger
- entities/vladimir-finkelstein
- entities/jean-pierre-lardy
- entities/george-pan
- entities/thomas-ta
- entities/john-tierney
- entities/riskmetrics-group
- entities/jp-morgan
- entities/deutsche-bank
- entities/goldman-sachs
revision_id: 1
schema_version: 2
source_hash: sha256:84d8e448069b7bbec9ad90cb153132382c4097def7d21f4157de0f447e9764f6
source_path: markdown_output/finger-2002-creditgrades-technical-document.md
source_type: notes
sources: []
tags:
- creditgrades
- structural-models
- credit-default-swaps
- default-barrier
- equity-to-credit
- asset-volatility
- capital-structure-arbitrage
- industry-model
title: CreditGrades Technical Document
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: 2d88e1f3-a9af-5bc9-a89e-f92d085b5563
version_read: Technical document, May 2002 (RiskMetrics Group)
year: 2002
---

<!-- AUTHORED REGION START -->
# CreditGrades Technical Document

**Authors:** Christopher C. Finger (ed.), Vladimir Finkelstein, Jean-Pierre Lardy, George Pan, Thomas Ta, John Tierney · **Year:** 2002 · **Venue:** RiskMetrics Group
**Version read:** Technical document, May 2002 (RiskMetrics Group)

## Summary

This is the technical manual for CreditGrades, a structural credit model released by RiskMetrics with JPMorgan, Goldman Sachs and Deutsche Bank. Its stated aim is a transparent, standard way to turn equity market data into a credit spread. Unlike default-trained commercial models, it is tuned to match CDS spreads, not to predict default rates.

The model follows Black and Cox. The firm defaults when its asset value first hits a barrier equal to the recovery on its debt. The key change is that the barrier level is uncertain, drawn from a lognormal distribution. This lets default happen suddenly and lifts short-dated spreads, which pure diffusion models get too low. Asset value and volatility are tied to the stock price and equity volatility by simple approximations, so the result is a closed-form survival probability and CDS spread.

The empirical chapter picks the volatility input. A 1,000-day historical equity volatility best matches the volatilities implied by 5-year CDS quotes. As a ranking tool, the model agrees with market CDS rankings better than Moody's RiskCalc.

The case studies show both uses and limits. When a firm's stock or volatility moves fast (Tyco, WorldCom), the historical-volatility input lags and the model spread is too low until implied volatility is used. In the monitoring cases (Enron, Kmart, Rite Aid, Lucent), the model's default probability rose weeks or months before S&P downgrades.

## Data

- Calibration and testing: mid-market 5-year CDS quotes, May 2000 to August 2001, 122 U.S. firms across ratings AAA to CCC and nine sectors; 6,194 quotes in total.
- Bond-specific recovery rates: JPMorgan database.
- Stock prices and 5-year LIBOR: DataMetrics; implied ATM equity volatility (longest tenor) from DataMetrics for the implied-volatility variant.
- Recovery mean and dispersion: Portfolio Management Data / S&P recovery database (Hu and Lawrence 2000), about 300 non-financial U.S. defaulters, 1987-1997.
- Debt per share: Bloomberg balance-sheet fields (short- and long-term borrowing, other liabilities, minority interest, preferred equity, market cap).
- Ranking comparison on 30 January 2001 and 15 November 2001 against Moody's RiskCalc and CDS-implied default probabilities.

## Method

Asset value per share $V$ follows GBM $dV_t/V_t = \sigma\,dW_t + \mu\,dt$ with $\mu$ set to 0 (leverage assumed stationary). Barrier $\bar L D$ with random recovery $L = \bar L e^{\lambda Z - \lambda^2/2}$, $Z \sim N(0,1)$ independent of $W$. Barrier uncertainty is approximated by starting a Brownian motion at time $-\lambda^2/\sigma^2$, which gives the closed form
$$P(t) = \Phi\left(-\frac{A_t}{2} + \frac{\ln d}{A_t}\right) - d\,\Phi\left(-\frac{A_t}{2} - \frac{\ln d}{A_t}\right),\quad d = \frac{S_0 + \bar L D}{\bar L D}e^{\lambda^2},\quad A_t^2 = \sigma^2 t + \lambda^2.$$
Market-observable mapping: $V_0 = S_0 + \bar L D$ and $\sigma = \sigma_S^* \frac{S^*}{S^* + \bar L D}$ for a reference price and volatility. CDS par spread with constant $r$ and issue recovery $R$:
$$c^* = r(1-R)\frac{1 - P(0) + e^{r\xi}(G(t+\xi) - G(\xi))}{P(0) - P(t)e^{-rt} - e^{r\xi}(G(t+\xi) - G(\xi))},\quad \xi = \lambda^2/\sigma^2,$$
where $G$ is the Rubinstein-Reiner first-passage function. Standard parameters: $\bar L = 0.5$, $\lambda = 0.3$. Debt per share = (ST borrowing + LT borrowing + 0.5 x other ST and LT liabilities - minority-interest adjustment) / (common shares + preferred-equivalent shares). Implied asset volatility is the $\sigma$ that matches a CDS quote; candidate estimators (252/500/750/1000/1250-day windows and EWMA with decay 0.94) are compared against it. Delta, gamma and vega of the CDS are given against equity price. Ranking accuracy is measured with cumulative accuracy profiles, decile mismatch histograms, Pearson correlation and Kendall's tau versus CDS-implied default probabilities.

## Key Findings

1. Implied asset volatility is stable through time for most firms. Among historical estimators, the 1,000-day window works best, with 88 percent of estimates within 10 percent of the CDS-implied value. Short-window and EWMA estimators do poorly.
2. The calibration sample is 6,194 five-year CDS quotes on 122 U.S. firms. Global recovery mean and dispersion are set to 0.50 and 0.30, taken from roughly 300 defaulted non-financial firms.
3. In ranking firms against CDS-implied default probabilities, CreditGrades reaches a Kendall's tau of 0.522 (January 2001) and 0.667 (November 2001). Moody's RiskCalc gets 0.358 and 0.502. The November Pearson correlation for CreditGrades is 0.816.
4. For Tyco in early 2002, the standard model gave about 230 bp while bond spreads were over 500bp, because the 1,000-day volatility lagged. Raising asset volatility to 60 percent gave 580bp, in line with the market. This shows the historical-volatility input lags in fast-moving names.
5. A WorldCom case trade, buying protection plus a stock hedge in September 2001 with a 10:1 hedge ratio, shows a 79 percent return on the equity outlay by end-March 2002.
6. As a monitoring tool, the model's 5-year default probability moved ahead of agency ratings. Kmart's rose from 17 to 24 percent about two months before an S&P downgrade. Lucent's went from 0.22 percent to 0.90 percent in mid-2000, while S&P waited until December.

## Limitations

- The model has no inputs for bond supply/demand, liquidity, new issuance or CDS-cash basis technicals; spreads within 10-20 percent of market are presented as normal agreement.
- The historical volatility input lags sudden moves; the document recommends checking implied volatility in such cases.
- Debt per share comes from quarterly/annual filings and misses intra-period capital structure changes and finance subsidiaries; banks and finance firms are excluded because the model gives far too high spreads.
- The time-shifted approximation implies a non-zero default probability at t = 0, which the authors call a technical artifact.
- Calibration sample is short (May 2000-August 2001). The case studies are chosen after the fact. The WorldCom trade return was later shown by Yu (2006) to depend on an undisciplined buy-and-hold exit.
- Vendor document with commercial endorsers; not peer reviewed.

## Questions Raised

- How much of the model-market spread gap is volatility mismeasurement that option-implied volatility would fix, versus true dislocation?
- Is a fixed barrier dispersion (lambda = 0.3) adequate across sectors and the cycle, or should it vary with leverage and debt maturity?
- Does the lead of model default probabilities over rating changes persist out of sample and after controlling for equity returns alone?

## Relevance to Bond Signals

CreditGrades gives a closed-form equity-implied spread from stock price, long-window equity volatility and debt per share. That makes it an easy fair-value anchor for corporate bond spreads. Market-minus-model spread gaps, and the model's default probability as an early-warning feature, are direct inputs for bond relative-value and downgrade-risk signals.

See [[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage: Literature Review for Bond Signals]].

## Concepts

- [[concepts/structural-models|Structural Models]]
- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/credit-default-swaps|Credit Default Swaps]]
- [[concepts/credit-default-swap-spread|Credit Default Swap Spread]]
- [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]]
- [[concepts/survival-probability|Survival Probability]]
- [[concepts/implied-volatility-skew|Implied Volatility Skew]]
- [[concepts/reduced-form-credit-models|Reduced-Form Credit Models]]
- [[concepts/credit-hedge-ratios-equity-options|Credit Hedge Ratios with Equity Options]]
- [[concepts/creditgrades-model|CreditGrades Model]]

## Entities

- [[entities/christopher-finger|Christopher C. Finger]]
- [[entities/vladimir-finkelstein|Vladimir Finkelstein]]
- [[entities/jean-pierre-lardy|Jean-Pierre Lardy]]
- [[entities/george-pan|George Pan]]
- [[entities/thomas-ta|Thomas Ta]]
- [[entities/john-tierney|John Tierney]]
- [[entities/riskmetrics-group|RiskMetrics Group]]
- [[entities/jp-morgan|JPMorgan]]
- [[entities/deutsche-bank|Deutsche Bank]]
- [[entities/goldman-sachs|Goldman Sachs]]

## Related Sources

- [[sources/kapadia-2012-limited-arbitrage-equity-credit|Limited arbitrage between equity and credit markets]]
- [[sources/avino-2024-hedging-credit-equity-options|Contingent Claims and Hedging of Credit Risk with Equity Options]]
- [[sources/cao-2023-implied-vol-bond-returns|Implied Volatility Changes and Corporate Bond Returns]]
- [[sources/dafonseca-2020-cds-equity-volatility-comovement|The Co-Movement of Credit Default Swap Spreads, Equity Returns and Volatility: Evidence from Asia-Pacific Markets]]
<!-- AUTHORED REGION END -->