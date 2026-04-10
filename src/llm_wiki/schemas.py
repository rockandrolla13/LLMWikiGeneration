"""Page schemas for LLM Wiki.

Defines dataclasses for all Tier 1 canonical page types:
- PageMeta: Common metadata for all pages
- SourcePage: Summary of an ingested source document
- EntityPage: Profile for a person, organization, or place
- ConceptPage: Explanation of an idea, technique, or methodology
- AnalysisPage: Saved query answer or comparison
- ContradictionPage: Record of disagreement between sources
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional
import hashlib


class PageType(Enum):
    """Types of wiki pages."""
    SOURCE = "source"
    ENTITY = "entity"
    CONCEPT = "concept"
    ANALYSIS = "analysis"
    CONTRADICTION = "contradiction"


class EntityType(Enum):
    """Types of entities."""
    PERSON = "person"
    ORGANIZATION = "organization"
    PLACE = "place"
    PRODUCT = "product"


class ConceptType(Enum):
    """Types of concepts."""
    TECHNIQUE = "technique"
    THEORY = "theory"
    FRAMEWORK = "framework"
    METHODOLOGY = "methodology"


class AbstractionLevel(Enum):
    """Abstraction levels for concepts."""
    FOUNDATIONAL = "foundational"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class ContradictionStatus(Enum):
    """Status of a contradiction."""
    UNRESOLVED = "unresolved"
    RESOLVED = "resolved"
    SUPERSEDED = "superseded"


class SourceType(Enum):
    """Types of source documents."""
    PAPER = "paper"
    ARTICLE = "article"
    BOOK = "book"
    NOTES = "notes"
    TRANSCRIPT = "transcript"


class MindMapPriority(Enum):
    """Priority levels for MIND_MAP inclusion."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    EXCLUDE = "exclude"


def compute_content_hash(content: str) -> str:
    """Compute SHA-256 hash of content."""
    return f"sha256:{hashlib.sha256(content.encode('utf-8')).hexdigest()}"


@dataclass
class PageMeta:
    """Common metadata for all wiki pages.

    All canonical wiki pages share this base metadata for
    identity, revision tracking, relationships, and classification.
    """
    # Identity
    title: str
    page_id: str  # e.g., "concepts/machine_learning"
    page_type: PageType

    # Revision tracking
    revision_id: int = 1
    revision_hash: str = ""
    created: datetime = field(default_factory=datetime.utcnow)
    updated: datetime = field(default_factory=datetime.utcnow)
    updated_by: str = ""  # Reference to op_id in manifest.jsonl

    # Relationships
    sources: list[str] = field(default_factory=list)  # page_ids of source pages
    related: list[str] = field(default_factory=list)  # page_ids of related pages

    # Classification
    tags: list[str] = field(default_factory=list)

    # MIND_MAP hints
    mind_map_priority: MindMapPriority = MindMapPriority.MEDIUM
    mind_map_category: Optional[int] = None  # Routing node [1-5]

    def to_frontmatter_dict(self) -> dict:
        """Convert to dictionary for YAML frontmatter."""
        return {
            "title": self.title,
            "page_id": self.page_id,
            "page_type": self.page_type.value,
            "revision_id": self.revision_id,
            "revision_hash": self.revision_hash,
            "created": self.created.isoformat() + "Z",
            "updated": self.updated.isoformat() + "Z",
            "updated_by": self.updated_by,
            "sources": self.sources,
            "related": self.related,
            "tags": self.tags,
            "mind_map_priority": self.mind_map_priority.value,
            "mind_map_category": self.mind_map_category,
        }


@dataclass
class SourcePage:
    """Summary page for an ingested source document.

    Created when a new source is ingested into the wiki.
    Links to the original file in raw/ and extracts key information.
    """
    meta: PageMeta

    # Source-specific fields
    source_path: str  # e.g., "raw/vaswani2017_attention.pdf"
    source_hash: str  # SHA-256 of source file
    source_type: SourceType = SourceType.ARTICLE
    authors: list[str] = field(default_factory=list)
    publication_date: Optional[str] = None
    publication_venue: Optional[str] = None

    # Content sections (populated during ingest)
    summary: str = ""
    key_claims: list[dict] = field(default_factory=list)  # [{claim, evidence, confidence}]
    methodology: str = ""
    limitations: str = ""
    notable_quotes: list[str] = field(default_factory=list)
    questions_raised: list[str] = field(default_factory=list)
    extracted_entities: list[str] = field(default_factory=list)  # page_ids
    extracted_concepts: list[str] = field(default_factory=list)  # page_ids

    def __post_init__(self):
        self.meta.page_type = PageType.SOURCE

    def to_frontmatter_dict(self) -> dict:
        """Convert to dictionary for YAML frontmatter."""
        d = self.meta.to_frontmatter_dict()
        d.update({
            "source_path": self.source_path,
            "source_hash": self.source_hash,
            "source_type": self.source_type.value,
            "authors": self.authors,
            "publication_date": self.publication_date,
            "publication_venue": self.publication_venue,
        })
        return d


