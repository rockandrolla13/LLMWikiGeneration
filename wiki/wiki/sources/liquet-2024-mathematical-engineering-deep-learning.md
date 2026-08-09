---
title: Mathematical Engineering of Deep Learning
page_id: sources/liquet-2024-mathematical-engineering-deep-learning
page_type: source
verification:
  status: unverified
  unverified_claims: 0
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_4_2026_06_19
tags:
- deep-learning
- mathematical-foundations
- neural-networks
- transformers
- optimization
- convolutional-neural-networks
- recurrent-neural-networks
- generative-models
- reinforcement-learning
- graph-neural-networks
- textbook
- linear-algebra
- calculus
- probability
- attention-mechanism
- lstm
- gru
- diffusion-models
- gans
- variational-autoencoders
- backpropagation
- adam
- automatic-differentiation
- machine-learning
- crc-press
sources:
- sources/liquet-2024-mathematical-engineering-deep-learning
related: []
mind_map_priority: high
authors:
- Benoit Liquet
- Sarat Moka
- Yoni Nazarathy
year: 2024
source_type: book
schema_version: 2
uuid: f226ed5b-1f4d-5549-8c09-a653fe54e7a2
content_hash: sha256:e022fe4cf1f64eb4da6dde77fd7ccef0fc8db416eecc87b5a6d67c76d52b0488
---

<!-- AUTHORED REGION START -->
# Mathematical Engineering of Deep Learning

**Authors:** Benoit Liquet, Sarat Moka, Yoni Nazarathy  
**Year:** 2024  
**Type:** book  
**Markdown source:** none retained. This page was written by a 2026-06-19 batch ingest that recorded `markdown_output/liquet-2024-mathematical-engineering-deep-learning.md`, which was never produced. Claims here are not machine-checkable until the document is converted.
## Summary

Mathematical Engineering of Deep Learning (Chapman & Hall/CRC, 2025; preface dated February 2024) by Benoit Liquet, Sarat Moka, and Yoni Nazarathy is an 8-chapter graduate-level textbook that presents deep learning entirely through mathematical notation — equations and algorithms — without tying coverage to any programming language, computational framework, neuroscience analogy, or historical narrative. The book is self-contained for readers who already have undergraduate-level exposure to calculus, probability, and linear algebra (roughly equivalent to three or four university courses). It progresses from machine learning principles and optimization through feedforward networks, CNNs, sequence models/transformers, and a final survey chapter on generative models, reinforcement learning, and graph neural networks. Two appendices provide mathematical support on multivariable calculus and information-theoretic expectations.

## Key Claims

- Deep learning is fully describable through mathematics at a level accessible to professionals from engineering, statistics, physics, econometrics, operations research, and pure mathematics, without requiring computer programming.
- The book deliberately avoids historical progression, neuroscientific analogies, and programming frameworks in order to let mathematically equipped readers quickly grasp the essentials.
- Readers need prior exposure to mathematical notation equivalent to at least three or four university courses (set notation, matrices, basic probability, calculus); no prior ML, statistics, optimization, or advanced probability is assumed.
- Gradient descent and its variants (including ADAM) are the universal training mechanism explored throughout, with automatic differentiation presented as a critical tool for gradient computation.
- Transformer models are positioned as the current state-of-the-art for large language models, arrived at via the progression: RNN -> LSTM/GRU -> encoder-decoder with attention -> transformer.
- Diffusion models are framed as a special case of Markovian hierarchical variational autoencoders, situating them within a principled probabilistic generative modeling framework.
- A companion website (deeplearningmath.org) provides supplementary examples and software usage details, keeping the book itself implementation-agnostic.

## Main Concepts

- Supervised and unsupervised learning principles
- Linear models and iterative optimization-based learning
- Gradient descent and first-order optimization methods
- ADAM adaptive optimization algorithm
- Automatic differentiation
- Second-order optimization methods
- Logistic regression as a shallow neural network
- Softmax / multinomial regression for multi-class classification
- Cross-entropy loss
- Autoencoders (shallow and variational)
- Backpropagation algorithm
- Weight initialization
- Batch normalization
- Dropout and regularization
- Fully connected / feedforward deep neural networks (MLP)
- Expressive power / universal approximation
- Activation functions
- Convolution operation
- Convolutional neural networks (CNNs)
- Inception, ResNets, and landmark CNN architectures
- Object localization and face identification
- Recurrent neural networks (RNNs)
- Long short-term memory (LSTM)
- Gated recurrent units (GRU)
- Encoder-decoder architectures
- Attention mechanism
- Transformer architecture
- Generative modeling principles
- Variational autoencoders (VAE)
- Diffusion models (as hierarchical VAEs)
- Generative adversarial networks (GANs)
- Reinforcement learning and Markov decision processes
- [[concepts/graph-neural-networks|Graph neural networks]]
- K-means clustering
- Principal component analysis (PCA)
- Singular value decomposition (SVD)
- Multivariable calculus (gradients, chain rule, Taylor's theorem)
- Cross-entropy, KL divergence, and information-theoretic expectations
- Multivariate normal distribution computations

## Key Entities

- Benoit Liquet (author)
- Sarat Moka (author)
- Yoni Nazarathy (author)
- Chapman & Hall / CRC Press (publisher)
- Taylor & Francis Group (parent publisher)
- AMSI (Australian Mathematical Sciences Institute) — origin of the 2021 summer school course
- deeplearningmath.org (companion website)
- ImageNet (dataset mentioned as key example)
- MNIST digits (dataset mentioned as key example)

## Questions Raised

- How does the treatment of transformers compare in depth and notation to dedicated transformer textbooks such as Phuong & Hutter (2022)?
- The book claims diffusion models are a special case of Markovian hierarchical VAEs — does the mathematical derivation include the score-matching or DDPM formulation, or only the hierarchical ELBO perspective?
- Given the book is programming-agnostic, how much of the optimization and backpropagation treatment is directly applicable to understanding framework internals (e.g., PyTorch autograd)?
- Does the reinforcement learning chapter cover deep Q-networks or policy gradient methods (e.g., PPO), or only the Markov decision process foundations?
- The preface says no advanced probability is needed — how is the variational autoencoder's ELBO derivation handled without measure theory or variational inference prerequisites?
- Are graph neural networks treated only for node classification, or do edge prediction and graph-level tasks also appear?

<!-- AUTHORED REGION END -->
