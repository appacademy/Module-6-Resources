# More about Flask
## Week 18 Day 2

---

## Templating with Jinja

---

### Jinja
- Jinja is an HTML templating language (similar to Pug)
- Add the Jinja package to your application (Optional, flask comes with Jinja as a dependency)
  - `pipenv install Jinja2`
- Flask looks for HTML templates in the `templates` folder inside the `app` package
    - Create a `templates` folder within your application
    - In `templates`, create HTML files that you would like your routes to render

---

### Rendering Templates
- In your app, import `render_template` from `flask`.
    - `render_template` renders an HTML page using the Jinja template engine
- Instead of returning HTML strings directly, call `render_template`, passing the name of the HTML file you would like to render
```python=
@app.route('/')
def index():
	return render_template('index.html')
```

---

### Rendering Templates with Arguments
- We can pass objects from our routes to `render_template` for use in our HTML files.
- Objects are passed as kwargs, where the key is the name of the item referenced in the HTML file, and the value is the object itself from the route.

```python=
@app.route('/')
def index():
    return render_template('index.html', display_item=value)
```

---


### Redirecting to Another Route
- We can redirect to another route with `redirect()`
- `redirect()` takes a string for the route location to redirect to and an optional default status code if the redirection is unsuccessful

```python=
@app.route('/')
def index():
    return redirect('/all', 404)
```

---

### Accessing Objects and Evaluating Code

- In our HTML files, we use `{{ display_item }}` to access objects that were passed in as kwargs to `render_template`
- We use the `{% %}` syntax to evaluate code within an HTML file
```python=
{% for x in items %}
{% endfor %}
```
```python=
{% if condition_a %}
{% elif condition_b %}
{% else condition_c %}
{% endif %}
```

---

### Extending and Including Content
We can use `extends` to reuse a base template in other HTML files:
```python=
{% extends "base.html" %}
```

The base template can include a placeholder for content from other HTML files:
```python=
{% block content %} {% endblock %}
```
Our other HTML files use the same tags to fill in that content.

We can reuse small templates with `include`:

```python=
{% include "other_template.html" %}
```

---

## Routing with Flask Blueprints

---

### Blueprints
Blueprints allow us to organize our code by breaking our routes into individual components, much like Routers did for us in Express.

---

### Creating a Blueprint
- Import the Blueprint package from Flask: 
  `from flask import Blueprint`
- Construct a Blueprint with the following arguments:
    - A name for the Blueprint
    - The name of the file where it is defined (use `__name__` to use the current file name)
    - A `url_prefix`, which will be prepended to all routes associated with this Blueprint

```python=
from flask import Blueprint

books_router = Blueprint('books', __name__, url_prefix='/books')
```


---


### Use the Flask Blueprint to make routes

- The `@blueprint_name.route` decorator allows us to define routes to associate with our Blueprint
    - Exactly like we would use it for the base `app` routes in our main file

```python=
# In the routes/books.py
from flask import Blueprint

books_router = Blueprint('books', __name__, url_prefix='/books')

@books_router.route('/')
def book_index():
    # Show all the books
```

---

### Register the Flask Blueprint with the Flask application

- To connect our Blueprint to our app, we import the module that it is defined in.
- Invoke the app's `register_blueprint` method with a reference to the Blueprint instance as an argument.

```python=
from flask import Flask
from book_app.routes import books_router # assuming we have a __init__.py in routes

app = Flask(__name__)
app.register_blueprint(books_router)
```

---

## Lecture Videos (26 min)
Watch:
- Handling Form Data With Flask I (12:39)
- Handling Form Data With Flask II (9:39)

---

### Creating Forms with WTForms
You must have a SECRET_KEY in your app configuration for CSRF token validation to be successful

- Create a forms directory and initialize it as a module with a `__init__.py`
- `pipenv install wtforms flask-wtf`
- `from flask_wtf import FlaskForm`
- Define form classes in the forms module
    - Form classes will inherit from `FlaskForm`
- From `wtforms` import field types for your form and any built-in validators

---

### Creating Forms with WTForms
```python=
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class NewBookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    rating = SelectField(
        "Rating",
        choices=["New favorite", "Great", "Good", "Underwhelming", "Bad", "Horrible"]
    )
    submit = SubmitField("Add Book")
```

---

### Field Types

- Check out the `wtforms` [docs](https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields) to understand different field types for your forms
- We can import validators into our form from `wtforms.validators` ([documentation](https://wtforms.readthedocs.io/en/2.3.x/validators/))

---


### Handling Get and Post Routes

In our app, we can handle:
- `GET` request for the form
- `POST` request with valid data
- `POST` request with invalid data

---

### GET Route

```python=
@books_router.route('/new_book', methods=["GET"])
def add_book():
    form = NewBookForm()

    return render_template("new_book.html", form=form)
```

---

### Form Error handling

- Invoking `validate_on_submit` on our form instance will return `True` if the `POST` had no validation error.
    - Once validated we can use `form.data` to access the data dictionary
- If the form was `POST`ed with errors, `validate_on_submit` will return `False`
    - If not validated we can key into `form.errors` to access the errors dictionary

---

### POST Route

```python=
@books_router.route('/new_book', methods=["GET", "POST"])
def add_book():
    form = NewBookForm()

    if form.validate_on_submit():
        title = form.data['title']
        
        with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
            with conn.cursor() as curs:
                curs.execute(
                    """
                    INSERT INTO books (name)
                    VALUES (%(title)s)
                    """,
                    {
                        "title": title
                    }
                )
                
        return redirect('/books/all')
    
    if form.errors:
        return form.errors

    return render_template("new_book.html", form=form)
```

---

### Project Time!

Today's project is Calendar This!

You will build a data-driven calendar application with Flask.