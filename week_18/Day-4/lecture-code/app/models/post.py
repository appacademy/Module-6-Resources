from .db import db
from .likes import likes

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(255), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    post_date = db.Column(db.Date, nullable=False)

    # relationship attribute
    user = db.relationship(
        "User", 
        back_populates="posts"
    )
    
    post_likes = db.relationship(
        "User",
        secondary=likes,
        back_populates="user_likes"
    )

    def __repr__(self):
        return f"< Post: {self.id}, author: {self.user.username}>"