"""Unit tests for schemas module.

Tests all dataclasses and enums in llm_wiki.schemas:
- PageType, EntityType, ConceptType, AbstractionLevel, etc.
- PageMeta, SourcePage, EntityPage, ConceptPage, AnalysisPage, ContradictionPage
- compute_content_hash function
"""

from datetime import datetime
import pytest

from llm_wiki.schemas import (
    PageType,
    EntityType,
    ConceptType,
    AbstractionLevel,
    ContradictionStatus,
    SourceType,
    MindMapPriority,
    PageMeta,
    SourcePage,
    EntityPage,
    ConceptPage,
    AnalysisPage,
    ContradictionPage,
    compute_content_hash,
)


class TestEnums:
    """Test all enum types."""

    def test_page_type_values(self):
        """PageType enum has correct values."""
        assert PageType.SOURCE.value == "source"
        assert PageType.ENTITY.value == "entity"
        assert PageType.CONCEPT.value == "concept"
        assert PageType.ANALYSIS.value == "analysis"
        assert PageType.CONTRADICTION.value == "contradiction"

    def test_page_type_from_value(self):
        """PageType can be created from string value."""
        assert PageType("source") == PageType.SOURCE
        assert PageType("entity") == PageType.ENTITY

    def test_page_type_invalid_value(self):
        """PageType raises error for invalid value."""
        with pytest.raises(ValueError):
            PageType("invalid")

    def test_entity_type_values(self):
        """EntityType enum has correct values."""
        assert EntityType.PERSON.value == "person"
        assert EntityType.ORGANIZATION.value == "organization"
        assert EntityType.PLACE.value == "place"
        assert EntityType.PRODUCT.value == "product"

    def test_concept_type_values(self):
        """ConceptType enum has correct values."""
        assert ConceptType.TECHNIQUE.value == "technique"
        assert ConceptType.THEORY.value == "theory"
        assert ConceptType.FRAMEWORK.value == "framework"
        assert ConceptType.METHODOLOGY.value == "methodology"

    def test_abstraction_level_values(self):
        """AbstractionLevel enum has correct values."""
        assert AbstractionLevel.FOUNDATIONAL.value == "foundational"
        assert AbstractionLevel.INTERMEDIATE.value == "intermediate"
        assert AbstractionLevel.ADVANCED.value == "advanced"

    def test_contradiction_status_values(self):
        """ContradictionStatus enum has correct values."""
        assert ContradictionStatus.UNRESOLVED.value == "unresolved"
        assert ContradictionStatus.RESOLVED.value == "resolved"
        assert ContradictionStatus.SUPERSEDED.value == "superseded"

    def test_source_type_values(self):
        """SourceType enum has correct values."""
        assert SourceType.PAPER.value == "paper"
        assert SourceType.ARTICLE.value == "article"
        assert SourceType.BOOK.value == "book"
        assert SourceType.NOTES.value == "notes"
        assert SourceType.TRANSCRIPT.value == "transcript"

    def test_mind_map_priority_values(self):
        """MindMapPriority enum has correct values."""
        assert MindMapPriority.HIGH.value == "high"
        assert MindMapPriority.MEDIUM.value == "medium"
        assert MindMapPriority.LOW.value == "low"
        assert MindMapPriority.EXCLUDE.value == "exclude"


class TestComputeContentHash:
    """Test compute_content_hash function."""

    def test_hash_returns_prefixed_sha256(self):
        """Hash returns sha256-prefixed string."""
        hash_val = compute_content_hash("test content")
        assert hash_val.startswith("sha256:")
        assert len(hash_val) == 7 + 64  # "sha256:" + 64 hex chars

    def test_hash_deterministic(self):
        """Same content produces same hash."""
        content = "This is test content."
        hash1 = compute_content_hash(content)
        hash2 = compute_content_hash(content)
        assert hash1 == hash2

    def test_hash_different_for_different_content(self):
        """Different content produces different hash."""
        hash1 = compute_content_hash("content A")
        hash2 = compute_content_hash("content B")
        assert hash1 != hash2

    def test_hash_empty_string(self):
        """Empty string produces valid hash."""
        hash_val = compute_content_hash("")
        assert hash_val.startswith("sha256:")
        # SHA-256 of empty string is a known value
        assert hash_val == "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

    def test_hash_unicode_content(self):
        """Unicode content produces valid hash."""
        hash_val = compute_content_hash("Hello, world!")
        assert hash_val.startswith("sha256:")


