---
title: Market Making
page_id: concepts/market-making
page_type: concept
revision_id: 3
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- trading
- liquidity-provision
- bid-ask-spread
- inventory-risk
- optimal-control
- fx
- stochastic-control
sources:
- sources/ellersgaard-2018-hedge-tracking-lob
- sources/fermanian-2017-md2c-corporate-bonds
- sources/gueant-2019-particle-filtering-bonds
- sources/brigida-2019-trade-intensity-liquidity
- sources/lu-2018-market-making
- sources/avellaneda-2008-market-making
- sources/bergault-2019-multi-asset-market-making
- sources/barzykin-2020-algorithmic-fx-market-making
- sources/barzykin-2021-fx-dealer-tiers
- sources/barzykin-2022-multi-currency-inventory
- sources/barzykin-2024-precious-metals
- sources/barzykin-2025-adverse-selection
- sources/bergault-2023-rfq-pricing
- sources/cartea-2015-optimal-execution
- sources/lokin-2024-fill-probabilities
- sources/cartea-2025-statistical-predictions-trading
related:
- concepts/limit-order-book
- concepts/liquidity-risk
- concepts/inventory-risk
- concepts/adverse-selection
- concepts/optimal-execution
- concepts/avellaneda-stoikov-model
- concepts/internalization-externalization
- concepts/client-tiering
- entities/olivier-gueant
- entities/philippe-bergault
- entities/alexander-barzykin
- entities/alvaro-cartea
- entities/sebastian-jaimungal
mind_map_priority: high
schema_version: 2
uuid: 7dd918fa-2530-5e68-833a-604059707bbe
content_hash: sha256:354ef3d54da9b378e28b28ff02ea8ec589aeeae0ca32d9aee9a1f23ecd8c3384
---

<!-- AUTHORED REGION START -->
# Market Making

**Market making** is the practice of continuously providing buy and sell quotes for financial instruments, earning the bid-ask spread while managing inventory risk. Market makers play a crucial role in liquidity provision and price discovery.

## Core Economics

### Revenue Sources
- **Spread Capture:** Profit from buying at bid, selling at ask
- **Information Fees:** Payment for flow from brokers
- **Rebates:** Exchange rebates for liquidity provision

### Risk Exposures
- **Inventory Risk:** Holding positions as prices move
- **Adverse Selection:** Trading against informed traders
- **Operational Risk:** Technology failures, latency

### Trade-offs
- Tight spreads → more trades but smaller margin
- Wide spreads → fewer trades but larger margin
- Inventory limits affect quote aggressiveness

## Mathematical Framework

### Avellaneda-Stoikov Model
The foundational continuous-time optimal control model:
```
dS = σ dW  (mid-price dynamics)
dX = dN^b - dN^a  (inventory dynamics)
```

Optimal quotes minimize:
- Inventory risk (penalize large positions)
- Missed opportunities (cost of wide spreads)

### Key Results
- Optimal spread increases with inventory
- Quotes skewed toward reducing inventory
- Solution via HJB equation

### Extensions
- **Cartea-Jaimungal:** Risk metrics, alpha signals
- **Gueant et al.:** Closed-form solutions
- **Guilbaud-Pham:** Make-take fees

## Market Structures

### Limit Order Book Markets
- Quote competition via LOB
- Price-time priority
- [[sources/ellersgaard-2018-hedge-tracking-lob|Ellersgaard & Tegner (2018)]]: Optimal hedging in LOB

### Request-for-Quote (RFQ)
- Client requests price from multiple dealers
- Dealer competition on each RFQ
- [[sources/fermanian-2017-md2c-corporate-bonds|Fermanian et al. (2017)]]: Corporate bond RFQ modeling

### Voice/OTC
- Bilateral negotiation
- Relationship-based pricing
- Less transparent than electronic

## Practical Considerations

### HFT Market Making
- Sub-millisecond latency
- Sophisticated signal processing
- [[sources/brigida-2019-trade-intensity-liquidity|Brigida & Pratt (2019)]]: HFT liquidity provision patterns

### Traditional Market Making
- Designated market maker obligations
- Wider spreads, longer holding periods
- Focus on less liquid instruments

### Hybrid Approaches
- Electronic execution with human oversight
- Risk management automation
- Cross-asset hedging

## Mid-Price Estimation

For illiquid instruments, determining the "fair" mid-price is crucial:

### Challenges
- No continuous traded price
- Sparse, irregular transactions
- Bid-ask bounce in observed prices

### Methods
- **CBBT:** Bloomberg composite prices
- **Particle Filtering:** [[sources/gueant-2019-particle-filtering-bonds|Gueant & Pu (2019)]]
- **Statistical Models:** Cross-sectional calibration

## Inventory Management

