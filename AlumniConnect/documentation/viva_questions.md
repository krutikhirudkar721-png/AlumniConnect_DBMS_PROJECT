# Viva Questions

### Why MySQL?
It is a relational DBMS supporting keys, constraints, joins, aggregation, views, indexes and transactions required by the project.

### Why separate skills?
Skills are many-to-many: one alumnus has many skills and one skill belongs to many alumni. The junction table implements this relationship without comma-separated data.


### Why separate career history?
An alumnus can have multiple jobs, so a separate table preserves career progression and avoids repeating attributes.

### What is 3NF?
A normalization level designed to reduce redundancy by ensuring non-key attributes depend on the key rather than other non-key attributes.

### Why GROUP BY and HAVING?
GROUP BY creates aggregate groups; HAVING filters groups after aggregation.

### What is an index?
A data structure that can speed up common searches/joins at the cost of storage and write overhead.

### What is a transaction?
A logical unit of database work. COMMIT persists it; ROLLBACK reverses uncommitted changes.

### How is SQL injection prevented?
User values are passed as bound parameters instead of concatenated into SQL.

### How are passwords protected?
Only password hashes are stored.
