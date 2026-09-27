---
authors:
- Doron Avramov
- Gergana Jostova
- Alexander Philipov
content_hash: sha256:2decb3d873d4ec788dde10d57fcb126d5f6bbbb2cf494d65a60060808e832405
created: 2026-09-27 01:47:00+00:00
page_id: sources/avramov-2025-predictability-corporate-bond-returns-structured-approach
page_type: source
related:
- concepts/corporate-bonds
- concepts/bond-momentum
- concepts/cross-sectional-momentum
- concepts/autocorrelation-time-series
- concepts/amihud-illiquidity
- concepts/alpha-signal
- concepts/feature-engineering
- concepts/overfitting-backtesting
- entities/doron-avramov
- entities/gergana-jostova
- entities/alexander-philipov
revision_id: 1
schema_version: 2
source_hash: sha256:55c19712c3201021a905e1cdeb0a208d9d36df87c7d1c41fbd0ffd0ac7b1e776
source_path: markdown_output/avramov-2025-predictability-corporate-bond-returns-structured-approach.md
source_type: paper
tags:
- corporate-bonds
- cross-predictability
- autocovariance
- portfolio-optimization
- trace-data
- ice-data
- credit-risk
- factor-momentum
- clock-calendar
- asset-bonds-rates
- added-by-hand
title: 'Predictability in Corporate Bond Returns: A Structured Approach'
updated: '2026-09-27T01:47:00Z'
uuid: 02616a1a-6eab-5458-9ac1-b7ecc66a329d
year: 2025
---

<!-- AUTHORED REGION START -->
# Predictability in Corporate Bond Returns: A Structured Approach

## Summary

The paper asks whether a corporate bond's future return can be forecast not just from its own lagged return but from the lagged returns of other bonds, an intertemporal cross-predictability question that has been little explored for corporate bonds relative to equities. It develops a zero-cost trading strategy whose weight matrix is chosen to maximize expected profit subject to a Frobenius-norm constraint on the underlying position matrix, yielding a closed-form solution that nests standard cross-sectional momentum as a special case and modifies the Principal Portfolios framework of Kelly, Malamud and Pedersen (2023). A restricted equal-mean variant removes reliance on expected-return estimates and behaves like an intertemporal analogue of the global minimum-variance portfolio.

The framework is tested on two independent U.S. corporate bond datasets: ICE BofA index constituents and FINRA TRACE trade-based data. Bonds are sorted into 82 sets of portfolios based on bond-level characteristics (yield, duration, option-adjusted spread, liquidity) and equity-linked firm characteristics (size, value, momentum, profitability), and each characteristic-based strategy is evaluated out of sample, decomposed into self-predictability and cross-predictability components, and combined into mean-variance tangency portfolios; strategy returns are also regressed on a bond market factor together with recession and low-sentiment dummies.

Credit-risk and trading-friction characteristics deliver the strongest predictability: ICE strategies generate out-of-sample returns exceeding 100 basis points per month with Sharpe ratios above 1.2, and TRACE strategies produce 70 to 90 basis points per month with Sharpe ratios around 1.0. Even the equal-mean specification that excludes expected-return inputs remains highly profitable, and cross-bond predictability alone often rivals or exceeds the contribution of a bond's own autocovariance. Tangency portfolios built from the 82 characteristic strategies reach Sharpe ratios between 1.2 and 1.4, roughly three times the passive bond market, and profitability tends to rise during recessions but weaken during low-sentiment periods.

The contribution is a tractable, closed-form decomposition of expected strategy profitability into a static component driven by dispersion in expected returns and a dynamic component driven by the auto- and cross-autocovariance structure, offering a new empirical foundation for corporate bond factor construction that complements characteristic-based frameworks such as IPCA and deep-factor models.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Observations are monthly bond and portfolio returns. The auto- and cross-covariance matrix is estimated over a rolling window of past monthly returns and used to forecast returns K months ahead, with K = 1 treated as a short-term horizon and K = 6 as an intermediate-term horizon; strategy weights are recomputed each month from that period's realized returns.

## Data

