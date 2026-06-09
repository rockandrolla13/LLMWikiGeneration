---
created: 2026-04-25 22:00:00+00:00
mind_map_priority: medium
page_id: concepts/liquidity-risk
page_type: concept
related:
- concepts/bond-capm
- concepts/capital-structure-arbitrage
- concepts/corporate-bond-liquidity-premium
- concepts/corporate-bonds
- concepts/credit-default-swap-spread
- concepts/credit-spread-curve
- concepts/default-rates
- concepts/factor-models
- concepts/illiquidity-premium
- concepts/limits-to-arbitrage
- concepts/liquidity-scoring-mechanism
- concepts/market-crash-liquidity-crisis
- concepts/private-credit
- concepts/risk-premia
- concepts/statistical-arbitrage
- concepts/term-structure-risk-premium
revision_id: 4
sources:
- sources/coppola-2025-asset-class-liquidity-indicators
- sources/dickerson-2023-bond-risk
- sources/kapadia-2012-limited-arbitrage-equity-credit
- sources/ms-2016-03-22-xccy-basis-primer
- sources/ms-2019-03-04-a-premium-for-size
tags:
- fixed-income
- risk-management
- market-microstructure
- trading
title: Liquidity Risk
updated: '2026-06-09T12:00:00Z'
---

# Liquidity Risk

Liquidity risk is the risk that an investor cannot buy or sell an asset quickly enough at a fair price, or that doing so will significantly impact the market price.

## Components

### Market Liquidity Risk
- **Bid-ask spread**: Cost of immediate execution
- **Market depth**: Size that can be traded without price impact
- **Resiliency**: Speed at which prices recover after large trades

### Funding Liquidity Risk
- Ability to meet margin calls or redemptions
- Cost of financing positions
- Rollover risk for short-term funding

## Measurement in Corporate Bonds

| Measure | Description |
|---------|-------------|
| Bid-ask spread | Direct transaction cost |
| Trading volume | Market activity indicator |
| Amihud measure | Price impact per unit volume |
| Roll measure | Implicit spread from price reversals |
| Age | Time since issuance (proxy) |

## Liquidity Premium in Bonds

Investors require compensation for holding illiquid bonds:
- Estimated at 50-100 bps for investment grade
- Higher for high yield (100-300 bps)
- Time-varying: spikes during crises

## Corporate Bond Specifics

Corporate bonds are particularly illiquid because:
- **Many issues**: Thousands of bonds vs. single equity
- **Dealer market**: No central exchange
- **Inventory costs**: Dealers face capital constraints
- **Credit cliff risk**: Downgrades trigger forced selling

## See Also

- [[concepts/bond-capm|Bond CAPM]]
- [[concepts/factor-models|Factor Models]]
- [[concepts/credit-spread-curve|Credit Spread Curve]]
- [[sources/dickerson-2023-bond-risk|Corporate Bond Risk Factor Pricing (2023)]]
- [[sources/coppola-2025-asset-class-liquidity-indicators|Coppola, Urga & Varaldo (2025) Asset Class Liquidity Risk Indicators]] — endogenous Markov-switching liquidity regimes across European/US equity and bond markets with funding-vs-market liquidity decomposition

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/kapadia-2012-limited-arbitrage-equity-credit]]

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/ms-2016-03-22-xccy-basis-primer]], [[sources/ms-2019-03-04-a-premium-for-size]]