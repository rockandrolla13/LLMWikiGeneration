---
title: "Olivier Guéant"
page_id: entities/olivier-gueant
page_type: entity
entity_type: person
revision_id: 2
created: 2026-04-25T22:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [researcher, market-making, optimal-execution, mathematical-finance, stochastic-control, fx]
sources: [sources/fermanian-2017-md2c-corporate-bonds, sources/gueant-2019-particle-filtering-bonds, sources/bergault-2019-multi-asset-market-making, sources/barzykin-2020-algorithmic-fx-market-making, sources/barzykin-2021-fx-dealer-tiers, sources/barzykin-2022-multi-currency-inventory, sources/barzykin-2024-precious-metals, sources/barzykin-2025-adverse-selection, sources/bergault-2023-rfq-pricing]
related: [concepts/market-making, concepts/optimal-execution, concepts/inventory-risk, concepts/internalization-externalization, concepts/avellaneda-stoikov-model, entities/philippe-bergault, entities/alexander-barzykin]
mind_map_priority: high
---

# Olivier Guéant

**Olivier Guéant** is a French applied mathematician and quantitative finance researcher specializing in market microstructure, optimal execution, and market making. He is a leading figure in the mathematical theory of market making and algorithmic trading, with particular expertise in stochastic optimal control applications to financial markets.

## Affiliation

- Université Paris 1 Panthéon-Sorbonne
- Centre d'Économie de la Sorbonne (CES)
- Institut Europlace de Finance

## Research Focus

### Market Making
- Optimal quote placement in limit order books and OTC markets
- [[concepts/inventory-risk|Inventory risk]] management
- Closed-form solutions for market making problems
- [[concepts/internalization-externalization|Internalization vs externalization]] decisions in FX markets
- Multi-asset and multi-currency market making

### FX Market Making
Extensive collaboration with [[entities/alexander-barzykin|Alexander Barzykin]] (HSBC) on practical FX market making:
- Active market making with internalization/externalization decisions
- Client tiering and differentiated pricing
- Multi-currency inventory management
- Precious metals market making

### Optimal Execution
- Minimizing market impact
- Portfolio liquidation
- Transaction cost analysis
- Mixed limit and market order strategies

### Corporate Bond Markets
- Multi-dealer-to-client (MD2C) platforms
- Request-for-quote (RFQ) modeling
- Mid-price estimation for illiquid bonds

## Key Contributions

### Mathematical Market Making
Developed closed-form solutions for the [[concepts/avellaneda-stoikov-model|Avellaneda-Stoikov]] market making model, making the theory practically applicable. His work extends the framework to include:
- Make-take fee structures
- Alpha signal integration
- Multiple asset market making with dimensionality reduction

### FX Market Making Framework
Built the modern theoretical framework for FX dealer market making:
- [[sources/barzykin-2020-algorithmic-fx-market-making]]: Introduced internalization-externalization dilemma
- [[sources/barzykin-2021-fx-dealer-tiers]]: Client tiering with empirical validation
- [[sources/barzykin-2022-multi-currency-inventory]]: Multi-currency inventory optimization
- [[sources/barzykin-2024-precious-metals]]: Extension to cointegrated precious metals
- [[sources/barzykin-2025-adverse-selection]]: Adverse selection and price reading

### Multi-Asset Market Making
[[sources/bergault-2019-multi-asset-market-making]]:
- Closed-form approximations using Riccati equations
- Dimensionality reduction for practical implementation
- Monte-Carlo validation of approximations

### RFQ Market Analysis
- [[sources/fermanian-2017-md2c-corporate-bonds]]: Dealer competition modeling
- [[sources/bergault-2023-rfq-pricing]]: RFQ pricing and liquidity dynamics

### Particle Filtering for Bonds
[[sources/gueant-2019-particle-filtering-bonds]]:
- Novel application of SMC to illiquid bond markets
- Handles censored RFQ observations
- Real-time mid-price distribution estimation

## Publications

### Books
- **"The Financial Mathematics of Market Liquidity: From Optimal Execution to Market Making"** (CRC Press, 2016) - Foundational textbook widely used in graduate programs

### Papers in This Wiki
- [[sources/bergault-2019-multi-asset-market-making]] - Multi-asset closed-form approximations
- [[sources/barzykin-2020-algorithmic-fx-market-making]] - Active FX market making
- [[sources/barzykin-2021-fx-dealer-tiers]] - Client tiering and hedging
- [[sources/barzykin-2022-multi-currency-inventory]] - Multi-currency inventory
- [[sources/barzykin-2024-precious-metals]] - Precious metals market making
- [[sources/barzykin-2025-adverse-selection]] - Adverse selection and price reading
- [[sources/bergault-2023-rfq-pricing]] - RFQ pricing dynamics
- [[sources/fermanian-2017-md2c-corporate-bonds]] - Corporate bond RFQ
- [[sources/gueant-2019-particle-filtering-bonds]] - Particle filtering for bonds

## Collaborations

Key collaborators:
- [[entities/philippe-bergault]] - Mathematical foundations and multi-asset extensions
- [[entities/alexander-barzykin]] - Industry collaboration on FX applications (HSBC)

## Influence

Guéant's work bridges:
- **Theory:** Rigorous stochastic control and HJB equation solutions
- **Practice:** Closed-form approximations implementable on trading desks
- **Industry:** Research supported by major banks (BNP Paribas, HSBC)

His textbook is widely used in graduate programs and by practitioners implementing algorithmic trading strategies. The FX market making framework developed with Barzykin represents a direct bridge between academic theory and real-world dealer operations.

## Contact

- Institution: Université Paris 1 Panthéon-Sorbonne, Centre d'Économie de la Sorbonne, 106-112 Boulevard de l'Hôpital, 75647 Paris Cedex 13, France

## See Also

- [[concepts/market-making|Market Making]]
- [[concepts/optimal-execution|Optimal Execution]]
- [[concepts/inventory-risk|Inventory Risk]]
- [[concepts/avellaneda-stoikov-model|Avellaneda-Stoikov Model]]
- [[concepts/internalization-externalization|Internalization vs Externalization]]
