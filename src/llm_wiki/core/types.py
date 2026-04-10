"""Domain types for LLM Wiki.

Re-exports all types from schemas.py for a cleaner import path.
New code can import from llm_wiki.core.types instead of llm_wiki.schemas.

Example:
    from llm_wiki.core.types import PageType, PageMeta, SourcePage
"""

# Re-export all types from schemas
from ..schemas import (
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
