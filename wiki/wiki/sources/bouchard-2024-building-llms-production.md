---
title: Building LLMs for Production
page_id: sources/bouchard-2024-building-llms-production
page_type: source
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_technical_books_2026_06_19
tags:
- llm
- production-ai
- rag
- fine-tuning
- prompt-engineering
- langchain
- llamaindex
sources:
- sources/bouchard-2024-building-llms-production
related: []
mind_map_priority: high
authors:
- Louis-François Bouchard
year: 2024
source_type: book
schema_version: 2
uuid: 9c222600-1da3-52f5-9e5c-7307f36b6a94
content_hash: sha256:a89879bc38b3085e14feb2388c4315549a1b7650dc434414617b51aecbfc0077
---

<!-- AUTHORED REGION START -->
# Building LLMs for Production

**Authors:** Louis-François Bouchard  
**Year:** 2024  
**Type:** book  
**Markdown source:** `markdown_output/bouchard-2024-building-llms-production.md`

## Summary

Building LLMs for Production (2024) by Louis-François Bouchard, Louie Peters, and the Towards AI team is a hands-on, code-accompanied textbook covering the full stack of deploying large language models in real-world applications. It progresses from transformer architecture fundamentals and key LLM terminology through prompt engineering, the LangChain and LlamaIndex frameworks, retrieval-augmented generation (RAG), autonomous agents, fine-tuning (SFT, LoRA, RLHF), and production deployment including quantization and pruning. Each chapter pairs theory with runnable Google Colab notebooks and end-to-end project tutorials (chatbots, summarizers, financial document analysis, etc.), targeting readers with basic Python skills but no prior AI/NLP background.

## Key Claims

- LLMs can be understood and used effectively without building models from scratch — Scaling Laws, Context Windows, and Emergent Abilities explain their power
- Prompt engineering is a first-class discipline with well-defined bad practices and effective techniques that must be learned before moving to fine-tuning or RAG
- LangChain and LlamaIndex are the primary industry frameworks for building RAG-enabled LLM applications, each with distinct strengths
- RAG is positioned as a practical alternative to fine-tuning for injecting external knowledge, with advanced techniques (production-ready pipelines, metrics, evaluation) covered explicitly
- Fine-tuning approaches — Supervised Fine-Tuning (SFT), Low-Rank Adaptation (LoRA), and Reinforcement Learning from Human Feedback (RLHF) — are covered with domain-specific examples (finance, medical)
- Deployment requires addressing quantization and pruning to make models viable on real infrastructure including cloud CPUs
- The book explicitly bridges the gap between academic curricula and industry demands, a gap the authors identified through direct startup and PhD experience

## Main Concepts

- [[concepts/retrieval-augmented-generation-(rag)|Retrieval-Augmented Generation (RAG)]]
- [[concepts/transformer-architecture-and-gpt-family|Transformer architecture and GPT family]]
- [[concepts/prompt-engineering-and-langchain-prompt-templates|Prompt engineering and LangChain prompt templates]]
- [[concepts/fine-tuning:-sft,-lora,-rlhf|Fine-tuning: SFT, LoRA, RLHF]]
- [[concepts/llm-agents-and-autonomous-reasoning-engines|LLM agents and autonomous reasoning engines]]
- [[concepts/model-deployment:-quantization-and-pruning|Model deployment: quantization and pruning]]
- [[concepts/large-multimodal-models|Large Multimodal Models]]

## Key Entities

- [[entities/louis-fran-ois-bouchard-cto-co-founder-towards-ai-|Louis-François Bouchard (CTO/Co-Founder, Towards AI)]]
- [[entities/louie-peters-ceo-co-founder-towards-ai-|Louie Peters (CEO/Co-Founder, Towards AI)]]
- [[entities/towards-ai-publisher-and-platform-|Towards AI (publisher and platform)]]
- [[entities/langchain|LangChain]]
- [[entities/llamaindex|LlamaIndex]]
- [[entities/openai-gpt-chatgpt-assistants-autogpt-|OpenAI (GPT, ChatGPT, Assistants, AutoGPT)]]
- [[entities/weights-biases-langsmith-mentioned-alongside-|Weights & Biases (LangSmith mentioned alongside)]]
- [[entities/cohere|Cohere]]
- [[entities/jerry-liu-co-founder-llamaindex-|Jerry Liu (Co-founder, LlamaIndex)]]
- [[entities/mila-quebec-ai-institute-|Mila (Quebec AI Institute)]]

## Questions Raised

- How do the tradeoffs between prompting, RAG, and fine-tuning shift as model capabilities and context windows grow beyond 2024 baselines?
- What are the long-term maintenance costs of production RAG pipelines versus fine-tuned models when underlying data distributions drift?
- To what extent do framework abstractions like LangChain and LlamaIndex obscure failure modes that practitioners need to understand at the model level?

<!-- AUTHORED REGION END -->
