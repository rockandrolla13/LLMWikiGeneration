---
authors:
- Adesola Adegboye
- Michael Kampouridis
- Colin G. Johnson
content_hash: sha256:77c72c56f627e4958b7dc057e3462ed545315215c0ddacbc606138d7b04ce8cc
created: 2026-09-27 01:47:00+00:00
page_id: sources/adegboye-2017-regression-genetic-programming-estimating-trend-end
page_type: source
publication_venue: 2017 IEEE Symposium Series on Computational Intelligence (SSCI)
  Proceedings
related:
- concepts/intrinsic-time
- concepts/high-frequency-data
- concepts/backtesting
- concepts/feature-engineering
- concepts/directional-change
- entities/adesola-adegboye
- entities/michael-kampouridis
revision_id: 1
schema_version: 2
source_hash: sha256:e3d6558e83f2033bedd2d62d91d71ca62983c020a710e43ae7908171be33182a
source_path: markdown_output/adegboye-2017-regression-genetic-programming-estimating-trend-end.md
source_type: paper
tags:
- directional-change
- genetic-programming
- forex
- intrinsic-time
- trend-reversal
- symbolic-regression
- trading-strategy
- clock-intrinsic
- asset-fx
- harvest-relevant
title: Regression genetic programming for estimating trend end in foreign exchange
  market
updated: '2026-09-27T01:47:00Z'
uuid: afe12228-ddfa-5488-b70b-8b5f7e9c36cf
year: 2018
---

<!-- AUTHORED REGION START -->
# Regression genetic programming for estimating trend end in foreign exchange market

## Summary

The paper addresses trend-reversal estimation in the directional-change (DC) framework for Forex data: given the length of a directional-change (DC) event, how long will the following overshoot (OS) event last? Prior work used simple linear equations, such as OS lasting twice (2x) the DC length, to estimate this. The authors instead use tree-based genetic programming (GP) to search for general linear and non-linear symbolic equations mapping DC length to OS length, evolved separately for upward and downward DC datasets.

The GP is trained on 10-minute interval Forex data for 5 currency pairs (EUR/GBP, EUR/USD, EUR/JPY, GBP/CHF, GBP/USD) from June 2013 to May 2014, using June-July 2013 data for tuning, via the I/F-Race package, across 5 thresholds (0.010%, 0.013%, 0.015%, 0.018%, 0.020%), and August 2013 to May 2014 (250 out-of-sample datasets) for regression testing. GP fitness is root-mean-square error between actual and estimated OS length. The best GP equation is then substituted for the linear estimator inside an existing multi-threshold DC trading strategy (DC+GA), producing GP+DC+GA, which is compared against the original DC+GA, an O+GA variant using the simple 2xDC equation, the EDDIE technical-analysis GP trading system, and buy-and-hold.

The GP-derived equations had lower average RMSE than both prior linear equations across all 5 currency pairs (mean RMSE 5.71024 vs 6.16841 and 6.13421), a difference confirmed significant by a Friedman test with Hommel post-hoc correction (alpha = 0.05). In trading, GP+DC+GA achieved the highest mean daily return (0.01896%) of all strategies tested, beating DC+GA (0.01125%), O+GA (-0.0093%), EDDIE (-0.00076%) and buy-and-hold (0.01274%), and this trading-return ranking was also confirmed significant against DC+GA and EDDIE by a further Friedman/Hommel test.

What is new is applying symbolic-regression GP to the DC-OS length relationship itself, rather than to a trading-signal generator, letting the estimator take arbitrary linear or non-linear tree-based forms tailored per direction (upward and downward) instead of a single fixed constant ratio, and then showing this more accurate regression carries through into higher and more consistent trading returns than intrinsic-time and physical-time benchmarks.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Observations are directional-change (DC) events defined by a fixed percentage price threshold applied to the underlying 10-minute interval price series: price is monitored until it moves by at least the threshold from the last confirmed extreme, which confirms a DC event and starts a run consisting of the DC event followed by an overshoot (OS) event that ends when an opposite DC event is confirmed. The prediction horizon is the OS event: given the observed DC event length, a genetic-programming-evolved equation estimates how long the following OS event will last, and the sum of the DC length and estimated OS length gives the predicted trend-reversal point.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** EUR/GBP, EUR/USD, EUR/JPY, GBP/CHF, GBP/USD
- **Venue:** not stated
- **Period:** June 2013 to May 2014 (tuning: June-July 2013; testing: August 2013 to May 2014)
- **Granularity:** 10-minute interval

## Features and Measures

