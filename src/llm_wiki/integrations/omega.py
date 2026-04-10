"""OMEGA (omega-memory) integration for LLM Wiki session management.

This module provides optional integration with OMEGA, a persistent memory
system for AI agents. OMEGA provides:
- Semantic storage for decisions, lessons, errors, summaries
- Session briefings for cross-session continuity
- Graph relationships between memories
- Checkpoint/resume for task continuity

All functions gracefully handle the case when omega-memory is not installed,
returning sensible defaults (False, None, empty lists).

Usage:
    from llm_wiki.integrations.omega import (
        is_omega_available,
        store_wiki_event,
        get_wiki_briefing,
    )

    if is_omega_available():
        store_wiki_event("decision", "Created new entity page", "my-wiki")
"""

from __future__ import annotations

import logging
from typing import Any

# Try to import omega-memory, set flag based on availability
_omega_available = False
_omega = None

try:
    import omega as _omega_module
    _omega = _omega_module
    _omega_available = True
except ImportError:
    pass

logger = logging.getLogger(__name__)


def is_omega_available() -> bool:
    """Check if omega-memory is installed and available.

    Returns:
        True if omega-memory is installed and can be used, False otherwise.
    """
    return _omega_available


def store_wiki_event(
    event_type: str,
    content: str,
    wiki_name: str,
    tags: list[str] | None = None,
) -> bool:
    """Store a wiki event in OMEGA persistent memory.

    Event types map to OMEGA memory types:
    - "decision": A decision made during wiki editing
    - "lesson": Something learned (e.g., a correction)
    - "error": An error encountered
    - "summary": A summary of work done

    Args:
        event_type: Type of event (decision, lesson, error, summary)
        content: Content/description of the event
        wiki_name: Name of the wiki this event relates to
        tags: Optional list of tags to attach to the memory

    Returns:
        True if event was stored successfully, False otherwise.
    """
    if not _omega_available or _omega is None:
        logger.debug("OMEGA not available, skipping store_wiki_event")
        return False

    try:
        # Build tags list with wiki context
        all_tags = [f"wiki:{wiki_name}"]
        if tags:
            all_tags.extend(tags)

        # Map event_type to OMEGA memory type
        valid_types = {"decision", "lesson", "error", "summary", "memory"}
        memory_type = event_type if event_type in valid_types else "memory"

        # Store in OMEGA using correct API:
        # store(content, event_type, metadata, session_id, project, ...)
        _omega.store(
            content=content,
            event_type=memory_type,
            metadata={"tags": all_tags, "wiki": wiki_name},
            project=wiki_name,
        )
        return True

    except Exception as e:
        logger.warning(f"Failed to store wiki event in OMEGA: {e}")
        return False


def get_wiki_briefing(wiki_name: str, limit: int = 5) -> list[dict[str, Any]]:
    """Get a session briefing for a specific wiki.

    Retrieves recent memories related to the wiki for cross-session
    continuity. Useful for resuming work on a wiki after a break.

    Args:
        wiki_name: Name of the wiki to get briefing for
        limit: Maximum number of memories to retrieve

    Returns:
        List of memory dictionaries, each containing:
        - content: The memory content
        - type: The memory type (decision, lesson, etc.)
        - tags: List of tags
        - timestamp: When the memory was created
        Returns empty list if OMEGA unavailable or on error.
    """
    if not _omega_available or _omega is None:
        logger.debug("OMEGA not available, returning empty briefing")
        return []

    try:
        # Query OMEGA for wiki-related memories using correct API:
        # query(query_text, limit, project, ...)
        results = _omega.query(
            query_text=wiki_name,
            limit=limit,
            project=wiki_name,
        )

        # Results come as a string, parse if needed
        if isinstance(results, str):
            # OMEGA returns formatted string, convert to list
            return [{"content": results, "type": "briefing"}] if results.strip() else []

        # Convert to list of dicts
        briefing = []
        for result in results:
            memory = {
                "content": getattr(result, "content", str(result)),
                "type": getattr(result, "type", "unknown"),
                "tags": getattr(result, "tags", []),
                "timestamp": getattr(result, "timestamp", None),
            }
            briefing.append(memory)

        return briefing

    except Exception as e:
        logger.warning(f"Failed to get wiki briefing from OMEGA: {e}")
        return []


