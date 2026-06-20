---
title: Hands-On RAG for Production
page_id: sources/mendelevitch-2025-hands-on-rag
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Ofer Mendelevitch
- Forrest Bao
year: 2025
publisher: O'Reilly Media
edition: Early Release
is_early_release: true
page_count_estimate: 80
tags:
- ai-engineering
- rag
related:
- concepts/agentic-rag
- concepts/chunking
- concepts/embeddings
- concepts/graph-rag
- concepts/hybrid-search
- concepts/llm-hallucination
- concepts/multimodal-rag
- concepts/prompt-injection
- concepts/rag-evaluation
- concepts/reranking
- concepts/retrieval-augmented-generation
- concepts/semantic-search
- concepts/vector-database
- entities/anthropic
- entities/forrest-bao
- entities/meta-ai
- entities/microsoft
- entities/ofer-mendelevitch
- entities/openai
- entities/patrick-lewis
- entities/vectara
mind_map_priority: medium
revision_hash: sha256:87cbf327acc6df2b
schema_version: 2
uuid: 512fefe9-82ed-5a8f-8b39-873adece21c6
content_hash: sha256:76a4767f2d60204c527584e53bad9a9d8a5b1643c847952fbcfb450675844406
---

<!-- AUTHORED REGION START -->
# Hands-On RAG for Production
*Design, Develop, and Deploy*

**Authors:** [[entities/ofer-mendelevitch|Ofer Mendelevitch]], [[entities/forrest-bao|Forrest Bao]]

**Year:** 2025

**Publisher:** O'Reilly Media

**Edition:** Early Release

## Summary

Hands-On RAG for Production is an O'Reilly Early Release (May 2025, first full edition planned for June 2026) by Ofer Mendelevitch and Forrest Bao of Vectara. It argues that while a [[retrieval-augmented-generation|RAG]] proof-of-concept is easy to build by gluing together an [[embeddings|embedding model]], a [[vector-database|vector database]], and an LLM, getting RAG to enterprise production is qualitatively harder along axes of response quality, latency, security, vendor integration, team expertise, and total cost of ownership. The book is structured around the gap between POC and production, with Chapter 1 introducing the RAG architecture (ingest flow, query flow, guardrails) and Chapter 4 (printed second in the Early Release) walking through the operational challenges and KPIs that accompany a production rollout.

The authors position RAG against alternatives such as chat-with-PDF and [[llm-hallucination|fine-tuning]], arguing that RAG is uniquely well suited to enterprise constraints because it supports access control via metadata filtering, instant knowledge addition and removal, and citation-grounded responses. They then preview advanced topics: [[hybrid-search|hybrid search]], [[reranking|reranking]], [[chunking|chunking]] strategies, [[agentic-rag|Agentic RAG]], [[multimodal-rag|Multimodal RAG]], and [[graph-rag|GraphRAG]]. Security is treated as a defense-in-depth problem across the ingestion layer, vector store, and generation step, including [[prompt-injection|prompt injection]] mitigation and RBAC over private corpora.

The intended audience is ML engineers, platform engineers, and enterprise architects who already know what RAG is and now need to ship it. The book is unusually opinionated about the value of turnkey RAG platforms (reflecting Vectara's perspective), and provides concrete production KPI tables ([[rag-evaluation|RAG evaluation]] metrics like context precision, context recall, hallucination rate, answer relevance) that readers can adapt as acceptance criteria. As an Early Release, several chapters are listed but unavailable; this extraction is based on the two chapters released (Chapter 1: Introduction, and Chapter 4: Deploying RAG to Production).

## Key Contributions

- A clear two-flow blueprint of a production RAG stack: an ingest flow (extract, chunk, embed, store) and a query flow (retrieve, rerank, generate, guardrail) — used as the spine of the rest of the book.
- A framing of POC-to-production as the central problem, with an explicit catalog of failure modes: no relevant data, weak retrieval pipeline, LLM hallucinations, and prompt design.
- A defense-in-depth security model for RAG across three attack surfaces (ingestion layer, vector store, generation step) including RBAC, PII redaction, and prompt injection mitigation.
- A concrete production KPI table (query latency mean/median, uptime, context precision/recall, hallucination rate, answer relevance, supported chunking/retrieval strategies) that operationalizes 'good RAG' as measurable acceptance criteria.
- A pragmatic case for turnkey RAG platforms versus DIY assembly, arguing that integration cost, vendor sprawl, and TCO (3-5x over initial estimates) often dominate the build-vs-buy decision.

## Key Topics Covered

RAG architecture and ingest/query flows, RAG vs chat-with-PDF and fine-tuning, Vector databases and semantic search, Hybrid search and reranking, Chunking strategies, LLM hallucinations and mitigation, RAG evaluation metrics, Production security: RBAC, PII, prompt injection, Agentic RAG, Multimodal RAG, GraphRAG, Total cost of ownership and team composition

## Questions Raised

- Which chunking strategies (fixed, semantic, layout-aware, agentic) actually win on which document types, and how should that be benchmarked?
- How should hallucination detectors be evaluated and calibrated when ground-truth faithfulness exists on a 'spectrum of factuality' rather than a binary?
- What is the right way to combine RBAC metadata filtering with semantic retrieval without leaking information through ranking signals?
- When does GraphRAG actually outperform well-tuned hybrid search, and at what data-volume threshold does the knowledge-graph build cost pay off?
- How should organizations evaluate the build-vs-buy tradeoff between DIY RAG stacks and turnkey platforms in a way that is not biased by vendor framing?

## Intended Audience

ML engineers, platform engineers, and enterprise architects who have built a RAG proof-of-concept and now need to ship a scalable, secure, observable production RAG system.

## Key Concepts in This Source

- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[concepts/vector-database|Vector Database]]
- [[concepts/embeddings|Embeddings]]
- [[concepts/semantic-search|Semantic Search]]
- [[concepts/hybrid-search|Hybrid Search]]
- [[concepts/reranking|Reranking]]
- [[concepts/chunking|Chunking]]
- [[concepts/llm-hallucination|LLM Hallucination]]
- [[concepts/agentic-rag|Agentic RAG]]
- [[concepts/graph-rag|GraphRAG]]
- [[concepts/prompt-injection|Prompt Injection]]
- [[concepts/rag-evaluation|RAG Evaluation]]
- [[concepts/multimodal-rag|Multimodal RAG]]

## Entities

- [[entities/ofer-mendelevitch|Ofer Mendelevitch]]
- [[entities/forrest-bao|Forrest Bao]]
- [[entities/vectara|Vectara]]
- [[entities/patrick-lewis|Patrick Lewis]]
- [[entities/meta-ai|Meta AI]]
- [[entities/microsoft|Microsoft]]
- [[entities/openai|OpenAI]]
- [[entities/anthropic|Anthropic]]

<!-- AUTHORED REGION END -->
