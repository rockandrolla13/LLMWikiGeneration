---
authors:
- Chen Hu
- Kouxiao Zhang
content_hash: sha256:a6cd790c40df7d5901ba3814b0ba493ad8f625fd7ffdb720e3dfc16192f5862c
created: 2026-08-13 00:00:00+00:00
page_id: sources/hu-2025-ofi-csi300-ou
page_type: source
related:
- concepts/order-flow-imbalance
- concepts/price-impact
- concepts/market-microstructure
- concepts/hawkes-processes
- concepts/order-imbalance
- sources/cont-2023-cross-impact-ofi
- sources/su-2021-generalized-ofi
revision_id: 1
schema_version: 2
source_hash: sha256:617735b92bacf884fb543d053587b105dd97c229c90e637e8a582d1d0ae2a69c
source_path: markdown_output/2505.17388.md
tags:
- order-flow-imbalance
- ornstein-uhlenbeck
- levy-process
- market-microstructure
- chinese-markets
- index-futures
- regime-switching
- forecast-horizon
title: 'Stochastic Price Dynamics in Response to Order Flow Imbalance: Evidence from
  CSI 300 Index Futures'
updated: '2026-08-13T00:00:00Z'
uuid: 7e5430ec-5c5d-5e9e-9b71-aed8b3d2ea44
year: 2025
---

<!-- AUTHORED REGION START -->
# Stochastic Price Dynamics in Response to Order Flow Imbalance: Evidence from CSI 300 Index Futures

## Summary

Treats an accumulated [[concepts/order-flow-imbalance|order flow imbalance]] as a **shock** and asks how the price responds over time, rather than fitting OFI against a matching-length return window. The response is modelled as a mean-reverting Ornstein–Uhlenbeck process driven by a jump-type Lévy process, substituted for the drift of geometric Brownian motion. The practical payoff is a statement about horizon choice: an indicator's usefulness is a function of response time, not a fixed property.

## The Methodological Point

Most OFI studies compute the indicator over a window of length $h$ and regress it on the return over the *next* window of the same length $h$. This paper's objection is that the symmetry is arbitrary. A 5-second OFI does not stop mattering after 5 seconds.

So OFI over a fixed historical window is treated as a step shock, and its response is measured across many subsequent horizons. The authors then exhaustively cross historical windows against forecast horizons rather than tying them together.

## The Model

Where much of the literature reaches for [[concepts/hawkes-processes|Hawkes processes]] to model self-exciting order flow, this paper follows Lehalle & Neuman in using an **Ornstein–Uhlenbeck process** — chosen for two properties the data shows: memory, and mean reversion.

The drift term of canonical geometric Brownian motion is replaced by this O-U process, justified by the empirically stable contemporaneous correlation between OFI and mid-price change. Solving the coupled SDEs yields the log-return process with explicit mean and variance under initial boundary conditions.

Two departures from the standard setup:

- The O-U process is driven by a **jump-type Lévy process**, not a Wiener process. The authors find empirically that tick-level order flow contributions are heavy-tailed, so a Gaussian driver misfits.
- They derive a time-varying, Sharpe-like quantity they call the **response ratio** (or quasi-Sharpe ratio), which measures the competition between OFI-induced deterministic drift and stochastic diffusion as the horizon extends. It has an asymptotic value, derived in the appendix.

## Data

One year of tick data on CSI 300 index futures. "Tick" here means the exchange's **500-millisecond snapshot**: a snapshot is emitted when a trade occurs or the book changes within the interval, and carries last trade price, interval volume and the current book. It is not event-by-event data. One index point equals CNY 300.

Four metrics are compared: OFI, trade imbalance (TI, using a Lee–Ready style classification of aggressive buys and sells), Lambda, and AvgEn.

## Findings

**Horizon dependence is the headline.** Regression PnL is essentially flat across historical window lengths for forecast horizons from 0.5 seconds to 10 minutes, and diverges sharply only beyond roughly 1500 ticks (12 minutes). Within a 2-minute historical window and horizons under 10 minutes, performance is stable and gradually improving. At short horizons the cumulative predicted return grows with horizon in a shape the authors describe as saturating-logarithmic — which matches the mean process their model predicts.

**Metric pairing depends on horizon.** Which secondary indicator best complements OFI changes with the forecast horizon; there is no horizon-free "best combination". LASSO with 5-fold cross-validated regularisation on a train/test split is used for the combination backtests.

**Market regimes.** Computing the statistics month by month rather than over the year, the authors classify months into efficient and inefficient regimes. Inefficient months are where high-frequency participation finds opportunity — and, they argue, where it contributes to pricing efficiency.

## A Screening Criterion for Microstructure Indicators

The most portable contribution is a test for whether a candidate indicator is worth keeping. A robust metric should:

1. Show significant contemporaneous correlation with price movement, with coefficients stable across time windows.
2. Show memory — high autocorrelation with slow decay.
3. Preserve both properties across market regimes, varying **quantitatively but never in sign**.

Sign reversal across regimes is the disqualifying failure. OFI passes; the framing is offered as an ex-ante screen for new indicators rather than a post-hoc rationalisation.

## Limitations

- A single instrument (CSI 300 futures) over one year. No cross-sectional or cross-market evidence.
- 500 ms snapshots, not order-by-order data, so event-type decomposition of the kind in [[sources/sitaru-2023-decomposed-ofi]] is not available.
- The regime classification is derived from the same year it describes; no out-of-period test of the taxonomy is reported.
- PnL figures are regression-implied and do not model execution or costs.

## Related

- [[sources/cont-2023-cross-impact-ofi]] — cited directly; this paper's horizon argument extends their point that prediction horizons should be lengthened
- [[sources/su-2021-generalized-ofi]] — the other Chinese-market OFI paper here, also constrained by snapshot frequency
- [[concepts/order-flow-imbalance]], [[concepts/price-impact]], [[concepts/market-microstructure]]

## Citation

Hu, C., & Zhang, K. (2025). Stochastic Price Dynamics in Response to Order Flow Imbalance: Evidence from CSI 300 Index Futures. arXiv:2505.17388. Guolian Futures Ltd., Shanghai.
<!-- AUTHORED REGION END -->