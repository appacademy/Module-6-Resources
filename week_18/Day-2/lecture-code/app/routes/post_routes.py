from flask import Blueprint, render_template, redirect
from ..posts import posts as seed_posts
from ..forms.post_form import PostForm
from datetime import date
from random import randint

posts = Blueprint("posts", __name__)


print(__name__, "Inside posts blueprint")



@posts.route("/all")
def feed():
    """Get all post and send to template for display"""
    # Query for all posts
    # all_posts = Post.query.all()
    sorted_posts = sorted(seed_posts, key=lambda post: post["date"], reverse=True)
    return render_template("feed.html", posts = sorted_posts)




@posts.route("/<int:id>")
def get_post_by_id(id):
    """returns a single post by its id"""
    # onme_post = Post.query.get(id)
    print(id)
    one_post = [post for post in seed_posts if post['id'] == id ]
    print(one_post)
    return render_template("feed.html", posts=one_post)



@posts.route("/new", methods=["GET", "POST"])
def create_new_post():
    """renders an empty form on get requests, and validates 
    a form and creates a resource on post requests"""
    form = PostForm()
    # form.author.choices= User.query.all()

    if form.validate_on_submit():
        # we will make a new post
        new_post = {
            "id": len(seed_posts) + 1,
            "caption": form.data["caption"],
            "image": form.data["image_url"],
            "author": form.data["author"],
            "date": date.today(),
            "likes": randint(1, 10)
        }
        print(new_post)
        seed_posts.append(new_post)
        return redirect("/posts/all")


    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, errors=form.errors)

    # DOTO - Post stuff
    return render_template("post_form.html", form=form, errors=None)

