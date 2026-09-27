---
authors:
- Charles-Albert Lehalle
- Eyal Neuman
content_hash: sha256:e936fb55ad08a2c8ec7329d6203293d72a119f5893eb1b08275b9767d3c545dd
created: 2026-09-27 01:47:00+00:00
page_id: sources/lehalle-2019-incorporating-signals-into-optimal-trading
page_type: source
related:
- concepts/sampling-clocks
- concepts/optimal-execution
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/price-impact
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/high-frequency-trading
- concepts/trader-clustering
revision_id: 1
schema_version: 2
source_hash: sha256:89ad3be55dd36e4bf461f1c3c0d337a70f51ac9492faaf77328d0e23c1a9e0ae
source_path: markdown_output/lehalle-2019-incorporating-signals-into-optimal-trading.md
source_type: paper
tags:
- optimal-execution
- order-book-imbalance
- market-impact
- ornstein-uhlenbeck
- high-frequency-trading
- market-microstructure
- trading-signals
- stochastic-control
- clock-compares
- asset-equity
- harvest-relevant
title: Incorporating Signals into Optimal Trading
updated: '2026-09-27T01:47:00Z'
uuid: ccd70d45-c6e3-5070-8ab0-a92fa826ddc2
year: 2018
---

<!-- AUTHORED REGION START -->
# Incorporating Signals into Optimal Trading

## Summary

The paper asks how a short-term predictive signal about future price moves can be incorporated into the classical optimal-execution problem, where a trader minimizes trading costs and inventory risk while unwinding a position over a fixed horizon.

The authors add a Markovian signal to the price drift inside two existing execution frameworks: the Gatheral-Schied-Slynko (GSS) setting with a transient, decaying market-impact kernel and a fuel constraint, and the Cartea-Jaimungal (CJ) setting with instantaneous impact and a terminal penalty instead. They prove existence and uniqueness of the optimal strategy in the GSS setting and solve it explicitly when the signal follows an Ornstein-Uhlenbeck process and impact decays exponentially, then show the CJ solution emerges as the limit of the GSS solution as impact becomes instantaneous. To motivate the choice of signal, they analyse nine months of tick-by-tick trade and order-book data for 13 Swedish large-tick stocks on NASDAQ OMX Stockholm, classifying trading members into four participant types and computing the order-book imbalance from the best bid and ask sizes just before each trade.

Theoretically, adding a signal can make the optimal execution strategy non-monotone, meaning that intermediate trades in the opposite direction of the overall order can lower expected costs, which points to the possibility of transaction-triggered price manipulation once a signal is present. Empirically, the order-book imbalance predicts the average price move over the following trades and mean-reverts, and a simple Ornstein-Uhlenbeck fit gives reversion and noise parameters consistent with the theoretical model. High-frequency market makers and proprietary traders, and to some extent global investment banks, condition their trading rate on the imbalance, while institutional brokers show little such sensitivity.

The main novelty is combining a Markovian, non-martingale signal with a decaying transient market-impact kernel for the first time, extending the GSS existence and uniqueness results, and linking this theory to a direct empirical demonstration that a specific liquidity signal (order-book imbalance) is both predictive and already used strategically by different classes of market participants.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The theoretical model runs in continuous calendar time over a fixed horizon [0,T]. The empirical analysis instead measures the imbalance and its predictive power over discrete trade counts (after 3, 5, 7, 10 and 100 trades), switching to 'trade time' rather than calendar seconds so that stocks with different trading frequencies are comparable when fitting the Ornstein-Uhlenbeck model; a separate analysis of participant behaviour aggregates trading rate and imbalance over fixed 10-minute calendar-time windows.

## Data

- **Asset class:** Equities
- **Instruments:** 13 large-tick stocks on NASDAQ OMX Stockholm, including Volvo AB, Nordea Bank AB, Telefonaktiebolaget LM Ericsson, Hennes & Mauritz AB, Atlas Copco AB, Swedbank AB, Sandvik AB, SKF AB, Skandinaviska Enskilda Banken AB, Nokia OYJ, Telia Co AB, ABB Ltd and AstraZeneca PLC
- **Venue:** NASDAQ OMX Stockholm
- **Period:** January 2013 to September 2013 (180 trading days)
- **Granularity:** tick-by-tick labelled trades matched with the order-book state just before each transaction

## Features and Measures

- **Order-book imbalance.** A signal built from the best bid quantity and best ask quantity just before a trade, used to gauge which side of the book is under more pressure.
- **Imbalance-conditioned trading rate (R+/R-).** An estimator of how much of a participant type's traded volume occurs in the direction of the current imbalance versus in the opposite direction, computed over 10-minute intervals.
- **Ornstein-Uhlenbeck signal model.** A mean-reverting stochastic process used both as the theoretical driver of the price drift and as the fitted empirical model for the imbalance's dynamics in trade time.

