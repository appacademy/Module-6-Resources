from flask.cli import AppGroup
from .users_seed import seed_users, undo_users
from .posts_seed import seed_posts, undo_posts

seed_commands = AppGroup("seed")


@seed_commands.command("all")
def seed():
    users = seed_users()
    seed_posts(users)
    print("Seeding complete")


@seed_commands.command("undo")
def undo():
    undo_posts()
    undo_users()
    print("Seeds undone!")

