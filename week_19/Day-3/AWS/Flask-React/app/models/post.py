from .db import db
from .like import likes

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(255), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    image = db.Column(db.String(250), nullable=False)
    post_date = db.Column(db.Date)

    # relationship atrribute
    user = db.relationship("User", back_populates="posts")
    post_likes = db.relationship(
        "User",
        secondary=likes,
        back_populates="user_likes"
    )



    def to_dict(self):
        return {
            "id": self.id,
            "caption": self.caption,
            "image": self.image,
            "postDate": self.post_date,
            "user": self.user.to_dict_no_post(),
            "likes": len(self.post_likes)
       }

# user id as a route parameter and post
# query for the post
# query for the user
# post.post_likes.append(user_who_liked it)
# db.session.commit()



# selected_post = Post.query.get(1)
# selected_post = {
#     "id": 1,
#     "caption": "Great post",
#     "author": 1,
#     "image": "https://someurlstring",
#     "post_date": "8/16/2023",
    # "user": {
    #     "id": 1,
    #     "username": "brads",
    #     "email": "brad@gamil.com",
    #     "profile_pic": "another url",
    #     "bio": "I am cool"
    # },
    # "likes": ["< User 1 >, <User 2>"]
# }
# selected_post.user.username