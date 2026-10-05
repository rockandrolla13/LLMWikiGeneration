---
abstraction_level: intermediate
concept_type: metric
content_hash: sha256:60fae09e90b55cdf826202056a7b20260dcbf82f1f62ada1ea0da8d0e0504d34
created: '2026-10-05T15:52:32Z'
page_id: concepts/cds-holding-period-return
page_type: concept
related:
- concepts/credit-default-swaps
- concepts/cds-momentum
revision_id: 1
schema_version: 2
sources:
- sources/lee-2021-cds-momentum-cross-market-spillovers
tags:
- credit-default-swaps
- returns
title: CDS Holding-Period Return
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: b2f861f2-a930-50af-b605-39ed05cbe38c
---

<!-- AUTHORED REGION START -->
# CDS Holding-Period Return

## Definition

The mark-to-market profit or loss on a unit-notional CDS position over a holding window, usually from the protection seller's side. It equals minus the spread change times the contract's risky annuity (RPV01), with the premium flows carried inside that annuity; if a credit event occurs in the window, the return is minus the loss given default. It turns spread quotes into returns that can be sorted, factor-tested and compared with bond and stock returns.

## Sources

- [[sources/lee-2021-cds-momentum-cross-market-spillovers|CDS Momentum: Slow-Moving Credit Ratings and Cross-Market Spillovers]]

## Related Concepts

- [[concepts/credit-default-swaps|Credit Default Swaps]]
- [[concepts/cds-momentum|CDS Momentum]]
<!-- AUTHORED REGION END -->