from flask import Blueprint, render_template, redirect
from ..posts import posts as seed_posts
from ..forms.post_form import PostForm
from datetime import date
from random import randint
from ..models import db, Post, User

posts = Blueprint("posts", __name__)


print(__name__, "Inside posts blueprint")


@posts.route("/all")
def feed():
    """Get all post and send to template for display"""
    # Query for all posts
    sorted_posts = Post.query.order_by(Post.date.desc()).all()
    # sorted_posts = sorted(seed_posts, key=lambda post: post["date"], reverse=True)
    return render_template("feed.html", posts=sorted_posts)


@posts.route("/<int:id>")
def get_post_by_id(id):
    """returns a single post by its id"""
    one_post = [Post.query.get(id)]
    print(id)
    # one_post = [post for post in seed_posts if post["id"] == id]
    print(one_post)
    return render_template("feed.html", posts=one_post)


@posts.route("/new", methods=["GET", "POST"])
def create_new_post():
    """renders an empty form on get requests, and validates
    a form and creates a resource on post requests"""
    form = PostForm()
    users = User.query.all()
    form.author.choices = [(user.id, user.username) for user in users]

    if form.validate_on_submit():
        # we will make a new post
        params = {
            "caption": form.data["caption"],
            "image": form.data["image_url"],
            "date": date.today(),
        }

        new_post = Post(**params)
        # new_post.author = form.data["author"]
        user = User.query.get(form.data["author"])
        new_post.user = user
        print(new_post)
        db.session.add(new_post)
        db.session.commit()

        # seed_posts.append(new_post)
        return redirect("/posts/all")

    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, errors=form.errors)

    # DOTO - Post stuff
    return render_template("post_form.html", form=form, errors=None)
