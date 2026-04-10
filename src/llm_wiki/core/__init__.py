"""Core package for LLM Wiki.

Provides:
- Protocol definitions for pluggable components
- Type re-exports for cleaner imports
- Generic registry pattern for extensibility

Example usage:
    from llm_wiki.core.types import PageType, PageMeta
    from llm_wiki.core.protocols import VerificationCheck, Registry
"""

from .protocols import (
    VerificationCheck,
    DerivedArtifactCompiler,
    PageFactory,
    Registry,
    VerificationRegistry,
    ArtifactRegistry,
)
from .types import (
    # Enums
    PageType,
    EntityType,
    ConceptType,
    AbstractionLevel,
    ContradictionStatus,
    SourceType,
    MindMapPriority,
    # Dataclasses
    PageMeta,
    SourcePage,
    EntityPage,
    ConceptPage,
    AnalysisPage,
    ContradictionPage,
    # Functions
    compute_content_hash,
)

__all__ = [
    # Protocols
    "VerificationCheck",
    "DerivedArtifactCompiler",
    "PageFactory",
    "Registry",
    "VerificationRegistry",
    "ArtifactRegistry",
    # Enums
    "PageType",
    "EntityType",
    "ConceptType",
    "AbstractionLevel",
    "ContradictionStatus",
    "SourceType",
    "MindMapPriority",
    # Dataclasses
    "PageMeta",
    "SourcePage",
    "EntityPage",
    "ConceptPage",
    "AnalysisPage",
    "ContradictionPage",
    # Functions
    "compute_content_hash",
]
