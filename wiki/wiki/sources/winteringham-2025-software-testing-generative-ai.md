---
title: Software Testing with Generative AI
page_id: sources/winteringham-2025-software-testing-generative-ai
page_type: source
verification:
  status: unverified
  unverified_claims: 0
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_5_2026_06_19
tags:
- software-testing
- generative-ai
- llm
- prompt-engineering
- test-automation
- rag
- fine-tuning
- ai-agents
- tdd
- exploratory-testing
- test-data
- ui-automation
- openai
- manning
- 2025
sources:
- sources/winteringham-2025-software-testing-generative-ai
related: []
mind_map_priority: medium
authors:
- Mark Winteringham
year: 2025
source_type: book
schema_version: 2
uuid: 6a6f43e0-b554-587e-b94d-0bd174749a4d
content_hash: sha256:6e8e09ab68adfcb12324e3ea7f0cf6aee5a3bd460e1a5ad56a82d1f0e8d64ee2
---

<!-- AUTHORED REGION START -->
# Software Testing with Generative AI

**Authors:** Mark Winteringham  
**Year:** 2025  
**Type:** book  
**Markdown source:** none retained. This page was written by a 2026-06-19 batch ingest that recorded `markdown_output/winteringham-2025-software-testing-generative-ai.md`, which was never produced. Claims here are not machine-checkable until the document is converted.
## Summary

Software Testing with Generative AI (2025) by Mark Winteringham, published by Manning Publications, is a practical guide for software testers and developers on integrating large language models (LLMs) into the software testing lifecycle. The book is organised around three tenets — Mindset, Technique, and Context — covering how to establish a productive relationship with LLMs, apply them to specific testing tasks via prompt engineering, and customise them with RAG and fine-tuning for domain-specific testing contexts. It spans 12 chapters across three parts, with a foreword by Nicola Martin.

## Key Claims

- Success with LLMs in testing depends on three pillars: Mindset, Technique, and Context
- LLMs carry risks including hallucinations, data provenance issues, and data privacy concerns that testers must actively manage
- Prompt engineering principles (clear instructions, structured output, few-shot prompting, giving the model time to think) significantly improve LLM output quality
- LLMs should be applied selectively to testing tasks based on their generative, transformation, and enhancing capabilities
- AI agents can serve as testing assistants by chaining tools and executing functions autonomously
- RAG and fine-tuning are complementary approaches to contextualising LLMs for domain-specific testing
- Automation bias is a real risk; testers must remain skeptical of LLM-generated outputs including risks and test cases
- A healthy skepticism of generated risks and test cases is essential to maintaining test quality

## Main Concepts

- Large Language Models (LLMs)
- [[concepts/prompt-engineering|Prompt engineering]]
- [[concepts/few-shot-prompting|Few-shot prompting]]
- Test-driven development (TDD) with LLMs
- AI-assisted test planning
- Test data generation and transformation
- UI automation with AI
- Exploratory testing augmented by AI
- AI agents as testing assistants
- Retrieval-Augmented Generation (RAG)
- Fine-tuning LLMs
- [[concepts/vector-databases|Vector databases]]
- Context windows and token limitations
- Automation bias
- Hallucinations in LLMs
- Data provenance
- Data privacy

## Key Entities

- Mark Winteringham (author)
- Nicola Martin (foreword author)
- Manning Publications (publisher)
- OpenAI (mentioned in context of test data management setup)
- Sam Moore (dedication)
- Becky Whitney (development editor)
- Robert Walsh (technical editor)
- Kishor Rit (review editor)
- Kathy Rossland (production editor)
- Lana Todorovic-Arndt (copy editor)
- Olga Milanko (proofreader)
- Tamara Svelic Sabljic (typesetter)
- Marija Tudor (cover designer)

## Questions Raised

- How should testers evaluate and choose between competing LLMs for specific testing tasks?
- What are the practical limits of LLM context windows in real testing scenarios and how does RAG overcome them?
- When is fine-tuning preferable to RAG for domain-specific testing contexts?
- How can teams guard against automation bias when using AI-generated test cases and risk lists?
- What does a mature AI test assistant look like beyond the toy examples in the book?
- How does the book's three-tenet model (Mindset/Technique/Context) hold up across different organisational testing maturity levels?

<!-- AUTHORED REGION END -->
