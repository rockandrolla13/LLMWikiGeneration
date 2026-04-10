---
title: Dashboard
---

# Wiki Dashboard

## Recent Pages
```dataview
TABLE page_type AS "Type", updated AS "Updated"
FROM ""
WHERE page_type
SORT updated DESC
LIMIT 10
```

## Pages by Type
```dataview
TABLE length(rows) AS "Count"
FROM ""
WHERE page_type
GROUP BY page_type
```

## Sources
```dataview
LIST
FROM "sources"
SORT file.name ASC
```

## Entities
```dataview
LIST
FROM "entities"
SORT file.name ASC
```

## Concepts
```dataview
LIST
FROM "concepts"
SORT file.name ASC
```

## Orphan Pages (no inbound links)
```dataview
LIST
FROM ""
WHERE length(file.inlinks) = 0
```
