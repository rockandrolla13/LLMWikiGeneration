"""Search module for LLM Wiki.

Provides search over wiki pages with pluggable backends:
- GrepSearchBackend: Built-in regex search (always available)
- QMDSearchBackend: External QMD tool (optional, hybrid BM25+vector)

The search module is Tier 2 (derived) - the search index can be
rebuilt from Tier 1 wiki pages at any time.
"""

import re
import subprocess
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Iterator
from enum import Enum

from .wiki import Wiki
from .frontmatter import parse_page, extract_wikilinks


class SearchBackendType(Enum):
    """Available search backends."""
    GREP = "grep"
    QMD = "qmd"


@dataclass
class SearchResult:
    """A single search result."""
    page_id: str
    title: str
    path: Path
    score: float  # Higher is better (0-1 normalized)
    snippet: str  # Text snippet with match context
    matches: list[str] = field(default_factory=list)  # Matched terms

    def to_dict(self) -> dict:
        return {
            "page_id": self.page_id,
            "title": self.title,
            "path": str(self.path),
            "score": self.score,
            "snippet": self.snippet,
            "matches": self.matches,
        }


@dataclass
class SearchQuery:
    """A search query with options."""
    text: str
    page_types: list[str] = field(default_factory=list)  # Filter by type
    tags: list[str] = field(default_factory=list)  # Filter by tags
    limit: int = 10
    include_content: bool = True  # Search in content
    include_frontmatter: bool = True  # Search in frontmatter


