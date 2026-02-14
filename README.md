# Flask Form App (SQLite + Email Confirmation)

A simple Flask web app that collects form submissions, saves them to a SQLite database, and sends a confirmation email to the user.

---

## Features

- Flask form submission (GET/POST)
- Saves submissions to SQLite using SQLAlchemy
- Sends confirmation email using Flask-Mail (Gmail SMTP)
- Flash message success feedback
- Bootstrap styling via CDN

---

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy (SQLite)
- Flask-Mail
- Bootstrap (CDN)

---

## Project Files

- app.py          # Flask app (routes, database model, email sending)
- templates/
  - index.html    # Form page (you create this)
- data.db         # SQLite database (auto-created on first run)

---

## Setup

1) Create and activate a virtual environment

python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

2) Install dependencies

pip install flask flask_sqlalchemy flask_mail

---

## IMPORTANT: Email Credentials (Security)

Do NOT hardcode your Gmail username/password in code.

Instead, set environment variables and read them in your app.

Example (Windows PowerShell):

$env:MAIL_USERNAME="your_email@gmail.com"
$env:MAIL_PASSWORD="your_gmail_app_password"

Example (macOS/Linux):

export MAIL_USERNAME="your_email@gmail.com"
export MAIL_PASSWORD="your_gmail_app_password"

Use a Gmail "App Password" (recommended) instead of your normal password.

---

## Run the App

python app.py

Then open:

http://127.0.0.1:5001

---

## Bootstrap CDN (Optional)

CSS:
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">

JS:
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js"></script>

---

## Notes

- The database (data.db) is created automatically the first time you run the app.
- If you see "database is locked" while developing, stop all running Flask terminals and restart the app.
- For best results with SQLite in debug mode, you can run with:
  app.run(debug=True, use_reloader=False, port=5001)
