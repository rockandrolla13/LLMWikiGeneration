"""Page factory functions for LLM Wiki.

Provides factory functions for creating wiki page dataclasses with
consistent defaults and proper page ID normalization.

Each factory function:
- Creates the appropriate page type with sensible defaults
- Normalizes the title to generate a consistent page_id
- Sets creation/update timestamps to current time
- Accepts **meta_overrides for customizing PageMeta fields
"""

from datetime import datetime
from typing import Optional

from ..schemas import (
    PageType,
    PageMeta,
    SourcePage,
    EntityPage,
    ConceptPage,
    AnalysisPage,
    ContradictionPage,
    SourceType,
    EntityType,
    ConceptType,
    AbstractionLevel,
    ContradictionStatus,
    MindMapPriority,
)
from ..io.wikilinks import normalize_page_id


def create_source_page(
    title: str,
    source_path: str,
    source_hash: str,
    summary: str = "",
    key_claims: Optional[list[dict]] = None,
    source_type: SourceType = SourceType.ARTICLE,
    authors: Optional[list[str]] = None,
    publication_date: Optional[str] = None,
    publication_venue: Optional[str] = None,
    methodology: str = "",
    limitations: str = "",
    notable_quotes: Optional[list[str]] = None,
    questions_raised: Optional[list[str]] = None,
    extracted_entities: Optional[list[str]] = None,
    extracted_concepts: Optional[list[str]] = None,
    **meta_overrides,
) -> SourcePage:
    """Create a SourcePage with consistent defaults.

    Args:
        title: Human-readable page title
        source_path: Path to the source file (e.g., "raw/paper.pdf")
        source_hash: SHA-256 hash of the source file
        summary: One-paragraph summary of the source
        key_claims: List of claims dicts [{claim, evidence, confidence}]
        source_type: Type of source document
        authors: List of author names
        publication_date: Date string (format flexible)
        publication_venue: Where the source was published
        methodology: Description of methods used in source
        limitations: Acknowledged limitations
        notable_quotes: List of important quotes from source
        questions_raised: Questions for follow-up
        extracted_entities: page_ids of entities mentioned
        extracted_concepts: page_ids of concepts mentioned
        **meta_overrides: Additional PageMeta field overrides

    Returns:
        Configured SourcePage instance
    """
    page_id = f"sources/{normalize_page_id(title)}"
    now = datetime.utcnow()

    meta = PageMeta(
        title=title,
        page_id=page_id,
        page_type=PageType.SOURCE,
        created=meta_overrides.pop("created", now),
        updated=meta_overrides.pop("updated", now),
        **meta_overrides,
    )

    return SourcePage(
        meta=meta,
        source_path=source_path,
        source_hash=source_hash,
        source_type=source_type,
        authors=authors or [],
        publication_date=publication_date,
        publication_venue=publication_venue,
        summary=summary,
        key_claims=key_claims or [],
        methodology=methodology,
        limitations=limitations,
        notable_quotes=notable_quotes or [],
        questions_raised=questions_raised or [],
        extracted_entities=extracted_entities or [],
        extracted_concepts=extracted_concepts or [],
    )


def create_entity_page(
    title: str,
    entity_type: EntityType = EntityType.PERSON,
    overview: str = "",
    relevance: str = "",
    aliases: Optional[list[str]] = None,
    external_ids: Optional[dict[str, str]] = None,
    appearances: Optional[list[dict]] = None,
    relationships: Optional[dict[str, list[str]]] = None,
    **meta_overrides,
) -> EntityPage:
    """Create an EntityPage with consistent defaults.

    Args:
        title: Human-readable entity name
        entity_type: Type of entity (person, organization, place, product)
        overview: Brief description of the entity
        relevance: Why this entity matters in the wiki context
        aliases: Alternative names for the entity
        external_ids: External identifiers {platform: id}
        appearances: List of appearance dicts [{source, context}]
        relationships: Relations to other pages {relation_type: [page_ids]}
        **meta_overrides: Additional PageMeta field overrides

    Returns:
        Configured EntityPage instance
    """
    page_id = f"entities/{normalize_page_id(title)}"
    now = datetime.utcnow()

    meta = PageMeta(
        title=title,
        page_id=page_id,
        page_type=PageType.ENTITY,
        created=meta_overrides.pop("created", now),
        updated=meta_overrides.pop("updated", now),
        **meta_overrides,
    )

    return EntityPage(
        meta=meta,
        entity_type=entity_type,
        aliases=aliases or [],
        external_ids=external_ids or {},
        overview=overview,
        relevance=relevance,
        appearances=appearances or [],
        relationships=relationships or {},
    )


