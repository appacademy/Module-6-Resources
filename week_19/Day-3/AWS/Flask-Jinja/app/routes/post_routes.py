from flask import Blueprint, render_template, redirect
from ..posts import posts as seed_posts
from ..forms.post import PostForm
from datetime import date
from random import randint
from ..models import db, Post, User
from .aws_helpers import get_unique_filename, upload_file_to_s3, remove_file_from_s3


posts = Blueprint("posts", __name__)
# print("in posts bp", __name__)


@posts.route("/all")
def get_all_posts():
    """get all the posts and return them """
    all_posts = Post.query.order_by(Post.post_date.desc()).all()
    see_posts = [post.to_dict() for post in all_posts]
    print(see_posts)
    print(all_posts)
    # sorted_posts = sorted(seed_posts, key=lambda post: post["date"], reverse=True)
    return render_template("feed.html", posts=all_posts)
    # return see_posts


@posts.route("/<int:id>")
def get_post_by_id(id):
    """return a single post by the id passed to the route"""
    one_post = Post.query.get(id)
    # one_post = [post for post in seed_posts if post["id"] == id ]
    print(one_post)
    return render_template("feed.html", posts=[one_post] )


@posts.route("/new", methods=["GET", "POST"])
def create_new_user():
    """ route that handles displaying a form on get requets and 
    handles post submission on post requests"""
    form = PostForm()
    form.author.choices = [(user.id, user.username) for user in User.query.all()]


    if form.validate_on_submit():
        selected_user = User.query.get(form.data["author"])

        image = form.data['image']
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        print(upload)

        if "url" not in upload:
            return render_template("post_form.html", form=form, errors=upload)


        
        new_post = Post(
            caption=form.data["caption"],
            image=upload["url"],
            user=selected_user,
            post_date=date.today(),    
        )
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/posts/all")

    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, errors=form.errors)

    return render_template("post_form.html", form=form, errors=None)



@posts.route("/update/<int:id>", methods=['GET', 'POST'])
def update_post(id):
    form = PostForm()

    form.author.choices = [(user.id, user.username) for user in User.query.all()]

    if form.validate_on_submit():
        # gets a ref to the resouce we want to update
        post_to_update = Post.query.get(id)
        # get e ref to the new user, if there is one
        selected_user = User.query.get(form.data["author"])
        post_to_update.user = selected_user
        post_to_update.caption = form.data["caption"]
        post_to_update.image = form.data["image"]
        db.session.commit()
        return redirect(f"/posts/{post_to_update.id}")


    elif form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, type="update", id=id, errors=form.errors)

    else:
        current_data = Post.query.get(id)
        form.process(obj=current_data)
        return render_template("post_form.html", form=form, type="update", id=id,  errors=None)



@posts.route("/delete/<int:id>")
def delete_post(id):
    post_to_delete = Post.query.get(id)


    file_to_delete = remove_file_from_s3(post_to_delete.image)

    if file_to_delete:
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect("/posts/all")
    
    else:
        print(file_to_delete)
        return "<h1>File delete error!</h1>"