"""Derived artifacts (Tier 2) for LLM Wiki.

Generates and maintains derived artifacts that can be rebuilt from Tier 1:
- index.md: Master catalog of all wiki pages
- MIND_MAP.md: Grep-friendly knowledge graph
- Freshness tracking for stale detection
"""

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional
import hashlib
import json

from .wiki import Wiki
from .frontmatter import parse_page, write_page, extract_wikilinks
from .schemas import PageType, MindMapPriority


# Generation header template
GENERATION_HEADER = """<!--
AUTO-GENERATED FILE - DO NOT EDIT MANUALLY
Generated: {timestamp}
Generator: llm-wiki {version}
Source hash: {source_hash}
Rebuild with: wiki:rebuild
-->

"""


@dataclass
class DerivedMeta:
    """Metadata for a derived artifact."""
    generated_at: datetime
    source_hash: str  # Hash of all source pages used
    generator_version: str
    is_stale: bool = False

    def to_dict(self) -> dict:
        return {
            "generated_at": self.generated_at.isoformat() + "Z",
            "source_hash": self.source_hash,
            "generator_version": self.generator_version,
            "is_stale": self.is_stale,
        }


@dataclass
class PageInfo:
    """Information about a wiki page for indexing."""
    page_id: str
    title: str
    page_type: str
    path: Path
    tags: list[str] = field(default_factory=list)
    summary: Optional[str] = None
    source_count: int = 0
    link_count: int = 0
    created: Optional[str] = None
    updated: Optional[str] = None
    mind_map_priority: str = "medium"
    mind_map_category: Optional[int] = None


def compute_source_hash(wiki: Wiki) -> str:
    """Compute a hash of all Tier 1 wiki pages.

    This hash changes when any canonical page changes,
    used to detect when derived artifacts are stale.

    Note: Does NOT include manifest.jsonl since rebuild
    itself modifies the manifest, which would immediately
    invalidate the freshness of just-built artifacts.
    """
    h = hashlib.sha256()

    # Sort pages for determinism
    pages = sorted(wiki.list_pages(), key=lambda p: str(p))

    for page_path in pages:
        # Hash the file content
        with open(page_path, "rb") as f:
            h.update(f.read())

    return f"sha256:{h.hexdigest()[:16]}"


def gather_page_info(wiki: Wiki) -> list[PageInfo]:
    """Gather information about all wiki pages."""
    pages = []

    for page_path in wiki.list_pages():
        try:
            metadata, content = parse_page(page_path)

            # Extract summary (first paragraph after title)
            lines = content.strip().split('\n')
            summary = None
            for i, line in enumerate(lines):
                if line.startswith('#'):
                    continue
                if line.strip():
                    summary = line.strip()[:200]
                    if len(line.strip()) > 200:
                        summary += "..."
                    break

            # Count links
            links = extract_wikilinks(content)

            pages.append(PageInfo(
                page_id=metadata.get("page_id", str(page_path.relative_to(wiki.wiki_dir).with_suffix(""))),
                title=metadata.get("title", page_path.stem),
                page_type=metadata.get("page_type", "unknown"),
                path=page_path,
                tags=metadata.get("tags", []),
                summary=summary,
                source_count=len(metadata.get("sources", [])),
                link_count=len(links),
                created=metadata.get("created"),
                updated=metadata.get("updated"),
                mind_map_priority=metadata.get("mind_map_priority", "medium"),
                mind_map_category=metadata.get("mind_map_category"),
            ))
        except Exception as e:
            # Skip pages with parse errors
            continue

    return pages


