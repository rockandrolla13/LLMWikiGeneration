---
content_hash: sha256:37ad10c40f04dd6ca4641bae9f4097c05f7435c79744e4832e798a74d9c677e5
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/entity-resolution
page_type: concept
related:
- concepts/knowledge-graph-construction
- sources/anthropic-2026-knowledge-graph-construction-cookbook
revision_id: 2
schema_version: 2
sources:
- sources/barrasa-2023-building-knowledge-graphs
- sources/bratanic-2025-essential-graphrag
- sources/anthropic-2026-knowledge-graph-construction-cookbook
tags:
- ai-engineering
- knowledge-graph-construction
title: Entity Resolution
updated: '2026-11-24T23:30:14Z'
updated_by: op_53f181d9343b
uuid: cb0844a6-5ea1-55c0-a2dc-20daa9cc5879
---

<!-- AUTHORED REGION START -->
# Entity Resolution

## Definition

The process of determining whether two or more records refer to the same real-world entity; the book operationalises it as a graph-based pipeline of data preparation, entity matching, and persistence of master 'golden' records.

## Sources

- [[sources/barrasa-2023-building-knowledge-graphs|Building Knowledge Graphs]]
- [[sources/bratanic-2025-essential-graphrag|Essential GraphRAG]]

## Related Concepts

- [[concepts/knowledge-graph-construction]]

## LLM Clustering With Descriptions

The Anthropic cookbook resolves entities by asking Claude to cluster names of one type, using the one-sentence description written for each entity at extraction time. This catches aliases with no shared characters ("Edwin Aldrin" and "Buzz Aldrin") and keeps apart entities that only share a name. Its stated failure modes are names dropped from every cluster and over-merging (a mission folded into its program). At scale it blocks candidates first by cheap signals and resolves within blocks of 50 to 100. See [[sources/anthropic-2026-knowledge-graph-construction-cookbook|Knowledge Graph Construction with Claude (Anthropic Cookbook)]].
<!-- AUTHORED REGION END -->
