# Render Debugging

Have you tried to deploy to render, and it just is not working?  Been there, it can be frustrating!  Hopefully you will find some help here!

Most of the time, the deployment issue are going to be related to your database.  Also, about half the time it could be an issue with deploying using postgres, and not really an issue with render.  (Postgres in production will enforce constraints that Sqlite did not in development, meaning while it worked for you in development, not so much in production)

## Migrations?

There is a good chance you needed more models than just the user model provided in the starter.  There is also the possibility you wanted to start from scratch on the migrations too.  Either of these are totally fine, as long as we add back the code from the starter we overwrote.

### Env.py in Migrations

The env.py that is part of the starter has been modified from the default, to include code to handle the SCHEMA in production.  If you deleted your migrations and did a `flask db init` you now have the default env.py, not the custom one from the project starter.  Make sure you env.py is the same as the code below, and if not replace the entire file with this code

```python

from __future__ import with_statement

import logging
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from flask import current_app
config.set_main_option(
    'sqlalchemy.url',
    str(current_app.extensions['migrate'].db.engine.url).replace('%', '%%'))
target_metadata = current_app.extensions['migrate'].db.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """

    # this callback is used to prevent an auto-migration from being generated
    # when there are no changes to the schema
    # reference: http://alembic.zzzcomputing.com/en/latest/cookbook.html
    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, 'autogenerate', False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info('No changes in schema detected.')

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=process_revision_directives,
            **current_app.extensions['migrate'].configure_args
        )
        # Create a schema (only in production)
        if environment == "production":
            connection.execute(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA}")

        # Set search path to your schema (only in production)
        with context.begin_transaction():
            if environment == "production":
                context.execute(f"SET search_path TO {SCHEMA}")
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

```

### Migration files

If you added any migration files, or started from scratch and made a new one, we will need some additional code in those as well for deployment to render.  For reference, here is the entire migration file from the starter to migrate the Users table.

```python

"""create_users_table
Revision ID: ffdc0a98111c
Revises:
Create Date: 2020-11-20 15:06:02.230689
"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = 'ffdc0a98111c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###qqqqqqqqq


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###

```

If you created a new migration file, the first thing you will need to do is import the environment and SCHEMA near the other import statements.

```python

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

```

Next, for each table you are creating in your migration there will be an `op.create_table()` method call.  After each `op.create_table()` call (and remember the closing `)` will be after all the column and constraint details), you will want to add the following conditional statement to handle prefixing the SCHEMA

```python

 if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")

```
*REMINDER* You will need to change the table name in the above code to match which table you are adding the conditional too.


## Let's check out those Models!

### Models defined with classes

So now hopefully your migration files are in good order, let's look toward the models!  For each one of our models we defined with a class, we need to add a conditional to add `__table_args__` for the SCHEMA.  Below is part of the User model from the starter, we will need to add the same conditional to all other models with class based definitions (if you created a join table with a `db.Table` instread of a class definition, there will be different instructions further below)  

```python

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

```

Make sure to add this conditional to all of your class defined models after the `__tablename__`! (and you will need to import `environment` and `SCHEMA` from the db.py file)

```python
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
```

### Foreign Keys

Every time we use a foreign key on any of our models (join tables included) in production, we will need to tell SqlAlchemy which SCHEMA it needs to look for the foreign key on.  If you look in the db.py file (in the models folder), there is a helper function to assist us with this.

```python

def add_prefix_for_prod(attr):
    if environment == "production":
        return f"{SCHEMA}.{attr}"
    else:
        return attr

```

We will need to import this function `add_prefix_for_prod`, as well as our `environment` and `SCHEMA` from db.py if we have not already.  Then for every foreign key, we want to pass the `add_prefix_for_prod` in to each `db.ForeignKey()` like the following...

```python

   user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

```

### Join Tables

As mentioned above, our join tables will also need a conditional for adding a SCHEMA when in production.  Add the below conditional after your `db.Table` to prefix it with the SCHEMA (you will need to change the varaible name to match whatever you saved your `db.Table` to).

```python
likes = db.Table(
    'likes',
    db.Model.metadata,
    db.Column('users', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), primary_key=True ),
    db.Column('jokes', db.Integer, db.ForeignKey(add_prefix_for_prod('jokes.id')), primary_key=True )
)

if environment == "production":
    likes.schema = SCHEMA


```

## How About Those Seeders?

So if you migrations and models are all set, how about those seed files?  A few things you will want to check out with them

### Order Matters!

In production we use postgres, which cares a whole lot more about enforcing rules and constraints than sqlite does.  So the order of how we apply and remove our seed files matters too.  The below code is taken from the `__init__.py` file in the `seeds` folder of the starter, and I have added 2 more seed files (from Dad Jokes)


```python

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo 
        # command, which will  truncate all tables prefixed with 
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_likes()
        undo_jokes()
        undo_users()
    seed_users()
    seed_jokes()
    seed_likes()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_likes()
    undo_jokes()
    undo_users()
    # Add other undo functions here
```

Note that when we seed, we first seed our tables that do no depend on other tables.  Above we seed `users` first, because it does not depend on any other tables, then we seed `jokes`because it has a foregin key to the users table, so it depends on `users` being created already.  Lastly we seed `likes` as it depends on both the `users` and `jokes` tables to already exist.

When we *undo* our seeds, we need to do it in the reverse order than when we seeded.  If we try to remove the `users` table first, we will get an error and both `posts` and `likes` depend on their being a `users` table.  If you are getting an error when something is `violating a foreign key constraint` you are probably undoing your seeds in the wrong order.



### Truncate vs Reset

We also want to remember that for each new seed file we make, we need to also add conditional logic to each seed undo function to `TRUNCATE` in production but `RESET` in development.  (This is due to sqlite vs poatgres requiring different commands to clear data from a table while also resetting the `id` attrubute)

```python

def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")
        
    db.session.commit()

```
