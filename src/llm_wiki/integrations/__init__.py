"""Integrations for LLM Wiki with external services.

This module provides optional integrations with external services.
All integrations are designed to gracefully degrade when dependencies
are not installed.

Available integrations:
- omega: OMEGA (omega-memory) persistent memory backend for session management
"""

# Import omega integration (handles ImportError gracefully)
from .omega import (
    is_omega_available,
    store_wiki_event,
    get_wiki_briefing,
    store_lesson,
    query_wiki_history,
    checkpoint_task,
    resume_task,
)

__all__ = [
    # Omega integration
    "is_omega_available",
    "store_wiki_event",
    "get_wiki_briefing",
    "store_lesson",
    "query_wiki_history",
    "checkpoint_task",
    "resume_task",
]
