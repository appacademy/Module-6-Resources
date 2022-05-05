# Getting started with Flask
## Week 18 Day 1

---

## Lecture Videos (15 min)
Watch:
- Setting Up A Flask App (13:39)

---

### Flask app setup

1. install flask
```bash
pipenv install flask
```
2. import `Flask` to the file where we are building our application
```python=
from flask import Flask
```
3. instantiate a `Flask` instance
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
5. install python-dotenv
```bash
pipenv install python-dotenv
```
6. run your application...
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
3. Set up your connection parameters in a dictionary, including `dbname`, `user`, and `password`:
```python=
CONNECTION_PARAMETERS = {
    "dbname": "widget_database",
    "user": "widget_user",
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

4. Open a connection to the database. Use the `with` keyword, and the `connect` method on `psycopg2`:
```python=
with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    # code to follow
```

5. Open a "cursor" to perform data operations.
```python=
with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
      # code to follow
```
6. With our cursor, we can use the `execute` method to run a SQL command:
```python=
with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
        curs.execute(
            """CREATE TABLE widgets (
            id SERIAL PRIMARY KEY,
            color VARCHAR(50),
            shape VARCHAR(50)
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
            FROM widgets
            """)
        results = curs.fetchone()
        print(results)
```


---


### Creating data with `psycopg2`
We can use parameterized SQL statements to insert data into our database.
```python=
# Inserting a new record
def add_new_widget(color, shape):
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute(
                """
                INSERT INTO widgets (color, shape)
                VALUES (%(color)s, %(shape)s)
                """,
                {
                    "color": color,
                    "shape": shape
                })

```

---


### Why can't I use f-string syntax?


[documentation](https://www.psycopg.org/docs/usage.html#the-problem-with-the-query-parameters)

---
