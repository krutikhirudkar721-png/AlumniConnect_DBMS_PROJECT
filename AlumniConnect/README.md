# AlumniConnect

## Alumni Management & Career Tracking System

AlumniConnect is an academic DBMS project developed to manage alumni information and track their academic background, career history, skills, mentorship availability, and professional details.

The system provides role-based access for administrators and alumni, along with a searchable alumni directory, dashboard, reports, and database-driven management features.

---

## Technology Stack

- **Database:** MySQL 8.x
- **Backend:** Python 3.11+ with Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Database Connector:** MySQL Connector/Python
- **Testing:** Pytest
- **Production Server:** Gunicorn
- **Development Environment:** Visual Studio Code
- **Database Tool:** MySQL Workbench

---

## Main Features

### 1. Role-Based Authentication

- Secure login system
- Password hashing
- Session-based authentication
- Role-based authorization
- Admin and Alumni roles

### 2. Admin Features

- View alumni directory
- Add new alumni
- Edit alumni information
- Delete alumni records
- Manage academic and professional information
- View dashboard statistics
- Access reports and analytics

### 3. Alumni Features

- Login securely
- View alumni directory
- View detailed alumni profiles
- View academic information
- View career information
- View skills and mentorship details
- Edit their own profile

### 4. Alumni Directory

The directory supports multi-filter searching using:

- Name
- Department
- Graduation year
- Company
- Designation
- Industry
- Location
- Skill
- Mentorship availability
- Minimum experience

Multiple filters can be combined using **AND logic**.

### 5. Academic Information

The system stores:

- Degree
- Institution
- Field of study
- Enrollment year
- Graduation year

### 6. Career Management

The system supports:

- Current employment
- Previous employment
- Company
- Industry
- Designation
- Job location
- Start date
- End date
- Current job status

### 7. Skills Management

Skills are implemented using a **many-to-many relationship** between alumni and skills through the `alumni_skills` junction table.

Skill levels supported:

- Beginner
- Intermediate
- Advanced
- Expert

### 8. Mentorship

Alumni can be marked as available for mentorship.

Mentorship information includes:

- Availability
- Domain
- Topics
- Availability details

### 9. Dashboard & Reports

The dashboard provides statistics such as:

- Total alumni
- Total departments
- Total companies
- Total skills
- Available mentors
- Alumni distribution by department
- Alumni distribution by graduation year

---

## Database Design

The database follows a normalized relational design and is designed around **Third Normal Form (3NF)**.

### Main Tables

- `departments`
- `alumni`
- `users`
- `education`
- `companies`
- `career_history`
- `skills`
- `alumni_skills`
- `mentorship`

### Database Relationships

- One department can have many alumni.
- One alumni can have multiple education records.
- One alumni can have multiple career history records.
- One company can have multiple career history records.
- Alumni and skills have a many-to-many relationship.
- One alumni can have one mentorship record.
- A user account can be linked to an alumni record.

The project also includes the database view:

- `alumni_directory_view`

---

## Database Features Demonstrated

The project demonstrates important DBMS concepts including:

- DDL (Data Definition Language)
- DML (Data Manipulation Language)
- DQL (Data Query Language)
- TCL (Transaction Control Language)
- Primary Keys
- Foreign Keys
- Unique Constraints
- NOT NULL Constraints
- CHECK Constraints
- DEFAULT Values
- Indexes
- JOIN operations
- Aggregate functions
- GROUP BY
- HAVING
- Subqueries
- EXISTS / NOT EXISTS
- Views
- Transactions
- Parameterized SQL queries
- Many-to-many relationships
- Normalization up to 3NF

---

## Project Structure

```text
AlumniConnect/
│
├── app/
│   ├── alumni/
│   │   └── routes.py
│   │
│   ├── auth/
│   │   └── routes.py
│   │
│   ├── database/
│   │   └── connection.py
│   │
│   ├── reports/
│   │   └── routes.py
│   │
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   │
│   ├── templates/
│   │   ├── add_alumni.html
│   │   ├── alumni.html
│   │   ├── alumni_profile.html
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── edit_alumni.html
│   │   ├── login.html
│   │   └── ...
│   │
│   └── __init__.py
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
│   └── ...
│
├── .env.example
├── .gitignore
├── config.py
├── README.md
├── requirements.txt
└── run.py
