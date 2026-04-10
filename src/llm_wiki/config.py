"""Wiki configuration (schema.yml) for LLM Wiki.

The schema.yml file defines the wiki's profile, taxonomy, and settings.
It's a Tier 1 canonical artifact that controls how the wiki operates.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
import logging
import yaml

logger = logging.getLogger(__name__)


class ConfigError(Exception):
    """Raised when wiki configuration is invalid.

    This indicates that a config file exists but cannot be parsed
    (invalid YAML) or contains invalid values (schema validation failed).
    """

    pass


@dataclass
class TaxonomyConfig:
    """Taxonomy configuration for organizing wiki content."""
    # Page type directories
    sources_dir: str = "sources"
    entities_dir: str = "entities"
    concepts_dir: str = "concepts"
    analyses_dir: str = "analyses"
    contradictions_dir: str = "contradictions"

    # Tag categories (for organization)
    tag_categories: dict[str, list[str]] = field(default_factory=dict)

    # Entity type mappings
    entity_types: list[str] = field(default_factory=lambda: [
        "person", "organization", "place", "product"
    ])

    # Concept type mappings
    concept_types: list[str] = field(default_factory=lambda: [
        "technique", "theory", "framework", "methodology"
    ])


@dataclass
class MindMapConfig:
    """Configuration for MIND_MAP.md generation."""
    enabled: bool = True
    max_nodes: int = 50
    routing_nodes: int = 5  # Number of hub nodes [1-5]
    words_per_node: tuple[int, int] = (150, 400)  # min, max


@dataclass
class SearchConfig:
    """Configuration for search functionality."""
    enabled: bool = True
    backend: str = "grep"  # "grep" (built-in) or "qmd" (external)
    qmd_path: Optional[str] = None


@dataclass
class WikiConfig:
    """Top-level wiki configuration.

    This is serialized to/from schema.yml in the wiki root.
    """
    # Wiki identity
    name: str = "My Wiki"
    description: str = ""
    profile: str = "research"  # research | reading | personal | business

    # Topic focus (helps LLM understand context)
    topic: str = ""
    domain_keywords: list[str] = field(default_factory=list)

    # Paths (relative to wiki root)
    raw_dir: str = "raw"
    wiki_dir: str = "wiki"
    assets_dir: str = "raw/assets"

    # Sub-configurations
    taxonomy: TaxonomyConfig = field(default_factory=TaxonomyConfig)
    mind_map: MindMapConfig = field(default_factory=MindMapConfig)
    search: SearchConfig = field(default_factory=SearchConfig)

    # Revision tracking
    track_revisions: bool = True
    keep_history: bool = False  # If True, keep old revisions in .history/

    # Creation metadata
    created_by: str = ""
    created_at: str = ""
    version: str = "1.0"

    def to_dict(self) -> dict:
        """Convert to dictionary for YAML serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "profile": self.profile,
            "topic": self.topic,
            "domain_keywords": self.domain_keywords,
            "paths": {
                "raw": self.raw_dir,
                "wiki": self.wiki_dir,
                "assets": self.assets_dir,
            },
            "taxonomy": {
                "sources_dir": self.taxonomy.sources_dir,
                "entities_dir": self.taxonomy.entities_dir,
                "concepts_dir": self.taxonomy.concepts_dir,
                "analyses_dir": self.taxonomy.analyses_dir,
                "contradictions_dir": self.taxonomy.contradictions_dir,
                "tag_categories": self.taxonomy.tag_categories,
                "entity_types": self.taxonomy.entity_types,
                "concept_types": self.taxonomy.concept_types,
            },
            "mind_map": {
                "enabled": self.mind_map.enabled,
                "max_nodes": self.mind_map.max_nodes,
                "routing_nodes": self.mind_map.routing_nodes,
                "words_per_node": list(self.mind_map.words_per_node),
            },
            "search": {
                "enabled": self.search.enabled,
                "backend": self.search.backend,
                "qmd_path": self.search.qmd_path,
            },
            "revision_tracking": {
                "enabled": self.track_revisions,
                "keep_history": self.keep_history,
            },
            "metadata": {
                "created_by": self.created_by,
                "created_at": self.created_at,
                "version": self.version,
            },
        }

    @classmethod
    def from_dict(cls, d: dict) -> "WikiConfig":
        """Create from dictionary (parsed YAML)."""
        paths = d.get("paths", {})
        taxonomy_d = d.get("taxonomy", {})
        mind_map_d = d.get("mind_map", {})
        search_d = d.get("search", {})
        revision_d = d.get("revision_tracking", {})
        metadata_d = d.get("metadata", {})

        taxonomy = TaxonomyConfig(
            sources_dir=taxonomy_d.get("sources_dir", "sources"),
            entities_dir=taxonomy_d.get("entities_dir", "entities"),
            concepts_dir=taxonomy_d.get("concepts_dir", "concepts"),
            analyses_dir=taxonomy_d.get("analyses_dir", "analyses"),
            contradictions_dir=taxonomy_d.get("contradictions_dir", "contradictions"),
            tag_categories=taxonomy_d.get("tag_categories", {}),
            entity_types=taxonomy_d.get("entity_types", ["person", "organization", "place", "product"]),
            concept_types=taxonomy_d.get("concept_types", ["technique", "theory", "framework", "methodology"]),
        )

        mind_map = MindMapConfig(
            enabled=mind_map_d.get("enabled", True),
            max_nodes=mind_map_d.get("max_nodes", 50),
            routing_nodes=mind_map_d.get("routing_nodes", 5),
            words_per_node=tuple(mind_map_d.get("words_per_node", [150, 400])),
        )

        search = SearchConfig(
            enabled=search_d.get("enabled", True),
            backend=search_d.get("backend", "grep"),
            qmd_path=search_d.get("qmd_path"),
        )

        return cls(
            name=d.get("name", "My Wiki"),
            description=d.get("description", ""),
            profile=d.get("profile", "research"),
            topic=d.get("topic", ""),
            domain_keywords=d.get("domain_keywords", []),
            raw_dir=paths.get("raw", "raw"),
            wiki_dir=paths.get("wiki", "wiki"),
            assets_dir=paths.get("assets", "raw/assets"),
            taxonomy=taxonomy,
            mind_map=mind_map,
            search=search,
            track_revisions=revision_d.get("enabled", True),
            keep_history=revision_d.get("keep_history", False),
            created_by=metadata_d.get("created_by", ""),
            created_at=metadata_d.get("created_at", ""),
            version=metadata_d.get("version", "1.0"),
        )

    def save(self, path: Path) -> None:
        """Save configuration to YAML file.

        Args:
            path: Path to schema.yml file
        """
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(self.to_dict(), f, default_flow_style=False, sort_keys=False)

    @classmethod
    def load(cls, path: Path) -> "WikiConfig":
        """Load configuration from YAML file.

        Args:
            path: Path to schema.yml file

        Returns:
            WikiConfig instance

        Raises:
            ConfigError: If the file contains invalid YAML or invalid config values
            FileNotFoundError: If the file does not exist
        """
        try:
            with open(path, "r", encoding="utf-8") as f:
                d = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ConfigError(
                f"Invalid YAML in config file '{path}': {e}\n"
                f"Please check the syntax of your schema.yml file."
            ) from e

        if d is None:
            # Empty file - use defaults but warn
            logger.warning(
                f"Config file '{path}' is empty; using default configuration"
            )
            d = {}

        try:
            return cls.from_dict(d)
        except (TypeError, ValueError, KeyError) as e:
            raise ConfigError(
                f"Invalid configuration in '{path}': {e}\n"
                f"Please check that all config values have the correct types."
            ) from e

    @classmethod
    def exists(cls, path: Path) -> bool:
        """Check if configuration file exists."""
        return path.exists()


def get_default_config(
    name: str = "My Wiki",
    topic: str = "",
    profile: str = "research",
) -> WikiConfig:
    """Create a default configuration for a new wiki.

    Args:
        name: Wiki name
        topic: Topic focus
        profile: Wiki profile (research, reading, personal, business)

    Returns:
        WikiConfig with sensible defaults
    """
    from datetime import datetime

    return WikiConfig(
        name=name,
        description=f"A {profile} wiki about {topic}" if topic else f"A {profile} wiki",
        profile=profile,
        topic=topic,
        domain_keywords=[],
        created_by="llm-wiki",
        created_at=datetime.utcnow().isoformat() + "Z",
    )
