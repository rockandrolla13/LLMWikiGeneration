---
authors:
- Julius Bonart
- Fabrizio Lillo
content_hash: sha256:f24a6e6e4d0c6c42783a78c2bcce0a80354a6963be03e16d9f6b16b0e749b15a
created: 2026-09-27 01:47:00+00:00
page_id: sources/bonart-2018-continuous-efficient-fundamental-price-discrete-order
page_type: source
related:
- concepts/trade-clock
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/market-microstructure-noise
- concepts/bid-ask-spread
- concepts/order-imbalance
- concepts/order-flow-imbalance
- concepts/price-impact
- concepts/high-frequency-data
- entities/fabrizio-lillo
revision_id: 1
schema_version: 2
source_hash: sha256:07c4aa02b8e932eb94e168221527375a238bb2bca5660d599e4ffa37d9d3b054
source_path: markdown_output/bonart-2018-continuous-efficient-fundamental-price-discrete-order.md
source_type: paper
tags:
- limit-order-book
- tick-size
- price-formation
- market-microstructure
- liquidity-provision
- order-imbalance
- nasdaq
- clock-trade
- asset-equity
- harvest-relevant
title: A continuous and efficient fundamental price on the discrete order book grid
updated: '2026-09-27T01:47:00Z'
uuid: 6076439e-5934-5046-85a2-6e0e5f875af6
year: 2016
---

<!-- AUTHORED REGION START -->
# A continuous and efficient fundamental price on the discrete order book grid

## Summary

The paper asks why the Madhavan-Richardson-Roomans (MRR) price-formation model, built for a continuous price scale, still seems to describe order-flow-driven price changes in stocks whose tick size is large relative to price. It postulates that liquidity providers share a belief in a continuous, efficient fundamental price that can lie outside the best bid and ask, and re-derives the MRR relations for a discretized order book with liquidity rebates. The key theoretical result is that relationships depending linearly on the price (the classic MRR identities linking price impact, trade-sign autocorrelation and spread) survive discretization on average, while relationships depending quadratically on the price, such as the covariance of mid-price returns, do not.

Empirically, the paper uses full order-book event data for 100 liquid Nasdaq stocks and tests the MRR relation across small-, medium- and large-tick groups, finding it holds well over several orders of magnitude even for the most large-tick stock in the sample. It also shows that limit orders at the best remain profitable even when the fundamental price sits outside the bid-ask interval, because exchange-paid liquidity rebates offset the loss, and that this produces a 'sticky' mid-price whose queue-depletion impact matches the rebate-adjusted half-tick.

The second half of the paper builds a proxy for the unobservable fundamental price from the squared volumes available at the best bid and ask, which (unlike a plain volume-weighted mid) can take values outside the spread. The authors show this proxy absorbs most of the information in the order-book imbalance, behaves close to unpredictable (as an efficient price should), and outperforms two simpler alternative proxies on several diagnostics, though it is not a complete solution: it captures only part of the imbalance information and the paper does not attempt to pin down the absolute level of book liquidity.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

The fundamental price and the MRR price-formation equations are indexed in transaction time, with p_t defined as the fundamental price immediately before the t-th trade. Response functions, trade-sign autocorrelations and return covariances are all measured as functions of a transaction-time lag l (number of subsequent trades), not wall-clock time. The underlying data is the full order-book event stream (limit orders, market orders, cancellations), but the price-formation and impact analysis samples the book state at each transaction and looks forward by trade-count lag.

## Data

