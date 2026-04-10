"""Wiki commands for LLM Wiki.

Provides high-level operations that can be invoked as skills:
- init: Initialize a new wiki
- ingest: Ingest a source document
- query: Search and answer questions
- lint: Health check the wiki
- rebuild: Regenerate derived artifacts
"""

from datetime import datetime
from pathlib import Path
from typing import Optional
import os

from .wiki import Wiki
from .manifest import (
    ManifestEntry,
    OperationType,
    OperationStatus,
    OperationInputs,
    OperationOutputs,
    Actor,
)
from .frontmatter import (
    write_page,
    compute_file_hash,
    normalize_page_id,
)
from .schemas import (
    PageType,
    PageMeta,
    SourcePage,
    EntityPage,
    ConceptPage,
    SourceType,
    MindMapPriority,
)


def wiki_init(
    root_dir: Path,
    name: str = "My Wiki",
    topic: str = "",
    profile: str = "research",
) -> dict:
    """Initialize a new wiki.

    Creates directory structure, configuration, and manifest.

    Args:
        root_dir: Path to wiki root
        name: Wiki name
        topic: Topic focus (e.g., "transformer architectures")
        profile: Wiki profile (research, reading, personal, business)

    Returns:
        Dict with operation result
    """
    wiki = Wiki(root_dir)

    if wiki.exists():
        return {
            "success": False,
            "error": f"Wiki already exists at {root_dir}",
            "hint": "Delete schema.yml and manifest.jsonl to reinitialize",
        }

    try:
        entry = wiki.init(name=name, topic=topic, profile=profile)
        return {
            "success": True,
            "op_id": entry.op_id,
            "message": f"Wiki '{name}' initialized at {root_dir}",
            "created": [
                "schema.yml",
                "manifest.jsonl",
                "wiki/index.md",
                "wiki/log.md",
                "raw/",
                "wiki/sources/",
                "wiki/entities/",
                "wiki/concepts/",
                "wiki/analyses/",
                "wiki/contradictions/",
            ],
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
        }


def wiki_ingest(
    wiki: Wiki,
    source_path: Path,
    title: Optional[str] = None,
    source_type: str = "article",
    authors: Optional[list[str]] = None,
    summary: str = "",
    key_claims: Optional[list[dict]] = None,
    extracted_entities: Optional[list[str]] = None,
    extracted_concepts: Optional[list[str]] = None,
    tags: Optional[list[str]] = None,
) -> dict:
    """Ingest a source document into the wiki.

    Creates a source page and optionally entity/concept pages.

    Args:
        wiki: Wiki instance
        source_path: Path to source file (relative to raw/)
        title: Page title (defaults to filename)
        source_type: Type of source (paper, article, book, notes, transcript)
        authors: List of author names
        summary: Summary of the source
        key_claims: List of {claim, evidence, confidence} dicts
        extracted_entities: List of entity names to create pages for
        extracted_concepts: List of concept names to create pages for
        tags: List of tags

    Returns:
        Dict with operation result
    """
    # Validate source exists
    full_source_path = wiki.root / source_path
    if not full_source_path.exists():
        return {
            "success": False,
            "error": f"Source not found: {source_path}",
        }

    # Generate page_id from filename
    stem = source_path.stem if hasattr(source_path, 'stem') else Path(source_path).stem
    page_id = f"sources/{normalize_page_id(stem)}"

    # Check if already ingested
    if wiki.page_exists(page_id):
        return {
            "success": False,
            "error": f"Source already ingested: {page_id}",
            "hint": "Use update operation to modify existing pages",
        }

    # Create manifest entry
    source_hash = compute_file_hash(full_source_path)
    entry = ManifestEntry.create(
        op_type=OperationType.INGEST,
        actor=Actor.LLM,
        inputs=OperationInputs(
            source_path=str(source_path),
            source_hash=source_hash,
        ),
    )

    try:
        # Create source page
        now = datetime.utcnow()
        meta = PageMeta(
            title=title or stem,
            page_id=page_id,
            page_type=PageType.SOURCE,
            revision_id=1,
            created=now,
            updated=now,
            updated_by=entry.op_id,
            tags=tags or [],
            sources=[],
            related=[],
            mind_map_priority=MindMapPriority.MEDIUM,
        )

        source_page = SourcePage(
            meta=meta,
            source_path=str(source_path),
            source_hash=source_hash,
            source_type=SourceType(source_type),
            authors=authors or [],
            summary=summary,
            key_claims=key_claims or [],
            extracted_entities=extracted_entities or [],
            extracted_concepts=extracted_concepts or [],
        )

        # Generate markdown content
        content = _generate_source_content(source_page)

        # Write page
        page_path = wiki.wiki_dir / f"{page_id}.md"
        content_hash = write_page(page_path, source_page.to_frontmatter_dict(), content)

        # Update frontmatter with computed hash
        frontmatter = source_page.to_frontmatter_dict()
        frontmatter["revision_hash"] = content_hash

        # Track created pages
        created_pages = [page_id]
        page_revisions = {page_id: 1}

        # Create entity pages if requested
        for entity_name in (extracted_entities or []):
            entity_result = _create_entity_page(
                wiki, entity_name, page_id, entry.op_id
            )
            if entity_result["success"]:
                created_pages.append(entity_result["page_id"])
                page_revisions[entity_result["page_id"]] = 1

        # Create concept pages if requested
        for concept_name in (extracted_concepts or []):
            concept_result = _create_concept_page(
                wiki, concept_name, page_id, entry.op_id
            )
            if concept_result["success"]:
                created_pages.append(concept_result["page_id"])
                page_revisions[concept_result["page_id"]] = 1

        # Complete manifest entry
        entry.outputs = OperationOutputs(
            created_pages=created_pages,
            page_revisions=page_revisions,
            derived_invalidated=["MIND_MAP.md", "index.md"],
        )
        entry.status = OperationStatus.COMPLETED

        # Append to manifest
        wiki.manifest.append(entry)

        # Append to log
        wiki.append_to_log(entry, f"Ingested {title or stem}")

        return {
            "success": True,
            "op_id": entry.op_id,
            "page_id": page_id,
            "created_pages": created_pages,
            "message": f"Ingested '{title or stem}' ({len(created_pages)} pages created)",
        }

    except Exception as e:
        entry.status = OperationStatus.FAILED
        entry.error_message = str(e)
        wiki.manifest.append(entry)
        return {
            "success": False,
            "op_id": entry.op_id,
            "error": str(e),
        }


