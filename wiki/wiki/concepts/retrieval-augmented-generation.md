---
content_hash: sha256:6e738c0a9423ca35f31c4c1d1cc2ff9f2bb21487638c15207aa88fec4bf8d2a9
created: '2026-05-17T16:44:06Z'
mind_map_priority: high
page_id: concepts/retrieval-augmented-generation
page_type: concept
related:
- concepts/self-attention
- concepts/transformers
- concepts/llm-knowledge-bases
- sources/karpathy-2026-llm-knowledge-bases-tweets
revision_id: 3
schema_version: 2
sources:
- sources/alammar-2024-hands-on-llm
- sources/anon-2024-vector-databases-rag
- sources/berryman-2024-prompt-engineering-llms
- sources/bratanic-2025-essential-graphrag
- sources/caelen-2023-developing-apps-gpt4
- sources/huyen-2025-ai-engineering
- sources/mendelevitch-2025-hands-on-rag
- sources/oshin-2025-learning-langchain
- sources/taulli-2024-ai-assisted-programming
- sources/thomas-2025-ai-value-creators
- sources/aryan-2025-llmops
- sources/pathan-2025-mastering-llm-applications-langchain
- sources/karpathy-2026-llm-knowledge-bases-tweets
tags:
- ai-engineering
- self-attention
- transformers
title: Retrieval-Augmented Generation
updated: '2026-11-23T14:43:11Z'
updated_by: op_5c91b297008c
uuid: 036ffd72-a47c-5151-b394-2825ba398afd
---

<!-- AUTHORED REGION START -->
# Retrieval-Augmented Generation

## Definition

An architectural pattern that augments large language models with real-time retrieval from external document corpora, dynamically combining retrieved facts with generative capabilities to produce responses grounded in private or up-to-date data. Reduces hallucinations and enables enterprise-scale grounded question answering.

## Sources

- [[sources/pathan-2025-mastering-llm-applications-langchain|Mastering LLM Applications with LangChain and Hugging Face]]
- [[sources/aryan-2025-llmops|LLMOps]]
- [[sources/alammar-2024-hands-on-llm|Hands-On Large Language Models]]
- [[sources/anon-2024-vector-databases-rag|Utilizing Vector Databases to Enhance RAG Models]]
- [[sources/berryman-2024-prompt-engineering-llms|Prompt Engineering for LLMs]]
- [[sources/bratanic-2025-essential-graphrag|Essential GraphRAG]]
- [[sources/caelen-2023-developing-apps-gpt4|Developing Apps with GPT-4 and ChatGPT]]
- [[sources/huyen-2025-ai-engineering|AI Engineering]]
- [[sources/mendelevitch-2025-hands-on-rag|Hands-On RAG for Production]]
- [[sources/oshin-2025-learning-langchain|Learning LangChain]]
- [[sources/taulli-2024-ai-assisted-programming|AI-Assisted Programming]]
- [[sources/thomas-2025-ai-value-creators|AI Value Creators]]

## Related Concepts

- [[concepts/self-attention]]
- [[concepts/transformers]]

## When RAG Is Not Needed

Karpathy reports that for a personal LLM wiki of about ~100 articles the agent answered complex questions without a retrieval system, using index files and short summaries it maintained itself. He also prefers whole documents in the context window over RAG for reading. See [[sources/karpathy-2026-llm-knowledge-bases-tweets|Karpathy on Obsidian, Second Brains and LLM Knowledge Bases]].
<!-- AUTHORED REGION END -->
