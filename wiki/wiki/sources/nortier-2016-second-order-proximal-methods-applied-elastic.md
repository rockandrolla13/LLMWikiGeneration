---
authors:
- Bertrand Nortier
content_hash: sha256:1f3547a0b4e50d2b90b1ee02fb772855e50c6e183becbc8cc47fb5dbdfede718
created: 2026-09-27 01:47:00+00:00
page_id: sources/nortier-2016-second-order-proximal-methods-applied-elastic
page_type: source
publication_venue: University of Oxford (Master of Science by Research thesis)
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/high-frequency-data
- concepts/order-flow-prediction
- concepts/feature-engineering
- concepts/backtesting
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:444736f621bd7eace934ebdf5de01b45617d8c3949ec7980735eb04d11373933
source_path: markdown_output/nortier-2016-second-order-proximal-methods-applied-elastic.md
source_type: paper
tags:
- limit-order-book
- ordinal-probit
- elastic-net
- proximal-methods
- variable-selection
- vglm
- high-frequency-trading
- thesis
- clock-event
- asset-futures
- harvest-relevant
title: Second Order Proximal Methods Applied to Elastic Net Penalised Vector Generalised
  Linear Models
updated: '2026-09-27T01:47:00Z'
uuid: d16f9b9c-18fe-524f-a4a4-97af14a52fcf
year: 2016
---

<!-- AUTHORED REGION START -->
# Second Order Proximal Methods Applied to Elastic Net Penalised Vector Generalised Linear Models

## Summary

The thesis asks how to fit the maximum penalised likelihood of vector generalised linear models (VGLMs), a broad family covering many univariate and multivariate regression models, when the penalty is an elastic net that is not everywhere differentiable. Because the elastic net mixes a smooth ridge term with a non-smooth lasso term, the usual Fisher scoring algorithm used to estimate VGLMs cannot be applied directly, so the thesis turns to proximal optimisation methods to handle the non-smooth part.

Its approach treats Fisher scoring as a Newton-type method and adapts existing proximal Newton theory to it, defining a proximal Fisher scoring algorithm that substitutes the Fisher information matrix for the Hessian at each step and shows the resulting sub-problem is equivalent to a penalised iteratively reweighted least squares update, solved in practice by coordinate descent on the lasso part. The author gives a geometric interpretation of the proximal operator, a backtracking line search condition, and summarises available convergence theory for the general proximal Newton case while noting that convergence specifically for proximal Fisher scoring has not been established.

The method is illustrated twice. First, an elastic-net penalised ordinal probit, adapted from a model originally proposed for transaction price changes, is fit to tick-level limit order book data for FTSE100 futures to select which lagged order-book covariates, out of 410 candidates, help predict the direction of the next mid-price move; a trading-style gain/loss function is used both to tune the regularisation path and to score the resulting strategy out of sample. Second, the same proximal Fisher scoring machinery is embedded in an EM algorithm to fit a regularised bivariate Poisson regression to health-care count data, selecting which covariates drive two correlated counts and their shared covariance.

What is new is the proximal Fisher scoring algorithm itself as a general second-order proximal method for penalised VGLMs, together with its concrete use in two different penalised models: a regularised ordinal probit for high-frequency order-book price prediction and an EM-based regularised bivariate Poisson regression, alongside a convergence-speed comparison against several competing estimation methods on a small worked example.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

For the financial application, the limit order book is recorded every time one of its ten bid or ten ask levels changes, so observations are irregularly spaced order-book update events rather than fixed time intervals. Each observation's covariates are the changes and depths at the ten best bid and ask levels and the time between the previous ten book updates, all measured over the last ten book changes, and the model predicts the sign of the very next mid-price change (up, unchanged or down).

## Data

- **Asset class:** Futures
- **Instruments:** FTSE100 index futures limit order book (10 bid levels and 10 ask levels)
- **Venue:** not stated
- **Period:** 27/10/2008 to 31/10/2008 (4.5 days)
- **Granularity:** asynchronous, event-driven limit order book updates; in-sample dataset of 5,000 points drawn from the first 10,000 observations, out-of-sample from observation 10,001 to 70,000

## Features and Measures

