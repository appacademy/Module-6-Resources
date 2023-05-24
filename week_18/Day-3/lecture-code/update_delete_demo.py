from pprint import pprint
from app.models import db, Post, User
from app import app


with app.app_context():
    # post = Post.query.get(5)
    post = db.session.get(Post, 4)
    # post.caption = "This darn punk stole my frickin' tent!!!"
    # post.image = ""
    pprint(post.to_dict())
    # post.author = 1
    # db.session.delete(post)
    db.session.commit()