- **directional change (DC) event.** A price move exceeding a fixed percentage threshold from the last confirmed extreme, marking the start of a new trend leg on an event-based, intrinsic time scale.
- **overshoot (OS) event.** The continuation of price movement in the same direction after a DC event is confirmed, lasting until an opposite DC event occurs; its length is what the paper tries to estimate.
- **GP-evolved DC-OS length equation.** A tree-structured symbolic regression equation, evolved by genetic programming, that maps observed DC event length to an estimated OS event length, fitted separately for upward and downward DC events.
- **multi-threshold DC trading strategy (DC+GA).** A trading strategy that runs several DC thresholds in parallel, each recommending buy, hold or sell, and combines their recommendations by a genetic-algorithm-evolved weighted majority vote.

## Method

The core model is tree-based genetic programming (GP) for symbolic regression: GP evolves expression trees, built from arithmetic functions (addition, subtraction, multiplication, division, power) and unary functions (sine, cosine, log, exponential) over an input terminal (DC event length) and ephemeral random constants, that predict OS event length from DC event length. A separate equation is evolved for upward and downward DC datasets. Fitness is the root-mean-square error between the GP's estimated OS length and the actual OS length; trees with only-constant terminals, negative estimates, or NaN or infinite fitness are penalised, and tournament selection, breaking ties by shorter tree depth, is used. GP hyperparameters were tuned with the I/F-Race package on 50 DC datasets built from 5 currency pairs and 5 thresholds (0.010%, 0.013%, 0.015%, 0.018%, 0.020%) using June-July 2013 data.

The evolved GP equation was then evaluated for regression accuracy on 250 out-of-sample DC datasets (August 2013 to May 2014) via average RMSE, benchmarked against the two prior linear DC-OS equations, with a Friedman non-parametric test and Hommel post-hoc correction used to test whether rank differences are statistically significant (alpha = 0.05). The same GP equation was then substituted for the fixed linear estimator inside an existing multi-threshold DC trading strategy (DC+GA), producing GP+DC+GA. Trading performance is judged by mean daily return and percentage of positive trading days, comparing GP+DC+GA against DC+GA, an O+GA variant using the simple 2xDC linear equation, the EDDIE technical-analysis GP trading system, and a buy-and-hold benchmark, again using a Friedman/Hommel test for significance. All evolutionary strategies are run 50 times per dataset and results averaged; buy-and-hold is deterministic and run once per dataset.

## Results

- GP-estimated OS length had lower average RMSE than both prior linear DC-OS equations in every one of the 5 currency pairs tested (mean RMSE 5.71024 for GP vs 6.16841 for Equation 2 and 6.13421 for Equation 1).
- A Friedman test with Hommel post-hoc correction showed the GP equation's rank advantage over both linear equations was statistically significant at the alpha = 0.05 level.
- Embedding the GP equation in the DC+GA trading strategy (GP+DC+GA) gave the highest mean daily return of all strategies tested: 0.01896%, versus 0.01125% for DC+GA, -0.0093% for O+GA, -0.00076% for EDDIE, and 0.01274% for buy-and-hold.
- GP+DC+GA's trading-return ranking was statistically significant against DC+GA and EDDIE by a further Friedman/Hommel test, but not significantly different from O+GA.
- GP+DC+GA had positive trading days in 50% of the test months on average across currency pairs, versus 36% for DC+GA and 58% for O+GA.
- GP+DC+GA underperformed the other DC-based strategies specifically when GBP was the base currency, even though it outperformed overall.
- EDDIE (technical analysis) had negative returns in 4 out of the 5 currency pairs tested (EUR/JPY, EUR/USD, GBP/CHF, GBP/USD).

## Limitations

- Tested on only 5 currency pairs and about ten months of out-of-sample data (August 2013 to May 2014).
- Only 10-minute interval data was used; the authors note future work should test tick data and longer periods, such as 5 years.
- Reader note: performance varied by base currency, with GP+DC+GA underperforming when GBP was the base currency, suggesting the equations may not generalise across all currency pairs.
- Statistical significance between GP+DC+GA and O+GA trading returns was not established, only a higher rank.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/backtesting|backtesting]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/directional-change|Directional Change]]
- [[entities/adesola-adegboye|Adesola Adegboye]]
- [[entities/michael-kampouridis|Michael Kampouridis]]

## Citation

Adesola Adegboye, Michael Kampouridis, Colin G. Johnson (2018). Regression genetic programming for estimating trend end in foreign exchange market. 2017 IEEE Symposium Series on Computational Intelligence (SSCI) Proceedings.

DOI: 10.1109/ssci.2017.8280833

Text ingested: `markdown_output/adegboye-2017-regression-genetic-programming-estimating-trend-end.md`, converted from `raw/ofi-event-clock/adegboye-2017-regression-genetic-programming-estimating-trend-end.pdf`.

Coverage of this summary: Read the entire paper (under): abstract, introduction, DC background and literature review, methodology, experimental setup, results and analysis, summary, and conclusion.

Known problems with the input: The cover sheet prints the citation year as (2018) while the conference name is '2017 IEEE Symposium Series on Computational Intelligence (SSCI)'; year field uses the printed citation year (2018).
<!-- AUTHORED REGION END -->