## Method

The theoretical part poses a cost functional combining expected trading costs from a transient or instantaneous market-impact model with a running inventory risk-aversion term, and minimizes it over admissible deterministic trading strategies given an observed Markovian signal at the start of trading. Existence and uniqueness are established for continuous, bounded, strictly positive-definite impact kernels, and an explicit singular strategy is derived for an exponential kernel and an Ornstein-Uhlenbeck signal; the equivalent instantaneous-impact (Cartea-Jaimungal) problem is solved via a Hamilton-Jacobi-Bellman equation with a value-function ansatz. The empirical part classifies NASDAQ OMX exchange members into four participant types from their membership codes, computes the imbalance from best bid and ask sizes before each trade, and fits linear regressions of the subsequent price move and of the future imbalance on the current imbalance to estimate the mean-reversion speed and noise level of an Ornstein-Uhlenbeck approximation; participant trading rates are then related to the imbalance over 10-minute windows to test whether trading speed is conditioned on the signal.

## Results

- Order-book imbalance predicts the average price move over the next 10 trades, with the price move averaging close to 0.6 times the imbalance value just before the first of those trades.
- The R2 of the regression of the 10-trade-ahead price move on the current imbalance ranges from about 1% (Nokia) to 16% (Volvo AB and Nordea Bank AB) across the 13 stocks, with p-values close to zero.
- The imbalance mean-reverts: fitting a discrete Ornstein-Uhlenbeck process at a scale of 7 trades (about 35 seconds) gives a reversion speed near 0.92 and a noise parameter near 0.22.
- Global investment banks are involved in 58% of trades and high-frequency traders in 32%, with institutional brokers making up the remaining 10%; on average 78% of trades have at least one identified participant type.
- High-frequency market makers send 73% of their orders as limit orders and trade less as the imbalance intensifies, consistent with providing liquidity and managing adverse selection.
- High-frequency proprietary traders and, for part of the sample, global investment banks trade more in the direction of the imbalance and less against it as the imbalance strengthens; institutional brokers show little such sensitivity.
- Adding a signal to the transient-impact model can make the optimal strategy non-monotone, which the authors link to a possible transaction-triggered price manipulation that is absent from the no-signal case.
- As the transient market-impact kernel is taken to the limit of instantaneous impact, the explicit Ornstein-Uhlenbeck solution from the transient-impact (GSS) framework converges to the solution obtained directly in the instantaneous-impact (Cartea-Jaimungal) framework.

## Limitations

- The impact-decay speed parameter rho cannot be estimated from the available data, so the authors use two arbitrary but plausible values in their illustrative figures.
- The empirical section is explicitly described as illustrative rather than an extensive econometric study, covering only 13 large, liquid stocks selected for having at least 100,000 trades by high-frequency proprietary traders.
- The explicit optimal-strategy results assume a deterministic strategy that uses only the signal's value at the start of trading, not a strategy that adapts to the signal's path; the authors note the fully adaptive version is left open.
- Reader note: all data come from a single exchange (NASDAQ OMX Stockholm) over a single nine-month window, so the identified imbalance dynamics may not generalize to other venues or periods.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/optimal-execution|optimal execution]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/price-impact|price impact]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/trader-clustering|trader clustering]]

## Citation

Charles-Albert Lehalle, Eyal Neuman (2018). Incorporating Signals into Optimal Trading.

DOI: 10.1007/s00780-019-00382-7

Text ingested: `markdown_output/lehalle-2019-incorporating-signals-into-optimal-trading.md`, converted from `raw/ofi-event-clock/lehalle-2019-incorporating-signals-into-optimal-trading.pdf`.

Coverage of this summary: Read the whole paper end to end: abstract, introduction, the theoretical model and results in Sections 2 and 3, the empirical analysis of NASDAQ OMX data in Section 4, the proofs in Section 5, and the appendix tables of participant classifications and estimated parameters.

Known problems with the input: Most equations and figures are rendered as 'picture intentionally omitted' placeholders in the markdown, so the exact formal cost functional, HJB equation and closed-form strategy expressions could not be verified beyond what the surrounding prose states; OCR artifacts appear in places, e.g. 'Narket participants' for 'Market participants', 'pamperers of the model' for 'parameters of the model', and 'apposite direction' for 'opposite direction'; these were not treated as content.
<!-- AUTHORED REGION END -->