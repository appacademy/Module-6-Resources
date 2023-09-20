from .db import db
from .like import likes


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    profile_pic = db.Column(db.String(250))
    bio = db.Column(db.String(1000))


    # relationship attributes
    posts = db.relationship("Post", 
        back_populates="user",
    )
    user_likes = db.relationship(
        "Post",
        secondary=likes,
        back_populates="post_likes"
    )
  
    # profile = ["<User Profile 1>"]
    # shopping cart = []

    # user.email
    # user.profile.bio2
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "profilePic": self.profile_pic,
            "bio": self.bio,
            "posts": [post.to_dict() for post in self.posts],
            "likes": len(self.user_likes)
        }

    def to_dict_no_posts(self, posts=None):
        ret_dict =  {
            "id": self.id,
            "username": self.username,
            "profilePic": self.profile_pic,
            "bio": self.bio,
            "likes": len(self.user_likes)
        }
        if posts != None:
            ret_dict["posts"] = [post.to_dict() for post in self.posts]

        return ret_dict