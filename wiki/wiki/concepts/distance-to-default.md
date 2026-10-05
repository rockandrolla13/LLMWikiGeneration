---
abstraction_level: intermediate
concept_type: metric
content_hash: sha256:bc627605bf36b8577a07de67e7e5a785c344f1490da98352c5c5790fac6b4bff
created: '2026-10-05T15:52:11Z'
page_id: concepts/distance-to-default
page_type: concept
related:
- concepts/merton-model
- concepts/structural-models
- concepts/creditgrades-model
revision_id: 1
schema_version: 2
sources:
- sources/bai-2016-anchoring-cds-spreads-firm-fundamentals
- sources/bharath-2008-forecasting-default-merton-distance-to-default
tags:
- credit-risk
- structural-models
title: Distance to Default
updated: '2026-10-05T15:52:11Z'
updated_by: op_afa4380123f6
uuid: 6ca56958-dd53-5561-a4d9-d849511c9efa
---

<!-- AUTHORED REGION START -->
# Distance to Default

## Definition

The Merton model's standardised credit measure: the log gap between the firm's asset value and its default point, adjusted for drift and scaled by asset volatility over the horizon. It counts how many standard deviations the firm is from default, and merges leverage and business risk into one number comparable across firms. The full version solves for unobserved asset value and volatility from equity value and equity volatility; the 'naive' version of Bharath and Shumway (2008) replaces that solve with simple proxies and forecasts default about as well.

## Sources

- [[sources/bai-2016-anchoring-cds-spreads-firm-fundamentals|Anchoring Credit Default Swap Spreads to Firm Fundamentals]]
- [[sources/bharath-2008-forecasting-default-merton-distance-to-default|Forecasting Default with the Merton Distance to Default Model]]

## Related Concepts

- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/structural-models|Structural Models]]
- [[concepts/creditgrades-model|CreditGrades Model]]
<!-- AUTHORED REGION END -->