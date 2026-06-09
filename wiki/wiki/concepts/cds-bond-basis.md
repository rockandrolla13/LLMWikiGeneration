---
created: 2026-05-05 23:20:00+00:00
page_id: concepts/cds-bond-basis
page_type: concept
related:
- concepts/corporate-bonds
- concepts/credit-hedge-ratios-equity-options
- concepts/credit-spread-curve
- concepts/credit-spread-puzzle
- concepts/default-rates
- concepts/hazard-rate-curve
- concepts/mark-to-market-credit-hedging
- concepts/option-implied-credit-information
- concepts/z-spread
revision_id: 3
sources:
- sources/avino-2024-hedging-credit-equity-options
- sources/ms-2011-04-18-hy-pricing-tomorrows-deleveraging
- sources/ms-2012-03-09-european-hy-leveraged-finance-playbook
- sources/ms-2012-03-12-what-were-watching
- sources/ms-2018-11-25-the-bear-has-begun
- sources/ms-2019-02-01-credit-strategy-chartbook
- sources/ms-2019-03-22-high-yield-hedge
- sources/ms-2019-04-12-meet-in-the-middle
- sources/ms-2020-03-25-global-volatility-playbook
- sources/ms-2020-03-27-add-to-credit
- sources/ms-2020-03-27-add-to-credit-markets-lead-economy
- sources/pullirsch-2006-credit-spread-risk
- sources/ubs-2012-next-gen-credit-curves
tags:
- creditETF
- CDS
- bonds
- basis-trading
- relative-value
title: CDS-Bond Basis
updated: '2026-06-09T12:00:00Z'
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

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/avino-2024-hedging-credit-equity-options]]

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/ms-2011-04-18-hy-pricing-tomorrows-deleveraging]], [[sources/ms-2012-03-09-european-hy-leveraged-finance-playbook]], [[sources/ms-2012-03-12-what-were-watching]], [[sources/ms-2018-11-25-the-bear-has-begun]], [[sources/ms-2019-02-01-credit-strategy-chartbook]], [[sources/ms-2019-03-22-high-yield-hedge]], [[sources/ms-2019-04-12-meet-in-the-middle]], [[sources/ms-2020-03-25-global-volatility-playbook]], [[sources/ms-2020-03-27-add-to-credit]], [[sources/ms-2020-03-27-add-to-credit-markets-lead-economy]]