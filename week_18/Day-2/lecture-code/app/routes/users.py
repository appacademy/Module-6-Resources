from flask import Blueprint, render_template
from app.posts import users, posts

user_routes = Blueprint("user_routes", __name__, url_prefix="/users")


@user_routes.route("/<int:id>")
def user_posts(id):
    user = list(filter(lambda x: x["id"] == id, users))[0]
    user_posts = list(filter(lambda x: user["name"] == x["author"], posts))
    print(user_posts)

    return render_template("posts.html", all_posts=user_posts, user=user)

