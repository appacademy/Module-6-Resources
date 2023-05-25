from .db import db
from datetime import datetime
from .likes import likes


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    caption = db.Column(db.String(2000), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())

    user = db.relationship("User", back_populates="posts")

    likes = db.relationship("User", secondary=likes, back_populates="likes")

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "caption": self.caption,
            "image": self.image,
            "date": self.date,
            "user": self.user,
            "likes": len(self.likes),
        }
