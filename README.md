# Personal Portfolio Website

A responsive portfolio website developed as part of a school project using **Django**, **Bootstrap 5**, **Python**, **HTML**, **CSS**, and **JavaScript**. This version expands upon the original portfolio by integrating a **Django backend** and **SQLite database** to dynamically display personal information and projects. The project demonstrates the use of the Django framework, Git version control, GitHub repository management, Bootstrap for responsive web design, and database-driven web development.

## Features

* One-page portfolio
* Modern gradient user interface
* About Me section
* Projects section
* Contact section
* Bootstrap 5 responsive layout
* Django template inheritance
* Static file management with Django
* SQLite database integration
* Django Admin
* Admin/superuser-only sign-in
* Admin dashboard for managing projects and technology stacks
* Add new projects through the dashboard
* Add new technology stacks through the dashboard
* Many-to-many relationship between projects and technology stacks
* Automatic display of newly added projects and technology stacks on the portfolio

## Built With

* Python
* Django
* SQLite
* Bootstrap 5 (CDN)
* HTML5
* CSS3
* JavaScript
* Git
* GitHub

## Requirements

- Python
- pip
- Git

## Project Structure

```text
Portfolio/
│
├── main/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── portfolio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/gkurtthomas/portfolio-site.git
```

### 2. Navigate to the project directory

```bash
cd Portfolio
```

### 3. Create and activate a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the same directory as `manage.py`.

Use `.env.example` as a guide:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

The `.env` file contains environment-specific configuration and should not be committed to the repository.

### 6. Apply the database migrations

Run:

```bash
python manage.py migrate
```

The database file is not included in the repository. Django will create the SQLite database and its required tables using the migrations included in the project.

### 7. Create a superuser

Create an administrator account for the dashboard:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter the username, email address, and password.

Only Django superusers are allowed to sign in to the portfolio dashboard.

### 8. Run the Django development server

```bash
python manage.py runserver
```

### 9. Open the website

Visit:

```text
http://127.0.0.1:8000/
```

## Admin Dashboard

The admin sign-in page is available at:

```text
http://127.0.0.1:8000/signin/
```

Only users with Django superuser privileges can successfully authenticate through this page.

After signing in, the user is redirected to:

```text
http://127.0.0.1:8000/dashboard/
```

The dashboard contains sections for managing projects and technology stacks.

### Projects

The Projects table displays:

* Project Name
* Description
* Tech Stack
* Link

Project descriptions displayed in the dashboard are truncated to 50 characters.

Projects can be added through the **Add Project** button.

The project form contains:

* Project Name
* Project Description
* Tech Stacks
* Link

Multiple technology stacks can be selected for a single project.

### Tech Stacks

The Tech Stacks table displays:

* Tech Stack Name
* Project It Was Used
* Date Added

Technology stacks can be added through the **Add Tech Stack** button.

Duplicate technology stack names are prevented. A single technology stack can be associated with multiple projects.

### Public Portfolio Updates

Projects and technology stacks added through the dashboard are automatically reflected in the public portfolio.

## Database

This project uses SQLite as its database during development.

The SQLite database file is intentionally excluded from the repository.

When setting up a fresh copy of the project, run:

```bash
python manage.py migrate
```

The migration files included in the repository create the required database structure.

## Environment Variables

The project uses a `.env` file for environment-specific settings.

The following variables are used:

| Variable        | Description                                           |
| --------------- | ----------------------------------------------------- |
| `SECRET_KEY`    | Django secret key used for application security       |
| `DEBUG`         | Enables or disables Django debug mode                 |
| `ALLOWED_HOSTS` | Specifies the hosts allowed to access the application |

A `.env.example` file is included in the repository as a template.

The actual `.env` file is excluded from version control and must not contain values that are committed to GitHub.

## Git and Repository

The project repository is available at:

https://github.com/gkurtthomas/portfolio-site

The repository uses Git for version control and GitHub for remote repository management.

Development work is completed on separate branches and merged into the main branch through pull requests.

## Fresh Project Setup

When cloning this project on a new computer:

1. Clone the repository.
2. Create a new `.venv` virtual environment.
3. Activate the virtual environment.
4. Install the packages using `pip install -r requirements.txt`.
5. Create a `.env` file using `.env.example`.
6. Run `python manage.py migrate`.
7. Run `python manage.py createsuperuser`.
8. Run `python manage.py runserver`.

No existing `db.sqlite3` or virtual environment is required because these files are excluded from the repository.

## Author

**Kurt Thomas Gonzales**

Computer Engineering Student

## License

This project was created for educational purposes as part of a school requirement.
