from datetime import datetime
from random import randint
from flask import Blueprint, render_template, redirect
from app.posts import posts
from app.forms.posts import NewPost


post_routes = Blueprint("post_routes", __name__)

@post_routes.route("/")
def all_posts():

    return render_template("all_posts.html", posts=posts)
    # return { post["id"]: post for post in posts }

@post_routes.route("/<int:id>")
def single_post(id):
    single_post = [posts[id]]
    # print(single_post)
    # return "single_post"
    return render_template("all_posts.html", posts=single_post)

@post_routes.route("/new")
def new_post():
    form = NewPost()
    print(form.data)
    return render_template("new_post_form.html", form=form)

@post_routes.route("/new", methods=["POST"])
def make_new_post():
    form = NewPost()
    # print("form!!!!", form.data)
    # print("form errors", form.errors)
    if form.validate_on_submit():
        params = {
            "id": len(posts) + 1,
            "author": form.data["author"],
            "image": form.data["image"],
            "caption": form.data["caption"],
            "date": datetime.now(),
            "likes": randint(0, 100)
        }
        posts.append(params)
        return redirect("/posts")
    # print("form errors", form.errors)

    return "Hello"

    
@post_routes.route("/<int:id>/delete")
def delete_post(id):
    post_to_delete = [post for post in posts if post["id"] == id][0]
    # test = posts.find()
    print(post_to_delete)
    posts.remove(post_to_delete)
    return redirect("/posts")
    

