from flask.cli import AppGroup
from .users import seed_users, undo_users
from .posts import seed_posts, undo_posts

# Creates a seed group to group similar commands 
seed_commands = AppGroup("seed")


@seed_commands.command("all")
def seed():
    users = seed_users()
    seed_posts(users)
    print("All seeds created!")



@seed_commands.command("undo")
def undo():
    undo_posts()
    undo_users()
    print("All seeds undone!")
