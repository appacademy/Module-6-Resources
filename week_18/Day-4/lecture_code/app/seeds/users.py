from sqlalchemy.sql import text
from app.models import User, db

def seed_users():
    users = [
        {
            "name": "Pip"
        },
        {
            "name": "Loki"
        },
        {
            "name": "Luna"
        },
        ]

    user_rows = []
    for user in users:
        curr_user = User(**user)
        user_rows.append(curr_user)
        db.session.add(curr_user)

    print("SEEDING USERS TABLE!!!!!!")
    db.session.commit()

    return user_rows


def undo_users():
    db.session.execute(text("DELETE FROM users;"))
    db.session.commit()
    print("DELETE ALL USERS!!!!!!")
