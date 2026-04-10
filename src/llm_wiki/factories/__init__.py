"""Factory functions for creating wiki page objects.

This module provides convenient factory functions for creating
page dataclasses with consistent defaults and proper page ID
normalization.

Example usage:
    from llm_wiki.factories import create_source_page, create_concept_page

    # Create a source page
    source = create_source_page(
        title="Attention Is All You Need",
        source_path="raw/vaswani2017.pdf",
        source_hash="sha256:abc123...",
        summary="Introduces the Transformer architecture.",
        authors=["Vaswani", "Shazeer", "Parmar"],
    )

    # Create a concept page
    concept = create_concept_page(
        title="Transformer Architecture",
        concept_type=ConceptType.TECHNIQUE,
        definition="A neural network architecture based on self-attention.",
    )
"""

from .pages import (
    create_source_page,
    create_entity_page,
    create_concept_page,
    create_analysis_page,
    create_contradiction_page,
)

__all__ = [
    "create_source_page",
    "create_entity_page",
    "create_concept_page",
    "create_analysis_page",
    "create_contradiction_page",
]
