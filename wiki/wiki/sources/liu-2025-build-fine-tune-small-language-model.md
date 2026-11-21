---
authors:
- J. Paul Liu
content_hash: sha256:e7fb73814e3f6d396ff73a32289cd0bd2db7274dd3d669275e10cce6e9c1c1c1
created: '2026-11-21T02:00:24Z'
edition: Leanpub version published 2025-11-24
is_early_release: false
isbn: 979-8-2747-6622-7 (paperback)
mind_map_priority: medium
page_id: sources/liu-2025-build-fine-tune-small-language-model
page_type: source
publisher: Leanpub
related:
- concepts/small-language-models
- concepts/direct-preference-optimization
- concepts/perplexity
- concepts/rotary-position-embeddings
- concepts/grouped-query-attention
- concepts/rmsnorm
- concepts/swiglu
- concepts/learning-rate-warmup-cosine-decay
- concepts/tokenization
- concepts/byte-pair-encoding
- concepts/fine-tuning
- concepts/instruction-fine-tuning
- concepts/transfer-learning
- concepts/language-model-pretraining
- concepts/self-attention
- concepts/causal-attention
- concepts/multi-head-attention
- concepts/layer-normalization
- concepts/positional-embeddings
- concepts/transformers
- concepts/llm-sampling-controls
- concepts/llm-evaluation
- concepts/dataset-engineering
- concepts/rlhf
- concepts/low-rank-adaptation
- concepts/model-compression
- concepts/inference-optimization
- concepts/large-language-models
- sources/thomas-2025-hands-on-small-language-models
- sources/raschka-2024-build-llm-from-scratch
- sources/dandekar-2025-build-deepseek-model
- sources/attention-paper
- sources/alammar-2024-hands-on-llm
- sources/huyen-2025-ai-engineering
- sources/bouchard-2024-building-llms-production
- entities/j-paul-liu
- entities/leanpub
- entities/jingyao-gong
- entities/minimind
- entities/andrej-karpathy
- entities/gpt-2
- entities/openwebtext
- entities/stanford-alpaca
- entities/anthropic-hh-rlhf
- entities/ultrafeedback
- entities/llama-cpp
- entities/ollama
- entities/vllm
- entities/google-colab
- entities/openai
- entities/hugging-face
- entities/huggingface-transformers
- entities/pytorch
- entities/weights-and-biases
- entities/anthropic
- entities/databricks
- contradictions/int8-quantization-speedup-small-models
revision_id: 1
schema_version: 2
source_hash: sha256:a08615c81430d0c61368ad332f28be15c4ca6f3b3488205fe931a645fe6e6903
source_path: markdown_output/liu-2025-build-fine-tune-small-language-model.md
source_type: book
sources: []
tags:
- small-language-models
- llm-training
- pretraining
- fine-tuning
- direct-preference-optimization
- llm-deployment
- beginner-guide
title: 'How to Build and Fine-Tune a Small Language Model: A Step-by-Step Guide for
  Beginners, Researchers, and Non-Programmers'
updated: '2026-11-21T02:00:24Z'
updated_by: op_faa1492c417c
uuid: c5d076dd-265e-5322-9942-66ca5f8ab202
year: 2025
---

<!-- AUTHORED REGION START -->
# How to Build and Fine-Tune a Small Language Model: A Step-by-Step Guide for Beginners, Researchers, and Non-Programmers

**Author:** [[entities/j-paul-liu|J. Paul Liu]]

**Year:** 2025

**Publisher:** [[entities/leanpub|Leanpub]] (self-published)

**Edition:** Leanpub version published 2025-11-24. Paperback ISBN 979-8-2747-6622-7. 479 pages.

**Source PDF:** `raw/small-language-models/liu-2025-build-fine-tune-small-language-model.pdf` (main checkout, gitignored)

## Summary

