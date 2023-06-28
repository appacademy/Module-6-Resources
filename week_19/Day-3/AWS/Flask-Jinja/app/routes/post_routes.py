from random import randint
from datetime import date
from flask import Blueprint, render_template, redirect, url_for
from ..forms.post_form import PostForm
from ..models import Post, User, db
from .AWS_helpers import get_unique_filename, upload_file_to_s3, remove_file_from_s3


post_routes = Blueprint("posts", __name__)

# print(__name__)

@post_routes.route("/all")
def all_posts():
  all_posts = Post.query.order_by(Post.post_date.desc()).all()
  print(all_posts)
  # response_posts = [post.to_dict() for post in all_posts]
  # print(response_posts)
  # return response_posts
  return render_template("feed.html", posts=all_posts)


@post_routes.route("/<int:id>")
def get_post_by_id(id):
    # one_post = [post for post in posts if post["id"] == id]
    # print(one_post)
    one_post = Post.query.get(id)
    print(one_post)
    return render_template("feed.html", posts=[one_post])

    
@post_routes.route("/new", methods=["GET", "POST"])
def new_post():
  form = PostForm() 
  form.user_id.choices = [ (user.id, user.username) for user in User.query.all()]

  
  if form.validate_on_submit():
    selected_user = User.query.get(form.data["user_id"])
    print(selected_user)


    image = form.data["image"]
    image.filename = get_unique_filename(image.filename)
    print(image)
    upload = upload_file_to_s3(image)
    print(upload)

    if "url" not in upload:
      return render_template("post_form.html", form=form, errors=[upload])

    new_post = Post(
      caption = form.data["caption"],
      image = upload["url"],
      user = selected_user,
      post_date = date.today(),
    )

    print(new_post)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for("posts.all_posts"))
  
  print(form.errors)
  if form.errors:
    return render_template()
  

  return render_template("post_form.html", form=form)



@post_routes.route("/update/<int:id>", methods=["GET", "POST"])
def update_post(id):
  form = PostForm()

  form.user_id.choices = [ (user.id, user.username) for user in User.query.all()]
  print(form.user_id.choices)

  if form.validate_on_submit():
    post_to_update = Post.query.get(id)

    selected_user = User.query.get(form.data["user_id"])
    post_to_update.user = selected_user
    post_to_update.caption = form.data["caption"]
    post_to_update.image = form.data["image"]
    post_to_update.post_date = date.today()
    db.session.commit()
    return redirect("/posts/all")


  elif form.errors:
    return render_template("post_form.html", form=form, errors=form.errors, type="update", id=id)


  else:
    current_data = Post.query.get(id)
    form.process(obj=current_data)
    return render_template("post_form.html", form=form, errors=None, type="update", id=id)


@post_routes.route("/delete/<int:id>")
def delete_post(id):
  post_to_delete = Post.query.get(id)

  file_delete = remove_file_from_s3(post_to_delete.image)

  if file_delete is True:
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect("/posts/all")

  else:
    return "<h1>File delete errors</h1>"