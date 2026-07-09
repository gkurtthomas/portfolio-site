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
* Django Admin for managing content

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

## Project Structure

```text
Portfolio/
│
├── main/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── portfolio/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository.

```bash
git clone https://github.com/gkurtthomas/portfolio-site.git
```

2. Navigate to the project directory.

```bash
cd Portfolio
```

3. Create and activate a virtual environment.

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the required packages.

```bash
pip install -r requirements.txt
```

5. Apply the database migrations.

```bash
python manage.py migrate
```

6. Run the Django development server.

```bash
python manage.py runserver
```

7. Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Author

**Kurt Thomas Gonzales**

Computer Engineering Student

## License

This project was created for educational purposes as part of a school requirement.
