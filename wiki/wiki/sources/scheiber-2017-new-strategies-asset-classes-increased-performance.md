---
authors:
- Matthias Scheiber
content_hash: sha256:e8726db2eff2e426fb6681643414436432a67a2973d601a55f5b353bf437a05d
created: 2026-09-27 01:47:00+00:00
page_id: sources/scheiber-2017-new-strategies-asset-classes-increased-performance
page_type: source
publication_venue: Birkbeck College, University of London
related:
- concepts/stochastic-time-change
- concepts/high-frequency-data
- concepts/order-flow
- concepts/feature-engineering
- concepts/cross-sectional-momentum
revision_id: 1
schema_version: 2
source_hash: sha256:fa31947dd6b2b41a42326e49c6bdd70810aa4cd1816eb50489fd5b39af6cc07f
source_path: markdown_output/scheiber-2017-new-strategies-asset-classes-increased-performance.md
source_type: paper
tags:
- commodity-futures
- copper
- kalman-filter
- agent-based-model
- transaction-time
- temperature-factor
- theory-of-storage
- equity-microstructure
- clock-time-change
- asset-multi
- harvest-relevant
title: New Strategies and Asset Classes for Increased Performance
updated: '2026-09-27T01:47:00Z'
uuid: 0982ce67-b6c6-5b8b-8279-70414a35bd96
year: 2017
---

<!-- AUTHORED REGION START -->
# New Strategies and Asset Classes for Increased Performance

## Summary

The thesis asks whether trading frequency itself, not just volatility, carries pricing information for stocks; whether a fundamental long-term copper price estimated from a three-factor model can help explain how fundamental and technical commodity traders interact; and whether the classical Theory of Storage relationship between the copper forward curve and inventories still holds once informal Chinese bonded-warehouse inventory used for financing deals is accounted for.

It builds on Geman and Ane's transaction-time subordination and Derman's temperature-of-a-stock idea, extending temperature into a time-varying, portfolio-level statistic computed on minute data for the S&P 500 Information Technology universe, and forms sextile-sorted long/short portfolios tested with an arbitrage-pricing-style regression. For copper, it fits a three-factor Kalman-filter model to multi-maturity futures data to obtain a fundamental value, feeds that value into a heterogeneous agent-based model of mean-reversion fundamentalists and trend-following chartists calibrated by the Generalized Method of Moments, and separately regresses the Shanghai copper forward spread on SHFE inventories and a hand-collected bonded-warehouse series.

High-temperature (high trading-frequency) stocks earned a positive beta-adjusted excess return over low-temperature stocks in a volatile sample window, and this heat premium survived controlling for market beta in a two-factor regression, although ex-post it was not simply compensation for higher risk. In the copper model, fundamentalist positioning strengthened when the spot price diverged from the model's fair value while chartists lost relative influence; the SHFE-inventory relationship to the forward spread stayed positive and significant, but adding bonded-warehouse inventory weakened that relationship after 2014.

What is new is extending temperature from a single-stock, static idea into a time-varying, cross-sectional, multi-stock statistic; embedding an estimated fundamental copper value directly inside an agent-based model rather than treating fundamentals as exogenous; and constructing an original bonded-warehouse dataset to test whether shadow Chinese commodity-financing inventory distorts the classical Theory of Storage.

## Clock and Sampling

**Time change: a stochastic clock used as a modelling device.**

See [[concepts/stochastic-time-change|Stochastic Time Change]].

Chapter 2 recasts calendar time as a stock-specific 'transaction time' or business time by rescaling volatility with the square root of a stock's own trading frequency (its 'temperature'), following Geman and Ane's stochastic subordination. Temperature is computed on one-minute return data for the S&P 500 IT universe using a rolling 60-minute window, over a three-month sample from December 2014 to March 2015 covering a turbulent market period; the heat-premium prediction horizon is the full sample window (long the highest-temperature sextile, short the lowest), not a fixed forward return horizon.

## Data

- **Asset class:** Several asset classes
- **Instruments:** S&P 500 Information Technology index constituents (65 stocks, e.g. Apple, Oracle); LME and Shanghai Futures Exchange copper futures across nine maturities; Chinese bonded copper warehouse volumes and Shanghai copper inventories.
- **Venue:** Not stated for equities (Bloomberg-sourced minute data); LME and Shanghai Futures Exchange for copper futures and inventories.
- **Period:** Equity study: December 2014 to March 2015 (minute data). Copper three-factor Kalman filter: July 1997 to May 2013 (monthly). Copper inventory/forward-spread study: 2009-2015, drawing on a bonded-warehouse survey published since 2008; the SHFE-vs-bonded-warehouse forward-spread regression uses 93 observations.
- **Granularity:** Minute data for equities; monthly data for copper futures curves, inventories and bonded-warehouse volumes.

## Features and Measures

- **Temperature of a stock.** A time-varying stock statistic equal to its rolling volatility multiplied by the square root of its trading frequency (number of trades per unit calendar time), computed over a 60-minute rolling window.
- **Temperature product, ratio and minimum.** Cross-stock statistics built from the pairwise product, ratio and minimum of individual stock temperatures against the S&P 500 index, meant to capture liquidity concentration, divergence and a systematic (portfolio-level) liquidity floor.
- **Heat premium / temperature risk factor.** A beta-adjusted long/short portfolio, long the highest-temperature sextile and short the lowest-temperature sextile of the S&P 500 IT universe, used as a factor in an arbitrage-pricing-style regression.
- **Three-factor copper price model.** Copper spot price decomposed into a stochastic long-term equilibrium level (geometric Brownian motion), a mean-reverting short-term deviation, and a scarcity term defined as the inverse of global copper inventory, estimated by Kalman filter on futures prices.
- **Fundamentalist/chartist excess demand.** In a heterogeneous agent-based model, fundamentalists' demand is driven by the discounted gap between the model's fundamental copper value and the spot price, while chartists' demand follows the recent price trend; transition probabilities between the groups are estimated by the Generalized Method of Moments.
- **Adjusted forward spread.** The Shanghai copper futures price minus the spot price, normalized by the spot price, regressed against SHFE inventories and a hand-collected bonded-warehouse inventory series to test the Theory of Storage.

