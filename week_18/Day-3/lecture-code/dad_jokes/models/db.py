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
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    # RELATIONSHIPS
    jokes = db.relationship("Joke", back_populates="user")
    author_likes = db.relationship("Joke",
        secondary=likes,
        back_populates="joke_likes",
        cascade="all, delete"
    )


    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "jokes": [j.to_dict_no_user() for j in self.jokes]
        }
    
    
    def to_dict_no_joke(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
   

class Joke(db.Model):
    __tablename__ = 'jokes'

    id = db.Column(db.Integer, primary_key=True)
    joke_body = db.Column(db.String(255), nullable=False)
    punchline = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    #RELATIONSHIPS
    user = db.relationship("User", back_populates="jokes")
    joke_likes = db.relationship("User",
        secondary=likes,
        back_populates="author_likes",
        cascade='all, delete'
    )


    def __repr__(self):
        return f"< JokeId: {self.id} Rating: {self.rating} >"


    def to_dict(self):
        return {
            "id": self.id,
            "joke_body": self.joke_body,
            "punchline": self.punchline,
            "rating": self.rating,
            "user": self.user.to_dict_no_joke(),
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