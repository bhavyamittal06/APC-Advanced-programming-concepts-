# Experiment 12: Django Login with Regular Expressions

## Aim
Create a Django web application to demonstrate user registration, login/logout, and input validation using regular expressions.

## Requirements
- Python 3.10+
- Django

## Run the project
Open a terminal in this folder and run:

```bash
python3 -m pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

Then open http://127.0.0.1:8000/

## Regular expressions used
- Username: `^[A-Za-z][A-Za-z0-9_]{2,19}$`
- Email: `^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$`
- Password: `^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w\s]).{8,}$`

## Result
The application registers users only after regex validation, authenticates registered users, provides a protected dashboard, and supports logout.
