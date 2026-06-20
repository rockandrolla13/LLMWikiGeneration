---
title: Green Bond Spreads
page_id: concepts/green-bond-spreads
page_type: concept
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- sustainable-finance
- green-bonds
- fixed-income
- esg
sources:
- sources/sehatpour-2024-green-bonds
related:
- concepts/yield-to-maturity
- concepts/credit-spread-curve
- concepts/association-rule-learning
- entities/christina-nikitopoulos
mind_map_priority: high
schema_version: 2
uuid: 0d55a3de-bd0b-544c-b9cd-aa4df4962efa
content_hash: sha256:33a6f59f0556367b60c531dbe4b6ee79922d84466162cadc1924f0e09dcd7e41
---

<!-- AUTHORED REGION START -->
# Green Bond Spreads

Green bond spreads measure the yield difference between green bonds and comparable conventional bonds, often referred to as the "greenium."

## Definition

$$\text{Green Spread} = \text{Green Bond Yield} - \text{Conventional Bond Yield}$$

A negative spread (greenium) indicates green bonds trade at a premium (lower yield).

## Measurement Challenges

### Traditional Approaches
- **Matched pair**: Find a conventional bond with similar characteristics
- **Problem**: Exact matches rarely exist (different maturities, coupons)

### Modern Approaches
- **Yield-to-maturity based**: Compare YTM within issuer
- **Association Rule Learning**: Data-driven pattern discovery
- **Regression-based**: Control for bond characteristics

## Greenium Evidence

| Market | Typical Greenium | Notes |
|--------|------------------|-------|
| Municipal (US) | -5 to -15 bps | Strongest evidence |
| Corporate (EU) | -2 to -5 bps | Mixed findings |
| Sovereign | Near zero | Limited data |

## Drivers of Green Bond Pricing

1. **Investor preferences**: ESG mandates, impact investing
2. **Supply constraints**: Limited green bond supply
3. **Certification costs**: Verification and reporting
4. **Liquidity effects**: Sometimes lower trading volume

## Research Findings (Sehatpour et al., 2024)

- Municipal green bonds show consistent greenium
- Greenium varies by sector and certification type
- Association Rule Learning reveals non-linear patterns
- YTM-based measures avoid matching design pitfalls

## See Also

- [[concepts/yield-to-maturity|Yield to Maturity]]
- [[concepts/credit-spread-curve|Credit Spread Curve]]
- [[concepts/association-rule-learning|Association Rule Learning]]
- [[sources/sehatpour-2024-green-bonds|Anatomy of Municipal Green Bond Yield Spreads (2024)]]

<!-- AUTHORED REGION END -->