This is a hands-on guide to building, training, aligning and deploying small language models (SLMs). Every chapter ships as a Google Colab notebook. Liu defines SLMs as models of roughly 125 million to 7 billion parameters. He argues they beat giant LLMs for narrow, private, high-volume or budget-limited tasks. Giant LLMs stay better for broad knowledge, complex reasoning and current information. The front matter adds that an SLM alone cannot replace a large LLM, and that practitioners often combine both.

The book has four parts. Part I (Ch 1-3) makes the case for SLMs. It then rebuilds a character-level GPT on Tiny Shakespeare after [[entities/andrej-karpathy|Andrej Karpathy]]'s "Let's build GPT" lecture, and fine-tunes Hugging Face [[entities/gpt-2|GPT-2]] (124M) on a toy recipe dataset. Part II (Ch 4-7) covers data preparation and tokenization, sizing a GPT-2-like model, a production training loop and evaluation.

Part III (Ch 8-10) is a case study. Liu adapts [[entities/jingyao-gong|Jingyao Gong]]'s Chinese [[entities/minimind|MiniMind]] project to English in three stages. Stage 1 pretrains a decoder-only model with RoPE, grouped-query attention, RMSNorm and SwiGLU on a subset of [[entities/openwebtext|OpenWebText]]. Stage 2 runs full supervised fine-tuning on [[entities/stanford-alpaca|Stanford Alpaca]]. Stage 3 aligns the model with Direct Preference Optimization against a frozen SFT reference.

Part IV (Ch 11-12) covers deployment and three worked production projects, with a closing section on ethics and safety. Appendices give a GPU cost calculator, hyperparameter cheat sheets and a dataset and model list. The book is practical and introductory. Several numbers disagree between chapters, and one scaling-law formula is inverted (see below).

## Chapter Summaries

