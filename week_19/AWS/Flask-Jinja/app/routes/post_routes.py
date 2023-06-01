from flask import Blueprint, redirect, render_template
# from ..posts import posts as file_posts
from ..forms import PostForm
from datetime import date
from random import randint
from ..models import db, Post, User
from .AWS_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3

posts = Blueprint("posts", __name__)


@posts.route("/all")
def get_all_posts():
    """route to fetch and display all posts"""
    # Query our DB to get all posts
    all_posts = Post.query.order_by(Post.post_date.desc()).all()
    print(all_posts)
    return render_template("feed.html", posts=all_posts)



@posts.route("/<int:id>")
def get_post_by_id(id):
    """returns a single post by the given route param id"""
    one_post = Post.query.get(id)
    # one_post = [post for post in file_posts if post["id"] == id ]
    return render_template("feed.html", posts=[one_post])



@posts.route("/new", methods=["GET", "POST"])
def create_post():
    """handles displaying a new post form on get requests 
    and validating submitted data on post requests"""
    form = PostForm()

    form.author.choices = [(user.id, user.username) for user in User.query.all()]

    if form.validate_on_submit():


        image = form.data["image"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)

        if "url" not in upload:
            return render_template("post_form.html", form=form, type="post", errors=[upload])


        print(form.data["author"])
        selected_user = User.query.get(form.data["author"])
        print(selected_user)

        new_post = Post(
            caption=form.data["caption"],
            image=upload["url"],
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
        db.session.commit()
        return redirect("/posts/all")

    elif form.errors:
        return render_template("post_form.html", form=form, errors=form.errors, type="update", id=id)

    else:
        current_data = Post.query.get(id)
        form.process(obj=current_data)
        return render_template("post_form.html", form=form, errors=None, type="update", id=id)



@posts.route("/delete/<int:id>")
def delete(id):
    post_to_delete = Post.query.get(id)

    file_delete = remove_file_from_s3(post_to_delete.image)

    if file_delete:
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect("/posts/all")

    else:
        return "<h1>File delete error!</h1>"


