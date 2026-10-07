---
authors:
- Abi Aryan
content_hash: sha256:5685207e2aab2014070cb41592017a98061741e58aa69a9d5b12846fee8c4912
created: '2026-10-07T18:46:39Z'
edition: Early Release
is_early_release: true
mind_map_priority: medium
page_count_estimate: null
page_id: sources/aryan-2025-llmops
page_type: source
publisher: O'Reilly Media
raw_location: wiki/raw/ai-engineering/
related:
- concepts/large-language-models
- concepts/transformers
- concepts/self-attention
- concepts/state-space-models
- concepts/foundation-models
- concepts/prompt-engineering
- concepts/retrieval-augmented-generation
- concepts/fine-tuning
- concepts/parameter-efficient-fine-tuning
- concepts/llm-evaluation
- concepts/ml-monitoring-and-observability
- concepts/distribution-drift
- concepts/ai-agents
- concepts/agentic-ai
- concepts/knowledge-graph
- concepts/inference-optimization
- concepts/llm-memory
- concepts/llm-hallucination
- concepts/llmops
- concepts/open-weight-models
- sources/huyen-2025-ai-engineering
- sources/huyen-2022-designing-ml-systems
- sources/gift-2021-practical-mlops
- sources/bouchard-2024-building-llms-production
- sources/wilson-2024-llm-security-playbook
- entities/abi-aryan
- entities/oreilly-media
- entities/openai
- entities/meta-ai
- entities/microsoft
- entities/hugging-face
revision_id: 1
schema_version: 2
source_path: markdown_output/aryan-2025-llmops.md
source_type: book
sources: []
tags:
- llmops
- mlops
- large-language-models
- production-ml
- llm-deployment
- reliability-engineering
- ml-team-structure
- o-reilly-book
title: LLMOps
updated: '2026-10-07T18:46:39Z'
updated_by: op_9a030901d060
uuid: 5673748b-4794-5dd2-b08c-73939dad953d
year: 2025
---

<!-- AUTHORED REGION START -->
# LLMOps
*Managing Large Language Models in Production*

**Authors:** [[entities/abi-aryan|Abi Aryan]]

**Year:** 2025

**Publisher:** O'Reilly Media

**Edition:** Early Release

**Early release.** Only part of the book was available. Chapters present: Chapter 1. Introduction to Large Language Models; Chapter 2. Introduction to LLMOps; Chapter 10. The Future of LLMs and LLMOps (headed 'Chapter 3. The Future of LLMs and LLMOps' in this early-release file; its note says it will be the 10th chapter of the final book).

**Note:** Early Release, Revision History first release 2025-01-29; planned First Edition July 2025; ISBN printed as 978-1-098-15414-1. The provisional table of contents lists 10 chapters; only chapters 1, 2 and 10 are available. Missing: Data Engineering for LLMs, API-First LLM Deployment, Model Domain Adaptation, LLM-Based Applications, Model Evaluation, Governance (Monitoring, Privacy and Security), Hardware Scaling. The copyright line and title page name only Abi Aryan. The download file name listed a second person as co-author; the book text does not name that person as an author, so they are not listed here (name withheld because an identical name appears in the file as what looks like a licence watermark). The EPUB metadata header holds placeholders and was ignored. Figure numbers in the last chapter are inconsistent (captions say 3-x, body text says 10-x).

## Summary

This is an early-release version of an O'Reilly book on running large language models in production. Only three of the planned ten chapters are present: an introduction to LLMs, an introduction to LLMOps, and a closing chapter on where LLMs and LLMOps are heading. The chapters on data, deployment, adaptation, evaluation, governance and hardware are not yet written.

Chapter 1 gives a plain primer. It covers transformers and self-attention, encoder-only, decoder-only and encoder-decoder designs, state space models such as Mamba, and small language models. It then discusses how to choose a model, the trade-offs between open-source, open-weight and proprietary models, common enterprise uses, and ten challenges of building with LLMs, from cost and latency to privacy and model drift.

Chapter 2 is the core. It defines LLMOps as an operational framework for LLM applications, argues it differs from MLOps (and is closer to DevOps), and sets four goals: safety, scalability, robustness and reliability. It describes team roles and how to hire or upskill an LLMOps engineer, shows how to turn the goals into SLOs, SLAs and KPIs, and proposes a three-level LLMOps maturity model adapted from Microsoft's MLOps maturity model. The final chapter is speculative. It covers modular and mixture-of-experts models, neurosymbolic hybrids, memory-augmented models, RAG with knowledge graphs, GPU trends, synthetic data, regulation and evaluation standards.