- **Ch 1, Introduction.** Weighs giant LLMs against SLMs on cost, privacy, control, availability and latency. Introduces the two architectures used later: GPT-2 (Ch 3-7) and MiniMind (Ch 8-10). Lists hardware options from free Colab to rented A100s and local RTX cards.
- **Ch 2, Let's Build GPT from Scratch.** Rebuilds Karpathy's character-level GPT on Tiny Shakespeare (65-character vocabulary). Moves from a bigram baseline through masked self-attention, multi-head attention, pre-LayerNorm blocks and learned position embeddings to a full small GPT trained with AdamW.
- **Ch 3, Quick Start.** Fully fine-tunes pretrained GPT-2 on 20 recipe sentences repeated to 200 examples, for 3 epochs, with the Hugging Face Trainer. Explains transfer learning, why the fine-tuning learning rate is low (to avoid catastrophic forgetting), and sampling temperature.
- **Ch 4, Dataset Preparation.** Compares character, word and BPE tokenization and trains a custom BPE tokenizer. Surveys data sources and covers cleaning, exact and near-duplicate removal (including MinHash LSH), output formats and quality checks. Gives a rule of thumb of 10MB of text for a 125M model, 100MB for 350M and 1GB for 1B.
- **Ch 5, Model Architecture and Configuration.** Breaks down GPT-2 Small's parameter count and the rule that each layer holds about 12 × n_embd² parameters. Discusses hidden size, depth, head count and context length, with preset configurations from 50M to 1B. Its scaling-law code is wrong (see Errors).
- **Ch 6, Training Loop and Monitoring.** Adds gradient accumulation, linear warmup plus cosine decay, gradient-norm clipping at 1.0, AdamW weight decay that skips biases and norms, logging and checkpointing. Trains a 77.2M GPT on 10,000 Wikipedia articles on an A100.
- **Ch 7, Evaluation and Benchmarks.** Scores the Ch 6 model on perplexity, token and sequence accuracy and a two-bucket confidence analysis. Compares it with random, most-frequent-token and 3-gram baselines and checks repetition and diversity. The model reaches perplexity 111.05 and token accuracy 27.27%, against 12.34% for the 3-gram baseline, and fails the sample readiness gate.
- **Ch 8, Stage 1: Pretraining MiniMind.** Swaps MiniMind's 6,400-token Chinese vocabulary for a 32,000-token ByteLevel BPE trained on OpenWebText, which reaches 5.64 characters per token. Builds about 548M training tokens and a 109,051,904-parameter model with weight tying. The untrained model's loss of 10.37 matches −log(1/32000). Training runs about 100K steps, with SLURM scripts for HPC, and ends at validation perplexity 17.37.
- **Ch 9, Stage 2: Supervised Fine-Tuning.** Formats Alpaca (52,002 examples) and optionally Databricks Dolly into a plain instruction template. Fully fine-tunes the Stage 1 model, computing the loss only on response tokens. Estimates 4-6 A100 hours.
- **Ch 10, Stage 3: Direct Preference Optimization.** Contrasts RLHF (reward model plus PPO) with DPO. Builds preference pairs from [[entities/anthropic-hh-rlhf|Anthropic HH-RLHF]] and [[entities/ultrafeedback|UltraFeedback]] and implements the DPO loss with β = 0.1 by default. Tracks reward margins and preference accuracy.
- **Ch 11, Production Deployment.** Surveys quantization, pruning and distillation, then applies PyTorch dynamic INT8 quantization to the MiniMind model and benchmarks it. Covers GGUF conversion for [[entities/llama-cpp|llama.cpp]], [[entities/ollama|Ollama]], a FastAPI server, [[entities/vllm|vLLM]], ONNX and edge deployment, with a serving cost comparison and break-even analysis.
- **Ch 12, Production Projects and Ethics.** Three end-to-end projects: a medical Q&A assistant that must refuse to diagnose, a code documentation generator and a multilingual support assistant that escalates to humans. Closes with bias, moderation, privacy and a deployment checklist.
- **Appendices.** GPU-hour and cost estimates across cloud providers, memory by precision, model-size tables, hyperparameter cheat sheets for pretraining, SFT, DPO and LoRA (rank 8-16, alpha usually 2 × r), and lists of datasets, small models and frameworks.

## Key Contributions

- One continuous notebook path from a character-level GPT to a three-stage English small model (pretrain, then SFT, then DPO). It targets non-programmers and domain researchers.
- An English adaptation of MiniMind: a 32K ByteLevel BPE tokenizer, OpenWebText pretraining, Alpaca SFT and HH-RLHF/UltraFeedback DPO, with multi-GPU SLURM scripts.
- Per-stage cost and time estimates for cloud A100s and a local RTX 4090. The book puts the whole pipeline at $24-48 on an A100.
- A worked evaluation suite for a small model: perplexity, token and sequence accuracy, confidence buckets, n-gram baselines, repetition and diversity scores and a readiness gate.
- A deployment chapter that runs its own INT8 benchmark and reports a slowdown, next to GGUF, Ollama, FastAPI and vLLM options.

## Errors and Unsupported Claims

