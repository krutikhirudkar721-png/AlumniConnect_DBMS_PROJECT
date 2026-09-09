# AlumniConnect Project Report

## Abstract
AlumniConnect is a centralized database-driven web application for managing alumni information and career progression using a normalized MySQL database and Flask backend.

## Aim
To maintain structured alumni data, track careers, support search/filtering and provide useful DBMS reports.

## Modules
Authentication, authorization, dashboard, alumni management, directory/search, education, career history, skills, mentorship and reports.

## Database
users, departments, alumni, education, companies, career_history, skills, alumni_skills and mentorship.

## Normalization
The schema follows 3NF-oriented principles. Multi-valued skills and historical career data are separated; department and company master data reduce duplication.

## Security
Passwords are hashed with Werkzeug, SQL uses parameters, admin routes use server-side authorization and secrets are loaded from environment variables.

## DBMS Concepts
PK, FK, UNIQUE, NOT NULL, CHECK, defaults, 1:N, M:N, joins, aggregates, GROUP BY, HAVING, subqueries, EXISTS, views, indexes and transactions.

## Limitations
Student accounts, password reset, email verification and advanced exports are outside the baseline scope.

## Future Scope
Student access, notifications, events, exports, advanced charts and multi-institution support.
