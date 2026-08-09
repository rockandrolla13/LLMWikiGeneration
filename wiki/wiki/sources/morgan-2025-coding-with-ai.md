---
title: Coding with AI
page_id: sources/morgan-2025-coding-with-ai
page_type: source
verification:
  status: unverified
  unverified_claims: 0
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_technical_books_2026_06_19
tags:
- ai-coding-tools
- github-copilot
- chatgpt
- software-development
- llm-applications
- developer-productivity
sources:
- sources/morgan-2025-coding-with-ai
related: []
mind_map_priority: medium
authors:
- Jeremy C. Morgan
year: 2025
source_type: book
schema_version: 2
uuid: 49b1720b-b924-50e1-9d9a-add587d9b52b
content_hash: sha256:498b9e59829e01c63f9a9ff865fa3332e7943b4bd3f0332733ffaa63c1fb8f64
---

<!-- AUTHORED REGION START -->
# Coding with AI

**Authors:** Jeremy C. Morgan  
**Year:** 2025  
**Type:** book  
**Markdown source:** none retained. This page was written by a 2026-06-19 batch ingest that recorded `markdown_output/morgan-2025-coding-with-ai.md`, which was never produced. Claims here are not machine-checkable until the document is converted.
## Summary

Coding with AI (MEAP edition) by Jeremy C. Morgan, published by Manning Publications, is a practical guide to integrating AI coding assistants into the software development workflow. The book covers how large language models power generative AI tools like GitHub Copilot and ChatGPT, contrasting them with traditional rule-based code completion. It walks through AI assistance at each phase of the software development lifecycle — from ideation and technology selection through code generation, code review and analysis, testing and debugging, documentation generation, and deployment — using a running project example (a Flask-based ham radio practice web app) to illustrate concepts hands-on. NOTE: The markdown source file is severely degraded; the PDF-to-markdown conversion extracted only images and table fragments, leaving the body text inaccessible as markdown. No table of contents or preface text was recoverable from the file. This summary is based solely on what was directly observable in extracted images and the sparse readable table data.

## Key Claims

- AI-assisted documentation reduces task time by 75-83% compared to traditional methods across tasks such as system overview, technical stack docs, user stories, and complete design documents (from a table in the book, ChatGPT-Assisted column vs Traditional Method)
- Generative AI for coding differs from traditional code completion in that it uses deep learning from vast internet-sourced code rather than pre-defined language rules, and operates at the scope of code files, blocks, functions, and libraries rather than just keywords
- GitHub Copilot is shown using the OpenAI Codex model as its backend, integrated via a plugin into Visual Studio Code, with a feedback loop between the editor context and model suggestions
- AI tools can assist at every phase of the SDLC: ideation/planning, technology selection, code generation, code review, testing/debugging, documentation, and deployment/maintenance
- The book uses a concrete running project (HAM-RADIO-PRACTICE-WEB, a Flask web app) to demonstrate AI-assisted development including route generation, SQLite data models, Jinja2 templates, and pytest unit tests
- A proxy server with toxicity filter is presented as a recommended architecture for routing code editor requests through to an LLM, applied both for incoming user prompts and outgoing LLM responses
- The TOC was not recoverable from the markdown file — text content is stored as page images that the PDF extractor could not decode

## Main Concepts

- AI-assisted code generation vs traditional code completion
- GitHub Copilot and LLM-powered coding assistants
- Software development lifecycle (SDLC) integration with AI
- Prompt engineering for code and documentation tasks
- Toxicity filtering and proxy architecture for LLM API access
- Automated documentation generation with ChatGPT
- Unit testing and test generation with AI assistance

## Key Entities

- Jeremy C. Morgan (author)
- Manning Publications (publisher)
- GitHub Copilot (OpenAI Codex-backed tool, shown in VS Code)
- ChatGPT / OpenAI (shown via ChatGPT 4 interface screenshots)
- Visual Studio Code (IDE used throughout examples)

## Questions Raised

- How does the book handle AI hallucination and incorrect code suggestions — what verification workflow does it recommend beyond 'you verify output'?
- Does the book address security risks of sending proprietary code through external LLM APIs, given the proxy/toxicity filter architecture shown?
- The MEAP (Manning Early Access Program) label on the file suggests this was a pre-publication draft — what chapters were complete at time of conversion?

<!-- AUTHORED REGION END -->
