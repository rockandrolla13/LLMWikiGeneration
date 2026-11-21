---
content_hash: sha256:d311e692b12f8be1a1a6379b459ed39831920f3c65adc9d4cd92e470bc494385
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/instruction-fine-tuning
page_type: concept
related:
- concepts/transformers
- concepts/direct-preference-optimization
- entities/stanford-alpaca
revision_id: 3
schema_version: 2
sources:
- sources/raschka-2024-build-llm-from-scratch
- sources/liu-2025-build-fine-tune-small-language-model
tags:
- ai-engineering
- transformers
title: Instruction Fine-Tuning
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 4a7be65f-a6ad-5ed9-90a1-50dad4e0945c
---

<!-- AUTHORED REGION START -->
# Instruction Fine-Tuning

## Definition

Supervised fine-tuning of a pretrained LLM on (instruction, response) pairs formatted with a prompt template (e.g. Alpaca-style) so the model learns to follow natural-language instructions rather than merely complete text. The final stage in transforming a base model into a chat or assistant model.

## Sources

- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]
- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025): Full SFT on Alpaca with the loss computed only on response tokens. Here SFT is followed by a DPO stage rather than being the last step.

## Related Concepts

- [[concepts/transformers]]

<!-- AUTHORED REGION END -->