- **Inverted Chinchilla rule (Ch 5).** The scaling-law code says "From Hoffmann et al. (2022): N_opt ≈ 20 × D", with N as parameters and D as training tokens. Its printed output follows that rule: 125M parameters map to 6M "optimal" training tokens, and 1B tokens map to 20B parameters. Hoffmann et al. give roughly the reverse, about 20 training tokens per parameter. That correction is paper-level knowledge, not from this book, so check it against the Chinchilla paper before citing it. Do not reuse the book's printed numbers.
- **Data budget (Ch 4).** The 10MB-per-125M-parameter rule is far below a 20-tokens-per-parameter budget, which would need billions of tokens for 125M parameters.
- **INT8 speed (Ch 11).** The overview table claims INT8 quantization gives a 2-3× speedup with under 1% quality loss. The book's own benchmark measures the reverse: FP32 57.7 tokens/s, the DPO model 54.7 and the INT8 model 30.2 (0.52× speed), with visibly worse INT8 output on some prompts. The text does not say which device ran the benchmark. See [[contradictions/int8-quantization-speedup-small-models|the contradiction page]].
- **Unbacked claims.** Ch 1 says a 350M model tuned on medical literature can beat GPT-4 on drug-interaction questions while running on a laptop. Ch 4 says a 350M model on excellent data will beat a 1B model on bad data. Neither claim has a citation or an experiment.
- **Illustrative tables.** The Ch 10 table of instruction following, helpfulness and refusal rate for pretrained, SFT and DPO models gives no evaluation protocol. Treat its figures as illustrative.
- **Perplexity comparison (Ch 8).** The claim that the model is "comparable to early GPT-2" compares perplexity 17.37 under a 32K lowercased tokenizer with GPT-2's figure under its own 50,257-token tokenizer. Perplexities under different tokenizers are not directly comparable.
- **Confidence analysis (Ch 7).** The book reads a two-bucket split (accuracy above versus below 80% predicted probability) as the model "knowing what it knows". A two-bucket split is weak evidence of [[concepts/calibration|calibration]].

## Internal Inconsistencies

- The Ch 2 model is called about 10M parameters, but its listed settings (n_embd 64, 4 layers, 4 heads, block size 32) imply far fewer. Ch 5 says Ch 2 used a context of 256.
- Ch 2 code uses learning rate 1e-3, while Ch 3 and Ch 6 say Ch 2 used 3e-4.
- Ch 5 and Ch 7 promise LoRA or QLoRA in Ch 8 or 9. Ch 8-9 instead cover MiniMind pretraining and full SFT. LoRA appears only in the Appendix B tables.
- MiniMind configurations disagree across Ch 5, Ch 8 and Appendix B (layer counts for the 26M and 109M variants, and the vocabulary size).
- Appendix B says MiniMind uses learned position encoding and GELU. Ch 8 says it uses RoPE and SwiGLU with no learned position embeddings.
- Ch 8 prints 109,051,904 parameters for the Stage 1 model. Ch 9 says the Ch 8 model has 128.41M parameters.
- Ch 8 pretrains on about 548M OpenWebText tokens over 2-3 days. Later chapters describe pretraining as 1B tokens, raw Wikipedia, or 16-24 A100 hours.

## Questions Raised

- How would the MiniMind-style 109M model score under a Chinchilla-sized token budget rather than about 548M tokens?
- Does the INT8 slowdown come from dynamic quantization on the benchmark device, and would static or 4-bit GGUF quantization reverse it?
- How much does the DPO stage change behaviour when measured with a stated protocol rather than the illustrative Ch 10 table?
- Would LoRA or QLoRA, promised but not delivered, match full SFT for a model this small?

## Intended Audience