def compile_index(wiki: Wiki) -> str:
    """Compile the index.md master catalog.

    Generates a deterministic index of all wiki pages,
    organized by page type with statistics.

    Args:
        wiki: Wiki instance

    Returns:
        Markdown content for index.md
    """
    from . import __version__

    pages = gather_page_info(wiki)
    source_hash = compute_source_hash(wiki)
    now = datetime.utcnow()

    # Group by type
    by_type: dict[str, list[PageInfo]] = {
        "source": [],
        "entity": [],
        "concept": [],
        "analysis": [],
        "contradiction": [],
    }

    for page in pages:
        ptype = page.page_type
        if ptype in by_type:
            by_type[ptype].append(page)

    # Sort each group by title for determinism
    for ptype in by_type:
        by_type[ptype].sort(key=lambda p: p.title.lower())

    # Build content
    lines = [
        GENERATION_HEADER.format(
            timestamp=now.isoformat() + "Z",
            version=__version__,
            source_hash=source_hash,
        ),
        f"# {wiki.config.name}",
        "",
        "Master catalog of all pages in this wiki.",
        "",
    ]

    # Sources section
    lines.extend([
        "## Sources",
        "*Summary pages for ingested source documents.*",
        "",
    ])
    if by_type["source"]:
        for page in by_type["source"]:
            lines.append(f"- [[{page.title}]] - {page.summary or '*No summary*'}")
        lines.append("")
    else:
        lines.extend(["(No sources ingested yet)", ""])

    # Entities section
    lines.extend([
        "## Entities",
        "*People, organizations, places.*",
        "",
    ])
    if by_type["entity"]:
        for page in by_type["entity"]:
            tags_str = f" `{', '.join(page.tags)}`" if page.tags else ""
            lines.append(f"- [[{page.title}]]{tags_str}")
        lines.append("")
    else:
        lines.extend(["(No entities yet)", ""])

    # Concepts section
    lines.extend([
        "## Concepts",
        "*Ideas, themes, topics.*",
        "",
    ])
    if by_type["concept"]:
        for page in by_type["concept"]:
            sources_str = f" ({page.source_count} sources)" if page.source_count > 0 else ""
            lines.append(f"- [[{page.title}]]{sources_str}")
        lines.append("")
    else:
        lines.extend(["(No concepts yet)", ""])

    # Analyses section
    lines.extend([
        "## Analyses",
        "*Comparisons, syntheses, query answers.*",
        "",
    ])
    if by_type["analysis"]:
        for page in by_type["analysis"]:
            lines.append(f"- [[{page.title}]]")
        lines.append("")
    else:
        lines.extend(["(No analyses yet)", ""])

    # Contradictions section
    lines.extend([
        "## Contradictions",
        "*Disagreements between sources.*",
        "",
    ])
    if by_type["contradiction"]:
        for page in by_type["contradiction"]:
            lines.append(f"- [[{page.title}]]")
        lines.append("")
    else:
        lines.extend(["(No contradictions yet)", ""])

    # Statistics
    total_pages = sum(len(pages) for pages in by_type.values())
    lines.extend([
        "---",
        "",
        "**Stats**",
        f"- Total sources: {len(by_type['source'])}",
        f"- Total entities: {len(by_type['entity'])}",
        f"- Total concepts: {len(by_type['concept'])}",
        f"- Total analyses: {len(by_type['analysis'])}",
        f"- Total contradictions: {len(by_type['contradiction'])}",
        f"- **Total pages: {total_pages}**",
        f"- Last updated: {now.strftime('%Y-%m-%d')}",
        "",
    ])

    return "\n".join(lines)


