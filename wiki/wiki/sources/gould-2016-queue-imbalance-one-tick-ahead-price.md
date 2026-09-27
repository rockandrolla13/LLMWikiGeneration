---
authors:
- Martin D. Gould
- Julius Bonart
content_hash: sha256:d45d58178b3b7bc5643711f711128eaa60ed86656732b0c84e80cdbef6e5f2e1
created: 2026-09-27 01:47:00+00:00
page_id: sources/gould-2016-queue-imbalance-one-tick-ahead-price
page_type: source
related:
- concepts/event-clock
- concepts/order-imbalance
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/high-frequency-trading
revision_id: 1
schema_version: 2
source_hash: sha256:3fcaedb58d4ee9c2d0075da0721fda20a20849fa539d7bebdef5915c089b0f28
source_path: markdown_output/gould-2016-queue-imbalance-one-tick-ahead-price.md
source_type: paper
tags:
- queue-imbalance
- limit-order-book
- logistic-regression
- price-prediction
- nasdaq
- market-microstructure
- tick-size
- local-regression
- clock-event
- asset-equity
- harvest-core
title: Queue Imbalance as a One-Tick-Ahead Price Predictor in a Limit Order Book
updated: '2026-09-27T01:47:00Z'
uuid: d77e1451-a2fd-5aae-b650-5153e6c6a2e6
year: 2015
---

<!-- AUTHORED REGION START -->
# Queue Imbalance as a One-Tick-Ahead Price Predictor in a Limit Order Book

## Summary

The paper asks whether the imbalance between the best-bid and best-ask queue sizes in a limit order book carries real, statistically significant information about which way the very next mid-price move will go, tested both as a yes/no direction call and as a probability forecast.

Using LOBSTER order-by-order Nasdaq data for 10 liquid stocks (5 large-tick, 5 small-tick) across the whole of 2014, the authors build, for each stock, a sample of mid-price-change events, record whether each move was up or down, and sample the queue imbalance at a random time before each event. They fit a logistic regression of the up/down outcome on the imbalance using an in-sample training split, check statistical significance with Wald and likelihood-ratio tests, and score out-of-sample performance on a held-out test split against a coin-flip null model, using the area under the ROC curve for direction calls and the mean squared residual for probability forecasts. They repeat the exercise with a semi-parametric local logistic regression that is not forced into a sigmoid shape.

Imbalance turns out to be a highly significant predictor for every stock in the sample. For large-tick stocks the improvement over the null model is considerable for both direction and probability forecasts; for small-tick stocks the improvement is real but smaller, especially for the probability forecasts. The local logistic fits track the plain logistic fits almost exactly, with only occasional small gains, at much greater computational cost.

What is new is less the logistic-regression method itself than the direct, careful out-of-sample test across a deliberately chosen tick-size spectrum, and the explanation offered for the large-tick/small-tick gap: for large-tick stocks the spread sits at the minimum one-tick size, so a mid-price move can only happen by a queue depleting to zero, which is exactly what queue imbalance measures, whereas for small-tick stocks a new order can also step inside a wider spread, a second channel that imbalance does not capture.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are indexed by successive mid-price-change events: for each stock-day, every time the mid-price moves is collected into an ordered set, and the outcome recorded is simply whether that move was up or down. The queue imbalance is measured once per inter-event interval, at a time drawn uniformly at random between the previous and the next mid-price-change event; a robustness check instead draws the sampling time uniformly from the discrete order-book update times inside the same interval, with qualitatively unchanged results. The prediction horizon is exactly one mid-price-change event ahead.

## Data

- **Asset class:** Equities
- **Instruments:** 10 liquid Nasdaq-listed stocks: 5 large-tick (Microsoft MSFT, Intel INTC, Micron Technology MU, Cisco Systems CSCO, Oracle ORCL) and 5 small-tick (Google GOOG, Amazon AMZN, Tesla Motors TSLA, Priceline PCLN, Netflix NFLX)
- **Venue:** Nasdaq
- **Period:** entire year of 2014 (252 trading days)
- **Granularity:** event-by-event LOBSTER order-book data, restricted to bid price, ask price and best-quote queue lengths; trading hours 10:00 to 15:30 each day; 100 mid-price-change events randomly subsampled per stock per day for a total of 25200 points per stock, split 80%/20% (20160/5040) into training and testing sets

## Features and Measures

