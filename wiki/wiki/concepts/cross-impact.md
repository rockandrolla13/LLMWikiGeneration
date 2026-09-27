---
content_hash: sha256:7349c1cbe3e5cb5bf07096853732ad068e69330a67b5d7dad35b9f633066f1b7
created: 2026-08-13 00:00:00+00:00
mind_map_priority: medium
page_id: concepts/cross-impact
page_type: concept
related:
- concepts/price-impact
- concepts/order-flow-imbalance
- concepts/limit-order-book
- concepts/market-microstructure
revision_id: 1
schema_version: 2
sources:
- sources/cont-2023-cross-impact-ofi
- sources/coz-2024-when-cross-impact-relevant
- sources/michael-2022-option-volume-imbalance-predictor-equity-market
tags:
- cross-impact
- price-impact
- order-flow-imbalance
- market-microstructure
- lasso
- network-structure
title: Cross-Impact
updated: '2026-09-27T01:47:00Z'
uuid: c5f23a01-f1e0-503d-a498-ee1848078a70
---

<!-- AUTHORED REGION START -->
# Cross-Impact

The effect of trading one asset on the price of *another*. It is intuitively obvious that it exists — index arbitrage, sector baskets and ETF creation all trade many names at once — and surprisingly hard to demonstrate that it adds anything once you model a single asset properly.

## The Core Finding

[[sources/cont-2023-cross-impact-ofi|Cont, Cucuringu & Zhang (2023)]] give the sharpest statement, on 100 S&P 500 names over 2017–2019.

Add other stocks' best-level [[concepts/order-flow-imbalance|OFI]] to a single-stock model and contemporaneous fit improves: significantly, for 91% of stocks. Add other stocks' *integrated* (multi-level) OFI to a model that already uses the stock's own integrated OFI, and the improvement is significant for only 28% of stocks — and out-of-sample it is slightly negative.

The proposed explanation is **substitution**. A multi-asset strategy places linked orders in two stocks at different depths. A model reading only stock $i$'s best level misses its own deeper order; stock $j$'s best-level flow partially stands in for it. Once stock $i$'s own book is integrated across depth, the proxy is redundant. Cross-asset OFI was, to a large extent, a surrogate for a stock's own deeper book.

Capponi & Cont had earlier shown that positive covariance between one stock's returns and another's order flow is *not* evidence of cross-impact, once the common factor in order flows is accounted for. This result extends that to out-of-sample and to multi-level flow.

## Where Cross-Impact Does Survive

Three places, and they matter.

**Forecasting.** Lagged cross-asset OFI significantly improves one-minute-ahead return prediction for *every* stock at the 1% level. The advantage decays quickly with horizon. The suggested mechanism is a **flow formation lag** — a large order forms in one name, other traders notice it a minute later and adjust. That would explain why cross-asset flow predicts without explaining contemporaneously.

**Portfolios.** Individual cross-impact coefficients are tiny (order $10^{-3}$ against self-impact of order 1) but they aggregate. Portfolio impact depends on the angle between the coefficient vector and the weight vector, so cross-terms only cancel when the portfolio is concentrated or when price dynamics are universal across names. For equal-weighted and first-eigenportfolio construction, cross-impact adds 2–3 points of out-of-sample $R^2$.

**Large tick-to-price stocks.** Cross-asset OFI explains price dynamics better where the tick is coarse relative to the price.

## Structure of the Cross-Impact Network

Treating the coefficient matrix as a weighted directed graph:

- **Best-level OFI coefficients show clear sector structure**, consistent with basket and index-arbitrage trading. Integrated OFI coefficients do not — the network is far sparser.
- The few links surviving a 95th-percentile threshold on integrated OFI are economically specific: GOOGL → GOOG (voting to non-voting, directional), Cigna → Anthem, Duke Energy → NextEra Energy. All are share-class or merger relationships.
- In the *forecasting* network, Information Technology, Communication Services and Consumer Discretionary have much the highest out-degree — they lead others rather than follow.
- Predictive cross-impact coefficients are frequently **negative**, consistent with Pasquariello & Vega.
- The adjacency matrices are strongly rank-1 (a market mode), with the next 6–8 singular values plausibly corresponding to sectors.

## The Estimation Trap

With $N \approx 100$ assets and 30 one-minute observations in an estimation window, OLS is ill-posed and cross-asset OFIs are strongly collinear — roughly 10% of pairwise correlations exceed 0.30. LASSO with cross-validated penalty is the standard remedy. Any cross-impact result estimated by unregularised OLS on a short window should be treated as suspect.

## Related

- [[concepts/price-impact]], [[concepts/order-flow-imbalance]]
- Researchers: [[entities/rama-cont|Rama Cont]] · [[entities/mihai-cucuringu|Mihai Cucuringu]] · [[entities/chao-zhang|Chao Zhang]]
- [[concepts/limit-order-book]], [[concepts/market-microstructure]]
<!-- AUTHORED REGION END -->