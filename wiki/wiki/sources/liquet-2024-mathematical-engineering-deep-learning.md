---
title: Mathematical Engineering of Deep Learning
page_id: sources/liquet-2024-mathematical-engineering-deep-learning
page_type: source
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
**Markdown source:** `markdown_output/liquet-2024-mathematical-engineering-deep-learning.md`

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

- [[concepts/supervised-and-unsupervised-learning-principles|Supervised and unsupervised learning principles]]
- [[concepts/linear-models-and-iterative-optimization-based-learning|Linear models and iterative optimization-based learning]]
- [[concepts/gradient-descent-and-first-order-optimization-methods|Gradient descent and first-order optimization methods]]
- [[concepts/adam-adaptive-optimization-algorithm|ADAM adaptive optimization algorithm]]
- [[concepts/automatic-differentiation|Automatic differentiation]]
- [[concepts/second-order-optimization-methods|Second-order optimization methods]]
- [[concepts/logistic-regression-as-a-shallow-neural-network|Logistic regression as a shallow neural network]]
- [[concepts/softmax-multinomial-regression-for-multi-class-classification|Softmax / multinomial regression for multi-class classification]]
- [[concepts/cross-entropy-loss|Cross-entropy loss]]
- [[concepts/autoencoders-shallow-and-variational-|Autoencoders (shallow and variational)]]
- [[concepts/backpropagation-algorithm|Backpropagation algorithm]]
- [[concepts/weight-initialization|Weight initialization]]
- [[concepts/batch-normalization|Batch normalization]]
- [[concepts/dropout-and-regularization|Dropout and regularization]]
- [[concepts/fully-connected-feedforward-deep-neural-networks-mlp-|Fully connected / feedforward deep neural networks (MLP)]]
- [[concepts/expressive-power-universal-approximation|Expressive power / universal approximation]]
- [[concepts/activation-functions|Activation functions]]
- [[concepts/convolution-operation|Convolution operation]]
- [[concepts/convolutional-neural-networks-cnns-|Convolutional neural networks (CNNs)]]
- [[concepts/inception-resnets-and-landmark-cnn-architectures|Inception, ResNets, and landmark CNN architectures]]
- [[concepts/object-localization-and-face-identification|Object localization and face identification]]
- [[concepts/recurrent-neural-networks-rnns-|Recurrent neural networks (RNNs)]]
- [[concepts/long-short-term-memory-lstm-|Long short-term memory (LSTM)]]
- [[concepts/gated-recurrent-units-gru-|Gated recurrent units (GRU)]]
- [[concepts/encoder-decoder-architectures|Encoder-decoder architectures]]
- [[concepts/attention-mechanism|Attention mechanism]]
- [[concepts/transformer-architecture|Transformer architecture]]
- [[concepts/generative-modeling-principles|Generative modeling principles]]
- [[concepts/variational-autoencoders-vae-|Variational autoencoders (VAE)]]
- [[concepts/diffusion-models-as-hierarchical-vaes-|Diffusion models (as hierarchical VAEs)]]
- [[concepts/generative-adversarial-networks-gans-|Generative adversarial networks (GANs)]]
- [[concepts/reinforcement-learning-and-markov-decision-processes|Reinforcement learning and Markov decision processes]]
- [[concepts/graph-neural-networks|Graph neural networks]]
- [[concepts/k-means-clustering|K-means clustering]]
- [[concepts/principal-component-analysis-pca-|Principal component analysis (PCA)]]
- [[concepts/singular-value-decomposition-svd-|Singular value decomposition (SVD)]]
- [[concepts/multivariable-calculus-gradients-chain-rule-taylor-s-theorem-|Multivariable calculus (gradients, chain rule, Taylor's theorem)]]
- [[concepts/cross-entropy-kl-divergence-and-information-theoretic-expectations|Cross-entropy, KL divergence, and information-theoretic expectations]]
- [[concepts/multivariate-normal-distribution-computations|Multivariate normal distribution computations]]

## Key Entities

- [[entities/benoit-liquet-author-|Benoit Liquet (author)]]
- [[entities/sarat-moka-author-|Sarat Moka (author)]]
- [[entities/yoni-nazarathy-author-|Yoni Nazarathy (author)]]
- [[entities/chapman-hall-crc-press-publisher-|Chapman & Hall / CRC Press (publisher)]]
- [[entities/taylor-francis-group-parent-publisher-|Taylor & Francis Group (parent publisher)]]
- [[entities/amsi-australian-mathematical-sciences-institute-origin-of-the-2021-summer-school-course|AMSI (Australian Mathematical Sciences Institute) — origin of the 2021 summer school course]]
- [[entities/deeplearningmath-org-companion-website-|deeplearningmath.org (companion website)]]
- [[entities/imagenet-dataset-mentioned-as-key-example-|ImageNet (dataset mentioned as key example)]]
- [[entities/mnist-digits-dataset-mentioned-as-key-example-|MNIST digits (dataset mentioned as key example)]]

## Questions Raised

- How does the treatment of transformers compare in depth and notation to dedicated transformer textbooks such as Phuong & Hutter (2022)?
- The book claims diffusion models are a special case of Markovian hierarchical VAEs — does the mathematical derivation include the score-matching or DDPM formulation, or only the hierarchical ELBO perspective?
- Given the book is programming-agnostic, how much of the optimization and backpropagation treatment is directly applicable to understanding framework internals (e.g., PyTorch autograd)?
- Does the reinforcement learning chapter cover deep Q-networks or policy gradient methods (e.g., PPO), or only the Markov decision process foundations?
- The preface says no advanced probability is needed — how is the variational autoencoder's ELBO derivation handled without measure theory or variational inference prerequisites?
- Are graph neural networks treated only for node classification, or do edge prediction and graph-level tasks also appear?

<!-- AUTHORED REGION END -->
