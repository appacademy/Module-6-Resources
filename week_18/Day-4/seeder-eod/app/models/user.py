from .db import db
from .likes import likes

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    profile_pic = db.Column(db.String(250))
    bio = db.Column(db.String(500))


    # relationship attributes
    posts = db.relationship(
        "Post", 
        back_populates="user", 
    )
    user_likes = db.relationship(
        "Post",
        secondary=likes,
        back_populates="post_likes",
    )


    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "profilePic": self.profile_pic,
            "bio": self.bio,
            "posts": [post.to_dict_no_user() for post in self.posts]
    }


    def to_dict_no_posts(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "profilePic": self.profile_pic,
            "bio": self.bio,
    }




    # post = Post.query.get(1)
    # post.image = "http:///urlstuff"
    # post.user.username
