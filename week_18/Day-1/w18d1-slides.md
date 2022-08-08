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
- Today: Intro to Flask and SQLite3
- Tuesday: Flask routing, templating, and forms
- Wednesday: Interacting with a database via the SQLAlchemy ORM
- Thursday: Data migrations with Alembic
- Friday: review, practice assessment walkthrough, and Kahoot!


---

### Intro to Flask & SQLite3 (Today)
- [Flask](https://flask.palletsprojects.com/)
    - Web server (like Express, but for Python)
- [SQLite3](https://docs.python.org/3/library/sqlite3.html)
    - Built in SQLite3 module for Python, allows Flask to communicate with a SQLite3 database

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

# Getting started with Flask & SQLite3
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

### SQLite3


Python has a built in module named `sqlite3` which allows us to connect directly to a SQLite3 database file from Python.

It is NOT the equivalent of Sequelize. We can use it directly, but typically we will want to use an actual ORM (SQLAlchemy). 


---


### Setting up `sqlite3` [1/2]

1. Import the `sqlite3` package at the top of your file.
```python=
import sqlite3
```
2. Create a new database to connect to in the terminal.
```python=
sqlite3 dev.db
```
3. Set up your connection parameters (file name for the SQLite3 database). 
```python=
DB_FILE = "dev.db"
```

---

### Quick note: the `with` keyword

 - `with` works like a `try/except/finally` block wrapped up into one keyword! It runs some setup logic, then "tries" the code in the `with` block, and whether or not it runs into an error, it runs some clean up code.

 - It is used to more easily manage common resources (e.g. closing a database connection, a file, etc.) We do not need to define anything, how to use the `with` keyword is defined in the modules.

 - We will use the `with` keyword to manage our database connections with `sqlite3`. 


---

### Setting up `sqlite3` [2/2]

4. Open a connection to the database. Use the `with` keyword, and the `connect` method on `sqlite3`:
```python=
with sqlite3.connect(DB_FILE) as conn:
```

5. Open a "cursor" to perform data operations.
```python=
with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor() 
```
6. With our cursor, we can use the `execute` method to run a SQL command:
```python=
with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor()
    curs.execute(
            """
            CREATE TABLE jokes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            joke_body VARCHAR(250),
            punchline VARCHAR(250),
            rating VARCHAR(15)
            );
            """    
    )
```


---

### Executing SQL with `sqlite3`

After executing a command, we can fetch the results using the `fetchone` or `fetchall` methods on the cursor.
- `fetchone()` will return a tuple of the first matched record
- `fetchall()` will return a list of tuples of all matching records
```python=
# Fetching one record
with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor()
    curs.execute(
        """
        SELECT *
        FROM jokes;
        """
    )
    results = curs.fetchall()
    print(results)
```


---


### Creating data with `sqlite3`
We can use parameterized SQL statements to insert data into our database.
```python=
# Inserting a new record
def create_joke(joke_body, punchline, rating):
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor() 
        curs.execute(
            """
            INSERT INTO jokes (joke_body, punchline, rating)
            VALUES(:joke_body, :punchline, :rating)
            """,
            {
                "joke_body": joke_body,
                "punchline": punchline,
                "rating": rating
            }
        )
```

---


### For the rest of today...

- No project/practice today

- Behavioral Interview Exercise (optional)

- Get started on homework

- EOD from Cesar on DS&A