def _generate_source_content(source: SourcePage) -> str:
    """Generate markdown content for a source page."""
    lines = [f"# {source.meta.title}", ""]

    if source.summary:
        lines.extend(["## Summary", "", source.summary, ""])

    if source.key_claims:
        lines.extend(["## Key Claims", ""])
        for i, claim in enumerate(source.key_claims, 1):
            lines.append(f"{i}. **Claim:** {claim.get('claim', '')}")
            if claim.get('evidence'):
                lines.append(f"   - Evidence: {claim['evidence']}")
            if claim.get('confidence'):
                lines.append(f"   - Confidence: {claim['confidence']}")
            lines.append("")

    if source.authors:
        lines.extend(["## Authors", ""])
        for author in source.authors:
            lines.append(f"- {author}")
        lines.append("")

    if source.extracted_entities:
        lines.extend(["## Extracted Entities", ""])
        for entity in source.extracted_entities:
            lines.append(f"- [[{entity}]]")
        lines.append("")

    if source.extracted_concepts:
        lines.extend(["## Extracted Concepts", ""])
        for concept in source.extracted_concepts:
            lines.append(f"- [[{concept}]]")
        lines.append("")

    lines.extend([
        "## Source",
        "",
        f"- **Path:** `{source.source_path}`",
        f"- **Type:** {source.source_type.value}",
        f"- **Hash:** `{source.source_hash[:20]}...`",
        "",
    ])

    return "\n".join(lines)


def _create_entity_page(
    wiki: Wiki,
    entity_name: str,
    source_page_id: str,
    op_id: str,
) -> dict:
    """Create an entity page for a name mentioned in a source."""
    page_id = f"entities/{normalize_page_id(entity_name)}"

    if wiki.page_exists(page_id):
        return {"success": False, "page_id": page_id, "reason": "already exists"}

    now = datetime.utcnow()
    meta = PageMeta(
        title=entity_name,
        page_id=page_id,
        page_type=PageType.ENTITY,
        revision_id=1,
        created=now,
        updated=now,
        updated_by=op_id,
        sources=[source_page_id],
        mind_map_priority=MindMapPriority.LOW,
    )

    content = f"""# {entity_name}

## Overview

*Entity extracted from [[{source_page_id}]]. Needs expansion.*

## Appearances in Sources

| Source | Context |
|--------|---------|
| [[{source_page_id}]] | Mentioned |
"""

    page_path = wiki.wiki_dir / f"{page_id}.md"
    frontmatter = meta.to_frontmatter_dict()
    content_hash = write_page(page_path, frontmatter, content)

    return {"success": True, "page_id": page_id, "hash": content_hash}


