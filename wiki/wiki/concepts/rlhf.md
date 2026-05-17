---
title: Reinforcement Learning from Human Feedback
page_id: concepts/rlhf
page_type: concept
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
tags:
- ai-engineering
sources:
- sources/berryman-2024-prompt-engineering-llms
- sources/caelen-2023-developing-apps-gpt4
- sources/huyen-2025-ai-engineering
related: []
mind_map_priority: high
revision_hash: sha256:eb85048e33430b72
---

# Reinforcement Learning from Human Feedback

## Definition

A post-training technique that aligns a model with human preferences by training a reward model on preference comparisons and then optimising the policy (typically with PPO) to maximise that reward. Huyen contrasts it with direct preference optimisation and supervised finetuning as alternative routes to alignment.

## Sources

- [[sources/berryman-2024-prompt-engineering-llms|Prompt Engineering for LLMs]]
- [[sources/caelen-2023-developing-apps-gpt4|Developing Apps with GPT-4 and ChatGPT]]
- [[sources/huyen-2025-ai-engineering|AI Engineering]]
