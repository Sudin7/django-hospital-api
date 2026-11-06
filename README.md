# Hospital Management System

A web-based Hospital Management System built using **Python, Django, and Django REST Framework (DRF)**. This project helps manage hospital staff and patient records through an organized backend system.

## Features

- **User Authentication:** User registration and login.
- **Staff Management:** Manage hospital staff information.
- **Patient Management:** Staff can add and manage patient records.
- **Patient Records:** Store patient details, contact information, gender, and admission dates.
- **REST API:** API endpoints for managing staff and patient data.
- **Database Management:** Relational database management using Django ORM.

## Tech Stack

- **Backend:** Python, Django
- **API:** Django REST Framework
- **Database:** PostgreSql
- **API Testing:** Postman
- **Version Control:** Git & GitHub



## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sudin7/django-hospital-api.git
cd django-hospital-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open your browser at:

`http://127.0.0.1:8000/`

## API

The project provides REST API endpoints for staff and patient management.

Base URL:

```text
/api/v1/
```

API endpoints depend on the configured routes in the API application.

## Learning Objectives

This project was developed to gain practical experience with:

- Django project architecture
- Django models and ORM
- User authentication
- CRUD operations
- Foreign Key relationships
- Django REST Framework
- RESTful API development
- API testing using Postman

