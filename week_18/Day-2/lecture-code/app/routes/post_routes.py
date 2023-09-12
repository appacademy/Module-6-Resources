from flask import Blueprint, render_template, redirect
from ..posts import posts as seed_posts
from ..forms.post_form import PostForm
from datetime import date
from random import randint

posts = Blueprint("posts", __name__)
# print("in the posts bp", __name__)


@posts.route("/all")
def get_all_posts():
    """returns all posts"""
    # Query   posts = Posts.query.all()
    return render_template("feed.html", posts=seed_posts)


@posts.route("/<int:id>")
def get_post_by_id(id):
    """returns a single post by the given id provided as a route parameter"""
    # one_post = Posts.query.get(id)
    one_post = [ post for post in seed_posts if post['id'] == id]
    return render_template("feed.html", posts=one_post)


@posts.route("/new", methods=['GET', 'POST'])
def create_new_post():
    """route to handle displaying the new post form on get requests, and validating 
    data and creating a new resource on post requests"""
    form = PostForm()

    if form.validate_on_submit():
        # handle the post method stuff
        new_post = {
            "id": len(seed_posts) + 1,
            "author": form.data['author'],
            "caption": form.data['caption'],
            "image": form.data['image_url'],
            "date": date.today(),
            "likes": randint(1, 7)
        }
        print(new_post)
        seed_posts.append(new_post)
        return redirect("/posts/all")

    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, errors=form.errors)

    return render_template("post_form.html", form=form, errors=None)