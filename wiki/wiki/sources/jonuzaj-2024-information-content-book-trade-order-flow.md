---
authors:
- Mariol Jonuzaj
- Alessio Sancetta
- Yuri Taranenko
content_hash: sha256:10afa289ad5d02604c57a4c16145298cd18a3054937ff19bedbe1e1cf35805c7
created: 2026-09-27 01:47:00+00:00
page_id: sources/jonuzaj-2024-information-content-book-trade-order-flow
page_type: source
related:
- concepts/volume-clock
- concepts/order-flow
- concepts/order-flow-imbalance
- concepts/order-flow-prediction
- concepts/limit-order-book
- concepts/price-impact
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/market-microstructure-noise
- entities/alessio-sancetta
revision_id: 1
schema_version: 2
source_hash: sha256:8f5d87b3ab3d7df41d4681875567e58cf57593f242561665767e199bc37a999c
source_path: markdown_output/jonuzaj-2024-information-content-book-trade-order-flow.md
source_type: paper
tags:
- order-flow
- limit-order-book
- volume-time
- high-frequency-trading
- machine-learning
- price-predictability
- market-microstructure
- nasdaq
- clock-volume
- asset-equity
- harvest-core
title: Information Content of Book and Trade Order Flow at Different Trading Volume
  Time Scales
updated: '2026-09-27T01:47:00Z'
uuid: 7f8e5669-6b3f-5880-807c-84a8105c1e3e
year: 2024
---

<!-- AUTHORED REGION START -->
# Information Content of Book and Trade Order Flow at Different Trading Volume Time Scales

## Summary

The paper asks how the information content of NASDAQ limit order book activity, split into book order flow (arriving orders including cancellations) and trade order flow (executed orders), affects the predictability of the direction of mid-price moves once observations are aggregated away from ultra-high frequency into coarser, volume-based time intervals, and how that predictability translates into economic value and reacts to execution speed.

The authors build volume-time bars for large-cap, mid-cap and lower-activity S&P 500 stocks traded on NASDAQ, using LOBSTER-reconstructed Level 3 order book and trade data over a multi-year sample. Within each bar they construct order-flow-based features drawn from the top book levels, trade flow, and mid-price change, and train four supervised classifiers - Linear Discriminant Analysis, a Ridge classifier, a Random Forest, and a Deep Neural Network, plus an average of their outputs - with a rolling multi-month training window, to predict the sign of the following bar's average mid-price change. They repeat this exercise at three volume-time granularities and evaluate classification accuracy, an economic-return measure based on virtual mid-price execution, permutation-based feature importance, and the decay of the price response after simulated microsecond execution delays. A separate panel regression relates the resulting daily returns to stock- and market-level explanatory variables and to a cross-exchange activity index.

Trade order flow, not book order flow, is the feature that keeps predicting mid-price direction once data are aggregated in volume time; book order flow's contemporaneous explanatory power, which prior ultra-high-frequency work documents, does not carry over to genuine out-of-sample, one-bar-ahead prediction. The resulting predictive edge in prices dissipates within roughly the first few milliseconds of a decision, and the more complex Random Forest and Deep Neural Network models do not clearly outperform the simpler Ridge and LDA classifiers. Returns from acting on the classifier signals are larger at finer volume-time granularity, are more profitable for higher-beta and higher-market-impact stocks, persist across several trading days, and have declined over the sample period.

Relative to prior high-frequency order-book prediction studies that work in tick or clock time, the contribution is to show, at aggregated volume-time scales, that the persistent source of predictive information shifts from the book to trades, to quantify the economic value of that information and its sensitivity to execution speed, and to link day-to-day variation in that value to market conditions such as volatility regime, market impact, and macro or FOMC announcement days; it also shows that a stock's relative order-message activity on NASDAQ versus other US venues is not monotonically related to how informative its NASDAQ order flow is.

## Clock and Sampling

**Volume clock: one observation per unit of volume traded.**

See [[concepts/volume-clock|Volume Clock]].

Observations are sampled at volume-time bars defined separately for each stock: a bar boundary is set whenever cumulative traded volume since the previous boundary reaches a fixed fraction of that stock's average daily volume, using fractions 0.001, 0.005 and 0.01 (i.e. 0.1%, 0.5% and 1% of expected average daily volume). Features are aggregated within each bar and the model predicts the sign of the average mid price over the following bar relative to the current bar's mid price, so the prediction horizon is exactly one volume-time bar ahead. A separate analysis replaces the bar-end mid price with the mid price after fixed clock-time delays of 50, 500, 1000 and 10000 microseconds to gauge how fast the predicted move is realized.

## Data

- **Asset class:** Equities
- **Instruments:** 35 large-cap US stocks that are constituents of the S&P 500, grouped into high, mid and low trading-activity tiers
- **Venue:** NASDAQ (LOBSTER-reconstructed NASDAQ TotalView-ITCH Level 3 data); a supplementary activity index also uses order-message counts from NYSE, NYSE ARCA, and two CBOE/BATS books (BZX and BYX)
- **Period:** 1 March 2019 to 28 February 2023
- **Granularity:** Level 3 order book messages (submissions, cancellations, deletions, and visible or hidden executions) for the first ten book levels, with exchange timestamps at nanosecond resolution, aggregated into volume-time bars as described above

## Features and Measures

- **Book order flow (BF).** For each of the first ten bid and ask book levels, a signed quantity built from the change in posted size or the size at a new price after a book update, aggregated within a volume-time bar into a bounded order-flow measure.
- **Trade flow (TF).** The sum within a volume-time bar of signed trade sizes, where a trade is signed positive if executed at or above the prevailing mid price and negative if executed below it.
- **Mid price change (dMid).** The change in the mid price, the average of the best bid and ask, between consecutive book updates, aggregated within a volume-time bar as a momentum feature.

