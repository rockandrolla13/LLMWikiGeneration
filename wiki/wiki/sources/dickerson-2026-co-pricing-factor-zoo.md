---
authors:
- Alexander Dickerson
- Christian Julliard
- Philippe Mueller
content_hash: sha256:589bb5ee312538e277291a956486b6379a5a856c8e5ce5eb0cbb5137983f220b
created: '2026-10-05T15:52:32Z'
page_id: sources/dickerson-2026-co-pricing-factor-zoo
page_type: source
publication_date: '2026'
publication_venue: Journal of Financial Economics (forthcoming); arXiv 2604.04430
related:
- concepts/bayesian-model-averaging
- concepts/factor-models
- concepts/corporate-bonds
- concepts/bond-capm
- concepts/term-structure-risk-premium
- concepts/bond-market-segmentation
- concepts/credit-risk-premium
- concepts/baa-corporate-bond-spread
- concepts/factor-investing
- concepts/business-cycles
- concepts/multiple-testing
- concepts/approximate-factor-models
- sources/dickerson-2023-bond-risk
- sources/dickerson-2024-bond-pitfalls
- sources/kelly-2026-ipca
- sources/avramov-2025-predictability-corporate-bond-returns-structured-approach
- sources/bali-2022-bond-ml
- sources/houweling-2017-factor-investing
- sources/dickerson-2026-corporate-bond-factor-replication-crisis
- analyses/capital-structure-arbitrage-literature-review
- entities/alexander-dickerson
- entities/christian-julliard
- entities/philippe-mueller
revision_id: 1
schema_version: 2
source_hash: sha256:2bf6fadbb0cb5618aab7dd1104cf95668204bec587e6074c2809d34c9b5263dd
source_path: markdown_output/dickerson-2026-co-pricing-factor-zoo.md
source_type: paper
sources: []
tags:
- factor-zoo
- stochastic-discount-factor
- bayesian-model-averaging
- corporate-bonds
- bond-stock-co-pricing
- treasury-term-structure-risk
- post-earnings-announcement-drift
- dense-sdf
title: The Co-Pricing Factor Zoo
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: 0533a61f-5317-5f1b-bb97-2c4590d91844
version_read: arXiv 2604.04430v1 (stamp 6 Apr 2026); earlier circulated as 'The Corporate
  Bond Factor Zoo'
year: 2026
---

<!-- AUTHORED REGION START -->
# The Co-Pricing Factor Zoo

**Authors:** Alexander Dickerson, Christian Julliard, Philippe Mueller · **Year:** 2026 · **Venue:** Journal of Financial Economics (forthcoming); arXiv 2604.04430
**Version read:** arXiv 2604.04430v1 (stamp 6 Apr 2026); earlier circulated as 'The Corporate Bond Factor Zoo'

## Summary

The paper asks which factors jointly price US corporate bonds and stocks. It takes 54 published factors: 16 tradable bond factors, 24 tradable stock factors and 14 nontradable macro and financial factors. Every combination of these is a candidate model, about 18 quadrillion in total. A Bayesian method scores all of them at once and averages them into one stochastic discount factor (SDF), the BMA-SDF.

Only five factors are individually likely to belong in the SDF: bond and stock post-earnings-announcement drift (PEADB, PEAD), idiosyncratic equity volatility (IVOL), the Treasury yield slope (YSP) and the AAA/BAA spread (CREDIT). But no small model is enough. The data want about 22 factors, because many factors are noisy proxies for the same underlying risks. Averaging them cuts the noise. The BMA-SDF prices bonds and stocks better than CAPM, the bond CAPM, FF5, the intermediary model, KNS and RPPCA, both in and out of sample.

The headline for bond research: corporate bond excess returns mix credit risk with Treasury term-structure risk. Bond factors are needed only because they price the Treasury part. Once bond returns are duration-adjusted, stock and nontradable factors alone price bonds and stocks as well as the full model. So the bond factor zoo is largely redundant for the credit part.

A tradable version, weighting factors by their posterior prices of risk and rebalanced yearly, earns an out-of-sample Sharpe ratio of 1.5 to 1.8 from July 2004 to December 2022. The SDF and its volatility move with the business cycle, spike in crises and predict future factor returns.

## Data

