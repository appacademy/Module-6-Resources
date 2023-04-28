from flask import Blueprint, redirect, render_template
# from ..posts import posts as file_posts
from ..forms import PostForm
from datetime import date
from random import randint
from ..models import db, Post, User


posts = Blueprint("posts", __name__)


@posts.route("/all")
def get_all_posts():
    """route to fetch and display all posts"""
    # Query our DB to get all posts
    all_posts = Post.query.order_by(Post.post_date.desc()).all()
    print(all_posts)
    all_posts_dict = [post.to_dict() for post in all_posts]
    print(all_posts_dict)
    return render_template("feed.html", posts=all_posts)
    # return {"response": all_posts_dict}



@posts.route("/<int:id>")
def get_post_by_id(id):
    """returns a single post by the given route param id"""
    one_post = Post.query.get(id)
    print(one_post.to_dict())
    # one_post = [post for post in file_posts if post["id"] == id ]
    # return render_template("feed.html", posts=[one_post])
    return one_post.to_dict()


@posts.route("/new", methods=["GET", "POST"])
def create_post():
    """handles displaying a new post form on get requests 
    and validating submitted data on post requests"""
    form = PostForm()

    form.author.choices = [(user.id, user.username) for user in User.query.all()]

    if form.validate_on_submit():
        print(form.data["author"])
        selected_user = User.query.get(form.data["author"])
        print(selected_user)

        new_post = Post(
            caption=form.data["caption"],
            image=form.data["image"],
            post_date = date.today(),
            user=selected_user
        )
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/posts/all")


    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, type="post", errors=form.errors)

    # implement post functionality here

    return render_template("post_form.html", form=form, type="post", errors=None)



@posts.route("/update/<int:id>", methods=["GET", "POST"])
def update_post(id):
    form = PostForm()

    form.author.choices = [(user.id, user.username) for user in User.query.all()]

    if form.validate_on_submit():
        post_to_update = Post.query.get(id)
        selected_user = User.query.get(form.data["author"])

        post_to_update.user = selected_user
        post_to_update.caption = form.data["caption"]
        post_to_update.image = form.data["image"]
        post_to_update.post_date = date.today()

        db.session.commit()
        return redirect(f"/posts/{post_to_update.id}")

    elif form.errors:
        return render_template("post_form.html", form=form, type="update", id=id, errors=form.errors)

    else:
        current_data = Post.query.get(id)
        form.process(obj=current_data)
        return render_template("post_form.html", form=form, type="update", id=id, errors=None)



@posts.route("/delete/<int:id>")
def delete_post(id):
    post_to_delete = Post.query.get(id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect("/posts/all")