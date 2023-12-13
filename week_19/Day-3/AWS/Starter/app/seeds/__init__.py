from flask.cli import AppGroup  
from .users import seed_users, undo_users
from .posts import seed_posts, undo_posts

seed_commands = AppGroup("seed")


@seed_commands.command("all")
def seed():
    users = seed_users()
    seed_posts(users)
    print('If we see this text, we would be seeding')



@seed_commands.command("undo")
def undo():
    undo_posts()
    undo_users()
    print("If we see this text, we would be destroying all our data... 💥")
