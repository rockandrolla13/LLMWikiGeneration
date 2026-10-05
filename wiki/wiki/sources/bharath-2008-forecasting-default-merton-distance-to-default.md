---
authors:
- Sreedhar T. Bharath
- Tyler Shumway
content_hash: sha256:117f9ac224c3e7bb7706542c80de7da1a1d0a6b21c05e21e6fb0764fb7f32036
created: '2026-10-05T15:52:32Z'
page_id: sources/bharath-2008-forecasting-default-merton-distance-to-default
page_type: source
publication_date: '2008'
publication_venue: Review of Financial Studies 21(3)
related:
- concepts/merton-model
- concepts/structural-models
- concepts/default-rates
- concepts/credit-default-swap-spread
- concepts/survival-probability
- concepts/reduced-form-credit-models
- concepts/distance-to-default
- sources/collin-dufresne-2001-determinants-credit-spread-changes
- sources/huang-2025-global-credit-spread-puzzle
- sources/kapadia-2012-limited-arbitrage-equity-credit
- analyses/capital-structure-arbitrage-literature-review
- entities/sreedhar-bharath
- entities/tyler-shumway
- entities/moodys
revision_id: 1
schema_version: 2
source_hash: sha256:9025dbda9a3f2b6867f259a324b07f9a98000da9ffd28ed2753cbb0069479c87
source_path: markdown_output/bharath-2008-forecasting-default-merton-distance-to-default.md
source_type: paper
sources: []
tags:
- distance-to-default
- merton-model
- default-prediction
- hazard-models
- naive-distance-to-default
- kmv
- cds-implied-default-probability
- bond-spreads
title: Forecasting Default with the Merton Distance to Default Model
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: aade2b04-ee1f-5c64-8573-bc0a55273929
version_read: Published version (RFS 21(3), pp. 1339-1369), JSTOR scan; markdown is
  an OCR text layer with garbled equations
year: 2008
---

<!-- AUTHORED REGION START -->
# Forecasting Default with the Merton Distance to Default Model

**Authors:** Sreedhar T. Bharath, Tyler Shumway · **Year:** 2008 · **Venue:** Review of Financial Studies 21(3)
**Version read:** Published version (RFS 21(3), pp. 1339-1369), JSTOR scan; markdown is an OCR text layer with garbled equations

## Summary

The paper tests the Merton distance-to-default (DD) model, the KMV-style method that backs firm value and asset volatility out of equity data. It asks three things. Is the Merton default probability a sufficient statistic for default? Does its functional form matter? Does the iterative solution for firm value and volatility matter?

To separate form from solution, the authors build a 'naive' DD. It keeps the same z-score shape but uses rough plug-ins. Debt is valued at face value. Debt volatility is a simple function of equity volatility. Expected asset return is last year's stock return. No equations are solved.

The Merton probability is a strong predictor on its own, but it is not sufficient. Other variables, especially past excess returns and net income over assets, add power. Once the naive measure and these variables are in a hazard model, the Merton probability adds little or nothing. The naive measure forecasts slightly better out of sample. It also tracks CDS-implied default probabilities and bond spreads better than the Merton measure does.

The conclusion is that the Merton model's value lies in its functional form, not in solving for unobserved firm value. A model that combines the naive DD with returns and accounting data does best.

## Data

- Firms: intersection of Compustat Industrial Quarterly and CRSP daily (NYSE, AMEX, NASDAQ), 1980-2003; financial SIC codes 6021, 6022, 6029, 6035, 6036 excluded.
- Defaults: Altman default database (1980-2000) plus Moody's default lists (2001-2003); 1449 defaults among 15,018 firms; 1,016,552 firm-months with complete data.
- Inputs: equity volatility from prior-year daily returns; face value of debt = Compustat item 45 (debt in current liabilities) + 0.5 x item 51 (long-term debt); risk-free rate from 1-year Treasury CMT in the text (Table 1 note says 3-month T-bill); market equity from CRSP; past excess return vs CRSP VW index; net income / total assets. Variables winsorised at 1st/99th percentiles (default probabilities not winsorised).
- Moody's KMV EDFs for 80 firms (August 2000) from a CFO Magazine article.
- Option-implied volatility: OptionMetrics IVY, 30-day ATM calls, 1996-2003 (101,201 firm-months).
- CDS: credittrade.com, December 1998 to July 2003, 3833 firm-months.
- Bonds: Lehman Brothers Fixed Income Database (Warga), 1980-1997, trader-priced, option-free, index-eligible, non-AAA; 61,776 bond-months; Treasury benchmarks from CRSP fixed-term indices.

## Method