## Key Contributions

- Defines LLMOps as its own operational framework and contrasts it with MLOps step by step across the model lifecycle (data, training, domain adaptation, evaluation, robustness, security). The author argues LLMOps has more in common with DevOps than with MLOps, because LLM apps are interactive, consumer-facing software.
- Sets four goals for LLMOps (safety, scalability, robustness, reliability) and shows how to measure each with service level objectives, service level agreements and KPIs, with example targets such as monthly uptime.
- Proposes a three-level LLMOps maturity model (Level 0 no LLMOps, Level 1 MLOps without LLM-specific practice, Level 2 full LLMOps), adapted from Microsoft's MLOps maturity model, with checklists on documentation, logging, A/B testing, bias monitoring, compliance, anonymisation and security audits.
- Describes the LLMOps engineer role: a sample working day, the skills to look for, a four-round interview process, and how to upskill an MLOps engineer instead of hiring externally.
- Argues that LLM fine-tuning is far costlier than for classic models. The book states the hyperparameter space of a large generative model is about 1,500 times that of BERT; note it attributes 175 billion parameters to GPT-4, which is not an official figure.
- Frames GenAI project failure as mainly operational, citing a Gartner prediction that 30% of GenAI projects would be abandoned, and an earlier Gartner prediction that 85% of ML projects would fail.

## Key Topics Covered

Transformer, encoder, decoder and state space architectures, Small language models, Open-source vs open-weight vs proprietary LLMs, Enterprise LLM use cases and AI agents, Ten challenges of building with LLMs, MLOps vs LLMOps lifecycle comparison, Four LLMOps goals: safety, scalability, robustness, reliability, LLMOps team roles and hiring, SLO / SLA / KPI framework, LLMOps maturity model, Mixture-of-experts, neurosymbolic and memory-augmented models, Future of GPUs, data management, privacy and evaluation standards

## Questions Raised

- How should an LLMOps team turn fuzzy goals like robustness into SLOs when LLM evaluation itself is unsolved?
- Is the three-level maturity model fine-grained enough, given that most teams sit between Level 1 and Level 2?
- Does LLMOps really need a separate engineer role, or is it an extension of MLOps and site reliability engineering?
- How will persistent memory and personalisation be monitored when they can draw wrong conclusions about users?

## Intended Audience

Engineers, MLOps practitioners and engineering managers who need to deploy, run and staff LLM applications in production. The early chapters assume little LLM background.

## Key Concepts in This Source

- [[concepts/large-language-models|Large Language Models]]
- [[concepts/transformers|Transformers]]
- [[concepts/self-attention|Self-Attention]]
- [[concepts/state-space-models|State-Space Models]]
- [[concepts/foundation-models|Foundation Models]]
- [[concepts/prompt-engineering|Prompt Engineering]]
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[concepts/fine-tuning|Fine-Tuning]]
- [[concepts/parameter-efficient-fine-tuning|Parameter-Efficient Fine-Tuning]]
- [[concepts/llm-evaluation|LLM Evaluation]]
- [[concepts/ml-monitoring-and-observability|ML Monitoring and Observability]]
- [[concepts/distribution-drift|Distribution Drift]]
- [[concepts/ai-agents|AI Agents]]
- [[concepts/agentic-ai|Agentic AI]]
- [[concepts/knowledge-graph|Knowledge Graph]]
- [[concepts/inference-optimization|Inference Optimization]]
- [[concepts/llm-memory|LLM Memory]]
- [[concepts/llm-hallucination|LLM Hallucination]]
- [[concepts/llmops|LLMOps]]
- [[concepts/open-weight-models|Open-Weight Models]]

## Entities

- [[entities/abi-aryan|Abi Aryan]]
- [[entities/oreilly-media|O'Reilly Media]]
- [[entities/openai|OpenAI]]
- [[entities/meta-ai|Meta AI]]
- [[entities/microsoft|Microsoft]]
- [[entities/hugging-face|Hugging Face]]

## Related Sources

- [[sources/huyen-2025-ai-engineering|AI Engineering]]
- [[sources/huyen-2022-designing-ml-systems|Designing Machine Learning Systems]]
- [[sources/gift-2021-practical-mlops|Practical MLOps: Operationalizing Machine Learning Models]]
- [[sources/bouchard-2024-building-llms-production|Building LLMs for Production]]
- [[sources/wilson-2024-llm-security-playbook|The Developer's Playbook for Large Language Model Security]]
<!-- AUTHORED REGION END -->