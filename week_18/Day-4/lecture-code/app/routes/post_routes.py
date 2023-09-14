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
    """returns all posts"""
    all_posts = Post.query.order_by(Post.post_date.desc()).all()
    print(all_posts)
    return render_template("feed.html", posts=all_posts)


@posts.route("/<int:id>")
def get_post_by_id(id):
    """returns a single post by the given id provided as a route parameter"""
    # one_post = Posts.query.get(id)
    # one_post = [ post for post in seed_posts if post['id'] == id]
    one_post = Post.query.get(id)
    # print(one_post.to_dict())
    return render_template("feed.html", posts=[one_post])


@posts.route("/new", methods=['GET', 'POST'])
def create_new_post():
    """route to handle displaying the new post form on get requests, and validating 
    data and creating a new resource on post requests"""
    form = PostForm()

    users = User.query.all()
    all_users = [user.to_dict() for user in users]
    # print(all_users)
    # print(users)
    form.author.choices = [(user.id, user.username) for user in User.query.all()]
    # print(form.author.choices)

    if form.validate_on_submit():
        selected_user = User.query.get(form.data["author"])
        # print(selected_user)
      
        new_post = Post(
            caption=form.data["caption"],
            image=form.data["image"],
            post_date=date.today(),
            user=selected_user,
        )
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
        # new_post = {
        #     "id": len(seed_posts) + 1,
        #     "author": form.data['author'],
        #     "caption": form.data['caption'],
        #     "image": form.data['image_url'],
        #     "date": date.today(),
        #     "likes": randint(1, 7)
        # }
        # print(new_post)
        # seed_posts.append(new_post)
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
        print(form.errors)
        return render_template("post_form.html", form=form, type="update", id=id, errors=form.errors)

    else:
        current_data = Post.query.get(id)
        form.process(obj=current_data)
        return render_template("post_form.html", form=form, type="update", id=id, errors=None)


@posts.route("/delete/<int:id>")
def delete_post(id):
    post_to_delete = Post.query.get(id)
    print(post_to_delete)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect("/posts/all")