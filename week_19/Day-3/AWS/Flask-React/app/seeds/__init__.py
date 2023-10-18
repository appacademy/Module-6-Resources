from flask.cli import AppGroup
from .users import seed_users, undo_users
from .posts import seed_posts, undo_posts

seed_commands = AppGroup("seed")


@seed_commands.command("all")
def seed():
    users = seed_users()
    seed_posts(users)
    print("WE WOULD WE WOULD SEED YOU SEED YOU")



@seed_commands.command("undo")
def undo_seeds():
    undo_posts()
    undo_users()
    print("WE WOULD WE WOULD UNSEED YOU UNSEED YOU")

