---
authors:
- Anthropic
content_hash: sha256:3cdb4fec3bbf7efcbb10615911627e6a2875fa63a0f882496633fc5548af127a
created: '2026-11-24T23:30:14Z'
mind_map_priority: high
page_id: sources/anthropic-2026-knowledge-graph-construction-cookbook
page_type: source
publication_date: '2026-03-23'
publication_venue: Claude Cookbook (anthropics/claude-cookbooks)
raw_location: raw/anthropic-kg-cookbook/
related:
- concepts/knowledge-graph-construction
- concepts/entity-resolution
- concepts/knowledge-graph
- concepts/structured-output
- concepts/graphrag
- concepts/llm-knowledge-bases
- concepts/autoresearch
- entities/anthropic
- entities/neo4j
revision_id: 1
schema_version: 2
source_hash: sha256:b454b21a22206ee1a3690cf5e0538954ba99a0b26d7d6bb0f809ed8b964ac250
source_path: raw/anthropic-kg-cookbook/guide.md
source_type: article
source_url: https://platform.claude.com/cookbook/capabilities-knowledge-graph-guide
sources: []
tags:
- knowledge-graph
- entity-resolution
- llm-extraction
- evaluation
- anthropic
title: Knowledge Graph Construction with Claude (Anthropic Cookbook)
updated: '2026-11-24T23:30:14Z'
updated_by: op_53f181d9343b
uuid: d0932a87-269d-567b-ba1d-d7b0db4fd5db
---

<!-- AUTHORED REGION START -->
# Knowledge Graph Construction with Claude (Anthropic Cookbook)

**Author:** Anthropic (claude-cookbooks repository) · **Date:** first published 2026-03-23, last checked 2026-11-24 · **Type:** tutorial notebook · **Original:** [guide](https://platform.claude.com/cookbook/capabilities-knowledge-graph-guide), [code](https://github.com/anthropics/claude-cookbooks/tree/main/capabilities/knowledge_graph)

## Summary

A tutorial notebook that builds a knowledge graph from unstructured documents using only prompts. It replaces the four classical stages, each of which used to need a trained model or hand-written rules, with Claude calls: named-entity recognition, relation extraction, entity resolution and entity summarization. The worked corpus is six short Wikipedia summaries about the Apollo program, chosen because they name the same people and places differently. The graph is held in memory with NetworkX and queried by serializing a subgraph back to Claude. The notebook ends with an evaluation harness that scores extraction against a small hand-labelled gold set, and it presents that harness as the feedback loop that turns a demo into a production system.

## Key Ideas

1. **One structured-output call per document** extracts typed entities (PERSON, ORGANIZATION, LOCATION, EVENT, ARTIFACT) and subject-predicate-object relations. A Pydantic schema passed to `client.messages.parse()` is the only "training" needed.
2. **Each entity gets a one-sentence description at extraction time.** The descriptions are reused later to tell apart entities that share a name.
3. **Entity resolution is an LLM clustering task**, run once per entity type. Claude groups surface forms into a canonical name with aliases. It catches "Edwin Aldrin" = "Buzz Aldrin", which string similarity misses because the names share no characters.
4. **Two models by role.** A small model (Haiku) does the high-volume extraction. A stronger model (Sonnet) does resolution and summarization, where evidence from several documents must be weighed.
5. **The graph is a directed multigraph.** Two entities can be linked by several predicates, and direction matters. Nodes carry type, source documents and a mention count. Edges carry the predicate and the source document.
6. **Hub entities get synthesized profiles**: a summary, 3 to 5 atomic key facts and a time range, built from every excerpt that mentions the entity plus its graph neighbourhood. The prompt forbids facts not supported by the excerpts.
7. **Multi-hop questions are answered from a serialized 2-hop subgraph**, and the answer must cite the edges it uses. The point is traceability: on a private corpus only the grounded answer works.
8. **Evaluation is precision and recall against a gold set**, with an alias map so that "the Moon" and "Moon" count as one hit. Relation scoring matches (source, target) pairs and ignores the predicate wording, so its recall is an upper bound.

## Notable Claims

- On the demo corpus, extraction found 40 raw entities and 44 relations. Resolution reduced 23 unique names to 21 canonical entities, and the graph formed a single connected component.
- Extraction precision was 1.00 on both gold-labelled articles, but recall was only 0.64 (Apollo 11) and 0.38 (Neil Armstrong). The extractor is told to keep only central entities, so it misses many that the gold set lists.
- The resolver has two failure modes. A name left out of every cluster silently disappears from the graph. And it can over-merge, for example folding "Gemini 12" into "Project Gemini".
- A resolver can make measured recall fall: if it picks a verbose canonical form the alias map does not know, a correct hit stops matching. The guide calls this a scoring artifact and fixes it by extending the alias map.
- To scale: cache the fixed schema and instructions with prompt caching, use the Message Batches API (50% off for jobs that can wait up to 24 hours), and resolve entities within small blocks of 50 to 100 candidates grouped by cheap signals.
- New documents should be resolved against the existing canonical set, not against each other, and an entity should be re-summarized only when its set of source documents changes materially.
- NetworkX is adequate up to a few hundred thousand edges. Beyond that the same schema maps onto a property graph or three Postgres tables (entities, relations, aliases).

## Quotes

> With Claude, each of those stages becomes a prompt.

## How This Wiki Relates

This wiki does the same four steps in markdown rather than in a graph object. Sources become entity and concept pages (extraction), duplicate pages are merged by hand or by lint (resolution), concept pages pool what several sources say (summarization), and wikilinks are the edges. The cookbook adds one thing this wiki lacks: a gold set with precision and recall. Hand-labelling the entities and concepts of a few sources would give the ingest prompts a measurable score. That score is what an autoresearch-style loop needs (see [[concepts/autoresearch|Autoresearch]]).

## Concepts

- [[concepts/knowledge-graph-construction|Knowledge Graph Construction]]
- [[concepts/entity-resolution|Entity Resolution]]
- [[concepts/knowledge-graph|Knowledge Graph]]
- [[concepts/structured-output|Structured Output]]
- [[concepts/graphrag|GraphRAG]]
- [[concepts/llm-knowledge-bases|LLM Knowledge Bases]]

## Entities

- [[entities/anthropic|Anthropic]]
- [[entities/neo4j|Neo4j]]

## Notes on the Source Text

- The notebook was converted to markdown (`guide.md`) from `guide.ipynb`, keeping cell text and text outputs. Figures were dropped.
- The model names in the notebook were updated in October 2026 to `claude-haiku-5-5` and `claude-sonnet-5-5`. The demo outputs were last regenerated on 2026-03-25, so they may come from earlier models.
- The gold set covers only two of the six articles.

## Source

`raw/anthropic-kg-cookbook/guide.md` (also `README.md`, `evaluation/`, `data/` in the same folder)
<!-- AUTHORED REGION END -->
