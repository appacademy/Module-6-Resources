from datetime import datetime
from random import randint
from flask import Blueprint, render_template, redirect
from app.posts import posts
from app.forms.post_form import NewPost

post_routes = Blueprint("post_routes", __name__)

@post_routes.route("/all")
def all_posts():
    return render_template("posts.html", all_posts=posts)


@post_routes.route("/new", methods=["GET", "POST"])
def new_post():
    form = NewPost()
    print(form.data)
    if form.validate_on_submit():
        params = {
            "id": len(posts) + 1,
            "author": form.data["author"],
            "caption": form.data["caption"],
            "image": form.data["image"],
            "date": datetime.now(),
            "likes": randint(0,100)
        }
        posts.append(params)
        return redirect("/posts/all")
    print(form.errors)
    return render_template("new_post.html", form=form)

@post_routes.route("/<int:id>/update", methods=["GET", "POST"])
def update_post(id):
    form = NewPost()
    if form.validate_on_submit():
        params = {
            "id": id,
            "author": form.data["author"],
            "caption": form.data["caption"],
            "image": form.data["image"],
            "date": datetime.now(),
            "likes": randint(0,100)
        }
        idx = [idx for idx, post in enumerate(posts) if post["id"] == id][0]
        posts[idx] = params
        return redirect("/posts/all")
    post = [post for post in posts if post["id"] == id][0]
    form.process(data=post)
    return render_template("new_post.html", id=post["id"], form=form)

@post_routes.route("/<int:id>/delete")
def delete_post(id):
    post_to_delete = [post for post in posts if post["id"] == id][0]
    posts.remove(post_to_delete)
    return redirect("/posts/all")
        
    