- Bonds: constituents of ICE BofA (BAML) High Yield (H0A0) and Investment Grade (C0A0) indices, January 1997 to December 2022, extended back to January 1986 with the Lehman Brothers Fixed Income database; merged with Mergent FISD and CRSP.
- Monthly; 444 months (1986:01-2022:12). Bond returns are not winsorized or trimmed.
- Returns: excess over the one-month risk-free rate (French website); also duration-adjusted returns net of a duration-matched Treasury portfolio (after van Binsbergen et al. 2025).
- Factors: 40 tradable (16 bond, 24 stock) and 14 nontradable = 54; robustness extends to 91 candidates.
- In-sample test assets: 50 bond portfolios (25 credit spread x size, 25 rating x maturity), 33 stock anomaly portfolios, plus the 40 tradable factors (N = 123).
- Out-of-sample assets: 77 bond and 77 stock portfolios from 14 cross-sections (16,383 combinations), 29 Treasury portfolios (2- to 30-year, Liu-Wu yields), and Jensen-Kelly-Pedersen and Dick-Nielsen et al. anomaly sets.
- Robustness data: LBFI/BAML firm-level, quote-only, WRDS TRACE and DFPS TRACE.

## Method

Linear SDF $M_t=1-(f_t-E[f_t])^\top\lambda_f$; cross-sectional layer $\mu_R=\lambda_c 1_N+C_f\lambda_f+\alpha$ with pricing errors $\alpha\sim N(0_N,\sigma^2\Sigma_R)$, following the Bryzgalova, Huang and Julliard (2023) method. Time-series layer: Normal-inverse-Wishart posterior for factor and return moments.

Continuous spike-and-slab prior: $\lambda_j\mid\gamma_j,\sigma^2\sim N(0,\,r(\gamma_j)\psi_j\sigma^2)$ with $r(1)=1$, $r(0)=r\ll1$ (set to 0.001), $\pi(\gamma_j=1\mid\omega_j)=\omega_j$, $\omega_j\sim Beta(a_\omega,b_\omega)$ (baseline Beta(1,1), 50% prior inclusion), and $\psi_j=\psi\,\tilde\rho_j^\top\tilde\rho_j$ where $\tilde\rho_j$ are cross-sectionally demeaned factor-asset correlations. Weak factors get small $\psi_j$ and are shrunk to zero. The paper's extension: $\lambda\mid\sigma^2,\gamma\sim N(0,\sigma^2D^{-1})$, with a hyperparameter $\kappa\in(-1,1)$ scaling prior precision by $(1+\kappa)$ for bond and $(1-\kappa)$ for stock factors, so one can tilt the prior Sharpe-ratio share toward one factor class. The prior Sharpe ratio is set as 20-80% of the ex post maximum (5.4 annualized); results are shown mostly at 80%.

BMA-SDF: $M^{BMA}_t=\sum_{m=1}^{\bar m}M_{t,\gamma^m}\Pr(\gamma^m\mid data)$, which equals the factor-space average $M^{BMA}_t=1-\sum_{j=1}^{K}E[\lambda_j\mid data,\gamma_j=1]\Pr(\gamma_j=1\mid data)(f_{j,t}-E[f_{j,t}])$ as $r\to0$. Posterior probabilities say which factors are likely true risks; posterior prices of risk $E[\lambda_j\mid data]$ give portfolio weights. Self-pricing of tradable factors penalizes noisy proxies; a simulation shows the BMA recovers the true price of risk even when only noisy proxies are included.

Duration-adjusted return: $R_{bond\,i,t}-R^{Treasury}_{dur\,bond\,i,t}=(R_{bond\,i,t}-R_{f,t})-(R^{Treasury}_{dur\,bond\,i,t}-R_{f,t})$, i.e. excess return minus its Treasury component. Benchmarks are estimated by GLS-GMM. Trading: normalize posterior MPRs of tradable factors to sum to one, scale to MKTS volatility, expanding window from a 222-month start, re-estimated yearly. Economic properties: ARMA(3,1) for the conditional mean, GARCH(1,1) for conditional volatility; predictive regressions of factor returns on $E_{t-1}[\sigma^2_t]$ and $E_{t-1}[M_t]\times E_{t-1}[\sigma^2_t]$.

## Key Findings

