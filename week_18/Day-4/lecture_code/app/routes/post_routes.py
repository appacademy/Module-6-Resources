from flask import Blueprint, render_template, redirect
from app.forms import PostForm
from app.models import User, Post, db


post_routes = Blueprint("posts", __name__, url_prefix="/posts")


@post_routes.route("/all")
def get_all_posts():
    all_posts = Post.query.all()
    return render_template("all-posts.html", posts=all_posts, id=None)

@post_routes.route("/users/<int:id>")
def user_posts(id):
    user = User.query.get(id)
    user_posts = user.posts
    return render_template("all-posts.html", posts=user_posts, username=user.name)

@post_routes.route("/new", methods=["GET", "POST"])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        id = form.data["author"]
        user = User.query.get(id)
        params = {
            "author": user,
            # "author_id": id,
            "caption": form.data["caption"],
            "image_url": form.data["image"],
        }
        post = Post(**params)
        db.session.add(post)
        db.session.commit()
        return redirect("/posts/all")
    return render_template("new-post.html", form=form)

@post_routes.route("/<int:id>/update", methods=["GET", "POST"])
def update_post(id):
    form = PostForm()
    if form.validate_on_submit():
        updated_post = Post.query.get(id)
        updated_post.caption = form.data["caption"]
        updated_post.image_url = form.data["image"]
        updated_post.author_id = form.data["author"]
        db.session.commit()
        return redirect("/posts/all")

    elif form.errors:
        return render_template("new-post.html", post_id=id, form=form, errors=form.errors)
    else:
        post = Post.query.get(id)
        form.process(data=post.to_dict()) # type: ignore
        return render_template("new-post.html", post_id=id, form=form)


@post_routes.route("/<int:id>/delete")
def delete_post(id):
    post_to_delete = Post.query.get(id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect("/posts/all")

@post_routes.route("/<int:id>/like")
def like_post(id):
    post = Post.query.get(id)
    user = User.query.get(1)
    if post in user.liked_posts:
        user.liked_posts.remove(post)
    else:
        user.liked_posts.append(post)
    print(post.user_likes)
    print(user.liked_posts)
    db.session.commit()
    return redirect("/home")

