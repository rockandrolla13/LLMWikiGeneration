---
abstraction_level: intermediate
concept_type: theory
content_hash: sha256:6d4dee71929a4d30784367265487250d42ff3e9ac345b291dc816944daa42f28
created: '2026-10-05T15:52:11Z'
page_id: concepts/unit-recovery-claim
page_type: concept
related:
- concepts/credit-default-swaps
- concepts/capital-structure-arbitrage
revision_id: 2
schema_version: 2
sources:
- sources/carr-2011-american-puts-credit-protection
- sources/chan-2023-price-convergence-cds-put-option
- sources/shi-2022-cds-implied-volatility-trading-strategies
- sources/kricheff-2012-pragmatists-guide-leveraged-finance
- sources/whitman-2009-distress-investing
tags:
- credit-default-swaps
- options
- credit-risk
title: Unit Recovery Claim
updated: '2026-10-22T21:10:31Z'
updated_by: op_0cdb8cc1f169
uuid: a2513425-0d49-5511-8ad4-adfaadb45382
---

<!-- AUTHORED REGION START -->
# Unit Recovery Claim

## Definition

A credit claim that pays one dollar at the default time if default happens before expiry, and nothing otherwise. Carr and Wu (2011) show it can be replicated by a strike-scaled spread of deep out-of-the-money American puts when the stock price, at default, falls into a 'default corridor' below the strikes; it can also be backed out of a CDS spread under fixed recovery and a flat hazard rate. Comparing the two gives a near model-free test of whether equity options and CDS agree on default risk. The CBOE once listed it as Credit Event Binary Options.

## Sources

- [[sources/whitman-2009-distress-investing|Distress Investing: Principles and Technique]] (2009)
- [[sources/kricheff-2012-pragmatists-guide-leveraged-finance|A Pragmatist's Guide to Leveraged Finance: Credit Analysis for Bonds and Bank Debt]] (2012)
- [[sources/carr-2011-american-puts-credit-protection|A Simple Robust Link Between American Puts and Credit Protection]]
- [[sources/chan-2023-price-convergence-cds-put-option|Price Convergence Between Credit Default Swap and Put Option: New Evidence]]
- [[sources/shi-2022-cds-implied-volatility-trading-strategies|The Information Content of CDS Implied Volatility and Associated Trading Strategies]]

## Related Concepts

- [[concepts/credit-default-swaps|Credit Default Swaps]]
- [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]]
<!-- AUTHORED REGION END -->