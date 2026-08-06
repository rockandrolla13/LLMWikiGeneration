"""LLM Wiki - LLM-maintained personal knowledge base."""

__version__ = "0.1.0"

from .wiki import Wiki
from .config import WikiConfig, ConfigError, get_default_config
from .manifest import (
    Manifest,
    ManifestEntry,
    OperationType,
    OperationStatus,
    Actor,
)
from .schemas import (
    PageType,
    PageMeta,
    SourcePage,
    EntityPage,
    ConceptPage,
    AnalysisPage,
    ContradictionPage,
)
from .commands import (
    wiki_init,
    wiki_ingest,
    wiki_stats,
    wiki_rebuild,
    wiki_freshness,
    wiki_query,
    wiki_find_links,
    # Session commands (Tier 3 - Ephemeral)
    wiki_session_start,
    wiki_session_end,
    wiki_session_status,
    wiki_session_log_navigation,
    wiki_session_log_query,
    wiki_session_set_context,
    # Help and guidance
    wiki_help,
    wiki_guide,
    wiki_structure,
)
from .io import (
    parse_page,
    write_page,
    compute_content_hash,
    compute_file_hash,
    extract_wikilinks,
    normalize_page_id,
    is_generated,
    # Duplicate detection
    DuplicateCheckResult,
    check_duplicate,
    format_duplicate_result,
)
from .derived import (
    compile_index,
    compile_mind_map,
    check_freshness,
    rebuild_derived,
)
from .search import (
    SearchResult,
    SearchQuery,
    search_wiki,
    search_by_link,
    get_search_backend,
)
from .session import (
    SessionContext,
    SessionStatus,
    NavigationEntry,
    QueryEntry,
    OperationEntry,
    OperationKind,
    get_current_session,
    set_current_session,
    create_session,
    save_session_to_temp,
    load_session_from_temp,
    list_temp_sessions,
    cleanup_temp_sessions,
)
from .verify import verify_wiki, VerificationResult, VerificationReport
# Integrations (optional backends)
from .integrations import (
    is_omega_available,
    store_wiki_event,
    get_wiki_briefing,
    store_lesson,
    query_wiki_history,
    checkpoint_task,
    resume_task,
)

__all__ = [
    # Core
    "Wiki",
    "WikiConfig",
    "ConfigError",
    "get_default_config",
    # Manifest
    "Manifest",
    "ManifestEntry",
    "OperationType",
    "OperationStatus",
    "Actor",
    # Schemas
    "PageType",
    "PageMeta",
    "SourcePage",
    "EntityPage",
    "ConceptPage",
    "AnalysisPage",
    "ContradictionPage",
    # Commands
    "wiki_init",
    "wiki_ingest",
    "wiki_stats",
    "wiki_rebuild",
    "wiki_freshness",
    "wiki_query",
    "wiki_find_links",
    # Session commands (Tier 3 - Ephemeral)
    "wiki_session_start",
    "wiki_session_end",
    "wiki_session_status",
    "wiki_session_log_navigation",
    "wiki_session_log_query",
    "wiki_session_set_context",
    # Help and guidance
    "wiki_help",
    "wiki_guide",
    "wiki_structure",
    # Derived artifacts
    "compile_index",
    "compile_mind_map",
    "check_freshness",
    "rebuild_derived",
    # Search
    "SearchResult",
    "SearchQuery",
    "search_wiki",
    "search_by_link",
    "get_search_backend",
    # Session (Tier 3 - Ephemeral)
    "SessionContext",
    "SessionStatus",
    "NavigationEntry",
    "QueryEntry",
    "OperationEntry",
    "OperationKind",
    "get_current_session",
    "set_current_session",
    "create_session",
    "save_session_to_temp",
    "load_session_from_temp",
    "list_temp_sessions",
    "cleanup_temp_sessions",
    # Utilities
    "parse_page",
    "write_page",
    "compute_content_hash",
    "compute_file_hash",
    "extract_wikilinks",
    "normalize_page_id",
    "is_generated",
    # Duplicate Detection
    "DuplicateCheckResult",
    "check_duplicate",
    "format_duplicate_result",
    # Verification
    "verify_wiki",
    "VerificationResult",
    "VerificationReport",
    # Integrations (OMEGA)
    "is_omega_available",
    "store_wiki_event",
    "get_wiki_briefing",
    "store_lesson",
    "query_wiki_history",
    "checkpoint_task",
    "resume_task",
]
