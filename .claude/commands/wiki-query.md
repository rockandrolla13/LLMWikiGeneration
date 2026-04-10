Search the wiki and answer a question. $ARGUMENTS

If no question provided, ask what the user wants to know.

Process:
1. First check OMEGA for relevant past queries and learnings
2. Read MIND_MAP.md for orientation
3. Search wiki pages for relevant content
4. Synthesize an answer with citations

```python
from pathlib import Path
from llm_wiki import Wiki, wiki_query, is_omega_available, query_wiki_history, store_wiki_event

wiki = Wiki(Path("."))

# Check OMEGA for past related queries
if is_omega_available():
    past = query_wiki_history("<question_keywords>", wiki.config.name, limit=3)
    if past:
        print("Related past work found in OMEGA memory")

# Query the wiki
result = wiki_query(wiki, "<question>", max_results=5)

if result["success"]:
    print(f"Answer: {result['answer']}")
    print(f"Sources: {result['sources']}")

    # Store the query in OMEGA
    if is_omega_available():
        store_wiki_event(
            "summary",
            f"Query: {question} -> Found {len(result['sources'])} relevant pages",
            wiki_name=wiki.config.name,
        )
```

After answering:
1. Show the synthesized answer with citations
2. Offer to save valuable answers as analysis pages in wiki/analyses/
3. Suggest related questions or topics to explore
