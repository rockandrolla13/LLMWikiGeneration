---
authors:
- Parley Ruogu Yang
content_hash: sha256:4804bc4f528814ffa635ab2e41f28dfa5360356e6111b344f54d6730cfc2450d
created: 2026-09-27 01:47:00+00:00
page_id: sources/yang-2021-forecasting-high-frequency-financial-time-series
page_type: source
related:
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/limit-order-book
- concepts/high-frequency-data
- concepts/autocorrelation-time-series
- concepts/backtesting
revision_id: 1
schema_version: 2
source_hash: sha256:7ad71b541880ff9c0e594b7b7d3b144dab5fb3e76d163d9437f1f37b89fad1ad
source_path: markdown_output/yang-2021-forecasting-high-frequency-financial-time-series.md
source_type: paper
tags:
- adaptive-learning
- order-book-imbalance
- model-selection
- time-series-forecasting
- arima
- sharpe-ratio
- high-frequency-data
- clock-calendar
- asset-futures
- harvest-relevant
title: 'Forecasting high-frequency financial time series: an adaptive learning approach
  with the order book data'
updated: '2026-09-27T01:47:00Z'
uuid: 9331a5bd-a5ab-581b-87cd-a6d08d003737
year: 2020
---

<!-- AUTHORED REGION START -->
# Forecasting high-frequency financial time series: an adaptive learning approach with the order book data

## Summary

The paper asks how to forecast one-step-ahead prices of the CSI 300 Index Futures from order book data in a setting where the underlying time-series structure is time-varying and not always stationary, and whether letting the model specification itself adapt over time can do better than any single fixed specification. It also asks whether such an adaptive scheme can be reused for simple hypothesis tests about which model features tend to get selected.

The approach starts from best bid/ask price and quantity data for the CSI 300 Index Futures, aggregated into 5-minute wall-clock brackets within each trading session, from which the paper derives Order Imbalance (OIB, from quantities only) and Order Flow Imbalance (OFI, from signed changes in price and quantity), each summarised per bracket as a mean and as a normal-CDF 'p-score'. It explores stationarity with rolling Augmented Dickey-Fuller tests, then fits large grids of univariate ARIMAX(p,d,q) models and multivariate VARMA(p,q) models over different window sizes and explanatory-variable choices as 'fixed' models. It then proposes 'adaptive learning' model groups that, at each time step, select which fixed specification to use next by minimising a discounted loss over each candidate's recent forecast errors, with a further variant that penalises or rewards switching away from the previously selected window size and ARIMA order.

The main finding is that adaptively learnt models are broadly comparable to, but not clearly better than, the best fixed models when judged in aggregate by mean-squared error, mean absolute error or an annualised Sharpe ratio from a simple sign-of-forecast trading rule. Their advantage shows up specifically during unstable, non-stationary sub-periods, where they avoid some of the largest errors made by the best fixed model; large-window fixed models and models without explanatory variables dominate the adaptive model's choices most of the time, and multivariate VARMA models generally underperform univariate ones.

What is new is the forecast-error-driven adaptive model-selection scheme itself, including a time-varying penalisation/reward term that discourages or encourages switching between window sizes and ARIMA orders, together with simple Bayesian and frequentist hypothesis-testing procedures built directly on top of which functional forms the adaptive model selects over rolling periods.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Raw best bid/ask quotes and the latest traded price/volume are recorded within each second, with occasional gaps, and are aggregated into fixed 5-minute wall-clock brackets, 24 per trading session (two sessions per day), indexed by the bracket's end time. Within each bracket the volume-weighted mean price and the order book features are summarised, and the prediction target is the one-step-ahead (next 5-minute bracket) price change.

## Data

- **Asset class:** Futures
- **Instruments:** CSI 300 Index Futures
- **Venue:** China Financial Futures Exchange (CFFEX); intraday data supplied by CIFCO Guangzhou
- **Period:** 10 November 2017 to 17 April 2018, 105 trading days in total
- **Granularity:** Raw best bid/ask price and quantity plus latest traded price and volume, one or two entries expected per second, aggregated into 5-minute brackets (24 per trading session)

## Features and Measures

- **Order Imbalance (OIB).** A feature built purely from best bid and ask quantities, more positive when bid depth dominates and more negative when ask depth dominates.
- **Order Flow Imbalance (OFI).** A signed measure of order book events that nets changes in best bid and ask price and quantity into a single quantity representing a rise or fall in supply or demand.
- **p-score transform.** A normal-CDF transform of a bracket's standardised OIB or OFI value, which restricts the feature to a bounded range and stabilises its variance relative to the raw mean.
- **Adaptive learning loss (model groups 13 and 14).** A geometrically discounted, clipped loss computed over each candidate model's recent forecast errors, optionally combined with a penalty or reward for differing from the previously selected model's window size and ARIMA order, used to choose which fixed model to use at the next time step.

