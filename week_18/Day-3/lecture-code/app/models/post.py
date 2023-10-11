from .db import db
from .likes import likes

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(250), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    image = db.Column(db.String(250), nullable=False)
    post_date = db.Column(db.Date, nullable=False)


    # relationship attributes
    user = db.relationship(
        "User", 
        back_populates="posts",
    )
    post_likes = db.relationship(
        "User",
        secondary=likes,
        back_populates="user_likes",
    )


    def to_dict(self):
        return {
            "id": self.id,
            "caption": self.caption,
            "image": self.image,
            "postDate": self.post_date,
            "user": self.user.to_dict(),
            "likes": len(self.post_likes),
    }

# user = User.query.get(1)
# post = Post.query.get(1)
# if user not in post.post_likes:
#     post.post_likes.append(user)
# else:
#     print("user already liked this post!")



# selected_user = User.query.get(1)

#     new_post = Post(
#         caption="This is a great post",
#         user = selected_user
#     )
