---
title: "Adverse Selection"
page_id: concepts/adverse-selection
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [market-making, information-asymmetry, trading, market-microstructure]
sources: [sources/barzykin-2025-adverse-selection, sources/barzykin-2021-fx-dealer-tiers]
related: [concepts/market-making, concepts/inventory-risk, concepts/client-tiering, concepts/limit-order-book, entities/olivier-gueant]
---

# Adverse Selection

## Overview

**Adverse selection** in market making refers to the risk of trading against counterparties with superior information. When an informed trader hits a market maker's quote, the trade is likely to be followed by a price move against the market maker's new position.

## The Winner's Curse

### Mechanism
1. Informed trader knows price will rise
2. Hits market maker's ask (buys from MM)
3. Price rises, MM is now short at a loss
4. MM "won" the trade but lost money

### Consequence
Market makers widen spreads to compensate for:
- Expected loss to informed traders
- Uncertainty about counterparty type
- Information in order flow

## Detecting Informed Flow

### Trade-Level Signals
- Trade size (larger → more likely informed)
- Time of day (around news releases)
- Counterparty identity (known institutions)

### Flow-Level Patterns
- Persistent directional flow
- Clustering before announcements
- Correlation with future price moves

### Post-Trade Price Movement
Key metric: price change $\tau$ seconds after trade
- Positive (in trade direction) → informed
- Zero/negative → uninformed

## Mathematical Models

### Glosten-Milgrom (1985)
Bayesian updating on trader type:
$$P(\text{informed} | \text{buy}) = \frac{P(\text{buy} | \text{informed}) \cdot P(\text{informed})}{P(\text{buy})}$$

Spread compensates for expected information content.

### Kyle (1985)
Informed trader chooses order size:
- Trades gradually to hide information
- Price impact reveals information over time
- Equilibrium: linear price impact

### Modern Extensions
[[sources/barzykin-2025-adverse-selection|Barzykin et al. (2025)]]:

**Price Jump from Informed Trades:**
$$dS_t = \sigma dB_t + \sum_{n,k} \tilde{\zeta}^{n,k}(\delta_t^{n,k,b/a})\Delta^k dN_t^{n,k,b/a}$$

where:
- $\tilde{\zeta}^{n,k}$ = adverse selection impact by tier $n$ and size $k$
- Different client tiers have different informativeness

## Client Tiering and Adverse Selection

[[sources/barzykin-2021-fx-dealer-tiers]] segments clients by:

### Tier Characteristics
| Tier | Size | Frequency | Informativeness |
|------|------|-----------|-----------------|
| 1 (Retail) | Small | High | Low |
| 2 (Corporate) | Medium | Medium | Low |
| 3 (Institutional) | Large | Low | High |
| 4 (Algo/HF) | Variable | High | Very High |

### Optimal Response
- Widen spreads for high-informativeness tiers
- Volume discounts for uninformed flow
- Relationship pricing for long-term value

## Price Reading (Skew Sniffing)

[[sources/barzykin-2025-adverse-selection]] introduces a related risk:

### Mechanism
1. Market maker skews quotes based on inventory
2. Sophisticated traders observe skew
3. Infer MM's inventory position
4. Trade against the MM strategically

### Model Extension
Additional price drift from quote observation:
$$dS_t += \tilde{J}^n(\text{skew}_t^n) dt$$

### Mitigation
- Reduce quote skewing
- Add noise to quotes
- Segment information by client

## Practical Implications

### Spread Setting
- Base spread + adverse selection premium
- Tier-specific adjustments
- Time-varying based on market conditions

### Flow Segmentation
- Route informed flow to external market
- Internalize uninformed flow
- See [[concepts/internalization-externalization|Internalization vs Externalization]]

### Last Look
- Reject trades from suspected informed flow
- Regulatory and reputational considerations
- Trade-off with client relationships

## Empirical Evidence

### FX Markets
From [[sources/barzykin-2021-fx-dealer-tiers]] (HSBC data):
- Clear clustering of client behavior
- K-means identifies 3+ distinct tiers
- Tier assignment predicts post-trade price moves

### Equity Markets
- Market makers adjust quotes faster for institutional flow
- Spread widening around earnings
- Flow toxicity metrics (VPIN)

## See Also

- [[concepts/market-making|Market Making]]
- [[concepts/client-tiering|Client Tiering]]
- [[concepts/inventory-risk|Inventory Risk]]
- [[concepts/internalization-externalization|Internalization vs Externalization]]
- [[sources/barzykin-2025-adverse-selection|Barzykin et al. (2025)]]
- [[sources/barzykin-2021-fx-dealer-tiers|Barzykin et al. (2021)]]
