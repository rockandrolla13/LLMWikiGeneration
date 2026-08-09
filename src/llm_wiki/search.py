"""Search module for LLM Wiki.

Provides search over wiki pages with pluggable backends:
- BM25SearchBackend: Ranked chunk-level retrieval (default when rank_bm25 is
  installed)
- GrepSearchBackend: Built-in regex search (always available, the fallback)
- QMDSearchBackend: External QMD tool (optional, hybrid BM25+vector)

BM25 is the default because it was measured against grep on 40 questions built
from sampled pages (eval/eval_cases.json), each written to avoid its own page's
title words so the test measures retrieval rather than string matching:

    metric        grep    bm25
    recall@1        0%     80%
    recall@5        2%     90%
    recall@10       5%    100%
    MRR          0.009   0.850

Grep scores term frequency per page, so on a natural-language question the
common words ("in", "returns") match almost everything and drown the page that
actually answers it. 38 of 40 gold pages were never returned at all.

Re-run with /wiki-eval after any change here. A change that does not move those
numbers is not an improvement.

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
    BM25 = "bm25"


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


class BM25SearchBackend(SearchBackend):
    """Ranked retrieval over page chunks, via rank_bm25.

    Wraps ``llm_wiki.retrieval.bm25_index.BM25WikiIndex``, which was present but
    unreachable until 2026-08-09: nothing constructed it, and the one documented
    example passed the wrong path. ``chunk_wiki`` appends ``/wiki`` itself, so it
    wants the VAULT ROOT (``wiki/``), not ``wiki.wiki_dir``. Handing it wiki_dir
    yields zero chunks and BM25Okapi then dies on a divide-by-zero computing
    average document length. Passing the root indexes ~10.7k chunks.

    The index is built lazily and cached per vault root. A build over the current
    corpus takes about 1.8s, which is cheap enough that nothing is persisted:
    an on-disk index inside ``wiki/`` would be published by the mkdocs site and
    could go stale against the pages it claims to describe.
    """

    def __init__(self) -> None:
        self._index = None
        self._indexed_root: Optional[Path] = None

    def is_available(self) -> bool:
        try:
            from .retrieval.bm25_index import BM25WikiIndex  # noqa: F401
            return True
        except Exception:
            return False

    def build_index(self, wiki: Wiki) -> bool:
        try:
            from .retrieval.bm25_index import BM25WikiIndex
            self._index = BM25WikiIndex.build(wiki.root)
            self._indexed_root = wiki.root
            return True
        except Exception:
            self._index = None
            self._indexed_root = None
            return False

    def _ensure_index(self, wiki: Wiki) -> bool:
        if self._index is not None and self._indexed_root == wiki.root:
            return True
        return self.build_index(wiki)

    def search(self, wiki: Wiki, query: SearchQuery) -> list[SearchResult]:
        if not query.text.strip() or not self._ensure_index(wiki):
            return []

        # Ask for more chunks than pages wanted: several chunks share a page, and
        # filters may discard some. 6x was enough for every eval case to survive.
        hits = self._index.query(query.text, k=max(query.limit * 6, 30))
        if not hits:
            return []

        terms = [t.lower() for t in query.text.split() if len(t) >= 2]
        top = max(h.score for h in hits) or 1.0

        results: list[SearchResult] = []
        seen: set[str] = set()
        for hit in hits:                      # already score-descending
            if hit.page_id in seen:
                continue
            path = wiki.wiki_dir / f"{hit.page_id}.md"
            if not path.exists():
                continue
            try:
                metadata, _ = parse_page(path)
            except Exception:
                continue

            if query.page_types and metadata.get("page_type", "") not in query.page_types:
                continue
            if query.tags:
                if not set(query.tags) & set(metadata.get("tags", []) or []):
                    continue

            seen.add(hit.page_id)
            snippet = hit.snippet
            results.append(SearchResult(
                page_id=hit.page_id,
                title=hit.page_title or metadata.get("title", hit.page_id),
                path=path,
                score=hit.score / top,        # normalise to 0-1 like other backends
                snippet=snippet,
                matches=[t for t in terms if t in snippet.lower()],
            ))
            if len(results) >= query.limit:
                break
        return results


def get_search_backend(wiki: Wiki) -> SearchBackend:
    """Get the appropriate search backend based on configuration.

    Order: explicit config choice, then BM25 if importable, then grep. Grep is
    the last resort rather than the default because it scored recall@1 of 0% on
    the eval set (see module docstring); it stays as the fallback because it has
    no dependencies and always works.

    Args:
        wiki: Wiki instance

    Returns:
        SearchBackend instance
    """
    config = wiki.config.search

    if not config.enabled:
        # Return grep backend even if disabled (always available)
        return GrepSearchBackend()

    if config.backend == "grep":
        return GrepSearchBackend()

    if config.backend == "qmd":
        qmd = QMDSearchBackend(config.qmd_path)
        if qmd.is_available():
            return qmd
        # Fall back below if QMD not available

    bm25 = BM25SearchBackend()
    if bm25.is_available():
        return bm25

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
