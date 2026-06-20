---
title: Building Knowledge Graphs
page_id: sources/barrasa-2023-building-knowledge-graphs
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Jesus Barrasa
- Jim Webber
year: 2023
publisher: O'Reilly Media
edition: 1st
is_early_release: false
page_count_estimate: 290
tags:
- ai-engineering
- knowledge-graph
related:
- concepts/cypher-query-language
- concepts/entity-resolution
- concepts/graph-data-science
- concepts/graph-native-machine-learning
- concepts/knowledge-graph
- concepts/knowledge-lake
- concepts/metadata-knowledge-graph
- concepts/ontology
- concepts/property-graph-model
- concepts/rdf
- concepts/semantic-similarity
- concepts/taxonomy
- entities/apache-kafka
- entities/apache-spark
- entities/jesus-barrasa
- entities/jim-webber
- entities/maya-natarajan
- entities/neo4j
- entities/nicola-vitucci
- entities/rasa
- entities/spacy
- entities/wordnet
mind_map_priority: medium
revision_hash: sha256:1846b6522a7dda48
schema_version: 2
uuid: 160876ba-683d-537a-a65d-02afea7bc0d5
content_hash: sha256:00431e2b9f6fa3ad264cef4e858e68fea7977dcd8e6f13e4258867c2e877e38a
---

<!-- AUTHORED REGION START -->
# Building Knowledge Graphs
*A Practitioner's Guide*

**Authors:** [[entities/jesus-barrasa|Jesus Barrasa]], [[entities/jim-webber|Jim Webber]]

**Year:** 2023

**Publisher:** O'Reilly Media

**Edition:** 1st

## Summary

Building Knowledge Graphs is a hands-on technical guide by two Neo4j practitioners that frames the [[knowledge-graph|knowledge graph]] as a purposeful, contextualised arrangement of enterprise data rather than a particular technology stack. The first half teaches the substrate: the [[property-graph-model|property graph model]], the [[cypher-query-language|Cypher query language]], bulk and streaming data loading (LOAD CSV, Apache Hop, Kafka Connect, Spark), graph algorithms via Neo4j Graph Data Science, and [[graph-native-machine-learning|graph-native machine learning]] pipelines. Throughout, the authors argue that [[taxonomy|taxonomies]] and [[ontology|ontologies]] provide the 'organising principle' that turns a plain graph into a knowledge graph, and they deliberately position [[rdf|RDF]] as a useful exchange format rather than a mandatory storage choice.

The second half is organised around recurring use-case archetypes: [[metadata-knowledge-graph|metadata knowledge graphs]] for data lineage and governance, identity / [[entity-resolution|entity resolution]] graphs for master data and KYC, pattern-detection graphs for fraud rings and skills matching, dependency graphs for impact and root-cause analysis, and semantic search and similarity over unstructured text (including [[semantic-similarity|path, Leacock-Chodorow and Wu-Palmer similarity]] over WordNet). A capstone chapter on 'Talking to Your Knowledge Graph' connects the work to large language models, showing how an annotated ontology can drive natural language generation and ground LLM answers in graph facts to reduce hallucination.

The book closes with a forward-looking chapter on the [[knowledge-lake|knowledge lake]] — a foundational, enterprise-wide knowledge graph that sits beside data lakes and warehouses and subsumes departmental graphs. It is opinionated (Neo4j-centric, property-graph-first) and aimed at engineers and architects who want to build production knowledge graphs rather than reason abstractly about the Semantic Web.

## Key Contributions

- Codifies a four-level hierarchy of 'organising principles' for knowledge graphs: plain graphs, richer (labeled property) graphs, taxonomies, and ontologies — with explicit guidance to prefer 'just-enough semantics' over up-front ontological perfectionism
- Provides a reusable seven-archetype catalogue of knowledge-graph use cases (integration/search, metadata, identity, pattern detection, dependency, semantic search, conversational) each with Cypher implementations and architectural diagrams
- Reframes RDF as an exchange format rather than a storage requirement, decoupling knowledge graphs from the Semantic Web stack and grounding them in the property graph model
- Demonstrates a graph-based entity-resolution pipeline (data preparation → blocking keys → matching → persisted golden records via WCC) as an alternative to traditional MDM
- Introduces the 'knowledge lake' as an architectural pattern: a foundational, curated knowledge graph layered atop existing data lakes and warehouses to give meaning to bulk data after the fact
- Shows how an annotated ontology (using talk:direct / talk:inverse predicates) can drive both natural language querying and natural language generation directly from Cypher, anticipating LLM-grounding patterns

## Key Topics Covered

knowledge-graph, property-graph-model, cypher-query-language, rdf, ontology, taxonomy, graph-databases, neo4j, graph-data-science, graph-native-machine-learning, entity-resolution, metadata-knowledge-graph, fraud-detection, dependency-modeling, semantic-search, semantic-similarity, wordnet, natural-language-generation, knowledge-lake

## Questions Raised

- How should knowledge graphs be governed at enterprise scale to avoid 'recursive knowledge graphs all the way down' once they proliferate?
- Where is the right boundary between ontology-driven reasoning and machine-learning-driven enrichment of a knowledge graph?
- How can in-graph ML pipelines reach the modelling depth of external frameworks (PyTorch, TensorFlow, SageMaker) without losing the round-trip benefits of staying inside the graph?
- How exactly do knowledge graphs 'tame the hallucinatory nature of LLMs' — beyond the prototype shown, what production patterns and evaluation metrics apply?
- When standard ontologies (SNOMED CT, FIBO, schema.org) only partially fit a domain, how should organisations version and evolve hybrid in-house ontologies over time?

## Intended Audience

Software engineers, data engineers, data scientists, and solutions architects who want to build and operate production knowledge graphs (with Neo4j-flavoured tooling), plus technical managers and CIO/CDO readers seeking a deeper follow-up to the authors' earlier business-oriented Knowledge Graphs report.

## Key Concepts in This Source

- [[concepts/knowledge-graph|Knowledge Graph]]
- [[concepts/property-graph-model|Property Graph Model]]
- [[concepts/cypher-query-language|Cypher Query Language]]
- [[concepts/rdf|Resource Description Framework]]
- [[concepts/ontology|Ontology]]
- [[concepts/taxonomy|Taxonomy]]
- [[concepts/entity-resolution|Entity Resolution]]
- [[concepts/graph-data-science|Graph Data Science]]
- [[concepts/graph-native-machine-learning|Graph-Native Machine Learning]]
- [[concepts/metadata-knowledge-graph|Metadata Knowledge Graph]]
- [[concepts/knowledge-lake|Knowledge Lake]]
- [[concepts/semantic-similarity|Semantic Similarity]]

## Entities

- [[entities/jesus-barrasa|Jesus Barrasa]]
- [[entities/jim-webber|Jim Webber]]
- [[entities/neo4j|Neo4j]]
- [[entities/nicola-vitucci|Nicola Vitucci]]
- [[entities/maya-natarajan|Maya Natarajan]]
- [[entities/apache-kafka|Apache Kafka]]
- [[entities/apache-spark|Apache Spark]]
- [[entities/wordnet|WordNet]]
- [[entities/spacy|spaCy]]
- [[entities/rasa|Rasa]]

<!-- AUTHORED REGION END -->