def _create_concept_page(
    wiki: Wiki,
    concept_name: str,
    source_page_id: str,
    op_id: str,
) -> dict:
    """Create a concept page for a topic mentioned in a source."""
    page_id = f"concepts/{normalize_page_id(concept_name)}"

    if wiki.page_exists(page_id):
        return {"success": False, "page_id": page_id, "reason": "already exists"}

    now = datetime.utcnow()
    meta = PageMeta(
        title=concept_name,
        page_id=page_id,
        page_type=PageType.CONCEPT,
        revision_id=1,
        created=now,
        updated=now,
        updated_by=op_id,
        sources=[source_page_id],
        mind_map_priority=MindMapPriority.MEDIUM,
    )

    content = f"""# {concept_name}

## Definition

*Concept extracted from [[{source_page_id}]]. Needs definition.*

## Key Properties

- (To be filled)

## Claims Across Sources

| Claim | Source | Confidence |
|-------|--------|------------|
| - | [[{source_page_id}]] | - |

## Open Questions

- What is the precise definition?
"""

    page_path = wiki.wiki_dir / f"{page_id}.md"
    frontmatter = meta.to_frontmatter_dict()
    content_hash = write_page(page_path, frontmatter, content)

    return {"success": True, "page_id": page_id, "hash": content_hash}


def wiki_stats(wiki: Wiki) -> dict:
    """Get wiki statistics.

    Args:
        wiki: Wiki instance

    Returns:
        Dict with statistics
    """
    stats = wiki.get_stats()
    stats["wiki_name"] = wiki.config.name
    stats["wiki_topic"] = wiki.config.topic
    stats["wiki_profile"] = wiki.config.profile
    return stats


def wiki_rebuild(wiki: Wiki, force: bool = False) -> dict:
    """Rebuild all derived artifacts (Tier 2).

    Regenerates index.md and MIND_MAP.md from Tier 1 data.
    Only rebuilds if stale, unless force=True.

    Args:
        wiki: Wiki instance
        force: If True, rebuild even if fresh

    Returns:
        Dict with rebuild results
    """
    from .derived import check_freshness, rebuild_derived

    # Check freshness first
    freshness = check_freshness(wiki)

    if not force:
        # Check if any artifacts need rebuilding
        needs_rebuild = any(s.needs_rebuild for s in freshness.values())
        if not needs_rebuild:
            return {
                "success": True,
                "message": "All derived artifacts are fresh",
                "rebuilt": [],
                "freshness": {k: v.is_fresh for k, v in freshness.items()},
            }

    # Create manifest entry
    entry = ManifestEntry.create(
        op_type=OperationType.REBUILD,
        actor=Actor.LLM,
    )

    try:
        # Rebuild all derived artifacts
        result = rebuild_derived(wiki)

        entry.outputs = OperationOutputs(
            extra={
                "rebuilt": result["rebuilt"],
                "errors": result["errors"],
            }
        )
        entry.status = OperationStatus.COMPLETED
        wiki.manifest.append(entry)

        # Append to log
        wiki.append_to_log(entry, f"Rebuilt {', '.join(result['rebuilt'])}")

        return {
            "success": len(result["errors"]) == 0,
            "op_id": entry.op_id,
            "rebuilt": result["rebuilt"],
            "errors": result["errors"],
            "message": f"Rebuilt {len(result['rebuilt'])} artifacts",
        }

    except Exception as e:
        entry.status = OperationStatus.FAILED
        entry.error_message = str(e)
        wiki.manifest.append(entry)
        return {
            "success": False,
            "op_id": entry.op_id,
            "error": str(e),
        }


def wiki_freshness(wiki: Wiki) -> dict:
    """Check freshness of all derived artifacts.

    Args:
        wiki: Wiki instance

    Returns:
        Dict with freshness status for each artifact
    """
    from .derived import check_freshness

    freshness = check_freshness(wiki)

    return {
        "all_fresh": all(s.is_fresh for s in freshness.values() if s.exists),
        "artifacts": {
            name: {
                "exists": status.exists,
                "is_fresh": status.is_fresh,
                "needs_rebuild": status.needs_rebuild,
                "generated_at": status.generated_at.isoformat() if status.generated_at else None,
            }
            for name, status in freshness.items()
        },
    }


