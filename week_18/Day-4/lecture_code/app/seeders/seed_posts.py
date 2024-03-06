from datetime import datetime, timedelta
from random import randint
from sqlalchemy.sql import text
from ..models import db, Post, User

def random_date_2023():
    """Generate a random datetime between start and end which
    should be datetime objects"""
    start = datetime(2023, 1, 1)
    end = datetime.now()
    random_date = start + timedelta(
        # Get a random amount of seconds between start and end
        seconds=randint(0, int((end - start).total_seconds())),
    )
    return random_date

def seed_posts():
    pip_posts = [
            {
                "caption": "hello!",
                "image": "https://pipstagram.s3.amazonaws.com/137336008_406744080656046_3364448327964401597_n.jpg",
                "created_at": random_date_2023(),
            },
            {
                "caption": "you would've gotten that stick... if you knew how to swim",
                "image": "https://pipstagram.s3.amazonaws.com/14736358_1218308304908741_9131677530216988672_n.jpg",
                "created_at": random_date_2023(),
            },
            {
                "caption": "please, just give me another hour",
                "image": "https://pipstagram.s3.amazonaws.com/147984230_349580496062106_6664809776347526236_n.jpg",
                "created_at": random_date_2023(),
            },
            {
                "caption": "Ready for the job interview",
                "image": "https://pipstagram.s3.amazonaws.com/17332517_1437522652946724_7128079981032243200_n.jpg",
                "created_at": random_date_2023(),
            },
            {
                "caption": "let's just be friends",
                "image": "https://pipstagram.s3.amazonaws.com/18012097_255074681625671_5096963914957062144_n.jpg",
                "created_at": random_date_2023(),
            }
        ]

    lunas_posts = [
            {
                "caption": "my best buddy!",
                "image": "https://pipstagram.s3.amazonaws.com/15035574_1079682388796264_6184137089534132224_n.jpg",
                "created_at": random_date_2023(),
            }
        ]

    lokis_posts = [
            {
                "caption": "allow me to introduce myself",
                "image": "https://pipstagram.s3.amazonaws.com/2023-07-17+14.53.08.jpg",
                "created_at": random_date_2023(),
            },
            {
                "caption": "mmmm... dirt!",
                "image": "https://pipstagram.s3.amazonaws.com/2023-07-17+14.53.30.jpg",
                "created_at": random_date_2023(),
            },
            {
                "caption": "please sir, i beg of you",
                "image": "https://pipstagram.s3.amazonaws.com/2023-07-17+14.57.09.jpg",
                "created_at": random_date_2023(),
            }
        ]
    for post in pip_posts:
        current_post = Post(**post)
        current_post.author_id = 1
        db.session.add(current_post)

    for post in lunas_posts:
        current_post = Post(**post)
        current_post.author_id = 2
        db.session.add(current_post)

    for post in lokis_posts:
        current_post = Post(**post)
        current_post.author_id = 3
        db.session.add(current_post)

    db.session.commit()


def undo_posts():
    db.session.execute(text("DELETE FROM posts;"))
    db.session.commit()
