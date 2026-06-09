---
abstraction_level: intermediate
concept_type: technique
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/forecast-scaling-and-combination
page_type: concept
related:
- concepts/algorithmic-trading
- concepts/market-timing
revision_hash: sha256:e5629ccce85f8bbf8d4093539b14e5d9f00d5ee76ca089de9fdf8c8789bb9f3d
revision_id: 1
sources:
- sources/carver-2015-systematic-trading
tags: []
title: Forecast Scaling and Combination
updated: '2026-06-09T12:00:00Z'
updated_by: creditmacro-batch
---

# Forecast Scaling and Combination

## Definition

Rescaling each rule's raw signal into a standardised 'forecast' averaging absolute value 10, capped at +/-20, then blending multiple rules via forecast weights and a diversification multiplier.

## Sources

- [[sources/carver-2015-systematic-trading|Systematic Trading: A unique new method for designing trading and investing systems]]

## Related Concepts

- [[concepts/algorithmic-trading|algorithmic-trading]]
- [[concepts/market-timing|market-timing]]