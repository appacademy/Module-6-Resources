from random import choice, randint
import datetime


def random_date(start, end):
    """Generate a random datetime between `start` and `end` which
    should be datetime objects"""
    random_date = start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=randint(0, int((end - start).total_seconds())),
    )
    return random_date


posts = [
        {   
            "id": 1,
            "author": "Patch",
            "caption": "Napping Outside is always fun...",
            "image": "https://res.cloudinary.com/app-academy4/image/upload/v1647912033/Patchstagram/IMG_3394_fktg48.jpg",
            "date": random_date(datetime.datetime(2023, 1, 1), datetime.datetime.now()),
            "likes": randint(1, 10),
        },
        {
            "id": 2,
            "author": "Patch",
            "caption": "Napping inside is pretty awesome too...",
            "image": "https://res.cloudinary.com/app-academy4/image/upload/v1647912403/Patchstagram/64865942444__2B7B1A74-ECAF-4798-BEAB-D4890B7164C4_hnmowy.jpg",
            "date": random_date(datetime.datetime(2023, 1, 1), datetime.datetime.now()),
            "likes": randint(1, 10),
        },
        {
            "id": 3,
            "author": "Blue",
            "caption": "I like my fish",
            "image": "https://res.cloudinary.com/app-academy4/image/upload/v1647912006/Patchstagram/IMG_3437_u2frrk.jpg",
            "date": random_date(datetime.datetime(2023, 1, 1), datetime.datetime.now()),
            "likes": randint(1, 10),
       
        },
        {
            "id": 4,
            "author": "Patch",
            "caption": "Now THIS is a party!",
            "image": "https://res.cloudinary.com/app-academy4/image/upload/v1647912056/Patchstagram/IMG_3389_i6czzx.jpg",
            "date": random_date(datetime.datetime(2023, 1, 1), datetime.datetime.now()),
            "likes": randint(1, 10),
     
        },
        {
            "id": 5,
            "author": "Blue",
            "caption": "This punk stole my tent! ⛺️",
            "image": "https://res.cloudinary.com/app-academy4/image/upload/v1647912094/Patchstagram/IMG_3211_sy5wcy.jpg",
            "date": random_date(datetime.datetime(2023, 1, 1), datetime.datetime.now()),
            "likes": randint(1, 10),
        }
]