## Method

Four classifiers are trained: LDA with no penalty, a Ridge classifier (one-versus-all, ridge parameter chosen by generalised cross-validation), a Random Forest (500 trees, maximum depth 15), and a Deep Neural Network (two hidden layers of 64 nodes each, softmax output over three classes). Each predicts a three-class target (down, flat, up) built from the sign of the change between the next bar's average mid price and the current bar's mid price; predictions from the four models are also averaged into a fifth 'Avg' method. Estimation uses a rolling window of several months: at the end of each month the recent past trains the models, which then generate out-of-sample predictions for the following month, repeated across the sample and separately for each of the three volume-time granularities.

Classification performance is judged by accuracy, precision and recall, excluding the flat class from precision and recall because it occurs rarely. Economic value is judged by an average-return-per-bar measure that treats the classifier's output as a buy or sell decision executed virtually at the bar's mid price, expressed in basis points and scaled by the day's opening mid price; a related daily-return measure sums this over all bars in a day. Feature importance is measured by the drop in this return measure when a feature or group of features is randomly permuted across observations. The value of execution speed is measured by comparing the return if execution were delayed by 50, 500, 1000 or 10000 microseconds against immediate execution.

A panel regression relates the daily average return per bar, by stock, model and aggregation level, to model dummies, stock-level covariates (market beta, a square-root-law-style market impact index, a high-volume-day indicator, return and overnight-return jump indicators), market-level covariates (a high-VIX indicator, FOMC and macro-announcement dummies, Friday and summer dummies, and year dummies), and lags of the dependent variable to absorb autocorrelation, with stock fixed effects; the same specification is also estimated stock by stock.

## Results

- Classification accuracy for the sign of the aggregated mid-price change reaches as high as 73% for some stocks and aggregation levels, with predictability falling as the volume-time bars get coarser.
- Average economic returns from trading on the classifier signal are mostly of the order of 1 basis point per bar and decrease as the volume-time scale is aggregated from 0.1% up to 1% of average daily volume.
- Removing trade flow from the feature set reduces the average return per bar by as much as 100%, 78% and 55% (medians) at the 0.1%, 0.5% and 1% volume-time scales respectively, while removing book order flow has only a modest effect, showing trade flow is the dominant source of predictive value once data are aggregated.
- About 75% of the eventual price move in the predicted direction occurs within the first 500 microseconds after the decision point, and close to 100% occurs within the first 10 milliseconds, indicating the predictive edge is capturable mainly by very low-latency participants.
- During the March 2020 Covid sell-off, gross average daily returns from the trading rule reached as high as 40%, coinciding with unusually high traded volume.
- In the explanatory panel regression at the 0.1% aggregation, higher stock market beta (coefficient 0.099) and higher market-impact sensitivity (coefficient 0.249) are both associated with significantly higher average returns from the predictions.
- The daily economic value of predictions is persistent, with autoregressive coefficients on its own lags all positive and significant, and the estimated half-life of adjustment is about 1.2 trading days at the 0.1% aggregation.
- A stock's NASDAQ order-message activity relative to other major US venues shows no monotonic relationship with how informative its NASDAQ order flow is, and the predictive value of order flow has declined over the sample years, consistent with rising algorithmic competition.

## Limitations

- The paper only observes NASDAQ order flow; NASDAQ is often not the most heavily traded venue for a given stock (the authors note Apple trades far more heavily on NYSE ARCA), and no consolidated Level 3 feed across venues was available.
- The sample is restricted to one exchange's order flow for 35 S&P 500 stocks over about four years, so results may not generalise to other venues, smaller-cap names, or other asset classes.
- Trade direction is inferred from a simplifying sign rule around the mid price rather than a full trade-classification algorithm, though the authors report this affects few trades and does not change their conclusions.
- Models were deliberately left untuned to avoid data snooping, so the reported comparison across model complexity may understate what a fully tuned Random Forest or Deep Neural Network could achieve.
- Reader note: the headline economic-return figures, including the 40% Covid-period daily return, are gross of transaction costs, so they overstate net tradeable profitability.

## Related

- [[concepts/volume-clock|Volume Clock]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/price-impact|price impact]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[entities/alessio-sancetta|Alessio Sancetta]]

## Citation

Mariol Jonuzaj, Alessio Sancetta, Yuri Taranenko (2024). Information Content of Book and Trade Order Flow at Different Trading Volume Time Scales.

DOI: 10.2139/ssrn.5036269

Text ingested: `markdown_output/jonuzaj-2024-information-content-book-trade-order-flow.md`, converted from `raw/ofi-event-clock/jonuzaj-2024-information-content-book-trade-order-flow.pdf`.

Coverage of this summary: Read the full paper front to back: abstract, introduction and motivation, the limit order book description, the methodology sections on aggregation, order flow, targets, models and performance measures, the empirical results and relative-activity sections, the conclusion, and the tables and footnotes.

Known problems with the input: Markdown conversion splits many decimals with underscores/italics (e.g. '0 _._ 001') and replaces mathematical display equations with '==> picture... omitted <==' placeholders, so the exact algebraic formulas for order flow, the target variable, and the regression equations (1)-(10) could not be transcribed and are described here only qualitatively; The panel regression table (Table 8) is reformatted by the conversion into a hard-to-parse single blob mixing rows and columns across the three aggregation levels; only a small number of individual coefficients that were unambiguous were used above.
<!-- AUTHORED REGION END -->