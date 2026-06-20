---
authors:
- Davide E. Avino
- Enrique Salvador
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/avino-2024-hedging-credit-equity-options
page_type: source
publication_date: '2024'
publication_venue: The Review of Asset Pricing Studies, 14(2)
related:
- concepts/cds-bond-basis
- concepts/compound-option-model
- concepts/credit-hedge-ratios-equity-options
- concepts/mark-to-market-credit-hedging
- concepts/merton-model
- concepts/option-implied-credit-information
- concepts/volatility-smirk
- entities/davide-avino
- entities/enrique-salvador
- entities/peter-carr
- entities/robert-geske
- entities/robert-merton
revision_hash: sha256:128cdbc36398d8eb6e9f8d4e1a80c1445f9aac0b1a874ab96ebd95737af6fcad
revision_id: 1
source_hash: sha256:d228904f46af96fbf59ce9292315e235d77ffae830b3f93efe9065a8b6a5c254
source_path: raw/creditmacro/raae005.md
source_type: paper
sources: []
tags:
- credit-risk
- structural-models
- equity-options
- cds
- hedging
- volatility-skew
title: Contingent Claims and Hedging of Credit Risk with Equity Options
updated: '2026-06-20T01:03:51Z'
updated_by: op_32f967511f6a
schema_version: 2
uuid: d8939cff-e248-5bb9-8bcc-e9ef6a61fa49
content_hash: sha256:3f331350f75b66420663802c134c860e14f88053e15eb37a6e4d662b5738718a
---

<!-- AUTHORED REGION START -->
# Contingent Claims and Hedging of Credit Risk with Equity Options

**Authors:** Davide E. Avino, Enrique Salvador · **Year:** 2024 · **Venue:** The Review of Asset Pricing Studies, 14(2) · **Type:** paper

## Summary

Avino and Salvador use contingent-claims valuation to derive theoretical hedge ratios that measure the sensitivity of corporate bond credit spreads to equity put options, combining Merton's (1974) structural credit risk model with Geske's (1979) compound option pricing model. The firm value V is the single driving state variable, so the elasticity of the credit spread to the put price is decomposed analytically. Empirically, using monthly data on 230 North American firms (Aug 2001-Dec 2021) matching 5-year CDS spreads with American equity put options, option hedge ratios align with empirical CDS-spread sensitivities (coefficient not statistically different from one) and raise adjusted R-squared by up to 5 points. Option returns carry credit-relevant information not in equity prices, and a mark-to-market hedging approach is claimed to cut hedging costs ~90% for a short-CDS portfolio.

## Key Claims

1. Theoretical hedge ratios of bond credit spreads to equity put options are derived by combining Merton (1974) and Geske (1979); the authors claim to be first to test Geske compound-option sensitivities of credit spreads.
2. On 230 North American firms (2001-2021) the model coefficient on theoretical option hedge ratios is not statistically different from one, indicating accurate prediction of put-option sensitivities of CDS spreads.
3. Option model hedge ratios reduce out-of-sample RMSE of a short-CDS portfolio by 19% versus 14% for equity hedge ratios.
4. Option returns explain up to an additional 5% of CDS spread changes left unexplained by equity; the option-only component relates to the VIX index and the default spread.
5. A proposed mark-to-market hedging approach reduces hedging costs by almost 90% for a portfolio of short CDS positions.
6. Combining stocks and puts based on changes in the volatility smirk further reduces portfolio volatility.

## Questions Raised

- How sensitive are the hedge ratios to the maturity mismatch between short-dated puts and 5-year CDS contracts?
- How much of the incremental option information is genuinely option-specific versus aggregate credit/equity factors?
- How does mark-to-market hedging perform under transaction costs and wider bid-ask spreads?

## Concepts

- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/compound-option-model|Geske Compound Option Model]]
- [[concepts/credit-hedge-ratios-equity-options|Credit Hedge Ratios with Equity Options]]
- [[concepts/mark-to-market-credit-hedging|Mark-to-Market Credit Hedging]]
- [[concepts/volatility-smirk|Volatility Smirk as Informed-Trading Signal]]
- [[concepts/option-implied-credit-information|Option-Implied Information in Credit Markets]]
- [[concepts/cds-bond-basis|CDS-Bond Basis]]

## Entities

- [[entities/davide-avino|Davide E. Avino]]
- [[entities/enrique-salvador|Enrique Salvador]]
- [[entities/robert-merton|Robert C. Merton]]
- [[entities/robert-geske|Robert Geske]]
- [[entities/peter-carr|Peter Carr]]

## Source

- **Path:** `raw/creditmacro/raae005.md`
- **Type:** paper
- **Hash:** `sha256:d228904f46af96fbf...`
<!-- AUTHORED REGION END -->
