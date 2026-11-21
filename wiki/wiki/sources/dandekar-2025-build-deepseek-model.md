---
authors:
- Raj Abhijit Dandekar
- Rajat Dandekar
content_hash: sha256:4fc62abd53f623891d93a289844209796df963a391cd47ab2ca360feb354db36
created: 2026-06-19 00:00:00+00:00
mind_map_priority: high
page_id: sources/dandekar-2025-build-deepseek-model
page_type: source
related:
- sources/liu-2025-build-fine-tune-small-language-model
revision_id: 2
schema_version: 2
source_type: book
sources:
- sources/dandekar-2025-build-deepseek-model
tags:
- llm
- deepseek
- transformers
- mixture-of-experts
- attention-mechanisms
- reinforcement-learning
- quantization
title: Build a DeepSeek Model From Scratch
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: 5140ce07-e5ef-5b60-938f-98c48d6056fb
verification:
  status: unverified
  unverified_claims: 2
year: 2025
---

<!-- AUTHORED REGION START -->
# Build a DeepSeek Model From Scratch

**Authors:** Raj Abhijit Dandekar, Rajat Dandekar  
**Year:** 2025  
**Type:** book  
**Markdown source:** none retained. This page was written by a 2026-06-19 batch ingest that recorded `markdown_output/dandekar-2025-build-deepseek-model.md`, which was never produced. Claims here are not machine-checkable until the document is converted.
## Summary

Build a DeepSeek Model From Scratch (MEAP edition, 2025) by Raj Abhijit Dandekar, Rajat Dandekar, Sreedath Panat, and Naman Dwivedi is a hands-on technical guide that teaches readers how to implement the core innovations of the DeepSeek-R1 large language model from first principles using Python and PyTorch. The book is structured as a four-stage roadmap covering: (1) Key-Value Cache as an inference foundation, (2) core architectural components Multi-Head Latent Attention (MLA) and Mixture-of-Experts (MoE), (3) advanced training techniques including Multi-Token Prediction (MTP) and FP8 quantization, and (4) post-training methods including reinforcement learning and knowledge distillation. Implementations are designed to run on consumer hardware using scaled-down model versions. The book grew out of Vizuara's YouTube series "Build DeepSeek from Scratch" launched in February 2025.

## Key Claims

- DeepSeek-R1 represents the moment when open-source AI first rivaled top proprietary models (OpenAI o1-1217) on demanding benchmarks including AIME 2024 math and Codeforces coding at a fraction of the training cost.
- The two core architectural innovations replacing standard Transformer components are Multi-Head Latent Attention (MLA, replacing multi-head self-attention) and DeepSeek-MoE (replacing the feed-forward network).
- MLA addresses speed and memory bottlenecks in attention for long sequences; MoE addresses model scaling and capacity; MTP improves learning and inference speed; FP8 quantization addresses computational efficiency.
- DeepSeek-R1 was derived from the DeepSeek-V3 base (671B parameters) through a five-step post-training pipeline: cold-start fine-tuning, pure RL, rejection sampling self-labeling, data blending, and final RL.
- Knowledge distillation was used to compress DeepSeek-R1 into models as small as 1.5B parameters; open-sourced checkpoints based on Qwen2.5 and Llama3 were released at 1.5B, 7B, 8B, 14B, 32B, and 70B scales.
- An internal training scheduling strategy called DualPipe overlaps forward and backward passes to maximize GPU utilization during large-scale training.
- The book's implementations are designed to run on consumer hardware without requiring a supercomputer, using scaled-down versions of the model components.

## Main Concepts

- Key-Value (KV) Cache for efficient inference
- Multi-Head Latent Attention (MLA)
- Mixture-of-Experts (MoE)
- Multi-Token Prediction (MTP)
- FP8 quantization (8-bit floating-point)
- Reinforcement Learning for post-training (Pure RL, rejection sampling)
- Knowledge Distillation

## Key Entities

- DeepSeek (AI lab, China, founded 2023, led by Liang Wenfeng)
- Vizuara (YouTube channel / educational brand of the authors)
- OpenAI (GPT series, o1-1217 model, used as performance benchmark)
- Meta (LLaMA and LLaMA-2, referenced as open-source context)
- Qwen2.5 and Llama3 (base models used for distilled checkpoints)

## Questions Raised

- Can the four-stage build-from-scratch approach faithfully reproduce the efficiency gains of MLA and MoE at scaled-down consumer-hardware sizes, or do the gains only emerge at production scale?
- How does DeepSeek's Pure RL post-training step (which develops reasoning without explicit human guidance) compare mechanistically to RLHF used by OpenAI, and what are the trade-offs?
- Given that distilled models as small as 1.5B parameters are described as 'highly performant,' what is the minimum scale at which the MLA and MoE architectural innovations provide meaningful benefits over standard Transformer components?


## Related Sources

- [[sources/liu-2025-build-fine-tune-small-language-model|How to Build and Fine-Tune a Small Language Model]] (2025)
<!-- AUTHORED REGION END -->