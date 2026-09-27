---
authors:
- Bogdan Batrinca
content_hash: sha256:2c68f9c9145eaa56dff6f6deec5bbc73cd3c84c697d76cbacf485f34e3269d80
created: 2026-09-27 01:47:00+00:00
page_id: sources/batrinca-2016-analysis-key-drivers-trading-performance
page_type: source
publication_venue: PhD dissertation, University College London (Department of Computer
  Science)
related:
- concepts/feature-engineering
- concepts/backtesting
- concepts/overfitting-backtesting
revision_id: 1
schema_version: 2
source_hash: sha256:84de5649e9fc73ae52904509ea85101edf6c2b55b72cb4fac76475f292179685
source_path: markdown_output/batrinca-2016-analysis-key-drivers-trading-performance.md
source_type: paper
tags:
- trading-volume
- calendar-effects
- day-of-week-effect
- cross-market-holidays
- index-expiry
- ridge-regression
- volume-forecasting
- pan-european-equities
- clock-calendar
- asset-equity
- added-by-hand
title: Analysis of Key Drivers of Trading Performance
updated: '2026-09-27T01:47:00Z'
uuid: b9e7c417-010d-5d0c-be31-5a062c4881d3
year: 2016
---

<!-- AUTHORED REGION START -->
# Analysis of Key Drivers of Trading Performance

## Summary

The thesis asks what drives daily trading volume in pan-European equities, motivated by the practical problem of sizing algorithmic orders correctly: too large an order causes market impact, too small causes opportunity cost, and both depend on predicting volume well. It is built around four linked empirical studies using a pan-European daily data set of 2,353 stocks across 21 European countries (plus South Africa) from 1 January 2000 to 10 May 2015, complemented by a hand-built, high-precision non-trading and event calendar (bank holidays, stock index futures expiries, MSCI quarterly rebalances) since existing public calendars did not match actual exchange behaviour closely enough.

The first study fits stock-by-stock regression models to show that autoregressive and moving-average lagged volume, the previous day's intraday return and range, the overnight return (used as a proxy for opening-auction information), and day-of-week dummies each improve volume prediction, and that the price-volume relation is asymmetric (different in magnitude for positive versus negative returns) for a majority of stocks. The second and third studies isolate two recurring calendar phenomena as trading-volume effects rather than return effects: a 'cross-market holiday effect' (lower volume on a stock's own trading day when another major market is shut) and an 'expiry day effect' (higher volume around stock index futures expiries and MSCI quarterly index reviews), each validated first with pairwise randomisation tests and then modelled with ridge regression or stepwise linear regression, including multi-step-ahead variants for multi-day trade planning. The fourth study integrates these in-sample findings into an out-of-sample forecasting framework: seven statistical learning methods (OLS, stepwise regression, ridge regression, lasso regression, two k-nearest-neighbour variants, and support vector regression) are each fit stock-by-stock across six training-window types (five fixed moving windows from one month to two years, plus a growing window), together with separate cross-stock models for the sparse special-event dates, and their forecasts are compared by a dense-rank scheme per stock.

The main new contribution is combining these previously separate strands (endogenous volume/price dynamics, calendar anomalies studied by volume rather than by returns, and adaptive out-of-sample model selection) into one applied pipeline, culminating in a 'switching model' that selects among 42 event- and day-of-week-conditioned sub-models and clearly outperforms any single fixed method, and in stock-specific metamodels that instead pick a model based on each candidate's own recent forecasting track record.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

All analyses use fixed daily (end-of-day) observations: one row per stock per trading day, with the dependent variable being next trading day's logarithmic total volume predicted from information available up to and including the prior close. Special-event studies define a target date's relative volume as the log-ratio of that day's volume to the median volume of the preceding 20 trading days, and extend this to explicit multi-step-ahead horizons of 2 to 6 trading days; the final forecasting study additionally varies the training-window length (1, 3, 6, 12, 24 months, or an expanding/growing window) rather than the prediction horizon, which stays at one trading day ahead.

## Data

