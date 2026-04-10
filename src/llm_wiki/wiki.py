"""Core Wiki class for LLM Wiki.

The Wiki class is the main entry point for all wiki operations.
It coordinates between config, manifest, and page operations.
"""

from datetime import datetime
from pathlib import Path
from typing import Optional, Iterator
import os

from .config import WikiConfig, get_default_config
from .manifest import (
    Manifest,
    ManifestEntry,
    OperationType,
    OperationStatus,
    OperationInputs,
    OperationOutputs,
    Actor,
)
from .frontmatter import (
    parse_page,
    write_page,
    compute_file_hash,
    page_id_to_path,
    path_to_page_id,
    extract_wikilinks,
)
from .schemas import (
    PageType,
    PageMeta,
    SourcePage,
    EntityPage,
    ConceptPage,
    AnalysisPage,
    ContradictionPage,
    SourceType,
)


class Wiki:
    """Main interface for wiki operations.

    Coordinates between configuration, manifest, and page operations.
    All wiki mutations go through this class to ensure consistency.
    """

    def __init__(self, root_dir: Path):
        """Initialize wiki at given root directory.

        Args:
            root_dir: Path to wiki root (contains schema.yml, raw/, wiki/)
        """
        self.root = root_dir
        self._config: Optional[WikiConfig] = None
        self._manifest: Optional[Manifest] = None

    @property
    def config_path(self) -> Path:
        """Path to schema.yml configuration file."""
        return self.root / "schema.yml"

    @property
    def manifest_path(self) -> Path:
        """Path to manifest.jsonl operation ledger."""
        return self.root / "manifest.jsonl"

    @property
    def raw_dir(self) -> Path:
        """Path to raw sources directory."""
        return self.root / (self.config.raw_dir if self._config else "raw")

    @property
    def wiki_dir(self) -> Path:
        """Path to wiki content directory."""
        return self.root / (self.config.wiki_dir if self._config else "wiki")

    @property
    def assets_dir(self) -> Path:
        """Path to assets directory."""
        return self.root / (self.config.assets_dir if self._config else "raw/assets")

    @property
    def config(self) -> WikiConfig:
        """Get wiki configuration (lazy loaded)."""
        if self._config is None:
            if self.config_path.exists():
                self._config = WikiConfig.load(self.config_path)
            else:
                raise FileNotFoundError(
                    f"Wiki not initialized. Run init() first. "
                    f"Expected config at {self.config_path}"
                )
        return self._config

    @property
    def manifest(self) -> Manifest:
        """Get manifest (lazy loaded)."""
        if self._manifest is None:
            self._manifest = Manifest(self.manifest_path)
        return self._manifest

    def exists(self) -> bool:
        """Check if wiki is initialized."""
        return self.config_path.exists() and self.manifest_path.exists()

    def init(
        self,
        name: str = "My Wiki",
        topic: str = "",
        profile: str = "research",
    ) -> ManifestEntry:
        """Initialize a new wiki.

        Creates the directory structure, configuration, and initial manifest.

        Args:
            name: Wiki name
            topic: Topic focus
            profile: Wiki profile (research, reading, personal, business)

        Returns:
            ManifestEntry for the init operation

        Raises:
            FileExistsError: If wiki already exists
        """
        if self.exists():
            raise FileExistsError(
                f"Wiki already exists at {self.root}. "
                f"Delete schema.yml and manifest.jsonl to reinitialize."
            )

        # Create directory structure
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / "raw").mkdir(exist_ok=True)
        (self.root / "raw" / "assets").mkdir(exist_ok=True)
        (self.root / "wiki").mkdir(exist_ok=True)
        (self.root / "wiki" / "sources").mkdir(exist_ok=True)
        (self.root / "wiki" / "entities").mkdir(exist_ok=True)
        (self.root / "wiki" / "concepts").mkdir(exist_ok=True)
        (self.root / "wiki" / "analyses").mkdir(exist_ok=True)
        (self.root / "wiki" / "contradictions").mkdir(exist_ok=True)

        # Create configuration
        config = get_default_config(name=name, topic=topic, profile=profile)
        config.save(self.config_path)
        self._config = config

        # Create manifest with init operation
        entry = ManifestEntry.create(
            op_type=OperationType.INIT,
            actor=Actor.SYSTEM,
            inputs=OperationInputs(profile=profile, topic=topic),
        )
        entry.outputs = OperationOutputs(
            created_pages=[],
            extra={"created_files": ["schema.yml"]},
        )
        entry.status = OperationStatus.COMPLETED

        # Initialize manifest
        self._manifest = Manifest(self.manifest_path)
        self.manifest.append(entry)

        # Create initial index.md
        self._create_index()

        # Create initial log.md
        self._create_log(entry)

        return entry

    def _create_index(self) -> None:
        """Create the initial wiki/index.md file."""
        content = f"""# {self.config.name}

Master catalog of all pages in this wiki.

## Sources
*Summary pages for ingested source documents.*

(No sources ingested yet)

## Entities
*People, organizations, places.*

(No entities yet)

## Concepts
*Ideas, themes, topics.*

(No concepts yet)

## Analyses
*Comparisons, syntheses, query answers.*

(No analyses yet)

## Contradictions
*Disagreements between sources.*

(No contradictions yet)

---

**Stats**
- Total sources: 0
- Total pages: 0
- Last updated: {datetime.utcnow().strftime('%Y-%m-%d')}
"""
        index_path = self.wiki_dir / "index.md"
        metadata = {
            "title": "Wiki Index",
            "page_type": "index",
            "created": datetime.utcnow().isoformat() + "Z",
            "updated": datetime.utcnow().isoformat() + "Z",
        }
        write_page(index_path, metadata, content)

    def _create_log(self, init_entry: ManifestEntry) -> None:
        """Create the initial wiki/log.md file."""
        date = datetime.utcnow().strftime("%Y-%m-%d")
        content = f"""# Wiki Log

Chronological record of wiki operations.

---

## [{date}] init | Wiki initialized

Created initial wiki structure:
- `raw/` directory for source documents
- `raw/assets/` for images and attachments
- `wiki/` directory for generated content
- `wiki/index.md` master catalog
- `wiki/log.md` this log file
- `schema.yml` configuration

Operation ID: {init_entry.op_id}

Ready to ingest sources.
"""
        log_path = self.wiki_dir / "log.md"
        metadata = {
            "title": "Wiki Log",
            "page_type": "log",
            "created": datetime.utcnow().isoformat() + "Z",
            "updated": datetime.utcnow().isoformat() + "Z",
        }
        write_page(log_path, metadata, content)

    def get_page_dir(self, page_type: PageType) -> Path:
        """Get the directory for a given page type.

        Args:
            page_type: Type of page

        Returns:
            Path to the directory
        """
        type_to_dir = {
            PageType.SOURCE: self.config.taxonomy.sources_dir,
            PageType.ENTITY: self.config.taxonomy.entities_dir,
            PageType.CONCEPT: self.config.taxonomy.concepts_dir,
            PageType.ANALYSIS: self.config.taxonomy.analyses_dir,
            PageType.CONTRADICTION: self.config.taxonomy.contradictions_dir,
        }
        return self.wiki_dir / type_to_dir[page_type]

    def list_pages(self, page_type: Optional[PageType] = None) -> Iterator[Path]:
        """List all wiki pages, optionally filtered by type.

        Args:
            page_type: If provided, only list this type

        Yields:
            Path objects for each page
        """
        if page_type:
            page_dir = self.get_page_dir(page_type)
            if page_dir.exists():
                for p in page_dir.glob("*.md"):
                    yield p
        else:
            for pt in PageType:
                yield from self.list_pages(pt)

    def count_pages(self, page_type: Optional[PageType] = None) -> int:
        """Count wiki pages, optionally filtered by type.

        Args:
            page_type: If provided, only count this type

        Returns:
            Number of pages
        """
        return sum(1 for _ in self.list_pages(page_type))

    def get_page(self, page_id: str) -> tuple[dict, str]:
        """Get a page by its ID.

        Args:
            page_id: Page ID (e.g., "concepts/machine_learning")

        Returns:
            Tuple of (frontmatter, content)

        Raises:
            FileNotFoundError: If page doesn't exist
        """
        path = page_id_to_path(page_id, self.wiki_dir)
        return parse_page(path)

    def page_exists(self, page_id: str) -> bool:
        """Check if a page exists.

        Args:
            page_id: Page ID

        Returns:
            True if page exists
        """
        path = page_id_to_path(page_id, self.wiki_dir)
        return path.exists()

    def get_all_wikilinks(self) -> dict[str, list[str]]:
        """Get all wikilinks from all pages.

        Returns:
            Dict mapping page_id to list of linked page names
        """
        links = {}
        for page_path in self.list_pages():
            page_id = path_to_page_id(page_path, self.wiki_dir)
            _, content = parse_page(page_path)
            links[page_id] = extract_wikilinks(content)
        return links

    def append_to_log(self, entry: ManifestEntry, description: str) -> None:
        """Append an operation entry to log.md.

        Args:
            entry: ManifestEntry to log
            description: Human-readable description
        """
        log_path = self.wiki_dir / "log.md"
        date = datetime.utcnow().strftime("%Y-%m-%d")
        op_type = entry.op_type.value

        log_entry = f"""

---

## [{date}] {op_type} | {description}

Operation ID: {entry.op_id}
Status: {entry.status.value}
"""
        if entry.outputs.created_pages:
            log_entry += f"Created: {', '.join(entry.outputs.created_pages)}\n"
        if entry.outputs.updated_pages:
            log_entry += f"Updated: {', '.join(entry.outputs.updated_pages)}\n"

        # Append to log
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(log_entry)

    def get_stats(self) -> dict:
        """Get wiki statistics.

        Returns:
            Dict with various statistics
        """
        return {
            "total_sources": self.count_pages(PageType.SOURCE),
            "total_entities": self.count_pages(PageType.ENTITY),
            "total_concepts": self.count_pages(PageType.CONCEPT),
            "total_analyses": self.count_pages(PageType.ANALYSIS),
            "total_contradictions": self.count_pages(PageType.CONTRADICTION),
            "total_pages": self.count_pages(),
            "total_operations": self.manifest.count_operations(),
            "total_ingests": self.manifest.count_operations(OperationType.INGEST),
        }
