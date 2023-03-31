from flask.cli import AppGroup
from .users import seed_users, undo_users
from .posts import seed_posts, undo_posts

seed_commands = AppGroup("seed")


@seed_commands.command("all")
def seed():
    all_users = seed_users()
    seed_posts(all_users)
    print("SEEDS COMPLETED!")



@seed_commands.command("undo")
def undo():
    undo_posts()
    undo_users()
    print("UNDO SEEDS DONE!!")