Beginners, domain researchers and non-programmers who want to train and deploy their own small model from Colab notebooks. Readers who already know PyTorch will find the implementation material shallower than [[sources/raschka-2024-build-llm-from-scratch|Raschka's book]].

## Key Concepts in This Source

- [[concepts/small-language-models|Small Language Models]]
- [[concepts/direct-preference-optimization|Direct Preference Optimization]]
- [[concepts/perplexity|Perplexity]]
- [[concepts/rotary-position-embeddings|Rotary Position Embeddings (RoPE)]]
- [[concepts/grouped-query-attention|Grouped-Query Attention]]
- [[concepts/rmsnorm|RMSNorm]]
- [[concepts/swiglu|SwiGLU]]
- [[concepts/learning-rate-warmup-cosine-decay|Learning-Rate Warmup and Cosine Decay]]
- [[concepts/tokenization|Tokenization]]
- [[concepts/byte-pair-encoding|Byte Pair Encoding]]
- [[concepts/fine-tuning|Fine-Tuning]]
- [[concepts/instruction-fine-tuning|Instruction Fine-Tuning]]
- [[concepts/transfer-learning|Transfer Learning]]
- [[concepts/language-model-pretraining|Language Model Pretraining]]
- [[concepts/self-attention|Self-Attention]]
- [[concepts/causal-attention|Causal Attention]]
- [[concepts/multi-head-attention|Multi-Head Attention]]
- [[concepts/layer-normalization|Layer Normalization]]
- [[concepts/positional-embeddings|Positional Embeddings]]
- [[concepts/transformers|Transformers]]
- [[concepts/llm-sampling-controls|LLM Sampling Controls]]
- [[concepts/llm-evaluation|LLM Evaluation]]
- [[concepts/dataset-engineering|Dataset Engineering]]
- [[concepts/rlhf|Reinforcement Learning from Human Feedback]]
- [[concepts/low-rank-adaptation|Low-Rank Adaptation]]
- [[concepts/model-compression|Model Compression]]
- [[concepts/inference-optimization|Inference Optimization]]
- [[concepts/large-language-models|Large Language Models]]

## Entities

- [[entities/j-paul-liu|J. Paul Liu]]
- [[entities/leanpub|Leanpub]]
- [[entities/jingyao-gong|Jingyao Gong]]
- [[entities/minimind|MiniMind]]
- [[entities/andrej-karpathy|Andrej Karpathy]]
- [[entities/gpt-2|GPT-2]]
- [[entities/openwebtext|OpenWebText]]
- [[entities/stanford-alpaca|Stanford Alpaca]]
- [[entities/anthropic-hh-rlhf|Anthropic HH-RLHF]]
- [[entities/ultrafeedback|UltraFeedback]]
- [[entities/llama-cpp|llama.cpp]]
- [[entities/ollama|Ollama]]
- [[entities/vllm|vLLM]]
- [[entities/google-colab|Google Colab]]
- [[entities/openai|OpenAI]]
- [[entities/hugging-face|Hugging Face]]
- [[entities/huggingface-transformers|Hugging Face Transformers]]
- [[entities/pytorch|PyTorch]]
- [[entities/weights-and-biases|Weights and Biases]]
- [[entities/anthropic|Anthropic]]
- [[entities/databricks|Databricks]]

## Related Sources

- [[sources/thomas-2025-hands-on-small-language-models|Hands-on Small Language Models]]: a different SLM book by Alexander Thomas. It builds agentic apps on existing SLMs, while Liu trains SLMs. The overlap is the SLM framing and Ollama for local serving.
- [[sources/raschka-2024-build-llm-from-scratch|Build a Large Language Model (From Scratch)]]: the closest overlap. Both build a GPT from scratch, load GPT-2 weights and fine-tune. Raschka goes deeper on implementation. Liu adds the MiniMind pretrain-SFT-DPO case study and deployment.
- [[sources/dandekar-2025-build-deepseek-model|Build a DeepSeek Model From Scratch]]: another build-from-scratch book on modern decoder models.
- [[sources/attention-paper|Attention Is All You Need]]: cited in Ch 1, 2 and 12.
- [[sources/alammar-2024-hands-on-llm|Hands-On Large Language Models]]: Liu cites Alammar's "Illustrated Transformer" blog. Overlap on tokenization, attention and fine-tuning.
- [[sources/huyen-2025-ai-engineering|AI Engineering]]: higher-level treatment of fine-tuning, evaluation and inference optimization.
- [[sources/bouchard-2024-building-llms-production|Building LLMs for Production]]: overlap on deploying LLMs.

## Notes on the Source Text

The converted markdown flattens code listings into prose and splits some tables. Read exact code, formulas and table figures from the PDF. The figures on this page were checked against the PDF text. The front matter states that ChatGPT, Claude, Gemini and DeepSeek helped with writing and debugging, and that the code was tested in November 2025.
<!-- AUTHORED REGION END -->