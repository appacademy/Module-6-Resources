from flask import Blueprint, render_template, redirect
from ..posts import posts as seed_posts
from ..forms.post_form import PostForm
from datetime import datetime 
from random import randint

posts = Blueprint("posts", __name__)
# print(__name__)


@posts.route("/all")
def view_all_posts():
    # all_posts = Post.query.all()
    sorted_posts = sorted(seed_posts, key=lambda post: post["date"], reverse=True)
    return render_template("feed.html", posts=sorted_posts)



@posts.route("/<int:id>")
def post_by_id(id):
    # post = Post.guery.get(id)
    one_post = [post for post in seed_posts if post['id'] == id]
    print(one_post)
    return render_template("feed.html", posts=one_post)



@posts.route("/new", methods=["GET", "POST"])
def create_new_post():

    form = PostForm()

    if form.validate_on_submit():
        
        new_post = {
            "id": len(seed_posts) + 1,
            "author": form.data["author"],
            "caption": form.data["caption"],
            "image": form.data["image_url"],
            "date": datetime.now(),
            "likes": randint(1, 10)
        }
        print(new_post)
        seed_posts.append(new_post)
        return redirect("/posts/all")

    if form.errors:
        print(form.errors)    
        return render_template("post_form.html", form=form, errors=form.errors )


    return render_template("post_form.html", form=form, errors=None )