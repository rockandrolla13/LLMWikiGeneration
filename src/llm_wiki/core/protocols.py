"""Protocol definitions for LLM Wiki extensibility.

Defines contracts for pluggable components:
- VerificationCheck: Pluggable verification checks
- DerivedArtifactCompiler: Pluggable derived artifact compilers
- PageFactory: Pluggable page object factories

These protocols enable the registry pattern for extensibility.
"""

from typing import Protocol, TypeVar, Generic, TYPE_CHECKING
from pathlib import Path
from dataclasses import dataclass

if TYPE_CHECKING:
    from ..verify import VerificationResult


class VerificationCheck(Protocol):
    """Contract for pluggable verification checks.

    Verification checks examine wiki state and report issues.
    Each check has a name and an execute method that returns results.

    Example implementation:
        class FrontmatterCheck:
            @property
            def name(self) -> str:
                return "Page Frontmatter"

            def execute(self, wiki: Wiki) -> VerificationResult:
                # Check logic here
                return VerificationResult(...)
    """

    @property
    def name(self) -> str:
        """Human-readable check name for reports."""
        ...

    def execute(self, wiki: "Wiki") -> "VerificationResult":
        """Run the check and return result.

        Args:
            wiki: Wiki instance to verify

        Returns:
            VerificationResult with pass/fail status and details
        """
        ...


class DerivedArtifactCompiler(Protocol):
    """Contract for pluggable derived artifact compilers.

    Derived artifacts are Tier 2 files generated from Tier 1 data.
    Each compiler knows its artifact name, path, and how to compile content.

    Example implementation:
        class IndexCompiler:
            @property
            def name(self) -> str:
                return "index.md"

            def path(self, wiki: Wiki) -> Path:
                return wiki.wiki_dir / "index.md"

            def compile(self, wiki: Wiki) -> str:
                # Generate index content
                return "# Index\\n..."

            @property
            def needs_frontmatter(self) -> bool:
                return True
    """

    @property
    def name(self) -> str:
        """Artifact filename (e.g., 'index.md')."""
        ...

    def path(self, wiki: "Wiki") -> Path:
        """Full path where artifact should be written.

        Args:
            wiki: Wiki instance for path resolution

        Returns:
            Absolute path to the artifact file
        """
        ...

    def compile(self, wiki: "Wiki") -> str:
        """Generate artifact content.

        Args:
            wiki: Wiki instance to compile from

        Returns:
            Generated content as string
        """
        ...

    @property
    def needs_frontmatter(self) -> bool:
        """Whether to wrap content in YAML frontmatter.

        Returns:
            True if artifact should have frontmatter, False otherwise
        """
        ...


class PageFactory(Protocol):
    """Contract for page object factories.

    Factories encapsulate page construction with consistent defaults.
    This eliminates scattered object construction in commands.py.

    Example implementation:
        class SourcePageFactory:
            def create(
                self,
                title: str,
                source_path: str,
                source_hash: str,
                **kwargs
            ) -> SourcePage:
                meta = PageMeta(
                    title=title,
                    page_id=f"sources/{normalize_page_id(title)}",
                    page_type=PageType.SOURCE,
                    # ... consistent defaults
                )
                return SourcePage(meta=meta, source_path=source_path, ...)
    """

    def create(self, **kwargs) -> "PageMeta":
        """Create a page with consistent defaults.

        Args:
            **kwargs: Page-specific parameters

        Returns:
            Constructed page object
        """
        ...


# Generic Registry type for type-safe registries
T = TypeVar("T")


class Registry(Generic[T]):
    """Generic registry for pluggable components.

    Provides a simple key-value store for registering and retrieving
    components by name. Used for verification checks, artifact compilers, etc.

    Example usage:
        checks = Registry[VerificationCheck]()
        checks.register("frontmatter", FrontmatterCheck())

        for check in checks.all():
            result = check.execute(wiki)
    """

    def __init__(self) -> None:
        self._items: dict[str, T] = {}

    def register(self, name: str, item: T) -> None:
        """Register a component by name.

        Args:
            name: Unique identifier for the component
            item: Component instance to register

        Raises:
            ValueError: If name is already registered
        """
        if name in self._items:
            raise ValueError(f"Component already registered: {name}")
        self._items[name] = item

    def get(self, name: str) -> T:
        """Get a registered component by name.

        Args:
            name: Component identifier

        Returns:
            Registered component

        Raises:
            KeyError: If name is not registered
        """
        if name not in self._items:
            raise KeyError(f"Component not registered: {name}")
        return self._items[name]

    def all(self) -> list[T]:
        """Get all registered components.

        Returns:
            List of all registered components in registration order
        """
        return list(self._items.values())

    def names(self) -> list[str]:
        """Get all registered component names.

        Returns:
            List of registered names
        """
        return list(self._items.keys())

    def __contains__(self, name: str) -> bool:
        """Check if a name is registered."""
        return name in self._items

    def __len__(self) -> int:
        """Return number of registered components."""
        return len(self._items)


# Type aliases for specific registries
VerificationRegistry = Registry[VerificationCheck]
ArtifactRegistry = Registry[DerivedArtifactCompiler]
