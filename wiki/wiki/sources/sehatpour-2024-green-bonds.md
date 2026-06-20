---
title: Anatomy of Municipal Green Bond Yield Spreads
page_id: sources/sehatpour-2024-green-bonds
page_type: source
source_type: working-paper
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Mohammad Hadi Sehatpour
- Marta Campi
- Christina S. Nikitopoulos
- Gareth W. Peters
- Kylie-Anne Richards
year: 2024
venue: SSRN Working Paper
tags:
- green-bonds
- municipal-bonds
- yield-spreads
- association-rule-learning
- sustainable-finance
- machine-learning
related:
- sources/martin-2024-credit-curve
- concepts/green-bond-spreads
- concepts/association-rule-learning
- concepts/yield-to-maturity
- entities/gareth-peters
- entities/christina-nikitopoulos
mind_map_priority: high
schema_version: 2
uuid: 1cd009f2-30f7-5f93-b671-e5dfd6137234
content_hash: sha256:cb6aa7deda144c2c0d62a65365c9bd89450ed253d5d4922835fb025ca23e2ab1
---

<!-- AUTHORED REGION START -->
# Anatomy of Municipal Green Bond Yield Spreads

**Authors:** Mohammad Hadi Sehatpour, Marta Campi, [[entities/christina-nikitopoulos|Christina S. Nikitopoulos]], [[entities/gareth-peters|Gareth W. Peters]], Kylie-Anne Richards

**Year:** 2024

**Venue:** SSRN Working Paper

**Institutions:** UTS, Institut Pasteur, UC Santa Barbara, Future Fund

## Summary

Proposes novel approaches for computing [[concepts/green-bond-spreads|green bond spreads]] based on yields to maturity and their term structure, using [[concepts/association-rule-learning|Association Rule Learning]] to identify structuring attributes in California's municipal green bond market.

## Motivation

- Green bond market reached $3.2 trillion by mid-2024
- Supply-demand imbalance; most issuances oversubscribed
- Current matching designs have limitations (illiquidity, limited comparables)
- Need bond-specific spread measures for screening

## Key Contributions

### 1. Two Novel Spread Measures

**Tenor-Specific Approach (S¹):**
- Uses YTM to discount cash flows
- Compares green ZCBYTM with reference ZCBYTM at matching tenor
- Single point on yield curve

**Yield Curve Approach (S²):**
- Bootstrapped green curve vs. reference curve
- Varying discount rates by tenor
- Captures term structure information

### 2. Empirical Findings

**Spread Dynamics:**
- Both spreads positive and disparate early in sample
- Become negative and converge after 2022
- Reflects evolving green credit risk perception

### 3. Association Rule Learning Analysis

**Research Questions:**
1. Primary attributes associated with positive/negative spreads
2. Attributes for extreme spreads
3. Temporal consistency of spread attributes
4. Impact of nested/conditional associations
5. Term structure information in spread attributes

**Key Associations:**

*Positive Spreads:*
- Tax status (tax-exempt)
- Pricing strategy (premium)
- Self-reported green status
- High maturity

*Negative Spreads:*
- More complex interactions
- Callability
- Low maturity
- Higher coupon rates

### 4. Sector-Specific Patterns

- Power sector: Higher ratings, larger issues, specific UOPs
- Credit ratings, issue sizes vary by sector
- Use of proceeds differentiated

## Data

- California municipal green bonds
- Daily data 2020-2023
- Bloomberg YTM data
- US Treasury par curve as reference

## Implications

**For Investors:**
- Green bonds showing negative spreads (green premium)
- Tax status and pricing strategy important
- Diversification beyond traditional sectors

**For Issuers:**
- Maturity, callability, tax status affect spreads
- Structure offerings to attract investors
- Potential for competitive pricing

## See Also

- [[concepts/green-bond-spreads|Green Bond Spreads]]
- [[concepts/association-rule-learning|Association Rule Learning]]
- [[concepts/yield-to-maturity|Yield to Maturity]]
- [[sources/martin-2024-credit-curve|Martin 2024 (Credit Curve)]]

<!-- AUTHORED REGION END -->
