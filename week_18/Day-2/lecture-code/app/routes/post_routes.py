from flask import Blueprint, render_template, redirect
from ..posts import posts as seed_posts
from ..forms.post_form import PostForm
from datetime import date
from random import randint 

posts = Blueprint("posts", __name__)

# print("inside posts BP", __name__)


@posts.route("/all")
def get_all_posts():
    """get all posts and display them"""
    # posts = Post.query.all()
    print(seed_posts)
    sorted_posts = sorted(seed_posts, key=lambda post: post['date'], reverse=True)
    return render_template("feed.html", posts=sorted_posts)



@posts.route("/<int:id>")
def get_post_by_id(id): 
    """return a single post by its ID"""
    print(id)
    one_post = [post for post in seed_posts if post["id"] == id ]
    print(one_post)
    return render_template("feed.html", posts=one_post)

       

@posts.route("/new", methods=["GET", "POST"])
def add_new_post():
    """returns a new post form on get requests, 
    validates and saves the new resource on post"""

    form = PostForm()
    # query for data if needed in the form

    if form.validate_on_submit():
        new_post ={
            "id": len(seed_posts) + 1,
            "author": form.data["author"],
            "caption": form.data["caption"],
            "image": form.data["image_url"],
            "date": date.today(),
            "likes": randint(1, 10)
        }
        print(new_post)
        seed_posts.append(new_post)
        return redirect("/posts/all")
        # return new_post

    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, errors=form.errors)


    return render_template("post_form.html", form=form, errors=None)