def compile_mind_map(wiki: Wiki) -> str:
    """Compile the MIND_MAP.md knowledge graph.

    Generates a grep-friendly single-file synthesis with:
    - Numbered nodes [N] on single lines
    - Routing nodes [1-5] as hubs
    - Cross-references embedded naturally
    - 150-400 words per node

    Args:
        wiki: Wiki instance

    Returns:
        Markdown content for MIND_MAP.md
    """
    from . import __version__

    pages = gather_page_info(wiki)
    source_hash = compute_source_hash(wiki)
    now = datetime.utcnow()

    # Filter and sort pages by priority
    priority_order = {"high": 0, "medium": 1, "low": 2, "exclude": 3}

    # Filter out excluded pages
    included_pages = [p for p in pages if p.mind_map_priority != "exclude"]

    # Sort by priority then title
    included_pages.sort(key=lambda p: (priority_order.get(p.mind_map_priority, 2), p.title.lower()))

    # Limit to max nodes from config
    max_nodes = wiki.config.mind_map.max_nodes
    included_pages = included_pages[:max_nodes - 5]  # Reserve 5 for routing nodes

    # Build content
    lines = [
        GENERATION_HEADER.format(
            timestamp=now.isoformat() + "Z",
            version=__version__,
            source_hash=source_hash,
        ),
        f"# {wiki.config.name} - Knowledge Map",
        "",
        "Grep-friendly knowledge graph. Each node is a single line.",
        "",
        "**Search:** `grep \"^\\[5\\]\" MIND_MAP.md` returns node 5.",
        "",
        "---",
        "",
    ]

    # Group pages by category for routing nodes
    by_type: dict[str, list[PageInfo]] = {
        "source": [],
        "entity": [],
        "concept": [],
        "analysis": [],
        "contradiction": [],
    }

    for page in included_pages:
        ptype = page.page_type
        if ptype in by_type:
            by_type[ptype].append(page)

    # Node 1: Overview
    topic = wiki.config.topic or "various topics"
    total_pages = len(included_pages)
    overview_text = (
        f"This wiki covers {topic}. "
        f"It contains {len(by_type['source'])} source summaries, "
        f"{len(by_type['entity'])} entity profiles, "
        f"{len(by_type['concept'])} concept explanations, "
        f"and {len(by_type['analysis'])} analyses. "
        f"See [2] for sources, [3] for entities, [4] for concepts, [5] for analyses."
    )
    lines.append(f"[1] **Overview** - {overview_text}")
    lines.append("")

    # Node 2: Sources hub
    if by_type["source"]:
        source_refs = ", ".join([f"[{i+6}]" for i, _ in enumerate(by_type["source"][:5])])
        sources_text = f"Source documents ingested into this wiki. {len(by_type['source'])} sources total. Key sources: {source_refs}. Each source is summarized with key claims, methodology, and extracted entities/concepts."
    else:
        sources_text = "No sources ingested yet. Add documents to raw/ and run ingest to populate."
    lines.append(f"[2] **Sources** - {sources_text}")
    lines.append("")

    # Node 3: Entities hub
    if by_type["entity"]:
        entity_list = ", ".join([p.title for p in by_type["entity"][:5]])
        entities_text = f"People, organizations, and places mentioned across sources. {len(by_type['entity'])} entities tracked. Includes: {entity_list}. Each entity page tracks appearances and relationships."
    else:
        entities_text = "No entities extracted yet. Entities are created during source ingestion."
    lines.append(f"[3] **Entities** - {entities_text}")
    lines.append("")

    # Node 4: Concepts hub
    if by_type["concept"]:
        concept_list = ", ".join([p.title for p in by_type["concept"][:5]])
        concepts_text = f"Ideas, techniques, and methodologies synthesized from sources. {len(by_type['concept'])} concepts defined. Key concepts: {concept_list}. Each concept links to defining sources and related concepts."
    else:
        concepts_text = "No concepts defined yet. Concepts emerge during source ingestion and analysis."
    lines.append(f"[4] **Concepts** - {concepts_text}")
    lines.append("")

    # Node 5: Analyses hub
    if by_type["analysis"]:
        analysis_list = ", ".join([p.title for p in by_type["analysis"][:3]])
        analyses_text = f"Saved query answers, comparisons, and syntheses. {len(by_type['analysis'])} analyses. Includes: {analysis_list}. Analyses are created when answering questions worth preserving."
    else:
        analyses_text = "No analyses saved yet. Ask questions and save valuable answers to build this section."
    lines.append(f"[5] **Analyses** - {analyses_text}")
    lines.append("")

    # Detail nodes (6+)
    node_num = 6

    # Add source nodes
    for page in by_type["source"][:10]:  # Limit to 10 sources
        summary = page.summary or "Source document summary."
        # Truncate to ~300 chars for single line
        if len(summary) > 300:
            summary = summary[:297] + "..."
        lines.append(f"[{node_num}] **{page.title}** - {summary} See [[{page.title}]] for full details. Referenced from [2].")
        lines.append("")
        node_num += 1

    # Add concept nodes
    for page in by_type["concept"][:15]:  # Limit to 15 concepts
        summary = page.summary or "Concept definition."
        if len(summary) > 300:
            summary = summary[:297] + "..."
        sources_note = f"Based on {page.source_count} sources." if page.source_count > 0 else ""
        lines.append(f"[{node_num}] **{page.title}** - {summary} {sources_note} See [[{page.title}]]. Referenced from [4].")
        lines.append("")
        node_num += 1

    # Add entity nodes (fewer, lower priority)
    for page in by_type["entity"][:10]:  # Limit to 10 entities
        summary = page.summary or "Entity profile."
        if len(summary) > 250:
            summary = summary[:247] + "..."
        lines.append(f"[{node_num}] **{page.title}** - {summary} See [[{page.title}]]. Referenced from [3].")
        lines.append("")
        node_num += 1

    lines.extend([
        "---",
        "",
        f"*{node_num - 1} nodes total. Generated {now.strftime('%Y-%m-%d')}.*",
        "",
    ])

    return "\n".join(lines)


