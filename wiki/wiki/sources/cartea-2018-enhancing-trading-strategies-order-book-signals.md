---
authors:
- Álvaro Cartea
- Ryan Donnelly
- Sebastian Jaimungal
content_hash: sha256:24e4b371e0eab237a8dabcd6a96f04bfa29ec84ff8300a838d0d83744f2402ba
created: 2026-09-27 01:47:00+00:00
page_id: sources/cartea-2018-enhancing-trading-strategies-order-book-signals
page_type: source
publication_venue: Applied Mathematical Finance, 25:1, 1-35
related:
- concepts/trade-clock
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/limit-order-book
- concepts/market-making
- concepts/adverse-selection
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/order-flow
- entities/alvaro-cartea
- entities/sebastian-jaimungal
revision_id: 1
schema_version: 2
source_hash: sha256:a303756b00a3cc68fc4b12d2697b7a44db037dcb579696f4817ec268559b1ff8
source_path: markdown_output/cartea-2018-enhancing-trading-strategies-order-book-signals.md
source_type: paper
tags:
- volume-imbalance
- limit-order-book
- market-making
- adverse-selection
- stochastic-control
- nasdaq-equities
- high-frequency-trading
- order-flow-prediction
- clock-trade
- asset-equity
- harvest-core
title: Enhancing trading strategies with order book signals
updated: '2026-09-27T01:47:00Z'
uuid: 346c275c-57e2-50cb-928d-d6b42f1337eb
year: 2018
---

<!-- AUTHORED REGION START -->
# Enhancing trading strategies with order book signals

## Summary

The paper asks whether the volume resting on each side of the Nasdaq limit order book can predict the direction of the next market order and the price move that follows it, and whether that signal can be turned into a more profitable market-making strategy. The authors build a volume-imbalance measure from the ratio of bid-side to ask-side volume at the best quotes, then study its empirical relationship to market-order arrivals and mid-price changes using Nasdaq message data for a set of equities in 2014.

They first show that a naive market maker who always quotes at the best bid and ask loses money because almost all incoming market orders are absorbed entirely at the best price, so deeper resting orders are rarely filled and cannot protect against adverse selection. Motivated by this, they build a continuous-time Markov-chain-modulated jump model in which the mid-price, spread and a discretized imbalance state jump together at limit-order and market-order arrivals, and they pose the trading problem as a stochastic control problem in which an agent chooses when to post buy and sell limit orders at the best quotes to maximize terminal wealth net of inventory penalties, solved through a Hamilton-Jacobi-Bellman equation.

Empirically, a buy-heavy or sell-heavy imbalance reading is followed by the next market order being a buy or sell with high accuracy, and post-trade mid-price moves are larger and same-signed with the imbalance direction. Limit-order activity itself is concentrated in the milliseconds after a market order arrives. Calibrating the control model on the first half of 2014 and testing on the second half for two large-tick stocks (Intel and Oracle) and nine other Nasdaq names, the strategy that conditions on volume imbalance earns much higher annualized Sharpe ratios than both the always-quote benchmark and a version of the same model that ignores imbalance, and performance improves further as the inventory penalty is tightened.

The contribution is a simple, easily computed imbalance signal shown to have out-of-sample predictive power for order flow and short-horizon price changes, embedded directly into a solvable optimal-execution model for posting limit orders at the touch, with an empirical demonstration that the resulting strategy outperforms both a naive benchmark and posting rules that ignore book imbalance, including under a more conservative, imbalance-dependent assumption about the probability of getting filled.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Volume imbalance is computed continuously from resting best-bid/best-ask volume, and the predictive tests are anchored to each market order arrival: the sign and size of the mid-price change are measured on a fixed 10 ms lag after the market order (the paper states results are unchanged if the window is widened to 100 ms). The live trading strategy is instead evaluated over fixed 30-minute wall-clock intervals during the trading day, with model parameters recalibrated across a rolling sequence of half-hour trading periods and the first and last half-hour of each day excluded.

## Data

- **Asset class:** Equities
- **Instruments:** 11 Nasdaq-listed equities used in the main tests (AA, AMAT, ARCC, BXS, CSCO, EBAY, FMER, IMGN, INTC, NTAP, ORCL), with Intel (INTC) and Oracle (ORCL) used for the full trading-strategy backtest; a further set of stocks (AAPL, FARO, GOOG, MMM, SMH) appears only in appendix robustness tables.
- **Venue:** Nasdaq
- **Period:** All trading days in 2014; in-sample January to June 2014 (124 days) used for calibration and out-of-sample July to December 2014 used for testing, with 249 total trading days in the year. Some cross-sectional statistics (e.g., MO/queue depth tables) use only January 2014.
- **Granularity:** Full order-book message data (every limit order placement, cancellation and market order sent to Nasdaq), aggregated into half-hour trading intervals for the strategy backtest.

## Features and Measures

- **volume imbalance.** A ratio comparing the volume of resting limit orders at the best bid to the volume at the best ask, scaled to lie in [-1,1], used as a proxy for buying versus selling pressure.
- **imbalance regime.** A discretization of volume imbalance into a small number of states (e.g. buy-heavy, neutral, sell-heavy), used as a Markov state that drives order-arrival intensities and price jumps in the model.
- **spread state.** A finite-state process for the bid-ask spread, expressed in ticks, that jumps jointly with the imbalance regime and mid-price at limit-order and market-order arrivals.

