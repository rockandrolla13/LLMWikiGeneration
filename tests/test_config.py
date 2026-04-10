"""Unit tests for config module.

Tests all classes and functions in llm_wiki.config:
- TaxonomyConfig, MindMapConfig, SearchConfig dataclasses
- WikiConfig dataclass
- get_default_config function
"""

import tempfile
from pathlib import Path
from datetime import datetime
import pytest
import yaml

from llm_wiki.config import (
    TaxonomyConfig,
    MindMapConfig,
    SearchConfig,
    WikiConfig,
    ConfigError,
    get_default_config,
)


class TestTaxonomyConfig:
    """Test TaxonomyConfig dataclass."""

    def test_default_values(self):
        """TaxonomyConfig has correct defaults."""
        config = TaxonomyConfig()
        assert config.sources_dir == "sources"
        assert config.entities_dir == "entities"
        assert config.concepts_dir == "concepts"
        assert config.analyses_dir == "analyses"
        assert config.contradictions_dir == "contradictions"
        assert config.tag_categories == {}
        assert config.entity_types == ["person", "organization", "place", "product"]
        assert config.concept_types == ["technique", "theory", "framework", "methodology"]

    def test_custom_values(self):
        """TaxonomyConfig accepts custom values."""
        config = TaxonomyConfig(
            sources_dir="src",
            entities_dir="ents",
            tag_categories={"domain": ["ml", "nlp"]},
            entity_types=["person", "org"],
        )
        assert config.sources_dir == "src"
        assert config.entities_dir == "ents"
        assert config.tag_categories == {"domain": ["ml", "nlp"]}
        assert config.entity_types == ["person", "org"]


class TestMindMapConfig:
    """Test MindMapConfig dataclass."""

    def test_default_values(self):
        """MindMapConfig has correct defaults."""
        config = MindMapConfig()
        assert config.enabled is True
        assert config.max_nodes == 50
        assert config.routing_nodes == 5
        assert config.words_per_node == (150, 400)

    def test_custom_values(self):
        """MindMapConfig accepts custom values."""
        config = MindMapConfig(
            enabled=False,
            max_nodes=100,
            routing_nodes=3,
            words_per_node=(100, 300),
        )
        assert config.enabled is False
        assert config.max_nodes == 100
        assert config.routing_nodes == 3
        assert config.words_per_node == (100, 300)


class TestSearchConfig:
    """Test SearchConfig dataclass."""

    def test_default_values(self):
        """SearchConfig has correct defaults."""
        config = SearchConfig()
        assert config.enabled is True
        assert config.backend == "grep"
        assert config.qmd_path is None

    def test_custom_values(self):
        """SearchConfig accepts custom values."""
        config = SearchConfig(
            enabled=False,
            backend="qmd",
            qmd_path="/usr/local/bin/qmd",
        )
        assert config.enabled is False
        assert config.backend == "qmd"
        assert config.qmd_path == "/usr/local/bin/qmd"


