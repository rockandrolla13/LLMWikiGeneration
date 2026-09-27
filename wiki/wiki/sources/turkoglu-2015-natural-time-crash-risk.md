---
authors:
- Ata Türkoğlu
content_hash: sha256:5dc1e3cf58f526fcfa341f983e0b744ff1d63b7dbf0bb1ae78ed7ac492106ddb
created: 2026-09-27 01:47:00+00:00
page_id: sources/turkoglu-2015-natural-time-crash-risk
page_type: source
publication_venue: University of Essex (PhD thesis, Centre for Computational Finance
  and Economic Agents)
related:
- concepts/stochastic-time-change
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/order-imbalance
- concepts/liquidity-risk
- concepts/trade-classification
- concepts/stylized-facts
- concepts/high-frequency-trading
- concepts/informed-trading
- concepts/vpin
revision_id: 1
schema_version: 2
source_hash: sha256:a2c555f91bfc443a5f1574546f9be8003e6c9dd7986ade1afa48ca83d954f815
source_path: markdown_output/turkoglu-2015-natural-time-crash-risk.md
source_type: paper
tags:
- natural-time
- subordination
- flash-crash-prediction
- market-heat
- early-warning-system
- order-book-imbalance
- high-frequency-returns
- clock-time-change
- asset-multi
- harvest-core
title: Natural Time and Crash Risk
updated: '2026-09-27T01:47:00Z'
uuid: 3aabc212-4cc5-5893-a978-394be44e1676
year: 2015
---

<!-- AUTHORED REGION START -->
# Natural Time and Crash Risk

## Summary

The thesis asks why high-frequency financial returns deviate from the normal distribution assumed by much of finance theory, and whether the same market-microstructure information that explains this non-normality can also be used to predict financial crashes at different time horizons: intraday flash crashes and multi-month currency devaluations.

Chapter 2 introduces 'natural time', a subordination procedure that samples London Stock Exchange order-book and trade data in transaction (tick) time rather than calendar time, and rescales the resulting returns using order-book-derived variables (volume, duration, and trade-initiator or volume imbalance) chosen via maximum likelihood so the subordinated series approaches normality; results are checked with Kolmogorov-Smirnov and Jarque-Bera tests and benchmarked against a GARCH(1,1) model.

Chapter 3 tests whether the same order-book variables can forecast 'flash crashes'. It proposes 'Market Heat' (MH), a nonlinear combination of order imbalance, bid-side depth and order-book update duration, and compares it via linear discriminant analysis against a linear model and a VPIN-style toxicity measure, evaluated in-sample and out-of-sample on E-mini S&P 500 futures around the 6 May 2010 Flash Crash and on several London Stock Exchange stocks, using trades that are classified into buyer- or seller-initiated using exchange-provided tags rather than an inferred classification rule.

Chapter 4 extends the same crash-prediction logic to a macroeconomic setting, forecasting 1-month-ahead currency crashes and returns for 9 G10 countries using signaling, logit, probit and panel (fixed- and random-effects) models that combine macroeconomic fundamentals with market variables (VIX and TED-Spread). Across the three chapters the main findings are that transaction-time subordination with order-book variables recovers normality more often than GARCH; that Market Heat consistently outperforms a linear model and VPIN at predicting flash crashes in both markets tested; and that market variables, rather than most macroeconomic fundamentals, are the consistently significant predictors of currency crashes, with panel-model point forecasts showing AUCs above 0.60 that the author interprets as evidence of a profitable trading signal. What is new across the thesis is the combination of tick-time subordination with order-book variables to recover normality, the Market Heat metric itself, the use of exchange-provided trade-initiator tags to avoid bulk trade-classification error throughout, and applying market-liquidity variables (rather than only macroeconomic fundamentals) to currency crash prediction in developed rather than emerging markets.

## Clock and Sampling

**Time change: a stochastic clock used as a modelling device.**

See [[concepts/stochastic-time-change|Stochastic Time Change]].

The thesis samples data three different ways across its three empirical chapters. Chapter 2's core method ('natural time') samples London Stock Exchange order-book and trade data in transaction (tick) time, mainly at a 100-tick sampling frequency, and then applies a stochastic time change (subordination) that rescales each tick-time return using order-book variables (volume, duration, and order-imbalance measures) so the resulting series approaches a normal distribution; this subordination is compared against a calendar-time GARCH(1,1) benchmark. Chapter 3 reverts to fixed calendar-time sampling, aggregating order-book and trade data into 5-minute bars to predict crashes over a short forward horizon. Chapter 4 uses monthly calendar-time sampling of macroeconomic and market variables to predict currency crashes 1 month ahead.

