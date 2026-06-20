---
title: AI Engineering as a Discipline
page_id: analyses/ai-engineering-as-a-discipline
page_type: analysis
revision_id: 1
created: 2026-05-17 18:30:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
- llm
- foundation-models
- ml-engineering
- software-engineering
- synthesis
sources:
- sources/huyen-2022-designing-ml-systems
- sources/huyen-2025-ai-engineering
- sources/raschka-2024-build-llm-from-scratch
- sources/alammar-2024-hands-on-llm
- sources/berryman-2024-prompt-engineering-llms
- sources/mendelevitch-2025-hands-on-rag
- sources/oshin-2025-learning-langchain
- sources/wilson-2024-llm-security-playbook
- sources/thomas-2025-ai-value-creators
- sources/percival-2020-architecture-patterns-python
- sources/nelson-2024-swe-for-data-scientists
- sources/caelen-2023-developing-apps-gpt4
- sources/boonstra-2024-google-prompt-engineering
- sources/taulli-2024-ai-assisted-programming
- sources/bratanic-2025-essential-graphrag
- sources/hermans-2024-code-reading-in-practice
- sources/anon-2024-vector-databases-rag
- sources/barrasa-2023-building-knowledge-graphs
related:
- concepts/ai-engineering
- concepts/foundation-model
- concepts/foundation-models
- concepts/retrieval-augmented-generation
- concepts/prompt-engineering
- concepts/fine-tuning
- concepts/in-context-learning
- concepts/llm-evaluation
- concepts/ai-agents
- concepts/inference-optimization
- concepts/dataset-engineering
- concepts/sampling-strategies
- concepts/rlhf
- concepts/parameter-efficient-fine-tuning
- concepts/llm-as-a-judge
- concepts/continual-learning
- concepts/model-compression
- entities/chip-huyen
mind_map_priority: high
schema_version: 2
uuid: bf46678c-8d40-546e-893b-1d79987f240e
content_hash: sha256:24a6c9e34b7a13739fd1df1597241f2366416316af26ea1fed36361acafc3a9f
---

<!-- AUTHORED REGION START -->
# AI Engineering as a Discipline

## Overview

Between 2023 and 2025, a new engineering discipline crystallised around foundation models. It is not machine learning engineering — it does not centre on training, feature engineering, or model selection. It is not software engineering — its primary artefacts are probabilistic, non-deterministic, and unbounded in input space. It is not data science — the model is given, not chosen, and the work is downstream of the weights. Across the 18 books surveyed here, a coherent picture emerges: AI engineering is the practice of *adapting* pre-trained foundation models into reliable, evaluable, secure, and cost-bounded applications. Its primitives are prompts, retrieval pipelines, agent loops, evaluation rubrics, and inference budgets. Its borrowed primitives — repositories, services, tests, monitoring — come straight from classical software engineering, lightly refactored for stochastic outputs.

**Thesis:** AI engineering is the engineering discipline that emerges when the model is a procured commodity rather than a built artefact. It inherits the systems thinking of ML engineering and the modularity of software engineering, but its centre of gravity is *the prompt-context-evaluation triad*, a stack that did not exist as a first-class engineering concern before 2023.

---

## The Huyen trajectory: ML Engineering (2022) -> AI Engineering (2025)

[[entities/chip-huyen|Chip Huyen]]'s two books are the cleanest natural experiment in the literature. Same author, same publisher ([[entities/oreilly-media|O'Reilly]]), same audience, same insistence on *first principles over tools*. Three years apart. What changed is the entire object of study.

[[sources/huyen-2022-designing-ml-systems|Designing ML Systems (Huyen 2022)]] is built around a lifecycle that *starts with the model the team will train*: data engineering, feature engineering, labelling, training, evaluation, deployment, monitoring. The implicit premise is that the production team owns the weights.

[[sources/huyen-2025-ai-engineering|AI Engineering (Huyen 2025)]] starts from the opposite assumption: *the weights are someone else's*. The lifecycle compresses train-then-deploy into a single procurement decision and expands adapt-then-deploy into the bulk of the book. Huyen names this shift explicitly: foundation models flipped the workflow from *train-then-deploy* to *adapt-then-deploy*, making prompt, context, and evaluation the new core competencies.