class SearchBackend(ABC):
    """Abstract base class for search backends."""

    @abstractmethod
    def search(self, wiki: Wiki, query: SearchQuery) -> list[SearchResult]:
        """Execute a search query.

        Args:
            wiki: Wiki instance to search
            query: Search query with options

        Returns:
            List of SearchResult, sorted by score descending
        """
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if this backend is available."""
        pass

    @abstractmethod
    def build_index(self, wiki: Wiki) -> bool:
        """Build/rebuild the search index.

        Args:
            wiki: Wiki instance to index

        Returns:
            True if successful
        """
        pass


class GrepSearchBackend(SearchBackend):
    """Built-in regex-based search backend.

    Always available, no external dependencies.
    Uses simple term matching with TF-based scoring.
    """

    def is_available(self) -> bool:
        return True

    def build_index(self, wiki: Wiki) -> bool:
        # Grep backend doesn't need an index - it searches files directly
        return True

    def search(self, wiki: Wiki, query: SearchQuery) -> list[SearchResult]:
        """Search wiki pages using regex matching."""
        results = []

        # Parse query into terms
        terms = self._parse_query(query.text)
        if not terms:
            return []

        # Build regex pattern (case insensitive)
        pattern = re.compile(
            "|".join(re.escape(term) for term in terms),
            re.IGNORECASE
        )

        # Search each page
        for page_path in wiki.list_pages():
            try:
                result = self._search_page(
                    page_path, wiki, query, terms, pattern
                )
                if result:
                    results.append(result)
            except Exception:
                continue

        # Sort by score descending
        results.sort(key=lambda r: r.score, reverse=True)

        # Apply limit
        return results[:query.limit]

    def _parse_query(self, text: str) -> list[str]:
        """Parse query text into search terms."""
        # Split on whitespace, filter empty
        terms = [t.strip() for t in text.split() if t.strip()]
        # Remove very short terms (except for exact phrases in quotes)
        terms = [t for t in terms if len(t) >= 2]
        return terms

    def _search_page(
        self,
        page_path: Path,
        wiki: Wiki,
        query: SearchQuery,
        terms: list[str],
        pattern: re.Pattern,
    ) -> Optional[SearchResult]:
        """Search a single page for matches."""
        try:
            metadata, content = parse_page(page_path)
        except Exception:
            return None

        # Apply type filter
        if query.page_types:
            page_type = metadata.get("page_type", "")
            if page_type not in query.page_types:
                return None

        # Apply tag filter
        if query.tags:
            page_tags = set(metadata.get("tags", []))
            if not any(tag in page_tags for tag in query.tags):
                return None

        # Build searchable text
        searchable = ""
        if query.include_frontmatter:
            # Include title and tags
            searchable += metadata.get("title", "") + " "
            searchable += " ".join(metadata.get("tags", [])) + " "
        if query.include_content:
            searchable += content

        # Find matches
        matches = pattern.findall(searchable)
        if not matches:
            return None

        # Calculate score (simple TF)
        # More matches = higher score, normalized by document length
        match_count = len(matches)
        doc_length = max(len(searchable.split()), 1)
        score = min(1.0, match_count / (doc_length * 0.1))

        # Boost for title matches
        title = metadata.get("title", "")
        title_matches = pattern.findall(title)
        if title_matches:
            score = min(1.0, score + 0.3)

        # Extract snippet
        snippet = self._extract_snippet(content, pattern, max_length=200)

        # Get page_id
        page_id = metadata.get(
            "page_id",
            str(page_path.relative_to(wiki.wiki_dir).with_suffix(""))
        )

        return SearchResult(
            page_id=page_id,
            title=metadata.get("title", page_path.stem),
            path=page_path,
            score=round(score, 3),
            snippet=snippet,
            matches=list(set(m.lower() for m in matches)),
        )

    def _extract_snippet(
        self,
        content: str,
        pattern: re.Pattern,
        max_length: int = 200,
    ) -> str:
        """Extract a text snippet around the first match."""
        match = pattern.search(content)
        if not match:
            # Return start of content if no match
            return content[:max_length].strip() + "..."

        # Get context around match
        start = max(0, match.start() - 50)
        end = min(len(content), match.end() + 150)

        snippet = content[start:end].strip()

        # Clean up
        snippet = re.sub(r'\s+', ' ', snippet)
        snippet = re.sub(r'^[^\w]*', '', snippet)  # Remove leading punctuation

        if start > 0:
            snippet = "..." + snippet
        if end < len(content):
            snippet = snippet + "..."

        return snippet[:max_length]


class QMDSearchBackend(SearchBackend):
    """QMD-based search backend (optional).

    Uses QMD for hybrid BM25 + vector search.
    Requires QMD to be installed and configured.
    """

    def __init__(self, qmd_path: Optional[str] = None):
        self.qmd_path = qmd_path or "qmd"

    def is_available(self) -> bool:
        """Check if QMD is installed."""
        try:
            result = subprocess.run(
                [self.qmd_path, "--version"],
                capture_output=True,
                timeout=5,
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False

    def build_index(self, wiki: Wiki) -> bool:
        """Build QMD search index."""
        if not self.is_available():
            return False

        try:
            # QMD index command (adjust based on actual QMD CLI)
            result = subprocess.run(
                [self.qmd_path, "index", str(wiki.wiki_dir)],
                capture_output=True,
                timeout=300,
            )
            return result.returncode == 0
        except Exception:
            return False

    def search(self, wiki: Wiki, query: SearchQuery) -> list[SearchResult]:
        """Search using QMD."""
        if not self.is_available():
            return []

        try:
            # QMD search command (adjust based on actual QMD CLI)
            cmd = [
                self.qmd_path, "search",
                "--limit", str(query.limit),
                "--json",
                query.text,
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                timeout=30,
                cwd=wiki.wiki_dir,
            )

            if result.returncode != 0:
                return []

            # Parse JSON output (adjust based on actual QMD output format)
            import json
            data = json.loads(result.stdout)

            results = []
            for item in data.get("results", []):
                results.append(SearchResult(
                    page_id=item.get("id", ""),
                    title=item.get("title", ""),
                    path=Path(item.get("path", "")),
                    score=item.get("score", 0.0),
                    snippet=item.get("snippet", ""),
                    matches=item.get("matches", []),
                ))

            return results

        except Exception:
            return []


def get_search_backend(wiki: Wiki) -> SearchBackend:
    """Get the appropriate search backend based on configuration.

    Args:
        wiki: Wiki instance

    Returns:
        SearchBackend instance
    """
    config = wiki.config.search

    if not config.enabled:
        # Return grep backend even if disabled (always available)
        return GrepSearchBackend()

    if config.backend == "qmd":
        qmd = QMDSearchBackend(config.qmd_path)
        if qmd.is_available():
            return qmd
        # Fall back to grep if QMD not available

    return GrepSearchBackend()


def search_wiki(
    wiki: Wiki,
    query: str,
    page_types: Optional[list[str]] = None,
    tags: Optional[list[str]] = None,
    limit: int = 10,
) -> list[SearchResult]:
    """Search the wiki for pages matching the query.

    This is the main search entry point. It automatically
    selects the best available backend.

    Args:
        wiki: Wiki instance
        query: Search query text
        page_types: Optional list of page types to filter
        tags: Optional list of tags to filter
        limit: Maximum number of results

    Returns:
        List of SearchResult sorted by relevance
    """
    backend = get_search_backend(wiki)

    search_query = SearchQuery(
        text=query,
        page_types=page_types or [],
        tags=tags or [],
        limit=limit,
    )

    return backend.search(wiki, search_query)


def search_by_link(wiki: Wiki, page_id: str) -> list[SearchResult]:
    """Find all pages that link to a given page.

    Args:
        wiki: Wiki instance
        page_id: Page ID to find links to

    Returns:
        List of pages that link to the given page
    """
    results = []

    # Get the title of the target page
    try:
        metadata, _ = wiki.get_page(page_id)
        target_title = metadata.get("title", "")
    except FileNotFoundError:
        target_title = page_id.split("/")[-1]

    # Search all pages for wikilinks to this page
    for page_path in wiki.list_pages():
        try:
            metadata, content = parse_page(page_path)
            links = extract_wikilinks(content)

            # Check if any link matches the target
            if target_title in links or page_id in links:
                current_id = metadata.get(
                    "page_id",
                    str(page_path.relative_to(wiki.wiki_dir).with_suffix(""))
                )

                results.append(SearchResult(
                    page_id=current_id,
                    title=metadata.get("title", page_path.stem),
                    path=page_path,
                    score=1.0,
                    snippet=f"Links to [[{target_title}]]",
                    matches=[target_title],
                ))
        except Exception:
            continue

    return results