@dataclass
class FreshnessStatus:
    """Status of derived artifact freshness."""
    artifact: str
    exists: bool
    is_fresh: bool
    current_hash: Optional[str] = None
    artifact_hash: Optional[str] = None
    generated_at: Optional[datetime] = None

    @property
    def needs_rebuild(self) -> bool:
        return not self.exists or not self.is_fresh


def check_freshness(wiki: Wiki) -> dict[str, FreshnessStatus]:
    """Check freshness of all derived artifacts.

    Compares the source hash stored in each artifact's
    generation header against the current source hash.

    Args:
        wiki: Wiki instance

    Returns:
        Dict mapping artifact name to freshness status
    """
    current_hash = compute_source_hash(wiki)

    results = {}

    # Check index.md
    index_path = wiki.wiki_dir / "index.md"
    results["index.md"] = _check_artifact_freshness(index_path, current_hash)

    # Check MIND_MAP.md
    mind_map_path = wiki.root / "MIND_MAP.md"
    results["MIND_MAP.md"] = _check_artifact_freshness(mind_map_path, current_hash)

    return results


def _check_artifact_freshness(path: Path, current_hash: str) -> FreshnessStatus:
    """Check freshness of a single artifact."""
    if not path.exists():
        return FreshnessStatus(
            artifact=path.name,
            exists=False,
            is_fresh=False,
            current_hash=current_hash,
        )

    # Read file and extract source hash from header
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Look for source hash in generation header
    # Check first 25 lines to account for frontmatter
    artifact_hash = None
    generated_at = None

    for line in content.split("\n")[:25]:
        if "Source hash:" in line:
            artifact_hash = line.split(":", 1)[1].strip()
        if "Generated:" in line:
            try:
                ts = line.split(":", 1)[1].strip()
                generated_at = datetime.fromisoformat(ts.rstrip("Z"))
            except:
                pass

    is_fresh = artifact_hash == current_hash

    return FreshnessStatus(
        artifact=path.name,
        exists=True,
        is_fresh=is_fresh,
        current_hash=current_hash,
        artifact_hash=artifact_hash,
        generated_at=generated_at,
    )


def rebuild_derived(wiki: Wiki) -> dict:
    """Rebuild all derived artifacts.

    Regenerates index.md and MIND_MAP.md from Tier 1 data.

    Args:
        wiki: Wiki instance

    Returns:
        Dict with rebuild results
    """
    results = {
        "rebuilt": [],
        "errors": [],
    }

    # Rebuild index.md
    try:
        index_content = compile_index(wiki)
        index_path = wiki.wiki_dir / "index.md"

        # Write with frontmatter
        metadata = {
            "title": "Wiki Index",
            "page_type": "index",
            "generated": True,
            "updated": datetime.utcnow().isoformat() + "Z",
        }
        write_page(index_path, metadata, index_content)
        results["rebuilt"].append("index.md")
    except Exception as e:
        results["errors"].append(f"index.md: {e}")

    # Rebuild MIND_MAP.md
    try:
        mind_map_content = compile_mind_map(wiki)
        mind_map_path = wiki.root / "MIND_MAP.md"

        # Write directly (no frontmatter for MIND_MAP)
        with open(mind_map_path, "w", encoding="utf-8") as f:
            f.write(mind_map_content)
        results["rebuilt"].append("MIND_MAP.md")
    except Exception as e:
        results["errors"].append(f"MIND_MAP.md: {e}")

    return results