- **queue imbalance.** The normalized difference between the size of the best-bid queue and the size of the best-ask queue, ranging from -1 (all volume at the ask) to +1 (all volume at the bid).
- **mid-price direction indicator.** A binary variable equal to 1 if a given mid-price-change event was an increase and 0 if it was a decrease, ignoring the size of the move.
- **logistic regression of direction on imbalance.** A two-parameter logistic curve fit between queue imbalance and the up/down direction indicator, used both to classify direction and to output a probability of an upward move.
- **local logistic regression.** A semi-parametric version of the same fit that estimates a separate logistic regression at each value of imbalance, weighting nearby observations with a tricube kernel, to avoid imposing one global sigmoid shape.

## Method

For each of the 10 stocks, the authors build a sample of mid-price-change events from LOBSTER's event-by-event Nasdaq order-book records for 2014, restrict attention to trading hours of 10:00 to 15:30, draw a fixed random subsample of 100 mid-price-change events per stock per day (25200 events per stock in total), and split each stock's sample 80%/20% into training and test sets.

For each event they record the up/down direction indicator and sample the queue imbalance at a random time in the preceding inter-event interval, then fit a logistic regression of direction on imbalance by maximum likelihood on the training set; statistical significance is assessed with Wald tests on the two coefficients and a likelihood-ratio test against an intercept-only model.

Out-of-sample performance is judged against a null model that always predicts a 50% chance of an upward move: direction-classification quality is measured by the area under the ROC curve, and probability-forecast quality by the mean squared residual between the predicted probability and the realized outcome. The same procedure is repeated with a local, tricube-weighted logistic regression whose bandwidth (0.65) is chosen by 5-fold cross-validation, as a semi-parametric check on the parametric logistic fit.

## Results

- For all 10 stocks, the coefficient linking queue imbalance to the mid-price direction indicator is significant at the 99% level, with likelihood-ratio test statistics for the full model ranging from 483.24 (GOOG) to 6205.00 (CSCO).
- The fitted imbalance coefficient is larger for large-tick stocks (2.03 to 2.73) than for small-tick stocks (0.50 to 0.85), so imbalance moves the predicted probability of an upward move more sharply for large-tick names.
- Out-of-sample, the logistic regression's area under the ROC curve is 0.752 to 0.805 for large-tick stocks and 0.581 to 0.642 for small-tick stocks, against 0.5 for the null model.
- Out-of-sample mean squared residual for the logistic regression is 0.180 to 0.202 for large-tick stocks and 0.235 to 0.246 for small-tick stocks, against 0.25 for the null model.
- Local logistic regression gives out-of-sample scores that are nearly identical to the plain logistic regression's, with only small, stock-specific gains from the semi-parametric fit despite its greater computational cost.
- The average bid-ask spread sits close to the one-cent tick size for large-tick stocks (0.012 to 0.015 dollars) but is much wider for small-tick stocks (0.195 to 1.111 dollars), which the authors link to the stronger imbalance signal for large-tick names.

## Limitations

- The sample covers only 10 Nasdaq-listed US equities (5 large-tick, 5 small-tick) during a single year (2014), all traded on one price-time-priority venue.
- The prediction target is only the direction of the very next mid-price change, not its size or how predictability decays further ahead, and the imbalance is sampled only once per inter-event interval rather than continuously.
- The analysis uses only the best bid and ask queues and does not incorporate order-flow information from other trading venues for the same stocks.
- Reader note: because the underlying data source only records Nasdaq activity, order flow reaching these stocks through other venues is unobserved, so the measured imbalance could be a noisy proxy for the true consolidated order book.
- The authors themselves describe the non-monotonic local logistic curves found for some small-tick stocks as puzzling and not fully explained.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]

## Citation

Martin D. Gould, Julius Bonart (2015). Queue Imbalance as a One-Tick-Ahead Price Predictor in a Limit Order Book.

DOI: 10.1142/s2382626616500064

Text ingested: `markdown_output/gould-2016-queue-imbalance-one-tick-ahead-price.md`, converted from `raw/ofi-event-clock/gould-2016-queue-imbalance-one-tick-ahead-price.pdf`.

Coverage of this summary: Read the entire paper: abstract, introduction, the LOB and queue-imbalance background sections, the data description, the full methodology section (sample construction, in-sample/out-of-sample split, prediction and assessment formulation, local logistic regression), all results (distribution of imbalance, logistic regression fits and significance tests, out-of-sample performance, local logistic regressions), the discussion, and the conclusion.

Known problems with the input: The document itself is dated December 14, 2015, but the job's year_hint was 2016 (likely referring to a later published journal version); year was taken from the printed date on this version; No journal, conference, or working-paper series name is printed on the document itself, so venue is left blank; Tables 4, 5 and 6 were rendered by the PDF-to-markdown conversion as single cells containing multiple concatenated values per stock; in-sample/out-of-sample pairs were reconstructed by matching each table's stated column order, but a transcription error in the pairing is possible.
<!-- AUTHORED REGION END -->