@dataclass
class EntityPage:
    """Profile page for a person, organization, place, or product.

    Created when an entity is mentioned across sources and warrants
    its own dedicated page for tracking appearances and relationships.
    """
    meta: PageMeta

    # Entity-specific fields
    entity_type: EntityType = EntityType.PERSON
    aliases: list[str] = field(default_factory=list)
    external_ids: dict[str, str] = field(default_factory=dict)  # {platform: id}

    # Content sections
    overview: str = ""
    relevance: str = ""  # Why this entity matters in wiki context
    appearances: list[dict] = field(default_factory=list)  # [{source, context}]
    relationships: dict[str, list[str]] = field(default_factory=dict)  # {relation_type: [page_ids]}

    def __post_init__(self):
        self.meta.page_type = PageType.ENTITY

    def to_frontmatter_dict(self) -> dict:
        """Convert to dictionary for YAML frontmatter."""
        d = self.meta.to_frontmatter_dict()
        d.update({
            "entity_type": self.entity_type.value,
            "aliases": self.aliases,
            "external_ids": self.external_ids,
        })
        return d


@dataclass
class ConceptPage:
    """Explanation page for an idea, technique, or methodology.

    Created when a concept appears across multiple sources and
    requires synthesis and cross-referencing.
    """
    meta: PageMeta

    # Concept-specific fields
    concept_type: ConceptType = ConceptType.TECHNIQUE
    abstraction_level: AbstractionLevel = AbstractionLevel.INTERMEDIATE

    # Content sections
    definition: str = ""
    key_properties: list[str] = field(default_factory=list)
    how_it_works: str = ""
    concept_relationships: dict[str, list[str]] = field(default_factory=dict)  # {relation_type: [page_ids]}
    claims_across_sources: list[dict] = field(default_factory=list)  # [{claim, source, confidence}]
    contradictions: list[str] = field(default_factory=list)  # page_ids of contradiction pages
    open_questions: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.meta.page_type = PageType.CONCEPT

    def to_frontmatter_dict(self) -> dict:
        """Convert to dictionary for YAML frontmatter."""
        d = self.meta.to_frontmatter_dict()
        d.update({
            "concept_type": self.concept_type.value,
            "abstraction_level": self.abstraction_level.value,
        })
        return d


@dataclass
class AnalysisPage:
    """Saved query answer or comparison.

    Created when a valuable query response should be preserved
    in the wiki rather than lost to chat history.
    """
    meta: PageMeta

    # Analysis-specific fields
    query: str = ""  # Original question that prompted this analysis
    methodology: str = ""  # How the analysis was conducted

    # Content sections
    findings: str = ""
    evidence: list[dict] = field(default_factory=list)  # [{claim, sources, confidence}]
    conclusions: str = ""
    limitations: str = ""
    follow_up_questions: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.meta.page_type = PageType.ANALYSIS

    def to_frontmatter_dict(self) -> dict:
        """Convert to dictionary for YAML frontmatter."""
        d = self.meta.to_frontmatter_dict()
        d.update({
            "query": self.query,
        })
        return d


@dataclass
class ContradictionPage:
    """Record of disagreement between sources.

    Created when two or more sources make conflicting claims
    about the same topic. Tracks the contradiction status and
    potential resolutions.
    """
    meta: PageMeta

    # Contradiction-specific fields
    status: ContradictionStatus = ContradictionStatus.UNRESOLVED
    topic: str = ""  # page_id of the concept/entity being contradicted
    sources_involved: list[str] = field(default_factory=list)  # page_ids

    # Content sections
    claim_a: dict = field(default_factory=dict)  # {source, claim, evidence}
    claim_b: dict = field(default_factory=dict)  # {source, claim, evidence}
    analysis: str = ""
    possible_resolutions: list[str] = field(default_factory=list)
    current_status_explanation: str = ""
    impact_on_wiki: list[str] = field(default_factory=list)  # Affected page_ids

    def __post_init__(self):
        self.meta.page_type = PageType.CONTRADICTION

    def to_frontmatter_dict(self) -> dict:
        """Convert to dictionary for YAML frontmatter."""
        d = self.meta.to_frontmatter_dict()
        d.update({
            "status": self.status.value,
            "topic": self.topic,
            "sources_involved": self.sources_involved,
        })
        return d
