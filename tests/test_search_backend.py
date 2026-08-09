"""Guards for the BM25 search backend.

These exist because BM25WikiIndex was written, tested by nobody, and silently
unreachable for months. Two independent faults kept it that way, and each of
these tests pins one of them.
"""

import pytest

from llm_wiki import Wiki, wiki_init
from llm_wiki.io import write_page
from llm_wiki.search import (
    BM25SearchBackend,
    GrepSearchBackend,
    SearchQuery,
    get_search_backend,
)


@pytest.fixture
def wiki(tmp_path):
    wiki_init(tmp_path, name="Test Wiki")
    w = Wiki(tmp_path)
    write_page(
        w.wiki_dir / "concepts" / "cross-currency-basis.md",
        {"page_id": "concepts/cross-currency-basis",
         "title": "Cross-Currency Basis", "page_type": "concept"},
        "A floating/floating swap where two parties borrow and lend in "
        "different currencies; the basis measures the deviation from covered "
        "interest parity.",
    )
    write_page(
        w.wiki_dir / "concepts" / "layer-normalization.md",
        {"page_id": "concepts/layer-normalization",
         "title": "Layer Normalization", "page_type": "concept"},
        "Rescales activations to zero mean and unit variance across the "
        "feature dimension per sample, stabilising gradients in transformers.",
    )
    return w


class TestChunkerPathContract:
    """chunk_wiki appends '/wiki' itself, so it takes the VAULT ROOT."""

    def test_root_yields_chunks(self, wiki):
        from llm_wiki.retrieval.chunker import chunk_wiki
        assert len(chunk_wiki(wiki.root)) > 0

    def test_wiki_dir_yields_nothing(self, wiki):
        # The original failure. Passing wiki_dir looks right and returns an
        # empty corpus, which then kills BM25Okapi with a ZeroDivisionError on
        # average document length -- far from the actual mistake.
        from llm_wiki.retrieval.chunker import chunk_wiki
        assert chunk_wiki(wiki.wiki_dir) == []

    def test_index_builds_from_root(self, wiki):
        from llm_wiki.retrieval.bm25_index import BM25WikiIndex
        assert BM25WikiIndex.build(wiki.root).query("currencies") != []


class TestBackendSelection:
    def test_bm25_is_default_when_available(self, wiki):
        wiki.config.search.backend = "bm25"
        assert isinstance(get_search_backend(wiki), BM25SearchBackend)

    def test_grep_is_honoured_when_requested(self, wiki):
        # A vault that explicitly asks for grep must keep getting grep --
        # switching the default must not silently override a stated choice.
        wiki.config.search.backend = "grep"
        assert isinstance(get_search_backend(wiki), GrepSearchBackend)

    def test_disabled_search_falls_back_to_grep(self, wiki):
        wiki.config.search.enabled = False
        assert isinstance(get_search_backend(wiki), GrepSearchBackend)


class TestBM25Search:
    def test_finds_page_without_title_words(self, wiki):
        # The property grep lacks: no query term appears in the page title.
        results = BM25SearchBackend().search(
            wiki, SearchQuery(text="covered interest parity deviation", limit=5))
        assert "concepts/cross-currency-basis" in [r.page_id for r in results]

    def test_scores_are_normalised(self, wiki):
        results = BM25SearchBackend().search(
            wiki, SearchQuery(text="activations gradients", limit=5))
        assert results
        assert all(0.0 <= r.score <= 1.0 for r in results)

    def test_page_type_filter_is_applied(self, wiki):
        results = BM25SearchBackend().search(
            wiki, SearchQuery(text="currencies", page_types=["source"], limit=5))
        assert results == []

    def test_empty_query_returns_nothing(self, wiki):
        assert BM25SearchBackend().search(wiki, SearchQuery(text="   ")) == []

    def test_results_are_deduplicated_by_page(self, wiki):
        # query() ranks CHUNKS; several can share a page. The backend collapses
        # them, otherwise one long page fills the whole result list.
        results = BM25SearchBackend().search(
            wiki, SearchQuery(text="swap currencies basis parity", limit=10))
        ids = [r.page_id for r in results]
        assert len(ids) == len(set(ids))
