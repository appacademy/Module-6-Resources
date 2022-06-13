<style>
    .present {
        text-align: left;
    }
</style>


---

###### tags: `Week 18` `W18D1`

---

# Week 18 Roadmap

---

### Technologies
- Today: Intro to Flask and Psycopg
- Tuesday: Flask routing, templating, and forms
- Wednesday: Interacting with a database via the SQLAlchemy ORM
- Thursday: Data migrations with Alembic
- Friday: review, practice assessment walkthrough, and Kahoot!


---

### Intro to Flask & Psycopg (Today)
- [Flask](https://flask.palletsprojects.com/)
    - Web server (like Express, but for Python)
- [Psycopg2](https://www.psycopg.org/docs/index.html#)
    - Database adapter for Python, allows Flask to communicate with Postgres database

---

### More about Flask (Tuesday)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    - Templating language (like Pug)
- [WTForms](https://wtforms.readthedocs.io) & [Flask-WTF](https://flask-wtf.readthedocs.io)
    - WTForms is a form validation library
    - Flask-WTF integrates WTForms with Flask

---

### SQLAlchemy & Flask-SQLAlchemy (Wednesday)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/index.html)
    - Object-relational mapping tool (ORM) that makes it easier to interact with our database (like Sequelize)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com) 
    - Integrates SQLAlchemy with Flask


---

### Alembic & Flask-Migrate (Thursday)
- [Alembic](https://alembic.sqlalchemy.org)
    - Database migration tool that works with SQLAlchemy
- [Flask-Migrate](https://flask-migrate.readthedocs.io)
    - Integrates Alembic with Flask

---

### Review day (Friday)
- Independent study time
- Practice assessment walkthrough
- Kahoot

---

# Getting started with Flask & Psycopg
## Week 18 Day 1

---

## Lecture Videos (15 min)
Watch:
- Setting Up A Flask App (13:39)

---

### Flask app setup

1. Install flask
```bash
pipenv install flask
```
2. Create a folder for your application with a `__init__.py`.
3. Import `Flask` in the `__init__.py`
```python=
from flask import Flask
```
4. Instantiate a `Flask` instance
```python=
app = Flask(__name__)
```


---

### Flask app setup

4. Add a `.flaskenv` file. This file sets publicly visible environment variables for your Flask app
```bash=
FLASK_APP=app
FLASK_ENV=development
```
5. Install python-dotenv to load environment variables into the app configuration
```bash
pipenv install python-dotenv
```
6. Run your application!
```bash
pipenv run flask run
```

---

### Adding routes

We use the `@route` decorator to turn a function into a route that exists on our application. Whatever we `return` from the function will get sent to the browser.
```python=
@app.route("/")
def index():
    return "Welcome to our app"
```

---

### Adding a secret key (or other configuration variables)

In addition to the `.flaskenv` file which contains environment specific (not secret) information, we can use a `.env`.

This file contains environment variables we want to keep secret. Unlike `.flaskenv`, it will *not* be committed to GitHub.

```bash=
SECRET_KEY=EXTREMELYsecretstufffshhhhhhhh
```

---

### Making a Config class

Get the secret values from your `.env` and define a `Config` class which has all of the values you want to incorporate into your app.

```python=
import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
```

Then incorporate these values into your application using the the `config.from_object method`.


```python=
# in the __init__.py in the app folder
from flask import Flask
from book_app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
```

---

## Lecture Videos (10 min)
Watch:
- Psycopg Demo (7:32)

---

### Psycopg

`psycopg2` is a utility that lets us connect directly to a postgresql database from Python.

It is NOT the equivalent of Sequelize. We can use it directly, but typically we will want to use an actual ORM. Our ORM will rely on `psycopg2`, but it will have a much more convenient interface.

---

### Attention M1 users!

The M1 arm64 CPU architecture has historically been incompatible with `psycopg`. While you will be able to install the package without issue, you might run into problems trying to access a database with `psycopg` or `SQLAlchemy`.

If you do, please let us know and we will help you out!

---

### Setting up `psycopg2` [1/2]

1. Install `psycopg2`
```bash
pipenv install psycopg2-binary
```
2. Import the `psycopg2` package at the top of your file.
3. 2.5 Set up a database to connect to in psql
```python=
CREATE USER psycopg_test_user WITH 
        CREATEDB PASSWORD 'password';

CREATE DATABASE psycopg_test_db WITH 
        OWNER psycopg_test_user;
```
4. Set up your connection parameters in a dictionary, including `dbname`, `user`, and `password`:
```python=
CONNECTION_PARAMETERS = {
    "dbname": "book_database",
    "user": "book_user",
    "password": "password",
}
```

---

### Quick note: the `with` keyword

`with` works like a `try`/`except`/`finally` block wrapped up into one keyword! It runs some setup logic, then "tries" the code in the `with` block, and whether or not it runs into an error, it runs some clean up code.

It is used to more easily manage common resources (e.g. closing a database connection, a file, etc.)

We will use the `with` keyword to manage our database connections with `psycopg`.


---

### Setting up `psycopg2` [2/2]

5. Open a connection to the database. Use the `with` keyword, and the `connect` method on `psycopg2`:
```python=
with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    # code to follow
```

6. Open a "cursor" to perform data operations.
```python=
with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
      # code to follow
```
7. With our cursor, we can use the `execute` method to run a SQL command:
```python=
with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
        curs.execute(
            """CREATE TABLE books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(50),
            author VARCHAR(50)
            );""")
```


---

### Executing SQL with `psycopg2`

After executing a command, we can fetch the results using the `fetchone` or `fetchall` methods on the cursor.
- `fetchone()` will return a tuple of the first matched record
- `fetchall()` will return a list of tuples of all matching records
```python=
# Fetching one record
with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
        curs.execute(
            """
            SELECT *
            FROM books
            """)
        results = curs.fetchone()
        print(results)
```


---


### Creating data with `psycopg2`
We can use parameterized SQL statements to insert data into our database.
```python=
# Inserting a new record
def create_book(title, author):
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute(
                """
                INSERT INTO books (title, author)
                VALUES (%(title)s, %(author)s)
                """,
                {
                    "title": title,
                    "author": author
                })

```

---


### Why can't I use f-string syntax?


[documentation](https://www.psycopg.org/docs/usage.html#the-problem-with-the-query-parameters)


---


### For the rest of today...

- No project/practice today

- Behavioral Interview Exercise (optional)

- Get started on homework

- EOD from Cesar on DS&A
