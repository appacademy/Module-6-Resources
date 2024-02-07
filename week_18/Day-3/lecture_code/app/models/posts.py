from datetime import datetime
from .db import db


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    caption = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    user = db.relationship("User", back_populates="posts")
    user_likes = db.relationship("User", secondary="likes", back_populates="liked_posts")

    def to_dict(self):
        return {
            "id": self.id,
            "author_id": self.author_id,
            "caption": self.caption,
            "image": self.image,
            "created_at": self.created_at,
            "author": self.user.name,
            "likes": len(self.user_likes),
            "user_likes": [user.id for user in self.user_likes],
        }


