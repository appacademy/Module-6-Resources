from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


likes = db.Table(
    'likes',
    db.Model.metadata,
    db.Column('users', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('jokes', db.Integer, db.ForeignKey('jokes.id'), primary_key=True)
)



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.String(200))

    # Relationships will go here
    jokes = db.relationship("Joke", back_populates='user', cascade='all, delete') 
    author_likes = db.relationship(
        "Joke", 
        secondary=likes,
        back_populates="joke_likes",
        cascade="all, delete"
    )


    def __repr__(self):
        return f"< User: {self.username} >"


    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "jokes": [j.to_dict_no_user() for j in self.jokes]
        }

    
    def to_dict_no_jokes(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

# user1 = User.query.get(1)
# user1 = {
#     "id": 1,
#     "username": "Brad",
#     "email": "brad@gmail.com",
#     "password": "wings_wednesday",
#     "jokes": [<joke1>, <joke2>, <joke3>]
#     "author_likes" [<joke1>, <joke2>]
# }


class Joke(db.Model):
    __tablename__ = 'jokes'
    id = db.Column(db.Integer, primary_key=True)
    joke_body = db.Column(db.String(255), nullable=False)
    punchline = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    # Relationships will go here
    user = db.relationship("User", back_populates='jokes')
    joke_likes = db.relationship(
        "User",
        secondary=likes,
        back_populates="author_likes"
    )

    def __repr__(self):
        return f"< JokeId: {self.id} Rating: {self.rating} >"


    def to_dict(self):
        return {
            "id": self.id,
            "jokeBody": self.joke_body,
            "punchline": self.punchline,
            "rating": self.rating,
            "user": self.user.username,
            "likes": len(self.joke_likes)
        }


    def to_dict_no_user(self):
        return {
            "id": self.id,
            "joke_body": self.joke_body,
            "punchline": self.punchline,
            "rating": self.rating,
            "likes": len(self.joke_likes)
        }

# joke1 = Joke.query.get(1)
# joke1 = {
#     "id": 1,
#     "joke_body": "Something hilarious",
#     "punchline": "Something equally hilarious",
#     "rating": "G",
#     "user": <user1>
# }
# print(joke1.user.username)