class TestPageMeta:
    """Test PageMeta dataclass."""

    def test_create_minimal(self):
        """Create PageMeta with minimal required fields."""
        meta = PageMeta(
            title="Test Page",
            page_id="concepts/test",
            page_type=PageType.CONCEPT,
        )
        assert meta.title == "Test Page"
        assert meta.page_id == "concepts/test"
        assert meta.page_type == PageType.CONCEPT
        assert meta.revision_id == 1
        assert meta.revision_hash == ""
        assert isinstance(meta.created, datetime)
        assert isinstance(meta.updated, datetime)

    def test_create_with_all_fields(self):
        """Create PageMeta with all fields."""
        now = datetime.utcnow()
        meta = PageMeta(
            title="Full Page",
            page_id="sources/full",
            page_type=PageType.SOURCE,
            revision_id=5,
            revision_hash="sha256:abc123",
            created=now,
            updated=now,
            updated_by="op_123456",
            sources=["source1", "source2"],
            related=["related1"],
            tags=["tag1", "tag2"],
            mind_map_priority=MindMapPriority.HIGH,
            mind_map_category=2,
        )
        assert meta.revision_id == 5
        assert meta.revision_hash == "sha256:abc123"
        assert meta.updated_by == "op_123456"
        assert meta.sources == ["source1", "source2"]
        assert meta.related == ["related1"]
        assert meta.tags == ["tag1", "tag2"]
        assert meta.mind_map_priority == MindMapPriority.HIGH
        assert meta.mind_map_category == 2

    def test_to_frontmatter_dict(self):
        """PageMeta converts to frontmatter dict correctly."""
        now = datetime(2024, 1, 15, 12, 30, 0)
        meta = PageMeta(
            title="Test Page",
            page_id="concepts/test",
            page_type=PageType.CONCEPT,
            revision_id=2,
            created=now,
            updated=now,
            tags=["ml", "ai"],
        )
        d = meta.to_frontmatter_dict()

        assert d["title"] == "Test Page"
        assert d["page_id"] == "concepts/test"
        assert d["page_type"] == "concept"
        assert d["revision_id"] == 2
        assert d["created"] == "2024-01-15T12:30:00Z"
        assert d["updated"] == "2024-01-15T12:30:00Z"
        assert d["tags"] == ["ml", "ai"]
        assert d["mind_map_priority"] == "medium"

    def test_default_lists_are_independent(self):
        """Default lists are independent between instances."""
        meta1 = PageMeta(title="Page1", page_id="p1", page_type=PageType.CONCEPT)
        meta2 = PageMeta(title="Page2", page_id="p2", page_type=PageType.CONCEPT)

        meta1.sources.append("source1")
        meta1.tags.append("tag1")

        assert "source1" not in meta2.sources
        assert "tag1" not in meta2.tags