### What changed between the two books

| Dimension | Designing ML Systems (2022) | AI Engineering (2025) |
|---|---|---|
| **Primary artefact** | Model trained by the team | Foundation model adapted by the team |
| **Core competency** | Feature engineering, labelling, training pipelines | Prompt engineering, retrieval, evaluation |
| **Data work** | Label acquisition, weak supervision, feature stores | Dataset curation, synthesis, distillation, deduplication |
| **Adaptation toolkit** | Hyperparameter search, ensembles, retraining | Prompting -> RAG -> finetuning -> custom pretraining (escalation hierarchy) |
| **Evaluation** | Offline metrics + slice-based + A/B in production | LLM-as-a-judge, comparative ranking, reference metrics, plus everything from 2022 |
| **Deployment metrics** | Latency, throughput, accuracy, freshness | TTFT, TPOT, throughput, goodput, MFU, MBU |
| **Failure modes** | Distribution shift, label drift, training-serving skew | Hallucination, prompt injection, tool failure, reflection error, plus all of 2022 |
| **Cost lever** | Model compression, batch vs. online prediction | Quantisation, KV-cache, speculative decoding, model routing, caching |
| **Adversarial surface** | Adversarial inputs, model theft | Prompt injection, jailbreaks, data poisoning, training-data extraction |
| **Iteration unit** | Retraining run | Prompt revision + eval rerun |
| **Centre of mass** | Pipeline + monitoring | Prompt + context + evaluation |

### What stayed the same

Both books share an *opinionated insistence on first principles over tooling*. Both refuse to anchor to specific vendor APIs. Both treat evaluation as the practice that survives every other architectural change. Both elevate monitoring to a chapter, not a footnote. Both reject "one model per system" as a deployment fantasy. The MLOps platform layer — orchestration, observability, deployment topology — is largely intact between the two books. What changed is the workload running on top of it.

[[sources/huyen-2022-designing-ml-systems|Huyen 2022]] introduced [[concepts/continual-learning|continual learning]] as a maturity model from manual retraining to fully automated updates. [[sources/huyen-2025-ai-engineering|Huyen 2025]] inherits that mental model but redirects it: the "retraining" of an AI-engineering application is not gradient updates, it is prompt versioning, retrieval-index refresh, finetune-checkpoint rotation, and feedback-loop closure.

---

## What's new with foundation models

Across the corpus, five competency clusters appear that did not exist in 2022 ML engineering and do not exist in classical software engineering.

### 1. Prompt engineering as program design

The most counterintuitive shift in the corpus: the *prompt is a program*. [[sources/berryman-2024-prompt-engineering-llms|Berryman & Ziegler (2024)]] — two of GitHub Copilot's founding engineers — make this the spine of their book. They frame prompt engineering as *document engineering*: shape the prompt so it reads like the kind of document the model saw during training. They reverse-engineer the OpenAI tool-calling wire format (ChatML with TypeScript-style function signatures) and explain why each token in a tool call narrows a classification subproblem.

[[sources/boonstra-2024-google-prompt-engineering|Boonstra (2024)]], Google's prompt engineering whitepaper, codifies the practice with concrete sampling recipes (temperature 0.2 / top-K 0.95 / top-P 30 for balanced output, 0 for math and CoT) and a prompt-documentation table template (name, goal, model, sampling settings, prompt, output). [[sources/huyen-2025-ai-engineering|Huyen 2025]] dedicates a chapter to it and treats version control of prompts as a first-class concern alongside model versioning.

Prompt engineering appears in 6 of the 18 books as a named competency; chain-of-thought prompting appears in 6 books as a distinct technique. This is the single most cross-cited skill in the corpus.

### 2. Retrieval-augmented generation (RAG) pipelines

RAG appears in **10 of 18 books** — the most cross-cited concept in the corpus. It is the closest thing the discipline has to a default architecture pattern. The treatments differ:

