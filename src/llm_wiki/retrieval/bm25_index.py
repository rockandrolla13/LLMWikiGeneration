"""
BM25 search index over wiki chunks.

Usage
-----
# Build and save
idx = BM25WikiIndex.build(Path("wiki"), Path(".index/bm25"))

# Load
idx = BM25WikiIndex.load(Path(".index/bm25"))

# Or build-if-missing, otherwise load
idx = BM25WikiIndex.load_or_build(Path("wiki"), Path(".index/bm25"))

# Query
results = idx.query("conformal prediction", k=5)
"""
from __future__ import annotations

import json
import pickle
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List, Optional

from rank_bm25 import BM25Okapi

# Ensure src importable when run directly
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from llm_wiki.retrieval.chunker import Chunk, chunk_wiki  # noqa: E402


_TOKEN_RE = re.compile(r"[a-z0-9]+")


def _tokenize(text: str) -> List[str]:
    return _TOKEN_RE.findall(text.lower())


@dataclass
class SearchResult:
    page_id: str
    page_title: str
    heading_path: str
    snippet: str
    score: float
    source_citations: List[str]


class BM25WikiIndex:
    """BM25 index over wiki page chunks."""

    def __init__(self, model: BM25Okapi, chunks: List[Chunk]) -> None:
        self._model = model
        self._chunks = chunks

    # ------------------------------------------------------------------
    # Construction
    # ------------------------------------------------------------------

    @classmethod
    def build(
        cls,
        wiki_dir: Path,
        index_dir: Optional[Path] = None,
    ) -> "BM25WikiIndex":
        """Build the index from wiki_dir; optionally persist to index_dir."""
        chunks = chunk_wiki(wiki_dir)
        corpus = [_tokenize(c.text) for c in chunks]
        model = BM25Okapi(corpus)
        instance = cls(model, chunks)
        if index_dir is not None:
            instance.save(index_dir)
        return instance

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self, index_dir: Path) -> None:
        """Persist model (pickle) and chunks (JSON) to index_dir."""
        index_dir = Path(index_dir)
        index_dir.mkdir(parents=True, exist_ok=True)

        with open(index_dir / "bm25_model.pkl", "wb") as fh:
            pickle.dump(self._model, fh)

        chunks_data = [asdict(c) for c in self._chunks]
        with open(index_dir / "chunks.json", "w", encoding="utf-8") as fh:
            json.dump(chunks_data, fh, ensure_ascii=False, indent=2)

    @classmethod
    def load(cls, index_dir: Path) -> "BM25WikiIndex":
        """Load a previously saved index from index_dir.

        Security note: pickle is used here because rank_bm25's BM25Okapi contains
        Python-native numpy arrays and internal state that have no safe JSON
        representation.  The pickle file is written only by *this module* into a
        local .index/ directory that is never exposed to external input — callers
        must not pass user-controlled paths to this method.  The chunk metadata is
        stored separately as plain JSON and is loaded without pickle.
        """
        index_dir = Path(index_dir)

        # Safe: we only load a file we wrote ourselves (see save()); never load
        # pickle from an untrusted or user-supplied path.
        with open(index_dir / "bm25_model.pkl", "rb") as fh:
            model: BM25Okapi = pickle.load(fh)

        with open(index_dir / "chunks.json", encoding="utf-8") as fh:
            chunks_data = json.load(fh)

        chunks = [Chunk(**d) for d in chunks_data]
        return cls(model, chunks)

    @classmethod
    def load_or_build(
        cls,
        wiki_dir: Path,
        index_dir: Path,
    ) -> "BM25WikiIndex":
        """Load saved index if it exists; otherwise build (and save) it."""
        index_dir = Path(index_dir)
        model_path = index_dir / "bm25_model.pkl"
        chunks_path = index_dir / "chunks.json"
        if model_path.exists() and chunks_path.exists():
            return cls.load(index_dir)
        return cls.build(wiki_dir, index_dir)

    # ------------------------------------------------------------------
    # Query
    # ------------------------------------------------------------------

    def query(self, text: str, k: int = 5) -> List[SearchResult]:
        """Return the top-k chunks matching *text*, ranked by BM25 score."""
        tokens = _tokenize(text)
        scores = self._model.get_scores(tokens)

        # Pair with chunks and sort descending
        ranked = sorted(
            zip(scores, self._chunks),
            key=lambda t: t[0],
            reverse=True,
        )

        results: List[SearchResult] = []
        for score, chunk in ranked[:k]:
            snippet = chunk.text[:300].replace("\n", " ").strip()
            results.append(
                SearchResult(
                    page_id=chunk.page_id,
                    page_title=chunk.page_title,
                    heading_path=chunk.heading_path,
                    snippet=snippet,
                    score=float(score),
                    source_citations=chunk.source_citations,
                )
            )
        return results
