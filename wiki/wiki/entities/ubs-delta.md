---
title: UBS Delta
page_id: entities/ubs-delta
page_type: entity
entity_type: institution
revision_id: 1
created: 2026-05-05 23:25:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- creditETF
- risk-management
- portfolio-analytics
sources:
- sources/ubs-2012-next-gen-credit-curves
related:
- entities/lindsey-matthews
- entities/luca-bosatta
- concepts/hazard-rate-curve
schema_version: 2
uuid: ec460049-3143-58dc-a0ac-b3be38f89640
content_hash: sha256:d644e168541ae6abf5e7fead4c744997b0a368517d0656f9e3748c5e74068d57
---

<!-- AUTHORED REGION START -->
# UBS Delta

**UBS Delta** is UBS's portfolio analysis and risk management system. It provides institutional clients with tools for measuring and managing risk across asset classes.

## Capabilities

- Risk measures: sensitivities, deltas, Greeks, VaR, volatility, tracking error
- Full revaluation scenario analysis
- Solvency and shortfall risk
- Capital analytics
- Liquidity scoring
- Performance attribution
- Portfolio optimization

## D-Curves

UBS Delta's "D-Curves" represent their next-generation approach to credit curve calibration:

- **Unified hazard-rate curves** combining bonds and CDS across currencies
- **Market surfaces** for sector/rating combinations
- **[[concepts/market-implied-ratings|Market-implied ratings]]**
- Built daily for thousands of issuers

## Key Innovations

The D-Curves methodology addresses limitations of traditional spread-based approaches:

1. Higher correlation across currencies (>60% vs ~30%)
2. More robust and stable issuer curves
3. Consistent comparison of bonds and CDS
4. Reduced reliance on proxy curves

## Key Personnel

- [[entities/lindsey-matthews|Lindsey Matthews]] - Head of Client Development
- [[entities/luca-bosatta|Luca Bosatta]] - Head of Risk Modelling

## Awards

- Best Actuarial Software/Risk Engine - Insurance Risk 2012
- Best Broker-Supplied Tool/Technology - Buy-Side Technology Awards 2012

## Publications in This Wiki

- [[sources/ubs-2012-next-gen-credit-curves|Next-Generation Credit Curves (2012)]]

<!-- AUTHORED REGION END -->