- [[sources/mendelevitch-2025-hands-on-rag|Mendelevitch & Bao (2025)]] give the canonical two-flow blueprint: ingest flow (extract -> chunk -> embed -> store) and query flow (retrieve -> rerank -> generate -> guardrail). Their core contribution is the POC-to-production gap, with a KPI table (latency mean/median, context precision/recall, hallucination rate, answer relevance) that operationalises "good RAG".
- [[sources/alammar-2024-hands-on-llm|Alammar & Grootendorst (2024)]] walk through a complete RAG pipeline (chunking -> embeddings -> vector store -> dense retrieval -> reranking -> grounded generation -> evaluation) with both Cohere and local-model implementations.
- [[sources/anon-2024-vector-databases-rag|Anderson (2024)]] reduces RAG to its retrieval substrate: vector databases as the high-dimensional retrieval primitive that makes grounding feasible.
- [[sources/bratanic-2025-essential-graphrag|Bratanic & Hane (2025)]] argue vanilla RAG over text chunks leaves accuracy on the table; pair LLMs with a knowledge graph for precise, explainable retrieval. They reproduce Microsoft's GraphRAG pipeline (chunking -> community summarisation -> global/local search).
- [[sources/oshin-2025-learning-langchain|Oshin & Campos (2025)]] frame RAG as one position on a single "composition of techniques" arc that runs from one-shot LLM call through RAG, memory, agents, and evaluation.

The convergence on RAG is the strongest signal that AI engineering has stabilised around a default pattern.

### 3. Agentic patterns and tool use

[[sources/huyen-2025-ai-engineering|Huyen 2025]] formalises [[concepts/ai-agents|AI agents]] as systems where a foundation model plans, invokes tools, observes outputs, reflects, and revises. She catalogues failure modes — invalid tool, invalid parameters, goal failure, reflection error — and ties them to a memory taxonomy (internal knowledge, short-term context, long-term external memory).

[[sources/oshin-2025-learning-langchain|Oshin & Campos (2025)]] — written with first-party authority by a LangGraph core maintainer — articulates the *agency-vs-reliability frontier* as the central design decision. They catalogue cognitive architectures (router, parallelisation, orchestrator-worker, reflection) and multi-agent topologies (supervisor, swarm) as named, reusable patterns. [[sources/bratanic-2025-essential-graphrag|Bratanic & Hane]] add agentic-RAG as a distinct retrieval strategy.

### 4. Inference-time control and cost engineering

[[sources/huyen-2025-ai-engineering|Huyen 2025]] introduces a precise vocabulary for inference performance:

| Metric | Meaning |
|---|---|
| **TTFT** | Time to first token (user-perceived initial latency) |
| **TPOT** | Time per output token (streaming throughput) |
| **Throughput** | Total tokens per second across all requests |
| **Goodput** | Throughput meeting an SLA constraint |
| **MFU** | Model FLOPs utilisation |
| **MBU** | Model bandwidth utilisation |

This separates user-visible latency from system-level utilisation, exposing the latency-throughput tradeoff that ML engineering's classical "latency vs. accuracy" framing could not capture. [[sources/thomas-2025-ai-value-creators|Thomas et al (2025)]] tie this to the "generative computing" thesis: structured prompts, runtimes, memory slots, and KV-cache reuse as a software-engineering discipline that replaces today's brittle mega-prompts.

[[sources/raschka-2024-build-llm-from-scratch|Raschka (2024)]] grounds these abstractions: his from-scratch implementation walks through KV-caching, temperature scaling, and top-k sampling at the matrix-multiply level, making the inference-optimisation vocabulary concrete.

### 5. Hallucination management and grounding

Classical ML engineering had distribution shift; AI engineering has *hallucination*. [[sources/caelen-2023-developing-apps-gpt4|Caelen & Blete (2023)]] surface it as a first-class application risk. [[sources/thomas-2025-ai-value-creators|Thomas et al (2025)]] treat it as the central enterprise objection to GenAI. [[sources/mendelevitch-2025-hands-on-rag|Mendelevitch & Bao]] make hallucination rate one of their five production KPIs. The corpus does not have a settled mitigation framework, but the convergence on RAG as the grounding mechanism is the field's working answer.

[[sources/wilson-2024-llm-security-playbook|Wilson (2024)]] adds the adversarial dimension: prompt injection, data poisoning, and jailbreaks are amplified failure modes of the same probabilistic substrate that produces hallucinations.

