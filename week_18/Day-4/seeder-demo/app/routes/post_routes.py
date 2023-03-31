from flask import Blueprint, render_template, redirect
# from ..posts import posts as seed_posts
from ..forms.post_form import PostForm
from datetime import date
from random import randint
from ..models import db, User, Post


posts = Blueprint("posts", __name__)

# print("inside posts BP", __name__)


@posts.route("/all")
def get_all_posts():
    """get all posts and display them"""
    posts = Post.query.order_by(Post.post_date.desc()).all()
    print(posts)
    # sorted_posts = sorted(seed_posts, key=lambda post: post['date'], reverse=True)
    return render_template("feed.html", posts=posts)



@posts.route("/<int:id>")
def get_post_by_id(id): 
    """return a single post by its ID"""
    print(id)
    one_post = Post.query.get(id)
    # print(one_post.to_dict(user=True))
    return render_template("feed.html", posts=[one_post])

       

@posts.route("/new", methods=["GET", "POST"])
def add_new_post():
    """returns a new post form on get requests, 
    validates and saves the new resource on post"""

    form = PostForm()
    form.author.choices = [ (user.id, user.username) for user in User.query.all()]
    # print(form.author.choices)
    # query for data if needed in the form

    if form.validate_on_submit():
        selected_user = User.query.get(form.data["author"])
        # print(selected_user)

        new_post =Post(
            user=selected_user,
            caption= form.data["caption"],
            image= form.data["image"],
            post_date= date.today(),
        )
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
   
        return redirect("/posts/all")
        # return new_post

    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, type="post", errors=form.errors)


    return render_template("post_form.html", form=form, type="post", errors=None)



@posts.route("/update/<int:id>", methods=["GET", "POST"])
def update_post(id):
    form = PostForm()

    form.author.choices = [ (user.id, user.username) for user in User.query.all()]

    if form.validate_on_submit():
        post_to_update = Post.query.get(id)

        selected_user = User.query.get(form.data["author"])
        post_to_update.user = selected_user
        post_to_update.caption = form.data["caption"]
        post_to_update.image = form.data["image"]
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