- **Asset class:** Bonds and rates
- **Instruments:** US corporate bonds, both investment-grade and high-yield, using ICE BofA index constituents and FINRA TRACE trade reports
- **Venue:** ICE (Intercontinental Exchange) BofA corporate bond indexes and TRACE (FINRA's Trade Reporting and Compliance Engine), the latter via WRDS
- **Period:** ICE: December 1996 to June 2024; TRACE: July 2002 to June 2023
- **Granularity:** Monthly bond-level and portfolio returns, estimated over rolling windows

## Features and Measures

- **Weight-generating matrix (Psi).** An N-by-N matrix, built from a norm-constrained matrix L and a self-financing projection matrix, that maps each bond's own and other bonds' lagged returns into a zero-cost portfolio position.
- **Auto- and cross-autocovariance matrix (Omega).** The covariance between a bond's future return and the lagged returns of itself and all other bonds; decomposed into a diagonal (self-predictability) and off-diagonal (cross-predictability) part.
- **Equal-mean / GMVP-analog strategy.** A restricted version of the strategy that assumes identical expected returns across bonds so that positions depend only on autocovariances and cross-autocovariances, avoiding noisy mean-return estimation.
- **Tangency portfolio across characteristics.** A second-stage mean-variance optimized portfolio built by combining the 82 characteristic-sorted zero-cost strategies to measure the maximum achievable Sharpe ratio from signal combination.

## Method

The model treats each bond's future return as forecastable from an N-dimensional vector of all bonds' lagged returns through a weight-generating matrix built from a norm-constrained matrix and a projection matrix that enforces a zero-cost, self-financing position. The investor chooses the position matrix to maximize expected strategy profit subject to a Frobenius-norm constraint, which acts as a ridge-type regularizer equivalent to a zero-mean Gaussian prior; the constraint is calibrated so gross long and short exposure sums to two. The resulting closed-form solution decomposes expected profitability into a term driven by cross-sectional dispersion in expected returns and a term driven by the auto- and cross-autocovariance matrix, and nests the Lo-MacKinlay and Lewellen cross-sectional momentum strategy as a special case.

Performance is judged out of sample across the 82 characteristic-sorted portfolio strategies using six variants of the weight matrix (unrestricted, equal-mean, diagonal-only, off-diagonal-only, and upper- or lower-triangle-only) to isolate self- versus cross-predictability and test for asymmetries. Strategy-level Sharpe ratios are benchmarked against equally weighted and value-weighted bond market portfolios, and multi-strategy tangency portfolios are formed via mean-variance optimization across the 82 return series. Robustness to market risk, recessions and investor sentiment is assessed with regressions of strategy returns on the bond market factor together with recession and low-sentiment intercept dummies.

## Results

- ICE credit-risk-sorted strategies generate out-of-sample returns exceeding 100 basis points per month with Sharpe ratios above 1.2
- TRACE-based strategies produce monthly returns of 70 to 90 basis points with Sharpe ratios around 1.0
- The equal-mean specification, which excludes expected-return inputs, still delivers over 80 basis points per month in ICE and over 70 in TRACE
- Bond-signal tangency portfolios reach Sharpe ratios between 1.2 and 1.4, roughly three times the passive bond market
- Credit-risk strategies in the high-yield segment generate monthly alphas above 1.2%
- For ICE yield-sorted portfolios, a cross-autocovariance-only strategy generates 107 basis points per month, of which 57 basis points come from self-predictability and 50 from cross-predictability
- For TRACE, the analogous total strategy return is 96 basis points per month, with 89 from cross-predictability and 7 from self-predictability
- Stock-based tangency portfolios reach Sharpe ratios up to 0.9 in TRACE but perform more weakly in ICE

## Limitations

- Interest-rate-risk characteristics such as duration and convexity show little or even negative predictive power.
- Alpha magnitudes become less statistically significant once recession and sentiment controls are added, even though point estimates remain large.
- Reader note: relies on rolling-window estimates of a high-dimensional covariance matrix, so estimation noise in the autocovariance matrix could still affect out-of-sample results despite the norm constraint.
- Reader note: restricted to US dollar corporate bonds (ICE and TRACE); no evidence is given for other bond markets or currencies.

## Related

- [[concepts/corporate-bonds|corporate bonds]]
- [[concepts/bond-momentum|bond momentum]]
- [[concepts/cross-sectional-momentum|cross sectional momentum]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/amihud-illiquidity|amihud illiquidity]]
- [[concepts/alpha-signal|alpha signal]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
- [[entities/doron-avramov|Doron Avramov]]
- [[entities/gergana-jostova|Gergana Jostova]]
- [[entities/alexander-philipov|Alexander Philipov]]

## Citation

Doron Avramov, Gergana Jostova, Alexander Philipov (2025). Predictability in Corporate Bond Returns: A Structured Approach.

DOI: 10.2139/ssrn.5311686

Text ingested: `markdown_output/avramov-2025-predictability-corporate-bond-returns-structured-approach.md`, converted from `raw/ofi-event-clock/avramov-2025-predictability-corporate-bond-returns-structured-approach.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, methodology (sections 2.1-2.3), data description (ICE and TRACE, section 3), full results section 4, conclusion, references, and the appendix table of characteristic definitions.

Known problems with the input: Equations are rendered as omitted images in the markdown (labelled '==> picture... intentionally omitted <=='); only the surrounding prose describing them was used, not the equations themselves.
<!-- AUTHORED REGION END -->