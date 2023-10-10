from flask import Blueprint, render_template, redirect
from ..posts import posts as seed_posts


posts = Blueprint("posts", __name__)
print("in posts bp", __name__)


@posts.route("/all")
def get_all_posts():
    """get all the posts and return them """
    # all_post = Post.query.all()
    return render_template("feed.html", posts=seed_posts)


@posts.route("/<int:id>")
def get_post_by_id(id):
    """return a single post by the id passed to the route"""
    # one_post = Post.query.get(id)
    one_post = [post for post in seed_posts if post["id"] == id ]
    print(one_post)
    return render_template("feed.html", posts=one_post )

