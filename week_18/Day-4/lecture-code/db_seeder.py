from datetime import datetime, timedelta
from random import randint
from app import app
from app.models import db, User, Post

def random_date_2023():
    """Generate a random datetime between `start` and `end` which
    should be datetime objects"""
    start = datetime(2023, 1, 1)
    end = datetime.now()
    random_date = start + timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=randint(0, int((end - start).total_seconds())),
    )

    return random_date


with app.app_context():
#   db.drop_all()
#   print("All tables dropped")
#   db.create_all()
#   print("Created all tables")
  
  pip = User(username="Pip", email="pip@pip.pip", profile_pic="https://pipstagram.s3.amazonaws.com/137336008_406744080656046_3364448327964401597_n.jpg")
  loki = User(username="Loki", email="loki@loki.loki", profile_pic="https://pipstagram.s3.amazonaws.com/96422911_295207864815265_1703976767659593889_n.jpg")
  luna = User(username="Luna", email="luna@luna.luna", profile_pic="https://pipstagram.s3.amazonaws.com/14736358_1218308304908741_9131677530216988672_n.jpg")

  # print(dir(db.session))
  posts = [
    {
        "author": pip,
        "caption": "hello!",
        "image": "https://pipstagram.s3.amazonaws.com/137336008_406744080656046_3364448327964401597_n.jpg",
        "date": random_date_2023(),
        # "likes": randint(0, 100),
    },
    {
        "author": pip,
        "caption": "you would've gotten that stick... if you knew how to swim",
        "image": "https://pipstagram.s3.amazonaws.com/14736358_1218308304908741_9131677530216988672_n.jpg",
        "date": random_date_2023(),
        # "likes": randint(0, 100),
    },
    {
        "author": pip,
        "caption": "please, just give me another hour",
        "image": "https://pipstagram.s3.amazonaws.com/147984230_349580496062106_6664809776347526236_n.jpg",
        "date": random_date_2023(),
        # "likes": randint(0, 100),
    },
    {
        "author": luna,
        "caption": "my best buddy!",
        "image": "https://pipstagram.s3.amazonaws.com/15035574_1079682388796264_6184137089534132224_n.jpg",
        "date": random_date_2023(),
        # "likes": randint(0, 100),
    },
    {
        "author": pip,
        "caption": "Ready for the job interview",
        "image": "https://pipstagram.s3.amazonaws.com/17332517_1437522652946724_7128079981032243200_n.jpg",
        "date": random_date_2023(),
        # "likes": randint(0, 100),
    },
    {
        "author": pip,
        "caption": "let's just be friends",
        "image": "https://pipstagram.s3.amazonaws.com/18012097_255074681625671_5096963914957062144_n.jpg",
        "date": random_date_2023(),
        # "likes": randint(0, 100),
    },
    {
        "author": loki,
        "caption": "allow me to introduce myself",
        "image": "https://pipstagram.s3.amazonaws.com/2023-07-17+14.53.08.jpg",
        "date": random_date_2023(),
        # "likes": randint(0, 100),
    },
    {
        "author": loki,
        "caption": "mmmm... dirt!",
        "image": "https://pipstagram.s3.amazonaws.com/2023-07-17+14.53.30.jpg",
        "date": random_date_2023(),
        # "likes": randint(0, 100),
    },
    {
        "author": loki,
        "caption": "please sir, i beg of you",
        "image": "https://pipstagram.s3.amazonaws.com/2023-07-17+14.57.09.jpg",
        "date": random_date_2023(),
        # "likes": randint(0, 100),
    }
  ]
  [db.session.add(Post(**post)) for post in posts]
  
  db.session.add(pip)
  db.session.commit()