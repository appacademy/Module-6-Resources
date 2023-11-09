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

    def to_dict(self, user=False, printer=False):
        post_dict =  {
            "id": self.id,
            "caption": self.caption,
            "image": self.image,
            "postDate": self.post_date,

            "likes": len(self.post_likes)
        }
        if user:
            post_dict["user"] = self.user.to_dict_no_posts()

        if printer:
            print(post_dict)
            
        return post_dict

user.to_dict(user=True)
# post = Post.query.get(1)
# user = User.query.get(1)


# post.post_likes.append(user)

# user.user_likes.append(post)