class TestSourcePage:
    """Test SourcePage dataclass."""

    def test_create_source_page(self):
        """Create SourcePage with required fields."""
        meta = PageMeta(
            title="Paper Title",
            page_id="sources/paper",
            page_type=PageType.SOURCE,
        )
        page = SourcePage(
            meta=meta,
            source_path="raw/paper.pdf",
            source_hash="sha256:abc123",
        )
        assert page.meta.title == "Paper Title"
        assert page.source_path == "raw/paper.pdf"
        assert page.source_hash == "sha256:abc123"
        assert page.source_type == SourceType.ARTICLE

    def test_source_page_post_init_sets_type(self):
        """SourcePage __post_init__ sets page_type to SOURCE."""
        meta = PageMeta(
            title="Test",
            page_id="sources/test",
            page_type=PageType.ENTITY,  # Intentionally wrong
        )
        page = SourcePage(meta=meta, source_path="raw/test.md", source_hash="sha256:xxx")
        # __post_init__ should set it to SOURCE
        assert page.meta.page_type == PageType.SOURCE

    def test_source_page_with_all_fields(self):
        """Create SourcePage with all optional fields."""
        meta = PageMeta(title="Test", page_id="sources/test", page_type=PageType.SOURCE)
        page = SourcePage(
            meta=meta,
            source_path="raw/test.md",
            source_hash="sha256:xxx",
            source_type=SourceType.PAPER,
            authors=["Author A", "Author B"],
            publication_date="2024-01",
            publication_venue="Journal X",
            summary="A test summary.",
            key_claims=[{"claim": "Test claim", "evidence": "Evidence", "confidence": "high"}],
            methodology="Test methodology",
            limitations="Test limitations",
            notable_quotes=["Quote 1", "Quote 2"],
            questions_raised=["Q1", "Q2"],
            extracted_entities=["Entity1"],
            extracted_concepts=["Concept1"],
        )
        assert page.authors == ["Author A", "Author B"]
        assert page.publication_date == "2024-01"
        assert len(page.key_claims) == 1
        assert page.extracted_entities == ["Entity1"]

    def test_source_page_to_frontmatter_dict(self):
        """SourcePage converts to frontmatter dict."""
        meta = PageMeta(title="Test", page_id="sources/test", page_type=PageType.SOURCE)
        page = SourcePage(
            meta=meta,
            source_path="raw/test.md",
            source_hash="sha256:abc",
            source_type=SourceType.PAPER,
            authors=["John Doe"],
        )
        d = page.to_frontmatter_dict()

        assert d["title"] == "Test"
        assert d["source_path"] == "raw/test.md"
        assert d["source_hash"] == "sha256:abc"
        assert d["source_type"] == "paper"
        assert d["authors"] == ["John Doe"]


class TestEntityPage:
    """Test EntityPage dataclass."""

    def test_create_entity_page(self):
        """Create EntityPage with required fields."""
        meta = PageMeta(
            title="John Doe",
            page_id="entities/john_doe",
            page_type=PageType.ENTITY,
        )
        page = EntityPage(meta=meta)
        assert page.meta.title == "John Doe"
        assert page.entity_type == EntityType.PERSON

    def test_entity_page_post_init_sets_type(self):
        """EntityPage __post_init__ sets page_type to ENTITY."""
        meta = PageMeta(
            title="Test",
            page_id="entities/test",
            page_type=PageType.CONCEPT,  # Intentionally wrong
        )
        page = EntityPage(meta=meta)
        assert page.meta.page_type == PageType.ENTITY

    def test_entity_page_with_all_fields(self):
        """Create EntityPage with all fields."""
        meta = PageMeta(title="Test Corp", page_id="entities/test_corp", page_type=PageType.ENTITY)
        page = EntityPage(
            meta=meta,
            entity_type=EntityType.ORGANIZATION,
            aliases=["TC", "TestCorp"],
            external_ids={"linkedin": "testcorp", "website": "testcorp.com"},
            overview="A test corporation.",
            relevance="Important for testing.",
            appearances=[{"source": "src1", "context": "mentioned"}],
            relationships={"founded_by": ["entities/john_doe"]},
        )
        assert page.entity_type == EntityType.ORGANIZATION
        assert page.aliases == ["TC", "TestCorp"]
        assert page.external_ids["linkedin"] == "testcorp"

    def test_entity_page_to_frontmatter_dict(self):
        """EntityPage converts to frontmatter dict."""
        meta = PageMeta(title="Test", page_id="entities/test", page_type=PageType.ENTITY)
        page = EntityPage(
            meta=meta,
            entity_type=EntityType.PLACE,
            aliases=["Alias1"],
        )
        d = page.to_frontmatter_dict()

        assert d["entity_type"] == "place"
        assert d["aliases"] == ["Alias1"]


