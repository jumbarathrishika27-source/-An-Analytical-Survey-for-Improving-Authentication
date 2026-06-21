# An Analytical Survey for Improving Authentication

A Django-based full-stack web application for improving authentication using user registration, admin approval, QR-code verification, and encrypted file upload/decryption.

## Features

- User registration
- Admin login
- Admin user activation/deactivation
- End-user login
- QR-code based authentication step
- CSV file upload
- File encryption using Fernet encryption
- File decryption and download
- Separate user and admin dashboards

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript
- Bootstrap
- qrcode
- cryptography

## Project Structure

```txt
AnalyticalCloud/
├── AnalyticalCloud/      # Main Django project settings and URLs
├── users/                # User app: registration, login, upload, decrypt
├── admins/               # Admin app: user management and uploaded files
├── assets/               # Static files and templates
├── media/                # Uploaded files, ignored in Git
├── manage.py
├── requirements.txt
└── .gitignore

git clone https://github.com/jumbarathrishika27-source/-An-Analytical-Survey-for-Improving-Authentication.git
cd -An-Analytical-Survey-for-Improving-Authentication

python -m venv venv

venv\Scripts\activate

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

http://127.0.0.1:8000/

Home Page:      /
User Login:     /UserLogin/
User Register:  /UserRegister/
Admin Login:    /AdminLogin/

1. Clone the GitHub repository on PythonAnywhere.
2. Create a virtual environment.
3. Install requirements.
4. Run migrations.
5. Configure the Django web app.
6. Set static and media paths.
7. Reload the web app.