- **Asset class:** Equities
- **Instruments:** 100 liquid Nasdaq-listed stocks spanning small, medium and large relative tick size (e.g. SIRI, MSFT, AAPL, GOOG, AMZN; full list in the paper's summary table)
- **Venue:** Nasdaq (LOBSTER order-book reconstruction database)
- **Period:** full calendar year 2015, restricted to normal trading hours 09:30-16:00 and excluding the first and last hour of each trading day
- **Granularity:** complete limit order book message data: every market order arrival, limit order arrival and cancellation

## Features and Measures

- **Volume imbalance (iota).** The normalized difference between available volume at the best ask and best bid, used as a public signal of buying versus selling pressure on the price.
- **Fundamental price proxy p-hat.** A proxy for the latent fundamental price built from the squared volumes at the best bid and ask, which can take values outside the bid-ask interval and reduces to the mid-price when the book is balanced.
- **Alternative linear proxy p-hat prime.** A simpler linear generalization of the standard volume-weighted price, compared against the squared-volume proxy as an alternative fundamental-price estimator.
- **Standard volume-weighted price p-hat double-prime.** The conventional volume-weighted average of the best bid and ask, which by construction cannot lie outside the spread.
- **Response function R(l).** The expected price change l transactions after a trade, conditioned on that trade's sign, used to measure price impact and to test the MRR relation against the trade-sign autocorrelation.

## Method

The paper adapts the MRR structural price-formation model, in which quote revisions track the innovation in trade-sign order flow relative to its publicly expected value, to a market with a discrete tick and exchange-paid liquidity rebates. It derives that MRR's testable relation between the response function and trade-sign autocorrelation continues to hold on average once discretization is introduced, because the discretization error cancels for linear price statistics but not for quadratic ones such as return covariance. These predictions are tested empirically on 100 Nasdaq stocks split into large-, medium- and small-tick groups by their average spread, using the measured response function and trade-sign autocorrelation.

The paper then constructs and evaluates a fundamental-price proxy built from the squared best-quote volumes, comparing it against the raw mid-price and two alternative volume-weighted proxies. Performance is judged by (i) how much of the order-book imbalance's information the proxy absorbs, (ii) whether its own response function is close to flat (as an efficient, unpredictable price should be), and (iii) the autocorrelation of its returns and the corresponding volatility signature plot.

## Results

- The MRR relation between the response function and trade-sign autocorrelation, R(l)/(1-C(l)), holds accurately over several orders of magnitude across the 100-stock pool, including the stock with the largest relative tick in the sample.
- The permanent price impact of a queue depletion at the best is close to the rebate-adjusted half tick (0.5 + 0.3 = 0.8 cents) for essentially all large-tick stocks tested.
- The permanent impact of a large order-book imbalance (|iota| > 0.9) is similarly close to the rebate-adjusted half tick.
- The covariance relation predicted from the MRR framework holds well for small-tick stocks but performs poorly for large-tick stocks, consistent with the theory that discretization matters for quadratic but not linear price statistics.
- The squared-volume proxy p-hat captures about 80% of the information in the order-book imbalance, versus the mid-price on which the imbalance's impact is roughly 5 times larger (i.e. the imbalance's impact on the proxy is only about 20% as large as on the mid-price).
- The proxy's own response function differs between its first lag and its long-run value by only about 10%, compared with a factor of 2.5 for the same comparison on the raw mid-price, indicating the proxy behaves closer to an efficient price.
- The return autocorrelation of the proxy is close to zero at all lags tested, while the two alternative proxies show a persistent positive autocorrelation.
- In roughly 25% of queue-depletion events, the depleted queue is immediately refilled, which the authors read as evidence that liquidity providers do not always agree on whether a price change is warranted.

## Limitations

- The empirical analysis covers a single exchange (Nasdaq), a single tick size regime ($0.01), and a single year (2015).
- The fundamental-price proxy is only a partial solution: it captures around 80% of the imbalance information, described by the authors as encouraging but not outstanding.
- The paper does not derive a way to determine the absolute level of order-book liquidity, only the relative position of the fundamental price.
- Reader note: the model is described by the authors as phenomenological rather than derived from first principles of trader behavior.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/price-impact|price impact]]
- [[concepts/high-frequency-data|high frequency data]]
- [[entities/fabrizio-lillo|Fabrizio Lillo]]

## Citation

Julius Bonart, Fabrizio Lillo (2016). A continuous and efficient fundamental price on the discrete order book grid.

DOI: 10.1016/j.physa.2018.03.002

Text ingested: `markdown_output/bonart-2018-continuous-efficient-fundamental-price-discrete-order.md`, converted from `raw/ofi-event-clock/bonart-2018-continuous-efficient-fundamental-price-discrete-order.pdf`.

Coverage of this summary: Read the full paper end to end, including the abstract, introduction, literature review, order-book description, data section, both theoretical sections on transaction-history dependent price formation, the fundamental-price proxy section, conclusions and the appendix tables.
<!-- AUTHORED REGION END -->