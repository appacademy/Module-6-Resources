<style>
    .present {
        text-align: left;
    }
</style>

---

###### tags: `Week 18` `W18D4`

---

# Alembic Migrations & JSON with Flask
## Week 18 Day 4

---

### Lecture Videos (15 minutes)
Watch:
- Database Updates with Alembic (3:00)
- Changing a Table Name with Alembic Code Demo (8:00)

---

### Setting Up Flask-Migrate

1. Install packages (`alembic` and `flask-migrate`).

```bash
pipenv install alembic flask-migrate
```

2. Import `Migrate` from `flask_migrate` and use it to configure your migrations (in the file where you are defining your Flask application).

```python=
# add this to the top of the file with the imports
from flask_migrate import Migrate

# this goes after your app is instantiated
Migrate(app, db)
```

---

### Setting Up Flask-Migrate

3. Initialize your migrations repo.
```bash
flask db init
```
4. Set up the correct revision file name in the alembic.ini
```bash=
file_template = %%(year)d%%(month).2d%%(day).2d_%%(hour).2d%%(minute).2d%%(second).2d_%%(slug)s
```

5. Create a migration file.
```bash
flask db migrate
```

6. Apply your migrations to your database.
```bash
flask db upgrade
```


---

### Workflow
When you make changes to your models:

7. Run migrate to get a new migration script.
```bash
flask db migrate
```

8. Run upgrade to apply the changes.
```bash
flask db upgrade
```

---

### Alembic won't detect every change...
By default, Alembic only detects simple changes like new or dropped columns/models. It does not detect smaller changes to existing columns or models.

There are a few ways you can configure Alembic to detect these sorts of changes.

---

### Changing a Table Name

If you want to change the name of an existing table, use the `op.rename_table()` method in the migration script:
```python=
op.rename_table('old_name', 'new_name')
```

To do so, first generate the migration file and then add the above function call to the `upgrade()` function.

---

### Changing a Column Name

If you want to change the name of an existing column, use the `op.alter_column()` method with the kwarg `new_column_name` in the migration script:
```python=
op.alter_column('table_name', 'old_name', new_column_name='new_name')
```

To do so, first generate the migration file and then alter the `upgrade()` function with the above function call.

---

### Changing a Column Constraint
To configure Alembic to detect changes to an existing column's constraints, use the `compare_type=True` keyword argument.

In the `migrations/env.py` file, locate the final `context.configure()` call and add `compare_type=True` to the keyword arguments. 

---

### Downgrading

Downgrading shouldn't be a very common part of your workflow. If you want to downgrade a migration, you can use the `downgrade` command.

To undo a single migration:
```bash
flask db downgrade
```


---

## Lecture Videos 2 (15 min)
Watch:
- JSON With Flask (12:00)

---

### Model Instances vs. Dictionaries

Recall that, in JavaScript, we typically use objects for two purposes: as a collection of key/value pairs, and also as a collection of methods and properties.

In Python, key/value pairs in dictionaries are not the same as attributes on objects (a.k.a, classes).

```python=
book = Book.query.get(1)
print(book)
print(book.title)
```

If you try to send a model instance object from your server to your frontend, the frontend client won't know what to do with it. 

If we send a dictionary instead, Flask will automatically convert it to JSON so it can be understood by the client.

---

### Returning JSON from Python

We need to convert our database objects into dictionaries so that we can use our Flask back-end as an API.

```python=
book = Book.query.get(1)
book_dict = {
    "id": book.id,
    "title": book.title,
}
print(book_dict)  # Flask can automatically convert this to JSON
```


---

### Writing a `to_dict()` method

We can make our code `DRY`er by adding a method to our model classes to convert model instances to dictionaries.

That way we don't have to rewrite the same code on different routes when we send data to our front-end.


```python=
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    
    # other columns, methods, etc...

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
        }
```

---

### Project time!

Today's project is Package Tracker. You and your pair will build another data-driven Flask/SQLAlchemy application to track shipped packages. The project will ask you to use Flask-Migrate to migrate your data.