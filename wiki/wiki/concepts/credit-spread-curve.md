---
created: 2026-04-25 22:00:00+00:00
mind_map_priority: high
page_id: concepts/credit-spread-curve
page_type: concept
related:
- concepts/carry-rolldown
- concepts/cds-bond-basis
- concepts/corporate-bonds
- concepts/corporate-hybrid-bonds
- concepts/credit-spread-changes
- concepts/credit-spread-compression
- concepts/credit-spread-forecasting
- concepts/credit-spread-puzzle
- concepts/default-rates
- concepts/financial-conditions
- concepts/government-bond-spreads
- concepts/hyperscaler-data-center-bond-relative-value
- concepts/mean-reversion
- concepts/nelson-siegel-model
- concepts/project-finance-data-center-bonds
- concepts/speculative-grade-default-rate
- concepts/survival-probability
- concepts/term-structure-risk-premium
- concepts/z-spread
revision_id: 3
sources:
- sources/martin-2024-credit-curve
- sources/ms-2009-11-12-us-rate-strategist
- sources/ms-2011-03-28-high-grade-mid-cycle
- sources/ms-2011-04-18-hy-pricing-tomorrows-deleveraging
- sources/ms-2012-03-12-what-were-watching
- sources/ms-2013-12-04-faqs-on-corporate-hybrids
- sources/ms-2014-02-21-corporate-hybrid-primer
- sources/ms-2015-11-16-corporate-hybrids-playbook
- sources/ms-2016-04-13-euro-sovereign-bond-market-indicators
- sources/ms-2017-06-23-ig-fundamentals-in-good-shape
- sources/ms-2017-07-10-european-credit-watch
- sources/ms-2018-11-25-the-bear-has-begun
- sources/ms-2019-01-28-european-credit-reluctant-rally
- sources/ms-2019-01-28-european-credit-watch
- sources/ms-2019-02-01-credit-strategy-chartbook
- sources/ms-2019-02-04-corporate-hybrids-playbook
- sources/ms-2019-02-28-selling-the-rally
- sources/ms-2019-03-15-4q18-credit-fundamentals
- sources/ms-2019-04-12-meet-in-the-middle
- sources/ms-2019-05-23-value-tier2-seniors
- sources/ms-2020-03-10-cross-asset-moves-context
- sources/ms-2020-04-01-in-the-flow-q1-recap
tags:
- fixed-income
- credit-risk
- bond-pricing
- yield-curves
title: Credit Spread Curve
updated: '2026-06-09T12:00:00Z'
---

# Credit Spread Curve

The credit spread curve represents the term structure of credit spreads—the additional yield investors require above risk-free rates to hold a risky bond.

## Definition

A credit spread curve maps maturity (or duration) to credit spread, providing a complete picture of how credit risk is priced across different time horizons for a given issuer or rating category.

## Key Concepts

### Par vs Non-Par Problem
A critical distinction in credit spread construction:
- **Par bonds** trade at face value; their yields directly reflect current market spreads
- **Non-par bonds** have coupons that differ from current market rates, requiring adjustment

### Construction Approaches

1. **Z-spread method**: Constant spread added to the risk-free curve
2. **Survival probability method**: Derive spreads from default probability curves
3. **Interpolation methods**: Nelson-Siegel, splines, or piecewise linear

## Applications

- **Relative value analysis**: Identifying mis-priced bonds
- **Portfolio construction**: Systematic spread positioning
- **Risk management**: Duration and spread risk decomposition
- **Carry and rolldown**: Projecting returns from spread curve dynamics

## Mathematical Framework

The credit spread $s(t)$ at maturity $t$ relates to the survival probability $Q(t)$ and recovery rate $R$:

$$s(t) \approx -\frac{\ln Q(t)}{t} \cdot (1 - R)$$

## See Also

- [[concepts/z-spread|Z-Spread]]
- [[concepts/survival-probability|Survival Probability]]
- [[concepts/carry-rolldown|Carry and Rolldown]]
- [[sources/martin-2024-credit-curve|The Credit Curve Spread I (Martin, 2024)]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/corporate-bonds|corporate-bonds]]
- [[concepts/credit-spread-changes|credit-spread-changes]]
- [[concepts/credit-spread-compression|credit-spread-compression]]
- [[concepts/credit-spread-forecasting|credit-spread-forecasting]]
- [[concepts/credit-spread-puzzle|credit-spread-puzzle]]
- [[concepts/hyperscaler-data-center-bond-relative-value|hyperscaler-data-center-bond-relative-value]]
- [[concepts/project-finance-data-center-bonds|project-finance-data-center-bonds]]
- [[concepts/speculative-grade-default-rate|speculative-grade-default-rate]]

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/ms-2009-11-12-us-rate-strategist]], [[sources/ms-2011-03-28-high-grade-mid-cycle]], [[sources/ms-2011-04-18-hy-pricing-tomorrows-deleveraging]], [[sources/ms-2012-03-12-what-were-watching]], [[sources/ms-2013-12-04-faqs-on-corporate-hybrids]], [[sources/ms-2014-02-21-corporate-hybrid-primer]], [[sources/ms-2015-11-16-corporate-hybrids-playbook]], [[sources/ms-2016-04-13-euro-sovereign-bond-market-indicators]], [[sources/ms-2017-06-23-ig-fundamentals-in-good-shape]], [[sources/ms-2017-07-10-european-credit-watch]], [[sources/ms-2018-11-25-the-bear-has-begun]], [[sources/ms-2019-01-28-european-credit-reluctant-rally]], [[sources/ms-2019-01-28-european-credit-watch]], [[sources/ms-2019-02-01-credit-strategy-chartbook]], [[sources/ms-2019-02-04-corporate-hybrids-playbook]], [[sources/ms-2019-02-28-selling-the-rally]], [[sources/ms-2019-03-15-4q18-credit-fundamentals]], [[sources/ms-2019-04-12-meet-in-the-middle]], [[sources/ms-2019-05-23-value-tier2-seniors]], [[sources/ms-2020-03-10-cross-asset-moves-context]], [[sources/ms-2020-04-01-in-the-flow-q1-recap]]