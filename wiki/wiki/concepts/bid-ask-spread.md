---
title: Bid-Ask Spread
page_id: concepts/bid-ask-spread
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- market-microstructure
- market-making
- liquidity
- transaction-costs
sources:
- sources/bergault-2019-multi-asset-market-making
- sources/guillaume-1997-stylized-facts-fx
related:
- concepts/market-making
- concepts/market-microstructure
- concepts/liquidity-risk
- concepts/avellaneda-stoikov-model
mind_map_priority: medium
schema_version: 2
uuid: 966ebb57-7455-593f-a382-47c52af3d64d
content_hash: sha256:238bd9c3db5eb5d81a030b17d174e3ade1b30806c16116b739ff6964fc8f5006
---

<!-- AUTHORED REGION START -->
# Bid-Ask Spread

The gap between the best price at which you can sell and the best price at which you can buy. It is simultaneously a dealer's revenue, a taker's cost, and a source of contamination in price data — and the wiki treats it under all three headings.

## As Revenue

Spread capture is the primary income of [[concepts/market-making|market making]]: buy at the bid, sell at the ask. The trade-off is stated plainly on that page — tight spreads mean more trades at smaller margin, wide spreads fewer trades at larger margin, and inventory limits affect how aggressively you can quote.

The [[concepts/avellaneda-stoikov-model|Avellaneda-Stoikov model]] makes the choice explicit. The optimal half-spread widens with risk aversion, with the absolute size of the inventory, and as the horizon shortens; quotes are skewed to unwind inventory rather than held symmetric. [[sources/bergault-2019-multi-asset-market-making|Bergault et al. (2019)]] extend the quoting problem to correlated multi-asset portfolios with closed-form approximations. See [[concepts/inventory-risk|Inventory Risk]] and [[concepts/stochastic-optimal-control|Stochastic Optimal Control]].

## As Cost

[[concepts/liquidity-risk|Liquidity Risk]] lists the spread first among market-liquidity components — the cost of immediate execution — alongside depth and resiliency. Two of its measures are spread-derived: the quoted spread directly, and the Roll measure, which backs out an implicit spread from price reversals.

Spreads are wider where transparency is lower. [[concepts/trade-classification|Trade Classification]] notes corporate bonds have larger spreads than equities, no pre-trade transparency, and lower trade frequency.

## As Contamination

This is the part that catches researchers. Transaction prices alternate between bid and ask, which injects artificial negative autocorrelation into returns — **bid-ask bounce**.

[[sources/guillaume-1997-stylized-facts-fx|Guillaume et al. (1997)]] record negative first-order autocorrelation from bid-ask bounce as a [[concepts/stylized-facts|stylized fact]] of high-frequency FX, and note the price process behaves distinctly below roughly 10-15 minutes, where quote arrival and spread dynamics become first-order effects.

[[concepts/market-microstructure-noise|Market Microstructure Noise]] shows what this does to results. Price-based signals from month t−1 are mechanically linked to month t returns, creating false predictability. After correcting for it, the corporate bond short-term reversal premium falls from 0.90% monthly to roughly zero — a drop of more than 90% — and credit-spread premia fall 50-65%.

## See Also

[[concepts/market-making|Market Making]] · [[concepts/market-microstructure|Market Microstructure]] · [[concepts/market-microstructure-noise|Market Microstructure Noise]] · [[concepts/liquidity-risk|Liquidity Risk]] · [[concepts/avellaneda-stoikov-model|Avellaneda-Stoikov Model]] · [[concepts/inventory-risk|Inventory Risk]] · [[concepts/limit-order-book|Limit Order Book]] · [[concepts/stylized-facts|Stylized Facts]] · [[concepts/trade-classification|Trade Classification]] · [[concepts/rfq-markets|RFQ Markets]]

[[concepts/order-flow|Order Flow]] · [[concepts/spread|Spread]]

**Not yet written:** `concepts/price-impact`

<!-- AUTHORED REGION END -->
