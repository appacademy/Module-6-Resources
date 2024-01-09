from pprint import pprint
from datetime import datetime
from random import randint
from flask import Blueprint, render_template, redirect
from app.posts import posts, users
from app.forms import PostForm


post_routes = Blueprint("posts", __name__, url_prefix="/posts")


@post_routes.route("/all")
def all_posts():
    return render_template("all-posts.html", posts=posts, id=None)

@post_routes.route("/users/<int:id>")
def user_posts(id):
    user = list(filter(lambda x: x["id"] == id, users))[0]
    user_posts = [post for post in posts if post["author"] == user["name"]]
    print(user_posts)
    return render_template("all-posts.html", posts=user_posts, username=user["name"])

@post_routes.route("/new", methods=["GET", "POST"])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        username = [user["name"] for user in users if user["id"] == int(form.data["author"])][0]
        new_post = {
            "id": len(posts) + 1,
            "author": username,
            "caption": form.data["caption"],
            "image": form.data["image"],
            "date": datetime.now(),
            "likes": randint(1, 10)
        }
        posts.append(new_post)
        return redirect("/posts/all")
    return render_template("new-post.html", form=form)

@post_routes.route("/<int:id>/update", methods=["GET", "POST"])
def update_post(id):
    form = PostForm()
    if form.validate_on_submit():
        username = [user["name"] for user in users if user["id"] == int(form.data["author"])][0]
        new_post = {
            "id": id,
            "author": username,
            "caption": form.data["caption"],
            "image": form.data["image"],
            "date": datetime.now(),
            "likes": randint(1, 10)
        }
        idx = [idx for idx, post in enumerate(posts) if post["id"] == id][0]
        posts[idx] = new_post
        pprint(posts)
        return redirect("/posts/all")

    elif form.errors:
        pass
    else:
        post = [post for post in posts if post["id"] == id][0]
        user_id = [user["id"] for user in users if user["name"] == post["author"]][0]
        post["author"] = user_id
        form.process(data=post)
        return render_template("new-post.html", post_id=id, form=form)


@post_routes.route("/<int:id>/delete")
def delete_post(id):
    post_to_delete = [post for post in posts if post["id"] == id][0]
    posts.remove(post_to_delete)
    return redirect("/posts/all")
      
