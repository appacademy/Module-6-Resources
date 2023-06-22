from .db import db
from .likes import likes


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    image = db.Column(db.String(250), nullable=False)
    post_date = db.Column(db.Date, nullable=False)

    #relationship attributes
    user = db.relationship("User", back_populates="posts")
    post_likes = db.relationship(
        "User",
        secondary=likes,
        back_populates="user_likes"
    )


    def to_dict(self):
        return {
            "id": self.id,
            "caption": self.id,
            "image": self.image,
            "likes": len(self.post_likes),
            "postDate": self.post_date,
            "user": self.user.to_dict_no_post(),
        }


    def to_dict_no_user(self):
        return {
            "id": self.id,
            "caption": self.id,
            "image": self.image,
            "likes": len(self.post_likes),
            "postDate": self.post_date,
        }