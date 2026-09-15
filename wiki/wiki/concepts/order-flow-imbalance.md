---
content_hash: sha256:2643cbc049f23fde0255b3b1de0e05e7e55f36e30c196637f4aba7f3d0c44370
created: 2026-08-13 00:00:00+00:00
mind_map_priority: high
page_id: concepts/order-flow-imbalance
page_type: concept
related:
- concepts/order-imbalance
- concepts/order-flow
- concepts/price-impact
- concepts/cross-impact
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/square-root-law
revision_id: 1
schema_version: 2
sources:
- sources/cont-2023-cross-impact-ofi
- sources/sitaru-2023-decomposed-ofi
- sources/su-2021-generalized-ofi
- sources/hu-2025-ofi-csi300-ou
- sources/xu-2020-mlofi
tags:
- order-flow-imbalance
- market-microstructure
- limit-order-book
- price-impact
- order-flow
- high-frequency
title: Order Flow Imbalance
updated: '2026-08-13T00:00:00Z'
uuid: 8d68029b-1c56-5800-8e37-aeb82dbbff49
---

<!-- AUTHORED REGION START -->
# Order Flow Imbalance

A signed measure of net buying pressure built from changes in the [[concepts/limit-order-book|limit order book]] itself, rather than from trades. It is the workhorse variable of short-horizon equity price prediction, and its history is a sequence of arguments about what "net flow" should count.

## The Base Definition

For an order book event $n$ at level $\ell$, bid order flow rises when the bid price rises, or the bid price holds and the bid size grows — that is, whenever demand increases. Ask order flow is defined symmetrically for supply. OFI over $(t-h, t]$ is the sum of these signed contributions across every event in the interval.

Two things distinguish this from trade imbalance. It counts **limit order arrivals and cancellations, not just executions**, so it sees pressure that never trades. And it is a *flow* over an interval, not a state of the book.

Because limit order depth has a strong intraday pattern, OFI is normally scaled by average depth over the interval.

The construction is due to Cont, Kukanov & Stoikov (2014), who found best-level OFI explains roughly 65% of contemporaneous return variation.

## Four Generalisations

Everything since has extended OFI along one of four axes.

**Depth.** [[sources/xu-2020-mlofi|Xu, Gould & Howison (2020)]] replace the scalar with a **multi-level OFI** vector across the top levels of the book. Depth beyond the touch matters for price formation.

**Aggregation.** [[sources/cont-2023-cross-impact-ofi|Cont, Cucuringu & Zhang (2023)]] compress that vector into a scalar **integrated OFI** — the first principal component, which explains 89.06% of multi-level OFI variance. This raises contemporaneous $R^2$ from 71.16% to 87.14% in sample. A structural surprise: the *best level carries the smallest weight* in that component, and deeper levels get more weight for high-volume, low-volatility stocks.

**Event type.** [[sources/sitaru-2023-decomposed-ofi|Sitaru, Calinescu & Cucuringu (2023)]] split OFI into **add, cancel and trade** components, which sum back to standard OFI. This needs market-by-order data. It does not improve contemporaneous fit, but it roughly triples forecast-implied trading profit — and the component doing the work is *add*, not *trade*.

**Tick crossing.** [[sources/su-2021-generalized-ofi|Su et al. (2021)]] note that standard OFI assumes the best quote moves at most one tick between observations, which fails on three-second snapshot data. Their **generalized OFI** keys on the price *value* rather than its position, summing across every level traversed.

## Two Standing Results

**More levels help contemporaneously; they do not help forecasting.** Integrated OFI dominates best-level OFI for explaining same-interval returns, but gives no advantage at one-minute-ahead prediction. The suggested reason is that PCA discards which level a flow came from, and traders choose their level strategically.

**[[concepts/cross-impact|Cross-impact]] survives only where own-book information is incomplete.** Once a stock's own multi-level flow is properly integrated, other stocks' OFI adds nothing contemporaneously — cross-asset best-level OFI was largely a proxy for a stock's own deeper book. Cross-asset OFI does help *forecast*, and does matter at portfolio level.

## Relation to Impact Theory

OFI models are locally **linear**: return regressed on imbalance. Metaorder impact is **concave** — the [[concepts/square-root-law|square-root law]]. [[sources/maitrier-2026-square-root-impact-framework|Maitrier & Bouchaud]] argue these are consistent, with the linear aggregate relation emerging from overlapping square-root-impact [[concepts/metaorder|metaorders]], and predict a specific non-monotonic structure in the correlation between returns and volume-weighted imbalance.

## Practical Caveats

- Out-of-sample $R^2$ for *forecasting* is routinely **negative** in this literature even where trading PnL is strongly positive. Contemporaneous $R^2$ near 90% and forecasting $R^2$ near −0.1 describe the same variable at different tasks; they are not comparable numbers.
- The event-type decomposition triples the regressor count, and overfits severely under OLS.
- Data granularity constrains which variant is even computable: event data allows decomposition, snapshot data does not.

## Related

- Researchers: [[entities/rama-cont|Rama Cont]] · [[entities/mihai-cucuringu|Mihai Cucuringu]] · [[entities/chao-zhang|Chao Zhang]]
- [[concepts/order-imbalance]] — the broader family of imbalance measures
- [[concepts/order-flow]] — the underlying stream and its long memory
- [[concepts/price-impact]], [[concepts/cross-impact]], [[concepts/market-microstructure]]
<!-- AUTHORED REGION END -->