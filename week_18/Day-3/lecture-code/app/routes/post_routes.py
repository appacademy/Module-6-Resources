from flask import Blueprint, render_template, redirect
from ..posts import posts as seed_posts
from ..forms.post_form import PostForm
from datetime import date
from random import randint
from ..models import db, Post, User 


posts = Blueprint("posts", __name__)
# print("in the posts bp", __name__)


@posts.route("/all")
def get_all_posts():
    """get all posts and return a feed of those posts"""
    posts = Post.query.order_by(Post.post_date.desc()).all()
    print(posts)
    # sorted_posts = sorted(seed_posts, key=lambda post: post["date"], reverse=True)
    return render_template("feed.html", posts=posts)
    # return "<div><p>This is text</p></div>"
    # return sorted_posts



@posts.route("/<int:id>")
def get_post_by_id(id):
    """get a post by its id"""
    post = Post.query.get(id)
    # one_post = [post for post in seed_posts if post['id'] == id]
    print(post.to_dict())
    return render_template("feed.html", posts=[post])



@posts.route("/new", methods=["GET", "POST"])
def create_new_post():
    """handles displaying an empty form on get requests and 
    the submission of that form on post requests"""

    form = PostForm()
    form.author.choices = [(user.id, user.username) for user in User.query.all()]



    if form.validate_on_submit():
        selected_user = User.query.get(form.data["author"])
        # print(selected_user.to_dict())
        new_post = Post(
            caption=form.data["caption"],
            image=form.data["image"],
            post_date=date.today(),
            user=selected_user
        )
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/posts/all")

    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, errors=form.errors)


    return render_template("post_form.html", form=form, errors=None)



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
        return redirect(f"/posts/{post_to_update.id}")


    elif form.errors:
        return render_template("post_form.html", form=form,type="update", id=id, errors=form.errors)


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