class TestConceptPage:
    """Test ConceptPage dataclass."""

    def test_create_concept_page(self):
        """Create ConceptPage with required fields."""
        meta = PageMeta(
            title="Machine Learning",
            page_id="concepts/machine_learning",
            page_type=PageType.CONCEPT,
        )
        page = ConceptPage(meta=meta)
        assert page.meta.title == "Machine Learning"
        assert page.concept_type == ConceptType.TECHNIQUE
        assert page.abstraction_level == AbstractionLevel.INTERMEDIATE

    def test_concept_page_post_init_sets_type(self):
        """ConceptPage __post_init__ sets page_type to CONCEPT."""
        meta = PageMeta(
            title="Test",
            page_id="concepts/test",
            page_type=PageType.SOURCE,  # Intentionally wrong
        )
        page = ConceptPage(meta=meta)
        assert page.meta.page_type == PageType.CONCEPT

    def test_concept_page_with_all_fields(self):
        """Create ConceptPage with all fields."""
        meta = PageMeta(title="Test", page_id="concepts/test", page_type=PageType.CONCEPT)
        page = ConceptPage(
            meta=meta,
            concept_type=ConceptType.THEORY,
            abstraction_level=AbstractionLevel.ADVANCED,
            definition="A test concept definition.",
            key_properties=["Prop1", "Prop2"],
            how_it_works="Explanation of how it works.",
            concept_relationships={"depends_on": ["concepts/other"]},
            claims_across_sources=[{"claim": "C1", "source": "S1", "confidence": "high"}],
            contradictions=["contradictions/c1"],
            open_questions=["What is X?"],
        )
        assert page.concept_type == ConceptType.THEORY
        assert page.abstraction_level == AbstractionLevel.ADVANCED
        assert len(page.key_properties) == 2

    def test_concept_page_to_frontmatter_dict(self):
        """ConceptPage converts to frontmatter dict."""
        meta = PageMeta(title="Test", page_id="concepts/test", page_type=PageType.CONCEPT)
        page = ConceptPage(
            meta=meta,
            concept_type=ConceptType.FRAMEWORK,
            abstraction_level=AbstractionLevel.FOUNDATIONAL,
        )
        d = page.to_frontmatter_dict()

        assert d["concept_type"] == "framework"
        assert d["abstraction_level"] == "foundational"


class TestAnalysisPage:
    """Test AnalysisPage dataclass."""

    def test_create_analysis_page(self):
        """Create AnalysisPage with required fields."""
        meta = PageMeta(
            title="Comparison Analysis",
            page_id="analyses/comparison",
            page_type=PageType.ANALYSIS,
        )
        page = AnalysisPage(meta=meta)
        assert page.meta.title == "Comparison Analysis"
        assert page.query == ""
        assert page.methodology == ""

    def test_analysis_page_post_init_sets_type(self):
        """AnalysisPage __post_init__ sets page_type to ANALYSIS."""
        meta = PageMeta(
            title="Test",
            page_id="analyses/test",
            page_type=PageType.ENTITY,  # Intentionally wrong
        )
        page = AnalysisPage(meta=meta)
        assert page.meta.page_type == PageType.ANALYSIS

    def test_analysis_page_with_all_fields(self):
        """Create AnalysisPage with all fields."""
        meta = PageMeta(title="Test", page_id="analyses/test", page_type=PageType.ANALYSIS)
        page = AnalysisPage(
            meta=meta,
            query="What is the best approach?",
            methodology="Systematic review",
            findings="Key findings here.",
            evidence=[{"claim": "C1", "sources": ["S1"], "confidence": "high"}],
            conclusions="Conclusion text.",
            limitations="Some limitations.",
            follow_up_questions=["What next?"],
        )
        assert page.query == "What is the best approach?"
        assert page.methodology == "Systematic review"
        assert len(page.evidence) == 1

    def test_analysis_page_to_frontmatter_dict(self):
        """AnalysisPage converts to frontmatter dict."""
        meta = PageMeta(title="Test", page_id="analyses/test", page_type=PageType.ANALYSIS)
        page = AnalysisPage(meta=meta, query="Test query?")
        d = page.to_frontmatter_dict()

        assert d["query"] == "Test query?"


