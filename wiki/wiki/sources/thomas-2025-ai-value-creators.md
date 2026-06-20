---
title: AI Value Creators
page_id: sources/thomas-2025-ai-value-creators
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Rob Thomas
- Paul Zikopoulos
- Kate Soule
year: 2025
publisher: O'Reilly Media
edition: 1st
is_early_release: false
page_count_estimate: 300
tags:
- ai-engineering
- ai-strategy
related:
- concepts/agentic-ai
- concepts/ai-governance
- concepts/ai-hallucination
- concepts/ai-value-creator
- concepts/data-fabric
- concepts/foundation-model
- concepts/generative-ai
- concepts/generative-computing
- concepts/parameter-efficient-fine-tuning
- concepts/prompt-injection
- concepts/quantum-safe-cryptography
- concepts/retrieval-augmented-generation
- entities/anthropic
- entities/deepseek
- entities/hugging-face
- entities/ibm
- entities/instructlab
- entities/kate-soule
- entities/langchain
- entities/openai
- entities/paul-zikopoulos
- entities/rob-thomas
mind_map_priority: medium
revision_hash: sha256:1a77353f5ece31ae
schema_version: 2
uuid: 805ffa70-705f-515e-82fc-c1b0e7098814
content_hash: sha256:b1d8c8806ffa3aa8fa99c933db01d2d2ba2cbbdcfe0aac2761b74abdfcb78184
---

<!-- AUTHORED REGION START -->
# AI Value Creators
*Beyond the Generative AI User Mindset*

**Authors:** [[entities/rob-thomas|Rob Thomas]], [[entities/paul-zikopoulos|Paul Zikopoulos]], [[entities/kate-soule|Kate Soule]]

**Year:** 2025

**Publisher:** O'Reilly Media

**Edition:** 1st

## Summary

AI Value Creators is an IBM-authored business handbook arguing that enterprises must move beyond passively consuming generative AI services and instead become [[ai-value-creator|AI Value Creators]] — organisations that combine their proprietary data, governance, and a platform of [[foundation-model|foundation models]] to build differentiated AI solutions they own. Thomas, Zikopoulos, and Soule treat the rise of [[generative-ai|generative AI]] as a 'Netscape moment' for business: a once-a-decade inflection in which competitive advantage will be decided not by who has access to the biggest model but by who pairs their data with the right mix of open and proprietary models, [[agentic-ai|agentic AI]], and disciplined governance.

The book lays out a pragmatic playbook: identify horizontal then vertical use cases, treat data as a differentiator via a [[data-fabric|data fabric]], steer base models with techniques like [[parameter-efficient-fine-tuning|PEFT]], [[retrieval-augmented-generation|RAG]], and InstructLab rather than retraining from scratch, and bake [[ai-governance|AI governance]] levers — fairness, robustness, explainability, lineage — in from day one. It is explicit that 'one model will not rule them all' and that smaller, fit-for-purpose open models will dominate enterprise stacks. Chapter 5 covers the dark side: [[ai-hallucination|hallucinations]], copyright lawsuits, deepfakes, [[prompt-injection|prompt injection]] attacks, data poisoning, and the 'steal now, crack later' case for [[quantum-safe-cryptography|quantum-safe cryptography]]. The closing chapter sketches [[generative-computing|generative computing]] as a future paradigm in which neurons join bits and qubits as first-class compute elements managed by structured runtimes rather than mega-prompts.

The angle versus competitors is corporate-strategic rather than technical: there is little code and no model implementation detail. Instead it offers a mental model and decision framework for executives, line-of-business leaders, and architects who must decide what to build, what to buy, what data to expose, and how to govern AI — drawing heavily on IBM's experience with watsonx, Granite, InstructLab, and customer engagements such as L'Oréal.

## Key Contributions

- Three-tier consumption taxonomy — AI baked into software, AI by API call, and the platform-based AI Value Creator pattern — as the central organising frame for enterprise AI strategy
- The 'your AI needs an IA' thesis: a data fabric and data-as-a-product discipline are prerequisites for differentiated GenAI, since the average LLM contains roughly 1% of any given enterprise's data
- A governance lever set — fairness, robustness, explainability, lineage — proposed as forethoughts rather than afterthoughts and as a future competitive moat once raw accuracy commoditises
- A multi-model, multi-modal future thesis: fit-for-purpose smaller open models plus judge models, safety models, and reasoning models, rather than a single monolithic frontier LLM
- The 'generative computing' proposal: structured prompts, runtimes, memory slots, and KV-cache reuse as a software-engineering discipline that replaces today's brittle mega-prompts

## Key Topics Covered

generative AI strategy, AI value creation, foundation models, agentic AI, AI governance, data strategy and data fabric, model selection (open vs proprietary), fine-tuning and InstructLab, retrieval-augmented generation, AI safety and prompt injection, AI regulation and copyright, quantum-safe cryptography, generative computing

## Questions Raised

- How should indemnification, copyright, and 'digital essence' rights be allocated when foundation models are trained on copyrighted or scraped data?
- What is the right governance and audit regime for agentic systems whose tool use and control flow are emergent rather than specified?
- How quickly will 'generative computing' runtimes mature into something practitioners can adopt, and which framework (LangChain successors, IBM stacks, others) will define that layer?
- Where exactly is the line between democratising AI through open source and ceding control of critical infrastructure to actors with different values?
- How should enterprises measure the ROI of AI value creation versus the simpler ROI of consuming embedded or hosted AI?

## Intended Audience

Enterprise executives, line-of-business leaders, data and AI strategy owners, and enterprise architects deciding how to adopt generative AI and agents — not ML engineers seeking implementation detail.

## Key Concepts in This Source

- [[concepts/ai-value-creator|AI Value Creator]]
- [[concepts/foundation-model|Foundation Model]]
- [[concepts/generative-ai|Generative AI]]
- [[concepts/agentic-ai|Agentic AI]]
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[concepts/parameter-efficient-fine-tuning|Parameter-Efficient Fine-Tuning]]
- [[concepts/ai-hallucination|AI Hallucination]]
- [[concepts/ai-governance|AI Governance]]
- [[concepts/data-fabric|Data Fabric]]
- [[concepts/prompt-injection|Prompt Injection]]
- [[concepts/generative-computing|Generative Computing]]
- [[concepts/quantum-safe-cryptography|Quantum-Safe Cryptography]]

## Entities

- [[entities/rob-thomas|Rob Thomas]]
- [[entities/paul-zikopoulos|Paul Zikopoulos]]
- [[entities/kate-soule|Kate Soule]]
- [[entities/ibm|IBM]]
- [[entities/instructlab|InstructLab]]
- [[entities/hugging-face|Hugging Face]]
- [[entities/deepseek|DeepSeek]]
- [[entities/langchain|LangChain]]
- [[entities/openai|OpenAI]]
- [[entities/anthropic|Anthropic]]

<!-- AUTHORED REGION END -->
