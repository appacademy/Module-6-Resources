from .db import db
from .like import likes


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer,primary_key=True)
    caption = db.Column(db.String(250), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    image = db.Column(db.String(250), nullable=False)
    post_date = db.Column(db.Date, nullable=False)

    # relationship attributes
    user = db.relationship("User", 
        back_populates="posts",
    )
    post_likes = db.relationship(
        "User",
        secondary=likes,
        back_populates="user_likes"
    )


    def to_dict(self):
        return {
            "id": self.id,
            "caption": self.caption,
            "image": self.image,
            "postDate": self.post_date,
            "user": self.user.to_dict_no_posts(),
            "likes": len(self.post_likes)
       }

# Query output with the relationship attribute
    # post = Post.query.get(1)
    # post = {
    #     "id": 1,
    #     "caption": "Cats say something",
    #     "author": 1,
    #     "image": "http://url",
    #     "post_date": "9/13/23",
    #     "user":[ {
    #         "id": 1,
    #         "username": 'patch',
    #         "email": "patch@hotmail.com",
    #         "profile_pic": "http://url",
    #         "bio": "patch is cool"
    #     } ]
    # }