---
title: Prompt Engineering
page_id: sources/boonstra-2024-google-prompt-engineering
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Lee Boonstra
year: 2024
publisher: Google
edition: null
is_early_release: false
page_count_estimate: 68
tags:
- ai-engineering
- prompt-engineering
related:
- concepts/automatic-prompt-engineering
- concepts/chain-of-thought-prompting
- concepts/few-shot-prompting
- concepts/llm-sampling-controls
- concepts/prompt-engineering
- concepts/react-prompting
- concepts/role-prompting
- concepts/self-consistency
- concepts/step-back-prompting
- concepts/system-prompting
- concepts/tree-of-thoughts
- concepts/zero-shot-prompting
- entities/gemini
- entities/google
- entities/jason-wei
- entities/langchain
- entities/lee-boonstra
- entities/shunyu-yao
- entities/tom-brown
- entities/vertex-ai
- entities/xuezhi-wang
mind_map_priority: medium
revision_hash: sha256:33e32f4fdcec0b68
---

# Prompt Engineering

**Authors:** [[entities/lee-boonstra|Lee Boonstra]]

**Year:** 2024

**Publisher:** Google

## Summary

Lee Boonstra's [[prompt-engineering|Prompt Engineering]] whitepaper is Google's short, practitioner-facing guide (~68 pages) to crafting prompts for large language models, written primarily against Gemini in Vertex AI but presented as broadly applicable to GPT, Claude, Gemma, and LLaMA. It argues that prompting is an iterative engineering discipline, not a casual chat activity: outputs depend jointly on the model, its [[llm-sampling-controls|sampling controls]] (temperature, top-K, top-P), wording, examples, structure, and operational discipline around documenting attempts.

The whitepaper walks through a canonical ladder of techniques: [[zero-shot-prompting|zero-shot]] and [[few-shot-prompting|few-shot]] prompting, [[system-prompting|system]] / contextual / [[role-prompting|role]] prompts for framing, then advanced reasoning methods - [[step-back-prompting|step-back prompting]], [[chain-of-thought-prompting|chain-of-thought]], [[self-consistency|self-consistency]] sampling, [[tree-of-thoughts|tree-of-thoughts]], and [[react-prompting|ReAct]] for tool-using agents. It also covers [[automatic-prompt-engineering|automatic prompt engineering]] (using an LLM to generate and score candidate prompts via BLEU/ROUGE) and a dedicated section on code prompts (writing, explaining, translating, debugging).

The second half is a best-practices manual: provide diverse examples, prefer positive instructions over negative constraints, control max output length, parameterise prompts with variables, request JSON output for structured tasks (with json-repair for truncation), use JSON Schemas to structure inputs, set temperature to 0 for CoT, and document every prompt attempt in a standardised table (name, goal, model, temperature, top-K/top-P, prompt, output). The intended audience is developers and applied ML practitioners building production LLM features on Vertex AI or comparable platforms - not researchers - and the angle versus competing prompt guides is its grounding in Google's Gemini configuration knobs and Vertex AI Studio workflow.

## Key Contributions

- A clean taxonomy separating system, contextual, and role prompting as orthogonal framing concerns
- Concrete starting recipes for temperature/top-K/top-P (e.g. 0.2/0.95/30 for balanced output; 0 for math and CoT)
- A standardised prompt-documentation table template (name, goal, model, sampling settings, prompt, output) for tracking iterations
- Prefer-instructions-over-constraints heuristic with worked DO/DON'T examples
- End-to-end ReAct agent code example using LangChain + VertexAI + SerpAPI counting Metallica band members' children

## Key Topics Covered

prompt-engineering, llm-sampling-controls, zero-shot-prompting, few-shot-prompting, system-prompting, role-prompting, chain-of-thought-prompting, self-consistency, tree-of-thoughts, react-prompting, step-back-prompting, automatic-prompt-engineering, code generation prompts, JSON output and JSON Schema for LLMs, prompt documentation discipline

## Questions Raised

- How do prompting techniques transfer across model families (Gemini vs GPT vs Claude vs open-source) without re-tuning?
- What is the right evaluation metric for non-classification prompts - BLEU/ROUGE are mentioned but acknowledged as weak proxies for LLM quality?
- How should prompt versioning integrate with model versioning in production CI/CD pipelines?
- When does fine-tuning become preferable to ever-more-elaborate prompting?
- How should multimodal prompts (image + text) be designed - the whitepaper flags but does not develop this

## Intended Audience

Developers and applied ML engineers building LLM-powered features on Vertex AI (or comparable platforms) who want a structured, Google-flavoured introduction to prompt engineering techniques and operational best practices.

## Key Concepts in This Source

- [[concepts/prompt-engineering|Prompt Engineering]]
- [[concepts/zero-shot-prompting|Zero-shot Prompting]]
- [[concepts/few-shot-prompting|Few-shot Prompting]]
- [[concepts/chain-of-thought-prompting|Chain-of-Thought Prompting]]
- [[concepts/self-consistency|Self-Consistency]]
- [[concepts/tree-of-thoughts|Tree of Thoughts]]
- [[concepts/react-prompting|ReAct Prompting]]
- [[concepts/step-back-prompting|Step-Back Prompting]]
- [[concepts/system-prompting|System Prompting]]
- [[concepts/role-prompting|Role Prompting]]
- [[concepts/automatic-prompt-engineering|Automatic Prompt Engineering]]
- [[concepts/llm-sampling-controls|LLM Sampling Controls]]

## Entities

- [[entities/lee-boonstra|Lee Boonstra]]
- [[entities/google|Google]]
- [[entities/gemini|Gemini]]
- [[entities/vertex-ai|Vertex AI]]
- [[entities/langchain|LangChain]]
- [[entities/jason-wei|Jason Wei]]
- [[entities/shunyu-yao|Shunyu Yao]]
- [[entities/tom-brown|Tom Brown]]
- [[entities/xuezhi-wang|Xuezhi Wang]]