def wiki_query(
    wiki: Wiki,
    query: str,
    page_types: Optional[list[str]] = None,
    tags: Optional[list[str]] = None,
    limit: int = 10,
) -> dict:
    """Search the wiki for pages matching a query.

    Uses the configured search backend (grep by default).

    Args:
        wiki: Wiki instance
        query: Search query text
        page_types: Optional filter by page type (source, entity, concept, etc.)
        tags: Optional filter by tags
        limit: Maximum number of results

    Returns:
        Dict with search results
    """
    from .search import search_wiki, get_search_backend

    if not query or not query.strip():
        return {
            "success": False,
            "error": "Empty query",
        }

    try:
        backend = get_search_backend(wiki)
        results = search_wiki(
            wiki,
            query=query,
            page_types=page_types,
            tags=tags,
            limit=limit,
        )

        return {
            "success": True,
            "query": query,
            "backend": type(backend).__name__,
            "count": len(results),
            "results": [r.to_dict() for r in results],
        }

    except Exception as e:
        return {
            "success": False,
            "query": query,
            "error": str(e),
        }


def wiki_find_links(wiki: Wiki, page_id: str) -> dict:
    """Find all pages that link to a given page.

    Args:
        wiki: Wiki instance
        page_id: Page ID to find links to

    Returns:
        Dict with pages linking to the target
    """
    from .search import search_by_link

    try:
        results = search_by_link(wiki, page_id)

        return {
            "success": True,
            "target": page_id,
            "count": len(results),
            "linking_pages": [r.to_dict() for r in results],
        }

    except Exception as e:
        return {
            "success": False,
            "target": page_id,
            "error": str(e),
        }


# =============================================================================
# Session Commands (Tier 3 - Ephemeral)
# =============================================================================

def wiki_session_start(wiki: Optional[Wiki] = None) -> dict:
    """Start a new wiki session.

    Creates a new ephemeral session context for tracking navigation,
    queries, and operations. Session data is Tier 3 (ephemeral) -
    if lost, the wiki is still fully functional.

    Args:
        wiki: Optional Wiki instance to associate with the session

    Returns:
        Dict with session info
    """
    from .session import (
        SessionContext,
        get_current_session,
        set_current_session,
        OperationKind,
    )

    # Check if there's already an active session
    current = get_current_session()
    if current and current.is_active:
        return {
            "success": False,
            "error": "Session already active",
            "session_id": current.session_id,
            "hint": "Use wiki_session_end() to end the current session first",
        }

    # Create new session
    wiki_root = wiki.root if wiki else None
    session = SessionContext(wiki_root=wiki_root)
    set_current_session(session)

    # Log the session start operation
    session.log_operation(
        kind=OperationKind.OTHER,
        description="Session started",
    )

    return {
        "success": True,
        "session_id": session.session_id,
        "started_at": session.started_at.isoformat() + "Z",
        "wiki_root": str(wiki_root) if wiki_root else None,
        "message": f"Session {session.session_id} started",
    }


def wiki_session_end(save_to_temp: bool = False) -> dict:
    """End the current wiki session.

    Ends the active session and optionally saves it to temporary storage.

    Args:
        save_to_temp: If True, save session data to temp file before ending

    Returns:
        Dict with session summary
    """
    from .session import (
        get_current_session,
        set_current_session,
        save_session_to_temp,
        OperationKind,
    )

    session = get_current_session()
    if not session:
        return {
            "success": False,
            "error": "No active session",
            "hint": "Use wiki_session_start() to start a new session",
        }

    if not session.is_active:
        return {
            "success": False,
            "error": "Session already ended",
            "session_id": session.session_id,
        }

    # Log session end operation before ending
    session.log_operation(
        kind=OperationKind.OTHER,
        description="Session ended",
    )

    # End the session
    session.end()

    result = {
        "success": True,
        "session_id": session.session_id,
        "started_at": session.started_at.isoformat() + "Z",
        "ended_at": session.ended_at.isoformat() + "Z" if session.ended_at else None,
        "duration_seconds": session.duration_seconds,
        "pages_viewed": session.pages_viewed,
        "unique_pages_viewed": session.unique_pages_viewed,
        "queries_run": session.queries_run,
        "operations_count": session.operations_count,
        "message": f"Session {session.session_id} ended",
    }

    # Optionally save to temp
    if save_to_temp:
        temp_path = save_session_to_temp(session)
        result["saved_to"] = str(temp_path)

    # Clear the current session
    set_current_session(None)

    return result


