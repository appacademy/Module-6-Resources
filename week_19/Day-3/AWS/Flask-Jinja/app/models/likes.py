from .db import db


likes = db.Table(
    "likes",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
)

# "id"  "user_id"  "post_id"
#  1        1           1
#  2        1           2
#  3        1           1  
#  4        2           1 


