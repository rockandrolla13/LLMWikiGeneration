# Architecture Review: LLM Wiki

**Review Date:** 2026-04-07
**Codebase Version:** Phase 4 Complete
**Overall Score:** 6/10

---

## EXECUTIVE SUMMARY

The llm_wiki codebase has **solid foundational architecture** (clear Tier 1 vs Tier 2 separation, good schema definitions, pluggable search backends) but suffers from **critical cohesion problems** in 5 areas that severely limit extensibility.

| Dimension | Score | Assessment |
|-----------|-------|------------|
| Boundary Quality | 5/10 | Mixed modules - some focused, some over-broad |
| Dependency Direction | 7/10 | Generally good, minor lazy-loading issues |
| Abstraction Fitness | 5/10 | Concrete where abstract needed |
| Rate-of-Change Alignment | 4/10 | High-change modules tightly coupled |
| Extensibility | 5/10 | Adding features requires multi-file edits |

---

## CRITICAL FINDINGS (Severity: HIGH)

### 1. FRONTMATTER.PY - MULTI-CONCERN MODULE
**File:** `src/llm_wiki/frontmatter.py`

**Issue:** This module handles 4 distinct concerns:
- YAML frontmatter parsing/writing
- SHA-256 content hashing
- Wikilink extraction (regex)
- Page ID normalization

**Evidence:**
```python
# frontmatter.py lines 123-155 - YAML parsing
def parse_page(path: Path) -> tuple[dict, str]:

# frontmatter.py lines 166-174 - SHA-256 hashing
def compute_content_hash(content: str) -> str:
def compute_file_hash(path: Path) -> str:

# frontmatter.py lines 177-181 - regex wikilink extraction
def extract_wikilinks(content: str) -> list[str]:

# frontmatter.py lines 193-198 - string normalization
def normalize_page_id(name: str) -> str:
```

**Recommendation:** Split into:
- `io/page_io.py` - YAML frontmatter parsing/writing
- `security/hashing.py` - SHA-256 hashing
- `markup/wikilinks.py` - wikilink extraction
- `naming/page_ids.py` - page ID normalization

---

### 2. WIKI.PY - GOD CLASS PATTERN
**File:** `src/llm_wiki/wiki.py`

**Issue:** Wiki class handles:
- Path management (6 properties)
- Directory initialization (70 lines)
- Page read/write operations
- Statistics computation
- Logging operations

**Evidence:** The class has implicit dependencies on frontmatter, config, and manifest via lazy loading pattern.

**Recommendation:** Split into:
- `WikiPaths` - Path management and resolution
- `WikiState` - State queries (list_pages, get_page, get_stats)
- `WikiMutations` - Write operations (init, ingest)
- `WikiFactories` - Object construction

---

### 3. COMMANDS.PY - PAGE CONSTRUCTION EXPLOSION
**File:** `src/llm_wiki/commands.py`

**Issue:** `wiki_ingest()` (150 lines) constructs SourcePage, EntityPage, and ConceptPage objects directly with hardcoded defaults. Every new page type requires changes here.

**Evidence:** Lines 159-310 show extensive manual object construction with 10+ conditional branches.

**Recommendation:** Create page factories:
```python
# BEFORE
meta = PageMeta(
    title=title,
    page_id=page_id,
    page_type=PageType.SOURCE,
    revision_id=1,
    # ... 8 more defaults
)

# AFTER
source_page = SourcePageFactory.from_ingestion(
    source_path, title, source_type, authors=authors
)
```

---

### 4. DERIVED.PY - HARDCODED ARTIFACT EXPANSION
**File:** `src/llm_wiki/derived.py`

**Issue:** Adding a new derived artifact (e.g., TIMELINE.md) requires changes to 5 functions:
- `check_freshness()` - Add artifact path check
- `rebuild_derived()` - Add rebuild branch
- `compile_mind_map()` - Integrate new artifact refs
- Module docstring - Document new artifact
- `__init__.py` - Export new compiler

**Recommendation:** Registry pattern:
```python
DerivedArtifactRegistry.register(DerivedArtifact(
    name="TIMELINE.md",
    path=lambda wiki: wiki.root / "TIMELINE.md",
    compiler=compile_timeline,
))
# check_freshness() and rebuild_derived() work automatically
```

---

### 5. VERIFY.PY - MONOLITHIC VERIFICATION FUNCTIONS
**File:** `src/llm_wiki/verify.py`

**Issue:** Page iteration pattern is duplicated 3+ times across verification functions.

**Evidence:**
```python
# Lines 175-202 - verify_page_frontmatter
for page_path in wiki.list_pages():  # ITERATION
    # ...

# Lines 205-238 - verify_revision_hashes
for page_path in wiki.list_pages():  # DUPLICATED ITERATION
    # ...

# Lines 241-276 - verify_page_ids
for page_path in wiki.list_pages():  # DUPLICATED AGAIN
    # ...
```

**Recommendation:** Visitor pattern with PageBasedCheck base class:
```python
class FrontmatterCheck(PageBasedCheck):
    def check_page(self, page_path: Path, wiki: Wiki) -> list[str]:
        # Logic only - no iteration needed
```

---

## MODERATE FINDINGS (Severity: MEDIUM)

### 6. CONFIG LOADING - SILENT FAILURES
**File:** `src/llm_wiki/config.py:195-207`

Empty YAML file returns default config silently. Should fail fast.

### 7. MANIFEST SERIALIZATION - DUPLICATED LOGIC
**File:** `src/llm_wiki/manifest.py:145-192`

`to_json_line()` and `from_json_line()` have inverse field mappings that must stay in sync.

### 8. SEARCH BACKEND - SUBPROCESS ERROR HANDLING
**File:** `src/llm_wiki/search.py:287-329`

Silent exception swallowing, no logging, potential shell injection.

---

## MINOR FINDINGS (Severity: LOW)

### 9. WIKILINKS - REGEX IMPORTED IN FUNCTION
**File:** `src/llm_wiki/frontmatter.py:177-181`

`import re` inside function body instead of module level.

---

## PRIORITY REFACTORING ROADMAP

| Phase | Priority | Effort | Tasks |
|-------|----------|--------|-------|
| 1 | CRITICAL | 2-3 days | Split frontmatter.py, create page factories, create artifact registry |
| 2 | HIGH | 2-3 days | Decompose Wiki class, add dependency injection |
| 3 | MEDIUM | 1-2 days | Create VerificationCheck base class, improve error handling |
| 4 | LOW | 1 day | Fix manifest serialization, add logging |

---

## CONCLUSION

**Primary issue:** High-change modules (wiki.py, commands.py, derived.py, verify.py) lack proper abstraction boundaries, forcing multi-file edits for new features.

**Implementing Phase 1-2 refactorings would:**
- Reduce code duplication (eliminate 3x page iteration in verify.py)
- Enable plugin-based extensibility (new artifacts/checks without modifying core)
- Improve testability (eliminate hidden dependencies)
- Reduce friction for feature addition (single-file edits vs multi-file changes)

**Estimated effort:** 20-25 hours for full refactor
**Payoff:** 10x reduction in friction for adding new verification checks, artifacts, or commands
