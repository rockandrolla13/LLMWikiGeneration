Initialize a new LLM Wiki. $ARGUMENTS

Before creating the wiki, ask the user:
1. What topic or domain will this wiki focus on?
2. What name should the wiki have?
3. What profile fits best? (research, reading, personal, business)

Then execute:

```python
from pathlib import Path
from llm_wiki import wiki_init, is_omega_available, store_wiki_event

# Initialize the wiki
result = wiki_init(
    root_dir=Path("."),  # or user-specified path
    name="<wiki_name>",
    topic="<topic>",
    profile="<profile>",
)

if result["success"]:
    print(f"Wiki initialized: {result['message']}")

    # Store this decision in OMEGA for cross-session memory
    if is_omega_available():
        store_wiki_event(
            "decision",
            f"Initialized wiki '{result.get('name', 'wiki')}' focused on {topic}",
            wiki_name=result.get('name', 'wiki'),
        )
else:
    print(f"Error: {result['error']}")
```

After initialization, explain:
1. The directory structure created (raw/, wiki/, schema.yml, manifest.jsonl)
2. How to add sources (drop files in raw/)
3. Next step: use /wiki-ingest to add first source