## Method

The authors specify a continuous-time, pure-jump model in which three doubly stochastic Poisson random measures drive limit-order and market-order activity; each event can simultaneously move the mid-price, the imbalance regime and the spread. Jump distributions are estimated with symmetry constraints imposed between complementary buy/sell states to rule out long-run directional drift. Model parameters (arrival intensities, expected price jumps per state, and state-transition probabilities) are estimated by constrained maximum likelihood on 30-minute trading windows in the first six months of 2014, then forecast into subsequent half-hour periods with a linear factor/regression model fitted on the in-sample estimates.

Given these dynamics, the agent's problem is posed as a stochastic control problem: choose, at each instant, whether to have a live limit buy and/or limit sell order at the best quote so as to maximize expected terminal wealth minus a running inventory penalty and a terminal liquidation penalty, subject to inventory bounds. The value function solves a Hamilton-Jacobi-Bellman equation; existence and uniqueness of a classical solution, and a verification theorem linking it to the optimal control, are proved, and the optimal control reduces to a threshold rule on inventory for each combination of imbalance regime and spread.

Performance is judged out-of-sample using the annualized mean and standard deviation of half-hour PnL and the annualized Sharpe ratio (risk-free rate set to zero), computed for different numbers of imbalance states, inventory limits, and inventory-penalty strengths, and separately under a version where limit orders fill with a probability estimated from data rather than being filled with certainty.

## Results

- Depending on the equity, between 91.6% and 99.9% of market orders are filled using only the volume resting at the best bid or ask, leaving deeper resting limit orders with roughly a 0.1% to 8.4% chance of being touched by any given market order.
- GOOG has the smallest share of market orders confined to the best price, at 91.6%, while most other stocks examined stay above 99%.
- The always-quote (zero-intelligence) strategy produces negative annualized Sharpe ratios for every tested inventory limit, across all 11 equities.
- Conditioning the limit-order strategy on volume imbalance (3 or 5 imbalance states) produces markedly higher annualized Sharpe ratios than the imbalance-free version of the same model, across the same 11 stocks and range of inventory-penalty values.
- Increasing the running inventory penalty generally raises the strategy's annualized Sharpe ratio for both INTC and ORCL.
- Limit-order activity is heavily concentrated right after market orders arrive: less than 0.5% of the trading day falls within 50 ms of a market order, yet that window accounts for roughly 40% to 90% of all limit-order placement/cancellation events.
- Imposing a realistic, imbalance-dependent fill probability instead of assuming certain execution lowers the strategy's Sharpe ratios relative to the certain-fill case, but they remain considerably higher than the zero-intelligence benchmark.
- Out-of-sample testing spans July to December 2014, giving 1375 half-hour trading intervals for INTC and ORCL after excluding the first and last half-hour of each of the 249 trading days in 2014.

## Limitations

- The agent is assumed to be filled with certainty when posting at the best quote in the main results (except in one robustness check with an estimated, imbalance-dependent fill probability), and to have zero latency in repositioning orders.
- The model imposes a symmetry constraint between complementary imbalance states to rule out long-term directional speculation, which the authors note precludes strategies that exploit persistent short-term trends.
- The trading window is fixed at 30 minutes largely for tractability of computing Sharpe ratios across many periods; the authors state a strategy that runs continuously through the day and unwinds only at day's end should do better.
- The authors cannot rule out that the imbalance-based predictive relationship is affected by order-book spoofing, though they argue the imbalance signal appears robust to such manipulation.
- Reader note: the trading-strategy backtest is demonstrated mainly on two large-tick, single-exchange (Nasdaq) US equities (INTC, ORCL) over one calendar year (2014), so generalization to other tick regimes, venues or periods is untested here.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-making|market making]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-flow|order flow]]
- [[entities/alvaro-cartea|Álvaro Cartea]]
- [[entities/sebastian-jaimungal|Sebastian Jaimungal]]

## Citation

Álvaro Cartea, Ryan Donnelly, Sebastian Jaimungal (2018). Enhancing trading strategies with order book signals. Applied Mathematical Finance, 25:1, 1-35.

DOI: 10.1080/1350486x.2018.1434009

Text ingested: `markdown_output/cartea-2018-enhancing-trading-strategies-order-book-signals.md`, converted from `raw/ofi-event-clock/cartea-2018-enhancing-trading-strategies-order-book-signals.pdf`.

Coverage of this summary: Read the full converted markdown front-to-back, including the introduction, the volume-imbalance and empirical sections, the model and control-problem sections, the out-of-sample performance section, the conclusion, and the appendices with robustness tables; most equations rendered as omitted pictures or garbled inline symbols and were not usable as text.

Known problems with the input: A footnote giving Ryan Donnelly's contact address is badly garbled by the OCR conversion (it mixes a University of Washington postal address and email with unrelated page furniture); the superscript affiliation list in the author line was used instead, so this contact-footnote conflict is flagged rather than resolved; Most displayed equations in the body and appendices were converted to '==> picture... omitted <==' placeholders or corrupted inline symbol strings, so mathematical detail beyond what is described in prose could not be extracted.
<!-- AUTHORED REGION END -->