### Classic Theories
- **Ho-Stoll (1981):** Inventory-based spread adjustment
- **Kyle (1985):** Information-based trading
- **Glosten-Milgrom (1985):** Adverse selection

### Modern Approaches
- **Stochastic Optimal Control:** HJB equations
- **Reinforcement Learning:** Data-driven policies
- **Cross-Asset Hedging:** Delta-hedging options

### Hedging via LOB
[[sources/ellersgaard-2018-hedge-tracking-lob|Ellersgaard & Tegner (2018)]]:
- Combine limit and market orders for hedging
- Limit orders: slow but cost-effective
- Market orders: fast but expensive
- HJB QVI formulation

## Adverse Selection

### Detection
- Trade clustering on one side
- Information in trade signs
- Post-trade price movement

### Mitigation
- Wider spreads for informed flow
- Faster quote updates
- Flow segmentation
- [[sources/brigida-2019-trade-intensity-liquidity|Brigida & Pratt (2019)]]: HFT withdraws after many trades

## Performance Metrics

### P&L Decomposition
- **Capture:** Realized spread revenue
- **Inventory Mark-to-Market:** Unrealized gains/losses
- **Hedging Costs:** Cost of risk reduction

### Risk Metrics
- VaR on inventory positions
- Drawdown limits
- Position aging

## FX Market Making

FX market making has distinct characteristics from exchange-traded markets:

### Internalization vs Externalization
A key decision unique to OTC dealers: whether to warehouse client flow (internalization) or hedge in the interbank market (externalization). [[sources/barzykin-2020-algorithmic-fx-market-making|Barzykin et al. (2020)]] formalized this as a stochastic control problem with:
- Continuous streaming quotes to clients
- Optional hedging in the external market
- Trade-off between spread revenue and inventory risk

See [[concepts/internalization-externalization|Internalization vs Externalization]] for details.

### Client Tiering
FX dealers segment clients by characteristics:
- **Informed vs uninformed flow**: Different adverse selection risk
- **Trade size patterns**: Volume and frequency
- **Relationship value**: Long-term profitability

[[sources/barzykin-2021-fx-dealer-tiers|Barzykin et al. (2021)]] developed optimal pricing across tiers using HSBC data. See [[concepts/client-tiering|Client Tiering]].

### Multi-Currency Inventory
Managing positions across correlated currency pairs:
- Cross-hedging using currency correlations
- Portfolio-level inventory constraints
- [[sources/barzykin-2022-multi-currency-inventory|Barzykin et al. (2022)]]: Closed-form solutions for multi-currency problems

### Multi-Asset Extensions
[[sources/bergault-2019-multi-asset-market-making|Bergault et al. (2019)]]:
- Closed-form approximations using Riccati equations
- Dimensionality reduction for practical implementation
- Monte-Carlo validation showing <10% approximation error

## RFQ Markets

Request-for-quote markets (corporate bonds, FX options):
- Client requests price from multiple dealers
- Winner's curse in competitive bidding
- [[sources/bergault-2023-rfq-pricing|Bergault et al. (2023)]]: RFQ pricing with liquidity dynamics
- [[sources/fermanian-2017-md2c-corporate-bonds|Fermanian et al. (2017)]]: Corporate bond dealer competition

## Optimal Execution Integration

Market making and optimal execution are related problems:
- [[sources/cartea-2015-optimal-execution|Cartea & Jaimungal (2015)]]: Mixing limit and market orders
- Fill probability modeling: [[sources/lokin-2024-fill-probabilities|Lokin & Yu (2024)]]
- Both involve inventory management and price impact

See [[concepts/optimal-execution|Optimal Execution]] for execution-focused approaches.

## See Also

- [[concepts/limit-order-book|Limit Order Book]]
- [[concepts/liquidity-risk|Liquidity Risk]]
- [[concepts/adverse-selection|Adverse Selection]]
- [[concepts/optimal-execution|Optimal Execution]]
- [[concepts/avellaneda-stoikov-model|Avellaneda-Stoikov Model]]
- [[concepts/internalization-externalization|Internalization vs Externalization]]
- [[concepts/client-tiering|Client Tiering]]
- [[concepts/inventory-risk|Inventory Risk]]
- [[entities/olivier-gueant|Olivier Guéant]]
- [[entities/philippe-bergault|Philippe Bergault]]
- [[entities/alexander-barzykin|Alexander Barzykin]]

## Empirical Behavioral Clustering of Market Makers

[[sources/cartea-2025-statistical-predictions-trading|Cartea et al. (2025)]] use Euronext Amsterdam regulatory data (with algorithm- and member-level identifiers) to identify that only about one-third of Liquidity Providers behave as market makers — the rest cluster into directional and opportunistic styles despite sharing a single dealing capacity.

<!-- AUTHORED REGION END -->