def store_lesson(lesson: str, wiki_name: str) -> bool:
    """Store a lesson learned during wiki work.

    Convenience function for storing lessons (e.g., corrections,
    insights, patterns discovered) for future reference.

    Args:
        lesson: The lesson learned
        wiki_name: Name of the wiki this relates to

    Returns:
        True if lesson was stored successfully, False otherwise.
    """
    return store_wiki_event(
        event_type="lesson",
        content=lesson,
        wiki_name=wiki_name,
        tags=["lesson"],
    )


def query_wiki_history(
    query: str,
    wiki_name: str | None = None,
    limit: int = 10,
) -> list[dict[str, Any]]:
    """Query past wiki work using semantic search.

    Args:
        query: Search query text
        wiki_name: Optional wiki name to filter results (if None, searches all)
        limit: Maximum number of results to return

    Returns:
        List of matching memory dictionaries.
        Returns empty list if OMEGA unavailable or on error.
    """
    if not _omega_available or _omega is None:
        logger.debug("OMEGA not available, returning empty history")
        return []

    try:
        # Query OMEGA using correct API
        results = _omega.query(
            query_text=query,
            limit=limit,
            project=wiki_name if wiki_name else None,
        )

        # Results come as a string, parse if needed
        if isinstance(results, str):
            return [{"content": results, "type": "history"}] if results.strip() else []

        # Convert to list of dicts
        history = []
        for result in results:
            memory = {
                "content": getattr(result, "content", str(result)),
                "type": getattr(result, "type", "unknown"),
                "tags": getattr(result, "tags", []),
                "timestamp": getattr(result, "timestamp", None),
                "score": getattr(result, "score", None),
            }
            history.append(memory)

        return history

    except Exception as e:
        logger.warning(f"Failed to query wiki history from OMEGA: {e}")
        return []


def checkpoint_task(
    task_id: str,
    state: dict[str, Any],
    wiki_name: str,
) -> bool:
    """Checkpoint a task for cross-session continuity.

    Saves the current state of a task so it can be resumed later,
    even across different sessions.

    Args:
        task_id: Unique identifier for the task
        state: Task state dictionary to save
        wiki_name: Name of the wiki this task relates to

    Returns:
        True if checkpoint was saved successfully, False otherwise.
    """
    if not _omega_available or _omega is None:
        logger.debug("OMEGA not available, skipping checkpoint")
        return False

    try:
        # Check if omega has checkpoint functionality
        if hasattr(_omega, "checkpoint"):
            _omega.checkpoint(
                task_id=task_id,
                state=state,
            )
            return True

        # Fallback: store as a summary with checkpoint metadata
        import json
        checkpoint_content = json.dumps({
            "task_id": task_id,
            "state": state,
            "wiki_name": wiki_name,
        })

        _omega.store(
            content=f"[CHECKPOINT:{task_id}] {checkpoint_content}",
            event_type="summary",
            metadata={"checkpoint": True, "task_id": task_id},
            project=wiki_name,
        )
        return True

    except Exception as e:
        logger.warning(f"Failed to checkpoint task in OMEGA: {e}")
        return False


def resume_task(task_id: str) -> dict[str, Any] | None:
    """Resume a checkpointed task.

    Retrieves the saved state of a previously checkpointed task.

    Args:
        task_id: Unique identifier for the task to resume

    Returns:
        Task state dictionary if found, None otherwise.
    """
    if not _omega_available or _omega is None:
        logger.debug("OMEGA not available, cannot resume task")
        return None

    try:
        # Check if omega has resume functionality
        if hasattr(_omega, "resume"):
            state = _omega.resume(task_id=task_id)
            return state

        # Fallback: query for checkpoint
        results = _omega.query(
            query_text=f"CHECKPOINT:{task_id}",
            limit=1,
        )

        if not results or (isinstance(results, str) and not results.strip()):
            return None

        # Parse the checkpoint content
        import json
        if isinstance(results, str):
            content = results
        else:
            result = results[0]
            content = getattr(result, "content", str(result))

        # Extract JSON from checkpoint format
        if "[CHECKPOINT:" in content:
            json_start = content.find("] ") + 2
            checkpoint_data = json.loads(content[json_start:])
            return checkpoint_data.get("state")

        return None

    except Exception as e:
        logger.warning(f"Failed to resume task from OMEGA: {e}")
        return None
