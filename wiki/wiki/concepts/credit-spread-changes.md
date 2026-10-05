---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:c751b6c6a280c9b5315022e106787598dcdea97df5f225b8aeadf75adab6f89e
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/credit-spread-changes
page_type: concept
related:
- concepts/baa-corporate-bond-spread
- concepts/corporate-bonds
- concepts/credit-spread-compression
- concepts/credit-spread-curve
- concepts/credit-spread-puzzle
- concepts/default-rates
- concepts/duration-times-spread
revision_id: 3
schema_version: 2
sources:
- sources/collin-dufresne-2001-determinants-credit-spread-changes
- sources/bendor-2007-dts
- sources/cremers-2008-individual-stock-option-prices-credit-spreads
tags: []
title: Credit Spread Changes
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: ff9b7352-acd0-5765-afd4-078e3632029e
---

<!-- AUTHORED REGION START -->
# Credit Spread Changes

## Definition

Monthly changes in the yield difference between a corporate bond and a maturity-matched benchmark Treasury, used as the dependent variable because hedged bond portfolios are sensitive to spread rather than yield movements.

## Parallel or Proportional?

[[sources/bendor-2007-dts|Ben Dor et al. (2007)]] find spread changes are proportional to spread level, not parallel. Bonds at wider spreads widen more in sell-offs and tighten more in rallies. In sector-month regressions on the Lehman Brothers Credit Index (1989–2005), a proportional model explains 33% of spread variation against 16.9% for a parallel shift. Spread volatility scales with spread too: about 9% of spread per month for systematic moves and 11.5% for idiosyncratic ones. That is the basis for measuring spread exposure with [[concepts/duration-times-spread|DTS]].

## Sources

- [[sources/cremers-2008-individual-stock-option-prices-credit-spreads|Individual Stock-Option Prices and Credit Spreads]]
- [[sources/collin-dufresne-2001-determinants-credit-spread-changes|The Determinants of Credit Spread Changes]]
- [[sources/bendor-2007-dts|DTS (Duration Times Spread) (2007)]]

## Related Concepts

- [[concepts/corporate-bonds|corporate-bonds]]
- [[concepts/credit-spread-curve|credit-spread-curve]]
- [[concepts/credit-spread-puzzle|credit-spread-puzzle]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/baa-corporate-bond-spread|baa-corporate-bond-spread]]
- [[concepts/credit-spread-compression|credit-spread-compression]]
- [[concepts/default-rates|default-rates]]
<!-- AUTHORED REGION END -->