---
title: 'Statistical Rethinking: A Bayesian Course with Examples in R and STAN'
page_id: sources/mcelreath-2020-statistical-rethinking
page_type: source
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_5_2026_06_19
tags:
- bayesian-statistics
- statistical-modeling
- r
- stan
- mcmc
- multilevel-models
- causal-inference
- dag
- glm
- textbook
- rethinking
- mcelreath
- prior-predictive-simulation
- gaussian-process
- ode-models
- regularization
- missing-data
sources:
- sources/mcelreath-2020-statistical-rethinking
related: []
mind_map_priority: high
authors:
- Richard McElreath
year: 2020
source_type: book
schema_version: 2
uuid: 5a56db93-0164-5b97-948a-25023b298fe8
content_hash: sha256:bdff28ebe6dd39215008c45ba88df7ebada7196a3b9879a7a08bace793d7183c
---

<!-- AUTHORED REGION START -->
# Statistical Rethinking: A Bayesian Course with Examples in R and STAN

**Authors:** Richard McElreath  
**Year:** 2020  
**Type:** book  
**Markdown source:** `markdown_output/mcelreath-2020-statistical-rethinking.md`

## Summary

Statistical Rethinking: A Bayesian Course with Examples in R and Stan (2nd ed., 2020) by Richard McElreath is a graduate-level textbook published by CRC Press (Chapman & Hall/CRC Texts in Statistical Science). It teaches Bayesian statistical modeling from first principles using R and Stan, deliberately avoiding p-values and significance testing. The book spans 17 chapters plus endnotes and bibliography, progressing from basic probability and grid approximation through MCMC, GLMs, multilevel models, Gaussian processes, missing data, and ODE-based models. The second edition adds prior predictive simulation, DAGs for causal inference, splines, ordered categorical predictors, phylogenetic regression, and social network models, plus expanded raw Stan code. The author's stated goal is to provide the statistics textbook he wished he had in graduate school, written for researchers who sense something is wrong with conventional statistical practice but do not yet know where to turn.

## Key Claims

- The book explicitly rejects p-values and null hypothesis significance testing on epistemological grounds, not merely on Bayesian grounds.
- MCMC does not appear until Chapter 9 (halfway through); the first half uses quadratic (Laplace) approximation via the `quap` function to decouple learning Bayesian inference from learning MCMC.
- Prior predictive simulation is described as one of the most useful additions to the second edition, helping readers understand prior implications before seeing data.
- The author argues that formula-shortcut packages like `brms` and `rstanarm` hide the model structure and that explicit formula lists, while harder, produce deeper understanding.
- DAGs (directed acyclic graphs) are introduced to support causal inference, particularly in the context of multiple regression, spurious associations, and confounding.
- Chapter 16 is an entirely new chapter covering non-GLMM models including ordinary differential equation models.
- The book is designed for sequential, not random, access — it functions as a course, not a reference.
- All models are wrong, but some are useful (George Box maxim, quoted in code output).

## Main Concepts

- [[concepts/bayesian-statistical-inference|Bayesian statistical inference]]
- [[concepts/posterior-distribution|Posterior distribution]]
- [[concepts/prior-predictive-simulation|Prior predictive simulation]]
- [[concepts/quadratic-laplace-approximation-to-the-posterior|Quadratic (Laplace) approximation to the posterior]]
- [[concepts/markov-chain-monte-carlo-mcmc-|Markov Chain Monte Carlo (MCMC)]]
- [[concepts/hamiltonian-monte-carlo-hmc-|Hamiltonian Monte Carlo (HMC)]]
- [[concepts/directed-acyclic-graphs-dags-and-causal-inference|Directed acyclic graphs (DAGs) and causal inference]]
- [[concepts/spurious-association-and-collider-bias|Spurious association and collider bias]]
- [[concepts/multilevel-hierarchical-models-varying-effects-|Multilevel / hierarchical models (varying effects)]]
- [[concepts/generalized-linear-models-glm-and-maximum-entropy-priors|Generalized linear models (GLM) and maximum entropy priors]]
- [[concepts/regularization-and-overfitting-information-criteria-cross-validation-waic-|Regularization and overfitting (information criteria, cross-validation, WAIC)]]
- [[concepts/gaussian-processes|Gaussian processes]]
- [[concepts/missing-data-and-measurement-error|Missing data and measurement error]]
- [[concepts/ordered-categorical-models|Ordered categorical models]]
- [[concepts/splines|Splines]]
- [[concepts/ordinary-differential-equation-models|Ordinary differential equation models]]
- [[concepts/social-relations-model-social-network-|Social relations model (social network)]]
- [[concepts/phylogenetic-regression|Phylogenetic regression]]

