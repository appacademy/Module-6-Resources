from flask import Blueprint, redirect, render_template
from ..posts import posts as file_posts
from ..forms import PostForm
from datetime import date
from random import randint

posts = Blueprint("posts", __name__)


print(__name__)


@posts.route("/all")
def get_all_posts():
    """route to fetch and display all posts"""
    # Query our DB to get all posts
    # posts = Post.query.all()
    return render_template("feed.html", posts=file_posts)



@posts.route("/<int:id>")
def get_post_by_id(id):
    """returns a single post by the given route param id"""
    # post = Post.query.get(id)
    one_post = [post for post in file_posts if post["id"] == id ]
    return render_template("feed.html", posts=one_post)



@posts.route("/new", methods=["GET", "POST"])
def create_post():
    """handles displaying a new post form on get requests 
    and validating submitted data on post requests"""
    form = PostForm()


    if form.validate_on_submit():
        new_post = {
            "id": len(file_posts) + 1,
            "author": form.data["author"],
            "caption": form.data["caption"],
            "image": form.data["image_url"],
            "date": date.today(),
            "likes": randint(1, 10)
        }
        print(new_post)
        file_posts.append(new_post)
        return redirect("/posts/all")


    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, errors=form.errors)

    # implement post functionality here

    return render_template("post_form.html", form=form, errors=None)

