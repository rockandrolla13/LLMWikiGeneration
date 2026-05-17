---
title: Hazard Rate Curve
page_id: concepts/hazard-rate-curve
page_type: concept
revision_id: 1
created: 2026-05-05T23:20:00Z
updated: 2026-05-05T23:20:00Z
tags: [creditETF, credit-curves, default-probability, CDS, bonds]
sources: [sources/ubs-2012-next-gen-credit-curves]
related: [concepts/credit-spread-curve, concepts/cds-bond-basis, concepts/market-implied-ratings, concepts/survival-probability]
---

# Hazard Rate Curve

A **hazard rate curve** represents the term structure of instantaneous default probabilities (conditional default intensity) for an issuer. Unlike spread curves, hazard rates provide a consistent framework for comparing credit risk across bonds and CDS in different currencies.

## Definition

The hazard rate h(t) gives the instantaneous probability of default at time t, conditional on survival to that point:

```
P(default in [t, t+dt] | survival to t) = h(t) dt
```

The cumulative survival probability to time T is:
```
S(T) = exp(-∫₀ᵀ h(t) dt)
```

## Unified Hazard-Rate Approach

Developed by [[entities/ubs-delta|UBS Delta]] (2012), this methodology builds a single hazard-rate curve per issuer by jointly estimating from:

- Bond prices across all issued currencies
- CDS quotes referencing the entity
- Simultaneous estimation of currency/instrument basis

### Key Innovation

Treats bonds consistently with CDS using probability-weighted discounting:
- Two scenarios: default and no default
- Uses market funding rates (OIS + cross-currency basis swaps)
- Derives market-implied default probabilities

## Advantages Over Spread Curves

| Aspect | Spread Curves | Hazard Rate Curves |
|--------|---------------|-------------------|
| Cross-currency | ~30% correlation | >60% correlation |
| Data usage | Single currency | All currencies + CDS |
| Comparability | Different bases | Directly comparable |
| Stability | More volatile | More robust |

## Applications

1. **Credit Risk Modeling:** Single source of credit risk per issuer
2. **CDS Pricing:** Derive bond-implied CDS for issuers without traded CDS
3. **Relative Value:** Compare issuers on consistent basis
4. **CVA Calculation:** Mark credit exposure without traded instruments

## Conversion to Other Formats

Hazard rate curves can be converted to:
- Implied CDS spreads
- Par spreads
- Z-spreads
- Cumulative default probabilities

## Market Surfaces

Using issuer hazard rates, market surfaces can be built covering every rating and maturity for sector/region combinations, enabling:
- Market curves for ratings without traded names
- Reduced artificial jumps from rating migrations
- [[concepts/market-implied-ratings|Market-implied ratings]] derivation

## See Also

- [[concepts/credit-spread-curve]]
- [[concepts/cds-bond-basis]]
- [[concepts/survival-probability]]
- [[sources/ubs-2012-next-gen-credit-curves]]