def wiki_session_status() -> dict:
    """Get the current session status.

    Returns information about the active session, including
    navigation history, query history, and operations.

    Returns:
        Dict with session status and history
    """
    from .session import get_current_session

    session = get_current_session()
    if not session:
        return {
            "success": True,
            "has_session": False,
            "message": "No active session",
            "hint": "Use wiki_session_start() to start a new session",
        }

    return {
        "success": True,
        "has_session": True,
        "session_id": session.session_id,
        "status": session.status.value,
        "started_at": session.started_at.isoformat() + "Z",
        "ended_at": session.ended_at.isoformat() + "Z" if session.ended_at else None,
        "duration_seconds": session.duration_seconds,
        "wiki_root": str(session.wiki_root) if session.wiki_root else None,
        "statistics": {
            "pages_viewed": session.pages_viewed,
            "unique_pages_viewed": session.unique_pages_viewed,
            "queries_run": session.queries_run,
            "operations_count": session.operations_count,
        },
        "recent_pages": session.get_recent_pages(5),
        "recent_queries": session.get_recent_queries(5),
        "focus_pages": session.focus_pages,
        "working_context": session.working_context,
        "navigation_history": [e.to_dict() for e in session.navigation_history[-10:]],
        "query_history": [e.to_dict() for e in session.query_history[-10:]],
        "operations": [e.to_dict() for e in session.operations[-10:]],
    }


def wiki_session_log_navigation(
    page_id: str,
    title: Optional[str] = None,
    source: str = "direct",
) -> dict:
    """Log a page view to the current session.

    Args:
        page_id: Page that was viewed
        title: Page title (optional)
        source: How user arrived (search, link, direct)

    Returns:
        Dict with navigation entry info
    """
    from .session import get_current_session

    session = get_current_session()
    if not session or not session.is_active:
        return {
            "success": False,
            "error": "No active session",
            "hint": "Use wiki_session_start() to start a new session",
        }

    entry = session.log_navigation(page_id, title, source)

    return {
        "success": True,
        "page_id": entry.page_id,
        "timestamp": entry.timestamp.isoformat() + "Z",
        "session_pages_viewed": session.pages_viewed,
    }


def wiki_session_log_query(
    query: str,
    result_count: int = 0,
    top_results: Optional[list[str]] = None,
    filters: Optional[dict] = None,
) -> dict:
    """Log a search query to the current session.

    Args:
        query: Search query text
        result_count: Number of results found
        top_results: Page IDs of top results
        filters: Applied filters (page_types, tags)

    Returns:
        Dict with query entry info
    """
    from .session import get_current_session

    session = get_current_session()
    if not session or not session.is_active:
        return {
            "success": False,
            "error": "No active session",
            "hint": "Use wiki_session_start() to start a new session",
        }

    entry = session.log_query(query, result_count, top_results, filters)

    return {
        "success": True,
        "query": entry.query,
        "result_count": entry.result_count,
        "timestamp": entry.timestamp.isoformat() + "Z",
        "session_queries_run": session.queries_run,
    }


def wiki_session_set_context(
    context: Optional[str] = None,
    focus_pages: Optional[list[str]] = None,
) -> dict:
    """Set the working context for the current session.

    Args:
        context: Free-form notes about current work
        focus_pages: Page IDs being actively worked on

    Returns:
        Dict with updated context info
    """
    from .session import get_current_session

    session = get_current_session()
    if not session or not session.is_active:
        return {
            "success": False,
            "error": "No active session",
            "hint": "Use wiki_session_start() to start a new session",
        }

    if context is not None:
        session.set_context(context)

    if focus_pages is not None:
        session.set_focus(focus_pages)

    return {
        "success": True,
        "working_context": session.working_context,
        "focus_pages": session.focus_pages,
    }


# =============================================================================
# HELP AND GUIDANCE COMMANDS
# =============================================================================