def create_concept_page(
    title: str,
    concept_type: ConceptType = ConceptType.TECHNIQUE,
    abstraction_level: AbstractionLevel = AbstractionLevel.INTERMEDIATE,
    definition: str = "",
    key_properties: Optional[list[str]] = None,
    how_it_works: str = "",
    concept_relationships: Optional[dict[str, list[str]]] = None,
    claims_across_sources: Optional[list[dict]] = None,
    contradictions: Optional[list[str]] = None,
    open_questions: Optional[list[str]] = None,
    **meta_overrides,
) -> ConceptPage:
    """Create a ConceptPage with consistent defaults.

    Args:
        title: Human-readable concept name
        concept_type: Type of concept (technique, theory, framework, methodology)
        abstraction_level: How advanced the concept is
        definition: Clear definition of the concept
        key_properties: Important characteristics of the concept
        how_it_works: Explanation of mechanics/details
        concept_relationships: Relations to other concepts {relation_type: [page_ids]}
        claims_across_sources: Claims from different sources [{claim, source, confidence}]
        contradictions: page_ids of related contradiction pages
        open_questions: Unanswered questions about this concept
        **meta_overrides: Additional PageMeta field overrides

    Returns:
        Configured ConceptPage instance
    """
    page_id = f"concepts/{normalize_page_id(title)}"
    now = datetime.utcnow()

    meta = PageMeta(
        title=title,
        page_id=page_id,
        page_type=PageType.CONCEPT,
        created=meta_overrides.pop("created", now),
        updated=meta_overrides.pop("updated", now),
        **meta_overrides,
    )

    return ConceptPage(
        meta=meta,
        concept_type=concept_type,
        abstraction_level=abstraction_level,
        definition=definition,
        key_properties=key_properties or [],
        how_it_works=how_it_works,
        concept_relationships=concept_relationships or {},
        claims_across_sources=claims_across_sources or [],
        contradictions=contradictions or [],
        open_questions=open_questions or [],
    )


def create_analysis_page(
    title: str,
    query: str,
    findings: str = "",
    methodology: str = "",
    evidence: Optional[list[dict]] = None,
    conclusions: str = "",
    limitations: str = "",
    follow_up_questions: Optional[list[str]] = None,
    **meta_overrides,
) -> AnalysisPage:
    """Create an AnalysisPage with consistent defaults.

    Args:
        title: Human-readable title for the analysis
        query: Original question that prompted this analysis
        findings: Main findings/observations
        methodology: How the analysis was conducted
        evidence: Supporting evidence [{claim, sources, confidence}]
        conclusions: Key conclusions drawn
        limitations: Acknowledged limitations of the analysis
        follow_up_questions: Questions for further investigation
        **meta_overrides: Additional PageMeta field overrides

    Returns:
        Configured AnalysisPage instance
    """
    page_id = f"analyses/{normalize_page_id(title)}"
    now = datetime.utcnow()

    meta = PageMeta(
        title=title,
        page_id=page_id,
        page_type=PageType.ANALYSIS,
        created=meta_overrides.pop("created", now),
        updated=meta_overrides.pop("updated", now),
        **meta_overrides,
    )

    return AnalysisPage(
        meta=meta,
        query=query,
        methodology=methodology,
        findings=findings,
        evidence=evidence or [],
        conclusions=conclusions,
        limitations=limitations,
        follow_up_questions=follow_up_questions or [],
    )


def create_contradiction_page(
    title: str,
    topic: str,
    sources_involved: list[str],
    claim_a: Optional[dict] = None,
    claim_b: Optional[dict] = None,
    status: ContradictionStatus = ContradictionStatus.UNRESOLVED,
    analysis: str = "",
    possible_resolutions: Optional[list[str]] = None,
    current_status_explanation: str = "",
    impact_on_wiki: Optional[list[str]] = None,
    **meta_overrides,
) -> ContradictionPage:
    """Create a ContradictionPage with consistent defaults.

    Args:
        title: Human-readable title for the contradiction
        topic: page_id of the concept/entity being contradicted
        sources_involved: page_ids of sources with conflicting claims
        claim_a: First claim {source, claim, evidence}
        claim_b: Second claim {source, claim, evidence}
        status: Current status of the contradiction
        analysis: Analysis of the contradiction
        possible_resolutions: List of potential resolutions
        current_status_explanation: Why the contradiction has its current status
        impact_on_wiki: page_ids of pages affected by this contradiction
        **meta_overrides: Additional PageMeta field overrides

    Returns:
        Configured ContradictionPage instance
    """
    page_id = f"contradictions/{normalize_page_id(title)}"
    now = datetime.utcnow()

    meta = PageMeta(
        title=title,
        page_id=page_id,
        page_type=PageType.CONTRADICTION,
        created=meta_overrides.pop("created", now),
        updated=meta_overrides.pop("updated", now),
        **meta_overrides,
    )

    return ContradictionPage(
        meta=meta,
        status=status,
        topic=topic,
        sources_involved=sources_involved,
        claim_a=claim_a or {},
        claim_b=claim_b or {},
        analysis=analysis,
        possible_resolutions=possible_resolutions or [],
        current_status_explanation=current_status_explanation,
        impact_on_wiki=impact_on_wiki or [],
    )
