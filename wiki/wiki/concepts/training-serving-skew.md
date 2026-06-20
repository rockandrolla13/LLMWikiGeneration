---
title: Training-Serving Skew
page_id: concepts/training-serving-skew
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
sources:
- sources/nelson-2024-swe-for-data-scientists
related: []
mind_map_priority: medium
revision_hash: sha256:14356b876daea5ea
schema_version: 2
uuid: f51bd9b3-0484-5b38-9880-7838f3a12e06
content_hash: sha256:dca6920dd653377d9fc5f69f9cc22687dd7be0254bf9ff82e9ef9daae2c2f23f
---

<!-- AUTHORED REGION START -->
# Training-Serving Skew

## Definition

The mismatch that occurs when preprocessing logic at model training time diverges from preprocessing at inference time, causing deployed model performance to degrade. Mitigations include serializing the preprocessing pipeline alongside the model.

## Sources

- [[sources/nelson-2024-swe-for-data-scientists|Software Engineering for Data Scientists]]

<!-- AUTHORED REGION END -->
