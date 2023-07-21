from .db import db

class Post(db.Model):
  __tablename__ = "posts"
  
  id = db.Column(db.Integer, primary_key=True)
  # author = db.Column(db.String(50), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  caption = db.Column(db.String(2000))
  image = db.Column(db.String(255), nullable=False)
  date = db.Column(db.DateTime())
  
  author = db.relationship("User", back_populates="posts")
  # user_likes = db.relationship("User", secondary="likes", back_populates="post_likes")
  
  def to_dict(self):
    return {
      "id": self.id,
      "user_id": self.user_id,
      "caption": self.caption,
      "image": self.image,
      "date": self.date,
      "author": self.author.to_dict()["username"]
    }
  