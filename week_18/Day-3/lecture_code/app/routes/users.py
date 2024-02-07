from flask import Blueprint, render_template
# from app.posts import users, posts
from ..models import User, Post, likes

user_routes = Blueprint("user_routes", __name__, url_prefix="/users")


@user_routes.route("/<int:id>")
def user_posts(id):
    user = User.query.get(id)
    posts = user.posts
    print(posts)
    return render_template("posts.html", all_posts=[post.to_dict() for post in posts], username=user.name)

