from flask import Blueprint, render_template, redirect, request 
from ..posts import posts as seed_posts
from ..forms.post_form import PostForm
from datetime import date
from random import randint
from ..models import db, Post, User
from .AWS_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3


posts = Blueprint("posts", __name__)
# print(__name__)

@posts.route("/all")
def view_all_posts():
    all_posts = Post.query.order_by(Post.post_date.desc()).all()
    response = [post.to_dict() for post in all_posts]
    print(response)
    # sorted_posts = sorted(seed_posts, key=lambda post: post["date"], reverse=True)
    # return render_template("feed.html", posts=all_posts)
    return {'posts': response }


@posts.route("/<int:id>")
def post_by_id(id):
    post = Post.query.get(id)
    print(post)
    # one_post = [post for post in seed_posts if post['id'] == id]
    # print(one_post)
    return render_template("feed.html", posts=[post], details=True)



@posts.route("/new", methods=["GET", "POST"])
def create_new_post():

    form = PostForm()
    form.author.choices = [ (user.id, user.username) for user in User.query.all()]
    
    form["csrf_token"].data = request.cookies['csrf_token'] 
    # print([user.to_dict() for user in User.query.all()])
    # print(form.author.choices)

    if form.validate_on_submit():
        selected_user = User.query.get(form.data["author"])
        print(selected_user)


        image = form.data["image"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        print(upload)

        if "url" not in upload:
            return render_template("post_form.html", form=form, errors=[upload] )


        new_post = Post(
            caption=form.data["caption"],
            image=upload['url'],
            post_date=date.today(),
            user=selected_user,
        )
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
        # return redirect("/posts/all")
        return {"resPost": new_post.to_dict()}

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

    file_to_delete = remove_file_from_s3(post_to_delete.image)

    print(post_to_delete)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect("/posts/all")