class TestContradictionPage:
    """Test ContradictionPage dataclass."""

    def test_create_contradiction_page(self):
        """Create ContradictionPage with required fields."""
        meta = PageMeta(
            title="Contradiction A vs B",
            page_id="contradictions/a_vs_b",
            page_type=PageType.CONTRADICTION,
        )
        page = ContradictionPage(meta=meta)
        assert page.meta.title == "Contradiction A vs B"
        assert page.status == ContradictionStatus.UNRESOLVED

    def test_contradiction_page_post_init_sets_type(self):
        """ContradictionPage __post_init__ sets page_type to CONTRADICTION."""
        meta = PageMeta(
            title="Test",
            page_id="contradictions/test",
            page_type=PageType.CONCEPT,  # Intentionally wrong
        )
        page = ContradictionPage(meta=meta)
        assert page.meta.page_type == PageType.CONTRADICTION

    def test_contradiction_page_with_all_fields(self):
        """Create ContradictionPage with all fields."""
        meta = PageMeta(title="Test", page_id="contradictions/test", page_type=PageType.CONTRADICTION)
        page = ContradictionPage(
            meta=meta,
            status=ContradictionStatus.RESOLVED,
            topic="concepts/test_topic",
            sources_involved=["sources/s1", "sources/s2"],
            claim_a={"source": "S1", "claim": "Claim A", "evidence": "Evidence A"},
            claim_b={"source": "S2", "claim": "Claim B", "evidence": "Evidence B"},
            analysis="Analysis of the contradiction.",
            possible_resolutions=["Resolution 1"],
            current_status_explanation="Resolved by X.",
            impact_on_wiki=["concepts/test_topic"],
        )
        assert page.status == ContradictionStatus.RESOLVED
        assert page.topic == "concepts/test_topic"
        assert len(page.sources_involved) == 2

    def test_contradiction_page_to_frontmatter_dict(self):
        """ContradictionPage converts to frontmatter dict."""
        meta = PageMeta(title="Test", page_id="contradictions/test", page_type=PageType.CONTRADICTION)
        page = ContradictionPage(
            meta=meta,
            status=ContradictionStatus.SUPERSEDED,
            topic="concepts/x",
            sources_involved=["s1", "s2"],
        )
        d = page.to_frontmatter_dict()

        assert d["status"] == "superseded"
        assert d["topic"] == "concepts/x"
        assert d["sources_involved"] == ["s1", "s2"]


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_title(self):
        """PageMeta with empty title is allowed (though not recommended)."""
        meta = PageMeta(title="", page_id="test/empty", page_type=PageType.CONCEPT)
        assert meta.title == ""
        d = meta.to_frontmatter_dict()
        assert d["title"] == ""

    def test_special_characters_in_title(self):
        """PageMeta handles special characters in title."""
        meta = PageMeta(
            title="What's the 'best' approach?",
            page_id="test/special",
            page_type=PageType.ANALYSIS,
        )
        d = meta.to_frontmatter_dict()
        assert d["title"] == "What's the 'best' approach?"

    def test_unicode_in_content(self):
        """Hash handles unicode content."""
        hash_val = compute_content_hash("")
        assert hash_val.startswith("sha256:")

    def test_very_long_content_hash(self):
        """Hash handles very long content."""
        long_content = "x" * 1000000  # 1MB of content
        hash_val = compute_content_hash(long_content)
        assert hash_val.startswith("sha256:")
        assert len(hash_val) == 7 + 64

    def test_nested_dict_in_key_claims(self):
        """SourcePage handles nested dicts in key_claims."""
        meta = PageMeta(title="Test", page_id="sources/test", page_type=PageType.SOURCE)
        page = SourcePage(
            meta=meta,
            source_path="raw/test.md",
            source_hash="sha256:xxx",
            key_claims=[
                {
                    "claim": "Main claim",
                    "sub_claims": [
                        {"sub_claim": "Sub 1"},
                        {"sub_claim": "Sub 2"},
                    ],
                }
            ],
        )
        assert len(page.key_claims) == 1
        assert "sub_claims" in page.key_claims[0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
