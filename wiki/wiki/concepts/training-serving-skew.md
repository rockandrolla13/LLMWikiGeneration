---
title: Training-Serving Skew
page_id: concepts/training-serving-skew
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
sources:
- sources/nelson-2024-swe-for-data-scientists
related: []
mind_map_priority: medium
revision_hash: sha256:14356b876daea5ea
---

# Training-Serving Skew

## Definition

The mismatch that occurs when preprocessing logic at model training time diverges from preprocessing at inference time, causing deployed model performance to degrade. Mitigations include serializing the preprocessing pipeline alongside the model.

## Sources

- [[sources/nelson-2024-swe-for-data-scientists|Software Engineering for Data Scientists]]