def wiki_help(command: Optional[str] = None) -> dict:
    """Get help on wiki commands.

    Args:
        command: Specific command name (without wiki_ prefix), or None for overview

    Returns:
        Dict with help text and command info
    """
    commands = {
        "init": {
            "signature": "wiki_init(root_dir, name='My Wiki', topic='', profile='research')",
            "description": "Initialize a new wiki at the given directory",
            "example": "wiki_init(Path('.'), name='ML Research', topic='transformer architectures')",
            "profiles": ["research", "reading", "personal", "business"],
        },
        "ingest": {
            "signature": "wiki_ingest(wiki, source_path, title=None, source_type='article')",
            "description": "Ingest a source document into the wiki",
            "example": "wiki_ingest(wiki, Path('raw/attention-paper.pdf'), title='Attention Is All You Need')",
            "source_types": ["article", "paper", "book", "video", "podcast", "note"],
        },
        "query": {
            "signature": "wiki_query(wiki, question, max_results=5)",
            "description": "Search the wiki and get answers to questions",
            "example": "wiki_query(wiki, 'What is self-attention?')",
        },
        "stats": {
            "signature": "wiki_stats(wiki)",
            "description": "Get statistics about the wiki (page counts, link density, etc.)",
            "example": "wiki_stats(wiki)",
        },
        "rebuild": {
            "signature": "wiki_rebuild(wiki, force=False)",
            "description": "Regenerate derived artifacts (index.md, MIND_MAP.md)",
            "example": "wiki_rebuild(wiki, force=True)",
        },
        "freshness": {
            "signature": "wiki_freshness(wiki)",
            "description": "Check which sources or pages need updating",
            "example": "wiki_freshness(wiki)",
        },
        "find_links": {
            "signature": "wiki_find_links(wiki, page_id)",
            "description": "Find all pages that link to/from a specific page",
            "example": "wiki_find_links(wiki, 'concepts/attention')",
        },
        "session_start": {
            "signature": "wiki_session_start(wiki=None)",
            "description": "Start a new working session (tracks navigation, queries)",
            "example": "wiki_session_start(wiki)",
        },
        "session_end": {
            "signature": "wiki_session_end(save_to_temp=False)",
            "description": "End the current session, optionally save for later",
            "example": "wiki_session_end(save_to_temp=True)",
        },
        "session_status": {
            "signature": "wiki_session_status()",
            "description": "Get current session status and summary",
            "example": "wiki_session_status()",
        },
        "guide": {
            "signature": "wiki_guide(step=None)",
            "description": "Step-by-step guide for using the wiki",
            "example": "wiki_guide()  # or wiki_guide(step=2)",
        },
        "structure": {
            "signature": "wiki_structure(wiki=None)",
            "description": "Explain the wiki directory structure",
            "example": "wiki_structure(wiki)",
        },
    }

    # OMEGA memory functions (from llm_wiki.integrations.omega)
    omega_commands = {
        "is_omega_available": {
            "signature": "is_omega_available()",
            "description": "Check if OMEGA (omega-memory) is installed and available",
            "example": "if is_omega_available(): ...",
            "returns": "True if OMEGA is installed, False otherwise",
        },
        "store_wiki_event": {
            "signature": "store_wiki_event(event_type, content, wiki_name, tags=None)",
            "description": "Store a decision, lesson, error, or summary in OMEGA memory",
            "example": "store_wiki_event('decision', 'Using ISO dates in frontmatter', 'my-wiki')",
            "event_types": ["decision", "lesson", "error", "summary"],
        },
        "store_lesson": {
            "signature": "store_lesson(lesson, wiki_name)",
            "description": "Store a lesson learned (convenience wrapper for store_wiki_event)",
            "example": "store_lesson('Always check for duplicates before creating pages', 'my-wiki')",
        },
        "get_wiki_briefing": {
            "signature": "get_wiki_briefing(wiki_name, limit=5)",
            "description": "Get recent memories for a wiki (use at session start for continuity)",
            "example": "briefing = get_wiki_briefing('my-wiki')",
        },
        "query_wiki_history": {
            "signature": "query_wiki_history(query, wiki_name=None, limit=10)",
            "description": "Search past wiki work using semantic search",
            "example": "results = query_wiki_history('attention mechanism', 'ml-wiki')",
        },
        "checkpoint_task": {
            "signature": "checkpoint_task(task_id, state, wiki_name)",
            "description": "Save task state for cross-session continuity",
            "example": "checkpoint_task('ingest-batch', {'remaining': ['file2.pdf']}, 'my-wiki')",
        },
        "resume_task": {
            "signature": "resume_task(task_id)",
            "description": "Resume a previously checkpointed task",
            "example": "state = resume_task('ingest-batch')",
        },
    }

    if command:
        # Normalize command name - strip wiki_ prefix only if it's a wiki command
        cmd = command[5:] if command.startswith("wiki_") else command
        # Check wiki commands first
        if cmd in commands:
            return {
                "success": True,
                "command": f"wiki_{cmd}",
                **commands[cmd],
            }
        # Check OMEGA commands (use original command name for these)
        if command in omega_commands:
            return {
                "success": True,
                "command": command,
                "category": "OMEGA Memory",
                "import": "from llm_wiki.integrations.omega import " + command,
                **omega_commands[command],
            }
        else:
            all_commands = [f"wiki_{c}" for c in commands.keys()] + list(omega_commands.keys())
            return {
                "success": False,
                "error": f"Unknown command: {command}",
                "available": all_commands,
            }

    # Check OMEGA availability for status message
    from .integrations.omega import is_omega_available
    omega_status = "installed" if is_omega_available() else "not installed (pip install omega-memory[server])"

    # Overview of all commands
    return {
        "success": True,
        "overview": "LLM Wiki - Commands Reference",
        "commands": {
            "Core Operations": {
                "wiki_init": "Initialize a new wiki",
                "wiki_ingest": "Add a source document",
                "wiki_query": "Search and answer questions",
                "wiki_rebuild": "Regenerate derived files",
            },
            "Inspection": {
                "wiki_stats": "Wiki statistics",
                "wiki_freshness": "Check what needs updating",
                "wiki_find_links": "Find page connections",
            },
            "Session Management": {
                "wiki_session_start": "Start tracking session",
                "wiki_session_end": "End session",
                "wiki_session_status": "Current session info",
            },
            "OMEGA Memory (Tier 3)": {
                "is_omega_available": "Check if OMEGA is installed",
                "store_wiki_event": "Store decision/lesson/error",
                "store_lesson": "Store a lesson learned",
                "get_wiki_briefing": "Get session briefing",
                "query_wiki_history": "Search past work",
                "checkpoint_task": "Save task for later",
                "resume_task": "Resume checkpointed task",
            },
            "Help & Guidance": {
                "wiki_help": "This help system",
                "wiki_guide": "Step-by-step walkthrough",
                "wiki_structure": "Directory layout explained",
            },
        },
        "omega_status": omega_status,
        "hint": "Use wiki_help('command_name') for detailed help on a specific command",
    }


