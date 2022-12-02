from dad_jokes.models import db, User, Joke
from dad_jokes import app

with app.app_context():
    
    # db.drop_all()
    # print("All table dropped!")
    # db.create_all()
    # print("Create all tables!")

    user1 = User(
        username="Brad",
        email="brad@gmaile.com",
        password="password"
    )
    user2 = User(username="Andy", email="andy@gmail.com", password="cubingiscool")
    user3 = User(username="Blue", email="blue@gmail.com", password="iamaninja")
    user4 = User(username="Patch", email="patch@gmail.com", password="ilovefud")

    all_users = [user1, user2, user3, user4]
    add_users = [db.session.add(user) for user in all_users]
    db.session.commit()
    print("Users seeded!")

    joke1 = Joke(
        joke_body="What did the plumber say to the singer?",
        punchline="Nice pipes...",
        rating="G",
        user=user1,
        joke_likes=[user2, user3]
    )
 
    joke2 = Joke(
        joke_body='What do you call a lazy doctor?',
        punchline='Dr Doo-little...',
        rating='PG',
        user=user1,
        joke_likes=[user1, user2, user4]
    )

    joke3 = Joke(
        joke_body='What do you call a camel in a drought?',
        punchline='A dry humper...',
        rating='PG',
        user=user1
    )

    joke4 = Joke(
        joke_body='Did you hear Steve Harvey and his wife got into a fight?',
        punchline='It was a real family feud...',
        rating='R',
        user=user2,
        joke_likes=[user3, user4]
    )

    joke5 = Joke(
        joke_body='What do mermaids wash their fins with?',
        punchline='Tide...',
        rating='G',
        user=user2,
        joke_likes=[user1, user3, user4]
    )

    all_jokes = [joke1, joke2, joke3, joke4, joke5]
    add_jokes = [db.session.add(joke) for joke in all_jokes]
    db.session.commit()
    print("Jokes seeded")