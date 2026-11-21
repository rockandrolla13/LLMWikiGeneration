---
content_hash: sha256:104d706636d6780f66e713e4968982e3114b9eeed9f54e8be19352edb6a75625
created: '2026-05-17T16:44:06Z'
mind_map_priority: high
page_id: concepts/rlhf
page_type: concept
related:
- concepts/direct-preference-optimization
revision_id: 2
schema_version: 2
sources:
- sources/berryman-2024-prompt-engineering-llms
- sources/caelen-2023-developing-apps-gpt4
- sources/huyen-2025-ai-engineering
- sources/liu-2025-build-fine-tune-small-language-model
tags:
- ai-engineering
title: Reinforcement Learning from Human Feedback
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 4b8a6f80-9118-5ffa-82b2-fbd13cc3d648
---

<!-- AUTHORED REGION START -->
# Reinforcement Learning from Human Feedback

## Definition

A post-training technique that aligns a model with human preferences by training a reward model on preference comparisons and then optimising the policy (typically with PPO) to maximise that reward. Huyen contrasts it with direct preference optimisation and supervised finetuning as alternative routes to alignment.

## Sources

- [[sources/berryman-2024-prompt-engineering-llms|Prompt Engineering for LLMs]]
- [[sources/caelen-2023-developing-apps-gpt4|Developing Apps with GPT-4 and ChatGPT]]
- [[sources/huyen-2025-ai-engineering|AI Engineering]]
- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025): Ch 10 contrasts RLHF (reward model plus PPO) with [[concepts/direct-preference-optimization|DPO]] and implements DPO.

<!-- AUTHORED REGION END -->