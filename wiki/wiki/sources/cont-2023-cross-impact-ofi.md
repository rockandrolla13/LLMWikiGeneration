---
authors:
- Rama Cont
- Mihai Cucuringu
- Chao Zhang
content_hash: sha256:3ee4eb5a32094f1b2a0f194944d01a9de60ff12bff4d94f26e63f38a8dc5c671
created: 2026-08-13 00:00:00+00:00
page_id: sources/cont-2023-cross-impact-ofi
page_type: source
related:
- concepts/order-flow-imbalance
- concepts/cross-impact
- concepts/price-impact
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/order-imbalance
- entities/rama-cont
- entities/mihai-cucuringu
- entities/chao-zhang
- sources/xu-2020-mlofi
- sources/sitaru-2023-decomposed-ofi
revision_id: 1
schema_version: 2
source_hash: sha256:c00654ab9950984cd916bd38901dd3c820c38f78e475d5411ae897dc9d84596d
source_path: markdown_output/2112.13213.md
tags:
- order-flow-imbalance
- cross-impact
- price-impact
- limit-order-book
- market-microstructure
- integrated-ofi
- lasso
- equity-markets
title: Cross-Impact of Order Flow Imbalance in Equity Markets
updated: '2026-08-13T00:00:00Z'
uuid: 45c61d03-f04a-5acd-be91-dabce2defe66
year: 2023
---

<!-- AUTHORED REGION START -->
# Cross-Impact of Order Flow Imbalance in Equity Markets

## Summary

The paper that settles two questions about [[concepts/order-flow-imbalance|order flow imbalance]] at once. First, it shows how to compress OFI measured across ten levels of the [[concepts/limit-order-book|limit order book]] into a single **integrated OFI**, which explains contemporaneous returns far better than the best-level OFI of Cont, Kukanov & Stoikov (2014). Second, having done that, it shows that [[concepts/cross-impact|cross-impact]] largely evaporates: once a stock's own book is read properly, the order flow of *other* stocks adds nothing to explaining its contemporaneous return. Cross-asset flow does, however, help *forecast* returns a minute ahead — an asymmetry the authors read as a lag between flow forming and other traders noticing it.

## Data

Nasdaq ITCH via LOBSTER, top 100 S&P 500 components by market capitalisation as of 2019-12-31, over 2017-01-01 to 2019-12-31. The first and last 30 minutes of each session are dropped, leaving 10:00–15:30. Returns and OFIs are computed minutely; regressions use non-overlapping 30-minute estimation windows.

## The Integrated OFI

Level-$m$ order flow is accumulated over $(t-h, t]$ and scaled by average book depth across the top $M=10$ levels:

$$\text{ofi}^{m,h}_{i,t} = \frac{\text{OFI}^{m,h}_{i,t}}{Q^{M,h}_{i,t}}$$

The ten level-OFIs are strongly correlated — above 0.75 for every stock — and **the first principal component explains 89.06% (sd 6.12) of their total variance**. The integrated OFI is that first component, with the loading vector normalised by its $\ell_1$ norm so the weights sum to one.

Two structural findings about the loadings:

- The **best level carries the smallest weight** in the first component, but the highest cross-stock standard deviation. Level 1 is the least representative level, not the most.
- For **high-volume and low-volatility** stocks, deeper levels get more weight; for **low-volume and wide-spread** stocks, the best level dominates.

## Contemporaneous Impact: Cross-Impact Disappears

Four models: price impact on own best-level OFI (**PI¹**) or own integrated OFI (**PI^I**), each extended with the cross-section of other stocks' OFIs (**CI¹**, **CI^I**). PI models by OLS; CI models by LASSO, since $N \approx 100$ regressors against 30 observations makes OLS ill-posed.

| Model | In-sample $R^2$ | Out-of-sample $R^2$ |
|---|---|---|
| PI¹ (best-level, own) | 71.16 (13.80) | 64.64 (21.82) |
| CI¹ (best-level, cross) | 73.87 (12.23) | 66.03 (19.51) |
| PI^I (integrated, own) | 87.14 (9.16) | 83.83 (16.90) |
| CI^I (integrated, cross) | 87.85 (8.58) | 83.62 (14.53) |

The pattern is the point. Adding cross-asset terms to a best-level model buys 2.71 points in-sample; adding them to an integrated model buys 0.71. Out of sample, cross-impact on integrated OFI is *worse* than no cross-impact at all. Under a Giacomini–White test, **CI¹ beats PI¹ for 91.0% of stocks at the 1% level, but CI^I beats PI^I for only 28.1%**.

