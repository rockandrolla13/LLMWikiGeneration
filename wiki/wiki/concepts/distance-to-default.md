---
abstraction_level: intermediate
concept_type: metric
content_hash: sha256:2908142bdc2120c847f86d8358fb29548c5a8cfc936f9fad228577bdc89f30f8
created: '2026-10-05T15:52:11Z'
page_id: concepts/distance-to-default
page_type: concept
related:
- concepts/merton-model
- concepts/structural-models
- concepts/creditgrades-model
revision_id: 2
schema_version: 2
sources:
- sources/bai-2016-anchoring-cds-spreads-firm-fundamentals
- sources/bharath-2008-forecasting-default-merton-distance-to-default
- sources/correia-2012-value-investing-credit-markets
- sources/israel-2017-common-factors-corporate-bond-returns
- sources/kricheff-2012-pragmatists-guide-leveraged-finance
tags:
- credit-risk
- structural-models
title: Distance to Default
updated: '2026-10-22T21:10:31Z'
updated_by: op_0cdb8cc1f169
uuid: 6ca56958-dd53-5561-a4d9-d849511c9efa
---

<!-- AUTHORED REGION START -->
# Distance to Default

## Definition

The Merton model's standardised credit measure: the log gap between the firm's asset value and its default point, adjusted for drift and scaled by asset volatility over the horizon. It counts how many standard deviations the firm is from default, and merges leverage and business risk into one number comparable across firms. The full version solves for unobserved asset value and volatility from equity value and equity volatility; the 'naive' version of Bharath and Shumway (2008) replaces that solve with simple proxies and forecasts default about as well.

## Sources

- [[sources/kricheff-2012-pragmatists-guide-leveraged-finance|A Pragmatist's Guide to Leveraged Finance: Credit Analysis for Bonds and Bank Debt]] (2012)
- [[sources/israel-2017-common-factors-corporate-bond-returns|Common Factors in Corporate Bond Returns]] (2017)
- [[sources/correia-2012-value-investing-credit-markets|Value Investing in Credit Markets]] (2012)
- [[sources/bai-2016-anchoring-cds-spreads-firm-fundamentals|Anchoring Credit Default Swap Spreads to Firm Fundamentals]]
- [[sources/bharath-2008-forecasting-default-merton-distance-to-default|Forecasting Default with the Merton Distance to Default Model]]

## Related Concepts

- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/structural-models|Structural Models]]
- [[concepts/creditgrades-model|CreditGrades Model]]
<!-- AUTHORED REGION END -->