from .db import db
from .likes import likes

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(250), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey("users.id"))
    image = db.Column(db.String(250), nullable=False)
    post_date = db.Column(db.Date, nullable=False)

    # relationshi[ attributes
    user = db.relationship("User", back_populates="posts")
    post_likes = db.relationship(
        "User",
        secondary=likes,
        back_populates="user_likes"
    )



    def to_dict(self, user=False, printer=False):
        return_dict = {
            "id": self.id,
            "caption": self.caption,
            "image": self.image,
            "postDate": self.post_date,
        }
        if user:
            return_dict["user"]: self.user.to_dict_no_post()

        if printer:
            print(return_dict)

        return return_dict
#     ['< User 1>']

# post1.user.username