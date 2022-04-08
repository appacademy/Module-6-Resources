# Flask-SQLAlchemy Quick Reference
Here are some examples of useful patterns for models and queries with Flask-SQLAlchemy.
## Model Associations
### One-to-One relationship between Student and Scholarship
One-to-one relationships are not especially common, and they are implemented very similarly to one-to-many relationships. The key difference is just that on the parent data table, you would set use the `uselist=False` argument to indicate that a single corresponding entry on the child table is expected (so a list is not necessary).
#### On the student model
```python=
class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    # other columns
    scholarship = db.relationship(
        "Scholarship", uselist=False,
        back_populates="student"
    )
```

#### On the scholarship model
```python=
class Scholarship(db.Model):
    __tablename__ = "scholarships"
    id = db.Column(db.Integer, primary_key=True)
    # other columns
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    
    student = db.relationship("Student", back_populates="scholarship")
```

### One-to-Many relationship between Student and Class
#### On the student model
```python=
class Student(db.Model):
  __tablename__ = "students"
  id = db.Column(db.Integer, primary_key=True)
  # other columns
  classes = db.relationship("Class", back_populates="student")
```

#### On the class model
```python=
class Class(db.Model):
  __tablename__ = "classes"
  id = db.Column(db.Integer, primary_key=True)
  # other columns
  student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
  
  student = db.relationship("Student", back_populates="classes")
```

### Many to Many between Student and Lesson through student_lessons helper table

#### Helper table for joining
The helper table doesn't need to be defined as a class since we will never need to access the entries on it directly. Its only purpose is to connect our other two models.
```python=
student_lessons = db.Table(
    "student_lessons",
    db.Column(
        "student_id", 
        db.Integer, 
        db.ForeignKey("students.id"), 
        primary_key=True
    ),
    db.Column(
        "lesson_id", 
        db.Integer, 
        db.ForeignKey("lessons.id"), 
        primary_key=True
    )
)
```

#### On the lesson model
```python=
class Lesson(db.Model):
    __tablename__ = "lessons"
    id = db.Column(db.Integer, primary_key=True)
    # other columns
    
    students = db.relationship(
        "Student", 
        secondary=student_lessons, 
        back_populates="lessons"
    )
```

#### On the student model
```python=
class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    # other columns
    
    lessons = db.relationship(
        "Lesson", 
        secondary=student_lessons, 
        back_populates="students"
    )
```