---

## What stays the same

The corpus is unambiguous: software-engineering primitives do not go away when you cross into AI engineering. [[sources/percival-2020-architecture-patterns-python|Percival & Gregory (2020)]] is published before ChatGPT and contains zero foundation-model content — yet every modern RAG pipeline reinvents their patterns:

- The **Repository pattern** reappears as the vector-database abstraction in [[sources/mendelevitch-2025-hands-on-rag|Mendelevitch & Bao]] and [[sources/anon-2024-vector-databases-rag|Anderson]].
- The **Service Layer** reappears as the LangGraph orchestration node in [[sources/oshin-2025-learning-langchain|Oshin & Campos]].
- **Domain-Driven Design** reappears as the schema-design problem in [[sources/barrasa-2023-building-knowledge-graphs|Barrasa & Webber (2023)]] and [[sources/bratanic-2025-essential-graphrag|Bratanic & Hane]] (the property-graph model is a domain model).
- **Unit of Work** and **aggregates** reappear as the consistency-boundary problem when an agent edits external state.

[[sources/nelson-2024-swe-for-data-scientists|Nelson (2024)]] is the connective tissue between data work and SWE work, predating the AI engineering label but anticipating it. Her five attributes of good code — simplicity, modularity, readability, efficiency, robustness — apply unchanged to LLM-app code. Her warning about training-serving skew as a DRY-versus-deployment conflict generalises directly to prompt-template skew between dev and prod.

[[sources/hermans-2024-code-reading-in-practice|Hermans (2024)]] is the most surprising "stays the same": her five-dimension framework for reading code (structure, domain, code quality, context, collaboration) is the only treatment in the corpus of what to do when an AI assistant generates code you must then maintain. As [[sources/taulli-2024-ai-assisted-programming|Taulli (2024)]] notes, AI-assisted programming makes code reading more important, not less.

[[sources/huyen-2022-designing-ml-systems|Huyen 2022]] itself remains on the AI engineer's shelf: distribution shift, monitoring, continual learning, and test-in-production are unchanged. Only the *unit being monitored* changed.

---

## The skill stack: what an AI Engineer must know

Synthesising the corpus, an AI engineer's competencies form a four-layer stack:

| Layer | Competency | Anchor sources |
|---|---|---|
| **Foundation (theory)** | Transformer internals, attention, tokenization, sampling | [[sources/raschka-2024-build-llm-from-scratch|Raschka]], [[sources/alammar-2024-hands-on-llm|Alammar & Grootendorst]], [[sources/caelen-2023-developing-apps-gpt4|Caelen & Blete]] |
| **Adaptation (primary)** | Prompt engineering, RAG, finetuning (PEFT/LoRA/RLHF), agents | [[sources/huyen-2025-ai-engineering|Huyen 2025]], [[sources/berryman-2024-prompt-engineering-llms|Berryman & Ziegler]], [[sources/boonstra-2024-google-prompt-engineering|Boonstra]], [[sources/mendelevitch-2025-hands-on-rag|Mendelevitch & Bao]], [[sources/oshin-2025-learning-langchain|Oshin & Campos]] |
| **Production (engineering)** | Evaluation, observability, inference cost, deployment, security, modular code | [[sources/huyen-2022-designing-ml-systems|Huyen 2022]], [[sources/huyen-2025-ai-engineering|Huyen 2025]], [[sources/percival-2020-architecture-patterns-python|Percival & Gregory]], [[sources/nelson-2024-swe-for-data-scientists|Nelson]], [[sources/wilson-2024-llm-security-playbook|Wilson]] |
| **Strategy (business)** | Build-vs-buy, value identification, governance, fit-for-purpose model mix | [[sources/thomas-2025-ai-value-creators|Thomas et al]], [[sources/taulli-2024-ai-assisted-programming|Taulli]] |

Concretely, the AI engineer must be fluent in:

