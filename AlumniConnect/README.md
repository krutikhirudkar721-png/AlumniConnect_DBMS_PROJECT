# AlumniConnect
Alumni Management & Career Tracking System — academic DBMS project.

## Stack
MySQL + Python + Flask + HTML5 + CSS3 + JavaScript.

## Setup
1. Install Python 3.11+ and MySQL 8.x.
2. Create a virtual environment and run `pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` and set MySQL credentials.
4. Run `database/schema.sql` in MySQL Workbench.
5. Run `python database/seed_admin.py`, replace the two password placeholders in `database/sample_data.sql`, then run that SQL file.
6. Run `python run.py` and open `http://127.0.0.1:5000/login`.

Demo passwords: Admin@123 and Alumni@123.

Features: role-based login, alumni CRUD, education, career history, skills M:N model, mentorship, multi-filter search, dashboard, reports, SQL view, constraints, indexes and transaction examples.
