from .db import db
from .likes import likes


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    profile_pic = db.Column(db.String(255))
    bio = db.Column(db.String(1000))

    posts = db.relationship("Post", back_populates="user")

    likes = db.relationship("Post", secondary=likes, back_populates="likes")
