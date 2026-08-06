---
title: Math and Architectures of Deep Learning
page_id: sources/chaudhury-2024-math-architectures-deep-learning
page_type: source
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_4_2026_06_19
tags:
- deep-learning
- mathematics
- linear-algebra
- probability
- bayesian-inference
- neural-networks
- cnn
- optimization
- pytorch
- textbook
- manning
- svd
- pca
- backpropagation
- object-detection
- generative-models
- vae
- manifolds
- 2024
sources:
- sources/chaudhury-2024-math-architectures-deep-learning
related: []
mind_map_priority: high
authors:
- Krishnendu Chaudhury
year: 2024
source_type: book
schema_version: 2
uuid: 69aa4279-675f-5a85-a9ef-d424035d2590
content_hash: sha256:3a1a7c4dbe28a79d43a7b1fc54f4bbc0141eab24e6870e16935afa389da6df8f
---

<!-- AUTHORED REGION START -->
# Math and Architectures of Deep Learning

**Authors:** Krishnendu Chaudhury  
**Year:** 2024  
**Type:** book  
**Markdown source:** `markdown_output/chaudhury-2024-math-architectures-deep-learning.md`

## Summary

Math and Architectures of Deep Learning (2024, Manning Publications) by Krishnendu Chaudhury, with co-authors Ananya H. Ashok, Sujay Narumanchi, and Devashish Shankar, is a 14-chapter textbook that bridges rigorous mathematical foundations with practical deep learning implementation in PyTorch. It progresses from first-principles linear algebra, calculus, and probability through neural network training, CNNs, generative models, and Bayesian inference, with extensive PyTorch code woven into each chapter. The foreword is by Prith Banerjee. ISBN 9781617296482.

## Key Claims

- The book treats machine learning as a function approximation problem from the outset (Chapter 1)
- Every mathematical topic is grounded in PyTorch code examples, making it implementation-oriented as well as theory-heavy
- Cybenko's universal approximation theorem is covered in Chapter 7 (MLPs)
- SVD is presented as a unifying tool for PCA, document retrieval (LSA), and solving linear systems (Chapter 4)
- Bayesian tools are split across two chapters: frequentist-to-Bayesian bridge in Chapter 6 (MLE, MAP, GMMs, KL divergence) and a dedicated fully-Bayes chapter in Chapter 13 (conjugate priors, Normal-gamma distribution)
- Manifold theory and homeomorphism are introduced in Chapter 12 to provide a topological perspective on what neural networks learn
- Convolutions are treated algebraically as matrix multiplication in 1D, 2D, and 3D (Chapter 10)
- Object detection coverage includes R-CNN, Fast R-CNN, and Faster R-CNN with a deep dive into the region proposal network (Chapter 11)
- Regularization is framed via Occam's razor / minimum description length as well as Bayes' theorem (Chapter 9)
- Transposed convolution is covered with application to autoencoders and embeddings (Chapter 10)

## Main Concepts

- Linear algebra: vectors, matrices, tensors, eigendecomposition, SVD, PCA, Moore-Penrose pseudo-inverse, matrix diagonalization, spectral decomposition
- Vector calculus: gradient vectors, Hessian matrix, Taylor series (1D and multidimensional), loss surface geometry, convex/nonconvex functions
- Probability and statistics: frequentist probability, joint/marginal/conditional distributions, Gaussian, Binomial, Multinomial, Bernoulli, Categorical distributions
- Bayesian inference: Bayes theorem, entropy, cross-entropy, KL divergence, MLE, MAP, latent variables, Gaussian mixture models, conjugate priors, Normal-gamma distribution, fully Bayes estimation
- Neural network fundamentals: perceptron, MLP, forward propagation, backpropagation, activation functions (sigmoid, tanh, Heaviside)
- Loss functions: regression loss, cross-entropy, binary cross-entropy, softmax cross-entropy, focal loss, hinge loss
- Optimization: gradient descent, SGD with minibatches, momentum, Nesterov accelerated gradients, AdaGrad, RMSProp, Adam
- [[concepts/regularization-l1-l2-dropout-mdl-perspective|Regularization: L1, L2, dropout, MDL perspective]]
- Convolutions: 1D/2D/3D convolution, transposed convolution, pooling
- CNN architectures: LeNet, VGGNet, Inception, ResNet
- Object detection: R-CNN, Fast R-CNN, Faster R-CNN, region proposal network
- Manifold theory: Hausdorff property, second countable property, homeomorphism between manifolds
- Generative modeling: autoencoders, variational autoencoders (Chapter 14)
- Latent space and dimensionality reduction: PCA, LSA, VAE latent space
- Document retrieval: TF-IDF, cosine similarity, latent semantic analysis

## Key Entities

- Krishnendu Chaudhury (primary author)
- Ananya H. Ashok (co-author)
- Sujay Narumanchi (co-author)
- Devashish Shankar (co-author)
- Prith Banerjee (foreword author)
- Manning Publications (publisher)
- PyTorch (primary implementation framework)
- Christina Taylor (development editor)
- Mike Shepard (technical development editor)
- Lucian Mircea Sasu (technical proofreader)

## Questions Raised

- Chapter 14 on latent space, autoencoders, and VAEs is listed in the brief contents but not visible in the detailed TOC within the first 380 lines — full chapter coverage of VAEs is unconfirmed from this reading
- No explicit prerequisite statement is visible in the first 380 lines; the preface/about-this-book section (page xx) may contain this but was not read
- Whether transformers/attention mechanisms or LLMs appear later in the book is unknown from this excerpt
- The audience level (undergraduate, graduate, practitioner) is not explicitly stated in the TOC section; the about-this-book section would clarify this

<!-- AUTHORED REGION END -->