- **Asset class:** Equities
- **Instruments:** 2,353 pan-European common stocks (plus their volume on the BATS, CHI-X and Turquoise multilateral trading facilities, consolidated into a single volume series); later chapters restrict to constituents of specific indices used for the futures-expiry study (7 index futures) and the MSCI rebalance study (MSCI International Pan Euro Price Index)
- **Venue:** Primary European stock exchanges plus MTFs, sourced via Thomson Reuters Eikon
- **Period:** 1 January 2000 to 10 May 2015 (over 15 years); a pre-crisis (2000-2007) and post-crisis (2008-2015) split is used throughout to test for structural breaks around the 2007-08 financial crisis
- **Granularity:** daily OHLC prices and end-of-day consolidated trading volume (primary exchange plus MTF volume); no intraday or tick-level data is used

## Features and Measures

- **volume lag / volume window.** Autoregressive lagged daily log-volume terms (volume lag) and moving-average smoothed lagged volume terms (volume window), with the lag/window order chosen per stock by sequentially comparing nested models under 10-fold cross-validation.
- **intraday return and intraday range.** Previous trading day's close-to-open log-return and high-minus-low log-range, used as volatility/price-change proxies for predicting next-day volume, optionally split into separate positive and negative magnitude features (an 'asymmetric' representation).
- **overnight return.** The log-ratio between today's opening price and the prior close, corrected for the number of intervening non-trading nights, used as a proxy for the (unobserved) opening-auction volume and as the most recent available price information before the target day.
- **day-of-week indicators.** Dummy variables for each of the five trading weekdays, tested both alone (a traditional calendar-effect model) and jointly with the volume/price features, to see whether volume itself (not just returns) differs by weekday.
- **cross-market holiday indicators.** Indicator variables marking that a given stock's exchange is open while one or more other tracked countries' exchanges are shut for a bank holiday, used to explain reduced relative trading volume on such days.
- **futures-expiry and MSCI-rebalance indicators.** Indicator variables (with optional offsets of up to 5 trading days before/after the event) marking stock index futures expiry dates and MSCI quarterly index review dates, used to explain elevated relative trading volume around these recurring events.
- **relative volume.** The log-ratio of a stock's volume on a target date to the median of its volume over the prior 20 trading days, used as the dependent variable in the sparse special-event (holiday/expiry/rebalance) regression models so that observations from stocks of different sizes can be pooled.
- **switching model / stock-specific metamodel.** A model-selection layer that either picks, for a given date, the sub-model historically best-suited to that date's temporal circumstance (day-of-week, holiday, expiry, rebalance) or picks, at each forecast step, whichever of the seven learning methods/window types had the best recent (1- or 3-month) out-of-sample rank for that stock.

## Method

The in-sample studies (chapters 3-5) fit, independently for each stock, a sequence of nested multiple linear regression models built up from an intercept and autoregressive/moving-average volume terms, then adding price features (intraday return/range, overnight return, symmetric or asymmetric), then day-of-week or calendar-event indicators, using stepwise (forward or backward) feature selection under 10-fold cross-validation with average mean squared error (MSE) as the selection criterion. Sparse calendar-event effects (cross-market holidays, futures expiries, MSCI rebalances) are first tested for statistical existence with pairwise permutation (randomisation) tests using 1,000 relabelling repetitions and an empirical p-value, then modelled with ridge regression (for the cross-market holiday study, chosen for robustness to collinearity among many correlated country/holiday dummies) or ordinary least squares plus stepwise regression (for the expiry/rebalance study), including multi-step-ahead versions of each model for horizons of 2 to 6 trading days.

The final out-of-sample study (chapter 6) fits seven supervised learning methods per stock - OLS, stepwise regression, ridge regression, lasso regression, k-nearest neighbours (arithmetic-mean and inverse-distance-weighted variants), and support vector regression - each independently trained under six training-window regimes (moving windows of 1, 3, 6, 12 and 24 months, and an expanding/growing window), plus separate cross-stock models trained on pooled, volume-normalised observations for the sparse event dates. Performance is judged not by raw MSE (which differs enormously in scale across stocks) but by a dense per-stock ranking of methods based on their MSE, averaged across the stock universe; this ranking is then used to build a switching model that selects the historically best sub-model for each of 42 temporal circumstances (day-of-week crossed with event type), and separately to build stock-specific metamodels that pick, at each step, whichever method/window combination had the best rank over the preceding 1 or 3 months of that stock's own forecasts.

## Results

