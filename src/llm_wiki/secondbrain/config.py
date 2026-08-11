"""Where the Second Brain keeps its data.

Everything lives under one directory so it can be moved, backed up or deleted
in one go. The default is ``secondbrain/`` at the repository root, which is
gitignored -- this repository is public, and captured notes are not.

The vault is a plain folder of markdown files. Obsidian can open it directly.
It is deliberately *not* inside ``wiki/``: that vault has schema-v2 frontmatter,
provenance checking and a hand-curated MIND_MAP, and dropping untyped notes into
it would fail the integrity checks and pollute the index rebuild.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from .models import DEFAULT_CONFIDENCE_THRESHOLD

#: Directory name used for the Second Brain root, relative to the repo root.
DEFAULT_ROOT_NAME = "secondbrain"


def _repo_root() -> Path:
    """Return the repository root, found by walking up from this file."""
    return Path(__file__).resolve().parents[3]


@dataclass(frozen=True)
class SecondBrainConfig:
    """Resolved locations and thresholds.

    Attributes:
        root: The Second Brain directory.
        db_path: SQLite file holding nodes, edges, captures and events.
        vault_path: Markdown output folder, safe to open in Obsidian.
        confidence_threshold: Below this, a capture goes to needs_review.
    """

    root: Path
    db_path: Path
    vault_path: Path
    confidence_threshold: float = DEFAULT_CONFIDENCE_THRESHOLD

    @classmethod
    def resolve(cls, root: Path | str | None = None) -> "SecondBrainConfig":
        """Build a config from an explicit root, the environment, or the default.

        Precedence is explicit argument, then ``SECONDBRAIN_ROOT``, then
        ``secondbrain/`` beside the repository root. ``SECONDBRAIN_DB`` and
        ``SECONDBRAIN_VAULT`` override the two paths individually, and
        ``SECONDBRAIN_CONFIDENCE_THRESHOLD`` overrides the threshold.

        Args:
            root: Explicit root directory, if the caller has one.

        Returns:
            A resolved config. No directories are created here.
        """
        resolved_root = Path(
            root or os.environ.get("SECONDBRAIN_ROOT") or _repo_root() / DEFAULT_ROOT_NAME
        )
        db = os.environ.get("SECONDBRAIN_DB")
        vault = os.environ.get("SECONDBRAIN_VAULT")
        threshold = os.environ.get("SECONDBRAIN_CONFIDENCE_THRESHOLD")
        return cls(
            root=resolved_root,
            # The dot-prefixed data directory keeps the database out of
            # Obsidian's file tree; Obsidian hides dot directories.
            db_path=Path(db) if db else resolved_root / ".data" / "secondbrain.db",
            vault_path=Path(vault) if vault else resolved_root / "vault",
            confidence_threshold=(
                float(threshold) if threshold else DEFAULT_CONFIDENCE_THRESHOLD
            ),
        )

    def ensure_dirs(self) -> None:
        """Create the data and vault directories if they do not exist."""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.vault_path.mkdir(parents=True, exist_ok=True)
