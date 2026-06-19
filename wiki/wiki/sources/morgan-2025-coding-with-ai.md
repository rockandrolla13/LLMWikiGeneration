---
title: "Coding with AI"
page_id: sources/morgan-2025-coding-with-ai
page_type: source
revision_id: 1
created: 2026-06-19T00:00:00Z
updated: 2026-06-19T00:00:00Z
updated_by: batch_ingest_technical_books_2026_06_19
tags: [ai-coding-tools, github-copilot, chatgpt, software-development, llm-applications, developer-productivity]
sources: [sources/morgan-2025-coding-with-ai]
related: []
mind_map_priority: medium
authors: ["Jeremy C. Morgan"]
year: 2025
source_type: book
---

# Coding with AI

**Authors:** Jeremy C. Morgan  
**Year:** 2025  
**Type:** book  
**Markdown source:** `markdown_output/morgan-2025-coding-with-ai.md`

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

- [[concepts/ai-assisted-code-generation-vs-traditional-code-completion|AI-assisted code generation vs traditional code completion]]
- [[concepts/github-copilot-and-llm-powered-coding-assistants|GitHub Copilot and LLM-powered coding assistants]]
- [[concepts/software-development-lifecycle-(sdlc)-integration-with-ai|Software development lifecycle (SDLC) integration with AI]]
- [[concepts/prompt-engineering-for-code-and-documentation-tasks|Prompt engineering for code and documentation tasks]]
- [[concepts/toxicity-filtering-and-proxy-architecture-for-llm-api-access|Toxicity filtering and proxy architecture for LLM API access]]
- [[concepts/automated-documentation-generation-with-chatgpt|Automated documentation generation with ChatGPT]]
- [[concepts/unit-testing-and-test-generation-with-ai-assistance|Unit testing and test generation with AI assistance]]

## Key Entities

- [[entities/jeremy-c-morgan-author-|Jeremy C. Morgan (author)]]
- [[entities/manning-publications-publisher-|Manning Publications (publisher)]]
- [[entities/github-copilot-openai-codex-backed-tool-shown-in-vs-code-|GitHub Copilot (OpenAI Codex-backed tool, shown in VS Code)]]
- [[entities/chatgpt-openai-shown-via-chatgpt-4-interface-screenshots-|ChatGPT / OpenAI (shown via ChatGPT 4 interface screenshots)]]
- [[entities/visual-studio-code-ide-used-throughout-examples-|Visual Studio Code (IDE used throughout examples)]]

## Questions Raised

- How does the book handle AI hallucination and incorrect code suggestions — what verification workflow does it recommend beyond 'you verify output'?
- Does the book address security risks of sending proprietary code through external LLM APIs, given the proxy/toxicity filter architecture shown?
- The MEAP (Manning Early Access Program) label on the file suggests this was a pre-publication draft — what chapters were complete at time of conversion?
