---
title: Hands-on Small Language Models
page_id: sources/thomas-2025-hands-on-small-language-models
page_type: source
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_technical_books_2_2026_06_19
tags:
- small-language-models
- slm
- agentic-applications
- mcp
- ollama
- litellm
- rag
- wikidata
- knowledge-graphs
- practical-ml
- oreilly
- python
- docker
- huggingface
- sparql
- nlp
sources:
- sources/thomas-2025-hands-on-small-language-models
related: []
mind_map_priority: medium
authors:
- Alexander Thomas
year: 2025
source_type: book
schema_version: 2
uuid: 9d2fad09-0235-5558-b5fa-94b5855fc251
content_hash: sha256:4c58a50da17f13088091fdf5f9dc48ec562bf31fa88c10973225cd82b350435b
---

<!-- AUTHORED REGION START -->
# Hands-on Small Language Models

**Authors:** Alexander Thomas  
**Year:** 2025  
**Type:** book  
**Markdown source:** `markdown_output/thomas-2025-hands-on-small-language-models.md`

## Summary

Early-release O'Reilly book (first release 2026-01-21, first edition January 2027) by Alexander N. Thomas on building practical agentic applications using Small Language Models (SLMs). The available portion covers the book's table of contents, environment setup, and an introductory hands-on project called "Theoros" — a movie-search agentic system used as a throughline example. The book demonstrates how to combine SLMs with MCP (Model Context Protocol), Ollama, LiteLLM, LibreChat, and external data sources (Wikipedia, Wikidata, HuggingFace, Kaggle). Only Chapters 2 and 3 were available in the early release; Chapters 1 and 4–8 were listed but marked unavailable at time of extraction.

## Key Claims

- SLMs can run on commodity hardware including mobile and edge devices, making them more accessible than LLMs
- MCP (Model Context Protocol) from Anthropic is an open-source standard for connecting AI applications to external systems and is growing in adoption
- LiteLLM abstracts access to different model families, allowing local-to-hosted model switching via minor configuration changes
- Ollama exposes locally-run language models through an OpenAI-compatible API
- SPARQL generation via SLMs is unreliable because models have limited training data on SPARQL and Wikidata-specific patterns
- Wikidata uses RDF semantic triples (subject-predicate-object) to represent entity relationships and properties
- The book deliberately avoids datasets with personally identifying information to keep the focus on SLM mechanics
- LibreChat is used instead of Claude Desktop because it is not tied to a specific model family while still supporting MCP integration

## Main Concepts

- Small Language Models (SLMs)
- Agentic applications
- Model Context Protocol (MCP)
- Retrieval Augmented Generation (RAG)
- Ollama for local model serving
- LiteLLM as a model abstraction layer
- Wikidata / RDF / SPARQL
- Python Data Science Stack (NumPy, SciPy, pandas, Matplotlib, scikit-learn, Jupyter)
- Knowledge graphs
- Containerisation with Docker
- OpenRouter as a hosted model gateway
- Environment management with conda/miniconda

## Key Entities

- Alexander N. Thomas (author)
- O'Reilly Media (publisher)
- Nicole Butterfield (acquisitions editor)
- Michele Cronin (development editor)
- Anthropic (creator of MCP)
- Ollama (local model serving framework)
- LiteLLM (multi-provider LLM abstraction library)
- LibreChat (open-source chat application)
- OpenRouter (hosted multi-model API gateway)
- HuggingFace (model and dataset platform)
- Kaggle (ML competition and dataset platform)
- Wikimedia Foundation (Wikipedia and Wikidata)
- Anaconda / Miniconda (Python package manager)
- Docker (containerisation platform)

## Questions Raised

- Which SLM families are benchmarked in Chapter 3 (Selecting the Right Small Language Model)?
- How does the book handle security and privacy when SLMs are used with sensitive data, given the project deliberately avoids PII?
- What deployment targets are covered in Chapter 7 (edge, cloud, on-premise)?
- What compliance frameworks are addressed in Chapter 6 (Testing and Compliance)?
- How does the book compare multiple SLMs orchestrated together in Chapter 5?
- Is the Theoros codebase publicly available in a GitHub repository?
- The ISBN listed (979-8-341-67068-6) differs slightly from the errata URL ISBN (9798341670723) — which is correct?

<!-- AUTHORED REGION END -->
