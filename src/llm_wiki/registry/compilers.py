"""Default derived artifact compiler registry.

This module provides the default registry of artifact compilers.
Each compiler implements the DerivedArtifactCompiler protocol and
generates a specific derived artifact from Tier 1 wiki data.

Compilers:
    - IndexCompiler: Generates wiki/index.md master catalog
    - MindMapCompiler: Generates MIND_MAP.md knowledge graph

Usage:
    from llm_wiki.registry import get_default_compilers

    compilers = get_default_compilers()
    for compiler in compilers.all():
        content = compiler.compile(wiki)
        path = compiler.path(wiki)
        path.write_text(content)
"""

from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

from ..core.protocols import ArtifactRegistry

if TYPE_CHECKING:
    from ..wiki import Wiki


# Generation header template - matches derived.py
GENERATION_HEADER = """<!--
AUTO-GENERATED FILE - DO NOT EDIT MANUALLY
Generated: {timestamp}
Generator: llm-wiki {version}
Source hash: {source_hash}
Rebuild with: wiki:rebuild
-->

"""


class IndexCompiler:
    """Compiler for wiki/index.md (lightweight summary) and wiki/index.full.md (full catalog).

    Writes two files:
    - index.md: one line per page for query routing (small, fast to load)
    - index.full.md: full catalog with summaries and stats (for maintenance/status)
    """

    @property
    def name(self) -> str:
        """Artifact filename (primary output)."""
        return "index.md"

    def path(self, wiki: "Wiki") -> Path:
        """Full path where the primary artifact (lightweight summary) is written."""
        return wiki.wiki_dir / "index.md"

    def compile(self, wiki: "Wiki") -> str:
        """Generate index.md (lightweight summary) and write index.full.md as a side effect.

        Args:
            wiki: Wiki instance to compile from

        Returns:
            Markdown content for the lightweight index.md
        """
        from ..derived import compile_index_summary, compile_index
        from ..io import write_page

        # Write the full catalog as a side effect
        full_content = compile_index(wiki)
        index_full_path = wiki.wiki_dir / "index.full.md"
        metadata_full = {
            "title": "Wiki Index (Full)",
            "page_type": "index",
            "generated": True,
            "updated": datetime.utcnow().isoformat() + "Z",
        }
        write_page(index_full_path, metadata_full, full_content)

        # Return the lightweight summary for index.md
        return compile_index_summary(wiki)

    @property
    def needs_frontmatter(self) -> bool:
        """Whether to wrap content in YAML frontmatter."""
        return True


class MindMapCompiler:
    """Compiler for MIND_MAP.md knowledge graph.

    Generates a grep-friendly single-file synthesis with:
    - Numbered nodes [N] on single lines
    - Routing nodes [1-5] as hubs
    - Cross-references embedded naturally
    - 150-400 words per node
    """

    @property
    def name(self) -> str:
        """Artifact filename."""
        return "MIND_MAP.md"

    def path(self, wiki: "Wiki") -> Path:
        """Full path where artifact should be written."""
        return wiki.root / "MIND_MAP.md"

    def compile(self, wiki: "Wiki") -> str:
        """Generate MIND_MAP.md content.

        Args:
            wiki: Wiki instance to compile from

        Returns:
            Markdown content for MIND_MAP.md
        """
        from .. import __version__
        from ..derived import gather_page_info, compute_source_hash

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
        by_type: dict[str, list] = {
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

    @property
    def needs_frontmatter(self) -> bool:
        """Whether to wrap content in YAML frontmatter."""
        return False


# Module-level registry instance
# Compilers are registered here during module initialization
default_compilers: ArtifactRegistry = ArtifactRegistry()

# Register built-in compilers
default_compilers.register("index", IndexCompiler())
default_compilers.register("mind_map", MindMapCompiler())


def get_default_compilers() -> ArtifactRegistry:
    """Get the default artifact compiler registry.

    Returns a registry pre-populated with all built-in artifact compilers.
    Use this to regenerate all derived artifacts for a wiki.

    Returns:
        ArtifactRegistry with default compilers registered
    """
    return default_compilers
