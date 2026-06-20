---
title: Hands-On Large Language Models
page_id: sources/alammar-2024-hands-on-llm
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Jay Alammar
- Maarten Grootendorst
year: 2024
publisher: O'Reilly Media
edition: 1st
is_early_release: false
page_count_estimate: 408
tags:
- ai-engineering
- llm
related:
- concepts/chain-of-thought-prompting
- concepts/contrastive-learning
- concepts/dense-retrieval
- concepts/in-context-learning
- concepts/multimodal-embeddings
- concepts/parameter-efficient-fine-tuning
- concepts/prompt-engineering
- concepts/reinforcement-learning-from-human-feedback
- concepts/reranking
- concepts/retrieval-augmented-generation
- concepts/self-attention
- concepts/token-embeddings
- concepts/tokenization
- concepts/transformers
- entities/ashish-vaswani
- entities/bertopic
- entities/cohere
- entities/hugging-face
- entities/jay-alammar
- entities/langchain
- entities/maarten-grootendorst
- entities/nils-reimers
mind_map_priority: medium
revision_hash: sha256:582343ec71d7c232
schema_version: 2
uuid: 8c362acb-aa40-58e8-bc08-af2ce6d1bb28
content_hash: sha256:dbfdca51a1aefbc25b88afb24c53a77883836841c16dfee70a36688cd3e3ddc0
---

<!-- AUTHORED REGION START -->
# Hands-On Large Language Models
*Language Understanding and Generation*

**Authors:** [[entities/jay-alammar|Jay Alammar]], [[entities/maarten-grootendorst|Maarten Grootendorst]]

**Year:** 2024

**Publisher:** O'Reilly Media

**Edition:** 1st

## Summary

Hands-On Large Language Models by Jay Alammar and Maarten Grootendorst is an intuition-first, visually driven practitioner's guide to building with LLMs. The authors argue that the LLM landscape splits cleanly into representation models (encoder-style, used for classification, clustering, and search) and generative models (decoder-style, used for chat, summarisation, and reasoning), and they organise the book so that readers can mix the two families fluently. The book moves from foundational mechanics ([[tokenization|tokenization]], [[token-embeddings|token embeddings]], [[self-attention|self-attention]] inside [[transformers|transformer]] blocks) into applied pipelines (text classification, BERTopic clustering, [[prompt-engineering|prompt engineering]]), then into retrieval and grounding ([[dense-retrieval|dense retrieval]], [[reranking|reranking]], [[retrieval-augmented-generation|RAG]]), and finally into training ([[contrastive-learning|contrastive learning]] for embedding models, [[parameter-efficient-fine-tuning|PEFT]] with LoRA/QLoRA, and [[reinforcement-learning-from-human-feedback|preference tuning]] via reward models and DPO).

Its angle versus competitors is the illustrated, code-along treatment: dense diagrams of every architectural component paired with runnable Hugging Face / Cohere / LangChain notebooks, all hosted on Google Colab so readers need no local GPU. Where Sebastian Raschka's 'Build a Large Language Model from Scratch' implements GPT-2 line by line, Alammar and Grootendorst stay at the API and library level, optimising for breadth of applied recipes (search, RAG, classification, topic modelling, [[multimodal-embeddings|multimodal embeddings]], fine-tuning) rather than from-scratch implementation. The intended reader is a Python-fluent practitioner who wants to ship LLM-powered features and understand the system well enough to choose the right tool for each task.

The book also serves as a curated tour of the modern open-source LLM stack — sentence-transformers, BERTopic, LangChain, PEFT, TRL, BLIP-2, CLIP — and as a conceptual map linking each tool to the underlying idea ([[in-context-learning|in-context learning]], [[chain-of-thought-prompting|chain-of-thought]], contrastive objectives) it operationalises.

## Key Contributions

- Establishes representation-versus-generation as the primary mental model for navigating the LLM ecosystem, with explicit task-to-model-family mappings throughout.
- Provides a complete RAG construction pipeline (chunking → embeddings → vector store → dense retrieval → reranking → grounded generation → evaluation) with working Cohere and local-model implementations.
- Demystifies transformer internals with diagrams of the forward pass, KV caching, RoPE positional embeddings, and grouped-query attention at a level matching practitioner intuition rather than mathematical derivation.
- Walks through the modern three-stage training stack — pretraining, supervised fine-tuning, and preference tuning (RLHF/DPO) — with runnable QLoRA recipes that fit on consumer GPUs.
- Treats embedding models as first-class artefacts, showing contrastive training (SBERT), augmented SBERT, and TSDAE for domain adaptation as a unified toolkit for search and classification.

## Key Topics Covered

transformer architecture, tokenization, token and sentence embeddings, text classification, text clustering and topic modeling, prompt engineering, chain-of-thought and tree-of-thought reasoning, LangChain chains, memory, and agents, semantic search and dense retrieval, reranking, retrieval-augmented generation, multimodal models (CLIP, BLIP-2), contrastive learning for embedding models, LoRA / QLoRA fine-tuning, RLHF and DPO preference tuning

## Questions Raised

- How should practitioners decide between fine-tuning an embedding model and using a stronger off-the-shelf one as base models improve quarterly?
- What evaluation methodology generalises across RAG systems when retrieval quality, grounding faithfulness, and generation fluency interact non-linearly?
- When does parameter-efficient fine-tuning stop being competitive with prompting-plus-retrieval as context windows and instruction-following improve?
- How should multimodal embedding models be evaluated beyond CLIP-style image-text retrieval as use cases diversify into video, audio, and structured data?

## Intended Audience

Python-fluent ML practitioners and data scientists who want a visual, code-along introduction to building applied LLM systems (search, RAG, classification, fine-tuning) without deriving the math from scratch.

## Key Concepts in This Source

- [[concepts/transformers|Transformers]]
- [[concepts/self-attention|Self-Attention]]
- [[concepts/token-embeddings|Token Embeddings]]
- [[concepts/tokenization|Tokenization]]
- [[concepts/dense-retrieval|Dense Retrieval]]
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[concepts/reranking|Reranking]]
- [[concepts/prompt-engineering|Prompt Engineering]]
- [[concepts/in-context-learning|In-Context Learning]]
- [[concepts/chain-of-thought-prompting|Chain-of-Thought Prompting]]
- [[concepts/contrastive-learning|Contrastive Learning]]
- [[concepts/parameter-efficient-fine-tuning|Parameter-Efficient Fine-Tuning]]
- [[concepts/reinforcement-learning-from-human-feedback|Reinforcement Learning from Human Feedback]]
- [[concepts/multimodal-embeddings|Multimodal Embeddings]]

## Entities

- [[entities/jay-alammar|Jay Alammar]]
- [[entities/maarten-grootendorst|Maarten Grootendorst]]
- [[entities/cohere|Cohere]]
- [[entities/hugging-face|Hugging Face]]
- [[entities/langchain|LangChain]]
- [[entities/nils-reimers|Nils Reimers]]
- [[entities/ashish-vaswani|Ashish Vaswani]]
- [[entities/bertopic|BERTopic]]

<!-- AUTHORED REGION END -->
