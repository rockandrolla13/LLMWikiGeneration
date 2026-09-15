---
authors:
- Bogdan Sitaru
- Anisoara Calinescu
- Mihai Cucuringu
content_hash: sha256:8fb5bc4ce264dccd4cde78da8adcd4bf55386d94585d1d6aa1082f5ad454de42
created: 2026-08-13 00:00:00+00:00
page_id: sources/sitaru-2023-decomposed-ofi
page_type: source
related:
- concepts/order-flow-imbalance
- concepts/price-impact
- concepts/limit-order-book
- concepts/order-imbalance
- concepts/market-microstructure
- entities/mihai-cucuringu
- sources/cont-2023-cross-impact-ofi
- sources/xu-2020-mlofi
revision_id: 1
schema_version: 2
source_hash: sha256:81746fc0a0b190883b614808efe8a6eed6827b3150bea3cb3e64e34706b1bf1b
source_path: markdown_output/sitaru-2023-order-flow-decomposition.md
tags:
- order-flow-imbalance
- price-impact
- limit-order-book
- market-by-order
- lasso
- market-microstructure
- order-submission
- icaif
title: Order Flow Decomposition for Price Impact Analysis in Equity Limit Order Books
updated: '2026-08-13T00:00:00Z'
uuid: bad1ace5-a1ce-5435-9e5e-69bf9b5cc802
year: 2023
---

<!-- AUTHORED REGION START -->
# Order Flow Decomposition for Price Impact Analysis in Equity Limit Order Books

## Summary

Splits [[concepts/order-flow-imbalance|order flow imbalance]] into the three event types that generate it — **add**, **cancel**, **trade** — and asks whether the decomposition carries information the aggregate hides. The answer is a clean split: it does **not** help explain contemporaneous returns, but it roughly triples the trading profit of a forecasting model. The component that does the work is the one usually ignored — limit order *submissions*, not trades.

## The Construction

The standard OFI over $(t-h, t]$ is decomposed by indicator function on event type:

$$\text{OFI}^{\ell,h}_t = \text{OFIa}^{\ell,h}_t + \text{OFIc}^{\ell,h}_t + \text{OFIt}^{\ell,h}_t$$

The three components sum exactly to the undifferentiated OFI, so the decomposition is a refinement rather than a different quantity. Each is normalised by average level depth in the same way as standard OFI. This requires **market-by-order** data — event types are not recoverable from snapshots.

LOBSTER's seven event types are collapsed to three: add = type 1 (new limit order); cancel = types 2 and 3 (cancellation, deletion); trade = types 4, 5, 6 (visible execution, hidden execution, cross trade). Hidden-order execution does not change the book, so its OFI contribution is null.

## Data

The same dataset as [[sources/cont-2023-cross-impact-ofi|Cont, Cucuringu & Zhang]], deliberately, so the comparison is like-for-like: LOBSTER market-by-order data for the top 100 S&P 500 constituents at the start of 2017, over 2017-01-01 to 2019-12-31, restricted to 10:00–15:30.

## Contemporaneous: No Gain

Ten-second buckets, ten book levels, 30-minute in-sample window (180 observations), next 30 minutes out-of-sample.

| Model | IS $R^2$ | OS $R^2$ |
|---|---|---|
| PI¹⁰ (standard OFI, OLS) | 91.97 | 89.37 |
| PID¹⁰ (decomposed, OLS) | 93.0 | not reportable |
| PID¹⁰ (decomposed, LASSO) | 92.23 | 87.03 |
| PID^{I,10} (10 principal components) | 90.57 | 86.24 |

Decomposition buys about 1 point in-sample and gives back about 2 out-of-sample. Fitted by OLS it **overfits catastrophically** — for $\ell \geq 6$ the out-of-sample $R^2$ falls below −100% and the authors decline to report it. The cause is arithmetic: PID has three times the regressors of PI on the same 180 observations. Either LASSO or PCA restores generalisation, at no benefit over plain OFI.

A second contrast with the integrated OFI of Cont et al. is worth noting. There, one principal component captured ~89% of multi-level OFI variance. Here the first component of the *decomposed* vector captures only 59.43%, and five components are needed to reach 89.24%. Splitting by event type genuinely adds dimensions rather than re-expressing one.

## Forward-Looking: Large Economic Gain, No Statistical One

One-minute buckets and horizon, rolling 30-minute estimation (30 observations), lag sets $M_3 = \{1,2,3\}$ and $M_7 = \{1,2,3,5,10,20,30\}$ minutes. LASSO throughout except the two best-level OLS baselines.

**Statistically, decomposition loses.** Every out-of-sample $R^2$ is negative, and the best model is the simplest one — FPI¹ with $M_3$ and LASSO, at −0.082. Decomposed models have *worse* out-of-sample $R^2$ than their standard counterparts.

**Economically, decomposition wins by a wide margin.** Under the Chinco et al. forecast-implied portfolio (invest \$1 per minute, trade only when predicted return exceeds the spread, hold one minute, no trading costs):

| | FPI¹ OLS | FPI¹ LASSO | FPID¹ | FPI¹⁰ | FPID¹⁰ |
|---|---|---|---|---|---|
| $M_3$ — PnL (bps) / SR | 0.22 / 1.24 | 0.59 / 2.17 | 1.01 / 4.26 | 0.54 / 2.09 | **1.66 / 6.90** |
| $M_7$ — PnL (bps) / SR | 0.68 / 5.86 | 1.26 / 5.22 | 2.42 / 10.65 | 1.33 / 5.18 | **3.15 / 13.51** |

The best model, FPID¹⁰ with $M_7$, returns 3.15 bps per dollar traded at a Sharpe of 13.51 — which the authors state is at least five times the figures reported by Cont et al. Longer lags help by a factor of two to three; extra book levels help only for the decomposed models.

## Which Component Matters

Consistently, across every level and every lag:

$$F(\text{adds}) > F(\text{cancels}) > F(\text{trades})$$

where $F$ is the LASSO selection frequency. In the contemporaneous PID¹⁰ model the add variables are selected roughly three times more often than the others. In the forecasting model the trade component is *rarely* selected at all, and best-level add OFI stands out well above every other group.

Two further observations from the forecasting model: longer lags contribute more than shorter ones, and **53% of regressions select no variable at all** — over half the predictions are just the in-sample mean.

This is the paper's most interesting result. Order submissions, not executions, carry the forecasting content. It points at order placement behaviour rather than trade flow as the object worth modelling.

## Limitations

- Trading costs are excluded; PnL is reported in basis points so the reader can subtract their own.
- Orders are assumed to fill immediately at mid.
- The 53% all-intercept regressions mean the headline Sharpe rests on a minority of active minutes.
- Statistical and economic verdicts point in opposite directions; the authors lean on Kelly et al. and Chinco et al. to argue negative $R^2$ is not disqualifying, but the tension is not resolved.
- Universal and clustered (cross-stock pooled) specifications were tested and are reported as no better than per-stock fitting, but those results are not shown.

## Related

- [[sources/cont-2023-cross-impact-ofi]] — the baseline this paper reproduces and extends, same data
- [[sources/xu-2020-mlofi]] — multi-level OFI, the other axis of extension
- [[concepts/order-flow-imbalance]], [[concepts/price-impact]], [[concepts/limit-order-book]]

## Citation

Sitaru, B., Calinescu, A., & Cucuringu, M. (2023). Order Flow Decomposition for Price Impact Analysis in Equity Limit Order Books. *Proceedings of the 4th ACM International Conference on AI in Finance (ICAIF '23)*, 637–645. doi:10.1145/3604237.3626874
<!-- AUTHORED REGION END -->