## Key Entities

- [[entities/richard-mcelreath-author-max-planck-institute-for-evolutionary-anthropology-leipzig-|Richard McElreath (author; Max Planck Institute for Evolutionary Anthropology, Leipzig)]]
- [[entities/crc-press-chapman-hall-taylor-francis-group-publisher-|CRC Press / Chapman & Hall / Taylor & Francis Group (publisher)]]
- [[entities/max-planck-institute-for-evolutionary-anthropology-leipzig|Max Planck Institute for Evolutionary Anthropology, Leipzig]]
- [[entities/bret-beheim-contributor-commented-on-multiple-chapters-|Bret Beheim (contributor, commented on multiple chapters)]]
- [[entities/aki-vehtari-contributor-commented-on-multiple-chapters-|Aki Vehtari (contributor, commented on multiple chapters)]]
- [[entities/seamus-heaney-poet-quoted-in-preface-1939-2013-|Seamus Heaney (poet quoted in preface, 1939-2013)]]
- [[entities/emmanuel-paradis-author-of-r-for-beginners-recommended-resource-|Emmanuel Paradis (author of R for Beginners, recommended resource)]]
- [[entities/bruce-lee-metaphor-used-in-teaching-philosophy-passage-|Bruce Lee (metaphor used in teaching philosophy passage)]]
- [[entities/stan-probabilistic-programming-language-core-tool-|Stan (probabilistic programming language, core tool)]]
- [[entities/r-programming-language-primary-language-of-the-book-|R (programming language, primary language of the book)]]
- [[entities/rethinking-r-package-custom-package-accompanying-the-book-|rethinking (R package, custom package accompanying the book)]]
- [[entities/quap-function-in-rethinking-package-for-quadratic-approximation-|quap (function in rethinking package for quadratic approximation)]]
- [[entities/ulam-function-in-rethinking-package-replacing-map2stan-interfaces-to-stan-|ulam (function in rethinking package replacing map2stan, interfaces to Stan)]]
- [[entities/brms-r-package-mentioned-as-recommended-post-book-tool-|brms (R package, mentioned as recommended post-book tool)]]
- [[entities/rstanarm-r-package-mentioned-as-recommended-post-book-tool-|rstanarm (R package, mentioned as recommended post-book tool)]]
- [[entities/pymc-python-bayesian-library-recommended-alternative-|PyMC (Python Bayesian library, recommended alternative)]]
- [[entities/julia-programming-language-recommended-alternative-|Julia (programming language, recommended alternative)]]

## Questions Raised

- How does the `ulam` interface to Stan compare in capability to writing raw Stan models directly?
- What specific epistemological arguments does Chapter 1 make against p-values and null hypothesis testing?
- How does the book handle the distinction between causal and predictive inference across chapters 5 and 6?
- What data examples are used (cherry blossoms time series is mentioned; what others)?
- How does the phylogenetic regression chapter differ from standard treatments (described as 'heterodox')?
- Is Chapter 17 ('Horoscopes') a serious technical chapter or a concluding commentary?
- How does the book's treatment of information criteria (WAIC, LOO-CV) compare to frequentist AIC/BIC?

<!-- AUTHORED REGION END -->
