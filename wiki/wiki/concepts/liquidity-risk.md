---
title: "Liquidity Risk"
page_id: concepts/liquidity-risk
page_type: concept
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
tags: [fixed-income, risk-management, market-microstructure, trading]
sources: [sources/dickerson-2023-bond-risk]
related: [concepts/bond-capm, concepts/factor-models, concepts/credit-spread-curve]
mind_map_priority: medium
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
