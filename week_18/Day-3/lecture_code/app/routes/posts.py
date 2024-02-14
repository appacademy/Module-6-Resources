from datetime import datetime
from random import randint
from flask import Blueprint, render_template, redirect
from ..models import db, Post, User, likes
from app.forms.post_form import NewPost

post_routes = Blueprint("post_routes", __name__)

@post_routes.route("/all")
def all_posts():
    posts = Post.query.all()
    print([post.to_dict() for post in posts])
    return render_template("posts.html", all_posts=[post.to_dict() for post in posts])


@post_routes.route("/new", methods=["GET", "POST"])
def new_post():
    form = NewPost()
    if form.validate_on_submit():
        params = {
            "caption": form.data["caption"],
            "image": form.data["image"],
            "author_id": form.data["author"]
        }
        post = Post(**params)
        db.session.add(post)
        db.session.commit()
        return redirect("/posts/all")
    print(form.errors)
    return render_template("new_post.html", form=form)

@post_routes.route("/<int:id>/update", methods=["GET", "POST"])
def update_post(id):
    form = NewPost()
    if form.validate_on_submit():
        post = Post.query.get(id)
        post.author_id = form.data["author"]
        post.caption = form.data["caption"]
        post.image = form.data["image"]
        db.session.commit()
        return redirect("/posts/all")
    post = Post.query.get(id)
    post_dict = post.to_dict()
    post_dict["author"] = post_dict["author_id"]
    form.process(data=post_dict)
    return render_template("new_post.html", id=post.to_dict()["id"], form=form)

@post_routes.route("/<int:id>/delete")
def delete_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/posts/all")
        

@post_routes.route("/<int:id>/like")
def like(id):
    post = Post.query.get(id)
    user_1 = User.query.get(1)
    user_1.liked_posts.append(post)
    # post.user_likes.append(user_1)
    db.session.commit()
    return redirect("/posts/all")


@post_routes.route("/<int:id>/unlike")
def dislike(id):
    post = Post.query.get(id)
    user_1 = User.query.get(1)
    user_1.liked_posts.remove(post)
    # post.user_likes.append(user_1)
    db.session.commit()
    return redirect("/posts/all")

    

    

