---
title: Learning LangChain
page_id: sources/oshin-2025-learning-langchain
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Mayo Oshin
- Nuno Campos
year: 2025
publisher: O'Reilly Media
edition: 1st
is_early_release: false
page_count_estimate: 380
tags:
- ai-engineering
- langchain
related:
- concepts/chain-of-thought-prompting
- concepts/embeddings
- concepts/human-in-the-loop
- concepts/langchain
- concepts/langgraph
- concepts/langsmith
- concepts/llm-agent
- concepts/llm-as-a-judge
- concepts/llm-memory
- concepts/react-agent
- concepts/retrieval-augmented-generation
- concepts/structured-output
- concepts/tool-calling
- concepts/vector-store
- entities/harrison-chase
- entities/langchain
- entities/langgraph-framework
- entities/langsmith-platform
- entities/mayo-oshin
- entities/nuno-campos
- entities/openai
- entities/oreilly-media
- entities/shunyu-yao
mind_map_priority: medium
revision_hash: sha256:9a5841c55ec1fe33
schema_version: 2
uuid: e20d7c96-f1a1-518a-a37a-2f9be91a58b5
content_hash: sha256:c4fcde66c419859626ed0b86eb8344449353bf029e7e3e65059a19820ffaa191
---

<!-- AUTHORED REGION START -->
# Learning LangChain
*Building AI and LLM Applications with LangChain and LangGraph*

**Authors:** [[entities/mayo-oshin|Mayo Oshin]], [[entities/nuno-campos|Nuno Campos]]

**Year:** 2025

**Publisher:** O'Reilly Media

**Edition:** 1st

## Summary

Learning LangChain by Mayo Oshin and Nuno Campos is the first comprehensive O'Reilly treatment of the [[langchain|LangChain]] ecosystem, written with first-party authority by Campos, a core LangChain maintainer. The book argues that the central craft of LLM engineering is composing prompting techniques together: prompt templates, [[retrieval-augmented-generation|retrieval-augmented generation]], [[chain-of-thought-prompting|chain-of-thought reasoning]], [[tool-calling|tool calling]], and [[llm-memory|memory]] all become more powerful when chained, and LangChain exists to make that composition reliable.

It walks the reader through a single arc: a plain chat call, then a [[retrieval-augmented-generation|RAG]] pipeline built from document loaders, text splitters, [[embeddings|embeddings]], and a [[vector-store|vector store]]; then conversational memory using [[langgraph|LangGraph]]; then cognitive architectures (router, parallelisation, orchestrator/worker); then [[llm-agent|agent architectures]] built on the [[react-agent|ReAct]] pattern; and finally multi-agent systems with supervisor and swarm topologies. The closing chapters cover production deployment on LangGraph Platform, tracing and evaluation with [[langsmith|LangSmith]] (including [[llm-as-a-judge|LLM-as-a-judge]] evaluators), and three product patterns for shipping LLMs to end users: interactive chatbots, collaborative editing, and autonomous agents with [[human-in-the-loop|human-in-the-loop]] control.

The angle versus competitors (e.g. generic 'build an LLM app' books) is that the authors treat LangChain and LangGraph as the default abstractions and use the [[structured-output|structured output]], checkpointing, and observability primitives of the framework as load-bearing parts of the design — making it an opinionated, hands-on engineering manual rather than a survey.

## Key Contributions

- Unifying treatment of LangChain and LangGraph as a single development arc from one-shot LLM call through RAG, memory, agents, deployment, and evaluation
- Explicit framing of the 'agency vs. reliability' frontier as the central design decision for LLM applications, with concrete LangGraph patterns at each point on the curve
- First-party tour of LangGraph primitives (StateGraph, ToolNode, checkpointers, subgraphs, interrupt) by a core maintainer
- End-to-end production playbook: LangGraph Platform deployment, LangSmith tracing, offline and online evaluation with heuristic / human / LLM-as-a-judge evaluators
- Catalogue of cognitive architectures (router, parallelisation, orchestrator-worker, reflection) and multi-agent topologies (supervisor, swarm) as named, reusable patterns

## Key Topics Covered

langchain, langgraph, langsmith, retrieval-augmented-generation, embeddings, vector-store, chain-of-thought-prompting, tool-calling, react-agent, llm-memory, structured-output, human-in-the-loop, llm-agent, llm-as-a-judge, prompt-engineering, deployment, evaluation

## Questions Raised

- How will the agency-vs-reliability frontier shift as base models improve, and which of these LangGraph patterns will become obsolete?
- When is a hand-rolled orchestration layer preferable to LangChain/LangGraph's abstractions, and what is the cost of framework lock-in?
- How should LLM-as-a-judge evaluators be themselves validated against human ground truth at scale?
- What are the right UX primitives for LLM-native applications beyond chat, collaborative editing, and autonomous agents?

## Intended Audience

Software engineers and ML practitioners who want to build production-grade LLM applications and agents using the LangChain/LangGraph stack, with code in both Python and JavaScript.

## Key Concepts in This Source

- [[concepts/langchain|LangChain]]
- [[concepts/langgraph|LangGraph]]
- [[concepts/langsmith|LangSmith]]
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[concepts/embeddings|Embeddings]]
- [[concepts/vector-store|Vector Store]]
- [[concepts/chain-of-thought-prompting|Chain-of-Thought Prompting]]
- [[concepts/tool-calling|Tool Calling]]
- [[concepts/react-agent|ReAct Agent]]
- [[concepts/llm-memory|LLM Memory]]
- [[concepts/structured-output|Structured Output]]
- [[concepts/human-in-the-loop|Human-in-the-Loop]]
- [[concepts/llm-agent|LLM Agent]]
- [[concepts/llm-as-a-judge|LLM-as-a-Judge]]

## Entities

- [[entities/mayo-oshin|Mayo Oshin]]
- [[entities/nuno-campos|Nuno Campos]]
- [[entities/langchain|LangChain]]
- [[entities/langgraph-framework|LangGraph]]
- [[entities/langsmith-platform|LangSmith]]
- [[entities/harrison-chase|Harrison Chase]]
- [[entities/shunyu-yao|Shunyu Yao]]
- [[entities/openai|OpenAI]]
- [[entities/oreilly-media|O'Reilly Media]]

<!-- AUTHORED REGION END -->
