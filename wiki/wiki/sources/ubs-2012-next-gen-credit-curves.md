---
title: "Next-Generation Credit Curves"
page_id: sources/ubs-2012-next-gen-credit-curves
page_type: source
revision_id: 1
created: 2026-05-05T23:15:00Z
updated: 2026-05-05T23:15:00Z
tags: [creditETF, hazard-rate, credit-curves, CDS-bond-basis, market-implied-ratings]
authors: [entities/lindsey-matthews, entities/luca-bosatta]
institutions: [entities/ubs-delta]
related: [concepts/hazard-rate-curve, concepts/cds-bond-basis, concepts/market-implied-ratings, concepts/credit-spread-curve]
---

# Next-Generation Credit Curves

**Authors:** [[entities/lindsey-matthews|Lindsey Matthews]], [[entities/luca-bosatta|Luca Bosatta]]
**Institution:** [[entities/ubs-delta|UBS Delta]]
**Date:** 2012 (Risk magazine sponsored feature)
**Focus:** Unified hazard-rate approach to credit curve calibration

## Summary

Presents UBS Delta's "D-Curves" methodology for building credit curves by unifying bonds and CDS across multiple currencies into a single hazard-rate framework. Addresses limitations of traditional currency-specific spread curves and demonstrates improved correlation and stability.

## Problem Statement

**Traditional Approach Limitations:**
- Spread curves built separately by currency
- Bond curves separate from CDS curves
- Low correlation (~30%) between same-issuer curves in different currencies
- Rating-based proxy curves miss issuer idiosyncrasies
- Artificial jumps from ratings migrations

## The Unified Hazard-Rate Approach

### Methodology

**Key Innovation:** Jointly estimate one hazard-rate curve per issuer using:
- Bond prices across all issued currencies
- CDS quotes referencing the entity
- Simultaneous estimation of currency/instrument basis

**Technical Details:**
- Treat bonds consistently with CDS (two scenarios: default/no default)
- Discount probability-weighted values
- Use market funding rates (OIS + cross-currency basis swaps)
- Derive term structure of market-implied default probabilities

### Benefits

1. **Higher Correlation:**
   - Implied CDS curves across currencies: >60% correlation
   - vs. ~30% for traditional z-spread curves

2. **More Robust Curves:**
   - More data points support each curve
   - Less sensitive to single bond price spikes
   - Reduced need for proxy curves

3. **Cross-Currency Comparability:**
   - Hazard rates directly comparable across instruments
   - Can derive bond-implied CDS for issuers without traded CDS

4. **Extended Coverage:**
   - Generate market curves for rating/sector combinations without traded instruments
   - Useful for CVA marking

### Example: BMW

**Traditional (GBP only):**
- Few GBP bonds available
- Required sector proxy curve (single-A corporates) beyond 6 years
- ~200bp z-spread at long end using proxy

**Unified Approach:**
- Uses bonds in GBP, AUD, CAD, CHF, EUR, NOK
- Plus CDS quotes
- ~115bp hazard rate at long end (more accurate)

## Market Surfaces

### Construction

- Build surfaces for every rating and maturity simultaneously
- Each rating point influences adjacent ratings (weighted by distance)
- Covers region/sector combinations with sufficient data

### Advantages

- Greater granularity than traditional rating-by-rating approach
- Reduces artificial jumps from rating migrations
- Enables market curves for rating buckets without traded names

## Market-Implied Ratings

**Definition:** Rating that would make issuer's hazard rate lie on market surface at given tenor.

**Application:**
- Compare issuer vs. sector surface
- Compare issuer vs. global all-industries surface
- Track historical rating drift implied by markets

## Disadvantages Acknowledged

- Requires revision to how practitioners think about credit valuation
- Risk model alterations needed for portfolio risk
- More complex implementation

## Related Concepts

- [[concepts/hazard-rate-curve]]
- [[concepts/cds-bond-basis]]
- [[concepts/market-implied-ratings]]
- [[concepts/credit-spread-curve]]
- [[concepts/zero-coupon-curve]]
