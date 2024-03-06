from flask.cli import AppGroup
from .seed_posts import seed_posts, undo_posts
from .seed_users import seed_users, undo_users



seed_commands = AppGroup("seed")


@seed_commands.command("all")
def seed():
    seed_users()
    seed_posts()


@seed_commands.command("undo")
def undo():
    undo_users()
    undo_posts()