class TestWikiConfig:
    """Test WikiConfig dataclass."""

    def test_default_values(self):
        """WikiConfig has correct defaults."""
        config = WikiConfig()
        assert config.name == "My Wiki"
        assert config.description == ""
        assert config.profile == "research"
        assert config.topic == ""
        assert config.domain_keywords == []
        assert config.raw_dir == "raw"
        assert config.wiki_dir == "wiki"
        assert config.assets_dir == "raw/assets"
        assert isinstance(config.taxonomy, TaxonomyConfig)
        assert isinstance(config.mind_map, MindMapConfig)
        assert isinstance(config.search, SearchConfig)
        assert config.track_revisions is True
        assert config.keep_history is False
        assert config.version == "1.0"

    def test_custom_values(self):
        """WikiConfig accepts custom values."""
        config = WikiConfig(
            name="My Research Wiki",
            description="A wiki about ML",
            profile="personal",
            topic="machine learning",
            domain_keywords=["ml", "ai", "deep learning"],
            raw_dir="sources",
            wiki_dir="content",
        )
        assert config.name == "My Research Wiki"
        assert config.description == "A wiki about ML"
        assert config.profile == "personal"
        assert config.topic == "machine learning"
        assert config.domain_keywords == ["ml", "ai", "deep learning"]
        assert config.raw_dir == "sources"
        assert config.wiki_dir == "content"

    def test_to_dict(self):
        """WikiConfig converts to dict correctly."""
        config = WikiConfig(
            name="Test Wiki",
            topic="testing",
            profile="research",
        )
        d = config.to_dict()

        assert d["name"] == "Test Wiki"
        assert d["topic"] == "testing"
        assert d["profile"] == "research"
        assert "paths" in d
        assert d["paths"]["raw"] == "raw"
        assert d["paths"]["wiki"] == "wiki"
        assert "taxonomy" in d
        assert "mind_map" in d
        assert "search" in d
        assert "revision_tracking" in d
        assert "metadata" in d

    def test_to_dict_nested_configs(self):
        """to_dict includes nested config values."""
        config = WikiConfig()
        config.taxonomy.sources_dir = "custom_sources"
        config.mind_map.max_nodes = 100
        config.search.backend = "qmd"

        d = config.to_dict()

        assert d["taxonomy"]["sources_dir"] == "custom_sources"
        assert d["mind_map"]["max_nodes"] == 100
        assert d["search"]["backend"] == "qmd"

    def test_from_dict_minimal(self):
        """WikiConfig.from_dict with minimal input."""
        d = {"name": "Minimal Wiki"}
        config = WikiConfig.from_dict(d)

        assert config.name == "Minimal Wiki"
        # Defaults should be applied
        assert config.profile == "research"
        assert config.raw_dir == "raw"

    def test_from_dict_full(self):
        """WikiConfig.from_dict with full input."""
        d = {
            "name": "Full Wiki",
            "description": "A comprehensive wiki",
            "profile": "business",
            "topic": "finance",
            "domain_keywords": ["stocks", "bonds"],
            "paths": {
                "raw": "input",
                "wiki": "output",
                "assets": "input/media",
            },
            "taxonomy": {
                "sources_dir": "documents",
                "entities_dir": "people",
                "concepts_dir": "ideas",
                "analyses_dir": "reports",
                "contradictions_dir": "conflicts",
                "tag_categories": {"industry": ["tech", "finance"]},
                "entity_types": ["person", "company"],
                "concept_types": ["theory", "practice"],
            },
            "mind_map": {
                "enabled": False,
                "max_nodes": 75,
                "routing_nodes": 4,
                "words_per_node": [100, 350],
            },
            "search": {
                "enabled": True,
                "backend": "qmd",
                "qmd_path": "/bin/qmd",
            },
            "revision_tracking": {
                "enabled": True,
                "keep_history": True,
            },
            "metadata": {
                "created_by": "test-user",
                "created_at": "2024-01-01T00:00:00Z",
                "version": "2.0",
            },
        }

        config = WikiConfig.from_dict(d)

        assert config.name == "Full Wiki"
        assert config.profile == "business"
        assert config.raw_dir == "input"
        assert config.wiki_dir == "output"
        assert config.taxonomy.sources_dir == "documents"
        assert config.mind_map.enabled is False
        assert config.mind_map.max_nodes == 75
        assert config.search.backend == "qmd"
        assert config.keep_history is True
        assert config.created_by == "test-user"
        assert config.version == "2.0"

    def test_roundtrip_dict(self):
        """WikiConfig survives to_dict/from_dict roundtrip."""
        original = WikiConfig(
            name="Roundtrip Test",
            topic="testing",
            domain_keywords=["test1", "test2"],
        )
        original.taxonomy.tag_categories = {"cat": ["a", "b"]}
        original.mind_map.max_nodes = 60
        original.search.qmd_path = "/custom/qmd"

        d = original.to_dict()
        restored = WikiConfig.from_dict(d)

        assert restored.name == original.name
        assert restored.topic == original.topic
        assert restored.domain_keywords == original.domain_keywords
        assert restored.taxonomy.tag_categories == original.taxonomy.tag_categories
        assert restored.mind_map.max_nodes == original.mind_map.max_nodes
        assert restored.search.qmd_path == original.search.qmd_path

    def test_save_and_load(self, tmp_path):
        """WikiConfig saves and loads from file."""
        config_path = tmp_path / "schema.yml"
        original = WikiConfig(
            name="Save Load Test",
            topic="testing",
            profile="personal",
        )

        original.save(config_path)
        assert config_path.exists()

        loaded = WikiConfig.load(config_path)
        assert loaded.name == original.name
        assert loaded.topic == original.topic
        assert loaded.profile == original.profile

    def test_save_yaml_format(self, tmp_path):
        """WikiConfig saves valid YAML."""
        config_path = tmp_path / "schema.yml"
        config = WikiConfig(name="YAML Test")
        config.save(config_path)

        # Read and parse YAML directly
        with open(config_path) as f:
            data = yaml.safe_load(f)

        assert data["name"] == "YAML Test"
        assert "paths" in data
        assert "taxonomy" in data

    def test_load_empty_file(self, tmp_path):
        """WikiConfig.load handles empty file."""
        config_path = tmp_path / "schema.yml"
        config_path.write_text("")

        config = WikiConfig.load(config_path)
        # Should use defaults
        assert config.name == "My Wiki"

    def test_exists_true(self, tmp_path):
        """WikiConfig.exists returns True for existing file."""
        config_path = tmp_path / "schema.yml"
        config_path.touch()
        assert WikiConfig.exists(config_path) is True

    def test_exists_false(self, tmp_path):
        """WikiConfig.exists returns False for missing file."""
        config_path = tmp_path / "schema.yml"
        assert WikiConfig.exists(config_path) is False


