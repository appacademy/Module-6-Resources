from app.models import db, User, Post
from app import app
from random import choice
from faker import Faker

fake = Faker()


with app.app_context():

    db.drop_all()
    print("All table droppped!")
    db.create_all()
    print("Created all tables!")

    user_1 = User(
        username="Patchenator",
        email="patcj_the_cat@gmail.com",
        profile_pic="https://res.cloudinary.com/app-academy4/image/upload/v1647912257/Patchstagram/IMG_3074_ubqe1e.jpg",
        bio="I love naps and food"
    )

    user_2 = User(
            username="Blueberry44",
            email="blue@aol.com",
            profile_pic="https://res.cloudinary.com/app-academy4/image/upload/v1647912128/Patchstagram/66346842095__0566A55A-DF10-4E86-A59A-F5694436FA4E_wmoi1w.jpg",
            bio="I am a ninja! 🥷🏻",
    )

    user_3 = User(
            username="brads213",
            email="brad@gmail.com",
            profile_pic="https://ca.slack-edge.com/T03GU501J-USQFVK3GT-941e867a316f-512",
            bio="I am the father of 2 crazy cats",
    )

    
    all_users = [user_1, user_2, user_3]
    add_users = [db.session.add(user) for user in all_users] 
    db.session.commit()
    print("All users seeded")


    post_1 = Post(
        caption="Napping outside is always fun...",
        image="https://res.cloudinary.com/app-academy4/image/upload/v1647912033/Patchstagram/IMG_3394_fktg48.jpg",
        post_date=fake.date_between(start_date="-1y", end_date="today"),
        user=choice(all_users),
        post_likes=[user_2, user_3],
    )

    post_2 = Post(
        caption="Napping inside is pretty awesome too...",
        image="https://res.cloudinary.com/app-academy4/image/upload/v1647912403/Patchstagram/64865942444__2B7B1A74-ECAF-4798-BEAB-D4890B7164C4_hnmowy.jpg",
        post_date=fake.date_between(start_date='-1y', end_date='today'),
        user=choice(all_users),
        post_likes=[user_2, user_1],
    )

    post_3 = Post(
        caption= "I like my fish",
        image= "https://res.cloudinary.com/app-academy4/image/upload/v1647912006/Patchstagram/IMG_3437_u2frrk.jpg",
        post_date=fake.date_between(start_date='-1y', end_date='today'),
        user=choice(all_users),
        post_likes=[user_1, user_2, user_3],
    )       
    
    post_4 = Post(
        caption= "Now THIS is a party!",
        image= "https://res.cloudinary.com/app-academy4/image/upload/v1647912056/Patchstagram/IMG_3389_i6czzx.jpg",
        post_date=fake.date_between(start_date='-1y', end_date='today'),
        user=choice(all_users),
    )

    post_5 = Post(
        caption= "This punk stole my tent! ⛺️",
        image= "https://res.cloudinary.com/app-academy4/image/upload/v1647912094/Patchstagram/IMG_3211_sy5wcy.jpg",
        post_date=fake.date_between(start_date='-1y', end_date='today'),
        user=user_2,
        post_likes=[user_2, user_3]
    )

    all_posts = [post_1, post_2, post_3, post_4, post_5]
    add_posts = [db.session.add(post) for post in all_posts]
    db.session.commit()
    print("All posts seeded!")