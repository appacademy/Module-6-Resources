from .db import db


# class Like(db.Model):
#     __tablename__ = "likes"
#
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
#     post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key=True)

likes = db.Table(
    "likes",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True)
)
