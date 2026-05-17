---
title: "Client Tiering"
page_id: concepts/client-tiering
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [market-making, fx, pricing, client-segmentation, adverse-selection]
sources: [sources/barzykin-2021-fx-dealer-tiers, sources/barzykin-2020-algorithmic-fx-market-making]
related: [concepts/market-making, concepts/adverse-selection, concepts/internalization-externalization, entities/alexander-barzykin, entities/olivier-gueant, entities/philippe-bergault]
---

# Client Tiering

## Overview

**Client tiering** is the practice of segmenting clients into distinct groups and applying differentiated pricing strategies to each tier. In FX and OTC market making, this enables optimal balance between profitability, risk management, and client relationships.

## Motivation

### Why Tier Clients?
1. **Adverse Selection**: Different clients have different informativeness
2. **Profitability**: Some flow is more valuable than others
3. **Risk**: Certain clients create more inventory risk
4. **Relationship**: Long-term value varies by client type

### Trade-offs
- Aggressive pricing for "good" flow → more volume but lower margin
- Wide spreads for "toxic" flow → less adverse selection but may lose client
- Uniform pricing → simpler but suboptimal

## Tiering Framework

### [[sources/barzykin-2021-fx-dealer-tiers|Barzykin et al. (2021)]] Model

**Tier-Specific Order Arrival:**
$$\lambda_t^{n,b/a}(\delta^n) = \Lambda^n(Z_t) e^{-k^n \delta^n}$$

where:
- $n$ = tier index
- $\Lambda^n$ = baseline intensity for tier $n$
- $k^n$ = price sensitivity for tier $n$
- $Z_t$ = market regime

**Tier-Specific Spreads:**
Each tier receives customized quotes:
$$\delta^{n,b/a*}(q) = \text{base spread} + \text{inventory adjustment} + \text{tier premium}$$

## Empirical Identification

### K-Means Clustering
From HSBC FX streaming data:

**Features Used:**
- Average trade size
- Trade frequency
- Fill rate (acceptance of quotes)
- Post-trade price movement

**Results:**
Identified 3 primary clusters:
| Tier | Size | Frequency | Informativeness |
|------|------|-----------|-----------------|
| 1 | Small | High | Low |
| 2 | Medium | Medium | Medium |
| 3 | Large | Low | High |

### Validation
- Tiers show distinct post-trade price behavior
- Tier 3 (informed): Significant price movement in trade direction
- Tier 1 (uninformed): Near-zero expected impact

## Optimal Pricing by Tier

### Uninformed Tiers (Retail, Corporate)
- Tighter spreads to capture flow
- Higher [[concepts/internalization-externalization|internalization]] rate
- Lower adverse selection cost

### Informed Tiers (Institutional, Algo)
- Wider spreads to compensate for information
- Higher externalization rate
- May use last look protection

### Relationship Pricing
- Consider lifetime value, not just per-trade profit
- Cross-sell opportunities
- Pricing ladders (volume discounts)

## Mathematical Results

### Value Function Decomposition
Total value splits across tiers:
$$V(t, q, z) = \sum_n V^n(t, q, z)$$

Each tier contributes independently when arrival processes are independent.

### Closed-Form Approximations
For single-tier model, optimal spread:
$$\delta^*(q) = \frac{1}{k} + \gamma \sigma^2 (T-t) |q|$$

Extended to multiple tiers with tier-specific $k^n$.

## Practical Implementation

### Data Requirements
- Client identity mapping
- Historical trade data
- Fill rate tracking
- P&L attribution by client

### System Architecture
1. Client classification engine
2. Real-time tier lookup
3. Tier-specific pricing engine
4. Performance monitoring

### Challenges
- Client behavior changes over time
- Gaming: clients optimize for better tier
- Regulatory constraints on discrimination

## Extensions

### Size Tiering
[[sources/barzykin-2021-fx-dealer-tiers]] also considers size tiers:
- Small, medium, large trades
- Different price sensitivity per size
- Interaction with client tiers

### Dynamic Tiering
- Real-time informativeness estimation
- Regime-dependent tier behavior
- Machine learning for classification

### Multi-Asset Tiering
- Cross-asset client behavior
- Portfolio-level relationship value
- Correlation of client flow across products

## Industry Practice

### FX Dealers
- Most major dealers implement tiering
- Typically 3-5 tiers
- Automated via API pricing rules

### Pricing Ladders
Volume-based discounts within tiers:
| Volume Band | Spread |
|-------------|--------|
| < $1M | 3 pips |
| $1M - $10M | 2 pips |
| > $10M | 1.5 pips |

## See Also

- [[concepts/market-making|Market Making]]
- [[concepts/adverse-selection|Adverse Selection]]
- [[concepts/internalization-externalization|Internalization vs Externalization]]
- [[entities/alexander-barzykin|Alexander Barzykin]]
- [[sources/barzykin-2021-fx-dealer-tiers|Barzykin et al. (2021)]]
