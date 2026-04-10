Interactive guide for using LLM Wiki. $ARGUMENTS

Show the user how to use the wiki step by step.

```python
from llm_wiki import wiki_guide, wiki_help, wiki_structure, is_omega_available

# Get overview
guide = wiki_guide()
print(f"LLM Wiki - {guide['total_steps']} step guide")
print()
for step_num, title in guide['steps'].items():
    print(f"  {step_num}. {title}")
print()
print("Quick start:")
for item in guide['quick_start']:
    print(f"  {item}")
```

If user asks for a specific step, show detailed instructions:
- Step 1: Initialize wiki (wiki_guide(step=1))
- Step 2: Add source documents
- Step 3: Query the wiki
- Step 4: Organize by topics
- Step 5: Maintain the wiki
- Step 6: Use sessions

Also explain:
- OMEGA integration for cross-session memory
- The 3-tier data model (source of truth, derived, ephemeral)
- Available slash commands: /wiki-init, /wiki-ingest, /wiki-query, /wiki-status
