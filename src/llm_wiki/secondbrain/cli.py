"""Command line interface for the Second Brain.

Installed as ``sb``. Built on argparse rather than click so the package picks up
no new dependency -- the wiki's own rule is that a dependency has to earn its
place, and a CLI this size does not need one.

Exit codes: 0 success, 1 general error, 2 configuration error, 3 database error.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional, Sequence

from .config import SecondBrainConfig
from .digest import (
    DAILY_WORD_LIMIT,
    WEEKLY_WORD_LIMIT,
    build_digest,
    render_digest,
)
from .models import (
    CaptureStatus,
    Domain,
    EdgeType,
    NodeStatus,
    NodeType,
    PRIORITY_NAMES,
    short_id,
)
from .service import NodeNotFoundError, capture, complete, link, process
from .service import archive as archive_node
from .service import reopen as reopen_node
from .service import resolve_node, set_domain, set_priority, set_type
from .store import AmbiguousIdError, Store
from .vault import export_all, write_node

EXIT_OK = 0
EXIT_ERROR = 1
EXIT_CONFIG = 2
EXIT_DB = 3


def _enum(value: Optional[str], enum_cls):
    """Convert an optional string to an enum member, or None."""
    return None if value is None else enum_cls(value)


def build_parser() -> argparse.ArgumentParser:
    """Construct the full argument parser.

    Returns:
        A parser with every subcommand registered.
    """
    parser = argparse.ArgumentParser(
        prog="sb", description="Second Brain: capture, classify, retrieve."
    )
    parser.add_argument("--root", help="Second Brain directory (overrides the default)")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init", help="create the database and vault directories")

    p = sub.add_parser("capture", help="capture a thought")
    p.add_argument("content", help="the text to capture")
    p.add_argument("--source", "-s", default="cli", help="where it came from")

    p = sub.add_parser("inbox", help="list captures awaiting classification")
    p.add_argument("--status", "-s", choices=[s.value for s in CaptureStatus])
    p.add_argument("--limit", "-n", type=int, default=20)

    p = sub.add_parser("process", help="classify pending captures")
    p.add_argument("--id", dest="capture_id", help="process one capture")
    p.add_argument("--dry-run", action="store_true", help="report without writing")

    p = sub.add_parser("list", help="list nodes")
    p.add_argument("node_type", nargs="?", choices=[t.value for t in NodeType])
    p.add_argument("--status", "-s", choices=[s.value for s in NodeStatus])
    p.add_argument("--domain", "-d", choices=[d.value for d in Domain])
    p.add_argument("--limit", "-n", type=int, default=20)

    p = sub.add_parser("show", help="show one node in full")
    p.add_argument("reference", help="id prefix or exact title")

    p = sub.add_parser("query", help="substring search over titles and bodies")
    p.add_argument("term")
    p.add_argument("--limit", "-n", type=int, default=20)

    p = sub.add_parser("done", help="mark a node completed")
    p.add_argument("reference")

    p = sub.add_parser("reopen", help="return a node to active")
    p.add_argument("reference")

    p = sub.add_parser("archive", help="archive a node")
    p.add_argument("reference")

    p = sub.add_parser("priority", help="set priority 0 (critical) to 4 (backlog)")
    p.add_argument("reference")
    p.add_argument("level", type=int, choices=range(5))

    p = sub.add_parser("domain", help="set the domain tag")
    p.add_argument("reference")
    p.add_argument("value", choices=[d.value for d in Domain])

    p = sub.add_parser("retype", help="correct a node's type")
    p.add_argument("reference")
    p.add_argument("value", choices=[t.value for t in NodeType])

    p = sub.add_parser("link", help="create a typed edge between two nodes")
    p.add_argument("src")
    p.add_argument("dst")
    p.add_argument("rel", choices=[r.value for r in EdgeType])

    p = sub.add_parser("digest", help="what to focus on")
    p.add_argument("--weekly", action="store_true", help="seven days, 250 words")

    p = sub.add_parser("export", help="write the graph to the vault as markdown")
    p.add_argument("--limit", "-n", type=int, default=10_000)

    sub.add_parser("status", help="system health check")
    return parser


# -- command implementations ---------------------------------------------


def _cmd_init(config: SecondBrainConfig) -> int:
    config.ensure_dirs()
    Store(config.db_path).close()
    print(f"Initialised.\n  Database: {config.db_path}\n  Vault: {config.vault_path}")
    return EXIT_OK


def _cmd_capture(store: Store, config: SecondBrainConfig, args) -> int:
    item = capture(store, args.content, source=args.source)
    print(f"Captured ({short_id(item.id)}).")
    print("Not classified yet - run `sb process` to file it.")
    return EXIT_OK


def _cmd_inbox(store: Store, args) -> int:
    status = _enum(args.status, CaptureStatus)
    items = store.list_captures(status=status, limit=args.limit)
    if not items:
        print(f"Inbox is empty ({status.value if status else 'any status'}).")
        return EXIT_OK
    print(f"{'ID':<10} {'SOURCE':<8} {'STATUS':<14} CONTENT")
    for item in items:
        preview = item.content.replace("\n", " ")[:48]
        print(
            f"{short_id(item.id):<10} {item.source:<8} {item.status.value:<14} {preview}"
        )
    return EXIT_OK


def _cmd_process(store: Store, config: SecondBrainConfig, args) -> int:
    results = process(
        store,
        threshold=config.confidence_threshold,
        capture_id=args.capture_id,
        dry_run=args.dry_run,
    )
    if not results:
        print("Nothing pending.")
        return EXIT_OK
    for item, node, verdict in results:
        marker = "?" if verdict.confidence < config.confidence_threshold else " "
        ident = short_id(node.id) if node else short_id(item.id)
        print(
            f"{marker} {ident}  {verdict.node_type.value:<10} "
            f"{verdict.confidence:.2f}  {verdict.title}"
        )
        if verdict.confidence < config.confidence_threshold:
            print(f"    needs review: {'; '.join(verdict.reasons)}")
    if args.dry_run:
        print("\nDry run - nothing was written.")
    return EXIT_OK


def _cmd_list(store: Store, args) -> int:
    nodes = store.list_nodes(
        node_type=_enum(args.node_type, NodeType),
        status=_enum(args.status, NodeStatus),
        domain=_enum(args.domain, Domain),
        limit=args.limit,
    )
    if not nodes:
        print("No matching nodes.")
        return EXIT_OK
    print(f"{'ID':<10} {'TYPE':<10} {'STATUS':<10} {'PRI':<4} {'DUE':<12} TITLE")
    for node in nodes:
        print(
            f"{short_id(node.id):<10} {node.node_type.value:<10} "
            f"{node.status.value:<10} {node.priority:<4} {(node.due or '-'):<12} "
            f"{node.title}"
        )
    return EXIT_OK


def _cmd_show(store: Store, args) -> int:
    node = resolve_node(store, args.reference)
    print(f"{node.title}\n")
    print(f"  id         {node.id}")
    print(f"  type       {node.node_type.value}")
    print(f"  status     {node.status.value}")
    print(f"  priority   {node.priority} ({node.priority_name})")
    print(f"  domain     {node.domain.value}")
    print(f"  due        {node.due or '-'}")
    print(f"  created    {node.created_at.isoformat()}Z")
    if node.confidence is not None:
        print(f"  confidence {node.confidence}")
    if node.body and node.body.strip() != node.title:
        print(f"\n{node.body.strip()}")
    edges = store.edges_from(node.id)
    if edges:
        print("\nLinks:")
        for edge in edges:
            target = store.get_node(edge.dst)
            if target is not None:
                print(f"  {edge.rel.value} -> {target.title} ({short_id(target.id)})")
    return EXIT_OK


def _cmd_query(store: Store, args) -> int:
    nodes = store.search_nodes(args.term, limit=args.limit)
    if not nodes:
        print(f"Nothing matched {args.term!r}.")
        return EXIT_OK
    for node in nodes:
        print(f"{short_id(node.id)}  {node.node_type.value:<10} {node.title}")
    print("\nSubstring match, not semantic - wording that differs will be missed.")
    return EXIT_OK


def _cmd_digest(store: Store, args) -> int:
    days = 7 if args.weekly else 1
    limit = WEEKLY_WORD_LIMIT if args.weekly else DAILY_WORD_LIMIT
    text = render_digest(build_digest(store, days=days), word_limit=limit)
    print(text if text else "Nothing due, nothing pending review. Clear.")
    return EXIT_OK


def _cmd_status(store: Store, config: SecondBrainConfig) -> int:
    counts = store.counts()
    print("Second Brain Status\n")
    print("Configuration:")
    print(f"  Database: {config.db_path}")
    print(f"  Vault:    {config.vault_path}")
    print(f"  Threshold: {config.confidence_threshold}")
    print("\nDatabase:")
    print(f"  Total nodes:    {counts['nodes']}")
    print(f"  Total edges:    {counts['edges']}")
    print(f"  Total captures: {counts['captures']}")
    print(f"  Total events:   {counts['events']}")
    print("\nInbox:")
    print(f"  Pending:      {counts['pending']}")
    print(f"  Needs review: {counts['needs_review']}")
    return EXIT_OK


def _cmd_export(store: Store, config: SecondBrainConfig, args) -> int:
    config.ensure_dirs()
    written = export_all(store, config.vault_path, limit=args.limit)
    print(f"Exported {len(written)} nodes to {config.vault_path}")
    return EXIT_OK


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run the CLI.

    Args:
        argv: Argument list, defaulting to ``sys.argv[1:]``.

    Returns:
        A process exit code.
    """
    args = build_parser().parse_args(argv)
    try:
        config = SecondBrainConfig.resolve(args.root)
    except (ValueError, OSError) as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return EXIT_CONFIG

    if args.command == "init":
        return _cmd_init(config)

    if not config.db_path.exists():
        print(
            f"No database at {config.db_path}. Run `sb init` first.", file=sys.stderr
        )
        return EXIT_CONFIG

    try:
        with Store(config.db_path) as store:
            handlers = {
                "capture": lambda: _cmd_capture(store, config, args),
                "inbox": lambda: _cmd_inbox(store, args),
                "process": lambda: _cmd_process(store, config, args),
                "list": lambda: _cmd_list(store, args),
                "show": lambda: _cmd_show(store, args),
                "query": lambda: _cmd_query(store, args),
                "digest": lambda: _cmd_digest(store, args),
                "status": lambda: _cmd_status(store, config),
                "export": lambda: _cmd_export(store, config, args),
                "done": lambda: _mutate(store, config, complete, args.reference),
                "reopen": lambda: _mutate(store, config, reopen_node, args.reference),
                "archive": lambda: _mutate(
                    store, config, archive_node, args.reference
                ),
                "priority": lambda: _mutate(
                    store, config, set_priority, args.reference, args.level
                ),
                "domain": lambda: _mutate(
                    store, config, set_domain, args.reference, Domain(args.value)
                ),
                "retype": lambda: _mutate(
                    store, config, set_type, args.reference, NodeType(args.value)
                ),
                "link": lambda: _cmd_link(store, args),
            }
            return handlers[args.command]()
    except (NodeNotFoundError, AmbiguousIdError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return EXIT_ERROR
    except OSError as exc:
        print(f"Database error: {exc}", file=sys.stderr)
        return EXIT_DB


def _mutate(store: Store, config: SecondBrainConfig, fn, *fn_args) -> int:
    """Apply a mutation, report it, and keep the vault copy in step."""
    node = fn(store, *fn_args)
    if config.vault_path.exists():
        write_node(node, config.vault_path, store=store)
    print(
        f"{short_id(node.id)}  {node.node_type.value:<10} {node.status.value:<10} "
        f"p{node.priority} ({PRIORITY_NAMES[node.priority]})  {node.title}"
    )
    return EXIT_OK


def _cmd_link(store: Store, args) -> int:
    edge = link(store, args.src, args.dst, EdgeType(args.rel))
    print(f"{short_id(edge.src)} --{edge.rel.value}--> {short_id(edge.dst)}")
    return EXIT_OK


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
