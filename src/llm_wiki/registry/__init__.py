"""Registry package for pluggable LLM Wiki components.

This package provides default registries for verification checks and
artifact compilers. These registries enable extensibility - users can
add custom checks and compilers alongside the built-in ones.

Default registries are pre-populated with standard implementations:
- Verification checks: frontmatter, links, bidirectional links, etc.
- Artifact compilers: index.md, log.md, mind_map nodes

Usage:
    from llm_wiki.registry import get_default_checks, get_default_compilers

    # Run all default verification checks
    checks = get_default_checks()
    for check in checks.all():
        result = check.execute(wiki)

    # Compile all default derived artifacts
    compilers = get_default_compilers()
    for compiler in compilers.all():
        content = compiler.compile(wiki)

Extensibility:
    from llm_wiki.registry import default_checks
    from llm_wiki.core.protocols import VerificationCheck

    class CustomCheck:
        @property
        def name(self) -> str:
            return "My Custom Check"

        def execute(self, wiki) -> VerificationResult:
            # Custom logic here
            ...

    default_checks.register("custom", CustomCheck())
"""

from .checks import default_checks, get_default_checks
from .compilers import default_compilers, get_default_compilers

__all__ = [
    "default_checks",
    "get_default_checks",
    "default_compilers",
    "get_default_compilers",
]
