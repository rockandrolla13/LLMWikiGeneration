---
abstraction_level: intermediate
concept_type: metric
content_hash: sha256:d22e9731bcbb4464d50d2019d856bfa49c870330f90900f57c4bb3e64d361dfa
created: '2026-10-05T15:52:32Z'
page_id: concepts/cds-implied-volatility
page_type: concept
related:
- concepts/unit-recovery-claim
- concepts/credit-default-swaps
revision_id: 1
schema_version: 2
sources:
- sources/shi-2022-cds-implied-volatility-trading-strategies
tags:
- credit-default-swaps
- volatility
- cross-asset
title: CDS-Implied Volatility
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: 5eeb1080-cf65-53df-ba28-c6a1c0863276
---

<!-- AUTHORED REGION START -->
# CDS-Implied Volatility

## Definition

The equity volatility implied by a firm's CDS spread. It is obtained by mapping the spread through a credit-equity link, either a structural model or the unit-recovery-claim link between CDS and deep out-of-the-money puts, and inverting for volatility. Comparing it with option-implied volatility shows whether the credit and options markets agree on the firm's risk.

## Sources

- [[sources/shi-2022-cds-implied-volatility-trading-strategies|The Information Content of CDS Implied Volatility and Associated Trading Strategies]]

## Related Concepts

- [[concepts/unit-recovery-claim|Unit Recovery Claim]]
- [[concepts/credit-default-swaps|Credit Default Swaps]]
<!-- AUTHORED REGION END -->