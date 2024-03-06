from  ..models import db, User
from sqlalchemy.sql import text

def seed_users():
    users = [
            {
                "name": "Pip"
            },
            {
                "name": "Luna"
            },
            {
                "name": "Loki"
            }
            ]

    for user in users:
        current_user = User(**user)
        db.session.add(current_user)

    db.session.commit()


def undo_users():
    db.session.execute(text("DELETE from users;"))
    db.session.commit()

