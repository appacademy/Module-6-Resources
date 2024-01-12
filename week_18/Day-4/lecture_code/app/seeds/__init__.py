from flask.cli import AppGroup

from .posts import seed_posts, undo_posts
from .users import seed_users, undo_users

seed_commands = AppGroup("seed")


@seed_commands.command("all")
def seed():
    users = seed_users()
    seed_posts(users)


@seed_commands.command("undo")
def undo():
    undo_posts()
    undo_users()

