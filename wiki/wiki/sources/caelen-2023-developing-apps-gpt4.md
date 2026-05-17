---
title: Developing Apps with GPT-4 and ChatGPT
page_id: sources/caelen-2023-developing-apps-gpt4
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Olivier Caelen
- Marie-Alice Blete
year: 2023
publisher: O'Reilly Media
edition: 1st
is_early_release: false
page_count_estimate: 180
tags:
- ai-engineering
related:
- concepts/ai-hallucination
- concepts/chain-of-thought-prompting
- concepts/chatgpt
- concepts/embeddings
- concepts/few-shot-learning
- concepts/fine-tuning
- concepts/function-calling
- concepts/gpt-4
- concepts/gpt-plugins
- concepts/langchain
- concepts/large-language-models
- concepts/openai-api
- concepts/prompt-engineering
- concepts/prompt-injection
- concepts/retrieval-augmented-generation
- concepts/rlhf
- concepts/tokenization
- concepts/vector-database
- entities/faiss
- entities/langchain
- entities/marie-alice-blete
- entities/olivier-caelen
- entities/openai
- entities/tom-taulli
- entities/worldline
mind_map_priority: medium
revision_hash: sha256:1828104a73669f4b
---

# Developing Apps with GPT-4 and ChatGPT
*Build Intelligent Chatbots, Content Generators, and More*

**Authors:** [[entities/olivier-caelen|Olivier Caelen]], [[entities/marie-alice-blete|Marie-Alice Blete]]

**Year:** 2023

**Publisher:** O'Reilly Media

**Edition:** 1st

## Summary

Developing Apps with GPT-4 and ChatGPT is a short, hands-on O'Reilly book aimed at developers who want to ship production-grade applications on top of [[openai-api|OpenAI's hosted models]]. Caelen and Blete combine a researcher's and a software architect's perspective to cover the full surface: what [[large-language-models|LLMs]] are and how [[transformers|transformers]] and [[tokenization|tokenization]] work; how GPT evolved from GPT-1 through GPT-3, [[rlhf|RLHF]]-aligned InstructGPT, [[chatgpt|ChatGPT]], and [[gpt-4|GPT-4]]; and how to call each model through the Python SDK, manage token budgets, and reason about pricing.

The middle of the book is operational. It walks through API key management, security and privacy of user data, [[prompt-injection|prompt injection]] and other LLM-app vulnerabilities, and software architecture patterns for LLM-backed services, then builds four example projects: a news generator, a YouTube video summarizer, a Zelda-domain expert with a Redis-backed knowledge service, and a voice-controlled assistant using Whisper and Gradio. Chapter 4 systematizes [[prompt-engineering|prompt engineering]] (context, task, role, [[chain-of-thought-prompting|step-by-step reasoning]], [[few-shot-learning|few-shot examples]], output formatting, negative prompts) and contrasts it with [[fine-tuning|fine-tuning]] on synthetic email-marketing data.

Chapter 5 extends the model with [[langchain|LangChain]] (dynamic prompts, agents and tools, conversational memory, document loaders, [[embeddings|embeddings]], and [[retrieval-augmented-generation|retrieval-augmented question answering]] over a PDF stored in [[vector-database|FAISS]]) and with [[gpt-plugins|GPT-4 plug-ins]] defined via a manifest and an OpenAPI specification. The book's angle versus contemporaries is its compactness and its insistence on engineering concerns -- cost, latency, security, [[ai-hallucination|hallucination mitigation]], and [[function-calling|function calling]] as the bridge to existing software -- rather than ML internals.

## Key Contributions

- End-to-end developer playbook for the OpenAI Python SDK: chat completions, completions, embeddings, moderation, Whisper, DALL-E, with token-budget and pricing reasoning baked into every code path.
- Four worked example apps (news generator, YouTube summarizer, Zelda BOTW expert with Redis-backed retrieval, voice assistant with Whisper + Gradio) that map prompt-engineering choices onto concrete software architectures.
- A practical taxonomy of prompt design (context / task / role / step-by-step / few-shot / formatting / negative prompts) paired with a synthetic-data fine-tuning workflow on a real email-marketing use case.
- A LangChain walkthrough that wires embeddings, FAISS, RetrievalQA, ConversationChain memory, and agents/tools into a single retrieval-augmented chatbot pattern.
- Treatment of LLM-app security: API key management strategies, the inevitability of prompt injection, input/output analysis, and OpenAI's moderation endpoint.

## Key Topics Covered

openai-api, chatgpt, gpt-4, tokenization, prompt-engineering, few-shot-learning, chain-of-thought-prompting, fine-tuning, function-calling, embeddings, retrieval-augmented-generation, vector-database, langchain, gpt-plugins, rlhf, prompt-injection, ai-hallucination

## Questions Raised

- How will the OpenAI API surface (function calling, plug-ins, fine-tuning availability for GPT-3.5/GPT-4) evolve past late 2023 and which patterns in the book will be deprecated?
- When context windows become large enough to hold whole document corpora, how should retrieval-augmented generation be redesigned -- or skipped -- in production apps?
- Given that the authors call prompt injection effectively inevitable, what concrete layered defenses (sandboxing, output filters, capability scoping) belong in a GPT-app reference architecture?
- How should fine-tuning costs and synthetic-data quality be evaluated against retrieval-augmented and few-shot approaches for a given domain task?
- What is the right operational pattern (caching, batching, model routing between GPT-3.5 and GPT-4) for managing latency and per-token cost in user-facing LLM apps?

## Intended Audience

Python developers and software engineers (with light data-science background) who want to build production apps on top of the OpenAI API -- chatbots, content generators, retrieval QA, voice assistants -- without needing deep ML internals.

## Key Concepts in This Source

- [[concepts/openai-api|OpenAI API]]
- [[concepts/chatgpt|ChatGPT]]
- [[concepts/gpt-4|GPT-4]]
- [[concepts/large-language-models|Large Language Models]]
- [[concepts/tokenization|Tokenization]]
- [[concepts/prompt-engineering|Prompt Engineering]]
- [[concepts/few-shot-learning|Few-Shot Learning]]
- [[concepts/chain-of-thought-prompting|Chain-of-Thought Prompting]]
- [[concepts/fine-tuning|Fine-Tuning]]
- [[concepts/function-calling|Function Calling]]
- [[concepts/embeddings|Embeddings]]
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[concepts/vector-database|Vector Database]]
- [[concepts/langchain|LangChain]]
- [[concepts/gpt-plugins|GPT Plug-ins]]
- [[concepts/rlhf|Reinforcement Learning from Human Feedback]]
- [[concepts/prompt-injection|Prompt Injection]]
- [[concepts/ai-hallucination|AI Hallucination]]

## Entities

- [[entities/olivier-caelen|Olivier Caelen]]
- [[entities/marie-alice-blete|Marie-Alice Blete]]
- [[entities/openai|OpenAI]]
- [[entities/langchain|LangChain]]
- [[entities/faiss|FAISS]]
- [[entities/worldline|Worldline]]
- [[entities/tom-taulli|Tom Taulli]]
