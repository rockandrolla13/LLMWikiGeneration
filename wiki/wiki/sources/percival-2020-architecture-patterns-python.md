---
title: Architecture Patterns with Python
page_id: sources/percival-2020-architecture-patterns-python
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-06-20T01:03:51Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Harry Percival
- Bob Gregory
year: 2020
publisher: O'Reilly Media
edition: 1st
is_early_release: false
page_count_estimate: 300
tags:
- ai-engineering
- software-engineering
related:
- concepts/aggregate-pattern
- concepts/command-query-responsibility-segregation
- concepts/dependency-inversion-principle
- concepts/domain-driven-design
- concepts/domain-events
- concepts/event-driven-microservices
- concepts/hexagonal-architecture
- concepts/message-bus
- concepts/repository-pattern
- concepts/service-layer-pattern
- concepts/test-driven-development
- concepts/unit-of-work-pattern
- entities/bob-gregory
- entities/eric-evans
- entities/flask
- entities/harry-percival
- entities/ian-cooper
- entities/made-com
- entities/martin-fowler
- entities/redis
- entities/sqlalchemy
mind_map_priority: medium
revision_hash: sha256:fff22579b48b752b
schema_version: 2
uuid: 057d32fb-03ce-5b6b-84c3-3b8ea7d4cf7b
content_hash: sha256:86e37a4031572acd0d0efc24b1d8ae379724c23475aae6b5624dd8f263d25290
---

<!-- AUTHORED REGION START -->
# Architecture Patterns with Python
*Enabling Test-Driven Development, Domain-Driven Design, and Event-Driven Microservices*

**Authors:** [[entities/harry-percival|Harry Percival]], [[entities/bob-gregory|Bob Gregory]]

**Year:** 2020

**Publisher:** O'Reilly Media

**Edition:** 1st

## Summary

Architecture Patterns with Python is a practitioner's guide to building maintainable Python applications by porting the canonical enterprise-architecture patterns — from Evans's [[domain-driven-design|Domain-Driven Design]] and Fowler's Patterns of Enterprise Application Architecture — into idiomatic Python. Drawing on the authors' experience building warehouse-allocation systems at MADE.com, Percival and Gregory work a single running example (allocating order lines to stock batches) through twelve chapters, each adding one architectural pattern: [[domain-driven-design|domain modelling]], the [[repository-pattern|Repository pattern]], the [[service-layer-pattern|Service Layer]], the [[unit-of-work-pattern|Unit of Work]], [[aggregate-pattern|Aggregates]] and consistency boundaries, [[domain-events|Domain Events]], a [[message-bus|Message Bus]], [[command-query-responsibility-segregation|CQRS]], and dependency injection.

The book's central argument is that the [[dependency-inversion-principle|Dependency Inversion Principle]] — combined with [[test-driven-development|TDD]] discipline and a clean [[hexagonal-architecture|hexagonal architecture]] — lets Python teams build software whose core business logic is fast to test, independent of frameworks, and able to evolve from a Flask monolith into a set of [[event-driven-microservices|event-driven microservices]] without major rewrites. The authors are particularly opinionated about testing 'in high gear' at the service layer rather than coupling tests to the domain model, and about treating commands and events as first-class messages handled uniformly by a message bus.

It is positioned not as a replacement for Evans or Fowler but as a Python-native bridge to that literature, on the premise that the Python ecosystem (Flask, Django, SQLAlchemy, Celery) is increasingly being used to build the kind of complex 'enterprise software' that the Java and C# worlds have wrestled with for years.

## Key Contributions

- A working Python implementation of the Repository, Unit of Work, and Service Layer patterns that uses SQLAlchemy classical mapping so the ORM depends on the domain model rather than the other way round.
- A concrete recipe for evolving a Flask monolith into an event-driven, message-bus-centric system where every use case becomes a handler for a command or event.
- An opinionated test strategy ('high gear / low gear') that argues for moving most behavioural tests to the service layer so the domain model can be refactored freely.
- A pragmatic treatment of aggregates and consistency boundaries that links DDD aggregate choice directly to repository granularity and database concurrency control.
- A demonstration of CQRS without event sourcing — keeping a rich write model while building a separate denormalised read model updated by event handlers.

## Key Topics Covered

domain-driven-design, repository-pattern, unit-of-work-pattern, service-layer-pattern, aggregate-pattern, domain-events, message-bus, command-query-responsibility-segregation, event-driven-microservices, hexagonal-architecture, dependency-inversion-principle, test-driven-development, dependency-injection, ports-and-adapters, flask, sqlalchemy, redis-pubsub

## Questions Raised

- How do you retrofit these patterns into an existing legacy Python codebase (only briefly addressed in the epilogue)?
- When does the operational complexity of an event-driven, message-bus architecture outweigh the design benefits for a small team?
- How should event schemas be versioned and governed once events become an integration contract between independently deployed microservices?
- When (if ever) is full event sourcing worth the additional complexity over the CQRS-with-read-models approach the book demonstrates?

## Intended Audience

Mid-to-senior Python developers building non-trivial backend systems (Flask/Django/SQLAlchemy) who feel the pain of a tangled codebase and want to learn DDD, hexagonal architecture, and event-driven design without first translating Java/C# textbooks.

## Key Concepts in This Source

- [[concepts/domain-driven-design|Domain-Driven Design]]
- [[concepts/repository-pattern|Repository Pattern]]
- [[concepts/unit-of-work-pattern|Unit of Work Pattern]]
- [[concepts/hexagonal-architecture|Hexagonal Architecture]]
- [[concepts/dependency-inversion-principle|Dependency Inversion Principle]]
- [[concepts/test-driven-development|Test-Driven Development]]
- [[concepts/service-layer-pattern|Service Layer Pattern]]
- [[concepts/aggregate-pattern|Aggregate Pattern]]
- [[concepts/domain-events|Domain Events]]
- [[concepts/message-bus|Message Bus]]
- [[concepts/command-query-responsibility-segregation|Command-Query Responsibility Segregation]]
- [[concepts/event-driven-microservices|Event-Driven Microservices]]

## Entities

- [[entities/harry-percival|Harry Percival]]
- [[entities/bob-gregory|Bob Gregory]]
- [[entities/eric-evans|Eric Evans]]
- [[entities/martin-fowler|Martin Fowler]]
- [[entities/ian-cooper|Ian Cooper]]
- [[entities/made-com|MADE.com]]
- [[entities/flask|Flask]]
- [[entities/sqlalchemy|SQLAlchemy]]
- [[entities/redis|Redis]]

<!-- AUTHORED REGION END -->
