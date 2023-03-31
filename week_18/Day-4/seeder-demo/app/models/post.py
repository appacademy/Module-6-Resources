from .db import db
from .likes import likes


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(250), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey("users.id"))
    image = db.Column(db.String(250), nullable=False)
    post_date = db.Column(db.Date, nullable=False)

    # RELATIONSHIP ATTRIBUTED
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
        return f"<POST ID: {self.id} Author:{self.user.username} >"


    def to_dict(self):
        return {
            "id": self.id,
            "caption": self.caption,
            "image": self.image,
            "postDate": self.post_date,
            "user": self.user.to_dict_no_post()
       }


    #  def to_dict(self, user=False):
    #     data = {
    #         "id": self.id,
    #         "caption": self.caption,
    #         "image": self.image,
    #         "postDate": self.post_date,
   
    #     }
    #     if user == True:
    #         data["user"] = self.user.to_dict_no_post()
            
    #     return data

    def to_dict_no_user(self):
        return {
            "id": self.id,
            "caption": self.caption,
            "image": self.image,
            "postDate": self.post_date,
            "likes": len(self.post_likes)
       }
