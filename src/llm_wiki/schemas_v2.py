"""Pydantic v2 schemas for LLM Wiki second-brain (rev 3).

Defines the typed relation vocabulary and PageFrontmatterV2, the canonical
frontmatter model for all wiki pages from P4 onward.

Key design decisions (see docs/SECOND_BRAIN_DESIGN.md):
- ForwardRelType: relations authors write in frontmatter (7 values).
- EdgeRelType: relations returned by graph traversal (7 forward + 7 computed inverses).
- INVERSE_MAP: maps each forward rel to its computed inverse.
- Inverse edges are NEVER persisted to frontmatter; computed at graph-build time.
- schema_version defaults to 1; P9 migrate.py stamps it to 2 after backfill.
"""

from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Relation type literals
# ---------------------------------------------------------------------------

ForwardRelType = Literal[
    "extends",
    "special-case-of",
    "supersedes",
    "contradicts",
    "refutes",
    "depends-on",
    "was-response-to",
]

EdgeRelType = Literal[
    # Forward
    "extends",
    "special-case-of",
    "supersedes",
    "contradicts",
    "refutes",
    "depends-on",
    "was-response-to",
    # Computed inverses
    "extended-by",
    "generalizes",
    "superseded-by",
    "refuted-by",
    "required-by",
    "prompted",
]

# Maps each forward relation to its computed inverse.
# "contradicts" is self-inverse; both directions are forward.
INVERSE_MAP: dict[str, str] = {
    "extends": "extended-by",
    "special-case-of": "generalizes",
    "supersedes": "superseded-by",
    "contradicts": "contradicts",  # symmetric
    "refutes": "refuted-by",
    "depends-on": "required-by",
    "was-response-to": "prompted",
}


# ---------------------------------------------------------------------------
# Sub-models
# ---------------------------------------------------------------------------


class RelationSpec(BaseModel):
    """A single typed edge in the forward relations block."""

    target: str = Field(
        ...,
        description=(
            "Target page identifier. Pre-P9: page_id slug. "
            "Post-P9 migration: UUID string."
        ),
    )
    rel: ForwardRelType = Field(
        ...,
        description="Relation type. Must be one of the seven ForwardRelType values.",
    )


class VerificationSpec(BaseModel):
    """Verification metadata for a wiki page."""

    status: Literal["verified", "partial", "unverified", "disputed"] = Field(
        default="unverified",
        description="Overall verification status of the page content.",
    )
    unverified_claims: int = Field(
        default=0,
        ge=0,
        description="Count of claims flagged as unverified within the page body.",
    )


# ---------------------------------------------------------------------------
# Primary frontmatter model
# ---------------------------------------------------------------------------


class PageFrontmatterV2(BaseModel):
    """Canonical YAML frontmatter schema for LLM Wiki pages (schema_version >= 1).

    All fields match the YAML keys written to disk. Validation is intentionally
    lenient on optional fields so that existing v1 pages parse without error.
    """

    # Schema discriminator — 1 = v1 default; 2 = stamped by P9 migrate
    schema_version: int = Field(
        default=1,
        description="Schema version. 1 = v1 (no UUID/authored-region); 2 = fully migrated.",
    )

    # Core identity
    title: str = Field(..., description="Human-readable page title.")
    page_id: str = Field(
        ...,
        description="Stable slug identifier, e.g. 'concepts/attention_mechanism'.",
    )
    uuid: Optional[str] = Field(
        default=None,
        description="Stable UUID assigned by P1 identity.py. None until P9 migration.",
    )
    page_type: str = Field(
        ...,
        description="Page type: concept | source | entity | analysis | contradiction.",
    )

    # Revision tracking
    revision_id: int = Field(default=1, ge=1)
    content_hash: Optional[str] = Field(
        default=None,
        description=(
            "SHA-256 hash of the authored region only (format: 'sha256:<hex>'). "
            "Computed by io.authored_hash.compute_authored_hash(). "
            "None until authored-region markers are present."
        ),
    )

    # Timestamps
    created: str = Field(..., description="ISO 8601 creation timestamp string.")
    updated: str = Field(..., description="ISO 8601 last-updated timestamp string.")
    updated_by: str = Field(
        ...,
        description="Reference to op_id from manifest.jsonl, or agent/author identifier.",
    )

    # Quality
    verification: VerificationSpec = Field(default_factory=VerificationSpec)

    # Classification
    tags: list[str] = Field(default_factory=list)
    sources: list[str] = Field(
        default_factory=list,
        description="page_id slugs (or UUIDs post-P9) of source pages.",
    )

    # Typed knowledge graph (forward edges only — inverses are computed)
    relations: list[RelationSpec] = Field(
        default_factory=list,
        description=(
            "Forward-direction typed edges. "
            "Inverse edges are computed at graph-build time; never persisted here."
        ),
    )

    # MIND_MAP hints
    mind_map_priority: str = Field(
        default="medium",
        description="MIND_MAP inclusion priority: high | medium | low | exclude.",
    )

    class Config:
        # Allow extra fields from existing v1 pages (e.g. related, mind_map_category)
        extra = "allow"
