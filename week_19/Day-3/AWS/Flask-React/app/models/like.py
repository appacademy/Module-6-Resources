from .db import db


likes = db.Table(
    "likes",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
)


# example of input into likes and how composite primary key will prevent duplicatre combos
# like_1 = (1, 1)
# like_2 = (1, 2)
# like_3 = (2, 1)
# like_4 = (1, 1)