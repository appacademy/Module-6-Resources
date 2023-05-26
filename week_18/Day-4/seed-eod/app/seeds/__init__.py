from flask.cli import AppGroup
from .user import seed_users, undo_users
from .posts import seed_posts, undo_posts

seed_commands = AppGroup("seed")


@seed_commands.command("all")
def seed():
    users = seed_users()
    seed_posts(users)
    print("We seeded!")
    

@seed_commands.command("undo")
def undo():
    undo_posts()
    undo_users()
    print("We are now destroying some seed data")






