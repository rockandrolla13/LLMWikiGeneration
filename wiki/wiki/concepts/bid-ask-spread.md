---
content_hash: sha256:238bd9c3db5eb5d81a030b17d174e3ade1b30806c16116b739ff6964fc8f5006
created: 2026-08-06 00:00:00+00:00
mind_map_priority: medium
page_id: concepts/bid-ask-spread
page_type: concept
related:
- concepts/market-making
- concepts/market-microstructure
- concepts/liquidity-risk
- concepts/avellaneda-stoikov-model
revision_id: 1
schema_version: 2
sources:
- sources/bergault-2019-multi-asset-market-making
- sources/guillaume-1997-stylized-facts-fx
- sources/abdulkarim-2019-topics-market-microstructure
- sources/bakhach-2018-developing-trading-strategies-under-directional-changes
- sources/besson-2016-cross-or-not-cross-spread-that
- sources/bieganowski-2026-explainable-patterns-cryptocurrency-microstructure
- sources/bonart-2018-continuous-efficient-fundamental-price-discrete-order
- sources/calcada-2016-microstructural-changes-befor-macroeconomic-announcements-predictability
- sources/dahlhaus-2013-online-spot-volatility-estimation-decomposition-nonlinear
- sources/das-2026-predicting-stock-price-movements-high-frequency
- sources/deep-2025-binary-tree-option-pricing-under-market
- sources/dsouza-2003-empirical-analysis-liquidity-order-flow-brokered
- sources/eisler-2007-limit-order-book-different-time-scales
- sources/eisler-2011-price-impact-order-book-events-market
- sources/fabre-2025-learning-spoofability-limit-order-books-interpretable
- sources/ferreruela-2025-informed-trading-investor-beliefs-consensus-volatility
- sources/george-2025-deep-reinforcement-learning-trading-strategy-development
- sources/ginebri-2008-order-dynamics-italian-treasury-security-wholesale
- sources/glattfelder-2010-patterns-high-frequency-fx-data-discovery
- sources/hanke-2015-order-flow-imbalance-effects-german-stock
- sources/hiremath-2026-early-detection-latent-microstructure-regimes-limit
- sources/hirnschall-2020-deep-learning-approach-analyzing-limit-order
- sources/jeon-2026-when-does-order-flow-matter-state
- sources/jiang-2015-volume-synchronized-probability-informed-trading-vpin
- sources/kang-2019-flow-toxicity-highfrequency-trading-its-impact
- sources/karyampas-2011-probability-informed-trading-volatility-etf
- sources/kong-2025-volatility-estimation-agricultural-futures-markets-microstructure
- sources/liu-2025-reproducible-baseline-forecasting-high-frequency-realized
- sources/lu-2009-essays-behavioral-finance-market-microstructure
- sources/luo-2011-profitable-opportunities-around-macroeconomic-announcements-u
- sources/mucciante-2023-estimation-order-book-dependent-hawkes-process
- sources/qin-2026-polymarket-v1-database
- sources/rao-2024-hybrid-lstm-knn-framework-detecting-market
- sources/rola-2025-boltzmann-price-toward-understanding-fair-price
- sources/scaillet-2017-high-frequency-jump-analysis-bitcoin-market
- sources/sfendourakis-2020-lob-modeling-hawkes-processes-state-dependent
- sources/stoikov-2016-reducing-transaction-costs-low-latency-trading
- sources/takahashi-2025-returns-order-flow-imbalances-intraday-dynamics
- sources/valenzuela-2015-relative-liquidity-future-volatility
- sources/vlasiuk-2025-push-response-anomalies-high-frequency-s
- sources/wang-2012-order-imbalance-liquidity-returns-us-treasury-market
- sources/wang-2025-forecasting-liquidity-withdraw-machine-learning-models
- sources/wu-2012-information-content-euro-bund-futures-options
tags:
- market-microstructure
- market-making
- liquidity
- transaction-costs
title: Bid-Ask Spread
updated: '2026-09-27T01:47:00Z'
uuid: 966ebb57-7455-593f-a382-47c52af3d64d
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