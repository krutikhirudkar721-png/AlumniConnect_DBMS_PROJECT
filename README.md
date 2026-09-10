# 🎓 AlumniConnect

### Alumni Management & Career Tracking System

AlumniConnect is a database-driven web application developed as an academic **DBMS project** to manage alumni information and track their academic, professional, skills, and mentorship details.

The system provides role-based access for **Administrators and Alumni** and offers a searchable alumni directory with multiple filtering options.

---

## 🚀 Features

- 🔐 Role-based authentication (Admin & Alumni)
- 👥 Alumni management and CRUD operations
- 🎓 Academic / Education information
- 💼 Career history and current employment
- 🏢 Company and industry management
- 🛠️ Skills management using Many-to-Many relationships
- 🤝 Alumni mentorship availability
- 🔎 Advanced multi-filter alumni search
- 📊 Dashboard and reports
- 🗃️ MySQL relational database
- 🔒 Password hashing and parameterized SQL queries
- 📈 Database indexes, constraints and views
- 🔄 Transaction handling
- 📐 ER Diagram and normalized database design

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| MySQL | Database |
| HTML5 | Frontend structure |
| CSS3 | Styling |
| JavaScript | Client-side functionality |
| Gunicorn | Production server |
| Pytest | Testing |

---

## 🗄️ Database Design

The database is designed according to relational database principles and normalized up to **3NF (Third Normal Form)**.

### Main Entities

- `users`
- `alumni`
- `departments`
- `education`
- `companies`
- `career_history`
- `skills`
- `alumni_skills`
- `mentorship`

### DBMS Concepts Implemented

- Primary Keys
- Foreign Keys
- Unique Constraints
- NOT NULL Constraints
- CHECK Constraints
- Default Values
- Indexes
- JOINs
- Aggregate Functions
- GROUP BY / HAVING
- Subqueries
- EXISTS / NOT EXISTS
- Views
- Transactions
- Many-to-Many relationships
- Parameterized SQL queries

---

## 🔎 Alumni Search

The alumni directory supports multiple filters including:

- Name
- Graduation Year
- Department
- Company
- Designation
- Industry
- Location
- Skill
- Mentorship Availability
- Minimum Experience

Multiple filters can be combined to perform advanced searches.

---

## 📁 Project Structure

```text
AlumniConnect/
│
├── app/
│   ├── alumni/
│   ├── auth/
│   ├── database/
│   ├── reports/
│   ├── static/
│   └── templates/
│
├── database/
│   ├── schema.sql
│   ├── sample_data.sql
│   └── seed_admin.py
│
├── docs/
│   └── ER_Diagram.png
│
├── tests/
│
├── config.py
├── requirements.txt
├── run.py
└── README.md
