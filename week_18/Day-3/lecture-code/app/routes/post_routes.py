from flask import Blueprint, render_template, redirect
from ..posts import posts as seed_posts
from ..forms.post_form import PostForm
from datetime import date
from random import randint
from ..models import db, Post, User

posts = Blueprint("posts", __name__)
# print(__name__)


@posts.route("/all")
def view_all_posts():
    all_posts = Post.query.order_by(Post.post_date.desc()).all()
    # print(all_posts)
    # response = [post.to_dict() for post in all_posts]
    # print(response)
    # sorted_posts = sorted(seed_posts, key=lambda post: post["date"], reverse=True)
    return render_template("feed.html", posts=all_posts)
    # return response



@posts.route("/<int:id>")
def post_by_id(id):
    post = Post.query.get(id)
    print(post)
    # one_post = [post for post in seed_posts if post['id'] == id]
    # print(one_post)
    return render_template("feed.html", posts=[post])



@posts.route("/new", methods=["GET", "POST"])
def create_new_post():

    form = PostForm()
    form.author.choices = [ (user.id, user.username) for user in User.query.all()]
    # print([user.to_dict() for user in User.query.all()])
    # print(form.author.choices)

    if form.validate_on_submit():
        selected_user = User.query.get(form.data["author"])
        print(selected_user)

        new_post = Post(
            caption=form.data["caption"],
            image=form.data["image"],
            post_date=date.today(),
            user=selected_user,
        )
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/posts/all")

    if form.errors:
        print(form.errors)    
        return render_template("post_form.html", form=form, errors=form.errors )


    return render_template("post_form.html", form=form, errors=None )



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
        print(post_to_update)
        return redirect(f"/posts/{post_to_update.id}")


    elif form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, errors=form.errors, type="update", id=id )

    else:
        # Come back to here after lunch
        current_data = Post.query.get(id)
        form.process(obj=current_data)
        return render_template("post_form.html", form=form, errors=None, type="update", id=id)




@posts.route("/delete/<int:id>")
def delete_post(id):
    post_to_delete = Post.query.get(id)
    print(post_to_delete)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect("/posts/all")