- Volatility features (the prior day's intraday return and range) improve the autoregressive volume model in 86.95% of the 2,353 stocks studied.
- Price-volume asymmetry is common: 56.53% of stocks show intraday-return asymmetry and 54.07% show overnight-return asymmetry in the best (historical dynamic) model, combining to an overall asymmetry in 73.59% of stocks.
- Adding day-of-week features to the historical dynamic (volume-and-price) model beats the traditional 'raw' day-of-week-only model in 99.87% of stocks; Monday is the most consistently selected day-of-week feature, improving the model for over 75% of stocks with a negative coefficient in 90.89% of the models where it is selected, indicating persistently lower Monday volume.
- A cross-market holiday effect is confirmed by randomisation tests: median relative volume on cross-market holidays is -8.882% in log-ratio terms, corresponding to an 8.499% reduction in linear volume versus the 20-day benchmark; a separate randomisation test attributes lower Monday volumes specifically to Monday bank holidays rather than to a generic weekend effect.
- Stock index futures expiries and MSCI quarterly rebalances are both followed by elevated relative volume (confirmed by randomisation tests against Friday-only and end-of-month-only control dates respectively), but the MSCI rebalance months are only weakly different from adjacent non-rebalance months (two-tailed test rejects the null at p = 0.005 while the one-sided test for a larger effect does not, p = 0.999), so rebalances alone do not account for the broader end-of-month volume pattern.
- In the out-of-sample study, ridge regression trained on a 2-year moving window achieves the best average dense rank (6.96) of any single fixed method/window combination across all target dates; day-of-week features remain relevant out-of-sample, with Monday retained in about 42% of feature-selected models and Friday in about 25%.
- A switching model that selects among 42 event/day-of-week-specific sub-models achieves a markedly better average rank (5.64) than the best single fixed model, ridge regression on a 2-year window (7.73), and is the single best-performing model for 26.32% of the 2,181 evaluated stocks versus 1.65% for the next-best fixed model.
- Stock-specific metamodels that pick a model based on each stock's own recent (1- or 3-month) out-of-sample performance underperform the in-sample switching model: the 1-month metamodel has an average rank of 23.42 and the 3-month metamodel 14.93, both worse than several of the individually fixed models.

## Limitations

- Only end-of-day consolidated trading volume is available (opening-auction volume could not be licensed from the data vendor), so the overnight return is used only as an indirect proxy for the most recent pre-open information rather than a direct measure.
- Regression models in the in-sample studies (chapters 3-5) are fit independently per stock and are not intended to generalise as a single cross-sectional model; the authors state effect size and coefficient magnitude are not the focus of those studies.
- The stock-specific out-of-sample study (chapter 6) had a cumulative single-core runtime of 33 years across the full grid of methods, windows and stocks, which the thesis itself notes as a practical constraint on re-running the analysis for new step sizes.
- Reader note: the entire thesis models daily total trading volume for pan-European (and South African) equities using only daily OHLC and volume data; it contains no bonds, credit instruments, or intraday/tick-level clock, so any relevance to fixed-income microstructure feature design is by methodological analogy only, not by asset class or data granularity.

## Related

- [[concepts/feature-engineering|feature engineering]]
- [[concepts/backtesting|backtesting]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]

## Citation

Bogdan Batrinca (2016). Analysis of Key Drivers of Trading Performance. PhD dissertation, University College London (Department of Computer Science).

Text ingested: `markdown_output/batrinca-2016-analysis-key-drivers-trading-performance.md`, converted from `raw/ofi-event-clock/batrinca-2016-analysis-key-drivers-trading-performance.pdf`.

Coverage of this summary: Read the abstract, full introduction and thesis-structure sections, and then the data-set, methodology, results and discussion sections of all four empirical chapters (Examining Drivers of Trading Volume; European Trading Volumes on Cross-Market Holidays; Expiry Day Effects on European Trading Volumes; Developing a Volume Forecasting Model) plus the concluding chapter. The general background/literature-review chapter (chapter 2) and the bibliography were skimmed rather than read in full, since they are a survey of prior work rather than this thesis's own data, method or results.

Known problems with the input: This is a long PhD thesis (roughly 210 pages of body text); per the long-document instructions, the broad literature-review chapter and some background subsections within each empirical chapter were not read in full, only the data/method/results/discussion portions of each study; Almost all mathematical equations are rendered as omitted picture placeholders in the markdown conversion rather than as text, so equations are described qualitatively rather than reproduced; The job file's year_hint (2016) matches the year printed on the thesis title page, so no year discrepancy applies here.
<!-- AUTHORED REGION END -->