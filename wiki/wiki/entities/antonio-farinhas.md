---
title: Antonio Farinhas
page_id: entities/antonio-farinhas
page_type: entity
entity_type: person
revision_id: 1
created: 2026-04-26 12:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- researcher
- conformal-prediction
- uncertainty-quantification
- nlp
sources:
- sources/farinhas-2024-non-exchangeable-crc
related:
- concepts/conformal-prediction
- concepts/conformal-risk-control
- entities/andre-martins
- entities/chrysoula-zerva
mind_map_priority: medium
schema_version: 2
uuid: 8da08ae6-d1e8-56e0-a3cd-19422ee73ab8
content_hash: sha256:10cb5aca3b9dcbca7e5c7760fda26be74332381467f1489773c5f3283b3321ef
---

<!-- AUTHORED REGION START -->
# Antonio Farinhas

**Antonio Farinhas** is a researcher specializing in [[concepts/uncertainty-quantification|uncertainty quantification]] and [[concepts/conformal-prediction|conformal prediction]] for machine learning systems.

## Affiliation

- Instituto de Telecomunicações, Lisbon
- Instituto Superior Técnico, Universidade de Lisboa (Lisbon ELLIS Unit)

## Research Focus

Farinhas works on developing methods for reliable uncertainty quantification in machine learning, particularly for NLP applications. His research extends conformal prediction frameworks to handle non-exchangeable data distributions commonly encountered in real-world deployments.

## Key Contributions

### Non-Exchangeable Conformal Risk Control

[[sources/farinhas-2024-non-exchangeable-crc|Farinhas et al. (2024)]] at ICLR 2024 introduced a unified framework combining:
- Non-exchangeable conformal prediction (handling distribution drift)
- Conformal risk control (bounding arbitrary loss functions)

The method enables controlling expected loss of monotone functions when data violates exchangeability assumptions, with applications to time series, question answering, and multilabel classification.

## Collaborators

- [[entities/andre-martins|André F.T. Martins]] (Unbabel, IST)
- [[entities/chrysoula-zerva|Chrysoula Zerva]] (IST)
- [[entities/dennis-ulmer|Dennis Ulmer]] (ITU Copenhagen)

## Publications in This Wiki

- [[sources/farinhas-2024-non-exchangeable-crc|Non-Exchangeable Conformal Risk Control (ICLR 2024)]]

## See Also

- [[concepts/conformal-risk-control|Conformal Risk Control]]
- [[concepts/distribution-drift|Distribution Drift]]

<!-- AUTHORED REGION END -->