1. **Prompt design** — the system/user/role split, few-shot construction, format specification, defensive prompting against injection. ([[sources/berryman-2024-prompt-engineering-llms|Berryman]], [[sources/boonstra-2024-google-prompt-engineering|Boonstra]])
2. **Retrieval architecture** — chunking strategies, embeddings selection, vector vs. hybrid vs. graph retrieval, reranking. ([[sources/mendelevitch-2025-hands-on-rag|Mendelevitch & Bao]], [[sources/bratanic-2025-essential-graphrag|Bratanic & Hane]])
3. **Evaluation methodology** — LLM-as-a-judge, comparative ranking, slice-based, telemetry-driven, KPI tables. ([[sources/huyen-2025-ai-engineering|Huyen 2025]], [[sources/mendelevitch-2025-hands-on-rag|Mendelevitch & Bao]], [[sources/oshin-2025-learning-langchain|Oshin & Campos]])
4. **Foundation-model selection** — closed vs. open, parameter count vs. context window vs. cost vs. modality. ([[sources/huyen-2025-ai-engineering|Huyen 2025]], [[sources/thomas-2025-ai-value-creators|Thomas et al]])
5. **Inference-time control** — sampling parameters, structured output, function calling, streaming. ([[sources/huyen-2025-ai-engineering|Huyen 2025]], [[sources/raschka-2024-build-llm-from-scratch|Raschka]])
6. **Security** — OWASP LLM Top 10, prompt injection, training-data extraction, RBAC over retrieval. ([[sources/wilson-2024-llm-security-playbook|Wilson]], [[sources/mendelevitch-2025-hands-on-rag|Mendelevitch & Bao]])
7. **Framework fluency** — LangChain/LangGraph composition, agent topologies, deployment patterns. ([[sources/oshin-2025-learning-langchain|Oshin & Campos]], [[sources/caelen-2023-developing-apps-gpt4|Caelen & Blete]])
8. **Software engineering hygiene** — modular code, testing, repository pattern, observability. ([[sources/percival-2020-architecture-patterns-python|Percival & Gregory]], [[sources/nelson-2024-swe-for-data-scientists|Nelson]])
9. **Business framing** — when not to use AI, where value accrues, governance as a moat. ([[sources/thomas-2025-ai-value-creators|Thomas et al]])

The first five did not exist on a 2022 ML engineer's shelf. The last four were already there.

---

## Where books disagree

The corpus does not yet speak with one voice. Three contradictions stand out.

### Contradiction 1: Fine-tune vs RAG

When does customisation require finetuning rather than retrieval?

- [[sources/huyen-2025-ai-engineering|Huyen 2025]] is explicit and opinionated: *try prompting before RAG, RAG before finetuning, finetuning before custom pretraining*. The escalation hierarchy treats finetuning as a cost-of-last-resort.
- [[sources/mendelevitch-2025-hands-on-rag|Mendelevitch & Bao (2025)]] take the RAG-first stance even more strongly: most enterprise problems are knowledge-retrieval problems, not knowledge-acquisition problems.
- [[sources/alammar-2024-hands-on-llm|Alammar & Grootendorst]] devote substantial space to finetuning (full SFT, QLoRA, preference tuning) as a peer alternative, not a fallback. Their stance is that finetuning is underused, not overused.
- [[sources/raschka-2024-build-llm-from-scratch|Raschka]] takes finetuning seriously enough to implement LoRA from scratch in Appendix E, framing it as a core competency rather than an escalation.

The contradiction is *which adaptation lever is the default*. The corpus has not converged.

### Contradiction 2: Build from scratch vs. build on APIs

Where does the boundary lie between "AI engineer who builds on top" and "AI engineer who builds the model"?

- [[sources/raschka-2024-build-llm-from-scratch|Raschka (2024)]] implements GPT-2 in PyTorch from primitive ops, with no Hugging Face dependency. Pedagogy and architectural mastery are the explicit goals; he stops at supervised fine-tuning.
- [[sources/caelen-2023-developing-apps-gpt4|Caelen & Blete (2023)]] and [[sources/oshin-2025-learning-langchain|Oshin & Campos (2025)]] build entirely on hosted APIs and frameworks. The transformer is a black box; the work is composition.
- [[sources/alammar-2024-hands-on-llm|Alammar & Grootendorst]] sit in the middle: visual transformer internals plus practitioner pipelines.

