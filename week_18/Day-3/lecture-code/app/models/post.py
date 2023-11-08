from .db import db
from .likes import likes 

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(250), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey("users.id"))
    image = db.Column(db.String(250), nullable=False)
    post_date = db.Column(db.Date, nullable=False)

    # relationship attributed
    user = db.relationship(
        "User", 
        back_populates="posts"
    )

    # post = Post.query.get(1)
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
            "user": self.user.to_dict(),
            "likes": len(self.post_likes)
        }

# post = Post.query.get(1)
# user = User.query.get(1)


# post.post_likes.append(user)

# user.user_likes.append(post)