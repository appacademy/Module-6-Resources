from .db import db


class User(db.Model):
  __tablename__ = "users"
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), nullable=False)
  profile_pic = db.Column(db.String(255))
  # bio = db.Column(db.String(2000))
  
  posts = db.relationship("Post", back_populates="author")
  # post_likes = db.relationship("Post", secondary="likes", back_populates="user_likes")

  
  def to_dict(self, called_from_posts=False):
    return {
      "id": self.id,
      "username": self.username,
      "email": self.email,
      "profile_pic": self.profile_pic,
      "posts": [post.id for post in self.posts]
    }