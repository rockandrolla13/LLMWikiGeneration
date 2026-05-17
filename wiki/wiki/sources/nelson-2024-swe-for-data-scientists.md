---
title: Software Engineering for Data Scientists
page_id: sources/nelson-2024-swe-for-data-scientists
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Catherine Nelson
year: 2024
publisher: O'Reilly Media
edition: Early Release
is_early_release: true
page_count_estimate: 300
tags:
- ai-engineering
- software-engineering
related:
- concepts/code-linting-and-formatting
- concepts/docstrings
- concepts/dont-repeat-yourself
- concepts/error-handling-and-logging
- concepts/experiment-tracking
- concepts/modular-code-design
- concepts/naming-conventions
- concepts/pep-8-style-guide
- concepts/refactoring
- concepts/software-testing
- concepts/technical-debt
- concepts/training-serving-skew
- entities/catherine-nelson
- entities/huggingface-transformers
- entities/john-ousterhout
- entities/oreilly-media
- entities/pandas
- entities/scikit-learn
- entities/sphinx
- entities/tim-peters
- entities/weights-and-biases
mind_map_priority: medium
revision_hash: sha256:1be67d4ba7625b6b
---

# Software Engineering for Data Scientists
*From Notebooks to Scalable Systems*

**Authors:** [[entities/catherine-nelson|Catherine Nelson]]

**Year:** 2024

**Publisher:** O'Reilly Media

**Edition:** Early Release

## Summary

Catherine Nelson's 'Software Engineering for Data Scientists' (O'Reilly, 2024 Early Release) is a practitioner-oriented bridge book that argues data scientists who learn software engineering practices can 'do more data science'. Drawing on her own transition from sole data scientist on an engineering team, Nelson distils the engineering mindset — planning, standardisation, automation — into five attributes of good code: simplicity, [[modular-code-design|modularity]], readability, efficiency, and robustness. The book is structured in three parts: Data Science Practices (writing good functions, efficiency, OOP, errors/logging, [[software-testing|testing]]), Applying Software Engineering Best Practices ([[code-linting-and-formatting|linting and formatting]], [[refactoring|refactoring]], packaging, [[docstrings|documentation]]), and Putting Data Science Projects into Production (APIs with FastAPI, CI/CD automation, security, working in dev teams).

The argument is built around the costs of [[technical-debt|technical debt]] and the [[dont-repeat-yourself|DRY principle]], with concrete data-science framings — for example, the [[training-serving-skew|training-serving skew]] problem motivates why preprocessing pipelines must be serialised alongside trained models. Nelson positions software craftsmanship as inherently valuable for individual code longevity and team collaboration: code is read more than written, requirements always change, and projects increasingly outlive their original authors. The Early Release contains only Chapter 1 ('What Is Good Code?') and Chapter 2 ('Documentation'), with the remaining twelve chapters stubbed via [Link to Come] references.

The book targets early-career data scientists, self-taught practitioners moving in from math or the sciences, and experienced data scientists who collaborate with software developers. It explicitly excludes setup of development environments, languages other than Python, command-line scripting, and advanced Python — pointing readers to VanderPlas, Grus, Janssens, and Ramalho for those gaps. Its angle versus competitors is the deliberate translation of software-engineering vocabulary into idioms that data scientists, pandas/scikit-learn users, and Jupyter notebook authors will recognise.

## Key Contributions

- Frames five attributes of 'good code' for data scientists — simplicity, modularity, readability, efficiency, robustness — as a single coherent rubric for self-assessment
- Articulates training-serving skew as a concrete instance where the DRY principle clashes with ML deployment reality, and proposes serialised preprocessing pipelines (scikit-learn Pipelines, tensorflow_transform) as the resolution
- Promotes function-interface design ('contracts') as the entry point to modularity for notebook-style developers, including the practical advice to cap inputs at three or four arguments
- Treats documentation as a first-class engineering activity with concrete forms (comments, docstrings, READMEs, tutorials, Jupyter markdown) and explicit anti-patterns (comments that restate code, abbreviated names, stale docs)
- Recommends experiment tracking (Weights and Biases, sacred, SageMaker Experiments) as the structured-documentation equivalent for ML iteration, distinct from code documentation

## Key Topics Covered

good-code-attributes, dry-principle, modular-code-design, function-interfaces, pep-8-style-guide, code-linting-and-formatting, naming-conventions, docstrings, comments, readme-files, jupyter-notebook-documentation, experiment-tracking, training-serving-skew, technical-debt, refactoring, software-testing, error-handling-and-logging

## Questions Raised

- How should data scientists decide where to draw the boundary between an 'exploratory' notebook that does not need engineering rigour and one that does?
- What is the right minimum viable test suite for a notebook-driven analysis that may or may not be productionised?
- How should preprocessing be versioned and audited so that training-serving skew does not silently degrade production models?
- How do these practices scale to teams where data scientists, ML engineers, and software developers share a single codebase under Agile workflows (deferred to a later chapter that is not in this Early Release)?
- Which engineering practices justify the upfront time investment for a solo data scientist whose work is read by no one else?

## Intended Audience

Early-career data scientists, self-taught practitioners, and data analysts/ML engineers/data engineers who need to bridge from exploratory notebook work to maintainable production Python code, especially those collaborating with software developers

## Key Concepts in This Source

- [[concepts/dont-repeat-yourself|Don't Repeat Yourself (DRY)]]
- [[concepts/modular-code-design|Modular Code Design]]
- [[concepts/technical-debt|Technical Debt]]
- [[concepts/refactoring|Refactoring]]
- [[concepts/software-testing|Software Testing]]
- [[concepts/pep-8-style-guide|PEP 8 Style Guide]]
- [[concepts/code-linting-and-formatting|Code Linting and Formatting]]
- [[concepts/docstrings|Docstrings]]
- [[concepts/training-serving-skew|Training-Serving Skew]]
- [[concepts/error-handling-and-logging|Error Handling and Logging]]
- [[concepts/experiment-tracking|Experiment Tracking]]
- [[concepts/naming-conventions|Naming Conventions]]

## Entities

- [[entities/catherine-nelson|Catherine Nelson]]
- [[entities/oreilly-media|O'Reilly Media]]
- [[entities/john-ousterhout|John Ousterhout]]
- [[entities/tim-peters|Tim Peters]]
- [[entities/weights-and-biases|Weights and Biases]]
- [[entities/scikit-learn|scikit-learn]]
- [[entities/pandas|Pandas]]
- [[entities/sphinx|Sphinx]]
- [[entities/huggingface-transformers|Hugging Face Transformers]]
