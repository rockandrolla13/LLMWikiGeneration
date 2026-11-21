---
abstraction_level: advanced
concept_type: technique
content_hash: sha256:d789a8c01d635f32d9865bfb901e6df19aad48ed8819a67b8c89b6f9f778c28e
created: '2026-11-21T02:00:24Z'
page_id: concepts/direct-preference-optimization
page_type: concept
related:
- concepts/rlhf
- concepts/instruction-fine-tuning
- concepts/fine-tuning
revision_id: 1
schema_version: 2
sources:
- sources/liu-2025-build-fine-tune-small-language-model
tags: []
title: Direct Preference Optimization
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 502676e8-42f5-5100-86a0-c85d77a58791
---

<!-- AUTHORED REGION START -->
# Direct Preference Optimization

## Definition

Direct Preference Optimization (DPO) aligns a language model with preferences without a separate reward model or reinforcement learning. It trains on pairs of a chosen and a rejected response to the same prompt. The loss pushes up the policy's log-probability ratio, against a frozen reference model, on the chosen response relative to the rejected one. In Liu's implementation the loss is −log σ(β × (chosen log-ratio − rejected log-ratio)), where each log-ratio compares the policy with the frozen SFT reference.

## In Liu (2025)

DPO is the third stage of the MiniMind pipeline, after pretraining and supervised fine-tuning. The default β is 0.1. Preference pairs come from Anthropic HH-RLHF and UltraFeedback, from GPT-4-generated pairs, from variants sampled from the SFT model, or from human annotation. The trainer tracks reward margins and preference accuracy. The book says DPO gives results similar to RLHF but cites Rafailov et al. (2023) only in its reading list.

[[concepts/rlhf|RLHF]] is the reward-model-plus-PPO route that DPO replaces.

## Sources

- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model: A Step-by-Step Guide for Beginners, Researchers, and Non-Programmers]]

## Related Concepts

- [[concepts/rlhf|Reinforcement Learning from Human Feedback]]
- [[concepts/instruction-fine-tuning|Instruction Fine-Tuning]]
- [[concepts/fine-tuning|Fine-Tuning]]
<!-- AUTHORED REGION END -->