Both stances are taught as "AI engineering" but they represent opposing answers to the question *what does the AI engineer build?* Raschka's reader understands KV-caching from first principles; Oshin's reader has never written a softmax. They will both call themselves AI engineers.

### Contradiction 3: Agentic vs. scripted

How much agency is wise to grant a foundation model?

- [[sources/oshin-2025-learning-langchain|Oshin & Campos]] embrace the agentic frontier with named patterns (orchestrator-worker, reflection, swarm, supervisor). LangGraph exists *because* multi-step agency is the future they bet on.
- [[sources/huyen-2025-ai-engineering|Huyen 2025]] is more cautious: she catalogues agent failure modes (invalid tool, invalid parameters, goal failure, reflection error) as a warning, not a feature list.
- [[sources/berryman-2024-prompt-engineering-llms|Berryman & Ziegler]] — coming from Copilot — favour tightly scripted prompt assembly with deterministic context retrieval, snippetization, scoring, and budgeted prompt assembly. The "agent" is replaced by an engineered feedforward pipeline.
- [[sources/thomas-2025-ai-value-creators|Thomas et al]] place agentic AI as an emerging tier but warn that governance maturity must precede agency.

The unresolved question: is reliability achieved by reducing agency or by improving reflection? The corpus splits roughly 50/50.

---

## What's NOT yet codified

The corpus collectively leaves several gaps. These are the questions AI engineering has not yet answered.

| Gap | Evidence from corpus |
|---|---|
| **Evaluation methodology consensus** | Every book proposes an eval framework; none agrees on a standard. LLM-as-a-judge is widely used and widely critiqued for bias and calibration ([[sources/huyen-2025-ai-engineering|Huyen 2025]]). |
| **Agent reliability standards** | Failure-mode taxonomies exist ([[sources/huyen-2025-ai-engineering|Huyen]], [[sources/oshin-2025-learning-langchain|Oshin]]) but there is no agreed reliability metric analogous to MTBF. |
| **Cost engineering as a sub-discipline** | TTFT/TPOT/MFU vocabulary exists in [[sources/huyen-2025-ai-engineering|Huyen 2025]]; nothing analogous to FinOps for foundation models exists yet. |
| **Multi-modal application patterns** | Multi-modal models are mentioned in [[sources/huyen-2025-ai-engineering|Huyen 2025]], [[sources/thomas-2025-ai-value-creators|Thomas et al]], [[sources/alammar-2024-hands-on-llm|Alammar & Grootendorst]] but no book provides a multi-modal application architecture comparable to the RAG blueprint. |
| **Prompt versioning and CI** | Every book treats prompts as code, but no book gives a "prompt-git" workflow. |
| **Feedback-loop closure** | Implicit telemetry ([[sources/berryman-2024-prompt-engineering-llms|Berryman & Ziegler]]) and online evaluation ([[sources/oshin-2025-learning-langchain|Oshin & Campos]]) are sketched; no end-to-end "preference data flywheel" recipe exists. |
| **Model deprecation handling** | Closed-model APIs evolve; no book addresses how to migrate prompts and evals across model versions in production. |
| **Hallucination measurement standard** | [[sources/mendelevitch-2025-hands-on-rag|Mendelevitch & Bao]] include hallucination rate as a KPI but the field has no agreed measurement protocol. |

These gaps are where AI engineering as a discipline still has homework.

---

## Decision framework: where does AI Engineering sit?

The corpus implies — though no single book states — a decision boundary between AI engineering, ML engineering, and software engineering. Use this table to classify a problem.