## Method

Univariate models are ARIMAX(p,d,q) specifications fit by maximum likelihood inside a rolling window of size w, with seven explanatory-variable groups (none, OIB mean, OFI mean, both means, OIB p-score, OFI p-score, both p-scores) and a grid of w in {12,24,48,96}, p and q in {0,1,2} and d in {1,2}, giving 504 fixed univariate models in total. Multivariate models stack the return with a subset of the four order-book features into a VARMA(p,q) system with p fixed at 1, q in {0,1} and w in {48,96}, giving 48 fixed multivariate models. Model performance is judged by mean squared error, mean absolute error, and an annualised Sharpe ratio computed from a simple rule that buys or sells according to the sign of the one-step-ahead forecast.

Adaptive learning model group 13 selects, at each time t, the fixed specification with the lowest discounted, outlier-clipped loss over its own recent forecast errors; model group 14 adds a penalty or reward term (in three variants) that discourages or encourages switching window size and ARIMA order relative to the model chosen at the previous step, with the strength of both the loss and the switching term set from time-varying quantiles of the cross-sectional error distribution. Finally, the paper applies both a simple Bayesian test (using a Bayes factor built from how often functions in a subset are selected) and a frequentist binomial test to check, over rolling 5-day periods, whether particular functional-form subsets (for example large window size, no explanatory variable, or univariate versus multivariate training) are selected more often than chance.

## Results

- The sample covers 105 trading days from 10 November 2017 to 17 April 2018, of which 99 trading days remain available for adaptive-learning testing after initial model warm-up.
- Among fixed univariate models, the lowest mean squared error, 20.97, came from an ARIMA(0,1,1) model with window 96 and no explanatory variable, but its Sharpe ratio was only 0.13.
- The best Sharpe ratio among fixed univariate models, 5.76, came from a window-48 model using the OFI p-score feature, with mean squared error 22.30.
- Multivariate (VARMA) models did not outperform univariate ones: the best vector-model mean squared error was 21.03 (window 96), while the vector model with the highest Sharpe ratio, 3.24, had a much larger mean squared error of 1603.69, reflecting instability from a smaller window relative to the number of parameters.
- The best-performing adaptive learning model reached a mean squared error of 22.05 and a Sharpe ratio of 1.54, similar to but not better than the top fixed models on either metric.
- In a 5-trading-day period of high volatility starting 8 February 2018, two adaptive learning models reduced mean absolute forecast error to 6.14 and 6.08 respectively, versus 6.30 for the best fixed model.
- Over 152 observations for which the rolling ADF test still rejected stationarity after two differences, an adaptive learning model achieved a lower mean squared error (24.73) than the best fixed model (26.28), though a marginally higher mean absolute error (3.39 versus 3.30).
- Bayesian and frequentist hypothesis tests found repeated, strong evidence that the adaptive models favour large window sizes and no explanatory variables and strongly prefer univariate over multivariate training, while a preference for the second difference order or small windows appeared only sporadically, mainly within single-day sub-periods.

## Limitations

- The study is based on a single instrument, the CSI 300 Index Futures, and a single sample period of 105 trading days, without a test of generalisation to other instruments or periods.
- The Sharpe-ratio-based trading evaluation ignores transaction costs, market impact and slippage.
- Multivariate VARMA models are restricted to small window sizes and low lag orders because of the high parameter count relative to available degrees of freedom, which the paper notes as a source of instability.
- Reader note: the paper's own date (11 September 2020) differs from the job's year hint of 2021; the year printed on this version of the document was used.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/backtesting|backtesting]]

## Citation

Parley Ruogu Yang (2020). Forecasting high-frequency financial time series: an adaptive learning approach with the order book data.

DOI: 10.20944/preprints202103.0269.v1

Text ingested: `markdown_output/yang-2021-forecasting-high-frequency-financial-time-series.md`, converted from `raw/ofi-event-clock/yang-2021-forecasting-high-frequency-financial-time-series.pdf`.

Coverage of this summary: Read the full markdown file, including all sections, tables, figures captions and appendices.

Known problems with the input: Many equations are rendered as omitted images in the markdown conversion, so the exact functional forms of the loss functions, penalty terms and forecast maps could not be verified beyond what is stated in the surrounding prose; The paper prints a date of 11 September 2020 with no separate journal or arXiv identifier stated; the job file's year hint was 2021, so the year printed on this document (2020) was used instead.
<!-- AUTHORED REGION END -->