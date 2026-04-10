Store a decision, lesson, or note in OMEGA memory. $ARGUMENTS

Use this to explicitly save something for future sessions.

Types:
- decision: A choice made about the wiki (architecture, naming, organization)
- lesson: Something learned (what works, what doesn't, patterns discovered)
- error: A mistake to avoid in the future

```python
from pathlib import Path
from llm_wiki import Wiki, is_omega_available, store_wiki_event, store_lesson

if not is_omega_available():
    print("OMEGA not installed. Install with: pip install omega-memory[server]")
    exit()

wiki = Wiki(Path("."))

# Parse the user's input
# $ARGUMENTS contains: "<type>: <content>" or just "<content>"

# Store the memory
if "<type>" == "lesson":
    result = store_lesson("<content>", wiki.config.name)
else:
    result = store_wiki_event(
        event_type="<type>",  # decision, lesson, error
        content="<content>",
        wiki_name=wiki.config.name,
    )

if result:
    print(f"Stored {type}: {content}")
    print("This will be surfaced in future sessions when relevant.")
else:
    print("Failed to store memory")
```

Examples:
- /wiki-remember decision: Use ISO dates in all frontmatter
- /wiki-remember lesson: Entity pages need at minimum a description and first source
- /wiki-remember error: Don't create concept pages for trivial terms