## Method

Chapter 2 uses a multi-variate regression of temperature on stock and market returns, an augmented Dickey-Fuller unit-root test on the temperature series, pairwise correlation analysis across S&P 500 IT stocks, and a two-factor asset-pricing regression (market beta plus a temperature risk factor) run separately for each of 65 stocks and averaged, comparing time-based and frequency-adjusted returns.

Chapter 3 estimates the three-factor stochastic copper-price model with a Kalman filter on nine-maturity copper futures data, then feeds the resulting fundamental value into a simulated heterogeneous agent-based model with 500 agents (a minimum of 4 per group), whose behavioural parameters are estimated by the Generalized Method of Moments from monthly data.

Chapter 4 regresses the normalized Shanghai copper forward spread on SHFE inventories and the bonded-warehouse series (93 observations), and examines 1-year rolling Pearson and Spearman correlations between the forward spread and both SHFE-only and aggregate (SHFE plus bonded-warehouse) inventory measures.

## Results

- The high-temperature sextile of S&P 500 IT stocks outperformed the low-temperature sextile by +19.2% cumulatively over the sample period.
- A two-factor regression with market beta and a temperature risk factor across 65 S&P 500 IT stocks gave an R-squared of 0.37, close to the 0.38 obtained with market beta alone, with the temperature factor an additional statistically distinguishable driver.
- Ex-post, high-temperature stocks showed lower beta and lower volatility than low-temperature stocks once returns were beta-adjusted, so the heat premium was not simply compensation for higher market-linked risk.
- The Kalman-filtered three-factor copper model found the stochastic volatility component reverting faster than the spot-price component, with a positive, significant correlation between the two.
- In the calibrated agent-based model, fundamentalist trader numbers grew when copper's spot price diverged from the model's fundamental value, and chartists lost relative share, consistent with a stabilising mean-reversion channel.
- The Shanghai copper forward spread stayed positively related to SHFE inventories (Theory of Storage) across 2009-2015, but adding a hand-collected bonded-warehouse inventory series weakened that relationship, especially after the 2014 Qingdao warehousing scandal.
- China was estimated to account for 46% of global copper demand, with mine production projected to rise 9% in 2016, framing the demand backdrop for the inventory-financing analysis.

## Limitations

- The temperature/heat-premium result is shown over a single, deliberately volatile sample window (December 2014-March 2015) and one sector (S&P 500 IT), so generality across regimes and sectors is untested.
- The heat premium is demonstrated on time-based, beta-adjusted returns; the author notes most institutional investors cannot trade on a fully frequency-adjusted basis, so the practically realizable premium may differ.
- Reader note: the agent-based model's reported calibration standard errors are extremely small (e.g. 1.07E-09%), which is not explained in the text and may reflect a numerical or reporting artefact rather than genuine estimation precision.
- The bonded-warehouse series is built from a monthly survey of only 10-15 warehouses, traders and industry participants, so it is itself an approximation of true shadow inventory.
- Reader note: the thesis's abstract states the equity analysis focuses on a period in 'autumn 2015', but the Chapter 2 body text specifies the actual sample as December 2014 to March 2015; this extraction follows the body text and flags the inconsistency rather than silently resolving it.

## Related

- [[concepts/stochastic-time-change|Stochastic Time Change]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-flow|order flow]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/cross-sectional-momentum|cross sectional momentum]]

## Citation

Matthias Scheiber (2017). New Strategies and Asset Classes for Increased Performance. Birkbeck College, University of London.

DOI: 10.18743/pub.00040258

Text ingested: `markdown_output/scheiber-2017-new-strategies-asset-classes-increased-performance.md`, converted from `raw/ofi-event-clock/scheiber-2017-new-strategies-asset-classes-increased-performance.pdf`.

Coverage of this summary: Read the front matter, abstract, table of contents, and Chapter 1 introduction in full; Chapter 2 (temperature of a stock) in full across all seven sections; Chapter 3 (copper agent-based model) Sections 1 and 3-6 in full, with Section 2 (Related Work / literature review) skimmed only by heading; Chapter 4 Sections 1, 3 (data and results) and 4 (conclusion) in full, while Section 2's detailed sub-sections on interest-rate differentials and forward-curve shapes were not read in detail; and Chapter 5's overall conclusions in full.

Known problems with the input: Many equations throughout the thesis are rendered as omitted images in the converted markdown (e.g. the temperature, Kalman-filter, and agent-based-model equations), so exact functional forms could not be verified beyond the surrounding prose; The abstract states the equity 'heat premium' analysis focuses on a 3-month period in autumn 2015, while Chapter 2's body text gives the actual sample as 8 December 2014 to 8 March 2015; this is an inconsistency in the source document itself, not resolved by this extraction; Chapter 4 Section 2 (interest-rate differentials and detailed forward-curve mechanics, roughly pages 84-99) was not read in full for this extraction; the data and conclusion sections were used instead to characterise that chapter's findings.
<!-- AUTHORED REGION END -->