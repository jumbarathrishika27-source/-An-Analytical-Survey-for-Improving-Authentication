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
