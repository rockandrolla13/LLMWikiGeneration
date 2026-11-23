---
content_hash: sha256:dcce05c2453e7acf6979b0ba07bab8d9cb597b1ff5195c9af73815026c24fc3a
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/continual-learning
page_type: concept
related:
- concepts/data-distribution-shift
- sources/karpathy-2026-llm-knowledge-bases-tweets
revision_id: 2
schema_version: 2
sources:
- sources/huyen-2022-designing-ml-systems
- sources/karpathy-2026-llm-knowledge-bases-tweets
tags:
- ai-engineering
- data-distribution-shift
title: Continual Learning
updated: '2026-11-23T14:43:11Z'
updated_by: op_5c91b297008c
uuid: 65e70fa8-fdb9-5a34-a8fe-2c623f0be190
---

<!-- AUTHORED REGION START -->
# Continual Learning

## Definition

An infrastructure pattern that lets teams update deployed models on demand (stateless retraining or stateful fine-tuning) at the cadence required by data freshness, distribution shifts, or rare events such as Black Friday, contrasted with the term 'online learning'.

## Sources

- [[sources/huyen-2022-designing-ml-systems|Designing Machine Learning Systems]]

## Related Concepts

- [[concepts/data-distribution-shift]]

## Memory Ops and Weight Updates

Karpathy suggests adding memory operations as tools during RL training, and expects that more exotic long-term memory which changes the weights will be needed, by analogy with learning during sleep. He also floats fine-tuning a model on a personal wiki so it "knows" the content in its weights. See [[sources/karpathy-2026-llm-knowledge-bases-tweets|Karpathy on Obsidian, Second Brains and LLM Knowledge Bases]].
<!-- AUTHORED REGION END -->
