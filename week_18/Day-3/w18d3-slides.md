<style>
    .present {
        text-align: left;
    }
</style>

---

###### tags: `Week 18` `W18D3`

---

# Using SQLAlchemy with Flask
## Week 18 Day 3

---

## Setting Up SQLAlchemy with Flask

---

### Steps for setting up Flask-SQLAlchemy

1. Install sqlalchemy and flask-sqlalchemy
```bash
pipenv install sqlalchemy flask-sqlalchemy
```

2. Create your database
```bash 
sqlite3 dev.db
```

3. Add a DATABASE_URL to your `.env`
```bash=
DATABASE_URL=sqlite:///dev.db
```

---

### Steps for setting up Flask-SQLAlchemy

4. Modify your config class.
    a. Add a class variable called `SQLALCHEMY_DATABASE_URI`, and set the value to the `DATABASE_URL` from your environment

    b. Add a class variable called `SQLALCHEMY_TRACK_MODIFICATIONS` and set the value. This will turn off a Flask-SQLAlchemy feature that signals our app everytime a change is made to db objects.

```python=
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

---

### Steps for setting up Flask-SQLAlchemy


5. Create a models folder with a __init__.py and db.py files inside it, and then in the db.py file instantiate a `SQLAlchemy` object from `flask_sqlalchemy`.

```python=
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```

---

### Steps for setting up Flask-SQLAlchemy

6. Import the `db` instance into the file where you are defining your app.
```python=
from app.models import db
# much additional code...
db.init_app(app)
```


---

## Lecture Videos (20 min)
Watch:
- FlaskSQLAlchemy: Creating Mapping Files (15:00)


---


### Creating Models

Models inherit from the `db.Model` class, which comes from our `SQLAlchemy` instance.

If you want to specify a tablename, use the `__tablename__` property.

```python=
db = SQLALchemy()
class Book(db.Model):
    __tablename__ = "books"
```

---

### Columns on models

Columns are added to the model as class variables—instances of `db.Column` from our `SQLAlchemy` instance.

Column types (`db.String`, `db.Integer`, etc.) also come from our SQLAlchemy instance.

```python=
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    pages = db.Column(db.Integer, nullable=True)
```


---

### One-To-Many Relationships

Let's make a relationship between books and authors. Each book belongs to one author, authors can have many books.

First, let's create the Author model.

```python=
class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
```

---

### One-To-Many Relationships
Next we need to add a foreign key to the Book model that points to the Author model. To make a column into a foreign key we use `db.ForeignKey(tablename.columnname)`.

In a one-to-many relationship, the foreign key column will go on the child model referencing the parent. The child is the "many" side of the relationship.

```python=
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
```

---

### Adding the relationship property
Add a `db.relationship` to both of the models. 

Use the `back_populates` property to connect the two relationship attributes.

Use `cascade="all, delete"` on the parent model to cascade deletion of all related child objects ([documentation](https://docs.sqlalchemy.org/en/14/orm/cascades.html#delete)).

```python=
attribute_name = db.relationship("OtherModelName", back_populates="name_of_attribute_from_opposite_model")
```

```python=
# on the Book model
author = db.relationship("Author", back_populates="books")
```

```python=
# on the Author model
books = db.relationship("Book", back_populates="author", cascade="all, delete")
```



---

### One-To-One Relationships
These are very uncommon, so chances are you may never have to make one, but if you do, it's very similar to a One-To-Many relationship, you just need to add the `uselist=False` arguement to the many side of the relationship

```python=
# on the Book model
author = db.relationship("Author", back_populates="books")
```

```python=
# on the Author model
books = db.relationship("Book", back_populates="author", uselist=False)
```

---


### Many-to-Many Relationships

Many-to-many relationships are a lot like one-to-many relationships in terms of how they use the `db.relationship` property.

However, since neither of the two associated tables contains the foreign keys, we would need to build a separate association table to connect the models.

We use a `db.Table` to make an association table.

---

### Many-to-Many Relationships

The first argument to `db.Table` will be the table name, and then the second argument will be `db.Model.metadata` because we sill want to inherit from the model parent class. Ather that each additional argument is a column. A typical association table only needs two columns—one for each of the two foreign keys.

It does not need its own id column (this is different from Sequelize).

```python=
publishers_books = db.Table(
    "publishers_books",
    db.Model.metadata,
    db.Column(
        "book_id", db.Integer, db.ForeignKey("books.id"), primary_key=True
    ),
    db.Column(
        "publisher_id", db.Integer, db.ForeignKey("publishers.id"), primary_key=True
    )
)
```

---

### Many-to-Many Relationships

The only change we have to make the `db.relationship` attributes is to add a `secondary` argument. The value here is the association table.

We must add this `secondary` argument to both relationship attributes.

```python=
attribute_name = db.relationship(
    "OtherModelName",
    secondary=association_table_name,
    back_populates="name_of_attribute_from_opposite_model"
)
```

---

### Many-to-Many Relationships

On Book model:
```python=
publishers = db.relationship(
    "Book",
    secondary=publishers_books,
    back_populates="books"
)
```

On Publisher model:
```python=
books = db.relationship(
    "Publisher",
    secondary=publishers_books,
    back_populates="publishers"
)
```

---

### Creating records

To make a new row in your database, first create a new instance of one of your model classes.

After you create your instance, add it to your session and commit it to the database.

```python=
new_book = Book(title="Alice in Wonderland")
db.session.add(new_book)
db.session.commit()
```


---

### Lecture Videos (20 min)

Watch:
- FlaskSQLAlchemy: Interacting with Data (13:10)


---


### Querying with SQLAlchemy

To query the database, we use the `query` attribute on our `db.Model` classes.

Get all records:
```python=
all_books = Book.query.all()
```

Get one record by primary key:
```python=
one_book = Book.query.get(id)
```

---

### Filtering on queries

To apply a filter, you can use the `.filter` method, passing in an operator on a column. Use `.all()` to get a list of all records that match the filter, or use `.first()` to get the first matching record.

```python=
# all books where the title starts with "a"
Book.query.filter(Book.title.like("A%"))
```

```python=
# first book where the title starts with "a"
Book.query.filter(Book.title.like("A%")).first()
```

We can use `.join(OtherModel)` on a query to perform a join query.

```python=
# all authors with books >= 100 pages
Author.query.join(Book).filter(Book.pages >= 100)
```

[more available operators](https://docs.sqlalchemy.org/en/14/core/operators.html)

---

### Updating records
Once you have queried or created an instance of your model, you can update it by changing a value on that instance, and adding/commiting to the db.
```python=
book = Book.query.get(1)
book.author_id = 1
db.session.commit()
```

---


### Deleting records

Deleting records uses the `delete` method on the `db.session` object.
```python=
book = Book.query.get(1)
db.session.delete(book)
db.session.commit()
```

---

### Project Time!

Today's project is **Order Up!**. You will create a data-driven Flask + SQLAlchemy application to track orders for a restaurant.