def wiki_guide(step: Optional[int] = None) -> dict:
    """Step-by-step guide for using the wiki.

    Args:
        step: Specific step number (1-6), or None for overview

    Returns:
        Dict with guide content
    """
    steps = {
        1: {
            "title": "Initialize Your Wiki",
            "description": "Create a new wiki for your topic of interest",
            "action": """
from pathlib import Path
from llm_wiki import wiki_init

# Create a wiki for your interest area
result = wiki_init(
    root_dir=Path("./my-ml-wiki"),
    name="Machine Learning Research",
    topic="transformer architectures and attention mechanisms",
    profile="research"  # or: reading, personal, business
)
print(result)
""",
            "result": "Creates: schema.yml, manifest.jsonl, wiki/, raw/ directories",
            "next": "Drop source documents into the raw/ folder",
        },
        2: {
            "title": "Add Source Documents",
            "description": "Drop PDFs, markdown, or text files into raw/",
            "action": """
# Copy your sources to raw/
# Example: raw/attention-is-all-you-need.pdf
#          raw/bert-paper.pdf
#          raw/my-notes.md

# Then ingest them:
from llm_wiki import Wiki, wiki_ingest

wiki = Wiki(Path("./my-ml-wiki"))
result = wiki_ingest(
    wiki,
    source_path=Path("raw/attention-is-all-you-need.pdf"),
    title="Attention Is All You Need",
    source_type="paper",
    authors=["Vaswani et al."]
)
""",
            "result": "Creates source page, extracts entities/concepts, updates index",
            "next": "Repeat for each source, or ask questions",
        },
        3: {
            "title": "Query Your Wiki",
            "description": "Ask questions - the wiki searches and synthesizes",
            "action": """
from llm_wiki import Wiki, wiki_query

wiki = Wiki(Path("./my-ml-wiki"))
result = wiki_query(wiki, "What is self-attention and why is it important?")

# The result includes:
# - Relevant pages found
# - Synthesized answer
# - Sources cited
""",
            "result": "Returns answer with citations to wiki pages",
            "next": "Save valuable answers as analysis pages",
        },
        4: {
            "title": "Organize by Topics",
            "description": "Create subfolders for different interests",
            "action": """
# Wiki structure supports topics via page_id prefixes:
# - concepts/attention          → wiki/concepts/attention.md
# - concepts/transformers       → wiki/concepts/transformers.md
# - entities/vaswani            → wiki/entities/vaswani.md

# For entirely separate topics, create separate wikis:
wiki_init(Path("./wikis/ml-research"), name="ML Research", topic="...")
wiki_init(Path("./wikis/philosophy"), name="Philosophy Notes", topic="...")
wiki_init(Path("./wikis/work-projects"), name="Work", topic="...")
""",
            "result": "Each wiki is independent with its own sources and pages",
            "next": "Check wiki health periodically",
        },
        5: {
            "title": "Maintain Your Wiki",
            "description": "Check freshness, rebuild derived files, verify integrity",
            "action": """
from llm_wiki import Wiki, wiki_stats, wiki_freshness, wiki_rebuild

wiki = Wiki(Path("./my-ml-wiki"))

# Check statistics
stats = wiki_stats(wiki)
print(f"Pages: {stats['total_pages']}, Links: {stats['total_links']}")

# Check what needs updating
fresh = wiki_freshness(wiki)
print(f"Stale pages: {fresh['stale_pages']}")

# Rebuild index and mind map
wiki_rebuild(wiki, force=True)
""",
            "result": "Keeps wiki consistent and up-to-date",
            "next": "Use sessions to track your work",
        },
        6: {
            "title": "Use Sessions",
            "description": "Track what you're working on across conversations",
            "action": """
from llm_wiki import (
    wiki_session_start,
    wiki_session_status,
    wiki_session_log_query,
    wiki_session_end,
)

# Start a session
wiki_session_start()

# Your queries and navigation are tracked automatically
# Check session status anytime:
status = wiki_session_status()
print(f"Duration: {status['duration']}, Queries: {status['query_count']}")

# End session (optionally save for later)
wiki_session_end(save_to_temp=True)
""",
            "result": "Session context preserved for continuity",
            "next": "You're ready! Keep adding sources and asking questions.",
        },
    }

    if step and step in steps:
        return {
            "success": True,
            "step": step,
            "total_steps": len(steps),
            **steps[step],
        }

    # Overview
    return {
        "success": True,
        "title": "LLM Wiki - Getting Started Guide",
        "total_steps": len(steps),
        "steps": {i: s["title"] for i, s in steps.items()},
        "hint": "Use wiki_guide(step=1) to start, or wiki_guide(step=N) for a specific step",
        "quick_start": [
            "1. wiki_init(Path('.'), name='My Wiki', topic='your topic')",
            "2. Drop files in raw/",
            "3. wiki_ingest(wiki, Path('raw/file.md'))",
            "4. wiki_query(wiki, 'your question')",
        ],
    }