| Question to ask | If yes -> | Anchor source |
|---|---|---|
| Is the model already trained by someone else, and is your work to adapt it? | **AI Engineering** | [[sources/huyen-2025-ai-engineering|Huyen 2025]] |
| Are you training the model from data your team owns? | **ML Engineering** | [[sources/huyen-2022-designing-ml-systems|Huyen 2022]] |
| Is the problem deterministic, with no probabilistic component? | **Software Engineering** | [[sources/percival-2020-architecture-patterns-python|Percival & Gregory]] |
| Is the primary failure mode hallucination, prompt injection, or context-window overflow? | **AI Engineering** | [[sources/wilson-2024-llm-security-playbook|Wilson]], [[sources/mendelevitch-2025-hands-on-rag|Mendelevitch & Bao]] |
| Is the primary failure mode distribution shift, label drift, or feature staleness? | **ML Engineering** | [[sources/huyen-2022-designing-ml-systems|Huyen 2022]] |
| Is the primary cost lever quantisation, caching, or routing between foundation models? | **AI Engineering** | [[sources/huyen-2025-ai-engineering|Huyen 2025]] |
| Is the primary cost lever model compression, batch vs. online, or feature-store reuse? | **ML Engineering** | [[sources/huyen-2022-designing-ml-systems|Huyen 2022]] |
| Is the iteration unit a prompt edit + eval rerun? | **AI Engineering** | [[sources/berryman-2024-prompt-engineering-llms|Berryman & Ziegler]] |
| Is the iteration unit a retraining run? | **ML Engineering** | [[sources/huyen-2022-designing-ml-systems|Huyen 2022]] |
| Is the iteration unit a code change + unit-test pass? | **Software Engineering** | [[sources/nelson-2024-swe-for-data-scientists|Nelson]] |

### Decision tree, compact form

```
START
  |
  +-- Are model weights produced or procured?
  |     |
  |     +-- Produced -> ML Engineering
  |     +-- Procured -> AI Engineering
  |
  +-- Are outputs probabilistic / open-ended?
  |     |
  |     +-- No  -> Software Engineering
  |     +-- Yes -> AI or ML Engineering (use above split)
  |
  +-- Does the system include a retrieval or agent loop?
        |
        +-- Yes -> AI Engineering (specifically RAG / agent sub-track)
        +-- No  -> AI Engineering (prompt-only sub-track) or ML Engineering
```

The boundaries are not crisp. A team can be doing all three simultaneously: ML engineering for an embedding model they finetune, AI engineering for the RAG pipeline that uses it, software engineering for the FastAPI service that exposes it. The discipline's value is recognising *which mode you are in* on each layer.

---

## A canonical AI Engineering reference architecture

Synthesising [[sources/huyen-2025-ai-engineering|Huyen 2025]], [[sources/mendelevitch-2025-hands-on-rag|Mendelevitch & Bao]], [[sources/oshin-2025-learning-langchain|Oshin & Campos]], and [[sources/wilson-2024-llm-security-playbook|Wilson]], a reference AI-engineering application has the following shape:

```
+------------------------------+
|         User / Client        |
+------------------------------+
              |
              v
+------------------------------+
|   Input Guardrails           |   <- prompt injection, PII, abuse (Wilson)
+------------------------------+
              |
              v
+------------------------------+
|   Router / Model Selection   |   <- closed/open, fit-for-purpose (Huyen)
+------------------------------+
              |
              v
+------------------------------+      +-----------------+
|   Retrieval Layer            | ---> | Vector / Graph  |
|   (chunk, embed, retrieve)   |      |   Store (RAG)   |
+------------------------------+      +-----------------+
              |
              v
+------------------------------+
|   Prompt Assembly            |   <- system + context + user + tools (Berryman)
|   (within token budget)      |
+------------------------------+
              |
              v
+------------------------------+
|   Foundation Model Inference |   <- sampling controls, structured output (Huyen, Boonstra)
+------------------------------+
              |
              v
+------------------------------+
|   Tool Use / Agent Loop      |   <- ReAct, reflection, memory (Oshin, Huyen)
|   (optional)                 |
+------------------------------+
              |
              v
+------------------------------+
|   Output Guardrails          |   <- hallucination, jailbreak filter (Wilson, Mendelevitch)
+------------------------------+
              |
              v
+------------------------------+
|   Evaluation & Telemetry     |   <- LLM-as-judge, KPIs, feedback (Huyen, Mendelevitch)
+------------------------------+
              |
              v
+------------------------------+
|         User / Client        |
+------------------------------+
```

This stack would be unrecognisable to a 2022 ML engineer reading [[sources/huyen-2022-designing-ml-systems|Designing ML Systems]]. Every layer except retrieval has changed name, and every layer references concerns that did not exist as engineering primitives three years prior.

