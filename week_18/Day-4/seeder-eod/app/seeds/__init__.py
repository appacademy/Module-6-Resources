from flask.cli import AppGroup
from .users import seed_users, undo_users
from .posts import seed_posts, undo_posts

seed_commands = AppGroup("seed")


@seed_commands.command("all")
def seed():
    users = seed_users()
    seed_posts(users)
    print("IF WE SEE THIS WE WOULD BE SEEDING")


@seed_commands.command("undo")
def undo():
    undo_posts()
    undo_users()
    print("WE WOULD BE VICIOUSLY DESTROYING ALL OUR DATA NOW...")