---
content_hash: sha256:1db3fad4ebde72bb75a98ae1c3e11741f110a4c2bdf01c93c168464ab26298fd
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/knowledge-graph-construction
page_type: concept
related:
- sources/anthropic-2026-knowledge-graph-construction-cookbook
revision_id: 2
schema_version: 2
sources:
- sources/bratanic-2025-essential-graphrag
- sources/anthropic-2026-knowledge-graph-construction-cookbook
tags:
- ai-engineering
title: Knowledge Graph Construction
updated: '2026-11-24T23:30:14Z'
updated_by: op_53f181d9343b
uuid: 0cf8f0df-e048-5eb8-b365-875676317335
---

<!-- AUTHORED REGION START -->
# Knowledge Graph Construction

## Definition

The process of extracting entities, attributes, and relationships from unstructured text using LLMs with structured-output schemas, then importing the resulting triples into a graph database with entity resolution to merge duplicates.

## Sources

- [[sources/bratanic-2025-essential-graphrag|Essential GraphRAG]]

## With Claude, Stage by Stage

Anthropic's cookbook runs each classical stage as a prompt: one structured-output call per document extracts typed entities and triples, an LLM clusters surface forms into canonical entities, hub entities get synthesized profiles, and multi-hop questions are answered from a serialized subgraph with edge citations. It scores extraction with precision and recall against a hand-labelled gold set. On its demo corpus precision was 1.00 and recall 0.38 to 0.64. See [[sources/anthropic-2026-knowledge-graph-construction-cookbook|Knowledge Graph Construction with Claude (Anthropic Cookbook)]].
<!-- AUTHORED REGION END -->
