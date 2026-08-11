"""Second Brain: capture thoughts, classify them, retrieve them later.

A companion to the wiki rather than part of it. The wiki holds what you have
read; this holds what you thought while reading it. They stay in separate vaults
on purpose -- wiki pages are schema-v2, provenance-checked and index-rebuilt, and
untyped captures dropped among them would break those checks.

Typical use from Python::

    from llm_wiki.secondbrain import SecondBrainConfig, Store, capture, process

    config = SecondBrainConfig.resolve()
    config.ensure_dirs()
    with Store(config.db_path) as store:
        capture(store, "Idea: order flow imbalance may lead spread moves")
        process(store, threshold=config.confidence_threshold)

The same operations are available from the terminal as ``sb``.
"""

from .classify import Classification, classify, extract_due, make_title
from .config import SecondBrainConfig
from .digest import build_digest, render_digest
from .models import (
    DEFAULT_CONFIDENCE_THRESHOLD,
    PRIORITY_NAMES,
    Capture,
    CaptureStatus,
    Domain,
    Edge,
    EdgeType,
    Node,
    NodeStatus,
    NodeType,
    new_id,
    short_id,
)
from .service import (
    NodeNotFoundError,
    archive,
    capture,
    complete,
    link,
    process,
    process_one,
    reopen,
    resolve_node,
    set_domain,
    set_priority,
    set_type,
)
from .store import AmbiguousIdError, Store
from .vault import export_all, render_node, write_node

__all__ = [
    "AmbiguousIdError",
    "Capture",
    "CaptureStatus",
    "Classification",
    "DEFAULT_CONFIDENCE_THRESHOLD",
    "Domain",
    "Edge",
    "EdgeType",
    "Node",
    "NodeNotFoundError",
    "NodeStatus",
    "NodeType",
    "PRIORITY_NAMES",
    "SecondBrainConfig",
    "Store",
    "archive",
    "build_digest",
    "capture",
    "classify",
    "complete",
    "export_all",
    "extract_due",
    "link",
    "make_title",
    "new_id",
    "process",
    "process_one",
    "render_digest",
    "render_node",
    "reopen",
    "resolve_node",
    "set_domain",
    "set_priority",
    "set_type",
    "short_id",
    "write_node",
]
