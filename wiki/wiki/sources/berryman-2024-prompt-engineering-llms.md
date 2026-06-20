---
title: Prompt Engineering for LLMs
page_id: sources/berryman-2024-prompt-engineering-llms
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- John Berryman
- Albert Ziegler
year: 2025
publisher: O'Reilly Media
edition: 1st
is_early_release: false
page_count_estimate: 270
tags:
- ai-engineering
- llm
- prompt-engineering
related:
- concepts/chain-of-thought-prompting
- concepts/context-window
- concepts/few-shot-prompting
- concepts/llm-as-judge
- concepts/llm-evaluation
- concepts/llm-workflows
- concepts/prompt-assembly
- concepts/prompt-engineering
- concepts/react-reasoning-acting
- concepts/retrieval-augmented-generation
- concepts/rlhf
- concepts/tool-use
- entities/albert-ziegler
- entities/github-copilot
- entities/hamel-husain
- entities/john-berryman
- entities/openai
- entities/oreilly-media
mind_map_priority: medium
revision_hash: sha256:b199dea328348cb1
schema_version: 2
uuid: 04ec1a5a-bfb2-55eb-892e-d7c01fad20f6
content_hash: sha256:72b29fedbc6c9becf259e07da34d272cd7321619c72030641c3cb4e8c7dc650d
---

<!-- AUTHORED REGION START -->
# Prompt Engineering for LLMs
*The Art and Science of Building Large Language Model-Based Applications*

**Authors:** [[entities/john-berryman|John Berryman]], [[entities/albert-ziegler|Albert Ziegler]]

**Year:** 2025

**Publisher:** O'Reilly Media

**Edition:** 1st

## Summary

Prompt Engineering for LLMs is a practitioner's guide by two founding engineers of GitHub Copilot, John Berryman and Albert Ziegler, that treats [[prompt-engineering|prompt engineering]] as the core skill for building reliable LLM-based applications. The book's organising principle is that LLMs are, fundamentally, text-completion engines that mimic patterns from their training data; therefore the prompt engineer's job is to shape inputs so they resemble documents the model has 'seen before' and to steer the completion toward useful structure. Part I builds foundations (how LLMs and the [[transformers|transformer]] architecture work, tokenization, autoregressive sampling, the move from instruct models to chat via [[rlhf|RLHF]], and the anatomy of an LLM-application loop). Part II covers core techniques: sourcing static vs dynamic content, [[few-shot-prompting|few-shot prompting]], [[retrieval-augmented-generation|RAG]], summarization, [[prompt-assembly|prompt assembly]] with prioritised/scored snippets within the [[context-window|context window]], formatting (advice / analytic report / structured document modes), and 'taming' completions with preambles, recognizable boundaries, and logprob-based classification.

Part III turns to advanced application patterns: [[tool-use|tool use]] (decoded down to the ChatML wire format), [[chain-of-thought-prompting|chain-of-thought]] and [[react-reasoning-acting|ReAct]] reasoning, conversational agents, and multi-step [[llm-workflows|LLM workflows]] with stateful task agents and role delegation. A dedicated chapter on [[llm-evaluation|LLM evaluation]] argues for combining offline test suites (including [[llm-as-judge|LLM-as-judge]] graders and surgical code-completion benchmarks borrowed from Copilot) with online A/B testing and implicit telemetry like acceptance rate, while warning against naive thumbs-up/down signals. The closing chapter looks ahead to multimodal prompts and UI-level evolution.

The angle that distinguishes this book from other prompt-engineering titles is the Copilot-engineer perspective: prompts are treated as engineered documents inside a feedforward loop (retrieve, snippetize, score, pack, assemble), not as ad-hoc text. The book is aimed at application engineers building LLM features in real products, especially those becoming dedicated 'prompt engineers', and it consistently grounds advice in production patterns the authors used at GitHub Copilot.

## Key Contributions

- Frames prompt engineering as document engineering: shape the prompt so it reads like the kind of document the model saw during training ('the Little Red Riding Hood principle').
- Provides a concrete feedforward-pass pipeline (context retrieval -> snippetization -> scoring with priority tiers and floating-point scores -> prompt assembly within the token budget).
- Distinguishes static vs dynamic content and three prompt document shapes (advice conversation, analytic report, structured document) as templates for assembling completions.
- Reverse-engineers the OpenAI tool-calling wire format (ChatML with TypeScript-style function signatures) and explains why each token in a tool call narrows a classification subproblem.
- Articulates a dual offline/online evaluation strategy: surgical test-based proxies, LLM-as-judge rubrics, and implicit telemetry (acceptance rate, post-acceptance edits) rather than explicit ratings.
- Distinguishes conversational agents from LLM workflows and gives criteria for when to decompose a problem into a fixed multi-step pipeline versus letting an agent drive.

## Key Topics Covered

prompt-engineering, few-shot-prompting, chain-of-thought-prompting, retrieval-augmented-generation, tool-use, react-reasoning-acting, rlhf, prompt-assembly, context-window, llm-evaluation, llm-as-judge, llm-workflows, transformer-architecture, tokenization, logprobs

## Questions Raised

- How should prompt-assembly priority tiers and continuous scores be learned automatically rather than hand-tuned?
- What evaluation methodology generalises beyond code completion, where surgical delete-and-regenerate gives a near-perfect proxy metric?
- When is an open-ended conversational agent strictly preferable to a fixed LLM workflow, and how should one migrate between the two as a product matures?
- How portable are the OpenAI-specific tool-calling and ChatML patterns to other frontier models with different internal prompt formats?
- How do prompt-engineering practices need to change for multimodal models where 'document-like' training-data analogies are weaker?

## Intended Audience

Application engineers and dedicated prompt engineers building LLM-powered products who need a practitioner-grade mental model of prompts, context assembly, tools, agents, and evaluation, without requiring deep ML research background.

## Key Concepts in This Source

- [[concepts/prompt-engineering|Prompt Engineering]]
- [[concepts/few-shot-prompting|Few-shot Prompting]]
- [[concepts/chain-of-thought-prompting|Chain-of-Thought Prompting]]
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[concepts/react-reasoning-acting|ReAct]]
- [[concepts/tool-use|Tool Use]]
- [[concepts/rlhf|Reinforcement Learning from Human Feedback]]
- [[concepts/llm-evaluation|LLM Evaluation]]
- [[concepts/llm-as-judge|LLM-as-Judge]]
- [[concepts/prompt-assembly|Prompt Assembly]]
- [[concepts/context-window|Context Window]]
- [[concepts/llm-workflows|LLM Workflows]]

## Entities

- [[entities/john-berryman|John Berryman]]
- [[entities/albert-ziegler|Albert Ziegler]]
- [[entities/github-copilot|GitHub Copilot]]
- [[entities/openai|OpenAI]]
- [[entities/hamel-husain|Hamel Husain]]
- [[entities/oreilly-media|O'Reilly Media]]

<!-- AUTHORED REGION END -->
