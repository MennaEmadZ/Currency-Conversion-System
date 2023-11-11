# Currency Conversion System README

## Overview
This document outlines the setup and usage of a currency conversion system. The system provides APIs for user authentication, currency conversion, and viewing currency conversion history. It's built on Django and utilizes Celery for scheduled tasks.

## Setup Instructions

### 1. System Update and Upgrade
Update and upgrade your system packages using:
```bash
sudo apt update
sudo apt upgrade
```

### 2. Python Environment Setup
Set up a Python virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Dependency Installation
Install necessary dependencies using Poetry:
```bash
poetry install
```

### 4. Django Setup
Navigate to the Django project directory and set up the database:
```bash
cd curreny_sub_system
python manage.py makemigrations
python manage.py migrate
```

### 5. Running the Server
Start the Django development server:
```bash
python manage.py runserver
```

### 6. Celery Setup
In a separate shell, activate Celery for scheduled tasks and background actions:

- **Scheduler (runs every 48 hours):**
```bash
celery -A curreny_sub_system beat --loglevel=info
```

- **Worker (updates conversion status):**
```bash
celery -A curreny_sub_system worker --loglevel=info
```

### 7. Running Unit Tests
To run unit tests:
```bash
python manage.py test
```

## API Usage

### Authentication API
To authenticate users:
```bash
curl --location 'http://localhost:8000/auth/token/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "mennae",
    "password": "mennaemad1234"
}'
```

### Currency Conversion API
To perform currency conversion (replace `{access_token}` with the actual token):
```bash
curl --location 'http://localhost:8000/currency/conversion/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {access_token}' \
--data '{
"from_currency": "USD",
"to_currency": "EGP",
"amount": 150
}'
```

### History Get API
To retrieve the conversion history:
```bash
curl --location 'http://localhost:8000/currency/history/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {access_token}' \
--data ''
```

## Notes
- Ensure all commands are executed in the correct environment and directory.
- Replace credentials and tokens with appropriate values for your setup.
- Check Django and Celery documentation for more details and troubleshooting.