def wiki_structure(wiki: Optional["Wiki"] = None) -> dict:
    """Explain the wiki directory structure.

    Args:
        wiki: Optional Wiki instance to show actual paths

    Returns:
        Dict with structure explanation
    """
    structure = {
        "overview": """
LLM Wiki uses a 3-tier data model:

TIER 1 (Source of Truth) - You and LLM both write
├── schema.yml        Config: name, topic, taxonomy settings
├── manifest.jsonl    Append-only operation log
├── raw/              Source documents (immutable once added)
│   └── *.pdf, *.md   Your input files
└── wiki/             LLM-generated pages
    ├── sources/      Summary of each raw source
    ├── entities/     People, organizations, places
    ├── concepts/     Ideas, themes, topics
    ├── analyses/     Comparisons, syntheses, answers
    └── contradictions/  Conflicting claims between sources

TIER 2 (Derived) - Regenerated from Tier 1
├── wiki/index.md     Master catalog (auto-generated)
├── wiki/log.md       Operation history (auto-generated)
└── MIND_MAP.md       Knowledge graph overview (auto-generated)

TIER 3 (Ephemeral) - Session context, not persisted
└── Session memory    Navigation history, working context
""",
        "tiers": {
            1: {
                "name": "Source of Truth",
                "description": "Committed, version-controlled, never auto-deleted",
                "files": ["schema.yml", "manifest.jsonl", "raw/*", "wiki/sources/*", "wiki/entities/*", "wiki/concepts/*"],
            },
            2: {
                "name": "Derived Artifacts",
                "description": "Can be regenerated from Tier 1 anytime",
                "files": ["wiki/index.md", "wiki/log.md", "MIND_MAP.md"],
                "regenerate": "wiki_rebuild(wiki, force=True)",
            },
            3: {
                "name": "Ephemeral Context",
                "description": "Session state, not part of wiki content",
                "files": ["Session memory (in-memory)", "temp files"],
            },
        },
        "page_types": {
            "source": "Summary of an ingested document (raw/* → wiki/sources/*)",
            "entity": "Person, organization, place, or named thing",
            "concept": "Idea, theme, methodology, or topic",
            "analysis": "Comparison, synthesis, or answer to a query",
            "contradiction": "Conflicting claims flagged for resolution",
        },
    }

    if wiki:
        structure["current_wiki"] = {
            "root": str(wiki.root),
            "wiki_dir": str(wiki.wiki_dir),
            "raw_dir": str(wiki.raw_dir),
            "exists": wiki.exists(),
        }

    return {
        "success": True,
        **structure,
    }
