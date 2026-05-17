---
title: AI Engineering
page_id: sources/huyen-2025-ai-engineering
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Chip Huyen
year: 2025
publisher: O'Reilly Media
edition: 1st
is_early_release: false
page_count_estimate: 530
tags:
- ai-engineering
related:
- concepts/ai-agents
- concepts/ai-engineering
- concepts/dataset-engineering
- concepts/foundation-models
- concepts/in-context-learning
- concepts/inference-optimization
- concepts/llm-as-a-judge
- concepts/parameter-efficient-finetuning
- concepts/prompt-engineering
- concepts/retrieval-augmented-generation
- concepts/rlhf
- concepts/sampling-strategies
- entities/anthropic
- entities/chip-huyen
- entities/google
- entities/hugging-face
- entities/langchain
- entities/llamaindex
- entities/luke-metz
- entities/openai
- entities/oreilly-media
- entities/patrick-lewis
mind_map_priority: medium
revision_hash: sha256:aa134a902686eeab
---

# AI Engineering
*Building Applications with Foundation Models*

**Authors:** [[entities/chip-huyen|Chip Huyen]]

**Year:** 2025

**Publisher:** O'Reilly Media

**Edition:** 1st

## Summary

Chip Huyen's AI Engineering is a practitioner's framework for building production applications on top of foundation models. Written as a companion to her earlier Designing Machine Learning Systems, it focuses on the model adaptation stack that emerged when [[foundation-models|foundation models]] made it cheap to start an AI product but expensive to make it work reliably. Huyen argues that while [[ai-engineering|AI engineering]] inherits the discipline of traditional ML engineering — systematic experimentation, rigorous evaluation, relentless optimisation — the substitution of pre-trained foundation models for trained-from-scratch models shifts the centre of gravity from feature engineering and labelling toward prompt design, context construction, retrieval, and post-training.

The book is organised as a top-to-bottom traversal of that stack: understanding foundation models (architecture, post-training, sampling), evaluating them ([[llm-as-a-judge|LLM-as-a-judge]], reference-based metrics, comparative ranking), then the adaptation toolkit — [[prompt-engineering|prompt engineering]] and [[in-context-learning|in-context learning]], [[retrieval-augmented-generation|RAG]] and [[ai-agents|agents]], [[parameter-efficient-finetuning|parameter-efficient finetuning]] and [[rlhf|RLHF]] — followed by [[dataset-engineering|dataset engineering]], [[inference-optimization|inference optimisation]], and end-to-end architecture with guardrails, routing, caching, and user-feedback loops. The treatment is opinionated about ordering: try prompting before RAG, RAG before finetuning, evaluation before scaling, and feedback design before chasing benchmark scores.

Its angle relative to competitors is that it deliberately avoids tying itself to specific tools or APIs (LangChain, particular vector DBs, particular model providers) in favour of the underlying invariants — [[sampling-strategies|sampling]], retrieval algorithms, memory hierarchies, latency trade-offs — that survive vendor churn. Drawn from interviews with researchers at OpenAI, Anthropic, Google, NVIDIA, Meta, Hugging Face, LangChain, and LlamaIndex plus case studies from companies in production, the book targets ML/software engineers building AI products and the product managers and architects who collaborate with them.

## Key Contributions

- A clear demarcation between AI engineering and traditional ML engineering: pre-trained models flip the workflow from train-then-deploy to adapt-then-deploy, making prompt/context/evaluation the new core competencies
- An adaptation hierarchy — prompting → RAG → finetuning → custom pretraining — with explicit decision criteria for when to escalate and when each is the wrong tool
- A unified treatment of evaluation that fuses classical metrics (perplexity, exact match, similarity) with LLM-as-a-judge and comparative ranking, plus a four-step methodology for designing evaluation pipelines per component of a system
- A precise vocabulary for inference performance — TTFT, TPOT, throughput, goodput, MFU, MBU — that separates user-visible latency from system-level utilisation and exposes the latency/throughput trade-off
- A memory taxonomy for agents (internal knowledge, short-term context, long-term external memory) tied to RAG architectures and a catalogue of agent failure modes (invalid tool, invalid parameters, goal failure, reflection error)
- Elevation of dataset engineering — curation, synthesis, distillation, deduplication, AI-powered data generation — to a first-class engineering discipline rather than data prep

## Key Topics Covered

foundation-models, ai-engineering, prompt-engineering, in-context-learning, retrieval-augmented-generation, ai-agents, parameter-efficient-finetuning, rlhf, llm-as-a-judge, inference-optimization, dataset-engineering, sampling-strategies, evaluation-methodology, vector-databases, embeddings, quantization, model-distillation, guardrails, model-routing, user-feedback-loops

## Questions Raised

- How will preference finetuning evolve as the field debates why RLHF and DPO actually work?
- Can test-time compute be scaled indefinitely, or do adversarial outputs eventually defeat verifiers as sample counts grow?
- When closed-model providers restrict logprobs and other model internals, how do practitioners retain the ability to evaluate, debug, and route between models?
- How should AI engineering teams structure cross-functional collaboration with product, data, and infra as model adaptation replaces model training?
- What evaluation methodology will survive when benchmarks saturate faster than they can be designed?

## Intended Audience

AI/ML engineers and software engineers building production applications on top of foundation models, plus product managers, architects, and tech leads collaborating with them; readers transitioning from traditional ML engineering or full-stack engineering into the foundation-model era.

## Key Concepts in This Source

- [[concepts/foundation-models|Foundation Models]]
- [[concepts/ai-engineering|AI Engineering]]
- [[concepts/prompt-engineering|Prompt Engineering]]
- [[concepts/in-context-learning|In-Context Learning]]
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[concepts/ai-agents|AI Agents]]
- [[concepts/parameter-efficient-finetuning|Parameter-Efficient Finetuning]]
- [[concepts/rlhf|Reinforcement Learning from Human Feedback]]
- [[concepts/llm-as-a-judge|LLM-as-a-Judge]]
- [[concepts/inference-optimization|Inference Optimization]]
- [[concepts/dataset-engineering|Dataset Engineering]]
- [[concepts/sampling-strategies|Sampling Strategies]]

## Entities

- [[entities/chip-huyen|Chip Huyen]]
- [[entities/oreilly-media|O'Reilly Media]]
- [[entities/openai|OpenAI]]
- [[entities/anthropic|Anthropic]]
- [[entities/google|Google]]
- [[entities/hugging-face|Hugging Face]]
- [[entities/langchain|LangChain]]
- [[entities/llamaindex|LlamaIndex]]
- [[entities/patrick-lewis|Patrick Lewis]]
- [[entities/luke-metz|Luke Metz]]
