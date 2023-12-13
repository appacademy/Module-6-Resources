from .db import db


likes = db.Table(
    'likes',
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("posts_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True)
)

# (1, 1)
# (1, 2)
# (2, 1)
# (1, 1)