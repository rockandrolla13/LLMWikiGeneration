Add a document to the wiki end-to-end. $ARGUMENTS

**This skill handles the complete pipeline: PDF conversion → duplicate check → wiki ingestion → page creation.**

## Duplicate Detection (SHA-256 Idempotency)

Before creating source pages, content is hashed with SHA-256 to detect:
- **Duplicates**: Same content hash → Skip (enables safe batch re-runs)
- **Updates**: Same slug, different hash → Update existing page
- **New**: No match → Create new page

The `content_hash` field is stored in source frontmatter for tracking.

## Usage

```
/wiki-add path/to/paper.pdf
/wiki-add path/to/document.md
/wiki-add raw/conformal-prediction/*.pdf   # batch mode
```

## Automatic Pipeline

For each document:

### 1. Format Detection & Conversion
- **PDF files**: Auto-convert via pymupdf4llm → `markdown_output/`
- **Markdown files**: Use directly
- **Other formats**: Report unsupported

### 2. Content Analysis (Quick Pass)
Read the converted markdown and extract:
- Title and authors
- Main thesis/contribution (1-2 sentences)
- Key entities (people, organizations)
- Key concepts (ideas, methods)
- Source type (paper, article, book, note)

### 3. Wiki Ingestion
Create/update wiki pages:
- `wiki/sources/<slug>.md` - Source summary
- `wiki/entities/<name>.md` - For each person/org mentioned
- `wiki/concepts/<concept>.md` - For each key concept
- Update `wiki/index.md` with new entries
- Update `MIND_MAP.md` with new nodes

### 4. Cross-Reference Check
- Find related existing pages
- Add bidirectional links
- Flag potential contradictions

## Execution

```bash
# Step 1: Convert if PDF
if [[ "$1" == *.pdf ]]; then
    conda run -n llm-wiki python /media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/test_marker.py "$1"
    SOURCE="markdown_output/$(basename "$1" .pdf).md"
else
    SOURCE="$1"
fi
```

```python
# Step 2-4: Ingest and create pages
from pathlib import Path
from llm_wiki import Wiki, wiki_ingest

wiki = Wiki(Path("."))
result = wiki_ingest(wiki, source_path=Path(SOURCE))

if result["success"]:
    print(f"✓ Source: {result['source_page']}")
    print(f"✓ Created: {result.get('created_pages', [])}")
    print(f"✓ Updated: {result.get('updated_pages', [])}")
```

## Batch Mode

For multiple files:
```
/wiki-add raw/papers/*.pdf
```

Process each file sequentially, reporting:
- Progress: `[3/10] Processing paper-name.pdf...`
- Summary: `Added 10 sources, 15 entities, 23 concepts`

## Options

- `--dry-run`: Show what would be created without writing
- `--skip-existing`: Skip sources already in wiki (by slug)
- `--skip-duplicates`: Skip sources with matching content hash (default: enabled)
- `--no-entities`: Skip entity extraction
- `--no-concepts`: Skip concept extraction

## After Completion

1. Show summary of all pages created/updated
2. Highlight any contradictions found
3. Suggest related queries to explore
4. Offer to commit changes to git
