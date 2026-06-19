---
title: "Hands-on Small Language Models"
page_id: sources/thomas-2025-hands-on-small-language-models
page_type: source
revision_id: 1
created: 2026-06-19T00:00:00Z
updated: 2026-06-19T00:00:00Z
updated_by: batch_ingest_technical_books_2_2026_06_19
tags: [small-language-models, slm, agentic-applications, mcp, ollama, litellm, rag, wikidata, knowledge-graphs, practical-ml, oreilly, python, docker, huggingface, sparql, nlp]
sources: [sources/thomas-2025-hands-on-small-language-models]
related: []
mind_map_priority: medium
authors: ["Alexander Thomas"]
year: 2025
source_type: book
---

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

- [[concepts/small-language-models-slms-|Small Language Models (SLMs)]]
- [[concepts/agentic-applications|Agentic applications]]
- [[concepts/model-context-protocol-mcp-|Model Context Protocol (MCP)]]
- [[concepts/retrieval-augmented-generation-rag-|Retrieval Augmented Generation (RAG)]]
- [[concepts/ollama-for-local-model-serving|Ollama for local model serving]]
- [[concepts/litellm-as-a-model-abstraction-layer|LiteLLM as a model abstraction layer]]
- [[concepts/wikidata-rdf-sparql|Wikidata / RDF / SPARQL]]
- [[concepts/python-data-science-stack-numpy-scipy-pandas-matplotlib-scikit-learn-jupyter-|Python Data Science Stack (NumPy, SciPy, pandas, Matplotlib, scikit-learn, Jupyter)]]
- [[concepts/knowledge-graphs|Knowledge graphs]]
- [[concepts/containerisation-with-docker|Containerisation with Docker]]
- [[concepts/openrouter-as-a-hosted-model-gateway|OpenRouter as a hosted model gateway]]
- [[concepts/environment-management-with-conda-miniconda|Environment management with conda/miniconda]]

## Key Entities

- [[entities/alexander-n-thomas-author-|Alexander N. Thomas (author)]]
- [[entities/o-reilly-media-publisher-|O'Reilly Media (publisher)]]
- [[entities/nicole-butterfield-acquisitions-editor-|Nicole Butterfield (acquisitions editor)]]
- [[entities/michele-cronin-development-editor-|Michele Cronin (development editor)]]
- [[entities/anthropic-creator-of-mcp-|Anthropic (creator of MCP)]]
- [[entities/ollama-local-model-serving-framework-|Ollama (local model serving framework)]]
- [[entities/litellm-multi-provider-llm-abstraction-library-|LiteLLM (multi-provider LLM abstraction library)]]
- [[entities/librechat-open-source-chat-application-|LibreChat (open-source chat application)]]
- [[entities/openrouter-hosted-multi-model-api-gateway-|OpenRouter (hosted multi-model API gateway)]]
- [[entities/huggingface-model-and-dataset-platform-|HuggingFace (model and dataset platform)]]
- [[entities/kaggle-ml-competition-and-dataset-platform-|Kaggle (ML competition and dataset platform)]]
- [[entities/wikimedia-foundation-wikipedia-and-wikidata-|Wikimedia Foundation (Wikipedia and Wikidata)]]
- [[entities/anaconda-miniconda-python-package-manager-|Anaconda / Miniconda (Python package manager)]]
- [[entities/docker-containerisation-platform-|Docker (containerisation platform)]]

## Questions Raised

- Which SLM families are benchmarked in Chapter 3 (Selecting the Right Small Language Model)?
- How does the book handle security and privacy when SLMs are used with sensitive data, given the project deliberately avoids PII?
- What deployment targets are covered in Chapter 7 (edge, cloud, on-premise)?
- What compliance frameworks are addressed in Chapter 6 (Testing and Compliance)?
- How does the book compare multiple SLMs orchestrated together in Chapter 5?
- Is the Theoros codebase publicly available in a GitHub repository?
- The ISBN listed (979-8-341-67068-6) differs slightly from the errata URL ISBN (9798341670723) — which is correct?
