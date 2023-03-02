# Seed Commands

We can use some of `Flask's` built in functionality to create terminal seed
commands in our apps!

Our goal is to be able to run the terminal command of 
```terminal
pipenv run flask seed all 
```
to apply our seed data, and then also run 
```terminal
pipenv run flask seed undo 
```
to be able to remove all of our seed data.

## Seed Folder

We will want to make a seed folder, as a subfolder of our `app` folder.  We will
also want a `__init__.py` to not only create a module, but to define our seed
commands as well.

We will want to add the following to that `__init__.py` we just created.

```python
from flask.cli import AppGroup

seed_commands = AppGroup("seed")
```

The `AppGroup` function lets us group together similar commands under one group.
This will allow us to write in the terminal
```terminal
pipenv run flask seed
```
This is great progress, but now we need to add the "all" and "undo"
functionality!



## Command Decorators


To create our "all" and "undo" functionality, we will use the built in
`command()` decorator, which takes as an arguement the string value of the
terminal command you want to call the function with.  


```python
@seed_commands.command("all")
def seed():
    seed_users()
```

So the above code will run the decorated `seed` function any time `pipenv run
flask seed all` is run in the terminal.  While we could define our seeds
directly in the `seed` command, its better to abstract them to seperate files,
as different resources may require different imports, but also to help with
debugging.  

The complete `__init__.py` file in your seed folder, should look like the
following...

```python
from flask.cli import AppGroup
from .users import seed_users, undo_users

seed_commands = AppGroup("seed")

@seed_commands.command("all")
def seed():
    seed_users()
    print("All seeds created!")

@seed_commands.command("undo")
def undo():
    undo_posts()
    print("All seeds undone!")
```


## Resource Seed Files


You will want to make a seperate seed file for most of your resources (models)
but we will just walk through a users files here.  

Make a new file in the seed folder named `users.py` and write the following
code...

```python
from app.models import db, User
from sqlalchemy.sql import text

def seed_users():
    # run your seeds here
    pass

def undo_users():
    db.session.execute(text("DELETE FROM users"))
    db.session.commit()
```

We need to execute a raw `SQL` command to delete the rows from our database and
reset the autoincrementing `ID` column back to 1.  You will want to use a
similar set up for your other resource seed files, remembering to change the
function names, and the table name in the `undo` functions `SQL`.  A complete
user seed file might look like the following...


```python
from app.models import db, User
from sqlalchemy.sql import text


def seed_users():
    user1 = User(
            username="demouser",
            email="demo@aa.io",
            bio= "I love to demo things!",
    )

    db.session.add(user1)
    db.session.commit()

def undo_users():
    db.session.execute(text("DELETE FROM users"))
    db.session.commit()
```


## Making the final connection...


So far all of our code is looking great, but we have not told our `app` about
our wonderful seed commands, so they do not at all work.  Head over to the main
`__init__.py` file so we can take care of this issue!

We will need to import our `seed_commands` from the seed folder into our
`__init__.py`, and then we will need to add those commands to our `app` with the
following methods

```python
app.cli.add_command(seed_commands)
```

You main `__init__.py` file should look something like the following after you
add the above import and method invokation.  

```python
from flask import Flask, render_template, redirect
from flask_migrate import Migrate

# need to import seed commands from seeds folders
from .seeds import seed_commands

from .models import db
from .config import Config
from .routes.user_routes import users


app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)

# Need to add the seed commands to our app
app.cli.add_command(seed_commands)

app.register_blueprint(users, url_prefix="/users")
```

With all of the above code in place, you should be able to run these commands in
your terminal now!  Happy Seeding!


```terminal
pipenv run flask seed all 

pipenv run flask seed undo 
```