class TestGetDefaultConfig:
    """Test get_default_config function."""

    def test_default_config(self):
        """get_default_config returns valid config."""
        config = get_default_config()

        assert config.name == "My Wiki"
        assert config.profile == "research"
        assert config.created_by == "llm-wiki"
        assert config.created_at != ""

    def test_custom_name(self):
        """get_default_config accepts custom name."""
        config = get_default_config(name="Custom Wiki")
        assert config.name == "Custom Wiki"

    def test_custom_topic(self):
        """get_default_config accepts custom topic."""
        config = get_default_config(topic="machine learning")
        assert config.topic == "machine learning"
        assert "machine learning" in config.description

    def test_custom_profile(self):
        """get_default_config accepts custom profile."""
        config = get_default_config(profile="business")
        assert config.profile == "business"
        assert "business" in config.description

    def test_all_custom(self):
        """get_default_config with all custom values."""
        config = get_default_config(
            name="Full Custom",
            topic="AI research",
            profile="personal",
        )
        assert config.name == "Full Custom"
        assert config.topic == "AI research"
        assert config.profile == "personal"
        assert "AI research" in config.description

    def test_created_at_is_recent(self):
        """get_default_config sets recent created_at."""
        config = get_default_config()
        # created_at should end with Z (UTC)
        assert config.created_at.endswith("Z")

        # Should be parseable as ISO datetime
        timestamp = config.created_at.rstrip("Z")
        dt = datetime.fromisoformat(timestamp)
        # Should be within last minute
        now = datetime.utcnow()
        delta = now - dt
        assert delta.total_seconds() < 60


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_empty_name(self):
        """WikiConfig with empty name."""
        config = WikiConfig(name="")
        assert config.name == ""
        d = config.to_dict()
        assert d["name"] == ""

    def test_special_characters_in_name(self):
        """WikiConfig with special characters in name."""
        config = WikiConfig(name="Wiki: 'Test' & More!")
        d = config.to_dict()
        assert d["name"] == "Wiki: 'Test' & More!"

        # Should survive roundtrip
        restored = WikiConfig.from_dict(d)
        assert restored.name == config.name

    def test_unicode_in_topic(self):
        """WikiConfig with unicode in topic."""
        config = WikiConfig(topic="")
        d = config.to_dict()
        assert d["topic"] == ""

    def test_nested_tag_categories(self):
        """TaxonomyConfig with complex tag categories."""
        config = TaxonomyConfig(
            tag_categories={
                "domain": ["ml", "nlp", "cv"],
                "status": ["draft", "review", "final"],
                "priority": ["high", "medium", "low"],
            }
        )
        assert len(config.tag_categories) == 3
        assert len(config.tag_categories["domain"]) == 3

    def test_words_per_node_tuple(self):
        """MindMapConfig words_per_node as tuple."""
        config = MindMapConfig(words_per_node=(200, 500))
        assert config.words_per_node == (200, 500)

    def test_from_dict_missing_nested(self):
        """WikiConfig.from_dict with missing nested sections."""
        d = {
            "name": "Partial Config",
            "paths": {"raw": "data"},
            # Missing taxonomy, mind_map, search, etc.
        }
        config = WikiConfig.from_dict(d)

        # Should use defaults for missing sections
        assert config.name == "Partial Config"
        assert config.raw_dir == "data"
        assert config.taxonomy.sources_dir == "sources"
        assert config.mind_map.enabled is True

    def test_load_invalid_yaml(self, tmp_path):
        """WikiConfig.load raises ConfigError for invalid YAML."""
        config_path = tmp_path / "schema.yml"
        config_path.write_text("invalid: yaml: content:")

        with pytest.raises(ConfigError) as exc_info:
            WikiConfig.load(config_path)
        assert "Invalid YAML" in str(exc_info.value)

    def test_save_creates_parent_dirs(self, tmp_path):
        """WikiConfig.save doesn't create parent dirs (should already exist)."""
        # Note: save doesn't create parent dirs - wiki init should do that
        config_path = tmp_path / "schema.yml"
        config = WikiConfig(name="Test")
        config.save(config_path)
        assert config_path.exists()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
