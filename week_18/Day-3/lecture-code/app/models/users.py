from .db import db


class User(db.Model):
  __tablename__ = "users"
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), nullable=False)
  profile_pic = db.Column(db.String(255))
  
  posts = db.relationship("Post", back_populates="author")
  # post_likes = db.relationship("Post", secondary="likes", back_populates="user_likes")