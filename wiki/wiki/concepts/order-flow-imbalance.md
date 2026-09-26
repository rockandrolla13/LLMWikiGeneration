---
content_hash: sha256:bb18d90b3ca67b7df2f6f411e658441ce0b927e0f7d36eb87879151591700848
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
revision_id: 2
schema_version: 2
sources:
- sources/cont-2014-price-impact-order-book-events
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
updated: '2026-09-25T21:37:03Z'
uuid: 8d68029b-1c56-5800-8e37-aeb82dbbff49
---

<!-- AUTHORED REGION START -->
# Order Flow Imbalance

A signed measure of net buying pressure built from changes in the [[concepts/limit-order-book|limit order book]] itself, rather than from trades. It is the workhorse variable of short-horizon equity price prediction, and its history is a sequence of arguments about what "net flow" should count.

## The Base Definition

For an order book event $n$ at level $\ell$, bid order flow rises when the bid price rises, or the bid price holds and the bid size grows — that is, whenever demand increases. Ask order flow is defined symmetrically for supply. OFI over $(t-h, t]$ is the sum of these signed contributions across every event in the interval.

Two things distinguish this from trade imbalance. It counts **limit order arrivals and cancellations, not just executions**, so it sees pressure that never trades. And it is a *flow* over an interval, not a state of the book.

Because limit order depth has a strong intraday pattern, OFI is normally scaled by average depth over the interval.

The construction is due to [[sources/cont-2014-price-impact-order-book-events|Cont, Kukanov & Stoikov (2014)]], who found best-level OFI explains roughly 65% of contemporaneous return variation.

## What the Founding Paper Established

Four results from the 2014 paper are the base the rest of the page builds on.

**Impact is linear.** On 50 randomly chosen S&P 500 stocks over April 2010, ten-second mid-price changes regressed on best-level OFI give an average $R^2$ of 65%. A quadratic term adds three points and is insignificant. The fit rises as the interval lengthens and the finding is unchanged from half a second to ten minutes.

**The slope is inverse to depth.** The price impact coefficient $\beta_i$ in each half-hour window scales as $c / AD_i^{\lambda}$, where $AD_i$ is the average best-quote depth. $\lambda = 1$ cannot be rejected for 35 of the 50 stocks. This is what a stylised book with constant depth predicts, and it turns intraday patterns in impact and volatility into a consequence of the known intraday pattern in depth: impact is about twice its average at the open, where depth is half its average.

**Trades are already inside OFI.** Trade imbalance explains 32% of the same variation, and becomes insignificant once OFI is in the regression.

**The square-root price–volume relation is an aggregation artefact.** If prices follow OFI linearly and events are i.i.d., the central limit theorem makes OFI scale as the square root of event count while volume scales linearly with it, so a noisy square-root dependence of price change on volume emerges with a *random* slope. Volume drops out of the regression once $|\text{OFI}|$ is included.

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

OFI models are locally **linear**: return regressed on imbalance. Metaorder impact is **concave** — the [[concepts/square-root-law|square-root law]]. The founding paper already had a version of this tension, and resolved it in its own terms: a square-root relation between price change and *volume* over fixed intervals follows from linear OFI impact by a scaling argument, with a slope that is a fresh random draw each interval. That is a statement about interval aggregation, not about metaorders, so it does not by itself settle the metaorder question. [[sources/maitrier-2026-square-root-impact-framework|Maitrier & Bouchaud]] argue these are consistent, with the linear aggregate relation emerging from overlapping square-root-impact [[concepts/metaorder|metaorders]], and predict a specific non-monotonic structure in the correlation between returns and volume-weighted imbalance.

## Practical Caveats

- Out-of-sample $R^2$ for *forecasting* is routinely **negative** in this literature even where trading PnL is strongly positive. Contemporaneous $R^2$ near 90% and forecasting $R^2$ near −0.1 describe the same variable at different tasks; they are not comparable numbers.
- The event-type decomposition triples the regressor count, and overfits severely under OLS.
- Data granularity constrains which variant is even computable: event data allows decomposition, snapshot data does not.

## Related

- Researchers: [[entities/rama-cont|Rama Cont]] · [[entities/arseniy-kukanov|Arseniy Kukanov]] · [[entities/sasha-stoikov|Sasha Stoikov]] · [[entities/mihai-cucuringu|Mihai Cucuringu]] · [[entities/chao-zhang|Chao Zhang]]
- [[concepts/order-imbalance]] — the broader family of imbalance measures
- [[concepts/order-flow]] — the underlying stream and its long memory
- [[concepts/price-impact]], [[concepts/cross-impact]], [[concepts/market-microstructure]]
<!-- AUTHORED REGION END -->