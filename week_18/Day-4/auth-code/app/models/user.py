from .db import db
from .likes import likes
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    hashed_password = db.Column(db.String(100), nullable=False)
    profile_pic = db.Column(db.String(250))
    bio = db.Column(db.String(300))
    
    # relationship attribute
    posts = db.relationship(
        "Post",
        back_populates="user",
    )
    
    user_likes = db.relationship(
        "Post",
        secondary=likes,
        back_populates="post_likes"
    )

    @property 
    def password(self):
        return self.hashed_password


    @password.setter 
    def password(self, password):
        self.hashed_password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)


    def __repr__(self):
        return f'< User: {self.id}, username: {self.username} >'