---

## Closing observation

The clearest evidence that AI engineering is a distinct discipline is not in any single book — it is in the fact that one author, on the same topic ("how to ship intelligent systems"), wrote two books three years apart and produced *non-overlapping* tables of contents. [[entities/chip-huyen|Chip Huyen]]'s 2022 lifecycle (data -> features -> model -> deploy -> monitor) and her 2025 lifecycle (procure -> prompt -> retrieve -> evaluate -> serve) describe the same business problem with a different engineering substrate. The 16 other books, taken together, fill in the substrate's primitives — prompts, retrieval, agents, security, cost, software-engineering hygiene — and surface the contradictions the discipline has yet to resolve.

AI engineering is the engineering of *adaptation* on top of foundation models. It is held in place by classical software engineering below and by ML engineering's monitoring discipline alongside. Its identity comes from the layer in the middle.

---

## See Also

- [[concepts/ai-engineering|AI Engineering]] — the concept page
- [[concepts/foundation-models|Foundation Models]] / [[concepts/foundation-model|Foundation Model]]
- [[concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[concepts/prompt-engineering|Prompt Engineering]]
- [[concepts/in-context-learning|In-Context Learning]]
- [[concepts/ai-agents|AI Agents]]
- [[concepts/llm-as-a-judge|LLM-as-a-Judge]]
- [[concepts/inference-optimization|Inference Optimization]]
- [[concepts/dataset-engineering|Dataset Engineering]]
- [[concepts/sampling-strategies|Sampling Strategies]]
- [[concepts/parameter-efficient-fine-tuning|Parameter-Efficient Fine-Tuning]]
- [[concepts/rlhf|RLHF]]
- [[concepts/continual-learning|Continual Learning]]
- [[concepts/model-compression|Model Compression]]
- [[entities/chip-huyen|Chip Huyen]]
- [[sources/huyen-2022-designing-ml-systems|Designing ML Systems (Huyen 2022)]]
- [[sources/huyen-2025-ai-engineering|AI Engineering (Huyen 2025)]]
- [[sources/raschka-2024-build-llm-from-scratch|Build LLM from Scratch (Raschka 2024)]]
- [[sources/alammar-2024-hands-on-llm|Hands-On LLMs (Alammar & Grootendorst 2024)]]
- [[sources/berryman-2024-prompt-engineering-llms|Prompt Engineering for LLMs (Berryman & Ziegler 2024)]]
- [[sources/mendelevitch-2025-hands-on-rag|Hands-On RAG (Mendelevitch & Bao 2025)]]
- [[sources/oshin-2025-learning-langchain|Learning LangChain (Oshin & Campos 2025)]]
- [[sources/wilson-2024-llm-security-playbook|LLM Security Playbook (Wilson 2024)]]
- [[sources/thomas-2025-ai-value-creators|AI Value Creators (Thomas et al 2025)]]
- [[sources/percival-2020-architecture-patterns-python|Architecture Patterns with Python (Percival & Gregory 2020)]]
- [[sources/nelson-2024-swe-for-data-scientists|SWE for Data Scientists (Nelson 2024)]]
- [[sources/caelen-2023-developing-apps-gpt4|Developing Apps with GPT-4 (Caelen & Blete 2023)]]
- [[sources/boonstra-2024-google-prompt-engineering|Prompt Engineering (Boonstra 2024)]]
- [[sources/taulli-2024-ai-assisted-programming|AI-Assisted Programming (Taulli 2024)]]
- [[sources/hermans-2024-code-reading-in-practice|Code Reading in Practice (Hermans 2024)]]
- [[sources/bratanic-2025-essential-graphrag|Essential GraphRAG (Bratanic & Hane 2025)]]
- [[sources/anon-2024-vector-databases-rag|Vector Databases for RAG (Anderson 2024)]]
- [[sources/barrasa-2023-building-knowledge-graphs|Building Knowledge Graphs (Barrasa & Webber 2023)]]
- [[../MIND_MAP|MIND_MAP node [2] — AI Engineering]]

<!-- AUTHORED REGION END -->