- **lagged best bid/ask changes.** The change in each of the ten best bid and ten best ask prices over the previous ten limit order book updates, used as covariates for the ordinal probit regression.
- **book depth covariates.** The number of contracts resting at each of the ten best bid and ten best ask price levels over the previous ten updates, used as covariates.
- **interchange duration.** The time elapsed between each of the previous ten changes to the limit order book, used as a covariate for predicting the next mid-price move.
- **elastic net penalised ordinal probit.** A three-level ordinal regression (down, no change, up) on mid-price changes, penalised with an elastic net to perform variable selection among many correlated lagged order-book covariates.

## Method

The thesis's core methodological contribution recasts Fisher scoring, the standard estimator for vector generalised linear models, as a proximal Newton-type method so that non-differentiable elastic-net penalties can be optimised. It defines a proximal Fisher operator that replaces the Hessian with the Fisher information matrix, shows this step is equivalent to a penalised iteratively reweighted least squares update, and solves the lasso part with coordinate descent; a backtracking line search condition is also given.

On a small simulated ordinal-regression example (5 covariates, 30 samples), proximal Fisher scoring is compared for convergence speed against a smooth L1 approximation, a quadratic-programming reformulation, and the ISTA/FISTA proximal gradient methods.

The regularised ordinal probit is then applied to predict the direction of the next mid-price change in FTSE100 futures limit order book data using 410 lagged order-book covariates. The elastic-net regularisation path and mixing parameter are chosen using a trading-style gain/loss function evaluated by five-fold cross-validation on an in-sample set, and the chosen model is then evaluated by its cumulative gain/loss on a much larger out-of-sample set. A second application fits a regularised bivariate Poisson regression to health-care count data by embedding proximal Fisher scoring in an EM algorithm, selecting covariates for two counts and their shared covariance via a grid search over regularisation parameters scored with the Bayesian Information Criterion.

## Results

- In a small simulated example, the smooth L1 approximation converged in the fewest iterations, followed by proximal Fisher scoring (solved via coordinate descent or quadratic programming), then FISTA and ISTA.
- Proximal Fisher scoring usually converged without a backtracking line search, while the smooth approximation needed one and was sensitive to its tuning parameter.
- Of the 410 lagged order-book covariates, only four were retained by the elastic net: the change in the first best bid level and in the first, third and fourth best ask levels, each lagged ten periods.
- The in-sample cross-validated gain from the strategy was similar across elastic net mixing values of 0, 0.25, 0.5, 0.75 and 1, so a value of 0.5 was chosen without further justification.
- Applying the selected model to 60,000 out-of-sample data points produced a cumulative gain/loss path that was not the highest among the lambda values tried, but appeared less variable once each path was rescaled by its own standard deviation.
- In the health-care application, four of five candidate covariates were selected for one of the three Poisson components, and the BIC surface used to choose the regularisation grid was found to be non-convex.

## Limitations

- The author notes the ordinal-probit LOB application is a single example on one dataset and one gain/loss criterion, so the criterion's validity elsewhere is untested.
- The thesis states that convergence of proximal Fisher scoring itself, as opposed to the general proximal Newton method, has not been proven, since it does not satisfy the classical criterion used for quasi-Newton methods.
- The health-care Poisson application used a random subsample of 500 records and only 5 of the available covariates, purely to keep computation manageable.
- Reader note: the LOB dataset spans only about 4.5 days of a single futures contract, so results may not generalise across instruments or regimes.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/backtesting|backtesting]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Bertrand Nortier (2016). Second Order Proximal Methods Applied to Elastic Net Penalised Vector Generalised Linear Models. University of Oxford (Master of Science by Research thesis).

DOI: 10.5287/ora-m8wkpvbdn

Text ingested: `markdown_output/nortier-2016-second-order-proximal-methods-applied-elastic.md`, converted from `raw/ofi-event-clock/nortier-2016-second-order-proximal-methods-applied-elastic.pdf`.

Coverage of this summary: Read the full thesis: the abstract; Part I in full (introduction, literature review, VGLM framework, proximal Fisher scoring derivation, convergence discussion, and its appendices); Part II in full (introduction, literature review, ordinal probit model and estimation-method comparison, the HFFD application's data, strategy, regression settings, results, discussion, and its appendices); and Part III in full (bivariate Poisson EM proximal Fisher scoring, the health-care data application, conclusion, and its appendices).

Known problems with the input: Mathematical equations were rendered as images in the PDF-to-markdown conversion and appear only as picture placeholders, so exact formulas are described from surrounding prose rather than verified symbol-by-symbol; No exchange or trading venue is named for the FTSE100 futures limit order book dataset beyond the data provider (Oxford-Man Institute of Quantitative Finance).
<!-- AUTHORED REGION END -->