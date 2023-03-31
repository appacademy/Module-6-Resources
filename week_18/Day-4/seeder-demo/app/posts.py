from random import randint
from faker import Faker
fake = Faker()


users = [
    {   
        'username': "Patchenator",
        'fullName': "Patch",
        'email': "patch_the_cat@gmail.com",
        'password': "ILuvFud",
        'profile_pic': "https://res.cloudinary.com/app-academy4/image/upload/v1647912257/Patchstagram/IMG_3074_ubqe1e.jpg",
        'bio': "I love naps and food",
        'age': 6,
    },
    {
        'username': "Blueberry44",
        'fullName': "Blue",
        'email': "blue@aol.com",
        'password': "meowmeow",
        'profile_pic': "https://res.cloudinary.com/app-academy4/image/upload/v1647912128/Patchstagram/66346842095__0566A55A-DF10-4E86-A59A-F5694436FA4E_wmoi1w.jpg",
        'bio': "I am a ninja! 🥷🏻",
        'age': 6,
    },
    {
        'username': "brads213",
        'fullName': "Brad Simpson",
        'email': "brad@gmail.com",
        'password': "password",
        'profile_pic': "https://ca.slack-edge.com/T03GU501J-USQFVK3GT-947b84c598b8-512",
        'bio': "I am the father of 2 crazy cats",
        'age': 44,
    }
]

posts = [
        {   
            "id": 1,
            "author": users[0],
            "caption": "Napping Outside is always fun...",
            "image": "https://res.cloudinary.com/app-academy4/image/upload/v1647912033/Patchstagram/IMG_3394_fktg48.jpg",
            "date": fake.date_between(start_date='-1y', end_date='today'),
            "likes": randint(1, 10),
        },
        {
            "id": 2,
            "author": users[0],
            "caption": "Napping inside is pretty awesome too...",
            "image": "https://res.cloudinary.com/app-academy4/image/upload/v1647912403/Patchstagram/64865942444__2B7B1A74-ECAF-4798-BEAB-D4890B7164C4_hnmowy.jpg",
            "date": fake.date_between(start_date='-1y', end_date='today'),
            "likes": randint(1, 10),
        },
        {
            "id": 3,
            "author": users[1],
            "caption": "I like my fish",
            "image": "https://res.cloudinary.com/app-academy4/image/upload/v1647912006/Patchstagram/IMG_3437_u2frrk.jpg",
            "date": fake.date_between(start_date='-1y', end_date='today'),
            "likes": randint(1, 10),
       
        },
        {
            "id": 4,
            "author": users[2],
            "caption": "Now THIS is a party!",
            "image": "https://res.cloudinary.com/app-academy4/image/upload/v1647912056/Patchstagram/IMG_3389_i6czzx.jpg",
            "date": fake.date_between(start_date='-1y', end_date='today'),
            "likes": randint(1, 10),
     
        },
        {
            "id": 5,
            "author": users[1],
            "caption": "This punk stole my tent! ⛺️",
            "image": "https://res.cloudinary.com/app-academy4/image/upload/v1647912094/Patchstagram/IMG_3211_sy5wcy.jpg",
            "date": fake.date_between(start_date='-1y', end_date='today'),
            "likes": randint(1, 10),
        }
]
