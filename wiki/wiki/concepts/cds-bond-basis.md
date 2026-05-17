---
title: CDS-Bond Basis
page_id: concepts/cds-bond-basis
page_type: concept
revision_id: 1
created: 2026-05-05T23:20:00Z
updated: 2026-05-05T23:20:00Z
tags: [creditETF, CDS, bonds, basis-trading, relative-value]
sources: [sources/ubs-2012-next-gen-credit-curves, sources/pullirsch-2006-credit-spread-risk]
related: [concepts/hazard-rate-curve, concepts/credit-spread-curve, concepts/z-spread]
---

# CDS-Bond Basis

The **CDS-bond basis** is the difference between the CDS spread and the bond spread for the same issuer and maturity. Understanding and modeling this basis is critical for relative value analysis and unified credit curve construction.

## Definition

```
Basis = CDS Spread - Bond Spread (z-spread or asset swap spread)
```

- **Positive basis:** CDS trades wider than bonds
- **Negative basis:** Bonds trade wider than CDS

## Sources of Basis

### Funding Differences
- CDS is unfunded (no upfront principal)
- Bonds require funding at investor's cost
- Bond spreads implicitly include funding premium

### Structural Differences
- CDS: Protection on reference entity
- Bonds: Specific security with cash flows
- Delivery optionality in CDS

### Technical Factors
- Liquidity differences
- Repo availability for bonds
- Counterparty risk in CDS
- Currency of denomination

## Cross-Currency Basis

Same-issuer bonds in different currencies trade at different spreads due to:
- Different investor bases
- Currency-specific funding costs
- Cross-currency basis swap costs
- Local market liquidity

**Empirical Finding (UBS Delta 2012):**
- Traditional z-spreads: ~30% correlation across currencies
- Unified hazard rates: >60% correlation across currencies

## Modeling Approaches

### Traditional (Separate Curves)
- Build bond spread curve per currency
- Build CDS curve separately
- Treat as independent risk factors

### Unified Hazard-Rate Approach
- Joint estimation from all bonds and CDS
- Explicit basis parameters per currency/instrument
- Single credit risk factor per issuer

## Applications

1. **Basis Trading:** Exploit deviations from fair value
2. **Curve Construction:** Inform credit curve shape
3. **Risk Management:** Properly hedge bond vs. CDS exposure
4. **Relative Value:** Identify cheap/rich instruments

## Historical Context

Pre-crisis (2006), [[sources/pullirsch-2006-credit-spread-risk|Pullirsch]] noted bonds of same issuer in different currencies trade with "slightly different credit-spreads" - requiring currency-independent curve estimation.

Post-crisis, the importance of basis modeling increased significantly.

## See Also

- [[concepts/hazard-rate-curve]]
- [[concepts/credit-spread-curve]]
- [[concepts/z-spread]]
- [[sources/ubs-2012-next-gen-credit-curves]]
