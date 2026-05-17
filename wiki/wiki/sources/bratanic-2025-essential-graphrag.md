---
title: Essential GraphRAG
page_id: sources/bratanic-2025-essential-graphrag
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Tomaz Bratanic
- Oskar Hane
year: 2025
publisher: Manning
edition: 1st
is_early_release: false
page_count_estimate: 180
tags:
- ai-engineering
- rag
related:
- concepts/agentic-rag
- concepts/community-detection-graphrag
- concepts/entity-resolution
- concepts/graphrag
- concepts/hybrid-search
- concepts/knowledge-graph-construction
- concepts/parent-document-retrieval
- concepts/rag-evaluation
- concepts/retrieval-augmented-generation
- concepts/step-back-prompting
- concepts/text-to-cypher
- concepts/vector-similarity-search
- entities/arturo-geigel
- entities/ashish-vaswani
- entities/langchain
- entities/llamaindex
- entities/microsoft-graphrag
- entities/neo4j
- entities/openai
- entities/oskar-hane
- entities/paco-nathan
- entities/tomaz-bratanic
mind_map_priority: medium
revision_hash: sha256:8183d1362d61b136
---

# Essential GraphRAG
*Knowledge Graph-Enhanced RAG*

**Authors:** [[entities/tomaz-bratanic|Tomaz Bratanic]], [[entities/oskar-hane|Oskar Hane]]

**Year:** 2025

**Publisher:** Manning

**Edition:** 1st

## Summary

Essential GraphRAG argues that vanilla [[retrieval-augmented-generation|retrieval-augmented generation]] over unstructured text chunks leaves accuracy on the table, and that pairing LLMs with a [[knowledge-graph-construction|knowledge graph]] yields more precise, context-rich, and explainable retrieval. Bratanic and Hane, both from Neo4j, take readers through building a [[graphrag|GraphRAG]] system from scratch without leaning on existing frameworks, starting from baseline RAG with [[vector-similarity-search|vector similarity search]] and [[hybrid-search|hybrid search]] in Neo4j and progressively layering on advanced retrieval strategies, query-language generation, and agent orchestration.

The middle chapters develop the core GraphRAG toolkit. Chapter 3 introduces [[step-back-prompting|step-back prompting]] and [[parent-document-retrieval|parent document retrieval]] to fix recall and context-loss failure modes. Chapter 4 implements [[text-to-cypher|text-to-Cypher]] generation using schema-in-prompt, few-shot examples, and terminology maps, then contrasts a base-model approach with a finetuned specialist. Chapter 5 builds [[agentic-rag|agentic RAG]] from retriever tools, a router, and an answer critic. Chapter 6 walks through [[knowledge-graph-construction|knowledge graph construction]] from legal contracts (CUAD) using OpenAI Structured Outputs and [[entity-resolution|entity resolution]] in Neo4j. Chapter 7 is a full reproduction of [[microsoft-graphrag|Microsoft's GraphRAG]] over The Odyssey, featuring hierarchical [[community-detection-graphrag|community detection]], LLM-based community summarisation, and global vs local search.

The book closes with practical [[rag-evaluation|RAG evaluation]] using benchmark datasets and metrics for context recall, faithfulness, and answer correctness. It is aimed at engineers who already understand basic RAG and want stable architectural patterns for production GraphRAG, rather than at researchers looking for novel algorithms. Its angle versus competitors is that it is framework-light, Neo4j-grounded, and explicit about the tradeoffs between vector, graph, and hybrid retrieval paths.

## Key Contributions

- A from-scratch GraphRAG reference implementation in Neo4j that does not depend on LangChain or LlamaIndex orchestration, exposing every retrieval and prompting step.
- A clear taxonomy of retrieval strategies (vector, full-text, hybrid, step-back, parent document, text-to-Cypher, agentic) with guidance on when each one wins.
- A reproducible walkthrough of Microsoft's GraphRAG pipeline (chunking to community summarisation to global/local search) using The Odyssey as a small corpus.
- A practical recipe for LLM-based knowledge-graph construction from unstructured contracts via OpenAI Structured Outputs plus entity resolution.
- An evaluation pattern for GraphRAG systems centred on context recall, faithfulness, and answer correctness, with a reusable benchmark-design template.

## Key Topics Covered

LLM limitations (knowledge cutoff, hallucination, private data), Vector similarity search and hybrid search in Neo4j, Step-back prompting and parent document retrieval, Text-to-Cypher generation with schema and few-shot prompting, Agentic RAG (retriever tools, routing, answer critic), LLM-based knowledge graph construction and entity resolution, Microsoft GraphRAG: community detection and global/local search, RAG evaluation metrics and benchmark design

## Questions Raised

- How does GraphRAG scale to corpora orders of magnitude larger than The Odyssey, where community summarisation costs dominate?
- When is investing in a maintained knowledge graph cheaper than simply scaling vector retrieval with better chunking and rerankers?
- How should entity resolution be handled when extraction is performed incrementally over a streaming corpus rather than a one-shot batch?
- What is the right division of labour between a finetuned text-to-Cypher model and a general-purpose LLM with schema-in-prompt as schemas grow?
- How do you evaluate agentic GraphRAG end-to-end when answer critics and routers are themselves LLM-driven and non-deterministic?

## Intended Audience

Data scientists, software engineers, and ML developers with a working knowledge of Python and LLMs who want to add knowledge graphs to their RAG stack and build production-grade GraphRAG systems without relying on framework abstractions.

## Key Concepts in This Source

- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[concepts/graphrag|GraphRAG]]
- [[concepts/knowledge-graph-construction|Knowledge Graph Construction]]
- [[concepts/vector-similarity-search|Vector Similarity Search]]
- [[concepts/hybrid-search|Hybrid Search]]
- [[concepts/text-to-cypher|Text-to-Cypher Generation]]
- [[concepts/agentic-rag|Agentic RAG]]
- [[concepts/community-detection-graphrag|Community Detection for GraphRAG]]
- [[concepts/parent-document-retrieval|Parent Document Retrieval]]
- [[concepts/step-back-prompting|Step-Back Prompting]]
- [[concepts/entity-resolution|Entity Resolution]]
- [[concepts/rag-evaluation|RAG Evaluation]]

## Entities

- [[entities/tomaz-bratanic|Tomaz Bratanic]]
- [[entities/oskar-hane|Oskar Hane]]
- [[entities/paco-nathan|Paco Nathan]]
- [[entities/neo4j|Neo4j]]
- [[entities/microsoft-graphrag|Microsoft GraphRAG]]
- [[entities/langchain|LangChain]]
- [[entities/llamaindex|LlamaIndex]]
- [[entities/ashish-vaswani|Ashish Vaswani]]
- [[entities/openai|OpenAI]]
- [[entities/arturo-geigel|Arturo Geigel]]