Merton DD: equity is a call on firm value, $E = V N(d_1) - e^{-rT} F N(d_2)$, with $d_1 = \frac{\ln(V/F) + (r + 0.5\sigma_V^2)T}{\sigma_V\sqrt{T}}$, $d_2 = d_1 - \sigma_V\sqrt T$. The volatility link is $\sigma_E = \frac{V}{E}N(d_1)\sigma_V$. Following Crosbie-Bohn and Vassalou-Xing, they start from $\sigma_V = \sigma_E E/(E+F)$, invert the equity equation daily over the past year, re-estimate $\sigma_V$ and $\mu$ from implied asset returns, and iterate until $\sigma_V$ changes by less than $10^{-3}$. With $T = 1$:
$$DD = \frac{\ln(V/F) + (\mu - 0.5\sigma_V^2)T}{\sigma_V\sqrt T},\qquad \pi_{Merton} = N(-DD).$$
Naive DD: $\text{naive }D = F$, $\text{naive }\sigma_D = 0.05 + 0.25\sigma_E$, $\text{naive }\sigma_V = \frac{E}{E+F}\sigma_E + \frac{F}{E+F}(0.05 + 0.25\sigma_E)$, expected return = firm's prior-year stock return $r_{it-1}$:
$$\text{naive }DD = \frac{\ln[(E+F)/F] + (r_{it-1} - 0.5\,\text{naive }\sigma_V^2)T}{\text{naive }\sigma_V\sqrt T},\qquad \pi_{naive} = N(-\text{naive }DD).$$
Alternatives: Merton DD with $\mu = r$; simultaneous (non-iterative) solution of the two equations; simultaneous solution with option-implied $\sigma_E$. Tests: Cox proportional hazard models $\lambda(t) = \phi(t)\exp(x(t)'\beta)$ with time-varying covariates; out-of-sample quarterly decile sorts counting defaults per decile (hazard models re-estimated each quarter on past data for 1991-2003); CDS-implied one-year default probability from a discrete annual-payment CDS pricing equation with 75% risk-neutral LGD, then regressions of log CDS spread and $\pi_{CDS}$ on the DD probabilities; bond yield spread regressions with rating, year and industry dummies and accounting controls; hazard models adding bond spread.

## Key Findings

1. The sample covers 15,018 non-financial firms and 1,016,552 firm-months from 1980 to 2003, with 1449 defaults.
2. The naive and Merton default probabilities are highly correlated (0.8642), as are the naive and iterated asset volatilities (0.8748). Both probabilities rank-correlate about equally with Moody's KMV EDFs for 80 firms (0.788 and 0.786). The naive asset volatility tracks KMV's volatility much better than the iterated one (0.853 vs 0.574).
3. In Cox hazard models both probabilities are strongly significant together (Merton 1.697, naive 2.472), so the Merton probability is not a sufficient statistic. Once size, debt, inverse equity volatility, past excess return and NI/TA are added, the Merton coefficient falls to an insignificant 0.230. The naive probability stays significant at 1.366.
4. Out of sample (1980-2003), the top decile by Merton probability captures 64.9% of next-quarter defaults versus 65.8% for the naive probability. Over 1991-2003, a hazard model combining the naive probability with returns and NI/TA (Model 7) captures 75.8% versus 69.4% for the Merton probability.
5. Estimating the drift matters. Setting expected asset return equal to the risk-free rate drops top-decile capture to 60.0%. The naive model also misclassifies fewer defaulters into the safest half (5.7%) than a linear hazard model with the same inputs (8.5%).
6. CDS-implied one-year default probabilities correlate more with the naive measure (0.5199) than with the Merton measure (0.3762). In joint regressions of log CDS spreads, the naive measure drives out the Merton measure.
7. Within rating classes, bond yield spreads load on the default probabilities but only weakly. A coefficient of 0.5 on the naive probability means a move from 0% to 5% adds just 2.5 basis points of spread.

## Limitations

- The Merton DD implementation is a 'feasible' academic version, not Moody's KMV's proprietary model (different debt treatment, empirical DD-to-EDF mapping).
- The naive model's numerical choices (5% + 25% of equity vol for debt vol, past return as drift) are ad hoc by the authors' own account.
- Implied-volatility results rest on only 88 defaults; the bond-spread hazard test shrinks to 571 firms and 58 defaults.
- CDS-implied probabilities assume a 75% LGD and a simplified annual-payment pricing equation; about a quarter of firms show risk-neutral below physical probability, contrary to theory.
- Bond spread regressions condition on rating dummies, which absorb most spread variation, so small coefficients may understate economic content.
- Text and Table 1 note disagree on the risk-free rate used (1-year CMT vs 3-month T-bill).

## Questions Raised

- Would a richer drift or volatility specification (for example option-implied volatility across the full sample) restore value to solving the Merton system?
- How should distance to default be mapped into probabilities for pricing, given that it ranks defaults well but fits CDS and bond spread levels poorly?
- Does the bond spread itself dominate equity-based default measures in larger samples, as the small-sample hazard test suggests?

## Relevance to Bond Signals

A naive distance to default needs only market equity, face value of debt, equity volatility and the past-year return. It is a cheap, robust default-risk feature for corporate bond signals, and it matches or beats the iterated Merton version. For spread prediction, it should be combined with past returns and profitability, and judged within rating buckets, where its marginal spread effect is small.

See [[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage: Literature Review for Bond Signals]].

## Concepts

- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/structural-models|Structural Models]]
- [[concepts/default-rates|Default Rates]]
- [[concepts/credit-default-swap-spread|Credit Default Swap Spread]]
- [[concepts/survival-probability|Survival Probability]]
- [[concepts/reduced-form-credit-models|Reduced-Form Credit Models]]
- [[concepts/distance-to-default|Distance to Default]]

## Entities

- [[entities/sreedhar-bharath|Sreedhar T. Bharath]]
- [[entities/tyler-shumway|Tyler Shumway]]
- [[entities/moodys|Moody's KMV]]

## Related Sources

- [[sources/collin-dufresne-2001-determinants-credit-spread-changes|The Determinants of Credit Spread Changes]]
- [[sources/huang-2025-global-credit-spread-puzzle|The Global Credit Spread Puzzle]]
- [[sources/kapadia-2012-limited-arbitrage-equity-credit|Limited arbitrage between equity and credit markets]]
<!-- AUTHORED REGION END -->