---
title: Internalization vs Externalization
page_id: concepts/internalization-externalization
page_type: concept
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- market-making
- fx
- hedging
- inventory-risk
- otc-markets
sources:
- sources/barzykin-2020-algorithmic-fx-market-making
- sources/barzykin-2021-fx-dealer-tiers
- sources/barzykin-2022-multi-currency-inventory
related:
- concepts/market-making
- concepts/inventory-risk
- concepts/client-tiering
- entities/olivier-gueant
- entities/alexander-barzykin
- entities/philippe-bergault
schema_version: 2
uuid: 16546392-b420-561a-b280-bae4219dc4dc
content_hash: sha256:903776cc78fc193ec9889a81a33cffd482aee1bb2744237da65b1c89a8657672
---

<!-- AUTHORED REGION START -->
# Internalization vs Externalization

## Overview

**Internalization vs externalization** is the fundamental dilemma facing FX and OTC market makers: whether to warehouse client flow on the balance sheet (internalization) or immediately hedge in the external market (externalization).

This concept was formalized by [[entities/alexander-barzykin|Barzykin]], [[entities/philippe-bergault|Bergault]], and [[entities/olivier-gueant|Guéant]] in [[sources/barzykin-2020-algorithmic-fx-market-making|their 2020 paper]].

## The Dilemma

### Internalization (Warehousing)
**Definition:** Hold client trades on the book without hedging

**Advantages:**
- Keep full bid-ask spread as profit
- Natural netting: opposite client flows offset
- No external transaction costs

**Disadvantages:**
- [[concepts/inventory-risk|Inventory risk]] from price movements
- Concentration risk if flow is directional
- Capital charges on positions

### Externalization (Hedging)
**Definition:** Immediately hedge client trades in the interbank market

**Advantages:**
- Eliminate inventory risk
- Lock in spread profit
- Reduce capital requirements

**Disadvantages:**
- Pay external spread (reduces profit)
- Information leakage to market
- May not get full fill in size

## Mathematical Framework

### Model Setup ([[sources/barzykin-2020-algorithmic-fx-market-making]])

**Client Flow:**
Markov-modulated Poisson process with intensities:
$$\lambda_t^{b/a} = \Lambda(Z_t) e^{-k\delta_t^{b/a}}$$

where $Z_t$ = market regime (hidden state).

**Externalization Control:**
Choose externalization rate $\nu_t \in [0, \bar{\nu}]$:
- $\nu_t = 0$: Pure internalization
- $\nu_t = \bar{\nu}$: Maximum externalization

**Objective:**
$$\sup_{\delta, \nu} \mathbb{E}\left[X_T + q_T S_T - \phi \int_0^T q_t^2 dt\right]$$

### Key Results

**Pure Internalization Zone:**
There exists an inventory threshold below which externalization is never optimal:
$$|q| < q^* \implies \nu^* = 0$$

This captures natural netting benefits for small positions.

**Optimal Externalization:**
When inventory exceeds threshold:
$$\nu^*(q) = \bar{\nu} \cdot \mathbf{1}_{|q| > q^*}$$

The bang-bang structure means partial hedging is never optimal.

## Practical Implications

### Inventory Management
- Build inventory during low-volatility periods (internalize)
- Hedge aggressively during high-volatility regimes (externalize)
- Monitor netting ratios to calibrate thresholds

### Client Segmentation
Different internalization strategies by client type:
- Retail flow: High internalization (random, netable)
- Institutional flow: Higher externalization (informed, directional)
- See [[concepts/client-tiering|Client Tiering]]

### Multi-Currency Extension
[[sources/barzykin-2022-multi-currency-inventory]]:
- Cross-currency natural hedges
- Portfolio-level externalization decisions
- Correlation-aware inventory limits

## Industry Practice

### FX Dealers
Major FX dealers (HSBC, Citi, JPM) internalize substantial fractions:
- Estimated 60-80% internalization rates
- Higher for spot, lower for forwards
- Depends on market conditions

### Last Look
Related practice where dealers can reject trades:
- Reduces adverse selection risk
- Affects optimal internalization strategy
- Regulatory scrutiny increasing

## Extensions

### Precious Metals
[[sources/barzykin-2024-precious-metals]]:
- Gold/silver cointegration for hedging
- "Precious metal carry trade" via inventory
- Asymmetric internalization across metals

### Adverse Selection
[[sources/barzykin-2025-adverse-selection]]:
- Client informativeness affects optimal strategy
- Price reading by clients reduces internalization benefit
- First-order corrections to basic model

## See Also

- [[concepts/market-making|Market Making]]
- [[concepts/inventory-risk|Inventory Risk]]
- [[concepts/client-tiering|Client Tiering]]
- [[entities/alexander-barzykin|Alexander Barzykin]]
- [[entities/olivier-gueant|Olivier Guéant]]
- [[sources/barzykin-2020-algorithmic-fx-market-making|Barzykin et al. (2020)]]

<!-- AUTHORED REGION END -->