1. With 54 factors (40 tradable, 14 nontradable) the model space is 2^54, about 18 quadrillion models. Only five factors have posterior inclusion probability above the 50% prior across all shrinkage levels: PEADB, PEAD, IVOL, YSP and CREDIT. At an 80% prior, 30 of the 40 tradable factors are below 40%.
2. The SDF is dense. The posterior median number of factors is 22, with a 95% interval of 15 to 29; models with fewer than 10 factors have near-zero probability. The top five factors explain only about 47% of the BMA-SDF's time-series variation.
3. Out of sample, the BMA-SDF beats its closest rival (KNS) in 96.6% to 99.9% of 16,383 alternative test-asset cross-sections, depending on the fit measure.
4. A tradable BMA-SDF portfolio, rebalanced yearly, earns an out-of-sample annualized Sharpe ratio of 1.5 to 1.8 over July 2004 to December 2022. The equal-weighted factor portfolio earns 1.1. One dollar grows to $174, against $71 for RPPCA.
5. Bond factors price the Treasury part of corporate bond returns; stock factors cannot. A bond-factor BMA-SDF prices the Treasury component with a constrained R^2 of about 97% in sample and 92% out of sample. The stock-factor SDF reaches only 6%. With duration-adjusted bond returns, a stock-only BMA-SDF co-prices bonds and stocks as well as the full model.
6. At an 80% prior, discount-rate-news factors account for 75% of the SDF's squared Sharpe ratio versus 56% for cash-flow-news factors. The shares overlap, so the same risks are captured by several factor types.
7. Lagged SDF moments predict factor returns. At the monthly horizon the predictive regressions are significant in 75% of cases at 10% and 62% at 5%. SDF volatility shocks have a half-life of about 16.6 months, against 4.2 months for FF5 and 3 months for CAPMB.

## Limitations

Results are for linear SDFs and depend on prior settings (prior Sharpe ratio, sparsity, kappa tilt), although the paper reports these are robust. Baseline bond data are index-constituent quotes (BAML/LBFI, partly matrix-priced before 1997); TRACE-based data are used only as robustness checks. The tradable strategy ignores trading costs and uses only tradable factors. The factor set is limited to factors with public monthly series over the full sample. GARCH is fitted to the posterior-mean SDF rather than across draws, which the authors note is a computational compromise. Most robustness detail sits in the Internet Appendix, which was not in the file read.

## Questions Raised

- Does the credit component of bond returns stay priced by equity information once bond returns are corrected for the TRACE biases flagged in the companion replication-crisis paper?
- Is the bond PEAD factor (PEADB) implementable at bond-level trading costs, given it is the strongest tradable bond signal here?
- Can the dense BMA weighting be applied to bond-level signals rather than factor portfolios?

## Relevance to Bond Signals

For corporate-bond signal design, strip out Treasury/duration exposure before judging a credit signal; much apparent bond-factor power is term-structure risk. Equity-side information (PEAD, idiosyncratic volatility) and macro state variables (yield slope, AAA/BAA spread) are the most robust drivers. Combine many noisy signals with shrinkage weighting rather than picking a few.

See [[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage: Literature Review for Bond Signals]].

## Concepts

- [[concepts/bayesian-model-averaging|Bayesian Model Averaging]]
- [[concepts/factor-models|Factor Models]]
- [[concepts/corporate-bonds|Corporate Bonds]]
- [[concepts/bond-capm|Bond CAPM]]
- [[concepts/term-structure-risk-premium|Term Structure Risk Premium]]
- [[concepts/bond-market-segmentation|Bond Market Segmentation]]
- [[concepts/credit-risk-premium|Credit Risk Premium]]
- [[concepts/baa-corporate-bond-spread|BAA Corporate Bond Spread]]
- [[concepts/factor-investing|Factor Investing in Corporate Bonds]]
- [[concepts/business-cycles|Business Cycles]]
- [[concepts/multiple-testing|Multiple Testing]]
- [[concepts/approximate-factor-models|Approximate Factor Models]]

## Entities

- [[entities/alexander-dickerson|Alexander Dickerson]]
- [[entities/christian-julliard|Christian Julliard]]
- [[entities/philippe-mueller|Philippe Mueller]]

## Related Sources

- [[sources/dickerson-2023-bond-risk|Priced risk in corporate bonds]]
- [[sources/dickerson-2024-bond-pitfalls|Common Pitfalls in the Evaluation of Corporate Bond Strategies]]
- [[sources/kelly-2026-ipca|Instrumented Principal Component Analysis]]
- [[sources/avramov-2025-predictability-corporate-bond-returns-structured-approach|Predictability in Corporate Bond Returns: A Structured Approach]]
- [[sources/bali-2022-bond-ml|Predicting Corporate Bond Returns: Merton Meets Machine Learning]]
- [[sources/houweling-2017-factor-investing|Factor Investing in the Corporate Bond Market]]
- [[sources/dickerson-2026-corporate-bond-factor-replication-crisis|The Corporate Bond Factor Replication Crisis]]
<!-- AUTHORED REGION END -->