LASSO tells the same story through variable selection. Self-impact is chosen essentially always (99.85%, 99.96%). Cross-terms are chosen 17.34% of the time with best-level OFI but only 8.29% with integrated OFI, and their coefficients shrink to about a third the size.

The authors' explanation is a substitution argument: a multi-asset trading strategy places linked orders in stock $i$ and stock $j$ at *different* depths. A model reading only stock $i$'s best level misses its own deeper order, and cross-asset best-level OFI partially proxies for it. Integrate the levels and that proxy becomes redundant. Cross-asset OFI is a surrogate for a stock's own deeper book.

The few cross-links that survive a 95th-percentile threshold are economically legible: GOOGL → GOOG (the voting/non-voting share pair, and the direction is GOOGL leading), Cigna → Anthem, and Duke Energy → NextEra Energy — all merger-linked pairs.

## Where Cross-Impact Does Survive

Two places.

**Portfolios.** For an equal-weighted portfolio, out-of-sample $R^2$ goes 79.29 → 81.03 (best-level) and 85.26 → 87.97 (integrated) when cross-terms are added; the first-eigenportfolio results are similar. Cross-impact coefficients are individually tiny but aggregate at portfolio level, because portfolio impact depends on the angle between the coefficient vector and the weight vector.

**Large tick-to-price stocks.** Cross-asset OFIs explain price dynamics better for stocks with a higher tick-to-price ratio.

## Forecasting: Cross-Impact Returns

Predicting the next minute's return from lagged OFI at lags $L = \{1,2,3,5,10,20,30\}$ minutes:

| | FPI¹ | FCI¹ | FPI^I | FCI^I | AR | CAR |
|---|---|---|---|---|---|---|
| OS $R^2$ | −0.37 | −0.10 | −0.36 | −0.10 | −0.36 | −0.10 |

Every cross-sectional model beats its own-stock counterpart, significantly at the 1% level for all stocks. All $R^2$ are negative; the authors invoke Kelly et al. to argue that negative out-of-sample $R^2$ does not imply economically useless forecasts, and back it with trading PnL.

Unlike the contemporaneous case, **integrated OFI gives no forecasting advantage over best-level OFI**. The authors suggest this is because the integrated OFI discards level information — how far a level sits from the touch — and traders choose their level strategically, so level identity carries predictive content that PCA averages away.

Cross-impact coefficients are frequently **negative**, consistent with Pasquariello & Vega. Information Technology, Communication Services and Consumer Discretionary have much the highest out-degree centrality — they predict others rather than being predicted. The top out-degree names are AMZN, GOOG, GOOGL, NVDA and NFLX under best-level OFI.

The advantage decays fast: cross-asset PnL declines more steeply than own-stock PnL as the horizon extends from 1 to 30 minutes.

## Why the Asymmetry

Cross-asset flow helps forecasts but not contemporaneous fits. The proposed mechanism is a **flow formation lag**: a large order in AAPL at 10:00 is noticed by other traders who adjust their books at 10:01, so AAPL's OFI predicts other stocks' returns without explaining them contemporaneously. This is offered as a hypothesis, not tested — the authors note that testing it needs client-ID-level LOB data to confirm the same participant is behind linked orders in two instruments.

## Limitations

- Trading costs are excluded from all PnL figures.
- The substitution mechanism of Figure 7 is a proposed explanation, not a tested prediction; the authors flag that it requires client-ID data to verify.
- Physical time, not trading time, is used throughout, because stocks trade asynchronously.
- 100 large-cap US equities over three years; no claim is made about small caps or other venues.

## Version History

This paper accumulated four titles. Earlier versions circulated as *"Price Impact of Order Flow Imbalance: Multi-level, Cross-sectional and Forecasting"* (arXiv v1, December 2021), *"Price Impact of Order Flow Imbalances: Multi-level, Cross-asset and Forecasting"*, and *"Cross-Impact of Order Flow Imbalance: Contemporaneous and Predictive"*, before publication in *Quantitative Finance* under the present title. Bibliographic databases list these as separate works; they are one paper.

## Related

- [[sources/xu-2020-mlofi]] — the multi-level OFI vector this paper compresses into a scalar
- [[sources/sitaru-2023-decomposed-ofi]] — decomposes the same OFI by event type instead, on the same LOBSTER dataset
- [[sources/su-2021-generalized-ofi]] — an independent generalisation of OFI, on Chinese data
- [[concepts/cross-impact]], [[concepts/order-flow-imbalance]], [[concepts/price-impact]]

## Citation

Cont, R., Cucuringu, M., & Zhang, C. (2023). Cross-impact of order flow imbalance in equity markets. *Quantitative Finance*, 23(10), 1373–1393. arXiv:2112.13213.
<!-- AUTHORED REGION END -->