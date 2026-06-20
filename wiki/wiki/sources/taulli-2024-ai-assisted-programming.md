---
title: AI-Assisted Programming
page_id: sources/taulli-2024-ai-assisted-programming
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Tom Taulli
year: 2024
publisher: O'Reilly Media
edition: 1st
is_early_release: false
page_count_estimate: 250
tags:
- ai-engineering
- ai-strategy
related:
- concepts/ai-assisted-programming
- concepts/autonomous-ai-agents
- concepts/chain-of-thought-prompting
- concepts/code-completion
- concepts/code-refactoring
- concepts/few-shot-learning
- concepts/hallucination
- concepts/large-language-model
- concepts/modular-programming
- concepts/prompt-engineering
- concepts/retrieval-augmented-generation
- concepts/test-driven-development
- entities/amazon-codewhisperer
- entities/anthropic-claude
- entities/chatgpt
- entities/code-llama
- entities/cursor
- entities/github-copilot
- entities/google-gemini
- entities/replit
- entities/tabnine
- entities/tom-taulli
mind_map_priority: medium
revision_hash: sha256:2196e152748a3b04
schema_version: 2
uuid: 942eab87-e924-5a10-84c8-da055626d6bb
content_hash: sha256:07d60c30a40bdfb2b81d4065cd81f884a6b45092352ace3ddb2002c3cfaae927
---

<!-- AUTHORED REGION START -->
# AI-Assisted Programming
*Better Planning, Coding, Testing, and Deployment*

**Authors:** [[entities/tom-taulli|Tom Taulli]]

**Year:** 2024

**Publisher:** O'Reilly Media

**Edition:** 1st

## Summary

Tom Taulli's _AI-Assisted Programming_ (O'Reilly, 2024) is a practitioner's tour of the AI coding tool landscape and a methodology for working with it. It argues that generative AI has moved beyond autocomplete into every phase of the software development lifecycle, and that developers who treat tools like [[github-copilot|GitHub Copilot]], [[cursor|Cursor]], [[chatgpt|ChatGPT]], [[google-gemini|Gemini]], and [[anthropic-claude|Claude]] as collaborators — rather than oracles — will become substantially more productive. The book is divided roughly into three movements: foundations (how [[large-language-model|LLMs]] and [[transformers|transformer-based]] code models work, plus [[prompt-engineering|prompt engineering]] best practices), tool surveys (Chapters 4–6 catalogue Copilot, [[amazon-codewhisperer|CodeWhisperer]], [[tabnine|Tabnine]], [[replit|Replit]], Cody, Warp, Bito, Cursor, [[code-llama|Code Llama]], StableCode, AlphaCode, and the general-purpose chat LLMs), and lifecycle application (Chapters 7–9 on planning, coding, debugging, testing, and deployment).

Taulli's organising methodology is [[modular-programming|modular programming]]: because LLM context windows are finite and [[hallucination|hallucinations]] compound with scope, the developer should decompose every task into small functions with clear inputs and outputs, prompt the model per piece, and verify each output before composing. He treats [[prompt-engineering|prompt engineering]] as the central craft, with chapters covering specificity, [[few-shot-learning|zero- and few-shot learning]], leading words, [[chain-of-thought-prompting|chain-of-thought prompting]], and techniques for mitigating hallucinations. Practical case studies — Shopify, Accenture, hardware programming — and short developer testimonials illustrate adoption patterns. The closing chapters argue that AI raises rather than lowers the floor for developer judgement: skills shift toward debugging AI output, understanding generated architectures, and steering [[autonomous-ai-agents|autonomous AI agents]].

The book is positioned as a survey-plus-handbook rather than a deep technical reference. It is friendly to beginners (defining tokens, temperature, and BLEU/ROUGE/HumanEval evaluation metrics in passing) but stays useful for working developers by walking through concrete prompts, IDE workflows, and the trade-offs of each major tool.

## Key Contributions

- A pragmatic methodology pairing modular programming with prompt engineering: decompose a task into small, verifiable units, prompt per unit, and compose only after each piece is checked.
- A 2024-snapshot comparative survey of more than 15 AI coding tools — Copilot, CodeWhisperer, Tabnine, Cursor, Replit, Cody, Warp, Bito, CodeGPT, CodeWP, Duet AI, and the open-source family (Code Llama, StableCode, AlphaCode, PolyCoder, CodeT5, StarCoder).
- A catalogue of prompt-engineering patterns specialised for code: leading words, few-shot demonstrations, chain-of-thought decompositions, format specifications, and acronym disambiguation.
- A practical taxonomy of LLM coding drawbacks — hallucinations, IP risk, privacy, security, training-data gaps, and bias — with mitigation guidance.
- End-to-end lifecycle coverage: brainstorming, market research, PRD/SRS writing, TDD templates (Given-When-Then, AAA, SEVT), refactoring patterns (extract method, decomposing conditionals, dead-code removal), code review, unit testing, and deployment.

## Key Topics Covered

generative AI for software development, prompt engineering for code, GitHub Copilot deep dive, comparative tool survey (CodeWhisperer, Cursor, Tabnine, Replit, Cody, Warp, Bito), general-purpose LLMs for coding (ChatGPT, Gemini, Claude), open-source code LLMs (Code Llama, StableCode, AlphaCode, CodeT5), LLM evaluation (HumanEval, BLEU, ROUGE, perplexity, BERTScore), hallucination mitigation, modular programming with AI, refactoring with AI, test-driven development with AI, debugging, code review, and deployment workflows, autonomous AI coding agents, career impact and the 10x developer question

## Questions Raised

- How does the modular-prompt methodology scale to systems with non-local invariants (distributed consistency, concurrency) where small-unit verification is insufficient?
- What is the right governance model for IP and licence-contamination risk when AI tools regurgitate training data?
- How should organisations measure productivity gains from AI coding tools beyond self-reported developer surveys?
- Will the tool landscape consolidate around a few platforms or remain fragmented as the book suggests?
- How do autonomous coding agents change accountability when they commit code without human review?

## Intended Audience

Working software developers (beginner to mid-senior) and engineering managers who want a single, current overview of the AI-assisted programming landscape and a method for incorporating these tools into day-to-day work.

## Key Concepts in This Source

- [[concepts/ai-assisted-programming|AI-Assisted Programming]]
- [[concepts/prompt-engineering|Prompt Engineering]]
- [[concepts/chain-of-thought-prompting|Chain-of-Thought Prompting]]
- [[concepts/few-shot-learning|Few-Shot Learning]]
- [[concepts/hallucination|Hallucination]]
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[concepts/large-language-model|Large Language Model]]
- [[concepts/code-completion|Code Completion]]
- [[concepts/modular-programming|Modular Programming]]
- [[concepts/code-refactoring|Code Refactoring]]
- [[concepts/test-driven-development|Test-Driven Development]]
- [[concepts/autonomous-ai-agents|Autonomous AI Agents]]

## Entities

- [[entities/tom-taulli|Tom Taulli]]
- [[entities/github-copilot|GitHub Copilot]]
- [[entities/cursor|Cursor]]
- [[entities/chatgpt|ChatGPT]]
- [[entities/amazon-codewhisperer|Amazon CodeWhisperer]]
- [[entities/tabnine|Tabnine]]
- [[entities/replit|Replit]]
- [[entities/google-gemini|Google Gemini]]
- [[entities/anthropic-claude|Anthropic Claude]]
- [[entities/code-llama|Code Llama]]

<!-- AUTHORED REGION END -->