## Data

- **Asset class:** Several asset classes
- **Instruments:** Chapters 2-3 (LSE): the 10 largest FTSE 100 firms by market capitalisation - HSBC Holdings, Vodafone Group, BP, GlaxoSmithKline, British American Tobacco, Royal Dutch Shell, BG Group, Rio Tinto, Diageo and SAB Miller (Chapter 3's LSE analysis uses a subset: HSBC, BG Group, British Petroleum and British American Tobacco). Chapter 3 (CME): the E-mini S&P 500 futures contract. Chapter 4: spot exchange rates against the US dollar plus macroeconomic and market variables for 9 developed (G10) markets - United Kingdom, European Union (Eurozone), Switzerland, Sweden, Norway, Canada, Australia, Japan and New Zealand.
- **Venue:** London Stock Exchange SETS market (Chapters 2-3); Chicago Mercantile Exchange (Chapter 3); G10 foreign exchange and macroeconomic data (Chapter 4)
- **Period:** Chapters 2-3 LSE stock data: July 2007 to June 2008, split into 4 three-month sub-periods (P1-P4). Chapter 3 CME E-mini S&P 500 futures: in-sample 3 to 14 May 2010, out-of-sample continuing to 30 May 2010. Chapter 4 FX/macro data: January 2000 to December 2012, with January 2000 to June 2006 used as the in-sample (boom) period and July 2006 to December 2012 as the out-of-sample (crisis) period.
- **Granularity:** Chapters 2-3: Level 2 order-book depth and individual trade records, resampled to a 100-tick frequency (Chapter 2) or aggregated into 5-minute bars (Chapter 3). Chapter 4: monthly macroeconomic and market data, with lower-frequency series linearly interpolated to a monthly frequency.

## Features and Measures

- **Natural time subordination variables.** Order-book and trade-derived variables (cumulated volume, duration between sampling points, and the difference between buy- and sell-initiated trade counts or volume) used to rescale tick-time returns so that the resulting series approaches a normal distribution.
- **Market Heat (MH).** A nonlinear crash-warning metric that combines volume imbalance between bid- and ask-initiated trades, standing bid-side order-book depth (as a liquidity gauge), and the average order-book update duration to signal short-horizon flash-crash risk.
- **Rebuilt VPIN benchmark.** A volume-bucketed order-flow toxicity measure, based on the published VPIN framework, but reconstructed here using exchange-provided trade-initiator tags to classify trades instead of the usual bulk (probabilistic) trade-classification procedure.
- **Market variables (VIX and TED-Spread) as crash predictors.** Global market-based indicators of investor sentiment and banking-system stress used, alongside macroeconomic fundamentals, to predict currency crashes and FX returns for developed markets.

## Method

Chapter 2 treats calendar-time asset prices as a Brownian motion subordinated to a stochastic 'intrinsic time' process, and searches for the subordinator function that best recovers normality of tick-time returns. Four functional forms are tested: a linear combination of the subordination variables, an autoregressive version that adds the lagged squared return, an asymmetric version that estimates separate coefficients for positive and negative returns, and a combined autoregressive-asymmetric version. Coefficients are estimated by maximum likelihood assuming the subordinated returns are normal, using a global multi-start optimisation with $10^5$ starting points to avoid local optima. The resulting distributions are tested for normality with the Kolmogorov-Smirnov and Jarque-Bera tests, and compared against a GARCH(1,1) benchmark estimated on the same tick-time returns.

Chapter 3 builds 'Market Heat' (MH) from volume imbalance, bid-side depth and average order-book update duration, and links it algebraically to the microstructure-based probability-of-informed-trading framework. MH is compared against a simple linear combination of the same order-book and trade variables and a VPIN-style toxicity measure, rebuilt using exchange-provided trade-initiator tags rather than the usual bulk trade classification. All three measures are converted into a binary crash/no-crash signal via linear discriminant analysis (LDA) and evaluated in-sample and out-of-sample, across several crash thresholds, on E-mini S&P 500 futures data around the 6 May 2010 Flash Crash and on 5-minute LSE stock returns, using classification accuracy, precision and recall.

Chapter 4 forecasts 1-month-ahead currency crashes (defined as a 2% FX loss) and FX returns using macroeconomic variables (interest-rate premium, inflation, unemployment, current account/GDP, reserves/GDP, M2/GDP and GDP growth) and market variables (VIX, TED-Spread, and the local stock index return), all lagged by one period. Three binary approaches are compared: a KLR-style signaling/indicator model using country-specific quantile thresholds and a trailing window, and logit and probit models estimated both country-by-country and pooled across countries; all are evaluated via classification accuracy, precision, recall and ROC/AUC on out-of-sample data. Fixed-effects and random-effects panel models are also estimated to produce point forecasts of FX returns, evaluated with a return-weighted ('adjusted') ROC curve whose area under the curve indicates whether a simple buy-and-hold strategy on the point forecasts would be profitable.

## Results

- In Chapter 2, using a 100-tick sampling frequency on the 10 largest FTSE 100 stocks, subordination produced normally distributed returns in nine of forty stock-period combinations, versus five for the GARCH(1,1) benchmark, and the GARCH model's exogenous order-book terms were insignificant in every period.
- In Chapter 3, at a -1.00% crash threshold, in-sample classification accuracy for E-mini S&P 500 futures was 98.2% for Market Heat versus 90.0% for the linear model and 48.8% for VPIN; out-of-sample accuracy at the same threshold was 100.0% for Market Heat versus 97.7% for the linear model and 80.6% for VPIN.
- Market Heat flagged only about 2% of trades as a crash, far fewer than VPIN, which the thesis describes as classifying close to half of all trades as crashes.
- A version of Market Heat built with average trade duration instead of average order-book update duration performed markedly worse, indicating that order-book update duration carries most of the predictive information.
- In Chapter 4, requiring 3 or more indicator signals before flagging a currency crash pushed classification accuracy above 60% for several of the 9 G10 countries studied, though country-by-country logit and probit models produced no crisis predictions at all for Switzerland, Canada, Japan and New Zealand.
- Pooled logit and probit models for currency crashes, using only the market variables VIX and TED-Spread, achieved out-of-sample AUC values of 0.6053 and 0.6045 respectively, both above the 0.5 level of an uninformed classifier.
- The random-effects and fixed-effects panel models of 1-month-ahead FX returns produced adjusted-ROC AUC values of 0.6090 and 0.6084 respectively, both above 0.60, which the thesis interprets as evidence that a simple buy-and-hold strategy on the point forecasts would have been profitable.

## Limitations

- The author notes that the Chapter 2 sample (2007-2008) was an unusually turbulent period for the stocks studied, making it inherently harder to recover normally distributed returns than in the calmer periods used by earlier subordination studies.
- The author notes that Market Heat has low precision despite high recall, producing many false alarms even though it rarely misses a crash, and that its Chapter 3 evaluation on futures centres on a single dramatic event, the 6 May 2010 Flash Crash.
- The author notes that no direct asset-side (asset-bubble) indicator was included in the Chapter 4 currency-crash models, describing this as 'the missing link' left for future work, and that country-by-country logit/probit models could not produce any crisis predictions for Switzerland, Canada, Japan and New Zealand.
- The author notes that the profitability implied by the Chapter 4 panel models' adjusted AUC values was not backtested as an actual trading strategy accounting for execution costs.
- Reader note: Chapter 2's own analysis found that standing order-book imbalance variables were insignificant and were dropped, so the final natural-time subordinators rely on trade-level variables (volume, duration, initiator/volume imbalance) rather than the full depth of the order book.

## Related

- [[concepts/stochastic-time-change|Stochastic Time Change]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/liquidity-risk|liquidity risk]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/vpin|VPIN]]