- note: for all of these relationships, you can use `backref` instead of `back_populates`. `backref` only has to exist on one of the two models, and it will create the relationship on its counterpart. [more info on backref vs back_populates](https://stackoverflow.com/a/59920780)

### Many-to-Many relationship between Users and Users through follows helper table
Sometimes you may have a table that is joined to itself—you can still use a `db.relationship` to make it easier to access the related entries in both directions. For instance, you might have a User model, and you want to be able to access the collection of users that a given user follows as well as the user's followers.
#### On helper table
```python=
follows = db.Table(
    "follows", 
    db.Column("follower_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("followed_id", db.Integer, db.ForeignKey("users.id"))
)
```

#### On the User model
```python=
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    # columns
    followers = db.relationship(
        "User", 
        secondary=follows,
        primaryjoin=(follows.c.follower_id == id),
        secondaryjoin=(follows.c.followed_id == id),
        backref=db.backref("following", lazy="dynamic"),
        lazy="dynamic"
    )
    # this relationship allows you to access both the collection of users 
    # that follow a given user (with user.followers), and the collection
    # of users that a user follows (with user.following)
```
## Query Format
### For a collection of entities
```python=
# get all entities — this will return a list of Student objects
# the .all() method turns the result of the query from a generator
# into a list
students = Student.query.all()
```

### For one entity
#### by ID
```python=
# get the student with the ID 2
student = Student.query.get(2)
```
#### based on another value
```python=
# using filter_by
jeff = Student.query.filter_by(name="Jeff").first()
# using filter (these two will yield the same result)
jeff = Student.query.filter(Student.name == "Jeff").first()

# note: using the method `first` will get the first
# entity that meets the query, or if there are none
# it will return `None`. if you replaced `first` with `one`
# it will raise an exception if there is more than
# one result (or if there are none at all)
```

### Simple query examples (with `filter`, `order_by`, `limit`)
#### get the students whose usernames contain "sh"
```python=
Student.query.filter(Student.username.ilike("%sh%"))
```
##### get the three students whose names come last in the alphabet
```python=
last_students = Student.query.order_by(
    Student.name.desc()
).limit(3)

# case insensitive version - include import statement at top of file
from sqlalchemy import func
last_students = Student.query.order_by(
    func.lower(Student.name).desc()
).limit(3)
```
##### get students whose enrollment status is `True`
```python=
Student.query.filter(Student.enrolled.is_(True))
```
##### student whose enrollment status is `True` and whose usernames contain sh
```python=
# by chaining filters
filtered_students = Student.query.filter(
    Student.username.ilike("%ju%")
).filter(
    Student.enrolled.is_(True)
).all()
#
Student.query.filter(
    Student.username.ilike("%ju%"),
    Student.enrolled.is_(True)
).all()
```

### More complicated query examples (`group_by`, `join`, `subquery`)
#### Simple joining
If you have included the appropriate `db.relationship` on the models, explicitly joining two models in your query may not be necessary. When you define a `db.relationship` between two models, it means that the associated entry/entries from the other table are included as a property on any instance of that model. For example, one could get a list of all the students from a specific cohort with `cohort.students`—no need to query the students table and filter by the cohort ID. 
```python=
# get all the students from a specific cohort
cohort_a = Cohort.query.get(1)
students_from_a = cohort.students # a list of Student objects

# or the reverse—get the cohort object associated with a 
# specific student
student_four = Student.query.get(4)
cohort_of_student_four = student_four.cohort # a single Cohort object
```
#### Complicated queries
##### get students from all cohorts that started in August
```python=
august_students = Student.query.join(Cohort).filter(
    Cohort.start_month == ("August")
)
```

##### get cohorts who have more than 50 students
```python=
from sqlalchemy import func

# this subquery gets the number of students in each cohort
student_counts = db.session.query(
    func.count(Student.id).label("num_students"), 
    Student.cohort_id
).group_by(Student.cohort_id).subquery()

# by joining the previous subquery, we can selectively filter
# our cohorts based on size
large_cohorts = Cohort.query.join(
    student_counts, Cohort.id == student_counts.c.cohort_id
).filter(student_counts.c.num_students > 50).all()
```

##### get the average scores of the currently enrolled students
```python=
from sqlalchemy.sql import func

student_avgs = db.session.query(
    Student,
    func.avg(Score.percent_correct).label("average_score")
).join(Score).group_by(Student.id)
# be aware that this returns a collection of tuples, not Student objects
```


## Creating and updating data

Note on seeding: Unlike the workflow for seeding that we used with Sequelize, seeding the database in our SQLAlchemy projects looks just like adding entries to our database using the ORM. In the python group project skeleton, we're using a custom command line function for seeding (those `flask seed all`/`flask seed undo` commands are not built into Flask anywhere—Flask just allows you to define your own functions that run on the command line).  Your seed files can add data to the database just like on your routes. So the examples below could be used in seeders or in routes—it looks the same.

#### adding new data to database
```python=
# create a new entry
august = Cohort(start_month="August")


# setting up one-to-many associations
# 
# now lets create some students who belong to specific cohorts
# option 1: if you already have the id
student1 = Student(name="Laramie", cohort_id=3, enrolled=True)
# option 2: use the Cohort object to establish the relationship
student2 = Student(name="Marni", cohort=august, enrolled=True)



# setting up many-to-many relationships
#
# students can belong to many teams, teams can have many students
team1 = Team(color="blue", name="cool kids")
# you can add a student to a team by appending to the Student object
student1.teams.append(team1)
# or by appending to the Team object
team1.students.append(student2)

# finally, add all your new entries and commit
db.session.add(august)
db.session.add(student1)
db.session.add(student2)
db.session.add(team1)
db.session.commit()
```

#### updating existing data
```python=
# select your entry from the database - for example, by ID
score = Score.query.get(12)
# change the relevant information on that item
score.percent_correct = 75
#
# add and commit
db.session.add(score)
db.session.commit()
```

## Sending data as JSON
### Dictionaries
Recall that, in JavaScript, we typically use objects for two purposes: as a collection of key/value pairs, and also as a collection of methods and properties.

In Python, key/value pairs in dictionaries are _not_ the same as attributes on objects.

Dictionaries consist of key/value pairs. Accessing the value associated with a particular key uses bracket notation (`dictionary["my_key"] = some_value`). Keys can be any _hashable_ type (i.e. immutable types: strings, booleans integers, and tuples).

Accessing the methods and properties on objects is different. You can access these properties and methods using dot notation (`my_object.some_property = data`). When you get entries from your database using SQLAlchemy, these objects are instances of your Model classes, not dictionaries.

Python dictionaries can easily be serialized into JSON format (as can strings, numbers, booleans, `None`, lists, and tuples). Objects from your Model classes cannot. If you want to send an entity from your database to the frontend of your application, you will have to convert it to a dictionary.

### `to_dict()` methods
You may find it helpful to define methods on your database model classes for converting objects from that class into dictionaries. Each class would need a unique `to_dict` method which captures the relevent properties. You could even create multiple dictionary conversion methods for the same class that return different information (for example, separate methods for a summary versus a detail view).

That said, you are not required to write these methods—you could instead access the values of interest and create a dictionary directly on the route where you are returning the data.

However, since you will often need to send the same data from these classes in multiple routes. In that case, you can make your code more _DRY_ (Don't Repeat Yourself) by making reusable `to_dict` methods. 
```python=
class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    caffeinated = db.Column(db.Boolean, default=True)
    cohort_id = db.Column(db.Integer, db.ForeignKey("cohorts.id"))
    
    cohort = db.relationship("Cohort", back_populates="students")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "caffeinated": self.caffeinated,
            "cohort_id": self.cohort_id
        }
        
    
class Cohort(db.Model):
    __tablename__ = "cohorts"
    id = db.Column(db.Integer, primary_key=True)
    start_month = db.Column(db.String(15)) nullable=False)
    ptm = db.Column(db.String(50), nullable=False)
    ptm_tagline = db.Column(db.String(1000), nullable=False)
    
    students = db.relationship("Student", back_populates="cohort")
    
    def to_dict(self):
        return {
            "id": self.id,
            "start_month": self.start_month,
            "ptm": self.ptm,
            "ptm_tagline": self.ptm_tagline,
        }
```

Here are some example routes using the above methods.
```python= 
@app.route("/students")
def get_students():
    students = Student.query.all()
    return {"students": [student.to_dict() for user in users]}


@app.route("/students/<int:id>")
def get_user_by_id(id):
    student = Student.query.get(1)
    return student.to_dict()

@app.route("/cohorts/<int:id>")
def get_cohort(id):
    cohort = Cohort.query.get(id)
    return cohort.to_dict()

```
