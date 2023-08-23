from .db import db
from .like import likes

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    profile_pic = db.Column(db.String(250))
    bio = db.Column(db.String(250))

    # relationship atrribute
    posts = db.relationship("Post", back_populates="user")
    user_likes = db.relationship(
        "Post",
        secondary=likes,
        back_populates="post_likes"
    )


    def to_dict(self, posts=False):
        user_dictionary = {
            "id": self.id,
            "username": self.username,
            "profilePic": self.profile_pic,
            "bio": self.bio,
        }
        if posts:
            user_dictionary["posts"] = [post.to_dict() for post in self.posts]
  
        return user_dictionary


    def to_dict_no_post(self):
        return {
            "id": self.id,
            "username": self.username,
            "profilePic": self.profile_pic,
            "bio": self.bio,
        }