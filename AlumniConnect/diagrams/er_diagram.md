# ER Diagram

```mermaid
erDiagram
DEPARTMENTS ||--o{ ALUMNI : contains
ALUMNI ||--o{ EDUCATION : has
ALUMNI ||--o{ CAREER_HISTORY : has
COMPANIES ||--o{ CAREER_HISTORY : employs
ALUMNI ||--o{ ALUMNI_SKILLS : has
SKILLS ||--o{ ALUMNI_SKILLS : includes
ALUMNI ||--o| MENTORSHIP : offers
ALUMNI ||--o| USERS : authenticates
```
