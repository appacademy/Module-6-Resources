from .db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    posts = db.relationship("Post", back_populates="author")
    liked_posts = db.relationship("Post", secondary="likes", back_populates="user_likes")