## Citation

Ata Türkoğlu (2015). Natural Time and Crash Risk. University of Essex (PhD thesis, Centre for Computational Finance and Economic Agents).

Text ingested: `markdown_output/turkoglu-2015-natural-time-crash-risk.md`, converted from `raw/ofi-event-clock/turkoglu-2015-natural-time-crash-risk.pdf`.

Coverage of this summary: Read the abstract, Chapter 1 (introduction and structure), and for each of the three empirical chapters (2, 3, 4) the introduction, methodology, data, results and discussion sections, plus the full Chapter 5 conclusion (summary, contributions, future work). Skipped the three chapter-level literature-review sections and all appendices except a brief check of Appendix B's stock list.

Known problems with the input: This is a large PhD thesis (roughly 150 pages of body text plus extensive appendices); per the long-document reading rule, literature-review subsections and Appendices A and C-P (large per-stock/per-country result tables, order-book reconstruction detail, and regression tables) were not read in full and are not reflected here; Nearly all equations in the converted markdown were rendered as omitted-picture placeholders or garbled OCR text (e.g. variable names replaced with placeholder glyphs), so exact mathematical definitions of the subordination functions, VPIN, MH, LDA and the panel/binary models could not be verified beyond the surrounding prose description; The thesis states Chapter 2 was separately published as a journal article in Quantitative Finance, but that published version was not consulted; only the thesis text itself was used for this extraction.
<!-- AUTHORED REGION END -->