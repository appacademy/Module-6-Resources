from flask import Blueprint, render_template, redirect
from ..posts import posts as post_data
from ..forms.post_form import PostForm
from datetime import date
from random import randint

posts = Blueprint("posts", __name__)


print(__name__, "in the posts route file")



@posts.route("/all")
def get_all_posts():   
    """gat all of the posts that exist and display them in a feed""" 
    # query the DB for all posts
    # all_posts = Post.query.all()
    return render_template("feed.html", posts=post_data)


@posts.route("/<int:id>")
def get_post_by_id(id):
    """display a single post by its id"""
    # one_post = Post.query.get(id)
    one_post = [post for post in post_data if post["id"] == id]
    print(one_post)
    return render_template("feed.html", posts=one_post)


@posts.route("/new", methods=["GET", "POST"])
def create_new_post():
    form = PostForm()

    if form.validate_on_submit():
        new_post = {
            "id": len(post_data) + 1,
            "author": form.data["author"],
            "caption": form.data["caption"],
            "image": form.data["image_url"],
            "date": date.today(),
            "likes": randint(1, 10)
        }
        print(new_post)
        post_data.append(new_post)
        return redirect("/posts/all")

    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, errors=form.errors)

    return render_template("post_form.html", form=form, errors=None)